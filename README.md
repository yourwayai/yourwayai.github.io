# YourwayAI 开源导航门户

<p align="center">
  <img src="docs/public/logo.jpg" alt="YourwayAI Logo" width="200" style="border-radius:20px;">
</p>

![VitePress](https://img.shields.io/badge/VitePress-1.6.4-18d867?style=flat-square&logo=vitepress)
![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

**YourwayAI** 是一个极致纯净、高度自动化的开源知识与软件导航门户。我们致力于打破高昂商业软件的订阅壁垒，为黑客、极客和普通用户发掘世界上最优秀的开源替代品。

## 🌟 核心特色与架构升级

本项目并不仅仅是一个静态的 Markdown 展示模板，在底层它已经被打造成了一台高效运作的“数字知识收割机”：

- **💅 深度品牌订制**：拦截 VitePress 底层 CSS 变量，全站融入专属荧光绿（#18d867）品牌配色。
- **🔍 毫秒级全局检索**：内置 Local Search，支持秒查站点收录的所有开源信息。
- **🌐 顶级流量引擎 (Open Graph)**：引入全面的 SEO 及多媒体卡片分享配置，转发链接自动伸展巨型精美卡片。
- **📊 动态数据感知**：拒绝静态死文字，页面通过 API 实时读取展示 GitHub 开源项目的 Start 数量与版本进度章徽。
- **🛠️ 终极防盗链突破机制**：使用本地 Python 抓取配合全球图片代理服务器，完美绕过微信公众号等平台针对图片的防盗链拦截限制。

---

## 🚀 极其硬核的自动化收录双引擎（Automated Scripts）

我们彻底抛弃了低效的手工编排，本项目内置了两个强大的本地 Python 收录管道，您只管塞链接，其余的（拉取、格式化、甚至 Git Push 发布）全部交给脚本自动搞定！

### 引擎 1：GitHub 开源代码库一键收录
用来抓取标准的 GitHub 托管项目。
```bash
npm run add-tool -- https://github.com/用户名/仓库名
```
**它会自动做这些事**：
1. 调用内部逻辑解析并抓取 GitHub Repo 核心资料。
2. 生成自带漂亮排版且拥有实时动态徽章（Badges）的 Markdown 文档。
3. 自动注入导航系统并触发 Git Push 同步全网。

### 引擎 2：微信公众号长文极限破壁收录
用来对付反爬手段极其严苛的微信公众号文章体系。
```bash
npm run add-wx -- https://mp.weixin.qq.com/s/xxxxxx
```
**它会自动做这些事**：
1. 在您本地高信誉度 IP 下直穿微信防爬火墙。
2. 通过 BeautifulSoup 剔除一切无关广告元素，只留下纯净核心 `#js_content` 并一键 `Markdownify` 化。
3. 拦截微信 `data-src` 懒加载请求，并主动套一层 `images.weserv.nl` 的全球代理外壳，彻底终结“此图片来自微信公众平台，未经允许不可引用”这句魔咒！


---

## 🛠️ 快速启动本地环境

获取本代码后，您可以在本地进行热更新预览：

```bash
# 1. 安装核心运行库
npm install
pip3 install requests beautifulsoup4 markdownify

# 2. 启动急速开发服务器
npm run docs:dev
```

## 📂 简明极客目录

```text
YourwayAI/
├── docs/               
│   ├── .vitepress/              # VitePress 高级配置区
│   │   ├── theme/               # 自定义高亮渲染 CSS
│   │   └── config.mts           # 核心菜单、SEO、配置总线
│   ├── tools/                   # 所有被脚本自动抓取生成的文章本体
│   └── public/                  # 专属 Logo 及公共资源
├── scripts/            
│   ├── add_tool.py              # GitHub 收录引擎器
│   └── add_wx.py                # 微信文章破壁引擎器
└── package.json                 # 快捷终端命令定义
```

## 📄 开源与致谢

本项目由 **Yourway AI** 首发构建，使用 [MIT License](LICENSE) 开源协议，您可以自由定制与分发您的内容站点。
