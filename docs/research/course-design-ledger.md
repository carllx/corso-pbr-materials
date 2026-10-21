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
    2. **更早进入 Blender**：学生执行最小主动操作（亲手添加 UV Sphere、位移摆放、在 Material 属性下拉直接指派预置材质 `Mat_Warmup_Sphere`，并设置 2 分钟卡壳隐藏备用球体 fallback），认识 3D Viewport、Outliner、基础材质入口、视口导航与 Material Preview；热身**不单独评分、不提交、不要求精确复刻老师场景**；灯光行为明确：Material Preview 下默认不依赖 Scene Lights (use_scene_lights=False)，避免让学生调场景灯光；
    3. **分层讲解 UI**：几何体热身只讲基础视口导航与对象材质入口；正式手电筒任务才引入 Shading 工作区、Shader Editor、材质槽与预连 `Body_Color_Tint`。保持 Option B 预置节点方案，学生不连线不建节点；
    4. **概念导入先直观再应用**：游戏/数字内容 PBR 用途与视觉悬念 $\to$ 4 个英文标准术语（Base Color, Roughness, Metallic, Normal）及大白话 $\to$ 识别光照/视角与材质的区别 $\to$ 迁移到手电筒部位。“高光会跑，别把它画死在 Base Color 里”作为核心记忆锚点；Transmission vs Alpha 直观辨析；
    5. **开场不做知识测验**：消减开场 5 分钟摸底测试，直接通过 PPT 导入与几何体热身观察；保留后段 `Predict → Operate → Explain` 判别式学习证据；
    6. **单教师大班与保护核心**：160 分钟为总计划预算（PLAN BUDGET），重构 Block 1–6 候选分钟分配并明确超时优先剪裁规则（Cut Rules）；坚决保护材料观察、学生独立决策、反馈修订、保存退出重开持久化及轻量交付课内闭环；禁止通过隐性课后作业吸收超时；
    7. **旧规则替代确认 (Supersession Notice)**：正式替代 2026-10-01 决议中关于“Week 1 零技术链路变动 / 禁止新微实验”的静态限制（仅针对几何体热身）；手电筒主线和 Option B 保护核心继续有效。
- **学期执行主线正式裁定与 Blender 备选路线保全 (Course Offering Implementation Disposition / 2026-10-21)**：
  - 决议状态：**`TEACHER ACCEPTED — PAINTER-FIRST AS CURRENT SEMESTER MAINLINE`**
  - **核心判定与路线分流**：
    1. **本学期执行主线锁定**：课程负责人正式裁定，2026-2027-1 学期以学校现有 **GR2102 九讲 Substance 3D Painter 方案**为当前执行与备课主线（Current Execution & Preparation Mainline）；
    2. **Blender-first 备选路线完整保全**：此前研发的 Blender-first 方案完整保留为未来可恢复的备选路线（Restorable Alternative Baseline）。历史研发决议（阶段 1–2、Issue #37、Draft PR #38）在其对应研发阶段完全真实有效，历史记录严禁抹除或篡改；
    3. **当前教学起点**：以学校既有课件 **第 1 讲 MeetMat 案例** 与九讲审查成果作为新的备课与机房验证起点；
    4. **知识复用与软件隔离**：按需复用 PBR 光学物理原理、Predict-Operate-Explain 任务范式与容灾机制；严禁机械移植 Blender 着色器节点网络等专有操作；
    5. **教务大纲适用性门禁隔离**：课程负责人的实操主线裁定属于教学执行组织决策，**不代表学校教务对 2024/2026 版培养方案差异及教学大纲的正式批准闭环**；Issue #39 适用性门禁继续保持 `OPEN / UNRESOLVED`。

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
   - **历史研发基线 (阶段 1–2 / 已归档备选路线)**：历史以 **Blender 5.2 LTS** 为主要实操环境；历史 Blender-first 探针与资产完整保留为未来可恢复路线；
   - **当前学期执行基线 (SUPERSEDED FOR CURRENT SEMESTER per 2026-10-21 DISPOSITION)**：依据课程负责人 2026-10-21 权威裁定，本学期（2026-2027-1）正式切换为 **Substance 3D Painter**（依托广州软件学院既有九讲课件与机房资产），作为当前实际授课与备课主线；
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

## 5. Week 1 教师试走反馈（Round 1）审计与联动修订记录 (Teacher Trial Round 1 Audit)

> **审计与证据溯源说明**：  
> 本节记录基于 2026-10-10 本地教师单人试走反馈记录（本地试走工作区归档于 `~/Desktop/Week1-Teacher-Trial-Round1-Archive`，教师试讲/试走记录由项目教师口头与现场笔记反馈给出）。  
> 严格区分 **`TEACHER-REPORTED` (教师口头/现场反馈事实)**、**`TECHNICAL FACT` (经技术复核的确定性事实)** 与 **`PROJECT INFERENCE` (教学法推论与设计修订)**，不将口头体验伪造为多样本现场实测或独立目击验证。

### 5.1 教师试走反馈、事实判定与联动修订

1. **Multiply ＋ 纯白色运算行为**：
   - **教师试走反馈 (`TEACHER-REPORTED`)**：教师在实测调节中反馈拖动 Factor 滑块时外壳完全不发生颜色变化，直观体验易产生“软件卡死或节点失灵”的误判；
   - **技术事实判定 (`TECHNICAL FACT / VERIFIED`)**：在数学正片叠底（Multiply）运算中，纯白色 $(1.0, 1.0, 1.0)$ 是乘法的中性元（$C \times 1 = C$）。当插槽 B 颜色为纯白色时，无论 Factor 取何值，运算输出与原底色完全一致，这是确定性的物理与数学运算规律；
   - **教学修订 (`PROJECT INFERENCE`)**：在 Handout、Teaching Package 与教师指引中明确校正指导语言：保护 2.1 的 Predict-before-answer 顺序（学生先预测再实操），在 Explain 解释与排错提示中明确纯白不变色是正常运算，消除“软件失灵”误解。
2. **节点命名与原生术语混淆**：
   - **教师试走反馈 (`TEACHER-REPORTED`)**：教师指出初学者容易将自定义英文标签 `Body Color Tint` 误以为是 Blender 内置的原生节点类型，增加手册检索困惑；
   - **规范事实判定 (`TECHNICAL FACT / CONVENTION`)**：代码内部保持稳定索引键 `mix_node.name = "Body_Color_Tint"`（确保自动化测试与 bpy 脚本兼容），界面展示标签规范为 `mix_node.label = "Mix (外壳调色)"`（原生类型名居前，中文提示在后）；材料统一称呼为 `Mix 节点（外壳调色 / Body_Color_Tint）`。
3. **Block 2 $\to$ Block 5 概念到界面的知识过渡与 Principled BSDF 插槽视读**：
   - **教学认知反馈 (`TEACHER-REPORTED`)**：教师反馈从 B2 四大概念进入 B5 Shading 工作区时，面对中央 Principled BSDF 着色器网络存在认知断层；
   - **界面实测事实 (`TECHNICAL FACT`)**：在真实 Blender 5.2.2 LTS 中，Principled BSDF 顶部默认可见输入插槽主要为 `Base Color`、`Metallic`、`Roughness`，而 `Normal` 插槽位于着色器靠下方独立面板中；
   - **教学修订 (`PROJECT INFERENCE`)**：在 Block 5 增设可选 30 秒概念桥接（控制在既有 15 分钟预算内），引导学生建立从 B2 到 Principled BSDF 顶部可见核心插槽（Base Color / Metallic / Roughness）的直观映射，并说明 Normal 作为微观凹凸在下方独立区域且今天不动，明确“今天只调连入 Base Color 的调色小盒子”，降低认知负荷。
4. **热身球体刻面与平滑着色**：
   - **教师试走反馈 (`TEACHER-REPORTED`)**：教师反馈 `Shift + A` 原生添加的 UV Sphere 默认为 Flat Shading，刻面棱角明显，高光呈方块状，与右侧磨砂立方体的高光对比不够圆润精致；
   - **教学修订 (`PROJECT INFERENCE`)**：在 Handout 与指引中增加可选的“右键 $\to$ 平滑着色 (Shade Smooth)”微润色步骤，使高光圆润聚拢；明确该步骤为**可选提升项 (Optional / Cuttable)**，时间紧迫可跳过，不强制增加零基础学生的必要上机门槛。

### 5.2 教学方案定位与待决事项 (Decisions & Open Items)

- **Option B 预置节点方案权威定位**：
  - **当前设计权威**：Option B 预置节点脚手架（预连节点、学生调参）为**当前已由课程负责人确认采纳的教学设计决策 (CURRENT DESIGN DECISION per Issue #37)**；
  - **实测与容量状态**：其在 35 人/17 人大班真实课堂中的理解达成与时间容量保持 **`IN TRIAL / UNMEASURED / GATE OPEN`**；若后续大班真人容量或理解验证出现过载/失效，再评估方案 C。
- **待教师最终决策事项 (Pending Teacher Disposition)**：
  1. 手电筒初始构图与 Shading 工作区入口是否需要进一步微调视口相机或预置布局；
  2. 极简几何体热身（Block 3）在大班实际排课中是否确实能够在 15–20 分钟内闭环且不挤压后段手电筒时间（需真人课堂实测样本）；
  3. 教学材料 PDF 与图文版的排版优化（已确认列为后续呈现改进，不阻塞本次教学逻辑与资产工程验证）。

---

## 6. Week 1 手电筒漆面遮罩可行性与两级管线决议 (Paint Mask & Two-Stage Recoloring Pipeline)

> **决策与证据溯源说明**：  
> 本节记录 2026-10-12 基于课程负责人 (Course Owner) 在真实 Blender 5.2.2 LTS GUI 实测对照后的权威决定与 IDE 技术验证结果。严格遵守 `AGENTS.md` 证据纪律，区分 `TEACHER ACCEPTED`、`TECHNICAL FACT / VERIFIED` 与 `PROJECT INFERENCE`。

### 6.1 教师实测问题与权威决策 (Teacher Disposition per 2026-10-12 Review)

1. **混合模式局限性实测 (`TEACHER-REPORTED / VERIFIED`)**：
   - `Multiply`：绿色乘入原始红色旧漆后，外壳明显压暗发黑发焦，无法自由替换为军绿或目标明快色彩；
   - `Mix`：Factor=1.0 时虽然能替换为目标颜色，但原始底漆的微观明暗反差与磨损划痕细节被完全抹平，呈现扁平塑料感；
   - `Color`：能够改变漆面色相与饱和度并保留明暗质感，但由于缺乏分区，原本属于银灰色的磨损划痕与裸露金属同样出现严重绿色偏色；
   - **结论**：单靠切换 Blending Mode 无法充分解决真实工业旧漆改色问题。
2. **课程负责人权威决定 (`TEACHER ACCEPTED`)**：
   - Week 1 手电筒案例应尽可能**只改变漆面颜色，坚决保留裸露金属的合理表现与银灰色泽**；
   - **预置遮罩与保护管线**：遮罩与必要保护逻辑由教师预置，学生端继续维持 Option B 的极低认知负荷边界（不建节点、不接线、不画 Mask，只操作 1 个主调色节点的 2 个原生控件）；
   - 该决定改变的是 Option B 内部技术实现，不取消 Option B 的低认知负荷教学边界。

### 6.2 资产事实与技术验证 (`TECHNICAL FACT / VERIFIED`)

1. **贴图数据分布实测**：
   - 原版 Substance PBR 资产严格遵循导体/绝缘体物理法则：红色漆面区域 Metallic 数值在 `[0.00, 0.02]` (中位数 0.000)，裸露金属/划痕区域 Metallic 数值在 `[0.50, 1.00]` (中位数 0.749)，过渡带在 `[0.15, 0.45]`；
   - **结论**：原有资产数据完全足以可靠区分漆面与裸金属，无需重新人工手绘 Mask，更无需重新展开 UV！
2. **两级原生级联管线 (Two-Stage Pipeline)**：
   - 阶段 1：学生主交互节点 `Body_Color_Tint`（类型 `ShaderNodeMix`，Blend Type 为 `COLOR`，初始 Factor=0.0，Color B 预置军绿色）；
   - 阶段 2：预置只读金属保护滤网 `Metal_Protection_Filter`（类型 `ShaderNodeMix`，Blend Type 为 `MIX`，Factor 由 `ColorRamp` 漆面遮罩驱动，A 端接原贴图保护金属，B 端接学生改色结果）；
3. **定量验证指标**：
   - **中性开局与中性恢复**：Factor=0.0 时，全车与原版 baseline 绝对最大像素差为 0（100% 像素级零偏差恢复）；
   - **漆面改色**：漆面鲜明呈现军绿、深蓝或铁灰，局部纹理方差稳定在 1.17（明暗质感与微观划痕完整保留）；
   - **裸金属保护**：改色前后裸金属区域 RGB 变化量 < 2.8 个灰度级，绝无绿色偏色，银灰色泽与高光金属感完美稳固。

### 6.3 教学适配与 Predict-Operate-Explain 升级 (`PROJECT INFERENCE`)

1. **认知负荷保持**：学生依然只面对单个高亮激活的 `Mix (外壳调色)` 节点，操作控件仍为 2 个（Factor 滑块从 0.0 拖到 0.85，拾色器选颜色），完全维持 Block 5-6 的 15/25 分钟预算；
2. **判别题升级**：
   - 2.1 基础跟进：预测拖动 Factor 时红漆变色而边缘银灰金属受保护；实操验证；解释 Metallic 遮罩分区原理（呼应 B2 金属概念）；
   - 2.2 独立迁移：判别 Factor 拉回 0.0 即可一键中性出厂复位；判别 Color 模式下纯白色输入（饱和度 0）会导致漆面去色变成灰度漆面；
3. **Week 2 教学取向指针记录 (`TEACHER ACCEPTED`)**：
   - 教师已接受决定：Week 2 以视觉问题驱动 Blend Mode 选择（Multiply/Screen/Overlay/Color），通过少量直观数学示例建立颜色计算与未来代码驱动材质之间的联系。

---

## 7. 学期主线切换与双路线协作治理决议 (Course Offering Implementation Disposition: Painter Mainline & Blender Restorable Baseline)

> **决策与证据溯源说明**：  
> 本节记录 2026-10-21 课程负责人 (Course Owner) 关于 2026-2027-1 学期实操教学路线的权威裁定。严格遵循 `AGENTS.md` 证据纪律与历史保全原则，记录路线切换、备用路线指针、跨路线复用边界以及教务大纲门禁隔离。

### 7.1 课程负责人决议背景与裁定事实 (Course Owner Decision Record — 2026-10-21)
1. **决策结论**：**`TEACHER ACCEPTED — SUBSTANCE 3D PAINTER AS CURRENT SEMESTER MAINLINE`**
2. **核心判定**：
   - **执行主线切换**：本学期（2026-2027-1）正式以广州软件学院现有 GR2102 九讲 Substance 3D Painter 方案作为当前实际执行与备课主线；
   - **历史有效性与非改写纪律**：此前研发的 Blender-first 课程方案在其研发阶段具有完全合法性与技术闭环，历史记录完整保留，不作历史抹除或掩盖；
   - **备选路线定位**：Blender-first 方案作为未来可恢复备选路线（Restorable Alternative Baseline）完整保全，后续可随时根据教务或机房条件恢复。

### 7.2 Blender-first 备用路线可恢复资产与 Git 引用索引 (Blender Restorable Alternative Lineage & Pointers)
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
  - `e5ed611fd4a4545330bb7e3da4defe65aa3a8bee`: 仓库 `main` 分支基线；
- **Blender 备用教学工程与脚本资产**：
  - [`tools/teaching/build_week1_teaching_package.py`](../../tools/teaching/build_week1_teaching_package.py): Blender 5.2 LTS 原生资产确定性重构脚本；
  - [`tools/teaching/scaffold_week1_geometry_warmup.py`](../../tools/teaching/scaffold_week1_geometry_warmup.py): 几何体热身脚手架与眼睛图标隐藏契约；
  - [`docs/research/week1-executable-teaching-package-v0.1.md`](week1-executable-teaching-package-v0.1.md): 160 分钟手电筒教学包；
  - [`docs/research/week1-student-handout-v0.1.md`](week1-student-handout-v0.1.md): 手电筒学生任务单；
  - [`tests/test_week1_realignment.py`](../../tests/test_week1_realignment.py): 跨文档自动化契约测试。

### 7.3 跨路线知识复用边界 (Cross-Route Pedagogical Boundary & Non-Transferable Operations)
在切换至 Painter 主线后，严格贯彻“方法与原理可复用、软件专有操作严禁机械移植”边界：

1. **允许并推荐复用的内容 (Portable Pedagogical Principles & Theory)**：
   - **光学与 PBR 物理因果**：能量守恒、电介质 vs 导体、微表面粗糙度与高光展宽、“高光会跑，别把它画死在 Base Color 里”核心因果；
   - **教学交互范式**：`Predict → Operate → Explain` 任务设计；
   - **轻量决策卡机制**：三字段记录结构（初次决策 $\to$ 接收反馈 $\to$ 修订动作）；
   - **课堂节奏与容灾**：160 分钟单班节奏预算、四级反馈漏斗、Recovery Ladder A/B/C 三级容灾、超时剪裁规则 (Cut Rules)、No-hidden-homework 原则；
   - **工程规范评估**：以客观物理因果与图层结构为依据，杜绝纯主观审美打分；软件退出重启持久化验证。
2. **严禁机械移植的 Blender 专有操作 (Blender-Specific Operations NOT Transferable)**：
   - **着色器节点网络操作**：Blender Shader Editor, `ShaderNodeMix` 节点, Color 混合模式, ColorRamp, Principled BSDF 插槽直接接线（Painter 依托 Layer Stack、Fill Layer、图层混合模式、Black Mask、Generator / Smart Mask，而非手动连线）；
   - **视口与交互快捷键**：Blender 3D 视口三键客、`Shift+A` 加物体、`G/R/S` 变换、`Material Preview` 内置 HDRI 机制；
   - **数据块与槽位管理**：Blender Slot 0/1/2 材质槽、Outliner 数据块打包 (Pack All)、`bpy` 自动化脚手架脚本。

### 7.4 当前执行主线：Substance 3D Painter 第 1 讲起点与最小备课/机房验证工作
依据前期九讲课件与案例审查（广州软件学院 GZUS 课件资源库审查）：

1. **教学起点确立**：
   - 以学校现有第 1 讲 PPT 课件及官方 **MeetMat 案例** 为起点；
   - **第 1 讲核心知识焦点**：Painter 界面布局、Texture Set (纹理集) 概念、视口导航与环境光照旋转、图层堆栈 (Layer Stack) 与填充图层 (Fill Layer)、基础通道 (Base Color / Roughness / Metallic)、材质球指派与基础贴图导出。
2. **最小必要备课与机房实机验证清单 (Minimal Lab Verification Checklist)**：
   - **Gate A-1 (环境与授权核查)**：核实机房工作站安装的 Substance 3D Painter 确切版本（2020 / 2022 / 2024 / Steam 版或独立版），确认显存（建议 $\ge 4$GB）与驱动正常；
   - **Gate A-2 (MeetMat 资产工程完备性)**：在机房实机打开 MeetMat 初始工程或导入 `MeetMat.fbx`，核验各 Texture Set (Head, Body, Base) 正常映射且无丢材质报错；
   - **Gate A-3 (干净练习工程制作)**：准备供学生开局的空白/初始工程，杜绝包含历史已完成图层的“剧透”工程混入下发包；
   - **Gate A-4 (保存与重开持久化)**：实测保存为 `.spp` 工程，完全退出 Painter 进程，重新打开验证图层与贴图无丢失；
   - **Gate A-5 (轻量交付通道测试)**：测试学生导出 1 张视口渲染快照（Viewport Render / Iray snapshot）或一组标准贴图，验证机房网络收件可行性；
   - **Gate A-6 (先修技能门禁)**：确认学生是否具备基础 UV 概念认知，在讲授中明确 Texture Set 与 UV Tile 的对应关系。

### 7.5 课程负责人决策权威 vs 学校正式教学大纲适用性双轨定界
- **实操执行 vs 培养方案适用性定界**：
  - **轨 1（学期教学执行）**：Course Owner 裁定 Painter 主线即日起生效，指导当下备课与机房排课；
  - **轨 2（教务合规与培养方案）**：Issue #39 暴露的 2024/2026 培养方案学时差异（12 理论 + 24 实践 vs 18 理论 + 18 实践）、课程代码差异（GR2102 vs GR2018）、4 学时 PBR 综合实验定位，以及本学期 2026 秋授课班级（GR2102-1 / GR2102-3）正式执行的教学大纲版本，**继续保持 `UNRESOLVED / GATE OPEN` 门禁**；
- **纪律红线**：课程负责人的务实主线选择，**绝不臆测或伪称学校教务部门已完成正式审批或大纲勘误**；正式大纲状态待教务部门正式文件回执后方可核销。

### 7.6 GitHub 执行路线对齐、工单承载与交付成果 (2026-10-21)
1. **GitHub 工单映射与路线重定向**：
   - **Roadmap #1**：发表 Frontier Override 评论，正式重定向 Active Frontier 至 Painter-first 主线，明确旧 Blender 路线历史归档为可恢复备用路线；
   - **Issue #13**：发表 Route Lineage 评论，明确记录原 Blender-first v0.4 综合工作在历史 PR #18 处归档保全，历史记录不作静默篡改；
   - **创建新工单 [Issue #40](https://github.com/carllx/corso-pbr-materials/issues/40)**：作为当前学期 Painter-first 实施主线的承载工单（`Implementation — Painter-first 主线启动：第一讲 MeetMat 教师审查版与后八讲低分辨率依赖对照`），标签 `ready-for-human`，关联 #1、#13、#22、#39；
2. **核心成果物落位**：
   - **第一讲教师审查版教学草案**：[`docs/research/painter-week1-meetmat-teaching-draft-v0.1.md`](painter-week1-meetmat-teaching-draft-v0.1.md)
     - 涵盖课程整体介绍 (Orientation 15min)、PBR 核心物理通道的生活化直观比喻与科学边界；
     - 包含 MeetMat 准确操作示范步骤（界面/视口三键客/Shift+右键光照旋转/Texture Set/Fill Layer/Black Mask/Smart Material/Iray）；
     - 160 分钟单班节奏预算、3 条硬性超时剪裁规则 (Cut Rules)、四级反馈漏斗与 No-hidden-homework 原则；
     - 学生轻量三字段材质决策卡、保存退出重开持久化验证与三级机房容灾梯队；
     - 暴露并纠正原课件考勤分 10% 冲突，学时口径差异保持待核。
   - **后八讲低分辨率依赖对照**：[`docs/research/painter-courseware-dependency-contrast-w2-w9.md`](painter-courseware-dependency-contrast-w2-w9.md)
     - 梳理 9 讲能力递进线（消除换预设的机械重复）；
     - 提出 3 次平时作业（W2 塑料、W4 金属、W7 次表面）于 160 分钟课内独立完成的候选落位方案（待教师审定）；
     - 梳理 W7–W9 综合期末大作业候选边界（质量优先+简短说明与过程证据，Issue #22 待定）；
     - 支撑技术（UV/拓扑/烘焙）坚决防止反客为主，实操深度保持候选（剥离复杂肌肉拓扑超载负荷，资产预置为主）；
     - 评估第三方连接环境（建议 Blender 作为主要实操出口，Maya/Arnold 作为演示/选做候选，规避机房授权水印风险）；
     - 安排第 6 讲或第 9 讲轻量级 Blender-only 节点对照候选，仅作视野拓展不设为考核。
3. **事实探针结论与最小纠偏 (2026-10-21)**：
   - **官方 API 规范确认**：依据 2026-09-17 官方 `layerstack` API 文档，更正关于无法脚本创建 Fill Layer 与 Mask 的错误判断，确认现代 Painter 技术上已支持；同时维持“目标机房实际软件版本与脚本运行时未经实机验证 (`RUNTIME GATE OPEN`)”的门禁；
   - **第二讲 `.spp` 复用定位更正**：明确不建议直接作为学生 Starter（规避向下兼容报错与认知倒错），但完整保留其作为教师备课参考成品及开课前通过 GUI 提取干净白模 (`File -> Export Mesh`) 的可能，待机房真实 GUI 验证 (`PENDING GUI VERIFICATION`)。

---
*本台账随课程调研与设计推进持续更新，归档于 `docs/research/course-design-ledger.md`。*



