# External Knowledge Capabilities

本项目接入以下两个外部知识库（External Knowledge Repositories / Notebooks），作为外部研究与知识能力（External Research & Knowledge Capability），用于 source discovery、检索（retrieval）、方案对比（comparison）与知识综合（synthesis）。外部能力的输出本身不自动成为项目权威，需经教学与课程设计审核后方可沉淀入库：

## 1. Course Knowledge Notebook

- **Provider**: Gemini NotebookLM
- **Role / Scope**: 服务于《三维数字材质制作》课程自身的领域知识研究，包括但不限于：
  - PBR 基础理论
  - 游戏材质制作
  - UV
  - Baking
  - Texture / Material / Shader
  - Blender
  - Substance Painter
  - Substance Designer
  - Unreal / Unity
  - 国内外权威教材
  - 成熟课程、官方文档与教学资料
- **Locator**: `e29f9644-03b2-4e1b-bcb0-b954b5bf08be`
- **URL**: `https://notebook.google.com/notebook/e29f9644-03b2-4e1b-bcb0-b954b5bf08be`
- **Boundary Note**: 这是课程自身的领域知识库，聚焦于三维数字材质与贴图制作的理论、标准工作流与工具链，不应被定义成 AI-native Game Art Notebook。

## 2. AI Creative Workflow Notebook

- **Provider**: Gemini NotebookLM
- **Role / Scope**: 跨多个课程共享的外部 AI 创作工作流研究空间（Shared External AI Creative Production & Workflow Research Space），包括但不限于：
  - AI Game Art
  - AI Animation / Film
  - AI Character / Visual Development
  - AI 3D
  - AI Material / Texture
  - AI Video
  - 创作者与实际 production workflow
  - 新模型、新工具及工作方法
- **Locator**: `20a99ba1-092f-40fe-9317-8c7475f15d96`
- **URL**: `https://notebook.google.com/notebook/20a99ba1-092f-40fe-9317-8c7475f15d96`
- **Splitting Policy**: 目前不进一步拆分成 AI Game Notebook 与 AI Animation Notebook。仅在未来出现以下真实问题时重新评估拆分：
  1. 两个领域来源高度分化；
  2. 检索噪声明显影响研究；
  3. 游戏和动画已经形成各自稳定、独立的方法体系。

## 3. 知识边界与凭据约束

- **权威性界定**：NotebookLM 是研究与检索环境，不是项目最终事实权威（Project Authority）。被项目采纳的重要研究结论、课程判断与设计决定，应沉淀回 repository。
- **资料独立性**：两个 Notebook 职责分明，不要求复制相同材料。
- **安全与凭据**：严禁在代码仓库中保存任何 NotebookLM cookie、token、storage state 或其他身份凭据。
