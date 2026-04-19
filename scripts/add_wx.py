import sys
import os
import requests
from bs4 import BeautifulSoup
import markdownify
import re
import subprocess
from datetime import datetime

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

def save_article(info):
    # Generate a unique filename based on timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"wx_{timestamp}"
    
    content = f"""# {info['title']}

**来源**: {info['author']}
**原文链接**: [点击前往微信阅读]({info['url']})

---

{info['markdown']}
"""
    filepath = f"docs/tools/{filename}.md"
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created {filepath}")
    return filename

def update_config(info, filename):
    config_path = "docs/.vitepress/config.mts"
    if not os.path.exists(config_path):
        print(f"Config file {config_path} not found")
        return

    with open(config_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Create a short title for sidebar
    short_title = info['title']
    if len(short_title) > 18:
        short_title = short_title[:15] + "..."

    new_item = f"{{ text: '{short_title}', link: '/tools/{filename}' }}"
    
    if '星球专栏与优选资源' in content:
        pattern = r"(text:\s*'星球专栏与优选资源.*?'.*?items:\s*\[)(.*?)(\])"
        def item_replacement(m):
            header, items, closer = m.groups()
            if new_item in items:
                return m.group(0)
            
            items_list = [i.strip() for i in items.split(',') if i.strip()]
            items_list.append(new_item)
            formatted_items = ",\n          ".join(items_list)
            return f"{header}\n          {formatted_items}\n        {closer}"
        
        new_content = re.sub(pattern, item_replacement, content, flags=re.DOTALL)
    else:
        print("Warning: '星球专栏与优选资源' not found in sidebar. Please ensure this category exists.")
        return

    with open(config_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {config_path}")

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
    filename = save_article(info)
    update_config(info, filename)
    git_push(info)
    print("Done!")
