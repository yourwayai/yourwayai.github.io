# YourwayAI — 添加新项目标准操作流程（SOP）

> 本文件由 Antigravity AI 整理，记录了向 YourwayAI 网站添加新内容的完整标准流程。  
> 路径：`/Users/milong/Antigravity/yourwayAI/`

---

## 📋 概述

YourwayAI 是一个 VitePress 静态文档站点，托管于 GitHub Pages。新项目通过以下两种路径添加：

| 路径 | 来源 | 适用场景 |
|------|------|----------|
| **路径 A** — `add_wx_local.py` | 微信公众号文章 URL | 收录已有文章，内容直接提取 |
| **路径 B** — `add_tool.py` | GitHub 仓库 URL | 从仓库 README 自动生成介绍页 |

---

## 🅰️ 路径 A：微信文章 → 新项目

### 第一步：运行自动化脚本（一键完成）

```bash
# 在项目根目录执行
python3 scripts/add_wx_local.py <微信文章URL>

# 示例
python3 scripts/add_wx_local.py https://mp.weixin.qq.com/s/XXXXXXXXXXXXXXXX
```

或使用 npm 脚本：

```bash
npm run add-wx-local -- https://mp.weixin.qq.com/s/XXXXXXXXXXXXXXXX
```

**脚本自动完成以下所有步骤：**
1. 用 `curl` + iPhone UA 绕过微信反爬，抓取 HTML
2. 用 BeautifulSoup 解析标题、作者、正文，转为 Markdown
3. 调用 NVIDIA LLM API（meta/llama-3.1-70b-instruct）生成分类、短标题、描述
4. 创建 `docs/tools/wx_YYYYMMDDHHMMSS.md` 文件
5. 更新 `docs/.vitepress/config.mts` 侧边栏（自动增加计数）
6. `git add . && git commit && git push`
7. 运行 `npm run build:sitemap` 更新 sitemap 和 projects.md

---

### 第二步：补全 GitHub 仓库卡片（手动，约 2 分钟）

> 脚本会自动检测文章中的 GitHub 链接并插入基础引用，但 **`GithubRepoCard` 组件需手动添加**（含 Stars、Forks 等实时数据）。

#### 2a. 查询 GitHub 仓库数据

```bash
curl -s "https://api.github.com/repos/<owner>/<repo>" | grep -E '"stargazers_count"|"forks_count"|"pushed_at"'
```

#### 2b. 编辑文章文件，替换底部的纯文本链接

将文件末尾的：
```markdown
* **GitHub 仓库**: [owner/repo](https://github.com/owner/repo)
```

替换为完整的 GithubRepoCard 组件：
```markdown
<GithubRepoCard 
  repo="owner/repo"
  initialStars="12.3k"
  initialForks="890"
  initialContributors="45"
  initialVersion="v2.1.0"
  initialPushedAt="2026-07-09"
  :platforms="['Linux', 'macOS', 'Windows']"
  :deployments="['Docker', 'pip', 'Source Code']"
/>
```

#### 2c. 修正 frontmatter（如 LLM 超时导致默认值）

检查文件顶部的 frontmatter，确认以下字段正确：
```yaml
short_title: 'ToolName — 简短中文描述'   # 格式：工具名 — 描述，≤20字
description: '有意义的一句话描述'         # 非默认的"来自 YourwayAI 的优选资源"
category: '🤖 AI 与智能体'               # 见下方分类列表
```

#### 2d. 检查并修正侧边栏标签

```bash
grep "wx_YYYYMMDDHHMMSS" docs/.vitepress/config.mts
```

如标签被截断（如 `'ToolName 开源实测：macO'`），手动修正为正确格式：
```
{ text: 'ToolName — 正确的描述', link: '/tools/wx_YYYYMMDDHHMMSS' }
```

---

### 第三步：提交并推送

```bash
npm run build:sitemap
git add docs/tools/wx_YYYYMMDDHHMMSS.md docs/.vitepress/config.mts
git commit -m "docs: 完善 <ToolName> 页面元数据与 GitHub 仓库卡片，分类归入<分类名>"
git push
```

---

## 🅱️ 路径 B：GitHub 仓库 → 新项目（直接从仓库生成）

```bash
python3 scripts/add_tool.py https://github.com/<owner>/<repo>
# 或
npm run add-tool -- https://github.com/<owner>/<repo>
```

**脚本自动完成：**
1. 调用 GitHub API 获取仓库元信息（Stars、语言、协议等）
2. 获取 README 内容（Base64 解码）
3. 调用 NVIDIA LLM 生成完整中文介绍页（含核心特性、安装步骤、使用示例）
4. 创建 `docs/tools/<reponame>.md` 文件（非 wx_ 前缀）
5. 更新 config.mts 侧边栏
6. git push

> ⚠️ 路径 B 不包含 `build:sitemap`，完成后需手动运行：
> ```bash
> npm run build:sitemap && git add . && git commit -m "chore: 更新 sitemap" && git push
> ```

---

## 📚 分类体系

| 分类 | 适用内容 |
|------|----------|
| `🤖 AI 与智能体` | AI 模型、Agent 框架、LLM 工具、提示词工程 |
| `🛠️ 系统与运维` | 服务器、容器、CLI 工具、系统自动化、macOS 工具 |
| `🔒 安全与隐私` | 密码管理、VPN、2FA、加密工具 |
| `✍️ 知识与协作` | 笔记、Wiki、文档、团队协作 |
| `📂 实用与提效` | 文件转换、翻译、RSS、浏览器工具 |
| `💰 金融与支付` | 跨境支付、虚拟卡、订阅服务 |
| `🎨 设计与极客` | UI 设计、前端框架、创意开发 |
| `🍿 影音与娱乐` | 媒体服务器、播放器、流媒体 |

---

## 🧩 GithubRepoCard 参数说明

```markdown
<GithubRepoCard 
  repo="owner/repo"              # 必填：GitHub 仓库路径
  initialStars="12.3k"          # 格式：数字+单位（如 12.3k, 247）
  initialForks="890"             # 格式同上
  initialContributors="45"       # 贡献者数量（可省略）
  initialVersion="v2.1.0"       # 最新版本（可省略，写 N/A 或 Beta）
  initialPushedAt="2026-07-09"  # 最近推送日期，格式 YYYY-MM-DD
  :platforms="['Linux', 'macOS', 'Windows']"   # 支持平台数组
  :deployments="['Docker', 'pip', 'Source Code']"  # 部署方式数组
/>
```

**platforms 可选值**：`Linux`, `macOS`, `Windows`, `iOS`, `Android`, `Web`  
**deployments 可选值**：`Docker`, `pip`, `npm`, `cargo`, `brew`, `Homebrew`, `Source Code`, `Binary`, `CLI`, `GitHub Releases`

---

## 🛠️ 工具链速查

| 命令 | 作用 |
|------|------|
| `npm run add-wx-local -- <url>` | 从微信 URL 添加新文章 |
| `npm run add-tool -- <github_url>` | 从 GitHub 仓库添加新工具 |
| `npm run build:sitemap` | 更新 sitemap.xml 和 projects.md |
| `npm run docs:dev` | 本地预览站点（http://localhost:5173） |
| `npm run docs:build` | 全量构建（sitemap + VitePress） |
| `npm run update:stars` | 批量更新所有仓库 Star 数 |
| `npm run update:stars:dry` | Dry-run，只打印不写入 |

---

## 🚨 故障排除

### LLM API 超时（最常见问题）

**现象**：脚本输出 `LLM API Call Failed or Invalid JSON: ... Read timed out. Falling back to defaults.`

**后果**：
- `short_title` 被截断（如 `'LibreTranslate '`）
- `description` 变为默认值 `'来自 YourwayAI 的优选资源与文章推荐'`
- `category` 可能错误（默认 `📂 实用与提效`）

**修复**：手动编辑文件 frontmatter 和 config.mts 对应条目，参考第二步。

---

### 微信反爬（环境异常）

**现象**：脚本输出 `WeChat blocked this request (Current environment is abnormal).`

**解决**：脚本使用 iPhone Safari UA 通常可绕过，如仍失败，需等待 5-10 分钟后重试。

---

### 侧边栏分类不存在

**现象**：`Warning: Category '...' not found in sidebar.`

**解决**：在 `docs/.vitepress/config.mts` 中确认目标分类名称完全匹配（包含 emoji），或手动添加条目。

---

## 📁 关键文件路径

| 文件 | 作用 |
|------|------|
| `scripts/add_wx_local.py` | 微信文章自动化脚本（主用） |
| `scripts/add_tool.py` | GitHub 仓库自动化脚本 |
| `scripts/build-sitemap.cjs` | 生成 sitemap.xml 和 projects.md |
| `scripts/update_stars.py` | 批量更新 GitHub Star 数 |
| `docs/.vitepress/config.mts` | 侧边栏配置（含分类与计数） |
| `docs/tools/` | 所有项目 Markdown 文件目录 |
| `docs/public/sitemap.xml` | 自动生成，勿手动编辑 |
| `docs/projects.md` | 自动生成，勿手动编辑 |
