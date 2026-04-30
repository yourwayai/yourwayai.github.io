import sys
import os
import requests
import json
from bs4 import BeautifulSoup
import markdownify
import re
import subprocess
from datetime import datetime

# NVIDIA API Configuration
NV_API_KEY = "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"
NV_API_URL = "https://integrate.api.nvidia.com/v1/chat/completions"

def fetch_wechat_article(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }
    print(f"Fetching {url}...")
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch article: {e}")
        sys.exit(1)
        
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Check if we hit the anti-spider environment error
    # "当前环境异常"
    if "环境异常" in response.text and "去验证" in response.text:
        print("Error: WeChat blocked this request (Current environment is abnormal).")
        print("Please run this script from a stable residential IP or try again later.")
        sys.exit(1)
        
    # Extract Title
    title_tag = soup.find('h1', class_='rich_media_title')
    title = title_tag.text.strip() if title_tag else 'Untitled Article'
    
    # Author is often hidden, but let's try reading meta or js_name
    author_tag = soup.find('a', id='js_name')
    author = author_tag.text.strip() if author_tag else 'Unknown'
    
    # Extract Main Content
    content_div = soup.find('div', id='js_content')
    if not content_div:
        # Fallback if the DOM structure is slightly different
        content_div = soup.find('div', class_='rich_media_content')
        if not content_div:
            print("Failed to find the main content block (div#js_content).")
            sys.exit(1)

    # Process Images to bypass anti-hotlinking
    # WeChat uses data-src for real image URLs.
    imgs = content_div.find_all('img')
    for img in imgs:
        data_src = img.get('data-src')
        if data_src:
            # We use Weserv proxy
            img['src'] = f"https://images.weserv.nl/?url={data_src}"
            del img['data-src']
            
    # Remove unwanted style attributes and video placeholders to clean up the Markdown
    for tag in content_div.find_all(True):
        if tag.get('style'):
            del tag['style']
            
    # Convert to Markdown
    md_content = markdownify.markdownify(str(content_div), heading_style="ATX", strip=['script', 'style'])
    
    # Cleanup excessive newlines
    md_content = re.sub(r'\n{3,}', '\n\n', md_content)
    
    return {
        'title': title,
        'author': author,
        'url': url,
        'markdown': md_content.strip()
    }

def get_available_categories():
    config_path = 'docs/.vitepress/config.mts'
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Match text like: text: '📝 知识管理 (2)'
            # We want to capture the string before the ' ('
            matches = re.findall(r"text:\s*'([^']+?)(?:\s+\(\d+\))?'", content)
            return [m.strip() for m in matches if m.strip()]
    except Exception as e:
        print(f"Failed to read categories from config: {e}")
        return []

def categorize_article(info):
    categories = get_available_categories()
    if not categories:
        categories = ['📝 知识管理', '💬 沟通协作', '🎬 媒体与娱乐', '👨‍💻 开发者工具', '💡 微信专栏']
        
    print("Determining category and short title using NVIDIA LLM...")
    
    prompt = f"""
Analyze the following markdown content of a WeChat article.
1. Determine the most appropriate category from this exact list: {', '.join(categories)}.
   If it's an open-source project/tool, select the matching category. If unsure, default to '💡 微信专栏'.
2. Generate a highly concise sidebar title for this article in the format 'ProjectName — Subtitle'.
   - For open-source tools, use 'ToolName — Short Description' (e.g., 'Ghost — 开源博客系统').
   - For articles/columns, use 'Keyword — Short Description' (e.g., 'AI 订阅 — 支付宝付款攻略').
   - Maximum length: 15-20 characters.

Return ONLY a valid JSON object matching this schema exactly, nothing else:
{{
  "category": "the chosen category",
  "short_title": "The generated short title"
}}

Article Title: {info['title']}
Content Snippet:
{info['markdown'][:2500]}
"""

    headers = {
        "Authorization": f"Bearer {NV_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "meta/llama-3.1-70b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.1,
        "max_tokens": 100
    }
    
    try:
        res = requests.post(NV_API_URL, headers=headers, json=payload, timeout=20)
        res.raise_for_status()
        data = res.json()
        ai_response = data['choices'][0]['message']['content'].strip()
        
        # Parse JSON
        # Clean up markdown code blocks if the model added them
        if ai_response.startswith('```json'): ai_response = ai_response[7:]
        elif ai_response.startswith('```'): ai_response = ai_response[3:]
        if ai_response.endswith('```'): ai_response = ai_response[:-3]
        
        result = json.loads(ai_response.strip())
        cat = result.get('category', '💡 微信专栏')
        short_title = result.get('short_title', info['title'][:15])
        
        # Validate category
        valid_cat = cat if any(c in cat for c in categories) else '💡 微信专栏'
        print(f"AI Category Selected: {valid_cat}, Short Title: {short_title}")
        return valid_cat, short_title
    except Exception as e:
        print(f"LLM API Call Failed or Invalid JSON: {e}. Falling back to defaults.")
        
    return '💡 微信专栏', info['title'][:15]

def save_article(info, category):
    # Generate a unique filename based on timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    current_date = datetime.now().astimezone().isoformat()
    filename = f"wx_{timestamp}"
    
    content = f"""---
title: {info['title'][:50]}
description: '来自 {info['author']} 的优选资源与文章推荐'
icon: '💡'
category: '{category.replace("💡 ", "")}'
date: '{current_date}'
---
# {info['title']}

* **原文链接**: [{info['url']}]({info['url']})
* **作者**: {info['author']}

---

{info['markdown']}
"""
    file_path = f"docs/tools/{filename}.md"
    os.makedirs("docs/tools", exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created {file_path}")
    return filename

def update_config(info, filename, category, short_title):
    config_path = 'docs/.vitepress/config.mts'
    with open(config_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_item = f"{{ text: '{short_title}', link: '/tools/{filename}' }}"
    
    # We dynamically search for the exact matching category
    # E.g. category could be "👨‍💻 开发者工具"
    # We match "text: '👨‍💻 开发者工具 (5)'" taking into account the number part dynamically
    
    escaped_cat = re.escape(category)
    pattern = rf"(text:\s*'{escaped_cat}.*?'.*?items:\s*\[)(.*?)(\])"
    
    match = re.search(pattern, content, flags=re.DOTALL)
    if match:
        def item_replacement(m):
            header, items, closer = m.groups()
            if new_item in items:
                return m.group(0)
            
            items_list = [i.strip() for i in items.split(',') if i.strip()]
            items_list.append(new_item)
            formatted_items = ",\n          ".join(items_list)
            return f"{header}\n          {formatted_items}\n        {closer}"
        
        new_content = re.sub(pattern, item_replacement, content, flags=re.DOTALL)
        with open(config_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {config_path}")
    else:
        print(f"Warning: Category '{category}' not found in sidebar. Please ensure this category exists.")

def git_push(info):
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"内容集成：自动收录微信文章《{info['title']}》"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Successfully pushed to GitHub")
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/add_wx.py <wechat_url>")
        sys.exit(1)
    
    url = sys.argv[1]
    info = fetch_wechat_article(url)
    category, short_title = categorize_article(info)
    filename = save_article(info, category)
    update_config(info, filename, category, short_title)
    git_push(info)
    print("Done!")
