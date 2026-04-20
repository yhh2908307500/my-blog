# 个人博客系统搭建指南

本指南详细介绍如何使用 Hugo + GitHub Pages 搭建个人博客系统，使用 hugo-book 主题。

## 1. 环境准备

### 1.1 安装 Hugo

**Ubuntu/Debian 系统：**
```bash
sudo apt update && sudo apt install -y hugo
```

**macOS 系统：**
```bash
brew install hugo
```

**Windows 系统：**
1. 访问 [Hugo 官方下载页](https://github.com/gohugoio/hugo/releases)
2. 下载对应版本的可执行文件
3. 将可执行文件添加到系统 PATH 中

### 1.2 验证安装

```bash
hugo version
```

## 2. 项目初始化

### 2.1 创建项目目录

```bash
mkdir my-blog && cd my-blog
```

### 2.2 初始化 Hugo 项目

```bash
hugo new site . --force
```

## 3. 主题安装与配置

### 3.1 安装 hugo-book 主题

```bash
git clone https://github.com/alex-shpak/hugo-book themes/hugo-book
```

### 3.2 配置主题

编辑 `config.toml` 文件：

```toml
baseURL = "https://yhh2908307500.github.io/my-blog/"
languageCode = "zh-cn"
title = "我的博客"
theme = "hugo-book"

[params]
  # Book theme configuration
  BookTheme = "auto"
  BookToc = true
  BookSearch = true
  BookLogo = ""
  BookPageNav = true
  BookRepo = "https://github.com/yhh2908307500/my-blog"
  BookEditPath = ""
```

## 4. 内容创建

### 4.1 创建首页内容

创建 `content/_index.md` 文件：

```markdown
---
title: "首页"
---

# 欢迎来到我的博客

这是一个基于 Hugo + GitHub Pages 搭建的博客系统，使用 hugo-book 主题。

## 关于本博客

- **主题**: hugo-book
- **部署平台**: GitHub Pages
- **源码地址**: [GitHub](https://github.com/yhh2908307500/my-blog)

## 博客内容

- 技术分享
- 学习笔记
- 生活记录
```

### 4.2 创建文档目录

```bash
mkdir -p content/docs
```

创建 `content/docs/_index.md` 文件：

```markdown
---
title: "文档"
---

# 文档目录

这里存放博客的技术文档和学习笔记。
```

### 4.3 创建博客文章

创建 `content/docs/first-post.md` 文件：

```markdown
---
title: "第一篇博客"
date: 2026-04-20
draft: false
---

# 我的第一篇博客

这是我使用 Hugo + GitHub Pages 搭建博客后的第一篇文章。

## 搭建过程

1. 初始化 Hugo 项目
2. 安装 hugo-book 主题
3. 配置 GitHub Pages 部署
4. 发布第一篇文章

## 技术栈

- **静态站点生成器**: Hugo
- **主题**: hugo-book
- **部署平台**: GitHub Pages

希望这个博客能够记录我的学习和成长历程！
```

## 5. GitHub Pages 部署配置

### 5.1 初始化 Git 仓库

```bash
git init
git remote add origin git@github.com:yhh2908307500/my-blog.git
```

### 5.2 创建 .gitignore 文件

```bash
cat > .gitignore << 'EOF'
# Hugo generated files
public/
resources/_gen/

# OS generated files
.DS_Store
Thumbs.db

# IDE files
.vscode/
.idea/

# Other
node_modules/
.env
EOF
```

### 5.3 配置 GitHub Actions

创建 `.github/workflows/deploy.yml` 文件：

```yaml
name: Deploy Hugo site to GitHub Pages

on:
  push:
    branches:
      - master
  workflow_dispatch:

permissions:
  contents: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          submodules: true  # Fetch Hugo themes (true OR recursive)
          fetch-depth: 0    # Fetch all history for .GitInfo and .Lastmod

      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: 'latest'
          extended: true

      - name: Build
        run: hugo --minify

      - name: Deploy
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./public
```

### 5.4 推送代码到 GitHub

```bash
git add .
git commit -m "初始化博客系统"
git push -u origin master
```

### 5.5 配置 GitHub Pages

1. 登录 GitHub，进入仓库 `yhh2908307500/my-blog`
2. 点击 "Settings" -> "Pages"
3. 在 "Source" 部分，选择 "Deploy from a branch"
4. 在 "Branch" 部分，选择 "gh-pages" 分支，点击 "Save"

## 6. 本地开发与预览

### 6.1 启动本地服务器

```bash
hugo server -D
```

### 6.2 访问本地预览

打开浏览器，访问 `http://localhost:1313/my-blog/`

## 7. 日常使用

### 7.1 创建新文章

```bash
hugo new docs/new-post.md
```

### 7.2 构建项目

```bash
hugo --minify
```

### 7.3 部署更新

```bash
git add .
git commit -m "更新内容"
git push origin master
```

## 8. 主题配置

### 8.1 基本配置

在 `config.toml` 文件中，可以修改以下配置：

- `title`: 博客标题
- `baseURL`: 博客访问地址
- `languageCode`: 语言代码
- `theme`: 主题名称

### 8.2 主题特定配置

在 `[params]` 部分，可以修改：

- `BookTheme`: 主题风格（auto, light, dark）
- `BookToc`: 是否显示目录
- `BookSearch`: 是否启用搜索
- `BookLogo`: 网站 Logo
- `BookPageNav`: 是否显示页面导航
- `BookRepo`: GitHub 仓库地址

## 9. 常见问题与解决方案

### 9.1 部署失败

**问题**: GitHub Actions 部署失败

**解决方案**:
1. 检查仓库权限设置
2. 确认 `config.toml` 中的 `baseURL` 配置正确
3. 检查 GitHub Pages 配置是否正确

### 9.2 主题样式问题

**问题**: 主题样式不显示

**解决方案**:
1. 确保主题已正确安装
2. 检查 `config.toml` 中的 `theme` 配置
3. 尝试重新构建项目

### 9.3 本地预览问题

**问题**: 本地预览访问 404

**解决方案**:
1. 确保本地服务器正在运行
2. 检查访问地址是否正确
3. 确认内容文件已创建

## 10. 进阶配置

### 10.1 自定义样式

在 `static/css` 目录创建自定义 CSS 文件，然后在 `layouts/partials/head.html` 中引入。

### 10.2 添加导航菜单

在 `config.toml` 文件中添加：

```toml
[[menu.main]]
  name = "首页"
  url = "/"
  weight = 1

[[menu.main]]
  name = "文档"
  url = "/docs/"
  weight = 2
```

### 10.3 集成评论系统

可以集成 Disqus、Utterances 等评论系统，具体配置参考各评论系统的文档。

## 11. 总结

通过本指南，你已经成功搭建了一个基于 Hugo + GitHub Pages 的个人博客系统，使用 hugo-book 主题。现在你可以开始创作和分享你的内容了！

---

**博客地址**: https://yhh2908307500.github.io/my-blog/
**源码地址**: https://github.com/yhh2908307500/my-blog
