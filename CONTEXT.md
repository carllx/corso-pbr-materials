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
- **参考版本与教学运行版本关系 (Reference Version ≠ Teaching Runtime Version)**：
  - 教学运行时基准以稳定、现代的 LTS 环境为目标（当前目标为 **Blender 5.2 LTS**）；
  - 成熟的早期权威教学资料（如 4.2/4.5 时代参考）仍可按需选择性复用；
  - 仅实际采纳的教学段落需要在目标教学运行时下完成有界的版本差量核实（Version-delta validation），避免因软件小版本迭代而无谓全盘推翻成熟教学沉淀。

## 领域模型与核心术语 (Glossary)

- **Course Knowledge Notebook**:
  服务于《三维数字材质制作》课程领域知识研究的外部知识库环境（Locator: `e29f9644-03b2-4e1b-bcb0-b954b5bf08be`），涵盖 PBR 理论、材质与着色器制作管线、教材与官方技术文档。

- **AI Creative Workflow Notebook**:
  跨课程共享的外部 AI 创作与生产工作流研究空间（Locator: `20a99ba1-092f-40fe-9317-8c7475f15d96`），涵盖游戏、动画、3D 与材质等方向的 AI 模型、工具与实际生产工作流。

- **Diffuse Reflection vs Specular Reflection (漫反射 vs 镜面反射)**:
  - **Diffuse Reflection (漫反射)**：光线穿透表面进入介质内部，经多次微观折射散射后重新穿出表面形成的光学反射现象，呈现材质漫反射颜色；纯金属会完全吸收折射光转化为热能，因而无漫反射分量；
  - **Specular Reflection (镜面反射)**：光线在物体表面微平面直接发生的方向性反射；
  - **Specular Highlight (镜面高光)**：光源照射下由镜面反射产生的动态高光波瓣视觉表现，随视线与光源动态交互，绝非画在贴图里的死颜色，亦非默认独立贴图通道。

- **Base Color vs Diffuse Map vs Albedo Map (基底色 vs 漫反射贴图 vs 反照率贴图)**:
  - **Base Color (基底色)**：Metallic/Roughness 工作流核心贴图。对绝缘体 (`Metallic=0`) 记录漫反射颜色；对纯金属 (`Metallic=1`) 记录其法向镜面反射率 ($F_0$)；严格剔除烘焙光影与 AO；
  - **Albedo Map (反照率贴图)**：物理光学中表面纯净固有反射率的度量贴图，严格剔除所有定向光照、高光与阴影信息；
  - **Diffuse Map (漫反射贴图)**：常用于传统光照模型或 Specular/Glossiness 工作流（在 Specular/Glossiness 中纯金属的 Diffuse 设为纯黑）；传统资产中的 Diffuse 贴图往往混有烘焙阴影与脏污。三者数据组织与物理定义截然不同，严禁作为无条件同义词混用。

- **Material Channel vs Texture Map vs Layer vs Mask (材质通道 vs 纹理贴图 vs 图层 vs 遮罩)**:
  - **Material Channel (材质通道)**：着色器或材质系统内的数据输入插槽（如 Base Color、Roughness、Metallic、Normal 等）；
  - **Texture Map (纹理贴图)**：存储在磁盘或显存中的二维位图文件（如 `.png`、`.exr`），可映射至一个或多个通道（或经 Channel Packing 通道打包组装）；
  - **Layer (图层)**：分层材质绘制软件（如 Substance 3D Painter）中的合成逻辑单元（如 Fill Layer、Paint Layer），可同时包含并驱动多个材质通道；
  - **Mask (遮罩)**：单通道标量灰度数据，用于定义图层或效果在模型表面的空间可见度与插值混合权重（如 Black Mask、White Mask），本身属于图层控制属性而非着色器材质通道。

## 架构决策与设计原则

- 决策记录参见 `docs/adr/`（如需创建）。
- 本项目遵循单上下文模型（Single-context layout）。
- 详细知识架构见 `docs/research/knowledge-architecture.md`，设计台账见 `docs/research/course-design-ledger.md`，外部能力见 `docs/agents/capabilities.md`。

## 决策权威与人机协作边界 (Course Owner & Agent Decision Authority Boundary)

- **Course Owner / 教师人类决策权威 (Human Decision Authority)**：
  - 拥有课程培养目标、9 周大纲架构、实操深度、作业练习体系、平时/期末考核评价框架以及所有里程碑门禁（Review / Exit / Gating）的最终裁决与冻结权；
  - 任何教学方案的正式采纳、范围基线调整或门禁放行，必须经由 Course Owner 显式确认。
- **Agent / 智能体工程协作边界 (Agent Boundary)**：
  - 负责在既定授权与约束内执行一手实证调研、软件运行时技术切片验证、可执行教学资产包与自动化脚本构建、以及有界文本修订（Bounded Corrections）；
  - 严禁擅自冻结未经人类批准的考核比例、评分标准或跨周架构重排；
  - 严禁在未获人类授权的情况下私自关闭门禁 Issue 或解锁下游阻断任务。
