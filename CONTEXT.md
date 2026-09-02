# CONTEXT: 三维数字材质制作 (corso-pbr-materials)

## 课程定位与核心原则 (Course Positioning & Principles)

- **核心对象**：课程核心聚焦于 **材质与纹理创作 (Material / Texture Authoring)**，而非完整的次世代游戏资产制作全流程。
- **支撑知识边界**：建模（Modeling）、拓扑重构（Retopology）、高低模（High/Low Poly）、UV 展开与贴图烘焙（Baking）等属于材质制作的支撑性前置知识；教学深度以“足以理解并支撑材质与纹理工作流”为准，严防反客为主成为课程主体。
- **研究与设计依据**：课程设计必须基于可核查的权威教材目录、官方教学体系、成熟行业课程及最新生产工作流进行实证构建，严禁由 Agent 脱离事实凭空臆造课程结构。
- **三种核心材质创作范式 (Authoring Paradigms)**：
  1. 基于贴图的 PBR 材质工作流（Texture-based / PBR materials）；
  2. 程序化与参数化材质工作流（Procedural / Parametric materials）；
  3. AI 辅助与生成式材质工作流（AI-assisted / Generative material workflows）。
- **应用出口定位**：实时游戏（Game Realtime）与动画/视觉开发（Animation / LookDev）是材质创作能力的两个下游应用出口，而非割裂的两门独立课程。

## 领域模型与核心术语 (Glossary)

- **Course Knowledge Notebook**:
  服务于《三维数字材质制作》课程领域知识研究的外部知识库环境（Locator: `e29f9644-03b2-4e1b-bcb0-b954b5bf08be`），涵盖 PBR 理论、材质与着色器制作管线、教材与官方技术文档。

- **AI Creative Workflow Notebook**:
  跨课程共享的外部 AI 创作与生产工作流研究空间（Locator: `20a99ba1-092f-40fe-9317-8c7475f15d96`），涵盖游戏、动画、3D 与材质等方向的 AI 模型、工具与实际生产工作流。

## 架构决策与设计原则

- 决策记录参见 `docs/adr/`（如需创建）。
- 本项目遵循单上下文模型（Single-context layout）。
- 详细知识架构见 `docs/research/knowledge-architecture.md`，设计台账见 `docs/research/course-design-ledger.md`，外部能力见 `docs/agents/capabilities.md`。
