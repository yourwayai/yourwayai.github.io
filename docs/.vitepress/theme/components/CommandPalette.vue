<script setup>
import { ref, computed, onMounted, onUnmounted, nextTick } from 'vue'
import { useRouter, useData } from 'vitepress'

// ── 工具数据 ──────────────────────────────────────────────
// VitePress srcDir 为 docs/，因此 glob 路径必须以 /tools/ 开头
const modules = import.meta.glob('/tools/*.md', { eager: true })

const allTools = Object.entries(modules)
  .map(([path, mod]) => {
    const fm = mod.default?.__pageData?.frontmatter || mod.__pageData?.frontmatter || {}
    const slug = path.replace('/tools/', '').replace(/\.md$/, '')
    const rawTitle = fm.title || slug
    const displayTitle = fm.short_title || rawTitle
    return {
      title: displayTitle,
      fullTitle: rawTitle,
      description: fm.description || '',
      category: fm.category || '',
      icon: fm.icon || '',
      stars: fm.stars || '',
      date: fm.date || '2000-01-01',
      link: `/tools/${slug}`,
    }
  })
  .sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime())

// ── 状态 ────────────────────────────────────────────────
const isOpen = ref(false)
const query = ref('')
const activeIndex = ref(0)
const searchInputRef = ref(null)
const router = useRouter()
const { page } = useData()

// ── 搜索逻辑 ────────────────────────────────────────────
const results = computed(() => {
  const q = query.value.trim().toLowerCase()
  if (!q) return allTools.slice(0, 10)
  return allTools.filter(t =>
    t.title.toLowerCase().includes(q) ||
    t.fullTitle.toLowerCase().includes(q) ||
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
  if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
    e.preventDefault()
    isOpen.value ? close() : open()
    return
  }
  // 全局 / 键（仅在非首页且非输入框内触发，避免与首页页内过滤框冲突）
  if (
    e.key === '/' &&
    !isOpen.value &&
    page.value.relativePath !== 'index.md' &&
    document.activeElement?.tagName !== 'INPUT' &&
    document.activeElement?.tagName !== 'TEXTAREA'
  ) {
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
// Helper: highlight matching text safely (escape HTML first)
function escapeHtml(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
}

function highlightMatch(text, query) {
  const safeText = escapeHtml(text)
  if (!query) return safeText
  const escaped = escapeHtml(query).replace(/[.*+?^${}()|[\]\\]/g, '\\$&')
  return safeText.replace(new RegExp(`(${escaped})`, 'gi'), '<mark>$1</mark>')
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
