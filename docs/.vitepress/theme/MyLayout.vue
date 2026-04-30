<script setup>
import DefaultTheme from 'vitepress/theme'
import ScrollToTopBottom from './components/ScrollToTopBottom.vue'

const { Layout } = DefaultTheme
</script>

<template>
  <Layout>
    <template #layout-bottom>
      <ScrollToTopBottom />
    </template>
  </Layout>
</template>
