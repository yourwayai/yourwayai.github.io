import { defineConfig } from 'vitepress'

export default defineConfig({
  base: '/yourwayai/',
  title: "YourwayAI开源导航站",
  description: "发现优质的免费开源软件",
  themeConfig: {
    // 网站顶部的导航栏
    nav: [
      { text: '首页', link: '/' },
      { text: '软件库', link: '/tools/outline' },
      { text: '关于', link: '/about' }
    ],

    // 网站左侧的分类侧边栏
    sidebar: [
      {
        text: '笔记与知识库',
        items: [
          { text: 'Outline (团队Wiki)', link: '/tools/outline' },
          { text: 'Memos (碎片化笔记)', link: '/tools/memos' }
        ]
      },
      {
        text: '媒体与影音',
        items: [
          { text: 'Jellyfin (私人影院)', link: '/tools/jellyfin' }
        ]
      },
      {
        text: '自动化收录',
        items: [
          { text: '命令行的艺术',
          link: '/tools/the-art-of-command-line' },
          { text: 'V8 Engine',
          link: '/tools/v8' },
          { text: 'chatwoot', link: '/tools/chatwoot' }
        ]
      },
      {
        text: '公众号优选',
        items: [
          { text: '本地Copilot：Tabby',
          link: '/tools/tabby' },
          { text: 'GitHub热榜开源 Tabb...', link: '/tools/wx_20260413125042' }
        ]
      }
    ],

    // 右上角的社交链接
    socialLinks: [
      { icon: 'github', link: 'https://github.com/BruceMi321/yourwayai' }
    ]
  }
})
