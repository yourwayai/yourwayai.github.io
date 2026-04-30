---
title: FluentFlyout
description: "Windows 11 上最美的开源媒体浮层应用，完美融合 Fluent 2 设计语言，比微软官方做得更好。"
category: '👨‍💻 开发者工具'
date: '2026-04-28T22:46:22+08:00'
---
# FluentFlyout：Windows 11 的媒体浮层完美替代品

![FluentFlyout OpenGraph Image](https://opengraph.githubassets.com/1/unchihugo/FluentFlyout)

**FluentFlyout** 是为 Windows 11 精心打造的开源媒体浮层应用，完全基于微软的 **Fluent 2 Design** 设计规范构建。当你按下键盘上的音量键或快捷键时，它以一个精致、流畅、原生感十足的浮层弹出媒体信息——比 Windows 11 系统自带的媒体控制更美观，功能也更强大。

> "Windows 11 may have just gained another must-have app." — **Windows Central**
>
> "Does a better job than what Microsoft officially offers." — **Neowin**

* **GitHub Repo**: [unchihugo/FluentFlyout](https://github.com/unchihugo/FluentFlyout)
* **Star 数**: ⭐ 2,600+
* **官方主页**: [https://fluentflyout.com](https://fluentflyout.com)
* **核心语言**: C# (WPF)
* **开源协议**: GNU General Public License v3.0

---

## ✨ 核心特性

### 1. 媒体浮层（Audio Flyout）
当你控制音量或切换歌曲时，弹出包含以下信息的精美浮层：
- 🎵 **专辑封面**（高清图片）
- 🎤 **歌曲标题 & 艺术家**
- ⏯️ **完整媒体控制**：播放/暂停、上一曲/下一曲
- 🔁 **播放模式**：循环播放全部、单曲循环、随机播放

### 2. "Up Next" 浮层
当一首歌即将结束时，自动弹出下一首歌的预告浮层，让你提前掌握播放队列，无需打开任何应用。

### 3. 锁定键状态浮层（Lock Keys Flyout）
当按下 Caps Lock、Num Lock 或 Scroll Lock 时，以简洁浮层实时显示锁定键状态，告别不知道大写锁定是否开启的困扰。

### 4. 任务栏媒体小组件（Taskbar Widget）
将当前正在播放的歌曲信息**直接显示在 Windows 11 任务栏**上，无需浮层弹出即可一目了然地查看媒体状态。

### 5. 原生 Windows 11 视觉体验
- 🌟 **Fluent 2 组件**：与系统 UI 高度一致的控件
- 🪟 **Mica 模糊背景**：利用 Windows 11 的 Mica 材质效果，背景自动融入桌面内容
- 🎨 **系统主题跟随**：自动适配你的 Windows 强调色
- 🌓 **深色/浅色模式**：与系统主题同步切换
- ⚡ **丝滑动画**：60fps 流畅过渡动画
- 📍 **自定义浮层位置**：可调整弹出位置
- 🔕 **系统托盘运行**：安静驻留后台，不干扰工作

---

## 📥 安装方式

FluentFlyout 提供两个版本，功能基本相同：

### 方式一：GitHub 免费版（完全开源）

1. 访问 [最新发布页面](https://github.com/unchihugo/FluentFlyout/releases/latest)
2. 下载 `*.cer` 证书文件，双击安装并信任（本地签名证书）
3. 下载 `*.msixbundle` 安装包，双击安装
4. 启动后在系统托盘中找到 FluentFlyout 图标

```
⚠️ GitHub 版本需要手动更新，安装时需要先安装自签名证书。
```

### 方式二：Microsoft Store 版（自动更新）
在 Microsoft Store 搜索 **FluentFlyout** 即可一键安装。Store 版提供自动后台更新，并解锁少量额外特性（需一次性付费 €2.99，用于支持开发者持续维护）。

> **GitHub 版是完全免费且功能完整的**，Store 版的额外功能仅为可选加成，不影响核心体验。

---

## ⚙️ 个性化设置

点击系统托盘图标进入 FluentFlyout 设置：
- 调整浮层弹出位置（左上、右上、左下、右下、居中等）
- 开关各类浮层（媒体、音量、锁定键）
- 设置任务栏小组件显示内容
- 配置深色/浅色模式偏好
- 调整动画速度

---

## 🛠️ 技术栈

FluentFlyout 基于成熟的 Windows 开发生态构建：
- **WPF (Windows Presentation Foundation)**: UI 框架
- **MicaWPF**: Mica 模糊效果实现
- **WPF-UI**: Fluent 2 设计组件库
- **WindowsMediaController**: Windows 媒体会话 API 封装

---

## 💡 适用场景与总结

如果你是 Windows 11 用户，且对系统自带的媒体控制 OSD（屏幕显示）感到不满——它太丑、信息太少、动画太生硬——FluentFlyout 就是你需要的答案。它不需要任何配置即可开箱即用，静静地待在系统托盘里，在你需要时以最优雅的方式呈现媒体信息。安装后几乎没有任何理由卸载它。
