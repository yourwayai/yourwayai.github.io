import sys
import os
import requests
import re
import subprocess

def fetch_github_info(url):
    # Extract owner and repo from URL
    match = re.search(r'github\.com/([^/]+)/([^/]+)', url)
    if not match:
        print("Invalid GitHub URL")
        sys.exit(1)
    
    owner, repo = match.groups()
    repo = repo.replace('.git', '')
    
    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    print(f"Fetching info for {owner}/{repo}...")
    
    response = requests.get(api_url)
    if response.status_code != 200:
        print(f"Failed to fetch data: {response.status_code}")
        sys.exit(1)
    
    data = response.json()
    return {
        'name': data.get('name'),
        'description': data.get('description', 'No description provided.'),
        'stars': data.get('stargazers_count', 0),
        'url': data.get('html_url'),
        'filename': repo.lower()
    }

def create_markdown(info):
    content = f"""# {info['name']}

{info['description']}

## 🌟 项目信息
* **GitHub**: [{info['url']}]({info['url']})
* **星标数**: ⭐ {info['stars']}
* **类型**: 开源项目

## 🚀 简介
该项目是 GitHub 上的优质开源资源，由社区共同维护。

## 📥 访问与了解
您可以访问 [GitHub 仓库]({info['url']}) 获取更多详细文档和源代码。
"""
    filepath = f"docs/tools/{info['filename']}.md"
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created {filepath}")
    return filepath

def update_config(info):
    config_path = "docs/.vitepress/config.mts"
    if not os.path.exists(config_path):
        print(f"Config file {config_path} not found")
        return

    with open(config_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the new item
    new_item = f"{{ text: '{info['name']}', link: '/tools/{info['filename']}' }}"
    
    # Try to find '自动化收录' category, or create it
    if '自动化收录' in content:
        # Append to existing category
        pattern = r"(text:\s*'自动化收录'.*?items:\s*\[)(.*?)(\])"
        def replacement(m):
            header, items, closer = m.groups()
            if new_item in items:
                return m.group(0) # Already exists
            separator = ", " if items.strip() else ""
            return f"{header}{items}{separator}{new_item}{closer}"
        
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    else:
        # Add new category to sidebar
        # We'll look for the end of the sidebar array
        pattern = r"(sidebar:\s*\[)(.*?)(\],)"
        category = f"""
      {{
        text: '自动化收录',
        items: [
          {new_item}
        ]
      }},"""
        def replacement(m):
            start, mid, end = m.groups()
            return f"{start}{mid}{category}{end}"
        
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open(config_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {config_path}")

def git_push(info):
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"自动添加工具: {info['name']}"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Successfully pushed to GitHub")
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/add_tool.py <github_url>")
        sys.exit(1)
    
    url = sys.argv[1]
    info = fetch_github_info(url)
    create_markdown(info)
    update_config(info)
    git_push(info)
    print("Done!")
