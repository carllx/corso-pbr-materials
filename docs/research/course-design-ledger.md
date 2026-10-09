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
  - *历史裁决事实*：完成单一外部下游交付探针 (Blender 5.2 LTS $\to$ glTF 2.0 $\to$ WebGL PBR Runtime via Chrome，`PASS`)，作为轻量级外部交付示范样本，保留 Game Realtime 与 Animation / LookDev 双出口；
  - *Post-Astra 教学路线纠偏 (2026-09-19)*：依据独立架构审查与 Issue #5 官方指令（Comment ID: `5737300653`），撤回 70–80% 实践固化占比，56–72h 降级为历史规划情境；恢复陌生非金属载体近迁移要求；确立承重型分层反馈架构；设立 LO3 空间局部性教学实操检查点 (`PENDING GATE 01`)；
- **Semester Offering Re-baseline (真实教务容量重基准化 / 2026-09-19)**：`COMPLETED`
  - 依据真实课表核实事实：第 10–18 周共 **9 个教学周**、**36 学时**、单学时 40 分钟、单班每周排定面授 160 分钟、单班总面授 **24 实际小时**；
  - 覆盖两个独立教学班：GR2102-1（35 人）与 GR2102-3（17 人），单教师现场主讲；
  - 完成有界影响分析报告（`course-offering-impact-analysis-2026-2027-1.md`），明确 9 周用于解除下游交付与 LookDev 挤压，释放主资产反馈打磨空间，严禁借周次扩张新内容；
  - 历史草案存档：`week1-8-conditional-planning-draft-v0.1.md` 标记为**历史条件性规划草案 (Historical Conditional Draft)**；
- **当前规划前沿 (Current Frontier)**：**`Teacher Review Rebaseline`**
  - **#19 Case Topology Closeout**：完成案例拓扑 Join 实证审计与决策收口；
  - **Accepted W1–W6 Bounded Hybrid**：Course Owner 正式接受 W1–W6 采用有限主案例 + 有界代表性微案例混合模型；
  - **Fixed W7–W9 New-Final Boundary**：锁定 W1–W6 基础演练与 W7–W9 全新期末大作业彻底解耦的宏观边界；
  - **Next Dependencies**：下一阶段严格依赖于 **Issue #22（期末大作业架构设计）**，待其完成后方可启动并综合生成 **Week 1–9 排课草案 v0.4**（注：v0.4 尚未生成，严禁标记为完成）。
- **课程负责人决策记录 (Course Owner Decision Record — 2026-10-03)**：
  - **决策结论**：**`TEACHER ACCEPTED — USE BOUNDED HYBRID AS W1–W6 TOPOLOGY BASELINE`**
  - **核心判定**：
    1. **锁定宏观边界**：W1–W6 基础演练 $\neq$ W7–W9 全新独立综合期末大作业（Fixed Macro Boundary）；期末大作业严禁继续使用 W1–W6 主练习资产；
    2. **确立拓扑基线**：W1–W6 采纳选项 C（有限主案例 + 有界代表性微案例模型）；
    3. **证据属性说明**：CORE42 后续外部语料审计未发现足以改变路线的冲突（`NO CONTRADICTION FOUND`），直接正向强化了 W1–W6 聚焦微案例配合复合主道具的教学组织证据；CORE42 是外部验证凭据（Reported with Provenance），而非该 Course Owner 决策本身的产生来源。
- **Week 1 教学实施包与教师验收决议 (Week 1 Executable Package & Teacher Review / Issues #11, #15, #14)**：
  - 决议状态 (2026-10-01)：**`TEACHER ACCEPTED WITH DELTAS — APPLY BOUNDED CORRECTIONS THEN USE AS BASELINE`**
    *(注：其中关于“W1 技术链路零变动/禁止新微实验”及原 B1–B4 迟滞上机节奏，已被 2026-10-09 Issue #37 决议部分替代 PARTIALLY SUPERSEDED)*
  - **决议事实与有界修正 (Bounded Correction)**：
    - 教师与 Course Owner 正式认可 Week 1 教学设计方案及 160 分钟课时节奏，附带一项有界修正：第一周开局显式预留 **15 分钟课程整体介绍 (Course Orientation)** 占位段；
    - **占位段规范**：内容后续由全课权威设计回填，最终覆盖 W1–W9 演进轨迹、后八周教学结构、作业练习体系、期末项目期望及考核评价框架原则；现阶段不编造或冻结任何具体成绩比例；
    - **课时重分配 (历史记录，现已由 Issue #37 替代)**：原 Block 1: 20 min (15 min Orientation + 5 min 入学摸底)；Block 2: 15 min；Block 10: 5 min；
    - **核心实践循环保持**：坚决保护“材质动作 $\to$ 现场反馈 $\to$ 受控修订 $\to$ 保存退出重开持久化 $\to$ 缓冲容灾”完整循环；
    - **门禁纪律**：本工单仅完成有界修正并作为后续基线，**严禁启动后续 W1–W9 v0.3 重排，不提前解除 Issue #13 阻塞**。
- **Week 1 前半段教学重构决议：几何体热身与手电筒主线对齐 (Issue #37 / 2026-10-09)**：
  - 决议状态 (2026-10-09)：**`TEACHER ACCEPTED — REALIGN WEEK 1 FRONT-HALF (PROPOSED TIMING / RUNTIME REQUIRED FOR CAPACITY & ASSETS)`**
  - **核心判定与设计原则**：
    1. **一条主线、两类素材职责**：低复杂度原生球体/立方体用于视觉原理的最小直观解释与 Blender 基本手感操作热身；Poly Haven **Vintage Flashlight** 严格保留为第一周正式材质观察/改色案例及 W1–W6 有界混合拓扑连续性载体；W7–W9 独立期末资产边界保持不变；
    2. **更早进入 Blender**：学生亲手添加、选中、移动/缩放少量原生几何体，认识 3D Viewport、Outliner、基础对象属性/材料入口、视口导航与 Material Preview；热身**不单独评分、不提交、不要求精确复刻老师场景**；灯光行为明确：Material Preview 下默认不依赖 Scene Lights，避免让学生调场景灯光；
    3. **分层讲解 UI**：几何体热身只讲基础视口导航与对象材质入口；正式手电筒任务才引入 Shading 工作区、Shader Editor、材质槽与预连 `Body_Color_Tint`。保持 Option B 预置节点方案，学生不连线不建节点；
    4. **概念导入先直观再应用**：游戏/数字内容 PBR 用途与视觉悬念 $\to$ 4 个英文标准术语（Base Color, Roughness, Metallic, Normal）及大白话 $\to$ 识别光照/视角与材质的区别 $\to$ 迁移到手电筒部位。“高光会跑，别把它画死在 Base Color 里”作为核心记忆锚点；Transmission vs Alpha 直观辨析；
    5. **开场不做知识测验**：消减开场 5 分钟摸底测试，直接通过 PPT 导入与几何体热身观察；保留后段 `Predict → Operate → Explain` 判别式学习证据；
    6. **单教师大班与保护核心**：160 分钟为总计划预算（PLAN BUDGET），重构 Block 1–6 候选分钟分配并明确超时优先剪裁规则（Cut Rules）；坚决保护材料观察、学生独立决策、反馈修订、保存退出重开持久化及轻量交付课内闭环；禁止通过隐性课后作业吸收超时；
    7. **旧规则替代确认 (Supersession Notice)**：正式替代 2026-10-01 决议中关于“Week 1 零技术链路变动 / 禁止新微实验”的静态限制（仅针对几何体热身）；手电筒主线和 Option B 保护核心继续有效。

---

## 2. Stable / Accepted Boundaries (稳定边界与已确认决定)

以下原则与边界已在前期研究与讨论中确立，作为后续大纲与教学设计的基础约束：

0. **课程负责人与人机决策权威边界 (Course Owner & Human Decision Authority Boundary)**：
   - **人类决策权威 (Human Decision Authority)**：Course Owner（教师/课程负责人）拥有教学目标、9 周大纲架构、实操深度、平时/期末考核评价框架以及所有 Gate 里程碑（Review / Exit）的最终裁决与冻结权；
   - **智能体工程协作边界 (Agent Boundary)**：Agent 承担一手实证调研、运行时技术切片验证、教学包与自动化脚本重构及有界文本草案编写；严禁在未获人类显式确认前擅自冻结评分比例、私自启动大纲重排或放行阻断门禁。

1. **课程核心聚焦于 Material / Texture Authoring**：
   - 核心教学与训练对象是**材质与纹理创作**本身，不扩张为大而全的次世代游戏资产建模与全案制作流程。
2. **前置支撑知识的边界控制**：
   - 建模（Modeling）、拓扑（Retopology）、高低模（High/Low Poly）、UV 展开等属于材质制作的支撑性知识；
   - 教学深度以“足以支撑材质制作与贴图绘制工作流”为度，由教师预置干净资产模型，严禁喧宾夺主成为考核主体。
3. **真实教学容量约束 (Verified 9-Week / 24-Contact-Hour Reality)**：
   - 严格在单班每周 160 分钟、9 周总计 24 实际小时物理接触时间内组织教学；不设计未经验证的分钟数伪精确配额；
   - 35 人班与 17 人班维持完全一致的学习标准与考核 Rubric，现场通过四级反馈漏斗（共性讲评、自查互查、流动抽检、工件异步核验）自适应调节节奏。
4. **宏观阶段解耦与案例拓扑架构 (Macro Boundary Decoupling & Case Topology)**：
   - **已锁定宏观边界 (FIXED MACRO BOUNDARY)**：
     - **W1–W6 = 教学基础演练与能力构建 (Teaching / Practice Capability Construction)**；
     - **W7–W9 = 全新独立综合期末大作业 (New Comprehensive Final Project)**；
     - **彻底解耦原则**：W7–W9 严禁继续使用 W1–W6 主练习资产（如 Flashlight）作为期末作品，消除前期练习的历史包袱；
   - **W1–W6 案例拓扑架构 (TEACHER ACCEPTED)**：
     - **核心模型**：采纳**有限主案例 + 有界代表性微案例模型 (Limited Main Case + Bounded Representative Micro-Cases, Bounded Hybrid)**；
     - **当前候选资产结构**：
       - **Vintage Flashlight**：作为 W1–W5-ish 主练习的连续性主干（Continuity Backbone，具体周次安排由后续排课草案 v0.4 确定）；
       - **Classical Bust**：作为 W3 或之后的法线/浮雕（Normal / representation）有界微案例候选（Bounded Micro-case Candidate，具体实操组织深度待定）；
       - **Antique Ceramic Vase 01**：作为 W6 光滑施釉近迁移测试候选（Near-transfer Candidate，归档即闭环，仍受运行时/模板门禁约束）；
     - **排课纪律**：具体周次不写成冻结的时间表（Not a frozen timetable）。
5. **极简双应用出口定位**：
   - 实时游戏（WebGL/glTF 交付核验，允许标准烘焙/导出预设）与动画/视觉开发（Cycles 预置离线演播室 LookDev 一致性归因）统一在材质能力框架下，复用主资产源工程，不开设两套庞大生产管线。
6. **制作环境与工具触发纪律**：
   - **主要实操制作环境**：以 **Blender 5.2 LTS** 为当前暂定主要实操环境；
   - **条件性工具对比触发**：Blender-first 为默认宿主；仅当 LO3 空间局部实操探针证明 Blender 原生界面存在不可接受的教学摩擦时，才在受控修改任务上启动与 Substance 3D Painter 的狭窄成本对比；
   - 广域软件比选与参考搜索保持关闭。
7. **最终教材与教学资源体系决议**：
   - **Primary Textbook Skeleton**：Zeeshan Jawed Shah (2022) 保持为教材目录骨架（教材骨架 ≠ 学生实践主线）；
   - **PBR Theory Foundation**：Adobe《The PBR Guide, 3rd ed.》(2018) 定稿为光学物理与通道语义底座；
   - **Observation & LookDev Reference**：Eran Dinur (2026) 定稿为质感观察与审美解构参考；
   - **Practice Reference Fragment**：CORE42 保持为成熟操作片段参考，教师负责过滤非规范手法；
   - **Living Technical Authority**：Painter 官方源、Blender 5.2 官方手册与 OpenPBR 1.1 规范为活体权威。

---

## 3. Working Hypotheses & Open Gates (工作假设与前置门禁)

*注：以下条目反映当前进入 9 周条件性排课阶段的最新共识与门禁隔离：*

- **假设 1（形成性检查定位与评分未冻结）**：Checklist 与过程诊断定位于**形成性质量控制检查点 (Formative Checkpoints)**，作为推进制作的必要证据。其具体在总评中的分值、权重及计分形式保持为 `UNKNOWN`，待学校官方考查政策明确后方可冻结。Owner 偏向“最终作品质量优先”，但不取消过程诊断与证据链。
- **假设 2（LO3 空间局部修改与保护范围定义）**：LO3 达成要求稳定（在定义保护范围内无非预期修改）；具体在 Blender 中的交互路径保持条件性，受 `[PENDING GATE 01]` 门禁约束。
- **假设 3（近迁移三分类因果判断）**：近迁移任务不使用非黑即白的“二元失效”标准，而是考察学生对物理规则的精细分类判断（可直接迁移 / 经调整后迁移 / 不适用或误导）。
- **假设 4（单师 52 人异步审查负荷控制）**：将全员逐人审核移至课外并不意味着教师容量免费。必须控制工件复杂度与形式，依托结构化 Checklist 提升批阅周转率，课内杜绝排队等待。
- **假设 5（门禁阻断正交化架构）**：
  - `[GATE 1: CALENDAR]` 星期排定与调课补课核实 $\to$ 仅阻断 `calendar freeze`；
  - `[GATE 2: GRADING]` 校方考查成绩比例文件 $\to$ 仅阻断 `grading policy freeze`；
  - `[GATE 3: HARDWARE]` 机房 GPU 与显存参数核查 $\to$ 仅阻断 `exact render assumptions`；
  - `[GATE 4: SOFTWARE]` 学校软件预装部署时限 $\to$ 仅阻断 `implementation readiness`；
  - `[GATE 5: LO3 PROBE]` LO3 空间局部性实操探针 $\to$ 仅阻断 `LO3 exact teaching path`。
- **假设 6（未决资产运行时与交付门禁 / Unresolved Runtime & Asset Gates）**：
  以下关键技术与资产链路严格保持为 `UNRESOLVED / CONDITIONAL`，严禁假设为已验证：
  - **`[GATE-ASSET-01]`**：Flashlight M6 (风化锈蚀) / M7 (缝隙积灰) 的几何承载性（待网格运行时解构核验）；
  - **`[GATE-ASSET-02]`**：Vase 01 零摩擦 `.blend` 模板工程与近迁移可用性；
  - **`[GATE-RT-01]`**：外部 Web 实时查看器的机房离线运行与 GPU 兼容性（未通过前严格保持 EEVEE 视口基线）；
  - **Exact Normal Bake Implementation**：高低模法线烘焙实操形式（保持为活跃教学候选 Active Teaching Candidate。已定边界：不作为默认 45 分钟全员完整烘焙、不进入 Week 1、不锁死于固定周次、不将全员从零高低模投影烘焙设为默认；待定选项：教师演示 / 边界受控的学生微实验 / 可选拓展 / 延期或移除；具体实操深度、时间预算、周次落位与作业设计留待后续排课草案综合与运行时验证，绝非只读观察最终裁决）；
  - **Final Assignment Form**：期末大作业的具体选型、交付规格与评分细则（完整留待 Issue #22 独立解答）。

---

## 4. Open Questions & Next Actions (待决问题与后续行动)

1. **LO3 空间局部性 GUI 实操探针测试**：在合适节点组织真实 Blender 5.2 界面下的局部绘制—保存—重开验证，判定是否需触发 Painter 条件性窄对比。
2. **学校教务管理输入补全**：获取考查课平时/期末成绩比例硬性规定，获取机房 PC 硬件参数与软件预装窗口。
3. **正式执行课表排定与冻结**：待 Issue #22（期末大作业架构设计）确立、相关前置门禁核销后，启动综合生成《Week 1–9 排课草案 v0.4》，并依规提交 Course Owner 审定冻结。

---
*本台账随课程调研与设计推进持续更新，归档于 `docs/research/course-design-ledger.md`。*
