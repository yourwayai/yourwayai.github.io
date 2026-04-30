<template>
  <div class="scroll-widget" :class="{ 'is-visible': isVisible }">
    <button @click="scrollToTop" class="scroll-btn" title="回到顶部">
      <svg viewBox="0 0 24 24" class="icon"><path fill="currentColor" d="M7.41 15.41L12 10.83l4.59 4.58L18 14l-6-6-6 6z"></path></svg>
    </button>
    <button @click="scrollToBottom" class="scroll-btn" title="直达底部">
      <svg viewBox="0 0 24 24" class="icon"><path fill="currentColor" d="M7.41 8.59L12 13.17l4.59-4.58L18 10l-6 6-6-6 1.41-1.41z"></path></svg>
    </button>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const isVisible = ref(false)

const checkScroll = () => {
  // Show widget if scrolled down slightly (e.g., 200px)
  isVisible.value = window.scrollY > 200
}

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  })
}

const scrollToBottom = () => {
  window.scrollTo({
    top: document.documentElement.scrollHeight,
    behavior: 'smooth'
  })
}

onMounted(() => {
  window.addEventListener('scroll', checkScroll)
  checkScroll()
})

onUnmounted(() => {
  window.removeEventListener('scroll', checkScroll)
})
</script>

<style scoped>
.scroll-widget {
  position: fixed;
  right: 2rem;
  bottom: 2rem;
  display: flex;
  flex-direction: column;
  gap: 10px;
  z-index: 100;
  opacity: 0;
  transform: translateY(20px);
  pointer-events: none;
  transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.scroll-widget.is-visible {
  opacity: 1;
  transform: translateY(0);
  pointer-events: auto;
}

.scroll-btn {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-border);
  color: var(--vp-c-text-2);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  /* Premium glassmorphism effect */
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
  padding: 0;
}

/* Dark mode tweaks */
:root.dark .scroll-btn {
  background: rgba(30, 30, 30, 0.8);
  border-color: rgba(255, 255, 255, 0.1);
}

.scroll-btn:hover {
  background: var(--vp-c-brand-1);
  color: white;
  border-color: var(--vp-c-brand-1);
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
}

.icon {
  width: 24px;
  height: 24px;
}

@media (max-width: 768px) {
  .scroll-widget {
    right: 1rem;
    bottom: 1rem;
  }
}
</style>
