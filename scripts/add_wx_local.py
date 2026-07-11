import sys
import os
import re
import json
import requests
import subprocess
from bs4 import BeautifulSoup
import markdownify
from datetime import datetime

# NVIDIA API Configuration
NV_API_KEY = "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"
NV_API_URL = "https://integrate.api.nvidia.com/v1/chat/completions"

def fetch_via_curl(url):
    print(f"Fetching {url} via curl...")
    ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
    try:
        res = subprocess.run(
            ["curl", "-s", "-H", f"User-Agent: {ua}", url],
            capture_output=True,
            text=True,
            check=True
        )
        html = res.stdout
        if "环境异常" in html and "去验证" in html:
            print("Error: WeChat blocked this request (Current environment is abnormal).")
            print("Please fallback to browser scratchpad method.")
            sys.exit(1)
        return html
    except Exception as e:
        print(f"Failed to fetch via curl: {e}")
        sys.exit(1)

def parse_html_content(full_html, url):
    # Unescape escaped newlines if they were logged as '\\n'
    full_html = full_html.replace('\\\\n', '\n').replace('\\n', '\n')
    
    soup = BeautifulSoup(full_html, 'html.parser')
    
    # Extract Title
    title_tag = soup.find('h1', class_='rich_media_title')
    if not title_tag:
        title_tag = soup.find('span', class_='js_title_inner')
    title = title_tag.text.strip() if title_tag else 'Untitled Article'
    
    # Extract Author
    author_tag = soup.find('a', id='js_name')
    author = author_tag.text.strip() if author_tag else 'Unknown'
    
    # Extract Main Content
    content_div = soup.find('div', id='js_content')
    if not content_div:
        content_div = soup.find('div', class_='rich_media_content')
    
    if not content_div:
        print("Failed to find main content block (js_content / rich_media_content).")
        sys.exit(1)

    # Process Images to bypass anti-hotlinking
    imgs = content_div.find_all('img')
    for img in imgs:
        data_src = img.get('data-src')
        if data_src:
            img['src'] = f"https://images.weserv.nl/?url={data_src}"
            del img['data-src']
            
    # Remove unwanted style attributes
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

def parse_local_file(file_path, url):
    print(f"Reading from local file: {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # If the file is a markdown file with HTML chunks (scratchpad format)
    if file_path.endswith('.md'):
        chunks = re.findall(r'```html\n(.*?)\n```', content, re.DOTALL)
        if chunks:
            full_html = "".join(chunks)
        else:
            full_html = content
    else:
        full_html = content
        
    return parse_html_content(full_html, url)

def get_available_categories():
    config_path = 'docs/.vitepress/config.mts'
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            content = f.read()
            matches = re.findall(r"text:\s*'([^'()]+?)(?:\s+\(\d+\))?'", content)
            return [m.strip() for m in matches if m.strip()]
    except Exception as e:
        print(f"Failed to read categories from config: {e}")
        return []

def categorize_article(info):
    categories = get_available_categories()
    if not categories:
        categories = ['🤖 AI 与智能体', '🛠️ 系统与运维', '🔒 安全与隐私', '✍️ 知识与协作', '📂 实用与提效', '💰 金融与支付', '🎨 设计与极客', '🍿 影音与娱乐']
        
    print("Determining category, short title, and description using NVIDIA LLM...")
    
    prompt = f"""
    Analyze the following markdown content of a WeChat article.
    1. Determine the most appropriate category from this exact list: {', '.join(categories)}.
       If it's an open-source project/tool, select the matching category. If unsure, default to '💡 微信专栏'.
    2. Generate a highly concise sidebar title for this article in the format 'ProjectName — Subtitle'.
       - For open-source tools, use 'ToolName — Short Description' (e.g., 'Ghost — 开源博客系统').
       - For articles/columns, use 'Keyword — Short Description' (e.g., 'AI 订阅 — 支付宝付款攻略').
       - Maximum length: 15-20 characters.
    3. Generate a dynamic, engaging, SEO-friendly short description (50-100 characters) in Chinese summarizing the key value or content of the article.
    
    Return ONLY a valid JSON object matching this schema exactly, nothing else:
    {{
      "category": "the chosen category",
      "short_title": "The generated short title",
      "description": "The generated short description"
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
        "max_tokens": 250
    }
    
    try:
        res = requests.post(NV_API_URL, headers=headers, json=payload, timeout=20)
        res.raise_for_status()
        data = res.json()
        ai_response = data['choices'][0]['message']['content'].strip()
        
        if ai_response.startswith('```json'): ai_response = ai_response[7:]
        elif ai_response.startswith('```'): ai_response = ai_response[3:]
        if ai_response.endswith('```'): ai_response = ai_response[:-3]
        
        result = json.loads(ai_response.strip())
        cat = result.get('category', '💡 微信专栏')
        short_title = result.get('short_title', info['title'][:15])
        description = result.get('description', f"来自 {info['author']} 的优选资源与文章推荐")
        
        valid_cat = cat if any(c in cat for c in categories) else '💡 微信专栏'
        print(f"AI Category Selected: {valid_cat}, Short Title: {short_title}")
        return valid_cat, short_title, description
    except Exception as e:
        print(f"LLM API Call Failed or Invalid JSON: {e}. Falling back to defaults.")
        
    return '📂 实用与提效', info['title'][:15], f"来自 {info['author']} 的优选资源与文章推荐"

def save_article(info, category, short_title, description):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    current_date = datetime.now().astimezone().isoformat()
    filename = f"wx_{timestamp}"
    
    # Try to extract github repo URL from markdown content
    github_url = None
    github_match = re.search(r"https://github\.com/([a-zA-Z0-9_-]+)/([a-zA-Z0-9_.-]+)", info['markdown'])
    if github_match:
        owner = github_match.group(1)
        repo = github_match.group(2).replace(".git", "").strip()
        github_url = f"https://github.com/{owner}/{repo}"
        repo_name = f"{owner}/{repo}"
        
        # Clean up duplicate lines in markdown body
        lines = info['markdown'].split("\n")
        cleaned_lines = []
        for line in lines:
            stripped = line.strip()
            is_link_line = (
                "开源仓库直达" in stripped or
                "项目仓库直达" in stripped or
                "官方项目仓库" in stripped or
                "项目官方 GitHub 仓库" in stripped or
                "项目开源地址" in stripped or
                stripped.startswith("* **GitHub Repo**:") or
                stripped.startswith("* **GitHub 仓库**:") or
                stripped.startswith("* **GitHub**:")
            )
            if not is_link_line:
                cleaned_lines.append(line)
        info['markdown'] = "\n".join(cleaned_lines)

    body = info['markdown'].strip()
    if github_url:
        new_link_block = f"\n* **GitHub 仓库**: [{repo_name}]({github_url})\n"
        insert_patterns = [
            r"\n---\n\n\*\*推荐阅读[：:]?\*\*",
            r"\n👇👇👇"
        ]
        inserted = False
        for pat in insert_patterns:
            m = re.search(pat, body)
            if m:
                idx = m.start()
                body = body[:idx] + "\n" + new_link_block + body[idx:]
                inserted = True
                break
        if not inserted:
            body = body + "\n\n" + new_link_block
            
    content = f"""---
title: {info['title'][:50]}
short_title: '{short_title}'
description: '{description}'
icon: '💡'
category: '{category}'
date: '{current_date}'
---
# {info['title']}

* **原文链接**: [{info['url']}]({info['url']})
* **作者**: {info['author']}

---

{body}
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
    
    escap = re.escape(category)
    pattern = rf"(text:\s*'{escap}.*?'.*?items:\s*\[)(.*?)(\])"
    
    match = re.search(pattern, content, flags=re.DOTALL)
    if match:
        def item_replacement(m):
            header, items, closer = m.groups()
            if new_item in items:
                return m.group(0)
            
            items_list = re.findall(r'\{[^{}]*\}', items)
            if new_item not in items_list:
                items_list.append(new_item)
            formatted_items = ",\n          ".join(items_list)
            
            count_match = re.search(r'\((\d+)\)', header)
            if count_match:
                old_count = int(count_match.group(1))
                new_count = old_count + 1
                new_header = header.replace(f"({old_count})", f"({new_count})")
            else:
                new_header = header
                
            return f"{new_header}\n          {formatted_items}\n        {closer}"
        
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
        print("Usage: python3 scripts/add_wx_local.py <wechat_url_or_scratchpad_path> [wechat_url]")
        sys.exit(1)
        
    arg1 = sys.argv[1]
    if arg1.startswith("http://") or arg1.startswith("https://"):
        url = arg1
        html = fetch_via_curl(url)
        info = parse_html_content(html, url)
    else:
        file_path = arg1
        if len(sys.argv) < 3:
            print("Usage for file parsing: python3 scripts/add_wx_local.py <scratchpad_path> <wechat_url>")
            sys.exit(1)
        url = sys.argv[2]
        info = parse_local_file(file_path, url)
        
    category, short_title, description = categorize_article(info)
    filename = save_article(info, category, short_title, description)
    update_config(info, filename, category, short_title)
    git_push(info)
    
    # Run sitemap build
    subprocess.run(["npm", "run", "build:sitemap"], check=True)
    print("Done!")
