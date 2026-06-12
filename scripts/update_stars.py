#!/usr/bin/env python3
"""
update_stars.py — 自动从 GitHub API 拉取最新 star 数并写回 docs/tools/*.md 的 frontmatter

用法:
    python3 scripts/update_stars.py

可选环境变量:
    GITHUB_TOKEN — 设置后可使用已认证请求 (5000次/小时)，否则仅有 60次/小时
    DRY_RUN=1   — 仅预览改动，不写入文件
"""

import os
import re
import sys
import json
import time
import urllib.request
import urllib.error
from pathlib import Path
from typing import Optional, Tuple

# ────────────────────────── 配置 ──────────────────────────
TOOLS_DIR = Path(__file__).parent.parent / "docs" / "tools"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
DRY_RUN = os.environ.get("DRY_RUN", "0") == "1"

# 跳过非技术工具（金融/支付类文章，无 GitHub 仓库）
SKIP_FILES = {"wx_20260419212801.md", "wx_20260419212858.md", "wx_20260421112236.md"}

# GitHub 仓库 URL 正则（捕获 owner/repo）
GITHUB_REPO_PATTERN = re.compile(
    r"https://github\.com/([a-zA-Z0-9_.-]+)/([a-zA-Z0-9_.-]+)"
)

# frontmatter stars 字段正则
STARS_FM_PATTERN = re.compile(r"^(stars:\s*)(.+)$", re.MULTILINE)


# ────────────────────────── 工具函数 ──────────────────────────
def format_stars(count: int) -> str:
    """将 star 数格式化为人类可读的缩写字符串"""
    if count >= 1_000_000:
        return f"{count / 1_000_000:.1f}M"
    if count >= 1_000:
        return f"{count / 1_000:.1f}k"
    return str(count)


def fetch_github_stars(owner: str, repo: str) -> Optional[int]:
    """通过 GitHub API 获取仓库的 star 数，失败返回 None"""
    # 清理 repo 名称（去掉末尾的 .git 和特殊字符）
    repo = repo.rstrip("/").split("#")[0].split("?")[0]
    repo = repo.rstrip(".git") if repo.endswith(".git") else repo

    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "yourwayai-stars-updater/1.0",
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            remaining = int(resp.headers.get("X-RateLimit-Remaining", -1))
            if remaining != -1 and remaining < 10:
                print(f"  ⚠️  GitHub API 剩余次数不足: {remaining}/hour，稍候再试")
            return data.get("stargazers_count")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"  ⚠️  仓库不存在: {owner}/{repo}")
        elif e.code == 403:
            print(f"  ⛔ API 速率限制，请稍后再试或设置 GITHUB_TOKEN")
        else:
            print(f"  ❌ HTTP {e.code}: {owner}/{repo}")
        return None
    except Exception as e:
        print(f"  ❌ 请求失败 ({owner}/{repo}): {e}")
        return None


def extract_first_github_repo(content: str) -> Optional[Tuple[str, str]]:
    """从文件内容中提取第一个 GitHub 仓库（owner, repo），自动跳过代码块中的链接"""
    # 去除 fenced 代码块（``` ... ``` 或 ~~~ ... ~~~），避免误读示例代码中的占位 URL
    code_block_pattern = re.compile(r"```[\s\S]*?```|~~~[\s\S]*?~~~", re.MULTILINE)
    clean_content = code_block_pattern.sub("", content)

    # 也尝试从 GithubRepoCard 的 repo= 属性直接提取（最精确）
    repo_card_match = re.search(r'repo=["\']([a-zA-Z0-9_.-]+)/([a-zA-Z0-9_.-]+)["\']', clean_content)
    if repo_card_match:
        return repo_card_match.group(1), repo_card_match.group(2)

    matches = GITHUB_REPO_PATTERN.findall(clean_content)
    for owner, repo in matches:
        # 跳过 GitHub 头像和已知非项目链接
        if "github.com" in repo or "githubusercontent" in owner:
            continue
        # 跳过明显不是仓库的链接（如 github.com/orgs, github.com/users 等）
        if owner in ("orgs", "users", "topics", "collections", "sponsors", "apps"):
            continue
        # 清理 repo 名称
        clean_repo = repo.split("/")[0].split(".")[0] if "/" in repo or "." in repo else repo
        # 去除 markdown 链接括号污染
        clean_repo = re.sub(r"[)\]\"'>].*", "", clean_repo)
        if clean_repo:
            return owner, clean_repo
    return None


def update_stars_in_content(content: str, new_stars_str: str) -> Tuple[str, bool]:
    """
    替换 frontmatter 中的 stars 字段。
    返回 (新内容, 是否已修改)
    """
    # 确保只在 frontmatter 区域内操作
    fm_match = re.match(r"^---\r?\n([\s\S]*?)\r?\n---", content)
    if not fm_match:
        return content, False

    fm_text = fm_match.group(1)
    stars_match = STARS_FM_PATTERN.search(fm_text)

    if stars_match:
        old_val = stars_match.group(2).strip().strip("'\"")
        if old_val == new_stars_str:
            return content, False  # 无需更新
        new_fm_text = STARS_FM_PATTERN.sub(
            lambda m: f"{m.group(1)}'{new_stars_str}'", fm_text
        )
        new_content = content.replace(fm_text, new_fm_text, 1)
        return new_content, True
    else:
        # frontmatter 中没有 stars 字段，在最后一行 key 前插入
        new_fm_lines = fm_text.rstrip() + f"\nstars: '{new_stars_str}'"
        new_content = content.replace(fm_text, new_fm_lines, 1)
        return new_content, True


# ────────────────────────── 主程序 ──────────────────────────
def main():
    md_files = sorted(TOOLS_DIR.glob("*.md"))
    total = len(md_files)
    updated = 0
    skipped_no_repo = 0
    skipped_api_fail = 0
    skipped_no_change = 0

    print(f"🔍 扫描 {total} 个工具文档 ({'DRY RUN 预览模式' if DRY_RUN else '写入模式'})")
    if GITHUB_TOKEN:
        print("🔑 已检测到 GITHUB_TOKEN，使用已认证请求 (上限 5000次/小时)")
    else:
        print("⚠️  未设置 GITHUB_TOKEN，使用匿名请求 (上限 60次/小时)")
    print("─" * 60)

    for idx, md_path in enumerate(md_files, 1):
        filename = md_path.name

        if filename in SKIP_FILES:
            print(f"[{idx:02}/{total}] ⏭  跳过 (非技术工具): {filename}")
            skipped_no_repo += 1
            continue

        content = md_path.read_text(encoding="utf-8")
        repo_info = extract_first_github_repo(content)

        if not repo_info:
            print(f"[{idx:02}/{total}] ⏭  无 GitHub 仓库: {filename}")
            skipped_no_repo += 1
            continue

        owner, repo = repo_info
        print(f"[{idx:02}/{total}] 📡 {filename} → {owner}/{repo} ...", end=" ", flush=True)

        stars_count = fetch_github_stars(owner, repo)
        if stars_count is None:
            print("❌ 获取失败")
            skipped_api_fail += 1
            # 避免速率限制，失败后等待一秒
            time.sleep(1)
            continue

        stars_str = format_stars(stars_count)
        new_content, changed = update_stars_in_content(content, stars_str)

        if not changed:
            print(f"✅ 无变化 ({stars_str})")
            skipped_no_change += 1
        elif DRY_RUN:
            print(f"🔎 预览更新 → stars: '{stars_str}'")
            updated += 1
        else:
            md_path.write_text(new_content, encoding="utf-8")
            print(f"⭐ 已更新 → stars: '{stars_str}'")
            updated += 1

        # 礼貌性延迟，避免触发 API 速率限制
        time.sleep(0.5)

    print("─" * 60)
    print(f"📊 完成！更新: {updated}  无仓库/跳过: {skipped_no_repo}  无变化: {skipped_no_change}  API 失败: {skipped_api_fail}")


if __name__ == "__main__":
    main()
