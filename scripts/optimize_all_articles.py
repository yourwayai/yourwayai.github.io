import os
import re
import requests
import time

ALL_MAPPINGS = {
    "2fauth.md": "Bubka/2FAuth",
    "3x-ui.md": "MHSanaei/3x-ui",
    "beszel.md": "henrygd/beszel",
    "chatwoot.md": "chatwoot/chatwoot",
    "cookcli.md": "cooklang/cookcli",
    "fluentflyout.md": "unchihugo/FluentFlyout",
    "goose.md": "aaif-goose/goose",
    "hermes-agent.md": "NousResearch/hermes-agent",
    "jellyfin.md": "jellyfin/jellyfin",
    "memos.md": "usememos/memos",
    "outline.md": "outlinewiki/outline",
    "penpot.md": "penpot/penpot",
    "rsshub.md": "DIYgod/RSSHub",
    "stirling-pdf.md": "Stirling-Tools/Stirling-PDF",
    "storybook.md": "storybookjs/storybook",
    "the-art-of-command-line.md": "jlevy/the-art-of-command-line",
    "v8.md": "v8/v8",
    "wx_20260429211232.md": "c4illin/convertx",
    "wx_20260511214354.md": "prometheus/prometheus",
    "wx_20260511215131.md": "localsend/localsend",
    "wx_20260511215328.md": "raullenchai/Rapid-MLX",
    "wx_20260518005642.md": "moeru-ai/airi",
    "wx_20260518005748.md": "fcitx5-android/fcitx5-android",
    "wx_20260518005849.md": "shiyu-coder/Kronos",
    "wx_20260524213111.md": "AlexsJones/llmfit",
    "wx_20260524213854.md": "HKUDS/CLI-Anything",
    "wx_20260524214020.md": "supertone-inc/supertonic",
    "wx_20260524214529.md": "anthropics/financial-services-plugins",
    "wx_20260524214734.md": "bytedance/UI-TARS-desktop",
    "wx_20260524214934.md": "ItzCrazyKns/Vane",
    "wx_20260530171127.md": "perplexityai/bumblebee",
    "wx_20260530171254.md": "debpalash/OmniVoice-Studio",
    "wx_20260530171455.md": "orailnoor/DroidDesk",
    "wx_20260530171544.md": "himomohi/AirTranslate",
    "wx_20260530171623.md": "TeamDev-IP/MoBrowser-App-Icon-Maker",
    "wx_20260530171710.md": "itsfatduck/optimizerDuck",
    "wx_20260605172228.md": "DayuanJiang/next-ai-draw-io",
    "wx_20260605172524.md": "OpenBMB/VoxCPM",
    "wx_20260605173109.md": "cloudflare/agentic-inbox",
    "wx_20260605173551.md": "TurixAI/TuriX-CUA",
    "wx_20260605173728.md": "OpenBMB/PilotDeck",
    
    # 5 missing mapped repos
    "wx_20260421130229.md": "TryGhost/Ghost",
    "wx_20260511214626.md": "InvoiceShelf/InvoiceShelf",
    "wx_20260511214924.md": "dani-garcia/vaultwarden",
    "wx_20260518005305.md": "cosmicstack-labs/mercury-agent",
    "wx_20260518005533.md": "Forget-C/Jellyfish",
    
    # 2 corrected repos
    "wx_20260413125458.md": "ComposioHQ/open-chatgpt-atlas",
    "wx_20260518003237.md": "msitarzewski/agency-agents"
}

def format_number(num):
    try:
        num = int(num)
        if num >= 1000000:
            return f"{num/1000000:.1f}M"
        elif num >= 1000:
            return f"{num/1000:.1f}k"
        return str(num)
    except:
        return str(num)

def format_local_stars(stars_str):
    if not stars_str or stars_str == "N/A":
        return "N/A"
    stars_str = stars_str.lower()
    if 'k' in stars_str or 'm' in stars_str:
        return stars_str
    try:
        val = float(stars_str)
        if val >= 1000:
            return f"{val/1000:.1f}k"
        return str(int(val))
    except:
        return stars_str

def parse_local_fallbacks(content):
    stars = "N/A"
    license_val = "N/A"
    
    # Try to find: * **Star 数**: ⭐ 3,900+
    star_match = re.search(r"Star\s*数[：:]\s*⭐\s*([0-9.,k+M]+)", content, re.IGNORECASE)
    if star_match:
        val = star_match.group(1).replace(",", "").replace("+", "").strip()
        stars = val
        
    # Try to find: * **开源协议**: AGPL v3.0
    lic_match = re.search(r"开源协议[：:]\s*([A-Za-z0-9. -/]+)", content)
    if lic_match:
        license_val = lic_match.group(1).strip()
        
    return format_local_stars(stars), license_val

def fetch_github_data(repo, local_stars, local_license):
    print(f"Fetching GitHub data for {repo}...")
    headers = {'Accept': 'application/vnd.github.v3+json'}
    repo_url = f'https://api.github.com/repos/{repo}'
    try:
        # Polite sleep to avoid hitting rate limits too fast
        time.sleep(0.5)
        res = requests.get(repo_url, headers=headers, timeout=10)
        if res.status_code == 200:
            data = res.json()
            return {
                "stars": format_number(data.get("stargazers_count")),
                "forks": format_number(data.get("forks_count")),
                "license": data.get("license", {}).get("spdx_id", local_license) if data.get("license") else local_license,
                "version": "N/A",
                "pushed_at": data.get("pushed_at", "2026-06-11"),
                "contributors": "N/A",
                "owner_name": data.get("owner", {}).get("login", repo.split('/')[0])
            }
        else:
            print(f"  GitHub API returned {res.status_code} for {repo}. Using fallbacks.")
    except Exception as e:
        print(f"  Network error fetching {repo}: {e}. Using fallbacks.")
        
    return {
        "stars": local_stars,
        "forks": "N/A",
        "license": local_license,
        "version": "N/A",
        "pushed_at": "2026-06-11T00:00:00Z",
        "contributors": "N/A",
        "owner_name": repo.split('/')[0]
    }

def process_content(content, card_block):
    # Case 1: Replace plain GitHub link if it exists
    github_link_pattern = re.compile(
        r"\r?\n\s*\*\s*\*\*(?:GitHub|Github|github)\s+仓库\*\*:\s*(?:\[[^\]]+\]\(https://github\.com/[^)]+\)|https://github\.com/[^\s\n]+)",
        re.IGNORECASE
    )
    if github_link_pattern.search(content):
        content = github_link_pattern.sub("\n\n" + card_block, content)
        return content
        
    # Case 2: Insert before **推荐阅读**
    rec_pattern = re.compile(r"\r?\n\s*\*\*推荐阅读[：:]?\*\*", re.IGNORECASE)
    match = rec_pattern.search(content)
    if match:
        idx = match.start()
        content = content[:idx] + "\n" + card_block + content[idx:]
        return content
        
    # Case 3: Default append to the end
    content = content.rstrip() + "\n\n" + card_block
    return content

def main():
    tools_dir = "docs/tools"
    success_count = 0
    
    for filename, repo in ALL_MAPPINGS.items():
        filepath = os.path.join(tools_dir, filename)
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}, skipping.")
            continue
            
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        if "<GithubRepoCard" in content:
            print(f"GithubRepoCard already exists in {filename}, skipping.")
            continue
            
        print(f"\nProcessing {filename} (Repo: {repo})")
        
        # 1. Parse local fallbacks from content
        local_stars, local_license = parse_local_fallbacks(content)
        
        # 2. Fetch data (API with fallback)
        stats = fetch_github_data(repo, local_stars, local_license)
        
        # 3. Parse frontmatter
        fm_match = re.match(r"^---\r?\n([\s\S]*?)\r?\n---", content)
        if not fm_match:
            print(f"No frontmatter found in {filename}, skipping.")
            continue
        fm_block = fm_match.group(1)
        
        # 4. Modify Frontmatter: set icon to owner's avatar URL, set stars
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
        
        # 5. Insert card block
        pushed_date = stats['pushed_at'].split('T')[0]
        platforms_str = "['Linux', 'macOS', 'Windows']" # Standard default
        deployments_str = "['Docker', 'Source Code']" # Standard default
        
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
        
        content = process_content(content, card_block)
        
        # Write back file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        success_count += 1
        
    print(f"\nOptimization completed! Processed {success_count} files.")

if __name__ == "__main__":
    main()
