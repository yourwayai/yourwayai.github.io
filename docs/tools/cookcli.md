---
title: CookCLI
description: "基于 Cooklang 的开源菜谱管理工具：命令行+内嵌 Web 服务器，让你的食谱库像代码仓库一样优雅管理。"
category: '👨‍💻 开发者工具'
date: '2026-04-28T22:45:04+08:00'
---
# CookCLI：程序员的菜谱管理神器

![CookCLI OpenGraph Image](https://opengraph.githubassets.com/1/cooklang/cookcli)

**CookCLI** 是 [Cooklang](https://cooklang.org) 生态系统的官方命令行工具，用 Rust 构建，集菜谱解析、购物清单生成、食材库存管理和内嵌 Web 服务器于一体。它的核心理念是将厨房食谱纳入 UNIX 哲学管理体系——**像管理代码一样管理你的食谱**。

* **GitHub Repo**: [cooklang/cookcli](https://github.com/cooklang/cookcli)
* **Star 数**: ⭐ 1,300+
* **官方主页**: [https://demo.cooklang.org](https://demo.cooklang.org)
* **核心语言**: Rust
* **开源协议**: MIT License

---

## 🍳 什么是 Cooklang？

Cooklang 是一种专为菜谱设计的**纯文本标记语言**。你用 `.cook` 文件格式记录食谱，食材、炊具和步骤都有明确的语法标记，便于机器解析和程序处理：

```cooklang
将 @橄榄油{2%汤匙} 加热，放入 @大蒜{3%瓣} 翻炒，
加入 @番茄罐头{400%克} 和 @食盐{适量}，用 #平底锅 小火炖 ~{20%分钟}。
```

这种格式让你的食谱成为**结构化数据**，可以被程序化地生成购物清单、按人数缩放食材用量，或用任意工具处理。

---

## ✨ 核心功能

### 1. `cook recipe` — 菜谱解析与格式转换
解析并展示 `.cook` 文件，支持人数缩放和多种输出格式：

```bash
# 查看菜谱（人类可读格式）
cook recipe "番茄肉酱意面.cook"

# 按 4 人份缩放食材
cook recipe "披萨.cook:4"

# 导出为 JSON（用于程序处理）
cook recipe "蛋糕.cook" -f json

# 保存为 Markdown
cook recipe "沙拉.cook" -f markdown > salad.md
```

### 2. `cook shopping-list` — 智能购物清单
从一个或多个菜谱中自动合并食材，生成按货架区域分类的购物清单：

```bash
# 多道菜合并购物清单
cook shopping-list "周一晚餐.cook" "周二早餐.cook"

# 含人数缩放
cook shopping-list "意面.cook:3" "沙拉.cook"

# 目录下所有菜谱
cook shopping-list *.cook
```

### 3. `cook server` — 内嵌 Web 服务器
一键启动本地 Web 界面，从任意设备的浏览器浏览你的食谱库：

```bash
# 默认启动，监听本地
cook server

# 允许局域网其他设备访问（手机、平板）
cook server --host

# 启动后自动打开浏览器
cook server --open
```

> 在线体验：[demo.cooklang.org](https://demo.cooklang.org)

### 4. `cook pantry` — 食材库存管理
跟踪家中食材库存，自动识别低库存、临期食材，并根据现有库存推荐可做的菜：

```bash
# 查看低库存或缺货食材
cook pantry depleted

# 检查 7 天内到期食材
cook pantry expiring

# 根据现有食材推荐菜谱
cook pantry recipes

# 支持部分匹配（60% 食材到位即推荐）
cook pantry recipes --partial --threshold 60
```

### 5. `cook import` — 从网页导入食谱
一键从任意菜谱网站导入并转换为 Cooklang 格式（需配置 OpenAI API Key）：

```bash
OPENAI_API_KEY=sk-xxx cook import https://www.example.com/recipe > recipe.cook
```

### 6. `cook search` / `cook doctor`
- **search**: 按食材、步骤关键词全文搜索整个食谱库
- **doctor**: 检查食谱语法错误、购物分类配置和库存配置的健康状况

---

## 📦 安装方式

```bash
# macOS / Linux（推荐，使用 Homebrew）
brew install cookcli

# Rust 用户（通过 Cargo）
cargo install cookcli

# 所有平台（下载预编译二进制）
# 访问：https://github.com/cooklang/CookCLI/releases
```

---

## ⚙️ 个性化配置

在食谱目录的 `config/` 文件夹中创建配置文件：

**`aisle.conf`** — 定义超市货架分区，让购物清单更有序：
```ini
[produce]
西红柿|番茄
大蒜|蒜

[dairy]
牛奶
黄油
奶酪
```

**`pantry.conf`** — 记录当前库存（已有食材自动从购物清单中排除）：
```toml
[冰箱]
牛奶 = { quantity = "2%L", low = "500%ml", expire = "10.05.2025" }
鸡蛋 = "12%个"

[储藏室]
大米 = { quantity = "5%kg", low = "1%kg" }
橄榄油 = { quantity = "1%L", low = "250%ml" }
```

---

## 💡 适用场景与总结

CookCLI 是工程师审美与厨房生活的完美结合。如果你习惯用 Git 管理一切，厌倦了截图或手抄食谱，想要用脚本自动化一周的饮食计划并生成精准购物清单——CookCLI 是目前最优雅的解决方案。

> 将你的食谱库放进 Git 仓库，像版本控制代码一样管理它，就是 Cooklang 生态给出的终极答案。
