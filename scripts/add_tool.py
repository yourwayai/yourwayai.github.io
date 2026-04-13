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
    
    # Try to find '自动化收录' category
    if '自动化收录' in content:
        # Append to existing category
        # Look for items: [ ... ] within the '自动化收录' section
        pattern = r"(text:\s*'自动化收录'.*?items:\s*\[)(.*?)(\])"
        def item_replacement(m):
            header, items, closer = m.groups()
            if new_item in items:
                return m.group(0) # Already exists
            
            items_list = items.strip().split(',')
            items_list = [i.strip() for i in items_list if i.strip()]
            items_list.append(new_item)
            
            formatted_items = ",\n          ".join(items_list)
            return f"{header}\n          {formatted_items}\n        {closer}"
        
        new_content = re.sub(pattern, item_replacement, content, flags=re.DOTALL)
    else:
        # Add new category to the end of the sidebar array
        # Find the sidebar array: sidebar: [ ... ]
        pattern = r"(sidebar:\s*\[)(.*?)(\]\s*,?\s*//?\s*右上角|sidebar:\s*\[)(.*?)(\]\s*\n\s*\})"
        # Simpler: find the last ']' before the next major section or end of themeConfig
        # We know our sidebar ends with a ']' followed by some whitespace and ']' (for themeConfig) or similar.
        
        # Let's use a non-regex approach for finding the insertion point if regex is too hard
        sidebar_start = content.find('sidebar: [')
        if sidebar_start != -1:
            # Find the match for the sidebar's closing bracket
            bracket_count = 0
            idx = sidebar_start + len('sidebar: [')
            while idx < len(content):
                if content[idx] == '[':
                    bracket_count += 1
                elif content[idx] == ']':
                    if bracket_count == 0:
                        # Found the closing bracket of the sidebar array
                        insertion_point = idx
                        category = f""",
      {{
        text: '自动化收录',
        items: [
          {new_item}
        ]
      }}"""
                        new_content = content[:insertion_point].rstrip() + category + content[insertion_point:]
                        break
                    else:
                        bracket_count -= 1
                idx += 1
        else:
            print("Could not find sidebar in config.mts")
            return

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
