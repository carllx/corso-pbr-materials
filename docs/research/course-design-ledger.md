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
- **当前规划前沿 (Current Frontier — 2026-10-21 更新)**：**`Painter-first Execution Mainline (Issue #40)`**
  - **主线切换裁定**：2026-10-21 Course Owner 权威裁定本学期（2026-2027-1）正式以广州软件学院 GR2102 既有九讲 Substance 3D Painter 方案为当前执行主线，由 **Issue #40** 承载（第一讲 MeetMat 教师审查版与后八讲低分辨率依赖对照）；
  - **Blender 备选路线保全**：原 Blender-first 路线及已验收决策（#19 案例拓扑收口、#37 几何体热身、W1–W6 混合模型、W7–W9 独立期末解耦边界）作为历史有效记录完整保留，定位为未来可恢复备选路线（Restorable Alternative Baseline），历史记录不删除、不改写；
  - **当代艺术引导原则与验证假设纳入**：确立“艺术引导 → 技术支撑 → 创作表达 → 作品验证”原则 (`TEACHER ACCEPTED`)；PBR 与 Painter 仍为主体，艺术作为观察判断引导资源（非艺术史单元），不改变九讲、软件与考核；第一讲 MeetMat 材质身份对比促成观察解释能力提升假设保持为待验证状态 (`PROJECT INFERENCE / VALIDATION PENDING`)，设置严格首讲验证门禁（详见 §5.9）；
  - **Next Dependencies**：当前阶段依赖于 Issue #40 教学草案与低分辨率对照的教师审查闭环；第一讲 MeetMat 教学草案与验证假设审查；机房目标 PC 实机探针；教材双层定性落实；Issue #39 培养方案适用性门禁保持独立跟踪。
- **课程负责人决策记录 (Course Owner Decision Record — 2026-10-03)**：
  - **决策结论**：**`TEACHER ACCEPTED — USE BOUNDED HYBRID AS W1–W6 TOPOLOGY BASELINE`**
  - **核心判定**：
    1. **锁定宏观边界**：W1–W6 基础演练 $\neq$ W7–W9 全新独立综合期末大作业（Fixed Macro Boundary）；期末大作业严禁继续使用 W1–W6 主练习资产；
    2. **确立拓扑基线**：W1–W6 采纳选项 C（有限主案例 + 有界代表性微案例模型）；
    3. **证据属性说明**：CORE42 后续外部语料审计未发现足以改变路线的冲突（`NO CONTRADICTION FOUND`），直接正向强化了 W1–W6 聚焦微案例配合复合主道具的教学组织证据；CORE42 是外部验证凭据（Reported with Provenance），而非该 Course Owner 决策本身的产生来源。
- **Week 1 教学实施包与教师验收决议 (Week 1 Executable Package & Teacher Review / Issues #11, #15, #14)**：
  - 决议状态 (2026-10-01)：**`TEACHER ACCEPTED WITH DELTAS — APPLY BOUNDED CORRECTIONS THEN USE AS BASELINE`**
  - **决议事实与有界修正 (Bounded Correction)**：
    - 教师与 Course Owner 正式认可 Week 1 教学设计方案及 160 分钟课时节奏，附带一项有界修正：第一周开局显式预留 **15 分钟课程整体介绍 (Course Orientation)** 占位段；
    - **占位段规范**：内容后续由全课权威设计回填，最终覆盖 W1–W9 演进轨迹、后八周教学结构、作业练习体系、期末项目期望及考核评价框架原则；现阶段不编造或冻结任何具体成绩比例；
    - **课时重分配 (严格等于 160 分钟)**：
      - Block 1: 20 min (15 min Orientation + 5 min 入学摸底)；
      - Block 2: 15 min (概念与光影剥离示范聚焦)；
      - Block 10: 5 min (轻量交付与收尾)；
      - 其余模块 (Block 3–9, 11) 严格保持不变；
    - **核心实践循环与技术链路零变动**：坚决保护“材质动作 $\to$ 现场反馈 $\to$ 受控修订 $\to$ 保存退出重开持久化 $\to$ 缓冲容灾”完整循环；不改动 Blender 5.2.2 LTS 运行时、Starter 资产或材质交互逻辑；
    - **门禁纪律**：本工单仅完成有界修正并作为后续基线，**严禁启动后续 W1–W9 v0.3 重排，不提前解除 Issue #13 阻塞**。

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

## 5. 学期主线切换与双路线协作治理决议 (Course Offering Implementation Disposition: Painter Mainline & Blender Restorable Baseline) <a id="section-7"></a><a id="第-7-节"></a>

> **决策与证据溯源说明**：  
> 本节记录 2026-10-21 课程负责人 (Course Owner) 关于 2026-2027-1 学期实操教学路线的权威裁定。严格遵循 `AGENTS.md` 证据纪律与历史保全原则，记录路线切换、备用路线指针、跨路线复用边界、第一讲实机门禁以及学院选用教材核验结论。  
> *(注：本节承载 2026-10-21 路线裁定，在前期部分讨论与工单中曾被称为“第 7 节 / Section 7”，现顺接第 4 节规范统一为第 5 节；历史与工单引用自动映射并兼容至本节。)*

### 5.1 课程负责人决议背景与裁定事实 (Course Owner Decision Record — 2026-10-21)
1. **决策结论**：**`TEACHER ACCEPTED — SUBSTANCE 3D PAINTER AS CURRENT SEMESTER MAINLINE`**
2. **核心判定**：
   - **执行主线切换**：本学期（2026-2027-1）正式以广州软件学院现有 GR2102 九讲 Substance 3D Painter 方案作为当前实际执行与备课主线；
   - **历史有效性与非改写纪律**：此前研发的 Blender-first 课程方案在其研发阶段具有完全合法性与技术闭环，历史记录完整保留，不作历史抹除或掩盖；
   - **备选路线定位**：Blender-first 方案作为未来可恢复备选路线（Restorable Alternative Baseline）完整保全，后续可随时根据教务或机房条件恢复。

### 5.2 Blender-first 备用路线可恢复资产与 Git 引用索引 (Blender Restorable Alternative Lineage & Pointers)
为保障备选路线完整可恢复，且遵循“不复制文件、不机械新建分支、不关闭/删除现有 PR”原则，建立如下 Git 指针索引：

- **核心 Draft PR 与工单分支**：
  - **Draft PR #38** (`design/issue-37-week1-geometry-warmup-realignment` @ Head `397b74bd9d2f034b9e73be73034a2a9822dfb80e`): Week 1 前半段几何体热身、分层 UI 与手电筒两级遮罩管线完整实现；
  - **PR #36** (`research/issue-35-week1-capacity-bounded-trial`): 课堂容量验证方法与时间记录契约；
  - **PR #34** (`docs/teacher-prep-decision-discipline`): 备课治理与极轻 PPT 投影规范；
  - **PR #33** (`impl/issue-32-week1-golive` @ `25bfe36`): Week 1 交付门禁与生命周期核验；
  - **PR #31** (`design/issue-22-final-project-contract`): 期末大作业架构；
  - **PR #25** (`research/issue-21-realtime-web-material-path`): WebGL/glTF 实时材质交付路径；
  - **PR #18** (`research/issue-13-week1-9-rebaseline-v0.3`): 历史条件性排课草案；
- **关键固定提交 SHA**：
  - `744b9e28414b1fea6bd1318dc904223258d662ea`: 教师交互边界完善、动态预算解析与负向测试套件；
  - `e5ed611fd4a4545330bb7e3da4defe65aa3a8bee`: 仓库 `main` 分支基线。

### 5.3 跨路线知识复用边界 (Cross-Route Pedagogical Boundary & Non-Transferable Operations)
在切换至 Painter 主线后，严格贯彻“方法与原理可复用、软件专有操作严禁机械移植”边界：

1. **允许并推荐复用的内容 (Portable Pedagogical Principles & Theory)**：
   - **光学与 PBR 物理因果**：能量守恒、电介质 vs 导体、微表面粗糙度与高光展宽、“高光会跑，别把它画死在 Base Color 里”核心因果；
   - **教学交互范式**：`Predict → Operate → Explain` 任务设计；
   - **轻量决策卡机制**：三字段记录结构（初次决策 $\to$ 接收反馈 $\to$ 修订动作）；
   - **课堂节奏与容灾**：160 分钟单班节奏预算、四级反馈漏斗、Recovery Ladder A/B/C 三级容灾、超时剪裁规则 (Cut Rules)、No-hidden-homework 原则；
   - **工程规范评估**：以客观物理因果与图层结构为依据，杜绝纯主观审美打分；软件退出重启持久化验证。
2. **严禁机械移植的 Blender 专有操作 (Blender-Specific Operations NOT Transferable)**：
   - **着色器节点网络操作**：Blender Shader Editor, `ShaderNodeMix` 节点, Color 混合模式, ColorRamp, Principled BSDF 插槽直接接线（Painter 依托 Layer Stack、Fill Layer、图层混合模式、Black Mask、Generator / Smart Mask，而非手动连线）；
   - **视口与交互快捷键**：Blender 3D 视口三键客、`Shift+A` 加物体、`G/R/S` 变换手感（Painter 使用 Alt+左/中/右键视口导航、Shift+右键旋转 HDRI 环境光）；
   - **特定数据结构**：Blender 材质槽 (Material Slots) 映射规则（Painter 使用 Texture Set 纹理集列表）。

### 5.4 Painter 第一讲落地执行与实机门禁 (Week 1 MeetMat Runtime Gate — RUNTIME REQUIRED)
针对切换后第 1 讲（MeetMat 入门）：
1. **第 1 讲核心知识焦点与计划预算**：Painter 界面布局、Texture Set (纹理集) 概念、视口导航与环境光照旋转、图层堆栈 (Layer Stack) 与填充图层 (Fill Layer)、基础通道 (Base Color / Roughness / Metallic)、材质球指派与基础贴图导出。**160 分钟单班面授时间严格定界为计划预算 (PLAN BUDGET)，非已实测容量**，实际耗时与大班节奏须经现场机房教学闭环。
2. **实机验证门禁状态 (`RUNTIME REQUIRED / OPEN`)**：
   - 所有关于 MeetMat 在 Painter 内部的交互演示步骤、白模或工程素材导出、贴图导出及保存退出重开持久化，当前在本地开发机处于 `RUNTIME REQUIRED / UNVERIFIED ON LOCAL HOST`（因本地开发环境未部署该商业应用）；
   - 必须在真实目标机房 PC 上完成 GUI 交互探针测试，方可宣称通过；
3. **最小必要备课与机房实机验证清单 (Minimal Lab Verification Checklist)**：
   - **Gate A-1 (环境与授权核查)**：核实机房工作站安装的 Substance 3D Painter 确切版本，确认显存与驱动正常；
   - **Gate A-2 (MeetMat 资产工程完备性)**：在机房实机打开 MeetMat 初始示例，核验各 Texture Set 正常映射；
   - **Gate A-3 (干净练习工程制作)**：准备供学生开局的空白/初始工程，杜绝剧透工程下发；
   - **Gate A-4 (保存与重开持久化)**：实测保存为 `.spp` 工程，完全退出 Painter 进程重开验证持久化；
   - **Gate A-5 (轻量交付通道测试)**：测试学生导出 1 张视口快照或标准贴图包的收件可行性。

### 5.5 课程负责人决策权威 vs 学校正式教学大纲适用性双轨定界
- **实操执行 vs 培养方案适用性定界**：
  - **轨 1（学期教学执行）**：Course Owner 裁定 Painter 主线即日起生效，指导当下备课与机房排课；
  - **轨 2（教务合规与培养方案）**：Issue #39 暴露的培养方案学时差异、课程代码差异、4 学时 PBR 综合实验定位，以及本学期 2026 秋授课班级正式执行的教学大纲版本，**继续保持 `UNRESOLVED / GATE OPEN` 门禁**；
- **纪律红线**：课程负责人的务实主线选择，**绝不臆测或伪称学校教务部门已完成正式审批或大纲勘误**；正式大纲状态待教务部门正式文件回执后方可核销。

### 5.6 学院选用教材核验结论与双层定性收敛 (2026-10-21)
1. **教材核实与版权页事实**：
   - **书目信息**：清华大学出版社 郑琳 编著《Substance 3D Painter游戏贴图绘制与材质制作》；
   - **版次与印次**：2024 年 2 月第 1 版，2024 年 8 月第 2 次印刷（重印；审批表登记出版日期为 2024-03-01）；
   - **书号与登记**：ISBN 978-7-302-65667-8，中国国家版本馆 CIP 数据核字 (2024) 第 048666 号；
   - 实测 138 物理页数字化成果在本地受控介质完成核验闭环，确认为学院审批表所列同一版本。
2. **双层定性与边界定界**：
   - **行政与选用身份**：学院教务归档《教材选用审批表》列名的选用教材；审批表记载大纲覆盖率 75% 属教务申报估计值，非逐项实测值；审批表实际记载的教学增删与案例融合安排为“根据课程时长、学生水平适当增删，融合实践案例，增加实践时间”；其实际教务适用性门禁仍由 Issue #39 独立跟踪；
   - **教学角色**：定性为“中文学生速查伴读手册与参数词典 (Chinese Student Companion)”；全书基于 8.3 (2022/2023) 编写，属第三方个人教学专著，**绝非 Adobe 官方技术规范**；版本差异以 AdobeDocs 活体源与机房探针为准；
   - **课程取舍界限**：全书 85.8% 字符集中于第 1~2 章，第 3~5 章案例依赖未随书附带资产与微课二维码；教材未覆盖的 UV 展开、烘焙与 Blender/Arnold 跨软件连接属于课程底层支撑与输出出口，“教材未覆盖”绝不等于“课程应删除”。

### 5.7 GitHub 执行路线对齐、工单承载与交付成果
1. **工单承载**：当前学期 Painter-first 实施主线由 **[Issue #40](https://github.com/carllx/corso-pbr-materials/issues/40)** 承载（标签 `ready-for-human`，关联 #1、#13、#22、#39）；
2. **核心交付物落位**：
   - **第一讲教师审查版教学草案**：[`docs/research/painter-week1-meetmat-teaching-draft-v0.1.md`](painter-week1-meetmat-teaching-draft-v0.1.md)；
   - **后八讲低分辨率依赖对照**：[`docs/research/painter-courseware-dependency-contrast-w2-w9.md`](painter-courseware-dependency-contrast-w2-w9.md)（平时作业与期末边界保持为候选建议 `CANDIDATE PROPOSAL / PENDING TEACHER DISPOSITION`，未获教师最终冻结）；
   - **学院旧课件认知审计**：[`docs/research/legacy-courseware-source-pedagogical-audit.md`](legacy-courseware-source-pedagogical-audit.md)；
   - **自动化能力与资产复用探针**：[`docs/research/painter-automation-and-asset-reuse-probe.md`](painter-automation-and-asset-reuse-probe.md)。

### 5.8 第一讲教师决定收敛与教学顺序确立 (Teacher Acceptance Record — 2026-10-21)
1. **教学组织顺序决议 (`TEACHER ACCEPTED`)**：
   - 裁定第一讲打破先讲理论后上机的模式，采用**“视觉观察 → 必要界面认识 → 教师示范 → 学生操作 → 理论解释 → 独立应用”**六步认知递进顺序；
2. **全员核心保底任务边界 (`TEACHER ACCEPTED`)**：
   - 严格收敛于 **MeetMat `Head` 部位的基础材质属性 (BaseColor/Roughness/Metallic)、双层 Fill Layer、Black Mask 开窗绘制，以及 `.spp` 规范保存与退出重开持久化**；
3. **非必经目标剔除与后续阶梯承接 (`TEACHER ACCEPTED` / `CANDIDATE BRIDGING`)**：
   - 明确 `Body`/`Base` 扩展、Smart Materials 智能材质、生成器 (Generators) 和 Iray 渲染器**不属于第一讲全员必经目标**；
   - **延后知识承接规划 (候选建议)**：Smart Materials 与 Generators 在 W2（塑料案例）进行候选认识与轻量观察，在 W4（金属做旧）深入拆解图层与 Mesh Maps 因果关系并产出修改证据；Iray 保持为后续周次成果展示的条件性候选，绝不设为全员必修或强制截图工具；周次与容量均待教师最终审定；
4. **容量定界、时间切片与实施路径推荐**：
   - **时间切片候选预算**：160 分钟计划预算严格闭环（Block 1: 15m $\to$ Block 2: 15m $\to$ Block 3 首次动手: 20m $\to$ Block 4: 15m $\to$ Block 5: 25m $\to$ Block 6: 20m $\to$ Block 7: 35m $\to$ Block 8 保存重开: 15m）；首次 Roughness 上手前移至第 30 分钟窗口，保存退出重开持久化预留 8–10 分钟保护时间；所有分钟数均为**候选计划预算 (`CANDIDATE PLAN BUDGET`)**，未经大班现场容量实测；
   - **开局实施路径推荐**：对比预置 Starter 与从零建层，**建议路径 B（基于官方内置 MeetMat Sample，引导学生从零建立图层）作为全员主干路径**（减少网络分发摩擦、规避跨版本工程冲突、建立底层图层心智）；将预置 Starter 作为极个别机器卡壳学生的 Tier 3 救急保底资产；两条路径均保留目标机房实操 PC 的现场验证门禁 (`RUNTIME REQUIRED`)。

---
### 5.9 当代艺术引导材质创作教学原则与验证假设 (Contemporary Art Guidance Principles & Validation Hypothesis — 2026-10-21)

1. **教师已接受教学原则 (`TEACHER ACCEPTED`)**：
   - **四步认知闭环**：教学全流程遵循**“艺术引导 → 技术支撑 → 创作表达 → 作品验证”**的递进逻辑；
   - **技术主体原则**：PBR 物理光学原理与 Substance 3D Painter 的工业级技术学习仍是课程的绝对主体，坚守物理可信性与工业标准制作规范；
   - **引导资源定位**：当代艺术仅作为材质观察、创作判断与表达意图的引导资源（启发学生从“被动按参数”走向“主动赋予物体材质身份”），**绝非独立增加艺术史或纯理论教学单元**；
   - **四项边界红线 (Guardrails)**：
     1. 不因此改变学院既定九讲教学周历与主题顺序；
     2. 不因此增加必修软件功能或增加额外工具链要求；
     3. 不因此修改教务归档的正式考核与评分标准（平时 50% 与期末 50% 架构不变，不冻结未决分值）；
     4. 不新增独立长期单一事实来源 (SSOT) 文档，本台账即为统一决策依据。
2. **待验证假设 (`PROJECT INFERENCE / VALIDATION PENDING`)**：
   - **假设命题**：在第一讲 MeetMat 中，通过对比相同模型的不同材质身份，引导学生解释材料选择如何改变物体的意义，可能提高学生自主进行材质选择、观察和解释的能力；
   - **证据属性定界**：该效果属于项目教学法推论与待验证假设，**尚未经真实课堂验证 (`UNVERIFIED IN REAL CLASSROOM / PENDING CLASSROOM VERIFICATION`)**，严禁未经实证即宣称为既定教学成果。
3. **适用范围与推进门禁 (Bounded Scope & Rollout Gate)**：
   - **适用范围严格受限**：仅在第一讲 MeetMat 作为**有界验证候选 (Bounded Validation Candidate)** 试点，严格在既有 160 分钟计划预算内消化，不增加课堂总时间；
   - **首讲闭环推广门禁 (`GATE: PENDING W1 VERIFICATION BEFORE ROLLOUT`)**：第一讲教学设计必须经由教师审查并完成真实大班课堂验证闭环后，方可由课程负责人评估决定是否向后续课次推广；未闭环前坚决不向 W2–W9 泛化扩散；
   - **学生学习证据定界**：评估与核验指标必须聚焦于**学生对材质的选择、视觉观察和因果解释能力**（如能否在轻量材质决策卡中清楚解释材料选择如何赋予物体特定意义及其与 PBR 物理通道设置的因果映射），而非单纯看学生最终作品“是否漂亮”的主观审美评价。

---
*本台账随课程调研与设计推进持续更新，归档于 `docs/research/course-design-ledger.md`。*
