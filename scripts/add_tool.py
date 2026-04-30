import sys
import os
import requests
import re
import subprocess
import base64
import json

# NVIDIA API Configuration
NV_API_KEY = "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"
NV_API_URL = "https://integrate.api.nvidia.com/v1/chat/completions"

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
            readme_content = base64.b64decode(readme_data['content']).decode('utf-8', errors='ignore')
    
    # Clean up readme content slightly to save tokens
    readme_clean = re.sub(r'<img[^>]*>', '', readme_content)
    readme_clean = re.sub(r'\[!\[.*?\]\(.*?\)\]\(.*?\)', '', readme_clean)

    # 4. Construct Image URL (GitHub Social Preview)
    og_image = f"https://opengraph.githubassets.com/1/{owner}/{repo_name}"

    return {
        'name': repo_data.get('name'),
        'full_name': repo_data.get('full_name'),
        'description': repo_data.get('description', 'No description provided.'),
        'stars': repo_data.get('stargazers_count', 0),
        'language': repo_data.get('language', 'Unknown'),
        'license': repo_data.get('license', {}).get('name', 'No License') if repo_data.get('license') else 'No License',
        'url': repo_data.get('html_url'),
        'homepage': repo_data.get('homepage') or repo_data.get('html_url'),
        'og_image': og_image,
        'readme_content': readme_clean,
        'filename': repo_name.lower(),
        'current_date': __import__('datetime').datetime.now().astimezone().isoformat()
    }

def generate_rich_markdown(info):
    print("Generating enriched markdown content using NVIDIA LLM...")
    
    prompt = f"""
You are an expert technical writer and developer advocate. I will provide you with the metadata and README content of a GitHub open-source project. 
Your task is to write a comprehensive, highly readable Chinese documentation page for this project, following a specific structure and using a highly professional and engaging tone.

Project Name: {info['name']}
Description: {info['description']}
Stars: {info['stars']}
Language: {info['language']}
License: {info['license']}
URL: {info['url']}
Homepage: {info['homepage']}
OpenGraph Image: {info['og_image']}

README Content (truncated):
{info['readme_content'][:15000]}

Please format your response EXACTLY as follows (in Markdown), keeping the frontmatter exactly as specified:

---
title: {info['name']}
description: [Write a catchy one-line description/pain point in Chinese, max 50 chars]
category: '👨‍💻 开发者工具'
date: '{info['current_date']}'
---
# {info['name']}：[Write a catchy subtitle]


![{info['name']} OpenGraph Image]({info['og_image']})

[Write 1-2 paragraphs of highly polished Chinese introduction summarizing the project's main value proposition. Make it sound premium and professional.]

* **GitHub Repo**: [{info['full_name']}]({info['url']})
* **Star 数**: ⭐ {info['stars']}
* **官方主页**: [{info['homepage']}]({info['homepage']})
* **核心语言**: {info['language']}
* **开源协议**: {info['license']}

---

## ✨ 核心特性

[Extract and rewrite the core features from the README into a structured, well-formatted list or sub-sections in Chinese. Be detailed, professional, and use emojis where appropriate.]

---

## 🚀 快速部署 / 安装

[Provide the installation or Docker deployment commands if found in the README. If not, provide a link to the official docs for installation. Format code blocks properly.]

---

## 💻 使用示例 (Optional)

[Provide a code snippet or usage example if available in the README. If not, omit this section.]

---

## 💡 适用场景与总结

[Conclude with the target audience and best use cases for this tool.]

Important Instructions:
1. Return ONLY the raw markdown content.
2. Do NOT wrap it in ```markdown ... ``` tags.
3. Ensure the Chinese translation is natural, technical, and accurate.
4. Keep the exact YAML frontmatter block at the very top.
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
        "temperature": 0.2,
        "max_tokens": 2048
    }
    
    try:
        res = requests.post(NV_API_URL, headers=headers, json=payload, timeout=60)
        res.raise_for_status()
        data = res.json()
        ai_response = data['choices'][0]['message']['content'].strip()
        
        # Sometimes models still wrap the whole thing in markdown blocks despite instructions
        if ai_response.startswith('```markdown'):
            ai_response = ai_response[11:]
        if ai_response.startswith('```'):
            ai_response = ai_response[3:]
        if ai_response.endswith('```'):
            ai_response = ai_response[:-3]
            
        return ai_response.strip()
    except Exception as e:
        print(f"LLM API Call Failed: {e}. Generating fallback markdown.")
        # Fallback to basic structure if API fails
        return f"""---
title: {info['name']}
description: {info['description'][:50]}
category: '👨‍💻 开发者工具'
---
# {info['name']}

![{info['name']} OpenGraph Image]({info['og_image']})

{info['description']}

* **GitHub Repo**: [{info['full_name']}]({info['url']})
* **Star 数**: ⭐ {info['stars']}
* **官方主页**: [{info['homepage']}]({info['homepage']})
* **核心语言**: {info['language']}
* **开源协议**: {info['license']}
"""

def create_markdown(info):
    content = generate_rich_markdown(info)
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
