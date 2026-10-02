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

## 3. 能力调用与执行元数据规范 (Execution Metadata & Operating Boundaries)

依据 Issue #13 流程复盘与实机验证结果，对外部 NotebookLM 能力的操作集成与调用边界确立如下规范：

- **Known Host & Execution Placement (已知宿主与环境配置)**：
  - 支持在已配置 Google 授权的 macOS 本地开发环境中运行；
  - 依赖本地 CLI 路径：`/Users/yamlam/.local/bin/notebooklm`，依托用户配置目录 `~/.notebooklm/profiles/default/storage_state.json` 的安全会话缓存。
- **Access Hint & Integration Path (访问路径与操作指令)**：
  - 会话诊断：`notebooklm auth check --test --json`（必须确认 `"checks.token_fetch": true`）；
  - 资产概览：`notebooklm source list --notebook <locator> --json`；
  - 精准查询：`notebooklm ask "<query>" --notebook <locator> --json`。
- **Verified Operations (已核实操作集合)**：
  - 已实测验证只读检索、来源清单读取及多来源问答综合；
  - 严禁执行未经显式授权的删除（`source delete` / `notebook delete`）或生成类重载操作。
- **Invocation Boundary (调用边界与人工触发原则)**：
  - 当且仅当研究工单显式触及已登记知识库覆盖的专业领域，或上游门禁要求交叉核验时触发调用；
  - 严禁智能体伪造外部能力调用结果；若会话失效或环境不支持，必须如实报告为不可访问，并请求人工介入登录。
- **Runtime Availability Requires Probe (运行时可用性需动态探测)**：
  - 外部服务连接受 Google 认证会话生命周期与网络限制影响，不可假设静态长期有效；
  - 每次涉及能力调用的工作单元开始前，必须执行最小受控探测（Bounded Probe），确认连接就绪后方可推进。

## 4. 知识边界与凭据溯源约束 (Provenance & Authority Rules)

- **权威性界定与溯源规则 (Provenance Rule)**：
  - NotebookLM 输出定位于“外部研究与交叉核验证据（Reported with Provenance）”，绝不自动成为项目事实权威（Project Authority）；
  - 引用外部能力时，必须记录完整来源元数据（Provider、Locator、精确 Query、提取语料标题与上下文），并经过教师或课程负责人审定后方可沉淀入库。
- **资料独立性**：两个 Notebook 职责分明，不要求复制相同材料。
- **安全与凭据**：严禁在代码仓库中保存任何 NotebookLM cookie、token、storage state 或其他身份凭据。
