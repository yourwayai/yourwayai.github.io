<template>
  <footer class="site-footer">
    <div class="footer-inner">
      <!-- Brand -->
      <div class="footer-brand">
        <img src="/logo.jpg" alt="YourwayAI Logo" class="footer-logo" />
        <span class="footer-name">YourwayAI</span>
      </div>

      <!-- Tagline -->
      <p class="footer-tagline">发现优质的免费开源软件，打破信息差，拥抱开源精神。</p>

      <!-- Divider -->
      <div class="footer-divider"></div>

      <!-- Bottom Row -->
      <div class="footer-bottom">
        <span class="footer-copyright">© 2026-present YourwayAI. All rights reserved.</span>
        <a href="mailto:brucemi@yourwaycareer.com" class="footer-contact">
          <span class="contact-icon">✉️</span>
          brucemi@yourwaycareer.com
        </a>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.site-footer {
  margin-top: 3rem;
  border-top: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg-soft);
  padding: 2rem 1.5rem 1.5rem;
}

.footer-inner {
  max-width: 800px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.8rem;
  text-align: center;
}

/* Brand row */
.footer-brand {
  display: flex;
  align-items: center;
  gap: 0.6rem;
}

.footer-logo {
  width: 28px;
  height: 28px;
  border-radius: 6px;
  object-fit: cover;
}

.footer-name {
  font-size: 1rem;
  font-weight: 700;
  color: var(--vp-c-text-1);
  letter-spacing: -0.01em;
}

/* Tagline */
.footer-tagline {
  font-size: 0.82rem;
  color: var(--vp-c-text-2);
  margin: 0;
  line-height: 1.5;
}

/* Divider */
.footer-divider {
  width: 100%;
  height: 1px;
  background: var(--vp-c-divider);
  margin: 0.4rem 0;
}

/* Bottom row */
.footer-bottom {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  gap: 1.2rem;
}

.footer-copyright {
  font-size: 0.78rem;
  color: var(--vp-c-text-3);
}

.footer-contact {
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
  font-size: 0.78rem;
  color: var(--vp-c-brand-1);
  text-decoration: none;
  font-weight: 600;
  transition: opacity 0.2s;
}

.footer-contact:hover {
  opacity: 0.75;
}

.contact-icon {
  font-size: 0.85rem;
}
</style>
