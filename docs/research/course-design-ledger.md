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
- **当前规划前沿 (Current Frontier)**：**`WEEK_1_9_CONDITIONAL_PLANNING_DRAFT_V0_2`**
  - 正式发布并硬化完成《Week 1–9 条件性排课草案 v0.2》（`week1-9-conditional-planning-draft-v0.2.md`），处于 **CONDITIONAL / NOT FROZEN** 状态；
  - 状态标识：`WEEK_1_9_CONDITIONAL_PLANNING_DRAFT_V0_2_BROWSER_ACCEPTED_AFTER_HARDENING`。

---

## 2. Stable / Accepted Boundaries (稳定边界与已确认决定)

以下原则与边界已在前期研究与讨论中确立，作为后续大纲与教学设计的基础约束：

1. **课程核心聚焦于 Material / Texture Authoring**：
   - 核心教学与训练对象是**材质与纹理创作**本身，不扩张为大而全的次世代游戏资产建模与全案制作流程。
2. **前置支撑知识的边界控制**：
   - 建模（Modeling）、拓扑（Retopology）、高低模（High/Low Poly）、UV 展开等属于材质制作的支撑性知识；
   - 教学深度以“足以支撑材质制作与贴图绘制工作流”为度，由教师预置干净资产模型，严禁喧宾夺主成为考核主体。
3. **真实教学容量约束 (Verified 9-Week / 24-Contact-Hour Reality)**：
   - 严格在单班每周 160 分钟、9 周总计 24 实际小时物理接触时间内组织教学；不设计未经验证的分钟数伪精确配额；
   - 35 人班与 17 人班维持完全一致的学习标准与考核 Rubric，现场通过四级反馈漏斗（共性讲评、自查互查、流动抽检、工件异步核验）自适应调节节奏。
4. **实践双主线分工 (Dual Practice Backbone Allocation)**：
   - **主工业资产**：小型工业复合外壳（贯穿 Weeks 1–5、7–9），承担因果分层、受控修改、烘焙交付与**终期唯一的重点精修打磨**；
   - **轻量近迁移资产**：预置 UV 陌生非金属载体（Week 6），独立完成 6 项行为与三分类迁移判断；**完成证据包归档后即闭环，后续周次不作为第二个期末精修作品**。
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

---

## 4. Open Questions & Next Actions (待决问题与后续行动)

1. **LO3 空间局部性 GUI 实操探针测试**：在合适节点组织真实 Blender 5.2 界面下的局部绘制—保存—重开验证，判定是否需触发 Painter 条件性窄对比。
2. **学校教务管理输入补全**：获取考查课平时/期末成绩比例硬性规定，获取机房 PC 硬件参数与软件预装窗口。
3. **正式执行课表冻结**：在上述 5 项门禁逐一核销后，将 Week 1–9 条件草案 v0.2 正式冻结为学期执行大纲。

---
*本台账随课程调研与设计推进持续更新，归档于 `docs/research/course-design-ledger.md`。*
