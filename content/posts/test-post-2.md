---
title: "测试文章 2：GitHub Actions 自动部署"
date: 2026-04-20T16:30:00+08:00
draft: false
---

# GitHub Actions 自动部署 Hugo 博客

这是我的第二篇测试文章，介绍如何使用 GitHub Actions 自动部署 Hugo 博客。

## 什么是 GitHub Actions？

GitHub Actions 是 GitHub 提供的持续集成和持续部署（CI/CD）服务，允许你在代码仓库中自动化各种工作流程。

## 为什么使用 GitHub Actions 部署 Hugo 博客？

1. **自动化**：每次推送代码时自动构建和部署
2. **免费**：GitHub Pages 是免费的，GitHub Actions 也有免费额度
3. **可靠**：GitHub 提供稳定的基础设施
4. **可定制**：可以根据需要定制部署流程

## 配置 GitHub Actions 部署

### 1. 创建工作流文件

在 `.github/workflows/` 目录下创建 `gh-pages.yml` 文件，内容如下：

```yaml
name: Deploy Hugo site to Pages

on:
  push:
    branches:
      - main
      - master
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: true

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    env:
      FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          submodules: true
          fetch-depth: 0

      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: 'latest'
          extended: true

      - name: Build
        run: hugo --minify

      - name: Setup Pages
        uses: actions/configure-pages@v5

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./public

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

### 2. 启用 GitHub Pages

在 GitHub 仓库设置中：

1. 访问 Settings > Pages
2. 在 Source 中选择 "GitHub Actions"
3. 保存设置

### 3. 推送代码

每次推送到 `master` 或 `main` 分支时，GitHub Actions 会自动触发部署。

## 部署状态

- 部署过程可以在 GitHub 仓库的 Actions 标签页查看
- 部署完成后，博客会自动发布到 `https://<username>.github.io/<repository>/`

## 常见问题

- **部署失败**：检查 GitHub Pages 是否启用
- **构建错误**：检查 Hugo 版本和主题兼容性
- **访问权限**：确保仓库设置正确

希望这篇文章对你有所帮助！