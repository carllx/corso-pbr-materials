# 《三维数字材质制作》课程设计动态台账 (Course Design Living Ledger)

> **文档定位**：记录《三维数字材质制作》课程在持续迭代中的已确认边界、工作假设与待解决核心问题，防止长对话中关键教学共识与研究线索丢失。

---

## 1. Research Gates & Milestone Status (研究门禁与里程碑状态)

- **Phase 1 (PBR Course Foundations)**：`PASS` (完成基线报告 `pbr-course-foundations.md`，确立物理可信性与管线原则)
- **Stage 1 (Textbook Closeout & Gap Analysis / Issue #2)**：`PASS`
  - *Gate 1 (Source Inventory Verification)*: `PASS` (核实 Course Knowledge Notebook 实际语料，确认 Shah 2022、Photorealism 2026、The PBR Guide 等核心资产就绪)
  - *Gate 2 (2026 Living Official Sources)*: `PASS` (补齐 Painter 2026、Designer、Sampler、Blender 4.5 与 OpenPBR 1.1 官方开源权威源)
  - *Gate 3 (Available-Corpus Gap Analysis)*: `PASS` (形成可审计 Gap Register，确立 Shah 骨架地位与 5 大更新点，裁定无需额外采购国内教材)
- **下一研究前沿 (Next Frontier)**：`Stage 2 — Teaching Value Matrix / AI 后教学价值整合` (合并传统能力矩阵与 AI Impact Research，逐项判定 Keep / Compress / Reframe / Replace / Add New Skill)

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
6. **最终教材与教学资源体系决议 (Textbook Decision Closeout)**：
   - **Primary Textbook Skeleton**：确立由 **Zeeshan Jawed Shah《Realistic Asset Creation with Adobe Substance 3D》(2022)** 承担，全书 0% 建模拓扑负担，完全契合纯材质工作流；其 5 大技术老化点（烘焙模式、OpenPBR、贴花包裹、曲线路径、资产重载）由 2026 Living Sources 升级修正。
   - **Theory & Vision Authority**：由 **Eran Dinur《The Complete Guide to Photorealism, 2nd Edition》(2026)** 主导物理光影与质感观察理论，由 **Adobe《The PBR Guide (Part 1 & 2)》** 划定物理参数安全色阶，由 **《Real-Time Rendering 4th (中英双语)》** 承担教师底层渲染技术底座。
   - **Practical Companion & 本土化落地**：裁定无需让学生人手付费采购国内中文教材；由授课教师基于 Adobe 100% 汉化官方帮助手册制备《8周中文实训界面对照与避坑指南 (Cheat Sheet)》，实现零成本前沿教学落地。
   - **不可获取教材定性**：CafeGroup 2025 与 Born Digital Designer 2022 保留为 Desired References，实证已证明其缺失不造成教学断层。

---

## 3. Working Hypotheses (工作假设 / 探索中假设)

*注：以下内容为目前值得深入研究、但**尚未定案**的工作假设，不作为最终课程决定。*

- **假设 1（核心绘制环境）**：Substance 3D Painter 作为资产级纹理绘制（Texture Authoring）的主要实战教学环境（OpenPBR 1.1 默认工作流）。
- **假设 2（程序化思维入口）**：Blender Shader Nodes 具备轻量、可视与免额外授权门槛的特点，与 Designer 核心节点互通，共同培养学生“程序化/参数化材质思维”。
- **假设 3（Designer 课时定位）**：Substance 3D Designer 以核心高度图与混合逻辑（Tile Generator, Flood Fill, Height Blend）为主，不展开数百个复杂函数节点，控制认知负荷。
- **假设 4（传统与 AI 的过渡桥梁）**：Substance 3D Sampler / Image-to-Material 与 Dinur Ch 19 提出的 ComfyUI ControlNet (Depth/Normal) 引导生成，承担起连接传统 PBR 贴图与现代生成式 AI 工作流的桥梁角色。
- **假设 5（外部资产平台教学角色分工）**：
  - **Sketchfab**：承担实时模型材质/通道在线拆解与检视（Inspector）的教学分析角色；
  - **Poly Haven**：承担高质量标准 PBR 材质参考与开源真实物理贴图源的角色；
  - **Fab (Epic Games)**：承担工业级生产资产与引擎级材质实例结构的参考角色。
- **假设 6（作品发布平台）**：是否将 Sketchfab（或 Web 实时 3D 视口）作为学生期末作品的标准发布与交互展示目标，仍待进一步评估作业流程。

---

## 4. Open Questions (待解决核心问题清单)

后续研究与大纲设计需重点回答以下问题：

1. **教材体系选型**：`CLOSED` (已在 Stage 1 / Issue #2 完成决策与证据闭环，见第二节)。
2. **程序化材质深度**：
   - 在 8 周基础课内，程序化/参数化材质（Procedural / Parametric Material）应达到何种教学深度（节点逻辑理解 vs. 独立输出复杂材质）？
3. **AI 工作流的重构边界 (Stage 2 重点)**：
   - AI 材质工作流（AI Material Workflow）在教学中究竟应当替代哪些繁琐操作、压缩哪些传统环节，又重新定义了哪些核心审美与技术控制能力？
4. **双出口能力的平衡标准**：
   - Game Realtime（注重性能、通道打包与实时光照）与 Animation / LookDev（注重高精度着色、次表面散射与复杂多层着色）两个应用出口，分别要求学生掌握到何种深度？

---
*本台账随课程调研与设计推进持续更新，归档于 `docs/research/course-design-ledger.md`。*
