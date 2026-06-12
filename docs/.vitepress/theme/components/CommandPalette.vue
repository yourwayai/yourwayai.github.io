<script setup>
import { ref, computed, onMounted, onUnmounted, nextTick } from 'vue'
import { useRouter } from 'vitepress'

// ── 工具数据 ──────────────────────────────────────────────
// 从 VitePress sidebar config 中提取的扁平化工具列表
// 使用 import.meta.glob 在构建时获取所有工具 frontmatter
const allTools = ref([])
const isLoading = ref(true)

// 加载所有工具的 frontmatter
const loadTools = async () => {
  try {
    // VitePress 在客户端没有直接的方式访问所有页面数据
    // 所以我们从预生成的 JSON 或内联数据获取
    const modules = import.meta.glob('/docs/tools/*.md', { eager: false })
    const tools = []
    
    for (const path in modules) {
      try {
        const mod = await modules[path]()
        const fm = mod.__pageData?.frontmatter || {}
        const slug = path.replace('/docs/tools/', '').replace('.md', '')
        if (fm.title) {
          tools.push({
            title: fm.title,
            description: fm.description || '',
            category: fm.category || '',
            icon: fm.icon || '',
            stars: fm.stars || '',
            link: `/tools/${slug}`,
          })
        }
      } catch (e) {
        // skip
      }
    }
    allTools.value = tools
  } catch (e) {
    // Fallback: use inline data from sidebar
    allTools.value = INLINE_TOOLS
  } finally {
    isLoading.value = false
  }
}

// 内联的工具数据 fallback（与 config.mts sidebar 同步）
const INLINE_TOOLS = [
  { title: 'Jellyfish — AI 短剧生产工作台', link: '/tools/wx_20260518005533', category: '🤖 AI 与智能体' },
  { title: 'Kronos — 金融大模型', link: '/tools/wx_20260518005849', category: '🤖 AI 与智能体' },
  { title: 'Hermes Agent — 开源 AI 代理', link: '/tools/hermes-agent', category: '🤖 AI 与智能体' },
  { title: 'Goose — 本地 AI 代理', link: '/tools/goose', category: '🤖 AI 与智能体' },
  { title: 'Rapid-MLX — 本地 AI 加速引擎', link: '/tools/wx_20260511215328', category: '🤖 AI 与智能体' },
  { title: 'The Agency — AI 专家智能体', link: '/tools/wx_20260518003237', category: '🤖 AI 与智能体' },
  { title: 'Mercury Agent — 本地 AI 智能体', link: '/tools/wx_20260518005305', category: '🤖 AI 与智能体' },
  { title: 'Project AIRI — 开源赛博女友终结者', link: '/tools/wx_20260518005642', category: '🤖 AI 与智能体' },
  { title: 'llmfit — 本地 LLM 模型硬件智能管家', link: '/tools/wx_20260524213111', category: '🤖 AI 与智能体' },
  { title: 'CLI-Anything — 软件Agent化终结者', link: '/tools/wx_20260524213854', category: '🤖 AI 与智能体' },
  { title: 'Supertonic — 极速本地 TTS 引擎', link: '/tools/wx_20260524214020', category: '🤖 AI 与智能体' },
  { title: 'financial-services — 金融 AI 智能体', link: '/tools/wx_20260524214529', category: '🤖 AI 与智能体' },
  { title: 'UI-TARS — 多模态 GUI Agent', link: '/tools/wx_20260524214734', category: '🤖 AI 与智能体' },
  { title: 'Vane — 本地 AI 搜索引擎', link: '/tools/wx_20260524214934', category: '🤖 AI 与智能体' },
  { title: 'OmniVoice Studio — 本地 AI 配音', link: '/tools/wx_20260530171254', category: '🤖 AI 与智能体' },
  { title: 'Next AI Draw.io — 本地 AI 交互画图', link: '/tools/wx_20260605172228', category: '🤖 AI 与智能体' },
  { title: 'VoxCPM2 — 未来语音大模型', link: '/tools/wx_20260605172524', category: '🤖 AI 与智能体' },
  { title: 'Agentic Inbox — AI 智能收件箱', link: '/tools/wx_20260605173109', category: '🤖 AI 与智能体' },
  { title: 'TuriX-CUA — 开源桌面自动化助手', link: '/tools/wx_20260605173551', category: '🤖 AI 与智能体' },
  { title: 'PilotDeck — Agent 生产力操作系统', link: '/tools/wx_20260605173728', category: '🤖 AI 与智能体' },
  { title: 'Nanobot — 港大轻量开源 Agent', link: '/tools/wx_20260605173904', category: '🤖 AI 与智能体' },
  { title: 'NVIDIA Agent Skills — AI 助手精准接管', link: '/tools/wx_20260611153942', category: '🤖 AI 与智能体' },
  { title: 'Anthropic Agent Skills — AI 定制化时代', link: '/tools/wx_20260611154756', category: '🤖 AI 与智能体' },
  { title: 'Agent Reach — 联网脚手架', link: '/tools/wx_20260611155218', category: '🤖 AI 与智能体' },
  { title: '3x-ui — Xray 协议面板', link: '/tools/3x-ui', category: '🛠️ 系统与运维' },
  { title: 'Beszel — 轻量服务器监控', link: '/tools/beszel', category: '🛠️ 系统与运维' },
  { title: 'Prometheus — 云原生监控', link: '/tools/wx_20260511214354', category: '🛠️ 系统与运维' },
  { title: 'FluentFlyout — 电池弹窗美化', link: '/tools/fluentflyout', category: '🛠️ 系统与运维' },
  { title: 'DroidDesk — 轻松部署 Linux 桌面', link: '/tools/wx_20260530171455', category: '🛠️ 系统与运维' },
  { title: 'optimizerDuck — 免费 Windows 调优神器', link: '/tools/wx_20260530171710', category: '🛠️ 系统与运维' },
  { title: 'OfficeCLI — 自动化 Office 工作流', link: '/tools/wx_20260611154651', category: '🛠️ 系统与运维' },
  { title: 'Jujutsu — 极客版本地 Git', link: '/tools/wx_20260611155310', category: '🛠️ 系统与运维' },
  { title: '2FAuth — 自托管 2FA 令牌', link: '/tools/2fauth', category: '🔒 安全与隐私' },
  { title: 'Vaultwarden — 轻量级密码库', link: '/tools/wx_20260511214924', category: '🔒 安全与隐私' },
  { title: 'Fcitx5 — 开源输入法', link: '/tools/wx_20260518005748', category: '🔒 安全与隐私' },
  { title: 'Bumblebee — 开源安全扫描工具', link: '/tools/wx_20260530171127', category: '🔒 安全与隐私' },
  { title: 'Outline — 团队 Wiki 知识库', link: '/tools/outline', category: '✍️ 知识与协作' },
  { title: 'Memos — 碎片化灵感笔记', link: '/tools/memos', category: '✍️ 知识与协作' },
  { title: 'Ghost — 开源博客系统', link: '/tools/wx_20260421130229', category: '✍️ 知识与协作' },
  { title: 'Chatwoot — 全渠道客服中台', link: '/tools/chatwoot', category: '✍️ 知识与协作' },
  { title: 'Twenty — TypeScript 开源 CRM', link: '/tools/wx_20260611154932', category: '✍️ 知识与协作' },
  { title: 'Stirling-PDF — 全能 PDF 工具箱', link: '/tools/stirling-pdf', category: '📂 实用与提效' },
  { title: 'RSSHub — 万物皆可 RSS', link: '/tools/rsshub', category: '📂 实用与提效' },
  { title: 'LocalSend — 跨平台文件传输', link: '/tools/wx_20260511215131', category: '📂 实用与提效' },
  { title: 'Open Chrome — 浏览器神器', link: '/tools/wx_20260413125458', category: '📂 实用与提效' },
  { title: 'ConvertX — 格式转换利器', link: '/tools/wx_20260429211232', category: '📂 实用与提效' },
  { title: 'CookCLI — 菜谱管理命令行', link: '/tools/cookcli', category: '📂 实用与提效' },
  { title: 'AirTranslate — Mac全局音频翻译', link: '/tools/wx_20260530171544', category: '📂 实用与提效' },
  { title: 'InvoiceShelf — 开源财务管理', link: '/tools/wx_20260511214626', category: '💰 金融与支付' },
  { title: 'Penpot — 开源设计工具', link: '/tools/penpot', category: '🎨 设计与极客' },
  { title: 'Storybook — UI 组件开发环境', link: '/tools/storybook', category: '🎨 设计与极客' },
  { title: 'V8 Engine — JS 运行引擎', link: '/tools/v8', category: '🎨 设计与极客' },
  { title: 'The Art of Command Line — 终端神技', link: '/tools/the-art-of-command-line', category: '🎨 设计与极客' },
  { title: 'MoBrowser-App-Icon-Maker — AI 图标生成', link: '/tools/wx_20260530171623', category: '🎨 设计与极客' },
  { title: 'Jellyfin — 自建私人影院', link: '/tools/jellyfin', category: '🍿 影音与娱乐' },
]

// ── 状态 ────────────────────────────────────────────────
const isOpen = ref(false)
const query = ref('')
const activeIndex = ref(0)
const searchInputRef = ref(null)
const router = useRouter()

// ── 搜索逻辑 ────────────────────────────────────────────
const results = computed(() => {
  const q = query.value.trim().toLowerCase()
  const tools = allTools.value.length ? allTools.value : INLINE_TOOLS
  if (!q) return tools.slice(0, 10)
  return tools.filter(t =>
    t.title.toLowerCase().includes(q) ||
    (t.category || '').toLowerCase().includes(q) ||
    (t.description || '').toLowerCase().includes(q)
  ).slice(0, 12)
})

// ── 打开/关闭 ────────────────────────────────────────────
const open = async () => {
  isOpen.value = true
  query.value = ''
  activeIndex.value = 0
  await nextTick()
  searchInputRef.value?.focus()
}

const close = () => {
  isOpen.value = false
  query.value = ''
}

const navigate = (link) => {
  close()
  router.go(link)
}

// ── 键盘处理 ────────────────────────────────────────────
const onKeydown = (e) => {
  if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
    e.preventDefault()
    isOpen.value ? close() : open()
    return
  }
  // 全局 / 键（非输入框内）
  if (e.key === '/' && !isOpen.value && document.activeElement?.tagName !== 'INPUT' && document.activeElement?.tagName !== 'TEXTAREA') {
    e.preventDefault()
    open()
    return
  }
  if (!isOpen.value) return
  if (e.key === 'Escape') { close(); return }
  if (e.key === 'ArrowDown') { e.preventDefault(); activeIndex.value = Math.min(activeIndex.value + 1, results.value.length - 1) }
  if (e.key === 'ArrowUp') { e.preventDefault(); activeIndex.value = Math.max(activeIndex.value - 1, 0) }
  if (e.key === 'Enter' && results.value[activeIndex.value]) {
    navigate(results.value[activeIndex.value].link)
  }
}

const onInput = () => { activeIndex.value = 0 }

onMounted(() => {
  window.addEventListener('keydown', onKeydown)
  loadTools()
})
onUnmounted(() => { window.removeEventListener('keydown', onKeydown) })

// Expose open for external trigger
defineExpose({ open })
</script>

<template>
  <!-- Trigger Button (exported as slot, but also listens globally) -->
  <button
    class="cmd-trigger"
    @click="open"
    :aria-label="'全站搜索工具 (⌘K)'"
    id="cmd-palette-trigger"
  >
    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
    <span class="cmd-trigger-text">搜索工具...</span>
    <kbd class="cmd-trigger-kbd">
      <span>⌘</span>K
    </kbd>
  </button>

  <!-- Backdrop + Modal -->
  <Teleport to="body">
    <Transition name="cmd-fade">
      <div v-if="isOpen" class="cmd-backdrop" @click.self="close">
        <div class="cmd-modal" role="dialog" aria-modal="true" aria-label="工具搜索">
          <!-- Search Input -->
          <div class="cmd-input-row">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="cmd-search-icon"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
            <input
              ref="searchInputRef"
              v-model="query"
              @input="onInput"
              @keydown="onKeydown"
              type="text"
              placeholder="搜索工具名称、分类..."
              class="cmd-input"
              autocomplete="off"
              autocorrect="off"
              spellcheck="false"
            />
            <button class="cmd-esc-btn" @click="close">ESC</button>
          </div>

          <!-- Results -->
          <div class="cmd-results-container">
            <div v-if="results.length === 0" class="cmd-empty">
              <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/><path d="M8 11h6"/></svg>
              <p>未找到相关工具</p>
              <span>尝试搜索工具名称或分类</span>
            </div>
            <ul v-else class="cmd-results-list" role="listbox">
              <li
                v-for="(tool, idx) in results"
                :key="tool.link"
                class="cmd-result-item"
                :class="{ active: idx === activeIndex }"
                @mouseenter="activeIndex = idx"
                @click="navigate(tool.link)"
                role="option"
                :aria-selected="idx === activeIndex"
              >
                <span class="result-icon">
                  <img v-if="tool.icon && tool.icon.startsWith('http')" :src="tool.icon" alt="" width="20" height="20" />
                  <span v-else class="result-emoji">{{ tool.category?.split(' ')[0] || '🛠️' }}</span>
                </span>
                <span class="result-info">
                  <span class="result-title" v-html="highlightMatch(tool.title, query)"></span>
                  <span class="result-category">{{ tool.category }}</span>
                </span>
                <svg v-if="idx === activeIndex" xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="result-enter-icon"><polyline points="9 10 4 15 9 20"/><path d="M20 4v7a4 4 0 0 1-4 4H4"/></svg>
              </li>
            </ul>
            <div class="cmd-footer">
              <span><kbd>↑↓</kbd> 导航</span>
              <span><kbd>↵</kbd> 打开</span>
              <span><kbd>ESC</kbd> 关闭</span>
            </div>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script>
// Helper: highlight matching text (plain JS, not in setup for reuse)
function highlightMatch(text, query) {
  if (!query) return text
  const escaped = query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')
  return text.replace(new RegExp(`(${escaped})`, 'gi'), '<mark>$1</mark>')
}
</script>

<style scoped>
/* ── Trigger Button ─────────────────────────────────────── */
.cmd-trigger {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.38rem 0.75rem;
  border-radius: 8px;
  border: 1px solid var(--vp-c-border);
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-2);
  font-size: 0.85rem;
  cursor: pointer;
  transition: all 0.2s ease;
  white-space: nowrap;
  min-width: 160px;
}

.cmd-trigger:hover {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-text-1);
  background: var(--vp-c-bg);
}

.cmd-trigger-text {
  flex: 1;
  text-align: left;
}

.cmd-trigger-kbd {
  display: inline-flex;
  align-items: center;
  gap: 1px;
  padding: 0.1rem 0.3rem;
  border-radius: 4px;
  border: 1px solid var(--vp-c-border);
  background: var(--vp-c-bg);
  font-size: 0.7rem;
  font-family: monospace;
  color: var(--vp-c-text-3);
  line-height: 1;
}

/* ── Backdrop ────────────────────────────────────────────── */
.cmd-backdrop {
  position: fixed;
  inset: 0;
  z-index: 9999;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding-top: 15vh;
}

/* ── Modal ───────────────────────────────────────────────── */
.cmd-modal {
  width: min(620px, 92vw);
  border-radius: 16px;
  border: 1px solid var(--vp-c-border);
  background: var(--vp-c-bg);
  box-shadow: 0 24px 80px rgba(0, 0, 0, 0.35), 0 4px 16px rgba(0, 0, 0, 0.15);
  overflow: hidden;
}

.dark .cmd-modal {
  box-shadow: 0 24px 80px rgba(0, 0, 0, 0.6), 0 4px 16px rgba(0, 0, 0, 0.3);
}

/* ── Input ───────────────────────────────────────────────── */
.cmd-input-row {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1rem 1.25rem;
  border-bottom: 1px solid var(--vp-c-border);
}

.cmd-search-icon {
  flex-shrink: 0;
  color: var(--vp-c-text-3);
}

.cmd-input {
  flex: 1;
  border: none;
  outline: none;
  background: transparent;
  font-size: 1.05rem;
  color: var(--vp-c-text-1);
  font-family: inherit;
}

.cmd-input::placeholder {
  color: var(--vp-c-text-3);
}

.cmd-esc-btn {
  padding: 0.2rem 0.5rem;
  border-radius: 6px;
  border: 1px solid var(--vp-c-border);
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-3);
  font-size: 0.72rem;
  font-family: monospace;
  cursor: pointer;
  flex-shrink: 0;
}

/* ── Results ─────────────────────────────────────────────── */
.cmd-results-container {
  max-height: 420px;
  overflow-y: auto;
}

.cmd-results-list {
  list-style: none;
  margin: 0;
  padding: 0.5rem;
}

.cmd-result-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.65rem 0.85rem;
  border-radius: 10px;
  cursor: pointer;
  transition: background 0.12s;
}

.cmd-result-item.active,
.cmd-result-item:hover {
  background: var(--vp-c-brand-soft);
}

.result-icon {
  width: 28px;
  height: 28px;
  border-radius: 6px;
  overflow: hidden;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-border);
}

.result-icon img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  margin: 0;
}

.result-emoji {
  font-size: 0.95rem;
  line-height: 1;
}

.result-info {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 0.15rem;
}

.result-title {
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--vp-c-text-1);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.result-title :deep(mark) {
  background: rgba(var(--vp-c-brand-1-rgb, 100, 108, 255), 0.2);
  color: var(--vp-c-brand-1);
  border-radius: 2px;
  padding: 0 1px;
}

.result-category {
  font-size: 0.75rem;
  color: var(--vp-c-text-3);
}

.result-enter-icon {
  flex-shrink: 0;
  color: var(--vp-c-brand-1);
}

/* ── Empty State ─────────────────────────────────────────── */
.cmd-empty {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 3rem 2rem;
  color: var(--vp-c-text-3);
  gap: 0.5rem;
}

.cmd-empty p {
  font-size: 1rem;
  font-weight: 500;
  color: var(--vp-c-text-2);
  margin: 0;
}

.cmd-empty span {
  font-size: 0.85rem;
}

/* ── Footer ──────────────────────────────────────────────── */
.cmd-footer {
  display: flex;
  gap: 1rem;
  padding: 0.6rem 1.25rem;
  border-top: 1px solid var(--vp-c-border);
  font-size: 0.75rem;
  color: var(--vp-c-text-3);
}

.cmd-footer kbd {
  display: inline-flex;
  align-items: center;
  padding: 0.1rem 0.35rem;
  border-radius: 4px;
  border: 1px solid var(--vp-c-border);
  background: var(--vp-c-bg-soft);
  font-size: 0.7rem;
  font-family: monospace;
  margin-right: 3px;
}

/* ── Transition ──────────────────────────────────────────── */
.cmd-fade-enter-active,
.cmd-fade-leave-active {
  transition: opacity 0.15s ease;
}

.cmd-fade-enter-active .cmd-modal,
.cmd-fade-leave-active .cmd-modal {
  transition: transform 0.15s ease, opacity 0.15s ease;
}

.cmd-fade-enter-from,
.cmd-fade-leave-to {
  opacity: 0;
}

.cmd-fade-enter-from .cmd-modal {
  transform: translateY(-12px) scale(0.97);
  opacity: 0;
}

.cmd-fade-leave-to .cmd-modal {
  transform: translateY(-8px) scale(0.98);
  opacity: 0;
}

/* Mobile */
@media (max-width: 768px) {
  .cmd-trigger-text {
    display: none;
  }
  .cmd-trigger-kbd {
    display: none;
  }
  .cmd-trigger {
    min-width: unset;
    padding: 0.38rem 0.5rem;
  }
  .cmd-backdrop {
    padding-top: 0;
    align-items: flex-end;
  }
  .cmd-modal {
    width: 100%;
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
    border-bottom: none;
  }
  .cmd-results-container {
    max-height: 60vh;
  }
}
</style>
