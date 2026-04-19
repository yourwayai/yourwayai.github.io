import DefaultTheme from 'vitepress/theme'
import './style.css'
import HomeShowcase from './components/HomeShowcase.vue'

export default {
  extends: DefaultTheme,
  enhanceApp({ app, router, siteData }) {
    app.component('HomeShowcase', HomeShowcase)
  }
}
