<template>
  <div class="minimal-home-container">
    <header class="hero-section">
      <h1 class="hero-title">YourwayAI</h1>
      <p class="hero-tagline">发现极致优雅的重磅开源软件与极客工具</p>
      
      <!-- Fake Search Bar that opens VitePress modal -->
      <div class="hero-search-wrapper" @click="openSearch">
        <div class="hero-search-box">
          <span class="search-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          </span>
          <span class="search-placeholder">全站搜索开源工具与专栏...</span>
          <span class="search-shortcut">⌘ K</span>
        </div>
      </div>
    </header>

    <section class="core-categories-section">
      <div class="category-grid">
        <a href="/tools/outline" class="cat-card">
          <div class="cat-icon-wrapper"><span class="cat-icon">📝</span></div>
          <h3 class="cat-name">知识管理</h3>
        </a>
        <a href="/tools/chatwoot" class="cat-card">
          <div class="cat-icon-wrapper"><span class="cat-icon">💬</span></div>
          <h3 class="cat-name">沟通协作</h3>
        </a>
        <a href="/tools/jellyfin" class="cat-card">
          <div class="cat-icon-wrapper"><span class="cat-icon">🎬</span></div>
          <h3 class="cat-name">媒体与娱乐</h3>
        </a>
        <a href="/tools/the-art-of-command-line" class="cat-card">
          <div class="cat-icon-wrapper"><span class="cat-icon">👨‍💻</span></div>
          <h3 class="cat-name">开发者工具</h3>
        </a>
        <a href="/tools/wx_20260413125458" class="cat-card">
          <div class="cat-icon-wrapper"><span class="cat-icon">💡</span></div>
          <h3 class="cat-name">微信专栏</h3>
        </a>
      </div>
    </section>
  </div>
</template>

<script setup>
const openSearch = () => {
  // Try finding the native VitePress search button to trigger the modal.
  const searchBtn = document.querySelector('.VPNavBarSearch button') || document.querySelector('.DocSearch-Button');
  if (searchBtn) {
    searchBtn.click();
  }
};
</script>

<style scoped>
/* Reset and Base */
.minimal-home-container {
  min-height: calc(100vh - var(--vp-nav-height));
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 4rem 2rem 10rem;
  font-family: var(--vp-font-family-base);
  color: var(--vp-c-text-1);
}

/* Hero Section */
.hero-section {
  text-align: center;
  margin-bottom: 4rem;
  max-width: 800px;
  width: 100%;
}

.hero-title {
  font-size: 4rem;
  font-weight: 900;
  letter-spacing: -0.04em;
  margin-bottom: 1rem;
  background: linear-gradient(120deg, var(--vp-c-text-1) 0%, var(--vp-c-brand-1) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-tagline {
  font-size: 1.35rem;
  color: var(--vp-c-text-2);
  margin-bottom: 3.5rem;
  font-weight: 500;
}

/* Big Search Bar */
.hero-search-wrapper {
  max-width: 600px;
  margin: 0 auto;
  cursor: pointer;
  transition: transform 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

.hero-search-wrapper:hover {
  transform: translateY(-2px);
}

.hero-search-box {
  display: flex;
  align-items: center;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-border);
  border-radius: 20px;
  padding: 1.2rem 1.8rem;
  box-shadow: 0 10px 40px -10px rgba(0,0,0,0.08);
  transition: all 0.3s ease;
}

.hero-search-wrapper:hover .hero-search-box {
  border-color: var(--vp-c-brand-1);
  box-shadow: 0 15px 50px -10px var(--vp-c-brand-soft);
}

.search-icon {
  display: flex;
  color: var(--vp-c-text-2);
  margin-right: 1.2rem;
}

.search-placeholder {
  flex-grow: 1;
  text-align: left;
  font-size: 1.1rem;
  color: var(--vp-c-text-3);
}

.search-shortcut {
  font-size: 0.8rem;
  font-family: var(--vp-font-family-mono);
  background: var(--vp-c-bg-mute);
  padding: 0.3rem 0.6rem;
  border-radius: 6px;
  color: var(--vp-c-text-2);
  border: 1px solid var(--vp-c-border);
}

/* Core Categories Grid */
.core-categories-section {
  max-width: 1000px;
  width: 100%;
}

.category-grid {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.cat-card {
  display: flex;
  align-items: center;
  gap: 1rem;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-border);
  border-radius: 16px;
  padding: 1rem 1.5rem;
  text-decoration: none !important;
  color: inherit !important;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  min-width: 180px;
}

.cat-card:hover {
  transform: translateY(-4px);
  border-color: var(--vp-c-brand-1);
  background: var(--vp-c-bg);
  box-shadow: 0 12px 24px -10px rgba(0,0,0,0.1);
}

.cat-icon-wrapper {
  width: 40px;
  height: 40px;
  border-radius: 10px;
  background: var(--vp-c-bg-mute);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  transition: background 0.3s;
}

.cat-card:hover .cat-icon-wrapper {
  background: var(--vp-c-brand-soft);
}

.cat-name {
  margin: 0;
  font-size: 1.05rem;
  font-weight: 600;
  color: var(--vp-c-text-1);
}

/* Responsive tweaks */
@media (max-width: 768px) {
  .hero-title {
    font-size: 2.5rem;
  }
  .hero-tagline {
    font-size: 1.1rem;
    margin-bottom: 2.5rem;
  }
  .hero-search-box {
    padding: 1rem 1.2rem;
  }
  .search-placeholder {
    font-size: 1rem;
  }
  .cat-card {
    min-width: calc(50% - 0.75rem);
    padding: 0.8rem 1rem;
  }
}

@media (max-width: 480px) {
  .cat-card {
    min-width: 100%;
  }
  .search-shortcut {
    display: none;
  }
}
</style>
