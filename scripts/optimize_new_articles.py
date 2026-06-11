import os
import re

MAPPING = {
    "wx_20260611153942.md": "nvidia/skills",
    "wx_20260611154651.md": "iOfficeAI/OfficeCLI",
    "wx_20260611154756.md": "anthropics/skills",
    "wx_20260611154932.md": "twentyhq/twenty",
    "wx_20260611155218.md": "Panniantong/Agent-Reach",
    "wx_20260611155310.md": "martinvonz/jj"
}

STATIC_DATA = {
    "nvidia/skills": {
        "stars": "1.2k",
        "forks": "144",
        "license": "Apache-2.0",
        "version": "N/A",
        "pushed_at": "2026-06-11T05:39:30Z",
        "contributors": "43",
        "owner_name": "NVIDIA",
        "platforms": ["Linux", "macOS", "Windows"],
        "deployments": ["npx", "Command Line"]
    },
    "iOfficeAI/OfficeCLI": {
        "stars": "6.8k",
        "forks": "517",
        "license": "Apache-2.0",
        "version": "v1.0.110",
        "pushed_at": "2026-06-11T08:29:22Z",
        "contributors": "9",
        "owner_name": "iOfficeAI",
        "platforms": ["Linux", "macOS", "Windows"],
        "deployments": ["Binary", "Command Line"]
    },
    "anthropics/skills": {
        "stars": "149.2k",
        "forks": "17.6k",
        "license": "N/A",
        "version": "N/A",
        "pushed_at": "2026-06-09T20:35:19Z",
        "contributors": "14",
        "owner_name": "anthropics",
        "platforms": ["Linux", "macOS", "Windows"],
        "deployments": ["CLI", "plugins"]
    },
    "twentyhq/twenty": {
        "stars": "49.7k",
        "forks": "7.2k",
        "license": "AGPL-3.0",
        "version": "v2.11.0",
        "pushed_at": "2026-06-11T08:52:55Z",
        "contributors": "462",
        "owner_name": "twentyhq",
        "platforms": ["Linux", "macOS", "Windows"],
        "deployments": ["npx", "Docker Compose", "Docker"]
    },
    "Panniantong/Agent-Reach": {
        "stars": "26.2k",
        "forks": "2.2k",
        "license": "MIT",
        "version": "v1.4.2",
        "pushed_at": "2026-06-11T08:30:58Z",
        "contributors": "30",
        "owner_name": "Panniantong",
        "platforms": ["Linux", "macOS", "Windows"],
        "deployments": ["pip", "Python"]
    },
    "martinvonz/jj": {
        "stars": "29.6k",
        "forks": "1.1k",
        "license": "Apache-2.0",
        "version": "v0.42.0",
        "pushed_at": "2026-06-11T05:42:46Z",
        "contributors": "342",
        "owner_name": "jj-vcs",
        "platforms": ["Linux", "macOS", "Windows"],
        "deployments": ["cargo", "brew", "Binary"]
    }
}

def main():
    tools_dir = "docs/tools"
    
    for filename, repo in MAPPING.items():
        filepath = os.path.join(tools_dir, filename)
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}, skipping.")
            continue
            
        print(f"\nProcessing {filename} (Repo: {repo})")
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # 1. Fetch live/static GitHub stats
        stats = STATIC_DATA.get(repo)
        if not stats:
            print(f"No static data for repo {repo}, skipping.")
            continue
            
        # 2. Parse frontmatter
        fm_match = re.match(r"^---\r?\n([\s\S]*?)\r?\n---", content)
        if not fm_match:
            print(f"No frontmatter found in {filename}, skipping.")
            continue
        fm_block = fm_match.group(1)
        
        # 3. Modify Frontmatter: set icon to owner's avatar URL, set stars
        avatar_url = f"https://github.com/{stats['owner_name']}.png"
        
        # Replace or add icon in frontmatter
        old_icon_match = re.search(r"icon:\s*'([^']+)'", fm_block)
        if not old_icon_match:
            old_icon_match = re.search(r'icon:\s*"([^"]+)"', fm_block)
        
        if old_icon_match:
            old_icon_line = old_icon_match.group(0)
            new_icon_line = f"icon: '{avatar_url}'"
            new_fm_block = fm_block.replace(old_icon_line, new_icon_line)
        else:
            new_fm_block = fm_block + f"\nicon: '{avatar_url}'"
            
        # Replace or add stars in frontmatter
        stars_line = f"stars: '{stats['stars']}'"
        if "stars:" in new_fm_block:
            new_fm_block = re.sub(r"stars:\s*'[^']+'", stars_line, new_fm_block)
            new_fm_block = re.sub(r'stars:\s*"[^"]+"', stars_line, new_fm_block)
        else:
            new_fm_block = new_fm_block.rstrip() + f"\n{stars_line}"
            
        # Reconstruct content with updated frontmatter
        content = content[:fm_match.start(1)] + new_fm_block + content[fm_match.end(1):]
        
        # 4. Check if GithubRepoCard is already in the page
        if "<GithubRepoCard" in content:
            print(f"GithubRepoCard already exists in {filename}, skipping insertion.")
            continue
            
        # 5. Insert GithubRepoCard right before "**推荐阅读**" or at the end
        platforms_str = str(stats.get('platforms', ['Linux', 'macOS', 'Windows']))
        deployments_str = str(stats.get('deployments', ['Source Code']))
        
        # Format pushed_at to just YYYY-MM-DD
        pushed_date = stats['pushed_at'].split('T')[0]
        
        card_block = f"""<GithubRepoCard 
  repo="{repo}"
  initialStars="{stats['stars']}"
  initialForks="{stats['forks']}"
  initialContributors="{stats['contributors']}"
  initialVersion="{stats['version']}"
  initialPushedAt="{pushed_date}"
  :platforms="{platforms_str}"
  :deployments="{deployments_str}"
/>\n\n"""
        
        # Locate insertion index
        insert_match = re.search(r"\r?\n\s*\*\*推荐阅读[：:]?\*\*", content)
        if insert_match:
            idx = insert_match.start()
            content = content[:idx] + "\n" + card_block + content[idx:]
            print(f"Inserted GithubRepoCard in {filename}")
        else:
            content = content.rstrip() + "\n\n" + card_block
            print(f"Appended GithubRepoCard to the end of {filename}")
            
        # Write back file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        
    print("Optimization completed!")

if __name__ == "__main__":
    main()
