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
- **Stage 2 Gate 3B (Practice Implementation Re-baselining & Delivery Probe / Issue #5)**：`PASS` (历史裁决已正式通过，有界外部交付探针闭环成立)
  - *历史裁决事实*：完成单一外部下游交付探针 (Blender 5.2 LTS $\to$ glTF 2.0 $\to$ WebGL PBR Runtime via Chrome，`PASS`)，作为轻量级外部交付示范样本 (lightweight external delivery exemplar)，不排他性冻结最终交付运行时，保留 Game Realtime 与 Animation / LookDev 双出口；
  - *Post-Astra 教学路线纠偏 (2026-09-19)*：依据独立架构审查与 Issue #5 官方指令（Comment ID: `5737300653`），撤回 70–80% 实践固化占比，56–72h 降级为历史规划情境而非已验证工时；恢复陌生非金属载体近迁移要求；确立承重型反馈架构；设立 LO3 空间局部性教学实操检查点 (`PENDING BEFORE FROZEN EXECUTABLE SCHEDULE`)；
- **当前规划前沿 (Current Frontier)**：**`WEEK_1_8_CONDITIONAL_PLANNING_DRAFT`**
  - 完成首份《Week 1–8 条件性排课草案 v0.1》（`week1-8-conditional-planning-draft-v0.1.md`），处于 **CONDITIONAL / NOT FROZEN** 状态。

---

## 2. Stable / Accepted Boundaries (稳定边界与已确认决定)

以下原则与边界已在前期研究与讨论中确立，作为后续大纲与教学设计的基础约束：

1. **课程核心聚焦于 Material / Texture Authoring**：
   - 课程的核心教学与训练对象是**材质与纹理创作**本身，而不是大而全的次世代游戏资产制作全流程。
2. **前置支撑知识的边界控制**：
   - 建模（Modeling）、拓扑（Retopology）、高低模（High/Low Poly）、UV 展开与烘焙（Baking）等属于材质制作的支撑性知识；
   - 教学深度以“足以支撑材质制作与贴图绘制工作流”为度，由教师预置规整模型，严禁喧宾夺主成为课程主体。
3. **基于实证的课程设计纪律**：
   - 课程体系构建必须严格参考可核查的权威教材目录、官方认证教学体系、成熟行业课程及最新产业工作流，严禁由 Agent 脱离事实凭空臆造大纲结构。
4. **覆盖三种核心材质创作范式 (Three Authoring Paradigms)**：
   - **Texture-based / PBR Materials**：基于烘焙与贴图通道分层绘制的标准 PBR 工作流；
   - **Procedural / Parametric Materials**：基于节点与数学算法的程序化/参数化材质合成；
   - **AI-assisted / Generative Material Workflows**：AI 辅助生成、无缝贴图转换与智能纹理工作流。
5. **极简双应用出口定位**：
   - 实时游戏（Game Realtime，以 WebGL/glTF 交付核验为轻量范例）与动画/视觉开发（Animation / LookDev，以预置 Cycles 离线高质量光照评测为范例）统一在材质能力框架下，复用相同材质资产，不开设两套独立的庞大生产管线。
6. **最终教材与教学资源体系决议 (Final Textbook Closeout & Practice Decoupling)**：
   - **Primary Textbook Skeleton**：**Zeeshan Jawed Shah《Realistic Asset Creation with Adobe Substance 3D》(2022)** 正式保留为 Stage 1 选定的教材目录骨架，其建模前置极低，覆盖资产制作主干流程；其版本老化由 Living Official Sources 修正。明确原则：**教材/来源骨架 ≠ 学生实践主线**。
   - **实践主线重定基准 (Practice Re-baselining)**：
     - **教学运行时目标**：以 **Blender 5.2 LTS** 为当前暂定主要实操制作环境（Provisional Primary Authoring Runtime）；
     - **参考版本原则**：**参考版本 ≠ 教学运行版本**，成熟的 4.2/4.5 参考资料可选择性复用，仅采纳段落需进行有界版本差量验证；
     - **软件角色定位**：Blender-first 为当前主要制作宿主；Substance 3D Painter 保持为有条件的备选工具（仅在 LO3 空间局部修改实操暴露出无法承受的教学/支架摩擦时才授权定向对比）；
     - **广域参考搜索关闭**：`PRACTICE_REFERENCE_SEARCH_CLOSED_FOR_GATE_3B`。
   - **PBR Theory Foundation**：**Wes McDermott / Adobe《The PBR Guide, 3rd ed.》(2018)** 完整 PDF 正式定稿为物理理论底座，作为稳定的光学原理与反射率色阶基准，不作为 2026 软件操作源。
   - **Observation & LookDev Reference**：**Eran Dinur《The Complete Guide to Photorealism, 2nd ed.》(2026)** 正式定稿为质感观察与审美拔高参考。
   - **Bounded Procedural Foundation**：**Shah Ch 7–10 + Adobe Designer 官方入门 + Blender 5.2 Shader Nodes** 定稿为程序化基础组合。
   - **Living Technical Authority**：Painter 最新官方源、Blender 5.2 官方手册与 OpenPBR 1.1 规范定稿为活体技术权威。
   - **Chinese Student Companion**：**郑琳《Substance 3D Painter游戏贴图绘制与材质制作》(2024)** 为首选中文学生伴随候选（可选验证项，非阻塞项）。
   - **Teacher Graphics Reference**：《Real-Time Rendering 4th (中英双语)》定稿为教师底层渲染参考。

---

## 3. Working Hypotheses (工作假设 / 探索中假设)

*注：以下工作假设反映当前进入排课阶段的最新共识与探索动态：*

- **假设 1（单宿主制作与教学风险检查点）**：Blender 5.2 LTS 经脚本探针验证了参数/数据流隔离与外部交付闭环；其在学生真实 GUI 交互下的教学充分性尚未实证。将“指定空间区域编辑 $\to$ 非目标区域保全 $\to$ 保存重开二次修改”设立为课表最终冻结前的实操检查点 (`PENDING BEFORE FROZEN EXECUTABLE SCHEDULE`)。
- **假设 2（条件性工具对比触发规则）**：仅在 Blender 5.2 空间局部修改实操暴露出学生端无法克服的严重教学摩擦（如破坏性贴图丢失、反直觉复杂模板）时，才针对该特定任务开展狭窄有界的 Blender vs. Substance 3D Painter 对比。不开展宽泛的 Painter 全面评估。
- **假设 3（Designer 与 Sampler 角色非必修）**：Designer（程序化纹理）与 Sampler（AI/扫描采集转换）当前不作为学生端必修软件；保留为教师演示、概念参考或课外可选扩展，不构成 8 周学生实操依赖。
- **假设 4（程序化思维入口）**：Blender Shader Nodes 具备轻量、可视与免额外授权门槛的特点，足以独立支撑学生建立“参数化/程序化材质思维”。
- **假设 5（外部资产平台教学角色分工）**：
  - **Sketchfab**：承担实时模型材质/通道在线拆解与检视（Inspector）的教学分析角色；
  - **Poly Haven**：承担高质量标准 PBR 材质参考与开源真实物理贴图源的角色；
  - **Fab (Epic Games)**：承担工业级生产资产与引擎级材质实例结构的参考角色。
- **假设 6（容量约束与保护核心）**：历史 56–72h 仅为情境参考；在高校实际面授学时、作业规范与班级规模明确前，排课保持条件性。面对容量超载，优先裁减几何体体量与纯装饰性细节精修，坚决保护“反馈—修订—复核”、LO2 独立诊断、LO3 受控修改、近迁移证据与双出口核验。

---

## 4. Open Questions (待解决核心问题清单)

后续大纲细化需重点回答以下问题：

1. **教材体系选型与采购决策**：`CLOSED` (Stage 1 / Issue #2 已正式闭环，确立七层角色化资源体系)。
2. **LO3 空间局部修改实操可行性验证**：
   - 在 Blender 5.2 原生环境下，新手能否在可接受支架下独立完成“指定区域编辑—非目标保全—保存重开二次修改”的教学闭环？
3. **高校制度性容量参数核实**：
   - 校方实际每周面授分钟数、课外学时要求与师生配比为何，能否支撑全周期的承重型反馈与修订复核？
4. **陌生非金属载体近迁移设计**：
   - 如何在不增加复杂新物理模型的前提下，设计一份既能检验尺度/方向/粗糙度因果判断，又能在短时间内完成局部纠错的轻量级非金属载体任务？

---
*本台账随课程调研与设计推进持续更新，归档于 `docs/research/course-design-ledger.md`。*
