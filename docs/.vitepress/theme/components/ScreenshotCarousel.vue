<script setup>
const props = defineProps({
  screenshots: {
    type: Array,
    default: () => []
  },
  title: {
    type: String,
    default: ''
  }
})
</script>

<template>
  <div v-if="screenshots && screenshots.length > 0" class="screenshot-carousel-wrapper">
    <div class="screenshot-carousel-label">
      <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M3 9h18"/><path d="m9 16 3-3 3 3"/></svg>
      界面预览 <span class="count-badge">{{ screenshots.length }}</span>
    </div>
    <div class="screenshot-scroll-container">
      <div class="screenshot-track">
        <figure
          v-for="(src, idx) in screenshots"
          :key="idx"
          class="screenshot-item"
        >
          <img
            :src="src"
            :alt="`${title} 截图 ${idx + 1}`"
            loading="lazy"
            decoding="async"
          />
        </figure>
      </div>
    </div>
    <p class="carousel-hint">← 左右滑动查看更多 →</p>
  </div>
</template>

<style scoped>
.screenshot-carousel-wrapper {
  margin: 1.8rem 0 2rem;
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid var(--vp-c-border);
  background: var(--vp-c-bg-soft);
}

.screenshot-carousel-label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.65rem 1rem;
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--vp-c-text-2);
  border-bottom: 1px solid var(--vp-c-border);
  background: var(--vp-c-bg);
  letter-spacing: 0.02em;
}

.count-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
  border-radius: 99px;
  padding: 0 0.4rem;
  font-size: 0.75rem;
  font-weight: 700;
  min-width: 1.4rem;
  height: 1.4rem;
}

.screenshot-scroll-container {
  overflow-x: auto;
  overflow-y: hidden;
  scroll-snap-type: x mandatory;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: thin;
  scrollbar-color: var(--vp-c-border) transparent;
  cursor: grab;
}

.screenshot-scroll-container:active {
  cursor: grabbing;
}

.screenshot-scroll-container::-webkit-scrollbar {
  height: 4px;
}

.screenshot-scroll-container::-webkit-scrollbar-track {
  background: transparent;
}

.screenshot-scroll-container::-webkit-scrollbar-thumb {
  background: var(--vp-c-border);
  border-radius: 4px;
}

.screenshot-track {
  display: flex;
  gap: 0;
  width: max-content;
}

.screenshot-item {
  flex: 0 0 auto;
  scroll-snap-align: start;
  margin: 0;
  padding: 0;
  width: min(720px, 90vw);
  background: var(--vp-c-bg-soft);
  border-right: 1px solid var(--vp-c-border);
}

.screenshot-item:last-child {
  border-right: none;
}

.screenshot-item img {
  width: 100%;
  height: auto;
  max-height: 420px;
  object-fit: cover;
  object-position: top;
  display: block;
  margin: 0;
  border-radius: 0;
}

.carousel-hint {
  text-align: center;
  font-size: 0.75rem;
  color: var(--vp-c-text-3);
  padding: 0.4rem 0;
  margin: 0;
  background: var(--vp-c-bg);
  border-top: 1px solid var(--vp-c-border);
  letter-spacing: 0.05em;
}

@media (max-width: 768px) {
  .screenshot-item {
    width: 85vw;
  }
  .screenshot-item img {
    max-height: 240px;
  }
}
</style>
