import os
import subprocess
import re
import glob

def get_git_date(filepath):
    try:
        # Get the first commit date
        result = subprocess.run(
            ["git", "log", "--diff-filter=A", "--format=%aI", "-1", "--", filepath],
            capture_output=True, text=True, check=True
        )
        date_str = result.stdout.strip()
        if not date_str:
            # Fallback to file creation/modification time if not in git
            import datetime
            stat = os.stat(filepath)
            date_str = datetime.datetime.fromtimestamp(stat.st_mtime).isoformat()
        return date_str
    except subprocess.CalledProcessError:
        return "2026-04-30T00:00:00+00:00"

def add_date_to_frontmatter(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if date already exists
    if re.search(r'^date:\s*', content, re.MULTILINE):
        return

    date_str = get_git_date(filepath)
    
    # Insert date after title or description
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = parts[1]
            if "date:" not in frontmatter:
                # Add date
                new_frontmatter = frontmatter.rstrip() + f"\ndate: '{date_str}'\n"
                new_content = f"---{new_frontmatter}---{parts[2]}"
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Added date {date_str} to {filepath}")

if __name__ == "__main__":
    files = glob.glob("docs/tools/*.md")
    for f in files:
        add_date_to_frontmatter(f)
