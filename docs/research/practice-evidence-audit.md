# 循证教学案例与实践审计报告 (Phase A: Practice Evidence Audit)

> **文档定位**：本报告响应 GitHub Issue #19 契约及最新 Browser Review（证据分级与标签规范化）要求。在 Phase A 阶段，严格基于“证据优先 (Evidence-First)”原则，对候选教学案例（Vintage Flashlight、Antique Ceramic Vase 01、Classical Bust、历史抽样参考资产）的物理特征与既往实践动作展开客观审计，梳理 4 种拓扑候选假说与关键课堂动作的证据基础。  
> **门禁状态**：`PHASE A EVIDENCE AUDIT COMPLETE / TOPOLOGY PENDING #20 REVIEWED JOIN`。  
> **核心边界**：本报告在 Phase A **不冻结任何拓扑结论**，不推荐任何单一主干或期末方案；最终 Case Topology 的对比与推荐，必须在 Issue #20（材质行为图谱）经 Browser Review 确认后，通过独立的 Join 步骤完成并提交 Course Owner 裁定。本轮严禁执行 Join。

---

## 1. 审计背景与核心问题 (Context & Problem Formulation)

在《Week 1–9 条件性排课草案 v0.3》的初期推演中，存在若干未经实证充分检验的直觉假设：
1. **单一资产跨周期的材质覆盖盲区**：原设计直觉假设“Vintage Flashlight”可作为横跨全课的核心资产，未严格审计其几何与材质构成对完整 PBR 行为空间的覆盖度；
2. **课堂上下文切换的实操风险**：W6 原计划在 160 分钟单次面授中同时容纳“独立近迁移实操”与“主资产深化”，存在双资产环境切换与时间超支的教学风险；
3. **Stage 4（W7–W9）角色重构**：Course Owner 明确指示，W7–W9 应开启全新的综合期末大作业（由 Issue #22 独立设计），彻底解耦“前六周教学练习资产”与“期末考核项目”；
4. **实践动作的证据基础缺失**：烘焙（Bake）、程序化噪波（Noise）、AI 输入决策与实时导出等重负荷动作，此前缺少系统的可行性与课时适配度审计。

---

## 2. 候选教学案例资产事实与五维证据审计 (Five-Dimension Case Audit)

基于仓库已验证的资产权威事实（`docs/research/teaching-asset-feasibility-matrix.md`），对候选教学资产按五大维度进行循证审计：

### 2.1 候选资产已有仓库事实基准 (Asset Provenance Baseline)
- **Poly Haven `Vintage Flashlight`**（CC0 1.0 Universal，作者：Omar M. El-Safy）：
  - `[PROVENANCE VERIFIED]`: 约 11K 三角面（~11K tris），UV 已展开；
  - `[PROVENANCE VERIFIED]`: 官方材质构成：红色绝缘漆外壳（Red dielectric paint）、裸金属（Bare metal）、黑色橡胶/塑料把手（Black rubber/plastic）、镀铬反光碗（Chrome reflector）与玻璃透镜（Glass lens）；金属基底成分标记为通用工业金属；
  - `[PENDING RUNTIME VALIDATION]`: UV 是否存在微局部重叠（Overlap）、拉伸畸变（Distortion），以及局部目标区域是否适合初学者无损独立编辑，尚待运行时切片实测验证。
- **Poly Haven `Antique Ceramic Vase 01`**（CC0 1.0 Universal，作者：James Ray Cock）：
  - `[PROVENANCE VERIFIED]`: 约 9K 三角面（~9K tris），包含展开 UV；
  - `[PROVENANCE VERIFIED]`: 官方材质构成：高反光玻璃质光滑釉面、开片微裂纹法线、青花釉下彩，以及底部粗陶露胎圈；
  - `[PENDING RUNTIME VALIDATION]`: 自带分层遮罩（Mask01/02/03）与着色器节点框架适配性尚待运行时核验。
- **古典石膏胸像套件 (`Classical Bust Bundle`)**：
  - `[PROVENANCE VERIFIED]`: 扫描高模解构微实验载体，纯哑光石膏材质。
- **历史教学素材库 (`Legacy Assets & SPP Decks`)**：
  - 仅对已抽样检查过的部分历史案例（如旧科幻武器零件、机械臂部件）作事实判定；其余未检查文件严格保持 `UNREVIEWED_OUT_OF_SCOPE`，不作全盘属性外推。

### 2.2 五维证据审计表

| 候选资产对象 | 材质行为原型覆盖 (Material Diversity) | 几何拓扑与 UV 状态 (Geometry & UV Status) | 实体认知负荷 (Cognitive Fit) | 课时预算适配性估算 (Contact-Hour Planning Estimate) | 初学者现场失效模式假说 (Beginner Failure Hypotheses) | 审计处置分类建议 (Audit Disposition) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **老式手电筒<br>(Vintage Flashlight)** | 覆盖抛光金属(反光碗)、粗糙金属(磨损露底)、复合漆面与缝隙积灰；**缺乏纯哑光漫反射与大面积光滑施釉表面**。 | 约 11K 面，流形几何；UV 存在，但局部重叠/拉伸与编辑适用性**待运行时验证**。 | 极佳。学生对工业手电筒物理构成（外壳、开关、反光碗）具有天然生活直觉。 | 规划估算适合拆解分步演练；但多部件一次性全选编辑易产生认知干扰。 | 误将多部件指定为同一材质槽；保存退出时外置纹理未打包导致重开丢失。 | **`ADAPT_CANDIDATE`**<br>(具备良好复合工业材质属性，适合教学基础与进阶练习) |
| **古董陶瓷花瓶<br>(Antique Ceramic Vase 01)** | 极强覆盖光滑施釉介电质（全器皿）与底部粗陶；**完全无导电金属特征**。 | 约 9K 面，单一连续回转体，UV 存在，自带遮罩与分层节点框架**待运行时核验**。 | 极低。单一器皿形态，无机械机关，学生能 100% 聚焦于釉面反射与泥胎特征。 | 规划估算约 30–40m 完成独立介电质闭环（待教学实测）。 | 误将光滑高光当做金属反光打开 Metallic；沉溺于手绘复杂花纹脱离材质本质。 | **`REUSE_CANDIDATE`**<br>(适合作为检验非金属理解的独立近迁移或对比候选) |
| **古典石膏胸像<br>(Classical Bust Bundle)** | 极强覆盖纯哑光介电质漫反射与切线法线微浮雕；**无金属与光滑高光**。 | 低模（~1.3K 面）与高模烘焙对齐；低模剪影呈明显多边形棱角。 | 极佳。美术生对素描石膏像具备深厚反照率认知，利于破除阴影烘焙误区。 | 规划估算微实验约 20–25m（若用于独立烘焙全流程则严重超载）。 | 误以为法线贴图能抚平低模掠射角剪影棱角，产生混淆（教学纠偏良机）。 | **`ADAPT_MICRO_ONLY`**<br>(仅适合作为法线原理与观察演示的轻量微实验教具) |
| **历史抽样工程<br>(Inspected Legacy SPP Decks)** | 局部覆盖复杂磨损与旧机械；抽样资产多为强风格化与高频噪波堆叠。 | 抽样资产面数偏高，部分存在重叠 UV，对未抽样文件保持状态隔离。 | 较高。缺乏清晰因果分层，初学者易退化为盲目套用智能材质预设。 | 在 Blender 环境下重新整理着色槽成本极高，单节课无法收敛。 | 软件卡顿死锁、着色网络混乱、图层过多迷失物理因果。 | **`REFERENCE_ONLY`<br>/ `UNREVIEWED_OUT_OF_SCOPE`**<br>(不作为课堂必做；未细审文件保持库内归档) |

---

## 3. 关键实践动作可行性与课时适配审计 (Practice Action Feasibility Audit)

针对既往推演中涉及的核心实践动作，逐项审计其证据来源、知识契合度、课时规划估算与课堂可行性，确立当前的实证状态：

| 实践动作项 (Practice Action) | 追踪证据来源 (Traceable Evidence Source) | 知识目标契合度 (Knowledge Fit) | 课时预算规划估算 (Planning Estimate) | 课堂落地可行性与风险假说 (Classroom Risk Hypotheses) | 当前实证状态 (Status) |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **法线贴图认知与烘焙<br>(Normal Map & Bake)** | • `docs/research/source-native-knowledge-index.md` (Dinur Ch 1, 13; glTF §3.9.3 & §5.19.5)<br>• 教师自研古典石膏高低模对资产 | 核心：区分宏观几何剪影与微表面着色法线扰动。 | • 全流程烘焙规划估算：60–90m<br>• 微实验对比规划估算：20–25m<br>*(均待实测)* | 全班全员烘焙存在较高的网格 Cage 穿插与驱动排错风险假说；微实验观察稳定性较高。 | **BOUNDED MICRO-LAB<br>(严控在微实验对比范围)** |
| **程序化噪波扰动<br>(Procedural Noise)** | • `docs/research/source-native-knowledge-index.md` (Shah 2022 Ch 8; Dinur 2026 Ch 13)<br>• Blender 5.2 Manual (*Noise Texture Node*) | 核心：理解数学分形参数对微表面粗糙度与遮罩边缘的控制机制。 | 规划估算约 15–20m<br>*(待教学干跑验证)* | Blender 节点视口即时可调，但需防范初学者无节制嵌套导致节点网络不可控。 | **EVIDENCE-SUPPORTED CANDIDATE PRACTICE<br>(单节点参数化控制)** |
| **外部 / AI 贴图审查<br>(External/AI Input Review)** | • `docs/research/ai-impact-on-material-workflows.md`<br>• `docs/research/teaching-source-provenance.md`<br>• Dinur 2026 Ch 19 (AI Control Boundaries) | 关键：建立物理通道语义辨识力，学会“接受/拒绝/替换”决策。 | 规划估算约 20–30m<br>*(以结构化清单驱动)* | 采用预置样本进行人眼质检把关，不依赖机房网络安装复杂 AI 生成环境。 | **VIABLE HYPOTHESIS<br>(作为受控决策练习)** |
| **独立近迁移练习<br>(Near-Transfer Exercise)** | • `docs/research/curriculum-audit-pedagogy-evidence-2026-09-19.md` (近迁移评价机制)<br>• Dinur 2026 Ch 4 (非金属与自然表面) | 核心：脱离主资产教程步骤引导，独立在陌生模型上应用 PBR 原理。 | 规划估算约 30–40m<br>*(限制为参数辨识与分层判断)* | 若与主资产放在同一节课自由穿插，存在严重认知切换与时间挤占风险假说。 | **HYPOTHESIS REQUIRES ISOLATION<br>(必须具备硬性流程隔离)** |
| **Realtime 外部导出核验<br>(glTF / WebGL Export)** | • Issue #21 (glTF §3.9.2, Blender 5.2 glTF Manual)<br>• 待执行的轻量查看器运行时探针 | 核心：掌握通道打包约定与色彩空间，辨析离线与实时渲染差异。 | 规划估算约 30–45m<br>*(含导出与核验排错)* | 依赖受控查看器环境与机房运行权限；若发生 CORS 拦截需具备清晰恢复路径。 | **FEASIBLE PENDING RUNTIME PROBE<br>(待受控运行时实测)** |
| **跨工具迁移候选<br>(Same-Asset Painter Transfer)** | • 历史教学大纲与 Substance 教学资产<br>• 待独立执行的 Teacher/IDE Dry-run | 探索：验证相同模型在不同工具间的概念迁移。 | 规划估算时间开销显著（双软件启动、烘焙与图层操作）。 | 涉及机房双软件授权稳定性与学生界面认知负荷翻倍风险。 | **UNVERIFIED HYPOTHESIS<br>(待独立 dry-run 验证)** |

---

## 4. 案例排课拓扑选项集全景比对 (Topology Options for Join Evaluation)

为支撑后续与 Issue #20 的汇合决策，梳理 4 种具备完整理论逻辑的拓扑结构供评估。本阶段**不做定案选择，仅中立呈现候选特征与权衡风险假说**：

### 4.1 四大拓扑候选特征对比表

| 拓扑结构选项 | 核心组织逻辑 | 材质覆盖潜力假说 | 认知负荷与启动摩擦权衡 | 教学评价机制与特征 | 待 Join 阶段裁决的核心疑问 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **选项 1：单一主资产连续模型<br>(Single-Main-Asset)** | 全程 9 周使用同一款工业模型深化打磨。 | 局限于该资产固有材质，存在 M1/M2 盲区风险。 | 启动成本低；但中后期可能产生审美疲劳与套路化依赖。 | 全班进度高度统一，但难以检验脱离该资产后的独立判断力。 | 如何在单模型内补齐基础漫反射与纯介电质认知？ |
| **选项 2：阶段性递进模型<br>(Staged / Segmented)** | 按教学阶段（如每 2–3 周）更换不同物理类型的案例。 | 原型覆盖均衡，各案例专精特定行为。 | 每次更换资产均需重新熟悉几何拓扑与 UV，存在时间损耗风险。 | 各阶段均有独立阶段作品产出，评价维度清晰。 | 在 24 实际学时内，频繁更换资产是否会导致学生作品深度不足？ |
| **选项 3：有限主案例 + 有界微案例<br>(Bounded Hybrid)** | 以一个复合工业资产为主，穿插轻量微实验与短迁移。 | 兼顾工业分层与纯介电质互补。 | 主线熟练度高，微案例认知冲击适度；但 W6 面临课堂上下文切换风险。 | 具备独立近迁移检验样本。 | W6 单课时内能否安全实现“前段迁移 + 后段主干”的流程隔离？ |
| **选项 4：教学与期末项目解耦模型<br>(Decoupled Stage 4)** | **W1–W6 完成教学基础演练；W7–W9 独立展开全新综合期末项目**。 | 前期覆盖核心原型，后期由期末项目综合检验。 | 前期专注基础，后期自主发挥；期末面临全新资产的审题与启动成本。 | 能客观检验学生跨资产知识迁移与独立综合创作能力。 | 期末项目的资产形式、难度范围与评分接口如何界定（由 #22 解决）？ |

---

## 5. Phase A 审计小结与 Join Gate 状态说明

1. **资产事实与处置边界**：
   - `Vintage Flashlight` 具备良好的工业复合分层属性，但存在天然材质盲区，不可作为全课唯一材质依托；
   - `Antique Ceramic Vase 01` 与 `Classical Bust` 在纯介电质与微表面法线认知上具备良好互补潜力；
   - 历史未审 SPP 资产保持 `REFERENCE_ONLY` 或 `UNREVIEWED_OUT_OF_SCOPE`，严禁盲目引入课堂实操。
2. **拓扑决策保留**：
   - 拓扑模型选择尚未冻结。选项 4（W1–W6 教学演练与 W7–W9 期末大作业解耦）符合 Course Owner 关于 Stage 4 边界的最新决策，将作为 Join 时的重点考量基础。
3. **停靠门禁（Stop Gate）**：
   - **本工单在 Phase A 结束并就地停靠**。在 Issue #20 经 Browser Review 确认后，再行开展两者的正式 Join 分析，向 Course Owner 提交拓扑推荐案。本轮不执行 Join。
