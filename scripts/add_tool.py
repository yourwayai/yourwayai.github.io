import sys
import os
import requests
import re
import subprocess
import base64

def fetch_github_info(url):
    # Extract owner and repo from URL
    match = re.search(r'github\.com/([^/]+)/([^/]+)', url)
    if not match:
        print("Invalid GitHub URL")
        sys.exit(1)
    
    owner, repo_name = match.groups()
    repo_name = repo_name.replace('.git', '')
    
    # 1. Fetch Basic Repo Info
    api_url = f"https://api.github.com/repos/{owner}/{repo_name}"
    print(f"Fetching info for {owner}/{repo_name}...")
    
    response = requests.get(api_url)
    if response.status_code != 200:
        print(f"Failed to fetch repo data: {response.status_code}")
        sys.exit(1)
    
    repo_data = response.json()
    
    # 2. Try to fetch README content
    readme_content = ""
    readme_url = f"https://api.github.com/repos/{owner}/{repo_name}/readme"
    readme_res = requests.get(readme_url)
    if readme_res.status_code == 200:
        readme_data = readme_res.json()
        if readme_data.get('content'):
            readme_content = base64.b64decode(readme_data['content']).decode('utf-8')
    
    # Extract Features or Key Sections from README
    features = ""
    if readme_content:
        # 1. Clean up badges and common headers from the start
        content_clean = re.sub(r'(\[?!\[.*?\]\(.*?\))', '', readme_content) # Remove images/badges
        content_clean = re.sub(r'<[^>]+>', '', content_clean) # Remove raw HTML
        
        # 2. Try to find Feature-like sections (supporting emojis)
        # Regex to match headers like: ## ✨ Features, ## 🚀 Highlights, ## 💬 Support
        header_patterns = [
            r'## .*?(Features|Key Features|Core Features|Highlights|Capability|What is)(.*?)##',
            r'# .*?(Features|Key Features|Core Features|Highlights|Capability|What is)(.*?)#',
            r'## .*?(Usage|Success|About)(.*?)##'
        ]
        
        for pattern in header_patterns:
            match = re.search(pattern, content_clean, re.DOTALL | re.IGNORECASE)
            if match:
                features = match.group(2).strip()
                break
        
        # 3. Fallback: Take the first significant block of text if nothing found
        if not features:
            lines = content_clean.split('\n')
            paragraphs = []
            current_p = []
            for line in lines:
                if line.strip():
                    current_p.append(line)
                elif current_p:
                    paragraphs.append("\n".join(current_p))
                    current_p = []
            
            # Take first 2-3 non-empty paragraphs
            features = "\n\n".join([p for p in paragraphs if len(p) > 50][:3])

    # 4. Construct Image URL (GitHub Social Preview)
    # The standard URL pattern for GitHub's Open Graph images
    og_image = f"https://opengraph.githubassets.com/1/{owner}/{repo_name}"

    return {
        'name': repo_data.get('name'),
        'full_name': repo_data.get('full_name'),
        'description': repo_data.get('description', 'No description provided.'),
        'stars': repo_data.get('stargazers_count', 0),
        'language': repo_data.get('language', 'Unknown'),
        'license': repo_data.get('license', {}).get('name', 'No License') if repo_data.get('license') else 'No License',
        'url': repo_data.get('html_url'),
        'homepage': repo_data.get('homepage'),
        'og_image': og_image,
        'features': features,
        'filename': repo_name.lower()
    }

def create_markdown(info):
    homepage_section = f"* **官方主页**: [{info['homepage']}]({info['homepage']})" if info['homepage'] else ""
    
    features_section = f"\n## ✨ 核心特性\n{info['features']}" if info['features'] else ""

    content = f"""---
title: {info['name']}
description: {info['description'][:100] + ('...' if len(info['description']) > 100 else '')}
category: '👨‍💻 开发者工具'
---
# {info['name']}

![{info['name']} OpenGraph Image]({info['og_image']})

{info['description']}

* **GitHub Repo**: [{info['full_name']}]({info['url']})
* **Star 数**: ⭐ {info['stars']}
{homepage_section}
* **核心语言**: {info['language']}
* **开源协议**: {info['license']}
{features_section}
"""
    file_path = f"docs/tools/{info['filename']}.md"
    os.makedirs("docs/tools", exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created {file_path}")
    return info['filename']

def update_config(info, filename):
    config_path = 'docs/.vitepress/config.mts'
    with open(config_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_item = f"{{ text: '{info['name']}', link: '/tools/{filename}' }}"

    if '👨‍💻 开发者工具' in content:
        pattern = r"(text:\s*'👨‍💻 开发者工具.*?'.*?items:\s*\[)(.*?)(\])"
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
        sidebar_start = content.find('sidebar: [')
        if sidebar_start != -1:
            bracket_count = 0
            idx = sidebar_start + len('sidebar: [')
            while idx < len(content):
                if content[idx] == '[':
                    bracket_count += 1
                elif content[idx] == ']':
                    if bracket_count == 0:
                        insertion_point = idx
                        category = f""",
      {{
        text: '开发者生态 (Developer Ecosystem)',
        collapsed: false,
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
            return

    with open(config_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {config_path}")

def git_push(info):
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"内容优化：更新/添加工具 {info['name']} 的详尽资料与图片"], check=True)
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
    filename = create_markdown(info)
    update_config(info, filename)
    git_push(info)
    print("Done!")
