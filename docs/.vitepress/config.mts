import { defineConfig } from 'vitepress'
import fs from 'fs'
import path from 'path'
import { withPwa } from '@vite-pwa/vitepress'

export default withPwa(defineConfig({
  pwa: {
    outDir: '.vitepress/dist',
    registerType: 'autoUpdate',
    includeAssets: ['favicon.ico', 'logo.jpg'],
    manifest: {
      name: 'YourwayAI开源导航站',
      short_name: 'YourwayAI',
      description: '发现极致优雅的重磅开源软件与极客工具',
      theme_color: '#646cff',
      background_color: '#1b1b1f',
      display: 'standalone',
      start_url: '/',
      icons: [
        {
          src: '/logo.jpg',
          sizes: '192x192',
          type: 'image/jpeg'
        },
        {
          src: '/logo.jpg',
          sizes: '512x512',
          type: 'image/jpeg'
        }
      ]
    },
    workbox: {
      globPatterns: ['**/*.{js,css,html,ico,jpg,png,svg,woff2}'],
      navigateFallback: null,
      runtimeCaching: [
        {
          urlPattern: /^https:\/\/yourwayai\.github\.io\/.*/i,
          handler: 'NetworkFirst',
          options: {
            cacheName: 'yourwayai-cache',
            expiration: { maxEntries: 100, maxAgeSeconds: 60 * 60 * 24 * 7 }
          }
        },
        {
          urlPattern: /^https:\/\/github\.com\/.*/i,
          handler: 'StaleWhileRevalidate',
          options: {
            cacheName: 'github-avatars',
            expiration: { maxEntries: 200, maxAgeSeconds: 60 * 60 * 24 * 30 }
          }
        }
      ]
    }
  },

  base: '/',
  title: "YourwayAI开源导航站",
  description: "发现优质的免费开源软件",

  // 网站头部配置 (Favicon 与 OpenGraph 多媒体分享标签)
  head: [
    ['link', { rel: 'icon', href: '/logo.jpg' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:image', content: 'https://yourwayai.github.io/logo.jpg' }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }]
  ],
  
  // 启用最后更新时间
  lastUpdated: true,

  themeConfig: {
    // 网站Logo
    logo: '/logo.jpg',

    // 网站顶部的导航栏
    nav: [
      { text: '首页', link: '/' },
      { text: '项目目录', link: '/projects' },
      { text: '✨ 求职服务', link: '/ywc_resume_landing_page.html', target: '_blank' },
      { text: '关于', link: '/about' }
    ],

    // 网站左侧的分类侧边栏
    sidebar: [
      {
        text: '🤖 AI 与智能体 (41)',
        collapsed: false,
        items: [
          { text: 'Jellyfish — AI 短剧生产工作台', link: '/tools/wx_20260518005533' },
          { text: 'Kronos — 金融大模型', link: '/tools/wx_20260518005849' },
          { text: 'Hermes Agent — 开源 AI 代理', link: '/tools/hermes-agent' },
          { text: 'Goose — 本地 AI 代理', link: '/tools/goose' },
          { text: 'Rapid-MLX — 本地 AI 加速引擎', link: '/tools/wx_20260511215328' },
          { text: 'The Agency — AI 专家智能体', link: '/tools/wx_20260518003237' },
          { text: 'Mercury Agent — 本地 AI 智能体', link: '/tools/wx_20260518005305' },
          { text: 'Project AIRI — 开源赛博女友终结者', link: '/tools/wx_20260518005642' },
          { text: 'llmfit — 本地 LLM 模型硬件智能管家', link: '/tools/wx_20260524213111' },
          { text: 'CLI-Anything — 软件Agent化终结者', link: '/tools/wx_20260524213854' },
          { text: 'Supertonic — 极速本地 TTS 引擎', link: '/tools/wx_20260524214020' },
          { text: 'financial-services — 金融 AI 智能体', link: '/tools/wx_20260524214529' },
          { text: 'UI-TARS — 多模态 GUI Agent', link: '/tools/wx_20260524214734' },
          { text: 'Vane — 本地 AI 搜索引擎', link: '/tools/wx_20260524214934' },
          { text: 'OmniVoice Studio — 本地 AI 配音', link: '/tools/wx_20260530171254' },
          { text: 'Next AI Draw.io — 本地 AI 交互画图', link: '/tools/wx_20260605172228' },
          { text: 'VoxCPM2 — 未来语音大模型', link: '/tools/wx_20260605172524' },
          { text: 'Agentic Inbox — AI 智能收件箱', link: '/tools/wx_20260605173109' },
          { text: 'TuriX-CUA — 开源桌面自动化助手', link: '/tools/wx_20260605173551' },
          { text: 'PilotDeck — Agent 生产力操作系统', link: '/tools/wx_20260605173728' },
          { text: 'Nanobot — 港大轻量开源 Agent', link: '/tools/wx_20260605173904' },
          { text: 'NVIDIA Agent Skills — AI 助手精准接管', link: '/tools/wx_20260611153942' },
          { text: 'Anthropic Agent Skills — AI 定制化时代', link: '/tools/wx_20260611154756' },
          { text: 'Agent Reach — 联网脚手架', link: '/tools/wx_20260611155218' },
          { text: 'Open Notebook — 本地化 NotebookLM 替代方案', link: '/tools/wx_20260612100000' },
          { text: 'Supervision — 统一视觉模型输出标准', link: '/tools/wx_20260623201519' },
          { text: 'Skills — AI 上下文约束', link: '/tools/wx_20260711124623' },
          { text: 'Obsidian-Skills — 规范本地知识库', link: '/tools/wx_20260711131603' },
          { text: 'MisoTTS — 8B 开源语音模型', link: '/tools/wx_20260711132559' },
          { text: 'TimesFM — 谷歌开源时序预测模型', link: '/tools/wx_20260711132813' },
          { text: 'AirLLM — 低显存本地大模型推理', link: '/tools/wx_20260711133118' },
          { text: 'json-render — Vercel 开源生成式 UI 框架', link: '/tools/wx_20260722212844' },
          { text: 'Ponytail — AI 编码智能体极简主义约束', link: '/tools/wx_20260722213736' },
          { text: 'PPT Master — PDF 到可编辑 PPT 自动化', link: '/tools/wx_20260722214006' },
          { text: 'SenseNova-U1 — 商汤信息图生成与定点编辑大模型', link: '/tools/wx_20260727160720' },
          { text: 'ClawFeed — 开源 AI 资讯提炼与分发平台', link: '/tools/wx_20260727161635' },
          { text: 'StaffDeck — 数字员工全生命周期管理平台', link: '/tools/wx_20260727161713' },
          { text: 'Understand Anything — 代码库架构直观仪表盘', link: '/tools/wx_20260807225907' },
          { text: 'TokenHub — 私有化企业级 AI 网关', link: '/tools/wx_20260807230325' },
          { text: 'ai-for-grant-writing — 学术标书撰写 AI 工作流', link: '/tools/wx_20260815092126' },
          { text: 'ClaudeBar — macOS AI 编程配额监控', link: '/tools/wx_20260815092531' }
        ]
      },
      {
        text: '🛠️ 系统与运维 (17)',
        collapsed: false,
        items: [
          { text: '3x-ui — Xray 协议面板', link: '/tools/3x-ui' },
          { text: 'Beszel — 轻量服务器监控', link: '/tools/beszel' },
          { text: 'Prometheus — 云原生监控', link: '/tools/wx_20260511214354' },
          { text: 'FluentFlyout — 电池弹窗美化', link: '/tools/fluentflyout' },
          { text: 'DroidDesk — 轻松部署 Linux 桌面', link: '/tools/wx_20260530171455' },
          { text: 'optimizerDuck — 免费 Windows 调优神器', link: '/tools/wx_20260530171710' },
          { text: 'OfficeCLI — 自动化 Office 工作流', link: '/tools/wx_20260611154651' },
          { text: 'Jujutsu — 极客版本地 Git', link: '/tools/wx_20260611155310' },
          { text: 'Apple Container — macOS 原生容器', link: '/tools/wx_20260711131141' },
          { text: 'Forel — macOS 本地文件自动化', link: '/tools/wx_20260711134309' },
          { text: 'pgrust — Rust 重写 Postgres 18.3', link: '/tools/wx_20260722214639' },
          { text: 'franken_markdown — Rust零依赖 Markdown 渲染器', link: '/tools/wx_20260727161131' },
          { text: 'reed-solomon-turbo — Rust 高性能纠删码库', link: '/tools/wx_20260727161322' },
          { text: 'Openship — 开源自托管容器化部署平台', link: '/tools/wx_20260727161521' },
          { text: 'Dokploy — 开源 Docker Swarm 自托管 PaaS 面板', link: '/tools/wx_20260727161558' },
          { text: 'Home Lab Hub — 开源 Homelab 基础设施看板', link: '/tools/wx_20260807230942' },
          { text: 'Mailu — Docker 开源邮件服务器', link: '/tools/wx_20260815092411' }
        ]
      },
      {
        text: '🔒 安全与隐私 (4)',
        collapsed: false,
        items: [
          { text: '2FAuth — 自托管 2FA 令牌', link: '/tools/2fauth' },
          { text: 'Vaultwarden — 轻量级密码库', link: '/tools/wx_20260511214924' },
          { text: 'Fcitx5 — 开源输入法', link: '/tools/wx_20260518005748' },
          { text: 'Bumblebee — 开源安全扫描工具', link: '/tools/wx_20260530171127' }
        ]
      },
      {
        text: '✍️ 知识与协作 (5)',
        collapsed: false,
        items: [
          { text: 'Outline — 团队 Wiki 知识库', link: '/tools/outline' },
          { text: 'Memos — 碎片化灵感笔记', link: '/tools/memos' },
          { text: 'Ghost — 开源博客系统', link: '/tools/wx_20260421130229' },
          { text: 'Chatwoot — 全渠道客服中台', link: '/tools/chatwoot' },
          { text: 'Twenty — TypeScript 开源 CRM', link: '/tools/wx_20260611154932' }
        ]
      },
      {
        text: '📂 实用与提效 (9)',
        collapsed: false,
        items: [
          { text: 'Stirling-PDF — 全能 PDF 工具箱', link: '/tools/stirling-pdf' },
          { text: 'RSSHub — 万物皆可 RSS', link: '/tools/rsshub' },
          { text: 'LocalSend — 跨平台文件传输', link: '/tools/wx_20260511215131' },
          { text: 'Open Chrome — 浏览器神器', link: '/tools/wx_20260413125458' },
          { text: 'ConvertX — 格式转换利器', link: '/tools/wx_20260429211232' },
          { text: 'CookCLI — 菜谱管理命令行', link: '/tools/cookcli' },
          { text: 'AirTranslate — Mac全局音频翻译', link: '/tools/wx_20260530171544' },
          { text: 'LibreTranslate — 自托管离线翻译', link: '/tools/wx_20260711133932' },
          { text: 'MD-This-Page — 网页一键转 Markdown', link: '/tools/wx_20260815093123' }
        ]
      },
      {
        text: '💰 金融与支付 (4)',
        collapsed: false,
        items: [
          { text: '熊猫速汇 — 跨境汇款攻略', link: '/tools/wx_20260419212801' },
          { text: 'AI 订阅 — 支付宝付款全攻略', link: '/tools/wx_20260419212858' },
          { text: '效率工具 — AI 时代神器推荐', link: '/tools/wx_20260421112236' },
          { text: 'InvoiceShelf — 开源财务管理', link: '/tools/wx_20260511214626' }
        ]
      },
      {
        text: '🎨 设计与极客 (6)',
        collapsed: false,
        items: [
          { text: 'Penpot — 开源设计工具', link: '/tools/penpot' },
          { text: 'Storybook — UI 组件开发环境', link: '/tools/storybook' },
          { text: 'V8 Engine — JS 运行引擎', link: '/tools/v8' },
          { text: 'The Art of Command Line — 终端神技', link: '/tools/the-art-of-command-line' },
          { text: 'MoBrowser-App-Icon-Maker — AI 图标生成', link: '/tools/wx_20260530171623' },
          { text: 'PDFx — React 开源 PDF 组件库', link: '/tools/wx_20260815093312' }
        ]
      },
      {
        text: '🍿 影音与娱乐 (4)',
        collapsed: false,
        items: [
          { text: 'Jellyfin — 自建私人影院', link: '/tools/jellyfin' },
          { text: 'video-autopilot-kit — 开源短视频自动化框架', link: '/tools/wx_20260722214409' },
          { text: 'Wizarr — 影音服务器自动化邀请', link: '/tools/wx_20260722214537' },
          { text: 'Antra — 跨平台无损本地音乐库构建器', link: '/tools/wx_20260727160923' }
        ]
      }
    ],

    // 右上角的社交链接
    socialLinks: [
      { icon: 'github', link: 'https://github.com/yourwayai/yourwayai.github.io' }
    ],

    // 搜索功能
    search: {
      provider: 'local',
      options: {
        locales: {
          root: {
            translations: {
              button: {
                buttonText: '搜索文档',
                buttonAriaLabel: '搜索文档'
              },
              modal: {
                noResultsText: '无法找到相关结果',
                resetButtonTitle: '清除查询条件',
                footer: {
                  selectText: '选择',
                  navigateText: '切换',
                  closeText: '关闭'
                }
              }
            }
          }
        }
      }
    },

    // 编辑此页
    editLink: {
      pattern: 'https://github.com/yourwayai/yourwayai.github.io/edit/main/docs/:path',
      text: '在 GitHub 上编辑此页'
    },

    // 页面导航及本地化中文字段
    outline: {
      level: [2, 3],
      label: '页面导航'
    },
    docFooter: {
      prev: '上一页',
      next: '下一页'
    },
    lastUpdated: {
      text: '最后更新于'
    },
    returnToTopLabel: '回到顶部',
    sidebarMenuLabel: '相关文章',
    darkModeSwitchLabel: '主题',

    // 页脚
    footer: {
      message: 'Released under the MIT License.<br/><span style="display:inline-flex;align-items:center;gap:0.8rem;margin-top:0.5rem;font-size:0.9rem;"><a href="/ywc_resume_landing_page.html" target="_blank" rel="noopener">🏅 赞助我们</a> <span style="opacity:0.3">|</span> <a href="https://github.com" target="_blank" rel="noopener">GitHub</a> <span style="opacity:0.3">|</span> <a href="https://openai.com" target="_blank" rel="noopener">OpenAI</a> <span style="opacity:0.3">|</span> <a href="https://gemini.google.com" target="_blank" rel="noopener">Gemini</a> <span style="opacity:0.3">|</span> <a href="https://claude.ai" target="_blank" rel="noopener">Claude</a></span>',
      copyright: 'Copyright © 2026-present YourwayAI'
    }
  },

  async transformPageData(pageData) {
    const title = pageData.frontmatter.title || pageData.title || 'YourwayAI开源导航站'
    const desc = pageData.frontmatter.description || pageData.description || '发现极致优雅的重磅开源软件与极客工具'
    
    // Ensure head array exists
    pageData.frontmatter.head = pageData.frontmatter.head || []
    
    // Add og:title & og:description dynamically
    pageData.frontmatter.head.push(['meta', { property: 'og:title', content: title }])
    pageData.frontmatter.head.push(['meta', { property: 'og:description', content: desc }])
    pageData.frontmatter.head.push(['meta', { property: 'og:url', content: `https://yourwayai.github.io/${pageData.relativePath.replace(/\.md$/, '.html')}` }])
    
    // Check if there is a GitHub repository link in content and inject JSON-LD
    let githubUrl = null
    try {
      const absolutePath = path.resolve(__dirname, '..', pageData.relativePath)
      if (fs.existsSync(absolutePath)) {
        const content = fs.readFileSync(absolutePath, 'utf-8')
        // Regex to search for typical GitHub repository URL
        const githubMatch = content.match(/https:\/\/github\.com\/[a-zA-Z0-9_-]+\/[a-zA-Z0-9_.-]+/i)
        if (githubMatch) {
          githubUrl = githubMatch[0].replace(/\.git$/, '')
        }
      }
    } catch (e) {
      console.error(`Error reading file for ${pageData.relativePath}:`, e)
    }

    if (pageData.relativePath.startsWith('tools/') && githubUrl) {
      const jsonLd = {
        "@context": "https://schema.org",
        "@type": "SoftwareSourceCode",
        "name": title,
        "url": `https://yourwayai.github.io/${pageData.relativePath.replace(/\.md$/, '.html')}`,
        "codeRepository": githubUrl
      }
      pageData.frontmatter.head.push([
        'script',
        { type: 'application/ld+json' },
        JSON.stringify(jsonLd)
      ])
    }
  },

  async buildEnd(siteConfig) {
    const outDir = siteConfig.outDir
    const toolsDir = path.resolve(siteConfig.srcDir, 'tools')
    
    if (!fs.existsSync(toolsDir)) return

    try {
      const files = fs.readdirSync(toolsDir).filter(f => f.endsWith('.md'))
      const tools = []

      for (const file of files) {
        const filePath = path.join(toolsDir, file)
        const content = fs.readFileSync(filePath, 'utf-8')
        
        // Parse frontmatter
        const match = content.match(/^---\r?\n([\s\S]*?)\r?\n---/)
        const fm = {}
        if (match) {
          const lines = match[1].split('\n')
          for (let line of lines) {
            const parts = line.split(':')
            if (parts.length >= 2) {
              const key = parts[0].trim()
              const value = parts.slice(1).join(':').trim().replace(/^['"]|['"]$/g, '')
              fm[key] = value
            }
          }
        }
        
        // Parse title and description
        const title = fm.title || file.replace(/\.md$/, '')
        const description = fm.description || ''
        const dateStr = fm.date || fs.statSync(filePath).mtime.toISOString()
        const date = new Date(dateStr)

        tools.push({
          title,
          description,
          date,
          link: `https://yourwayai.github.io/tools/${file.replace(/\.md$/, '.html')}`
        })
      }

      // Sort by date descending and take top 50
      tools.sort((a, b) => b.date.getTime() - a.date.getTime())
      const latestTools = tools.slice(0, 50)

      // Generate RSS XML
      let rssXml = '<?xml version="1.0" encoding="utf-8"?>\n'
      rssXml += '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n'
      rssXml += '  <channel>\n'
      rssXml += '    <title>YourwayAI开源导航站</title>\n'
      rssXml += '    <link>https://yourwayai.github.io</link>\n'
      rssXml += '    <description>发现极致优雅的重磅开源软件与极客工具</description>\n'
      rssXml += '    <language>zh-CN</language>\n'
      rssXml += `    <pubDate>${new Date().toUTCString()}</pubDate>\n`
      rssXml += '    <atom:link href="https://yourwayai.github.io/rss.xml" rel="self" type="application/rss+xml"/>\n'

      for (const tool of latestTools) {
        rssXml += '    <item>\n'
        rssXml += `      <title><![CDATA[${tool.title}]]></title>\n`
        rssXml += `      <link>${tool.link}</link>\n`
        rssXml += `      <guid>${tool.link}</guid>\n`
        rssXml += `      <description><![CDATA[${tool.description}]]></description>\n`
        rssXml += `      <pubDate>${tool.date.toUTCString()}</pubDate>\n`
        rssXml += '    </item>\n'
      }

      rssXml += '  </channel>\n'
      rssXml += '</rss>\n'

      const rssPath = path.join(outDir, 'rss.xml')
      fs.writeFileSync(rssPath, rssXml, 'utf-8')
      console.log(`Generated RSS feed at ${rssPath} with ${latestTools.length} items.`)
    } catch (e) {
      console.error('Error generating RSS feed:', e)
    }
  }
}))
