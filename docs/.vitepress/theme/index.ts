import DefaultTheme from 'vitepress/theme'
import './style.css'
import HomeShowcase from './components/HomeShowcase.vue'
import MyLayout from './MyLayout.vue'

export default {
  extends: DefaultTheme,
  Layout: MyLayout,
  enhanceApp({ app, router, siteData }) {
    app.component('HomeShowcase', HomeShowcase)
  }
}
