const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const BASE_URL = 'https://yourwayai.github.io';
const DOCS_DIR = path.resolve(__dirname, '../docs');
const TOOLS_DIR = path.join(DOCS_DIR, 'tools');
const PUBLIC_DIR = path.join(DOCS_DIR, 'public');

// Helper to parse frontmatter from markdown
function parseFrontmatter(filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    const match = content.match(/^---\r?\n([\s\S]*?)\r?\n---/);
    if (!match) return {};
    
    const fmText = match[1];
    const fm = {};
    const lines = fmText.split('\n');
    for (let line of lines) {
      const parts = line.split(':');
      if (parts.length >= 2) {
        const key = parts[0].trim();
        const value = parts.slice(1).join(':').trim().replace(/^['"]|['"]$/g, '');
        fm[key] = value;
      }
    }
    return fm;
  } catch (e) {
    console.error(`Error parsing frontmatter for ${filePath}:`, e);
    return {};
  }
}

// Helper to get last modified date of a file (YYYY-MM-DD)
function getFileLastmod(filePath) {
  // Try git log first
  try {
    const gitDate = execSync(`git log -1 --format=%cd --date=short "${filePath}"`, { encoding: 'utf-8' }).trim();
    if (gitDate && /^[0-9]{4}-[0-9]{2}-[0-9]{2}$/.test(gitDate)) {
      return gitDate;
    }
  } catch (e) {
    // Git might not be available on CI or not tracked yet
  }
  
  // Try to parse date from frontmatter
  try {
    const fm = parseFrontmatter(filePath);
    if (fm.date) {
      const d = new Date(fm.date);
      if (!isNaN(d.getTime())) {
        return d.toISOString().split('T')[0];
      }
    }
  } catch (e) {}

  // Fallback to file system mtime
  try {
    const stat = fs.statSync(filePath);
    return stat.mtime.toISOString().split('T')[0];
  } catch (e) {}

  return new Date().toISOString().split('T')[0];
}

// Main logic
function main() {
  console.log('Generating Sitemap and Projects index...');

  const sitemapEntries = [];
  const toolsList = [];

  // 1. Process main markdown files in docs/
  const mainFiles = fs.readdirSync(DOCS_DIR);
  for (const file of mainFiles) {
    const filePath = path.join(DOCS_DIR, file);
    const stat = fs.statSync(filePath);
    
    if (stat.isFile() && file.endsWith('.md')) {
      const relativeRoute = file === 'index.md' ? '' : file.replace(/\.md$/, '.html');
      const url = `${BASE_URL}/${relativeRoute}`;
      const lastmod = getFileLastmod(filePath);
      sitemapEntries.push({ url, lastmod });
    }
  }

  // 2. Process tools in docs/tools/
  if (fs.existsSync(TOOLS_DIR)) {
    const toolFiles = fs.readdirSync(TOOLS_DIR);
    for (const file of toolFiles) {
      if (file.endsWith('.md')) {
        const filePath = path.join(TOOLS_DIR, file);
        const lastmod = getFileLastmod(filePath);
        const url = `${BASE_URL}/tools/${file.replace(/\.md$/, '.html')}`;
        sitemapEntries.push({ url, lastmod });

        // Parse meta for catalog
        const fm = parseFrontmatter(filePath);
        toolsList.push({
          filename: file,
          title: fm.title || file.replace(/\.md$/, ''),
          shortTitle: fm.short_title || fm.title || file.replace(/\.md$/, ''),
          description: fm.description || '',
          category: fm.category || '未分类',
          date: fm.date || lastmod,
          link: `/tools/${file.replace(/\.md$/, '.html')}`
        });
      }
    }
  }

  // 3. Process static HTML files in docs/public/
  if (fs.existsSync(PUBLIC_DIR)) {
    const publicFiles = fs.readdirSync(PUBLIC_DIR);
    for (const file of publicFiles) {
      if (file.endsWith('.html')) {
        // Exclude sitemap.xml if generated in public directory (it's XML anyway, but safety check)
        if (file.endsWith('.xml')) continue;
        const filePath = path.join(PUBLIC_DIR, file);
        const lastmod = getFileLastmod(filePath);
        const url = `${BASE_URL}/${file}`;
        sitemapEntries.push({ url, lastmod });
      }
    }
  }

  // 4. Write sitemap.xml
  let sitemapXml = '<?xml version="1.0" encoding="UTF-8"?>\n';
  sitemapXml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n';
  for (const entry of sitemapEntries) {
    sitemapXml += '  <url>\n';
    sitemapXml += `    <loc>${entry.url}</loc>\n`;
    sitemapXml += `    <lastmod>${entry.lastmod}</lastmod>\n`;
    sitemapXml += '  </url>\n';
  }
  sitemapXml += '</urlset>\n';

  const sitemapDest = path.join(PUBLIC_DIR, 'sitemap.xml');
  fs.mkdirSync(PUBLIC_DIR, { recursive: true });
  fs.writeFileSync(sitemapDest, sitemapXml, 'utf-8');
  console.log(`Generated sitemap.xml at ${sitemapDest} with ${sitemapEntries.length} pages.`);

  // 5. Generate docs/projects.md catalog
  // Group by category in a predefined order
  const categoryOrder = [
    '🤖 AI 与智能体',
    '🛠️ 系统与运维',
    '🔒 安全与隐私',
    '✍️ 知识与协作',
    '📂 实用与提效',
    '💰 金融与支付',
    '🎨 设计与极客',
    '🍿 影音与娱乐'
  ];

  // Group tools by category
  const groupedTools = {};
  for (const tool of toolsList) {
    const cat = tool.category;
    if (!groupedTools[cat]) {
      groupedTools[cat] = [];
    }
    groupedTools[cat].push(tool);
  }

  // Sort tools within each category by date descending
  for (const cat in groupedTools) {
    groupedTools[cat].sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());
  }

  // Build markdown content for projects.md
  let projectsMd = `---
title: 所有开源项目与工具目录
description: YourwayAI 收录的所有优质开源项目、极客工具与技术文章完整列表，助您快速发现好用的自托管方案。
---

# 所有开源项目与工具目录

本页面是 YourwayAI 收录的所有优质开源项目、自托管软件以及微信公众号技术专栏文章的完整分类目录，方便搜索引擎建立索引与用户快速索引。

---

`;

  // Append tools grouped by ordered categories
  const allCategories = Array.from(new Set([...categoryOrder, ...Object.keys(groupedTools)]));
  for (const cat of allCategories) {
    const tools = groupedTools[cat];
    if (tools && tools.length > 0) {
      projectsMd += `## ${cat} (${tools.length})\n\n`;
      for (const tool of tools) {
        // Build a nice descriptive list item
        const displayTitle = tool.shortTitle || tool.title;
        projectsMd += `- [**${displayTitle}**](${tool.link})：${tool.description}\n`;
      }
      projectsMd += '\n';
    }
  }

  const projectsDest = path.join(DOCS_DIR, 'projects.md');
  fs.writeFileSync(projectsDest, projectsMd, 'utf-8');
  console.log(`Generated projects.md catalog at ${projectsDest} with ${toolsList.length} tools.`);
}

main();
