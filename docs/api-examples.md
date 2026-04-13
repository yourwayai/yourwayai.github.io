# Runtime API Examples

VitePress provides several APIs to help you access site data or control the navigation.

## siteData

The `siteData` object contains the site-level configuration data.

```vue
<script setup>
import { useData } from 'vitepress'
const { site } = useData()
</script>

<pre>{{ site }}</pre>
```

## pageData

The `pageData` object contains data for the current page.

```vue
<script setup>
import { useData } from 'useData'
const { page } = useData()
</script>

<pre>{{ page }}</pre>
```
