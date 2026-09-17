# 《三维数字材质制作》课程设计动态台账 (Course Design Living Ledger)

> **文档定位**：记录《三维数字材质制作》课程在持续迭代中的已确认边界、工作假设与待解决核心问题，防止长对话中关键教学共识与研究线索丢失。

---

## 1. Research Gates & Milestone Status (研究门禁与里程碑状态)

- **Phase 1 (PBR Course Foundations)**：`PASS` (完成基线报告 `pbr-course-foundations.md`，确立物理可信性与管线原则)
- **Stage 1 (Textbook Closeout & Gap Analysis / Issue #2)**：`COMPLETED`
  - *Gate 1 (Source Inventory Verification)*: `PASS` (核实 Course Knowledge Notebook 实际语料，确认核心资产就绪)
  - *Gate 2 (2026 Living Official Sources)*: `PASS` (补齐 Painter 官方源、Designer、Sampler、Blender 与 OpenPBR 1.1 规范)
  - *Gate 3 (Available-Corpus Gap Analysis)*: `PASS` (完成证据修正，确立 Shah 骨架地位并由 2026 Living Sources 修正版本老化)
  - *Step 4A (Corpus Hygiene)*: `PASS` (核实最新 PBR Guide 完整双篇 PDF，完成语料瘦身，清理 6 个重复/低价值源，现存 24 个高纯度源)
  - *Step 4B (Conditional Acquisition Decision)*: `PASS` (完成一手选用证据审核；确立若买样书郑琳优先于伍福军；明确采购为可选验证项，非课程阻塞项)
  - *Step 5–6 (Final Resource Decision & Closeout)*: `COMPLETED` (固化七层角色化资源体系，方法归档于 `docs/methods/textbook-discovery-method.md`，关闭 Issue #2)
- **下一研究前沿 (Next Frontier)**：`Stage 2 Gate 3B — Practice Implementation Re-baselining & Controlled Revision Probe (Issue #5)` (确立教学运行时 Blender 5.2 LTS，对实践实现重定基准，验证受控修订充分性)

---

## 2. Stable / Accepted Boundaries (稳定边界与已确认决定)

以下原则与边界已在前期研究与讨论中确立，作为后续大纲与教学设计的基础约束：

1. **课程核心聚焦于 Material / Texture Authoring**：
   - 课程的核心教学与训练对象是**材质与纹理创作**本身，而不是大而全的次世代游戏资产制作全流程。
2. **前置支撑知识的边界控制**：
   - 建模（Modeling）、拓扑（Retopology）、高低模（High/Low Poly）、UV 展开与烘焙（Baking）等属于材质制作的支撑性知识；
   - 教学深度以“足以支撑材质制作与贴图绘制工作流”为度，严禁喧宾夺主成为课程主体。
3. **基于实证的课程设计纪律**：
   - 课程体系构建必须严格参考可核查的权威教材目录、官方认证教学体系、成熟行业课程及最新产业工作流，严禁由 Agent 脱离事实凭空臆造大纲结构。
4. **覆盖三种核心材质创作范式 (Three Authoring Paradigms)**：
   - **Texture-based / PBR Materials**：基于烘焙与贴图通道分层绘制的标准 PBR 工作流；
   - **Procedural / Parametric Materials**：基于节点与数学算法的程序化/参数化材质合成；
   - **AI-assisted / Generative Material Workflows**：AI 辅助生成、无缝贴图转换与智能纹理工作流。
5. **双应用出口定位**：
   - 实时游戏（Game Realtime）与动画/视觉开发（Animation / LookDev）是材质能力的两个主要应用出口，本课程将其统一在材质能力框架下，而非拆分为两门独立课程。
6. **最终教材与教学资源体系决议 (Final Textbook Closeout & Practice Decoupling)**：
   - **Primary Textbook Skeleton**：**Zeeshan Jawed Shah《Realistic Asset Creation with Adobe Substance 3D》(2022)** 正式保留为 Stage 1 选定的教材目录骨架（Selected Primary Textbook Skeleton），其建模前置极低，覆盖资产制作主干流程；其版本老化由 Living Official Sources 修正。但必须明确原则：**教材/来源骨架 ≠ 学生实践主线 (Textbook / Source Skeleton ≠ Student Practice Backbone)**。
   - **Gate 3B 实践主线重定基准 (Practice Re-baselining)**：
     - **教学运行时目标**：以 **Blender 5.2 LTS** 为当前核心教学运行时候选；
     - **参考版本原则**：**参考版本 ≠ 教学运行版本 (Reference Version ≠ Teaching Runtime Version)**，成熟的 4.2/4.5 参考资料可选择性复用，仅采纳段落需进行有界版本差量验证；
     - **候选实践路径**：Blender-only 为当前可逆的充分性候选 A；Painter 为有条件的候选 B（仅在 Blender 暴露出确凿的 retained-task 摩擦时进行定向检验）；
     - **广域参考搜索关闭**：`PRACTICE_REFERENCE_SEARCH_CLOSED_FOR_GATE_3B`。
   - **PBR Theory Foundation**：**Wes McDermott / Adobe《The PBR Guide, 3rd ed.》(2018)** 完整 PDF 正式定稿为物理理论底座（Selected PBR Theory Foundation），作为稳定的光学原理与反射率色阶基准，不作为 2026 软件操作源。
   - **Observation & LookDev Reference**：**Eran Dinur《The Complete Guide to Photorealism, 2nd ed.》(2026)** 正式定稿为质感观察与审美拔高参考（Selected Observation / LookDev Reference）。
   - **Bounded Procedural Foundation**：**Shah Ch 7–10 + Adobe Designer 官方入门 + Blender 5.2/4.5 Shader Nodes** 定稿为程序化基础组合；最终课时深度留待 Stage 2 裁定。
   - **Living Technical Authority**：Painter 8.3 (2023: dedicated Baking Mode, F8 快捷键, 视口包围盒预览)、Painter 12.1 (2026: redesigned/improved baking workflow, auto rebake, Paint Skew 偏斜修复, edge protection, OpenPBR 1.1 默认规范与工作流)、Painter 12.0 (2026: Warp to Geometry, Reload Mesh)、Painter 11.1 (2025-11: Ribbon Path) 及 Blender/OpenPBR 官方源定稿为活体技术权威。
   - **Chinese Student Companion**：**郑琳《Substance 3D Painter游戏贴图绘制与材质制作》(2024)** 为首选中文学生伴随候选（Preferred Candidate / Optional Acquisition），伍福军为次选；明确记录：*Chinese companion acquisition remains optional future validation, not a blocker.*
   - **Teacher Graphics Reference**：《Real-Time Rendering 4th (中英双语)》定稿为教师底层渲染参考。
   - **不可获取文献**：CafeGroup 2025 与 Born Digital Designer 2022 保持为 Desired References，不构成实际课程依赖。

---

## 3. Working Hypotheses (工作假设 / 探索中假设)

*注：以下工作假设反映前期 Stage 1 探索历史与当前 Gate 3B 实践重定基准动态。前期以 Painter 为中心、Designer 必修、Sampler 必修的推论作为历史推演保留，但在 Gate 3B 期间已转为**非约束待重开事项 (non-binding / reopened / conditional pending Gate 3B evidence)**。*

- **假设 1（实践主线与单宿主充分性，候选 A）**：Blender 5.2 LTS 已通过脚本自动化技术可行性探针 (scripted technical feasibility probe)；其在真实教学中面对学生/教师的人工 GUI 教学充分性 (human GUI teaching sufficiency) 尚待有界的手工门禁 (bounded manual gate) 检验。Blender-only 继续作为可逆的候选 A。
- **假设 2（定向辅助宿主，候选 B - 条件触发）**：仅在 Blender 5.2 暴露出学生/教师端无法消除的严重教学摩擦（如严重依赖难以维护的自定义黑箱节点组、破坏性贴图修改摩擦），且该摩擦会实质损害核心学习成效时，Substance 3D Painter 才作为定向补充工具进入评估。
- **假设 3（Designer 与 Sampler 角色非必修）**：Designer（程序化纹理）与 Sampler（AI/扫描采集转换）当前不作为学生端必修软件；保留为教师演示、概念参考或课外可选扩展，不构成 8 周学生实操依赖。
- **假设 4（程序化思维入口）**：Blender Shader Nodes 具备轻量、可视与免额外授权门槛的特点，足以独立支撑学生建立“参数化/程序化材质思维”。
- **假设 5（外部资产平台教学角色分工）**：
  - **Sketchfab**：承担实时模型材质/通道在线拆解与检视（Inspector）的教学分析角色；
  - **Poly Haven**：承担高质量标准 PBR 材质参考与开源真实物理贴图源的角色；
  - **Fab (Epic Games)**：承担工业级生产资产与引擎级材质实例结构的参考角色。

---

## 4. Open Questions (待解决核心问题清单)

后续研究与大纲设计需重点回答以下问题：

1. **教材体系选型与采购决策**：`CLOSED` (Stage 1 / Issue #2 已正式闭环，确立七层角色化资源体系，中文样书采购为可选验证项)。
2. **程序化材质深度**：
   - 在 8 周基础课内，Substance 3D Designer 与 Blender Shader Nodes 的课时分配与最终要求深度为何（属于 Stage 2 议题）？
3. **AI 工作流的重构边界 (Stage 2 重点)**：
   - AI 材质工作流（AI Material Workflow）在教学中究竟应当替代哪些繁琐操作、压缩哪些传统环节，又重新定义了哪些核心审美与技术控制能力？
4. **双出口能力的平衡标准**：
   - Game Realtime（注重性能、通道打包与实时光照）与 Animation / LookDev（注重高精度着色、次表面散射与复杂多层着色）两个应用出口，分别要求学生掌握到何种深度？

---
*本台账随课程调研与设计推进持续更新，归档于 `docs/research/course-design-ledger.md`。*
