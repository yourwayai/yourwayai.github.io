import DefaultTheme from 'vitepress/theme'
import './style.css'
import HomeShowcase from './components/HomeShowcase.vue'
import GithubRepoCard from './components/GithubRepoCard.vue'
import MyLayout from './MyLayout.vue'

export default {
  extends: DefaultTheme,
  Layout: MyLayout,
  enhanceApp({ app, router, siteData }) {
    app.component('HomeShowcase', HomeShowcase)
    app.component('GithubRepoCard', GithubRepoCard)
  }
}
