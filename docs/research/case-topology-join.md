# 教学案例排课拓扑综合论证报告 (Case Topology Join)

> **文档定位**：本报告响应 GitHub Issue #19 契约及最新复核指引（Browser Review / Course-Owner-readiness pass），作为 #19 Case Topology Join 的最终交付物。报告直接消费已合并至 `main` 的两份上游核心循证成果——《选定权威文献材质行为调研与初学者代表性材质集》（`docs/research/material-behavior-map.md`，#20）与《循证教学案例与实践审计报告 Phase A》（`docs/research/practice-evidence-audit.md`，#19 Phase A），同时将 Issue #21 当前状态（PR #25，`CONTENT PASS / RUNTIME GATE OPEN`，外部 Web 查看器未获端到端验收）作为并行同级约束（Sibling Constraint）。  
> **决策层级界定**：
> 1. **已锁定宏观边界 (Fixed Macro Boundary)**：W1–W6 教学演练与 W7–W9 全新综合期末大作业彻底解耦；“全程 9 周单手电筒贯穿”仅作为**历史已废弃基线 (Historical Rejected Baseline)** 归档；
> 2. **本报告核心任务**：对 W1–W6 教学演练阶段的案例拓扑选项展开横向比对，并提出基于实证的智能体推荐（Agent Recommendation）；
> 3. **核心边界与门禁纪律**：
>    - M1–M8 是本项目面向初学者的教学原型集（Project Pedagogical Synthesis），不是绝对物理分类法；
>    - 所有课时与时间开销均为规划估算（Planning Estimates），非真实机房硬实证；
>    - 绝不重新打开已验收的 Week 1 基线；
>    - **最终采纳状态**：本报告拓扑方案已获 Course Owner 正式采纳（**`TEACHER ACCEPTED — BOUNDED HYBRID W1–W6 TOPOLOGY BASELINE`**）；
>    - **宏观边界**：W1–W6 基础演练 $\neq$ W7–W9 全新独立综合期末大作业（Fixed Macro Boundary）；
>    - **未决门禁提示**：Teacher Acceptance 不等于资产与运行时实现已全部验证完成，`[GATE-ASSET-01]`、`[GATE-ASSET-02]`、`[GATE-RT-01]` 及具体 Normal Bake 实操形式继续保持 `UNRESOLVED / CONDITIONAL`；
>    - 严禁启动 Issue #22，严禁生成课表 v0.4，严禁启动 Week 2 教学包，严禁修改或合并 PR #18。  
> **门禁状态**：`TEACHER ACCEPTED — BOUNDED HYBRID W1–W6 TOPOLOGY BASELINE`。

---

## 1. 论证背景、已锁定边界与同级约束输入 (Context & Fixed Inputs)

### 1.1 已锁定宏观边界 (Fixed Macro Boundary)
根据 Course Owner 明确确立的教学大纲宏观决议：
- **全课划分为两个性质根本解耦的教学阶段**：
  - **第一阶段（W1–W6）**：教学基础演练与核心能力建构（Teaching / Practice Backbone）；
  - **第二阶段（W7–W9）**：开启全新的综合期末大作业（New Comprehensive Final Project），由 Issue #22 独立设计；
- **历史基线废止**：历史草案中“老式手电筒（Vintage Flashlight）做满 9 周并作为期末作品”的假说已被正式否决，仅保留为**历史已废弃基线 (Historical Rejected Baseline)**，不再作为活跃待选方案。

### 1.2 上游成果消费基准 (Consumed Upstream Baselines)
- **材质行为全景与代表性材质集（Issue #20 / PR #23，commit `b209878`）**：
  - 确立了基于 OpenPBR v1.1.1、Adobe PBR Guide (3rd ed) 与 Dinur (2026) 的 PBR 物理机制空间；
  - 提炼了 M1–M8 初学者代表性材质教学原型集（M1 哑光介电质、M2 光滑施釉介电质、M3 抛光金属、M4 粗糙金属、M5 复合漆面磨损、M6 风化锈蚀、M7 缝隙积灰、M8 微浮雕法线）；
  - 明确了单一手电筒资产在 M1（纯漫反射）与 M2（镜面施釉）上存在天然材质覆盖盲区；而其对 M6（锈蚀）与 M7（积灰）的承载性仍属于**推论性假设（`PROJECT INFERENCE / REQUIRES ASSET INSPECTION`）**。
- **案例特征与实践动作审计（Issue #19 Phase A / PR #24，commit `f37bdf5a`）**：
  - 确立了 Vintage Flashlight（~11K tris，`ADAPT_CANDIDATE`）、Antique Ceramic Vase 01（~9K tris，`REUSE_CANDIDATE`）、Classical Bust（高低模对，`ADAPT_MICRO_ONLY`）与历史资产（`REFERENCE_ONLY`）的资产事实基准；
  - 明确高低模从零全流程烘焙在机房面临显著教学摩擦，不可作为默认全员实操（具体实操深度待排课与机房验证确定）；近迁移练习需具备流程隔离。
- **Week 1 教学实施包已验收锁定（Issue #11 / #15 / #14）**：
  - Week 1 的 160 分钟教学结构（包含开局 15 分钟课程整体介绍）已被 Course Owner 验收锁定（`TEACHER ACCEPTED WITH DELTAS`），**本工单绝不重新打开 Week 1，不向 Week 1 插入新的微实验**。

### 1.3 兄弟工单同级约束 (Sibling Constraint: Issue #21 / PR #25)
- **实时导出与外部查看器状态**：最新审阅裁决为 **`CONTENT PASS / RUNTIME GATE REMAINS OPEN`**；
- **交付要求红线**：glTF 2.0 通道语义与 Blender 导出参数已获审定，但**外部 Web/离线浏览器查看器尚未在真实教学机房完成端到端（E2E）受控探针验证，绝不能作为已采用的教学交付要求**；
- **兜底基线（Fallback）**：在真实机房 Web 探针通过前，交互验证的权威基准严格保留在 **Blender 5.2 原生视口渲染（EEVEE Next / Material Preview）**，拓扑设计不得将跨进程 Web 查看器设为必选阻断路径。

### 1.4 真实教务容量与教师负荷硬约束 (Offering & Capacity Constraints)
- **教务事实**：全课 9 周、36 教学课节（每课节 40 分钟）、单班每周排定面授 160 分钟、单班总面授 **24 实际小时 (contact hours)**；
  - **W1–W6 教学演练阶段**：共 6 周 × 4 课节 = 24 教学课节 = 960 分钟 = 16 实际面授学时；
  - **W7–W9 期末大作业阶段**：共 3 周 × 4 课节 = 12 教学课节 = 480 分钟 = 8 实际面授学时 (8 contact hours，非“8课时”)；课外自习打磨仅作为建议性工作量（Recommended Workload），不是保证的容量来源或通过性门槛；
- **单师双班结构**：单一教师承担 **GR2102-1（35 人大班）** 与 **GR2102-3（17 人小班）**，总计 52 名学生；
- **反馈承载力算术与瓶颈**：在 35 人大班中，单次 160 分钟课堂若组织全员排队逐一深度讲评，人均理论时长仅约 $160 / 35 \approx 4.6$ 分钟，且会导致严重的课堂空转等待。因此，**在实操上面向全班进行流水线式的逐人深度 1:1 当面反馈是不可行的（Impractical）**。任何导致资产环境混乱、频繁触发低级文件/格式排错的拓扑，都会剧烈消耗教师的辅导带宽。

---

## 2. W1–W6 案例排课拓扑选项比对 (Evaluation of W1–W6 Topologies)

在“W1–W6 教学演练 $\to$ W7–W9 全新期末项目”的已锁定宏观边界下，本次 Join 聚焦评估 W1–W6 阶段的 3 种待选案例组织方案（同时将全 9 周单手电筒作为历史已废弃基线对比呈现）：

- **历史已废弃基线：9 周全程单手电筒 (Historical Rejected Baseline)**  
  全课程 9 周贯穿使用单一手电筒资产，直至结课。*(已废弃：直接违背 Stage 4 期末解耦决策，压低期末质量)*
- **选项 A：单一/有限主案例模型 (Single / Limited Main Case within W1–W6)**  
  W1–W6 仅围绕单一工业资产（Vintage Flashlight）逐步深入推进，完成基础与进阶练习。
- **选项 B：阶段性递进代表性案例模型 (Staged Representative Cases)**  
  W1–W6 划分为 2–3 个独立阶段，每阶段彻底更换一款专精特定材质行为的新模型（如阶段一基础介电质、阶段二工业金属、阶段三复合涂层）。
- **选项 C：有限主案例 + 有界代表性微案例模型 (Bounded Hybrid: Limited Main Case + Bounded Micro-Cases)**  
  以单一复合工业资产（Vintage Flashlight）为主干，穿插 1–2 个高度预置、免配置摩擦的轻量微案例（W3 或之后安排石膏胸像法线观察微实验；W6 安排预置陶瓷花瓶近迁移测试）。

### 2.1 七维全景比对矩阵 (Comprehensive 7-Dimension Matrix)

| 评价维度 | 历史已废弃基线：9 周全手电筒 (Historical Baseline) | 选项 A：W1–W6 单一主案例 (Limited Main Case) | 选项 B：W1–W6 阶段递进模型 (Staged Cases) | 选项 C：W1–W6 有限主案例 + 有界微案例 (Bounded Hybrid) |
| :--- | :--- | :--- | :--- | :--- |
| **1. 材质行为覆盖度<br>(Material Coverage)** | 🔴 **严重受限**<br>Flashlight 天然缺乏大面积均质哑光漫反射（M1）与施釉高光（M2）；M6 锈蚀与 M7 积灰仅为推论假说。 | 🔴 **局部存在盲区**<br>手电筒能较好支撑 M3–M5，但无法直观提供 M1 与 M2 教学载体；M6/M7 尚待实测核验。 | 🟢 **行为覆盖专精**<br>各阶段可针对性挑选模型对应 M1、M2 及金属行为。 | 🟡 **良好 (有界补齐)**<br>手电筒支撑 M3–M5 主线；微案例轻量补齐 M1（石膏）与 M2（花瓶）；M6/M7 保持条件性候选。 |
| **2. 知识迁移与检验能力<br>(Knowledge Transfer)** | 🔴 **无独立检验**<br>全流程单模型，无法检验脱离教程示范后的独立抽象能力。 | 🔴 **缺乏近迁移样本**<br>缺乏独立陌生载体检验学生对非金属菲涅尔等规则的自主判断力。 | 🟡 **多次短迁移**<br>经历多次换模；但在频繁适应中，可能弱化对单一因果逻辑的深入推演。 | 🟢 **具备标准近迁移**<br>W6 预置陌生非金属载体（花瓶），可有效进行“三分类因果判断”测试。 |
| **3. 资产切换与配置成本<br>(Setup / Switching Cost)** | 🟢 **零切换**<br>全课无资产更换摩擦。 | 🟢 **零切换**<br>W1–W6 无重新理解模型网格、UV 象限与着色槽的时间损耗。 | 🔴 **切换摩擦显著**<br>*(风险假说)* 多次导入新模型易导致学生耗费额外时间对齐网格、UV 与材质槽。 | 🟡 **中度可控**<br>微案例严格限制为“预置完成、免配置/只读”，严禁引入微资产的全套建模或展开流程。 |
| **4. 35/17 单师反馈承载力<br>(Single-Teacher Capacity)** | 🟡 **表面统一/甄别弱**<br>格式统一，但 35 人班易出现参数雷同，难辨真实掌握程度。 | 🟢 **格式高度收敛**<br>单一资产使 35 人班能高效运行自查清单与投屏共性纠偏，减少个别排错干扰。 | 🔴 **排错阻滞风险**<br>*(风险假说)* 35 人大班中，多次换模易集中爆发材质槽漏指定、贴图断裂等低级格式问题，挤占单师带宽。 | 🟡 **承载良好但需隔离**<br>主干运行稳定；关键在于 W6 必须严格隔离近迁移实操与阶段总成，避免双任务并发。 |
| **5. 期末作品质量支撑<br>(Final-Work Preparation)** | 🔴 **直接违背决策**<br>手电筒缺乏独特性，无法构成高质量个人 Portfolio，且违反 Stage 4 解耦边界。 | 🟡 **因果打磨深/形态单**<br>为 W7–W9 提供了扎实的工业金属因果经验，但在非金属釉面与有机质感上准备较弱。 | 🟡 **多而不精**<br>各阶段浅尝辄止，缺乏对单一复杂人造物进行深入因果分层打磨的完整体验。 | 🟢 **支撑充分**<br>既通过手电筒建立了深入的因果分层经验，又通过微案例拓宽了非金属理解，有效衔接 W7–W9。 |
| **6. 失败恢复与容灾负担<br>(Recovery / Failure Burden)** | 🔴 **早期缺陷持续带入**<br>前周的节点混乱若未发现，将直接损害结课质量。 | 🟡 **主干需版本存档**<br>若前期工程损坏需依赖教师分发的阶段标准存档（Starter Save）。 | 🟢 **阶段解耦**<br>单阶段失误不直接拖累下一阶段，具备局部容灾优势。 | 🟢 **双重容灾**<br>主资产依赖阶段存档保护；微案例若遇环境问题可随时降级为教师投屏演示，不阻断主线。 |
| **7. 未决门禁影响与依赖<br>(Unresolved Runtime Gates)** | 🔴 **门禁直接冲撞期末**<br>直接面临 #21 Web 导出未决门禁与烘焙门禁对结课考核的阻断风险。 | 🟡 **承受主干门禁**<br>主要受制于手电筒网格切片核验与 Blender 5.2 局部遮罩修改探针。 | 🔴 **门禁成倍累加**<br>教研团队必须为 3 套不同模型分别跑通网格流形、UV 与视口着色探针。 | 🟡 **依赖有界隔离**<br>仅需核验手电筒（主干）与花瓶模板（W6）；将 #21 导出未决状态安全隔离在平时练习之外。 |

---

## 3. 核心权衡分析与推论审视 (Trade-off Analysis & Evidence Labeling)

### 3.1 选项 A（W1–W6 单一主案例）的局限
- **核心优势**：在 35 人单师课堂中，单一资产能将软件操作与文件管理摩擦压缩至最低，使师生能专注于 Principled BSDF v2 节点因果逻辑与微表面粗糙度控制；
- **主要短板**：根据《材质行为图谱》（#20），手电筒缺乏大面积均质漫反射（M1）与厚玻璃态施釉面（M2）。若前六周完全不接触陌生非金属载体，学生在面对非金属菲涅尔与光滑高光时缺乏独立判断检验，对 W7–W9 期末大作业的非金属选型支撑不足。

### 3.2 选项 B（W1–W6 阶段递进模型）在 35 人单师大班的教学摩擦
- **资产切换的认知与操作摩擦**：`[ILLUSTRATIVE PLANNING SCENARIO / RISK HYPOTHESIS]` 在初学者阶段，每引入一套全新几何资产，均伴随对网格部件划分、法线朝向、UV 象限及着色槽映射的重新适应；
- **单师反馈容量承载挑战**：在 35 人大班中，单次 160 分钟面授支持全员逐一深度讲评在实操上不可行（人均理论时间仅约 4.6 分钟）。若频繁更换资产导致材质槽漏指定、贴图路径丢失等低级格式排错并发增加，教师将难以维持对核心物理着色与审美质感的有效辅导；
- **打磨深度受损**：分段练习容易导致学生停留在各资产的基础填色阶段，缺乏对“基材—底漆—磨损—积灰”这一完整服役因果链条的深层推演。

### 3.3 选项 C（有限主案例 + 有界微案例）的平衡逻辑与微观纪律
- **互补平衡**：以手电筒为贯穿主干，保障因果分层与受控修改的打磨深度；以轻量微案例定向弥补 M1 与 M2 盲区；
- **消除 Week 1 干扰**：严格尊重已锁定的 Week 1 结构（15 分钟导引 + 基础练习），**不得在 Week 1 插入石膏微实验**。古典石膏胸像的法线与剪影对比微实验仅作为 **W3 或之后的候选安排窗口 (Candidate Placement Window)**；
- **W6 课时建议与流程隔离**：
  - `[PLANNING RECOMMENDATION / ESTIMATE]` 建议 W6 单节 160 分钟面授进行明确的阶段切分：前半段以预置模板进行花瓶近迁移测试（建议规划估算约 40–50 分钟），完成三分类因果判断后即刻归档；后半段集中推进主干练习总成与期末项目导引；
  - 该课时切分仅作为规划建议估算，具体时间分配留待后续排课草案综合阶段与 Course Owner 审定，严禁在课堂中让两套资产无序穿插。

---

## 4. 智能体推荐方案与前置能力支撑 (Agent Recommendation & Prerequisite Capabilities)

基于上述权衡，提出以下明确的智能体推荐意见，提交 Course Owner 审定：

> ### 智能体推荐与负责人采纳结论 (Recommendation & Teacher Acceptance Disposition):
> 1. **已锁定宏观边界**：**W1–W6 教学基础演练 与 W7–W9 全新综合期末大作业彻底解耦 (Fixed Macro Boundary)**；
> 2. **W1–W6 案例拓扑基线**：**采纳选项 C（有限主案例 + 有界代表性微案例模型，Bounded Hybrid）**；
> 3. **最终决策状态**：**`TEACHER ACCEPTED — BOUNDED HYBRID W1–W6 TOPOLOGY BASELINE`**（智能体推荐已获 Course Owner 正式裁定采纳）；
> 4. **技术门禁前提**：采纳不等于资产与运行时已验证闭环，`[GATE-ASSET-01]`、`[GATE-ASSET-02]`、`[GATE-RT-01]` 及 Normal Bake 具象实操方式继续保持未决与条件性约束。

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                    已锁定宏观边界：W1–W6 教学演练 与 W7–W9 期末大作业彻底解耦                     │
└───────────────────────────────────────────┬─────────────────────────────────────────────┘
                                            │
        ┌───────────────────────────────────┴───────────────────────────────────┐
        ▼                                                                       ▼
┌───────────────────────────────────────────────┐       ┌───────────────────────────────────────────────┐
│      【推荐】W1–W6 教学演练：选项 C 有界混合模型   │       │      【锁定】W7–W9 全新独立综合期末大作业      │
│   (Limited Main Case + Bounded Micro-Cases)   │       │      (New Comprehensive Final Project)        │
├───────────────────────────────────────────────┤       ├───────────────────────────────────────────────┤
│ • 核心主干：Vintage Flashlight (攻坚 M3, M4, M5)│       │ • 资产定位：全新综合资产（严禁 Flashlight）   │
│ • 微实验观察：Classical Bust (W3+ 候选窗口, M8) │       │ • 容量定义：12 教学课节 / 480 分钟 / 8 接触学时│
│ • 近迁移测试：Antique Ceramic Vase 01 (W6, M2) │       │ • 核心机制：面向新资产独立应用前置能力        │
│ • 产出归档：W6 形成性证据包归档即止，不入期末 │       │ • 具体设计：由 Issue #22 独立制定规范与标准   │
└───────────────────────────────────────────────┘       └───────────────────────────────────────────────┘
```

### 4.1 推荐理由与实证支撑 (Justification & Traceability)
1. **最大化保护 35 人单师课堂教学带宽**：W1–W5 主线资产保持稳定，教师能持续依托投屏共性讲评与标准化 Checklist 推进辅导，避免大班排错阻塞；
2. **结构化补齐代表性材质行为**：
   - **M3 (镜面金属) / M4 (工业金属) / M5 (复合磨损漆面)**：由手电筒主干深度攻坚；
   - **M1 (哑光漫反射) / M8 (法线浮雕)**：作为高低模法线微案例候选（Active Teaching Candidate，非默认 45 分钟全员完整烘焙；实操形式如演示 vs 引导微实验 vs 拓展待排课综合与机房验证确定）；
   - **M2 (玻璃态施釉面)**：在 W6 通过预置花瓶工程完成独立近迁移判断；
   - **M6 (风化锈蚀) / M7 (缝隙积灰)**：根据 #20，手电筒对二者的承载性保持为**条件性候选（`candidate coverage pending GATE-ASSET-01`）**，若原模不理想可使用替代示例或由后续教研决定，不妄称全量闭环。
3. **清晰的失败容灾与阶段重启**：W1–W6 练习在 W6 归档后即告一段落；W7 进入期末大作业时学生基于新资产轻装上阵，消除前期练习的历史包袱。

### 4.2 W1–W6 为 W7–W9 期末大作业提供的前置核心能力 (Prerequisite Capabilities)
本工单（#19）不预设期末大作业的具体形式，仅明确 W1–W6 演练必须为 W7–W9 输送以下前置能力支撑：
1. **物理通道与参数解构力**：熟练掌握 Principled BSDF v2 核心滑块（Base Color, Metallic, Roughness, Normal, IOR, Coat）的物理含义，破除“反光即金属”、“纯白即 255”等初学者误区；
2. **材质因果与分层构建力**：能通过黑白遮罩、程序化噪波扰动与几何特征，构建“基底材质 $\to$ 表面涂层 $\to$ 磨损/脏迹”的物理因果分层网络；
3. **视口交互与 LookDev 自检力**：能在多方向环境光源与不同粗糙度下，利用 Blender 原生视口渲染（EEVEE Next / Material Preview）独立自查贴图断裂与高光响应；
4. **近迁移分类判断力**：具备在陌生几何与材质载体上辨识“直接适用 / 调整后适用 / 规则不适用”的物理规律迁移思维。

---

## 5. 未决门禁与后续必要探针清单 (Unresolved Gates & Required Probes)

为确保上述推荐方案在后续工程落地（Issue #22 期末设计与排课草案 v0.4）时不发生技术悬空，梳理以下必须核销的未决门禁：

| 门禁标识 | 关联工单与领域 | 当前状态 | 阻塞范围与影响 | 核销条件与所需探针动作 (Required Probe) |
| :--- | :--- | :---: | :--- | :--- |
| **`[GATE-RT-01]`<br>实时 Web 查看器探针** | Issue #21 / PR #25<br>(Realtime Export) | **OPEN**<br>(Content Pass / Runtime Open) | 阻断将“外部 Web/离线 HTML 查看器”列为必选交付项。 | 在典型机房环境（断网无外网环境）下，实测通过本地打开 GLB 查看器，验证是否存在 CORS 拦截或 GPU 崩溃；**未通过前，基线严格保持为 Blender 原生 EEVEE 视口验证**。 |
| **`[GATE-ASSET-01]`<br>Flashlight 运行时切片核验** | Issue #19 / 资产工程<br>(Asset Provenance) | **OPEN**<br>(Pending Inspection) | 决定 W2–W5 练习切片的平滑度，以及 M6 锈蚀 / M7 积灰的承载真实性。 | 对 Poly Haven 原版 Flashlight 进行运行时网格解构，核验：1) 三角面与非流形状态；2) UV 象限是否有重叠拉伸；3) 部件材质槽清晰度；4) M6 锈蚀与 M7 积灰是否有合理几何载体。 |
| **`[GATE-ASSET-02]`<br>Vase 01 预置模板核验** | Issue #19 / W6 迁移<br>(Near-Transfer) | **OPEN**<br>(Pending Inspection) | 影响 W6 近迁移练习的零摩擦启动。 | 制作一份开箱即用的 `.blend` 模板工程，核验学生能否在受控时间内仅凭调整节点参数与遮罩完成釉面与粗陶分层，确认无前置报错。 |
| **`[GATE-FINAL-01]`<br>期末项目规范裁定** | Issue #22<br>(Final Assignment) | **BLOCKED**<br>(Awaiting #19 Close) | 决定 W7–W9 期末大作业的具体实施路径、资产库与评分标准。 | 在本工单（#19 Join）经 Course Owner 裁定并合并后，由 Issue #22 独立进行期末大作业的方案制定与审定。 |

---

## 6. 留待 Issue #22 独立解答的核心问题 (Open Questions for Issue #22)

为坚决维护 Issue #22 的独立设计权威，本工单不做越界预设，将以下与期末项目密切相关的设计问题完整移交给 Issue #22：

1. **期末项目资产供给策略**：是由教师提供受控的候选资产包（Controlled Asset Bundle），还是允许学生在受控参数规格下自主选型/提交资产并经过教师审题？
2. **单人独立 vs 分组协作**：期末大作业采取个人独立全流程完成，还是允许轻量分组协作？
3. **W7–W9 课内三周组织节奏**：在 12 教学课节（480 分钟）内，立项指导、中期答疑与终期讲评的课时切分与检查点如何设立？
4. **交付物规格与出口规范**：期末交付物是以 Blender Cycles / EEVEE 离线高精度 LookDev 渲染图为主，还是在 Issue #21 门禁放行后引入实时资产交付？
5. **考核评价细则 (Rubric) 与平时/期末权重**：期末作业的技术与艺术评分维度如何界定？平时练习（W1–W6 形成性证据）与期末项目的具体成绩比例如何配合教务大纲冻结？

---

## 7. NotebookLM 外部知识库交叉核验附录 (Appendix: NotebookLM Cross-Source Integrity Check)

依据 Issue #13 流程复盘与 Issue #19 门禁契约，在 Course Owner 最终裁定前，调用项目已登记的外部知识库能力对本报告核心结论进行窄域交叉核验（Cross-Check）。核验凭据、局限性与结果记录如下：

### 7.1 核验能力环境与访问路径 (Capability Provenance & Execution)
- **Target Capability**: Course Knowledge Notebook (课程领域知识库)
- **Provider**: Gemini NotebookLM
- **Locator**: `e29f9644-03b2-4e1b-bcb0-b954b5bf08be`
- **Execution Host & Path**: 本地 IDE 环境依托 `notebooklm` CLI 成功执行 `source list` 并返回就绪（READY）的已登记来源，通过只读 `ask` 查询完成了本轮检索与问答综合；
- **权威性界定与次级凭据定位**: NotebookLM 输出属于外部研究与检索凭据（Reported with Provenance），不自动构成项目权威（Project Authority）。

### 7.2 三大核心问题检索结论 (Actual Cross-Check Findings)

1. **Q1: 案例组织拓扑（有限主案例+微案例 vs 频繁换模）**：
   - **判定**: **`NOT FOUND` (显式课程拓扑比较) / `AMBIGUOUS & COMPLEMENTARY` (实践先例)**；
   - **真实语料返回与上下文**:
     - 语料库来源未在理论层面显式讨论或对比初学者课程案例组织策略（单主资产配微案例 vs 频繁换模）；
     - 但在实践案例上存在互补先例：
       - **单一复杂主资产先例**：Zeeshan Jawed Shah《Realistic Asset Creation with Adobe Substance 3D》（来源 `6a26e0ee-...`）全书实践围绕单一高精细度的工业主道具——**老式收音机 (Antique Radio)** 展开，逐步贯穿参考、建模、烘焙、分层绘制（漆面金属、积灰、边缘磨损、玻璃）与渲染全流程，证明围绕单一复杂资产展开渐进教学是贴图专著的既有实践；
       - **多资产/微案例孤立演示先例**：Eran Dinur《The Complete Guide to Photorealism》（2021 版，来源 `0d62fe50-...`）则采用数十种独立的多样化微案例（如锈铁板、陶瓷茶壶、涂漆墙面、塑料玩具等）孤立剖析特定物理着色行为，而非全程跟随单一资产；
       - **技术规范与工具文档**：OpenPBR Surface 规范与 Khronos glTF 2.0 等技术文档专注于着色算式与交换参数，对教学法拓扑保持沉默（silent on pedagogy）。
2. **Q2: 关键实践动作的语料直接证据**：
   - **Normal / Bake 作为有界对比微实验**: **`PARTIALLY FOUND`**。Dinur (2021) Ch 13 明确提供了“法线贴图仅扰动着色法线，掠射角剪影保持平整”的视觉对比原理；但将 Bake 裁减为免配置只读微实验在语料中为 `NOT FOUND`（属于本项目针对机房排错负荷的教学法推论）；
   - **光滑非金属 / 陶瓷类材质学习**: **`FOUND`**。Adobe PBR Guide (Pt 1 & 2)、OpenPBR 规范、Blender 手册与 Dinur (2021) Ch 9 详尽阐述了非金属弱高光（$F_0 \approx 0.04$）、无色反射、菲涅尔效应与双层施釉（Clearcoat）物理机制；
   - **跨资产知识迁移与三分类评测**: **`NOT FOUND`**。语料聚焦于具体资产步骤或物理通则，未提及跨载体近迁移三分类测试设计（属于本项目教学评价推论）。
3. **Q3: 宏观阶段解耦冲突检查 (Contradiction Check)**：
   - **判定**: **`NO CONTRADICTION FOUND`**；
   - **真实语料返回与上下文**: 语料库中没有任何来源强制要求基础练习资产必须贯穿带入期末大作业，亦无任何来源反驳 W1–W6 基础演练与 W7–W9 独立期末大作业的 6+3 解耦模式。

### 7.3 语料版本局限性说明 (Corpus Freshness & Authority Limitations)
- **版本差异事实**: 仓库规范一手文献研究严格锁定 Dinur (2026) 2nd edition 与 OpenPBR v1.1.1 规范；而 NotebookLM 交叉核验调用的语料库现存来源包含早期版本（Dinur 2021 1st edition 与 OpenPBR v1.1 标题）；
- **权威性约束**: 这一版本差异并未在本次 Q1–Q3 核心物理与拓扑逻辑上产生实质性结论冲突，但充分表明：**NotebookLM 外部检索仅作为辅助性交叉验证凭据，绝不覆盖（does not override）项目权威一手文献与仓库审计的基准地位**。

### 7.4 初始交叉核验结论与分流 (Initial Integrity Verdict)
- **路线冲突判断 (Route-Changing Conflict)**: **`NO`**；
- **处置**: 语料库既未提出反驳证据，亦未提供足以推翻当前 W1–W6 推荐案的外部新事实。

### 7.5 CORE42 部署后专项决策支持实证审计 (Post-Deployment CORE42 Decision-Support Audit)

在完成 CG Cookie CORE V1 (Blender 4.2) 5 大认知源于 Course Knowledge Notebook 的规范部署后（部署注册表见 `docs/research/core42-deployment-registry.md`），针对本报告推荐的拓扑方案与教学机制，围绕 6 大核心议题执行了基于真实课时文本的专项闭环审计：

| 评估维度与审计议题 | 判定结果 | CORE42 来源与核心课时锚点 (`lesson_id`) | 真实教学事实与上下文证据 (Citation / Context) | 教学法边界与客观局限性 (Limitations) |
| :--- | :---: | :--- | :--- | :--- |
| **1. Limited Main Case + Bounded Micro-Cases**<br>(有限主案例 + 有界微案例混合拓扑) | **`SUPPORTS`** | • `CORE42_OVERVIEW.md`<br>• `CORE42_CASE_INDEX.md`<br>• `CORE42_MATERIALS_AND_SHADING.md`<br>• `CORE42_TEXTURING_WORKFLOWS.md`<br>微案例课时：`materials-shading-c04-l20/l21`, `materials-shading-c02-l13`, `texturing-c02-l06/l07`, `texturing-c05-l20/l21`, `texturing-c03-l10~l13`;<br>主干课时：`texturing-c04-l19`, `texturing-c07-l28~l33` | CORE42 Materials & Shading 与 Texturing 语料本身采用“聚焦微型示例（Cube/Plane/Sphere/Suzanne/Hammer 排除干扰验证单项节点与物理数学原理） + 统一贯穿的硬表面复合道具（LowPoly Binoculars 双筒望远镜贯穿拆 UV $\to$ 视口手绘 $\to$ 程序化合成 $\to$ PBR 烘焙导出）”的双层组织结构。这为本项目 W1–W6 选项 C（Limited Main Case + Bounded Micro-Cases）提供了直接的教学组织实践先例（而非外部课程自身的周次映射）。 | 原厂归档中望远镜 3D 模型源文件缺失（标注为 `UNRESOLVED` 资产关联）；望远镜偏硬表面，经验难以直接平移至有机角色或大型建筑；程序化纹理在非规则复杂曲面上易产生尺度失真。 |
| **2. Normal / Bake Bounded Comparison**<br>(法线/置换有界对比与烘焙定位) | **`PARTIAL`** | • `CORE42_TEXTURING_FOUNDATIONS.md`<br>• `CORE42_TEXTURING_WORKFLOWS.md`<br>• `CORE42_OVERVIEW.md`<br>课时：`texturing-c02-l06` (Bump/Normal), `texturing-c02-l07` (Displacement), `texturing-c07-l33` (Bake), `texturing-c03-l11` | CORE42 支持 Bump、Normal Map 与 Displacement 三大凹凸机制的物理对比（清晰区分着色法线扰动与真实网格置换），并支持把低模上的手绘与程序化混合材质烘焙扁平化导出为 PBR 贴图集（`c07-l33`）；但其**不直接提供本项目“石膏高低模 bounded classroom micro-lab”的教学设计**（高低模硬表面烘痕在 `c03-l11` 中指向外部工具 Substance Painter）。 | Blender 内部烘焙流程聚焦于材质通道扁平化，未在软件内提供高低模对齐投影烘焙教学方案。 |
| **3. Procedural / Noise**<br>(程序化噪波与数学纹理) | **`SUPPORTS`** | • `CORE42_TEXTURING_WORKFLOWS.md`<br>课时：`texturing-c05-l20` (Noise 4D W, Voronoi, Wave, Brick, Checker, White Noise), `texturing-c05-l21` (AO + Z-axis 灰尘污渍), `texturing-c07-l32` (望远镜皮革与磨损程序化收尾) | 程序化纹理定位为“无无限放大失真、无缝平铺、打破 CG 完美感”的细节生成工具，作为手绘与图像贴图的**辅助修饰图层**，并提炼了通用的 `AO (缝隙)` + `Separate XYZ Z轴 (顶部落灰)` 双层脏迹网络。 | 缺乏具象商标/文字控制力；三维坐标映射在非规则网格上易出现接缝错位；多层 4D 噪波与体积计算开销大。 |
| **4. UV & Channel Reasoning**<br>(UV 展开与 PBR 通道连接推理) | **`SUPPORTS`** | • `CORE42_TEXTURING_FOUNDATIONS.md`<br>• `CORE42_TEXTURING_WORKFLOWS.md`<br>课时：`texturing-c03-l10~l13` (Hammer 缝合线原则、拉伸修复、Texel Density 统一、0.007 安全边距防渗色、Smart UV / Follow Active Quads), `texturing-c07-l28` (Binoculars UV), `texturing-c04-l16/l19` (Principled BSDF 通道组装) | 建立“基础工具单一道具 (Hammer) $\to$ 复合资产 (Binoculars)”阶梯展开路线。严密区分色彩空间：**sRGB** 用于视觉色彩通道（Base Color/SSS Color），**Non-Color** 用于数值/矢量数据通道（Normal, Metallic, Roughness, Displacement, Alpha, Transmission），Node Wrangler 快捷键批量接入。Base Color 混合 AO 贴图建议采用 Multiply 模式 (Factor 0.75)。 | Smart UV 产生的非规则碎片在手绘与纹理映射时有严重碎裂风险，实操依然高度依赖手动标记缝合线规范。 |
| **5. Representative-Material Transfer**<br>(代表性材质物理规律迁移) | **`PARTIAL`** | • `CORE42_MATERIALS_AND_SHADING.md`<br>• `CORE42_TEXTURING_FOUNDATIONS.md`<br>• `CORE42_TEXTURING_WORKFLOWS.md`<br>课时：`texturing-c04-l16/l18` (能量守恒、金属/电介质二分法、垂直入射 $F_0 \approx 0.04$、菲涅尔效应), `texturing-c05-e01/l20` (金属+噪波锈蚀氧化迁移), `materials-shading-c02-l08/c04-l20` (玻璃与瓷器), `texturing-c05-l21` (灰尘积垢通用双层掩码) | 课程通过通用 PBR 物理法则（能量守恒、金属/电介质二分、菲涅尔增强）支持参数泛化认知，使金属、塑料、玻璃、皮革与灰尘的逻辑可迁移；但语料中**并未包含明确跨资产的近迁移实操测试设计（general PBR principle supports generalization $\neq$ source-backed pedagogical near-transfer test）**。 | 迁移停留在硬表面物理规律认知，缺乏教学法层面的结构化跨载体近迁移评测设计。 |
| **6. LookDev**<br>(外观开发与渲染环境自检) | **`SUPPORTS`** | • `CORE42_MATERIALS_AND_SHADING.md`<br>• `CORE42_TEXTURING_FOUNDATIONS.md`<br>• `CORE42_CASE_INDEX.md`<br>课时：`texturing-c03-l09` / `texturing-c04-l17` (PolyHaven autoshop_01_2k.hdr 中性环境光照管理), `materials-shading-c04-l18` (Cycles 光线弹跳与 Fast GI), `materials-shading-c03-l17` (EEVEE 屏幕空间反射与反射探针 Light Probe), `materials-shading-c04-l20` (焦散/色散对比), Viewport Shading (Material Preview 内置 HDRI 质感快速开发 vs Rendered 真实光照) | 通过引入标准中性 HDRI（PolyHaven 工业车间）、Material Preview 视口快速迭代以及 Cycles/EEVEE 引擎双向比对，为学员提供外观质感开发与视口自检手段。 | 聚焦于单道具视口评估，未涉及多灯光摄影棚演播室布光或多环境换光自动化评测套件。 |

### 7.6 终审路线决策判定 (Final Synthesis Verdict)
- **是否存在足以改变推荐路线的冲突 (Route-Changing Contradiction)**: **`NO`**；
- **决策结论**:
  1. **宏观解耦边界界定**：W1–W6 教学基础演练 $\to$ W7–W9 全新独立综合期末大作业是 **Course Owner 锁定的宏观边界（Fixed Macro Boundary）**；CORE42 语料库对此**没有发现冲突（No Contradiction Found）**；
  2. **微观拓扑支持界定**：CORE42 的直接正向证据主要支持 W1–W6 范围内的 **Limited Main Case + Bounded Micro-Cases（选项 C 有界混合模型）**，并在节点通道推理、程序化噪波分层与视口 LookDev 自检上提供了坚实的实证支撑；
  3. **智能体推荐与负责人采纳**：智能体分析推荐选项 C，并已获 Course Owner 正式裁定采纳（**`TEACHER ACCEPTED — BOUNDED HYBRID W1–W6 TOPOLOGY BASELINE`**）；宏观边界与 W1–W6 拓扑已锁定，技术与资产门禁继续受控等待后续工单。

---

## 8. 工单结项停靠状态说明 (Stop Gate & Human Review Disposition)

根据人机决策权威边界规范与 Issue #19 停靠契约：

1. **当前状态**：**`TEACHER ACCEPTED — BOUNDED HYBRID W1–W6 TOPOLOGY BASELINE`**；
2. **权威决策已锁定范围**：
   - **宏观边界**：W1–W6 基础演练与能力构建 $\to$ W7–W9 全新独立综合期末大作业（Fixed Macro Boundary）；
   - **W1–W6 拓扑基线**：有限主案例 + 有界微案例混合模型（Bounded Hybrid）；
3. **技术与资产未决门禁（保持条件性）**：
   - 负责人采纳不等于资产工程与运行时实现已全部验证完成；
   - `[GATE-ASSET-01]`（手电筒 M6/M7 风化积灰承载性验证）、`[GATE-ASSET-02]`（花瓶零摩擦模板验证）、`[GATE-RT-01]`（Web 3D viewer runtime 门禁保持 OPEN）及具体 Normal Bake 实操形式（演示 vs 引导微实验 vs 拓展，不等于已锁定为纯观察）仍为未决门禁；
4. **严守非目标（Non-Goals）**：
   - 本工单**未启动 Issue #22**；
   - 本工单**未生成排课草案 v0.4**；
   - 本工单**未启动 Week 2 可执行教学包编写**；
   - 本工单**未修改或合并 PR #18**；
   - **不得合并 PR #26**（PR #26 就地停靠等待负责人合并）；
5. **后续工单交接**：本分支（`research/issue-19-case-topology-join`）在完成提交、推送并在稳定 HEAD 上重跑代码审查后就地停靠，后续由 Issue #22 承接期末大作业设计，排课草案综合工单承接 v0.4 综合排课。
