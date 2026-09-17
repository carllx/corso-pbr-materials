# 《三维数字材质制作》教学层架构 (Teaching Layer Architecture)

> **研究阶段**：Stage 2 Gate 3A — Teaching Layer Architecture (Bounded Hardening)  
> **审查基线锚点**：`c309218624f574a10a3798c8f49d29bd605d8b9f` (Gate 2.5 最终审阅收口锚点)  
> **治理规范**：依据 GitHub Issue #5 (Gate 3 契约) 与 Issue #3 (Stage 2 总体策略)。  
> **核心使命**：为本科《三维数字材质制作》课程确立一套紧凑、可观察、可评估的学生学习成效（Learning Outcomes）体系。将 Candidate Set v2 (`V02-C01`–`V02-C47`) 从“研究审查全集（Research Inventory）”转化为“学生核心学习层（Student-Facing Layer）”与“教师/底层参考层（Teacher / Infrastructure Layer）”的双层教学架构。

---

## 目录
1. [定位与门禁边界声明 (Purpose & Gate Boundary)](#1-定位与门禁边界声明-purpose--gate-boundary)
2. [学生画像与课时规划情境假定 (Student Profile & Planning Scenario Assumptions)](#2-学生画像与课时规划情境假定-student-profile--planning-scenario-assumptions)
3. [拟定的可观察核心学习成效 (Proposed Observable Learning Outcomes)](#3-拟定的可观察核心学习成效-proposed-observable-learning-outcomes)
   - [LO1: 材质物理观察、艺术意图与情绪板多维解构](#lo1-材质物理观察艺术意图与情绪板多维解构)
   - [LO2: 光学因果推理与微表面物理可信性认知](#lo2-光学因果推理与微表面物理可信性认知)
   - [LO3: 多通道分层创作与空间局部受控修订](#lo3-多通道分层创作与空间局部受控修订)
   - [LO4: 参数化/程序化系统思维与变体控制](#lo4-参数化程序化系统思维与变体控制)
   - [LO5: 多源材质获取、AI 转换质量评估与混合精修](#lo5-多源材质获取ai-转换质量评估与混合精修)
   - [LO6: 目标交付约束对齐、着色一致性调校与 LookDev 验证](#lo6-目标交付约束对齐着色一致性调校与-lookdev-验证)
4. [跨成效去重与平衡性检查 (Cross-outcome Redundancy & Balance Check)](#4-跨成效去重与平衡性检查-cross-outcome-redundancy--balance-check)
5. [研究全集映射总表 (Research Inventory Mapping: LO $\to$ Candidates)](#5-研究全集映射总表-research-inventory-mapping-lo--candidates)
6. [显式非学生直面 / 教师底层参考清单 (Explicitly Non-Student-Facing / Teacher-Reference)](#6-显式非学生直面--教师底层参考清单-explicitly-non-student-facing--teacher-reference)
7. [后置 Gate 3B 待决技术候选 (Later Gate 3B Decision Candidates)](#7-后置-gate-3b-待决技术候选-later-gate-3b-decision-candidates)
8. [Gate 3A 总结与推进建议 (Gate 3A Recommendation)](#8-gate-3a-总结与推进建议-gate-3a-recommendation)

---

## 1. 定位与门禁边界声明 (Purpose & Gate Boundary)

### 1.1 核心问题与决策顺序
Gate 3 彻底打破“按 47 个 Candidate 逐个排课”的惯性，严格遵循以下决策顺序：
$$\text{Observable Student Performance} \longrightarrow \text{Required Depth} \longrightarrow \text{Minimum Content Combination} \longrightarrow \text{Candidate Mapping}$$

本报告（Gate 3A）专注回答：
> **对一个本科《三维数字材质制作》课程，学生最终应该能够表现出哪些少量、可观察、可评估的综合能力？**

### 1.2 绝对纪律与非目标边界 (Non-goals)
- **47 项是 Research Inventory，不是 47 个教学课时单元**：不存在“每一项 Candidate 必须在学生端分配课时”的约束，允许大量 Candidate 仅作为支撑依据、概念背书、教师参考或底层基础设施；
- **禁止排定 Week 1–8 具体周课表**：课程周程、具体课时切分属于 Stage 4 任务，本阶段严禁越界；
- **禁止编写完整作业题或打分量表 (Rubrics)**：本 Gate 仅定义可观察表现与达成最低证据，不设计期末大作业细节；
- **禁止重新打开 Gate 2.5 来源研究或修改 47 项分类结构**：Candidate Set v2 保持严格冻结；
- **不进行 47 项 Teaching Action 回填**：`KEEP / COMPRESS / REFRAME / REPLACE / ADD` 属于 Gate 3D 事项，本 Gate 只做粗粒度映射。

### 1.3 Gate 3A PASS 后的 Gate 3B 实践实现解耦澄清 (Post-PASS Clarification)
本架构文档在保持 `Gate 3A PASS` 及六大核心学习成效（LO1–LO6）框架不变的前提下，根据 Gate 3B 纠偏指令明确以下“能力目标与具体软件实现形式解耦”的澄清原则（避免先入为主将某种软件特定工作流捆绑为唯一达标标准）：
- **LO3 (分层与受控修订)**：图层栈（Layer Stack）、锚点（Anchor Points）或特定的多通道表现仅属于特定工具（如 Painter）的具体实现形态，不自动构成学生能力达标的唯一强制表现证据；核心成效在于建立“底漆/表层因果分层、空间局部受控修订且非目标区域保全”的直观心智模型；
- **LO4 (程序化与变体)**：固定数量的暴露参数（Exposed Parameters）、产品化封装的高级自定义节点组并非强制达标门槛；核心成效在于理解 DAG 节点拓扑驱动逻辑与基本的参数化变体控制；
- **LO5 (获取与 AI 评估)**：对低质或不合规外部/AI 资产的“有据拒绝、替换或局部采纳”同样属于合格的评估鉴别能力，并非所有坏输入都必须在软件中被完整“修复”。
*注：最终 LO3–LO5 的具体文字表述调整将严格依据 Gate 3B 运行环境实测探针证据在后续阶段完成，避免在测试前闭门预设。*

---

## 2. 学生画像与课时规划情境假定 (Student Profile & Planning Scenario Assumptions)

在校方具体排课计划最终确认前，必须将已知事实、规划情境假设与未决事项严格隔离，禁止将假定当成已核实事实。

### 2.1 已知事实 (Known Facts)
1. **课程周期**：设计基准周期为 **8 周**；
2. **前置支撑管线定位**：`course-design-ledger.md` 明确规定建模、高低模、拓扑与 UV 为**支撑性知识**，教学深度以支撑材质制作为度，不作为从零手撕复杂模型展开的建模课主体；
3. **创作范式覆盖要求**：必须涵盖纹理贴图分层绘制（Texture-based）、程序化参数化生成（Procedural/Parametric）与 AI/采集转换（AI/Acquisition）；
4. **出口定位**：实时游戏（Game Realtime）与动画/视觉开发（Animation / LookDev）统一在材质能力底座下，作为两个出口约束与验证场景，而非开设两门独立全流程课程。

### 2.2 规划情境假设 (Planning Scenario — Subject to Later Capacity Confirmation)
1. **学生前置能力假定**：
   - 假定学生具备基础的数字媒体/三维软件操作体验（如熟悉基础三维视口导航、简单多边形编辑与基本赋予材质球概念）；
   - **PBR 物理着色体系假定为第一次系统化接触**，对其微表面原理、通道解耦及数据规范缺乏先验系统训练；
   - 假定学生具备基础的美术造型/色彩感知，但缺乏将“真实世界表面不完美性”解构为“多通道物理数据”的结构化观察经验。
2. **课时负荷规划情境 (Workload Planning Scenario)**：
   - 设定参考规划情境：单周面授课时为 **4 课时**（合 3 实际小时），单周课外练习与自主作业为 **4–6 小时**；
   - 8 周总参考学习负荷约为 **56–72 实际人时 (Gross Student Hours)**；
   - *重要提示*：此情境仅作为当前评估能力容量与教学深度的规划基准，尚未经校方教务正式确认。它提醒教学设计必须聚焦于“因果推理、审美判断与可控修订”的核心直觉，防止盲目堆砌工具功能与复杂底层管线。

### 2.3 核心未决容量输入 (Unresolved Capacity Assumptions)
以下核心容量参数目前尚未最终锁定，属于后续排课与内容筛选必须核实的事项：
- `[CAPACITY ASSUMPTION — UNRESOLVED 01]`: **真实教学面授课时与课外作业预期学时**（直接决定实操深度的物理容量边界）；
- `[CAPACITY ASSUMPTION — UNRESOLVED 02]`: **学生入学时的三维建模、UV 与贴图实际技能基线**（决定前置支撑知识需占用多少铺垫时间）；
- `[CAPACITY ASSUMPTION — UNRESOLVED 03]`: 标准化机房 GPU 硬件算力档次（影响实时视口 LookDev 渲染与烘焙计算的上限）；
- `[CAPACITY ASSUMPTION — UNRESOLVED 04]`: 学生专业流向（偏向游戏引擎交互 vs 偏向影视动画 LookDev）的实际比例偏置。

---

## 3. 拟定的可观察核心学习成效 (Proposed Observable Learning Outcomes)

经审查，确立 **6 个高内聚、可评估的核心学习成效 (LO1–LO6)**：

```
                          ┌──────────────────────────────────────────────────────────┐
                          │    8 周本科《三维数字材质制作》核心学习成效 (LO1–LO6)    │
                          └────────────────────────────┬─────────────────────────────┘
                                                       │
         ┌──────────────────────────────┬──────────────┴───────────────┬──────────────────────────────┐
         ▼                              ▼                              ▼                              ▼
  【审美与物理感知】             【资产受控创作】              【系统抽象与演化】             【范式与交付验证】
  LO1: 观察与艺术意图解构       LO3: 多通道分层受控修订        LO4: 参数化系统与变体控制      LO5: 多源获取与 AI 评估精修
  LO2: 光学因果与物理可信性                                                                   LO6: 目标交付约束与 LookDev
```

---

### LO1: 材质物理观察、艺术意图与情绪板多维解构
*Physical Material Observation, Artistic Intent & Reference Decomposition*

- **Observable Student Performance (学生实际能做什么)**：
  面对实物参考照片或艺术概念设计，学生能用专业语言撰写材质艺术意图说明（明确材质年龄、经历的工艺加工、环境暴露史及视觉主次重点），并能将非结构化的参考图像，解构为结构化的四维特征清单：固有色基准、微表面光泽分布、宏观/微观法线凹凸特征、以及表层风化/污损因果演变。
- **Attainment Depth (达成深度)**：
  - `INDEPENDENT PRACTICE`：独立完成资产材质参考解构情绪板（Moodboard）与物理特征分析报告；
  - `RECOGNIZE & EXPLAIN`：解释视觉层级（Visual Hierarchy）如何通过粗糙度对比与细节频率对比建立，防止画面“碎、脏、乱”。
- **Prerequisite / Practice Burden (前置与练习负担)**：
  - `Low`。无需复杂三维软件技巧，重点在于感知训练、素描明度理解与视觉分析规范。
- **Human vs AI Responsibility Split (人机责任分工)**：
  - **学生亲自负责**：视觉观察、建立艺术意图假说、判断视觉中心、定义资产故事背景；
  - **AI / 辅助工具辅助**：色彩提取建议、相似材质参考检索、关键词描述补全；
  - *职责边界*：艺术意图与主次平衡由创作者审美把控，不可交由算法随机全权决定。
- **Irreplaceable Teaching Gain (不可替代教学收益)**：
  如果删除此项，学生容易沦为“无目的的滤镜与参数盲调者”，制作出技术指标看似合格但视觉平庸、缺乏逻辑与故事感的塑料化资产。
- **Minimum Evidence of Attainment (最低达成证据)**：
  学生能拿出一份包含主客观拆解的资产参考分析表，清楚解释该材质各主要特征区域（如特定边角磨损、底层变色）的视觉合理性，而非单纯由滤镜全图随机铺设。
- **Minimal Hands-on Hypothesis (动手实验假说)**：
  给定一个工业旧物（如生锈的铁皮油壶），学生标注其 Macro（结构分件）、Medium（磕碰凹陷）、Micro（拉丝微孔）三级频域细节分布图。
- **Supporting Candidate IDs (支撑候选能力)**：
  `V02-C01`, `V02-C09`
- **Teacher / Infrastructure-only Elements (教师/底层参考)**：
  高阶感知心理学实验、复杂的辐射度量化测色仪操作。
- **Unresolved Assumptions**：无。

---

### LO2: 光学因果推理与微表面物理可信性认知
*Appearance Causality & Microfacet Physical Plausibility*

- **Observable Student Performance (学生实际能做什么)**：
  在动态光照与多视角观察下，学生能独立识别并纠正材质的代表性物理矛盾。具体表现为：能诊断出“反照率明显脱离常见材质参考区间”、“金属度非预期杂色噪点”、“环境遮挡（AO）错误烘死在固有色中”、“法线贴图坐标系翻转导致凹凸颠倒”、“色彩空间误设（数据贴图被误标为 sRGB 引起粗糙度泛白）”，并能合理解释其背后的光学与着色因果。
- **Attainment Depth (达成深度)**：
  - `INDEPENDENT PRACTICE`：通道独立审查（Channel Isolation）、反照率合理区间排查、数据贴图色彩空间矫正；
  - `RECOGNIZE & EXPLAIN`：微表面微观几何分布（GGX NDF）、菲涅尔效应（Fresnel F0）、能量守恒的定性直方图关系；
  - `INFRASTRUCTURE / TEACHER REFERENCE`：微表面 BRDF 双向反射分布函数的积分推导与辐射度底层代码实现。
- **Prerequisite / Practice Burden (前置与练习负担)**：
  - `Medium`。需要克服传统数字绘图“所见即所得随意涂抹”的习惯，建立物理数据通道的直觉。
- **Human vs AI Responsibility Split (人机责任分工)**：
  - **学生亲自负责**：在视口中调整光照环境，切入各个单通道模式下进行因果归因与逻辑矛盾排查；
  - **AI / 自动化辅助**：通道直方图警报提示、通道自动打包脚本；
  - *职责边界*：学生应理解常见反照率范围（如 PBR Guide 建议的 30–240 sRGB 经验区间）作为诊断触发参考，理解出射光能量不超过入射光的能量守恒因果，而不是盲目依赖一键修复按钮。
- **Irreplaceable Teaching Gain (不可替代教学收益)**：
  这是现代物理着色与传统经验贴图的本质区别。若删除此项，学生难以理解为何资产在特定固定灯光下尚可、一旦切换至动态环境光照即发生视觉失真。
- **Minimum Evidence of Attainment (最低达成证据)**：
  教师给出一组包含常见物理冲突（如：Base Color 残留明显投影、纯质金属表面出现非预期的中间噪点灰度、Normal 绿通道坐标系反转）的材质资产，学生能指出主要问题、合理解释成因并进行参数纠正。
- **Minimal Hands-on Hypothesis (动手实验假说)**：
  在固定粗糙度条件下，调整入射光角度与表面属性，亲手观察比较高光扩散与菲涅尔边缘反射在不同材质类型上的直观差异。
- **Supporting Candidate IDs (支撑候选能力)**：
  `V02-C02`, `V02-C03`, `V02-C04`, `V02-C05`, `V02-C06`, `V02-C08`, `V02-C10`, `V02-C42`
- **Teacher / Infrastructure-only Elements (教师/底层参考)**：
  `V02-C02` 中的复杂微表面积分数学推导；`V02-C10` 底层 OCIO 配置文件的 XML 规范。
- **Conditional Teaching Rules & Nuances (规则适用条件说明)**：
  - *反照率范围说明*：30–240 sRGB 是实践经验诊断基准（Diagnostic Guideline），超出区间通常应触发合规性复核，但不可误读为能量守恒定律直接推出的数学绝对边界；
  - *金属度灰阶说明*：对于纯且均质的导体或绝缘体，金属度通常接近 0 或 1；但在氧化腐蚀过渡、半透明涂层边界、微观混合脏污或抗锯齿像素过滤等合法异质情况下，中间过渡灰阶在物理与工程上成立，不应一概判定为错误。
- **Unresolved Assumptions**：无。

---

### LO3: 多通道分层创作与空间局部受控修订
*Multi-channel Layered Authoring & Controlled Local Revision*

- **Observable Student Performance (学生实际能做什么)**：
  在资产级三维纹理绘制环境中，学生能参考制造工艺与时间风化规律，构建“基底材质 $\to$ 表面涂层 $\to$ 机械接触磨损 $\to$ 环境风化与积尘”的非破坏性多通道图层架构；能运用遮罩、几何投影与空间特征工具；当面临艺术指导（Art Direction）的具体修改意见（例如局部调整特定区域的掉漆范围并调整底层色相，同时保持金属高光与微观凹凸稳定）时，能执行明确边界的局部修改，同时保持无关通道与区域稳定。当任务要求后续可维护性与版本迭代时，能恢复或保留足够的编辑结构。
- **Attainment Depth (达成深度)**：
  - `INDEPENDENT PRACTICE`：非破坏性多通道图层架构搭建、基于模型几何贴图（Curvature/AO/Position 等）的自适应遮罩调配、局部手绘修饰与受控版本迭代；
  - `SUPPORTED / TEMPLATE PRACTICE`：智能材质模板（Smart Materials）的参数定制与资产间复用；
  - `RECOGNIZE & EXPLAIN`：在需要受控修订的任务情境下，从扁平无图层贴图中逆向提取特征遮罩并重构可编辑图层栈的方法。
- **Prerequisite / Practice Burden (前置与练习负担)**：
  - `High`。这是课程中实操比重较高的核心技能，要求学生熟悉三维绘制环境的图层堆栈与多通道交互。
- **Human vs AI Responsibility Split (人机责任分工)**：
  - **学生亲自负责**：规划图层架构、设定局部修改边界、精细控制遮罩权重、进行审美把控；
  - **AI / 算法工具辅助**：基于模型曲率生成初始破损遮罩底稿、智能填充底材纹理、生成程序噪波斑痕；
  - *职责边界*：扁平位图在不需要后续多版本修改的下游特定场景中是合法的交付形式；但当面对严苛的艺术指导与局部迭代需求时，学生应掌握分层重构与局部受控修订（Edit Locality）的能力。
- **Irreplaceable Teaching Gain (不可替代教学收益)**：
  生产管线对技术人员的关键诉求之一是“可修改性与版本迭代能力”。如果缺乏此项，学生面对修改意见往往只能破坏性重画或推倒重来。
- **Minimum Evidence of Attainment (最低达成证据)**：
  给定一个已完成材质的模型，要求学生在保持原有污垢和划痕逻辑自洽的前提下，对指定区域的涂层状态与细节特征进行受控局部修改，修改后图层组织清晰，未破坏其他通道的既有结构。
- **Minimal Hands-on Hypothesis (动手实验假说)**：
  在特定模型上使用遮罩、绘制效果与锚点链接，实现下层磨损图案动态关联上层涂层边界演变的操作链条。
- **Supporting Candidate IDs (支撑候选能力)**：
  `V02-C11`, `V02-C12`, `V02-C13`, `V02-C14`, `V02-C15`, `V02-C16`, `V02-C18`*, `V02-C19`*, `V02-C20`*, `V02-C21`*, `V02-C43`
- **Teacher / Infrastructure-only Elements (教师/底层参考)**：
  底层绘制工具自定义 Shader（QML/GLSL）编写；复杂自动化脚本批处理导出管线开发。
- **Unresolved Assumptions**：
  学生进入课程时对图层混合模式与通道遮罩的接受速度，需通过规范工程模板进行辅助引导。

---

### LO4: 参数化/程序化系统思维与变体控制
*Parametric System Thinking & Meaningful Procedural Variation*

- **Observable Student Performance (学生实际能做什么)**：
  学生能建立基于“输入 $\to$ 运算 $\to$ 输出”的有向无环图（DAG）数据流思维。能运用程序化噪波与数学映射节点（如范围重映射、数值混合），构建具有合理尺度的无缝表面材质系统；能将内部网络封装为包含语义参数（如磨损比例、平铺密度、粗糙度偏移）的模块化结构（Node Group / Subgraph），并通过调节暴露参数或随机种子，生成风格自洽且细节不重复的材质变体。
- **Attainment Depth (达成深度)**：
  - `SUPPORTED / TEMPLATE PRACTICE`：在有限节点范围内搭建小型程序化材质子图；
  - `INDEPENDENT PRACTICE`：在主材质中调节并暴露有意义的参数接口，消除平铺重复感（Tiling Breakup）；
  - `RECOGNIZE & EXPLAIN`：程序化动态算力开销与静态贴图烘焙之间的工程权衡（运行时生成 vs 显存与贴图读取）；
  - `INFRASTRUCTURE / TEACHER REFERENCE`：庞大复杂的工业级商业程序化宏图表系统；底层 HLSL/GLSL 节点数学算法实现。
- **Prerequisite / Practice Burden (前置与练习负担)**：
  - `Medium-High`。节点拓扑逻辑对非理工背景学生存在一定抽象门槛，教学宜通过结构化模板引导。
- **Human vs AI Responsibility Split (人机责任分工)**：
  - **学生亲自负责**：理解节点间的数据类型对应（标量 vs 向量 vs 色彩）、设计合理的参数接口边界、把控变体美感；
  - **AI / 节点工具辅助**：通过文字描述生成简单节点连接原型、推荐噪波类型组合；
  - *职责边界*：学生应能读懂节点数据流向，在材质出现数值截断或映射拉伸时，能定位到对应节点进行排查。
- **Irreplaceable Teaching Gain (不可替代教学收益)**：
  程序化思维是数字资产批量化、工业化与参数化复用的核心底座。删除此项，学生认知将受限于固定贴图，难以理解现代母材质架构与大规模环境资产系统。
- **Minimum Evidence of Attainment (最低达成证据)**：
  学生提交一个小型材质节点图（或 Node Group），包含清晰的 3–5 个外部暴露参数；调节参数数值或更换随机种子时，材质外观能产生合理的参数化变化，着色器无报错或数值溢出崩溃。
- **Minimal Hands-on Hypothesis (动手实验假说)**：
  使用晶体/分形噪波节点配合距离运算与范围重映射，构建一个起伏可控的地表高度图图元。
- **Supporting Candidate IDs (支撑候选能力)**：
  `V02-C22`, `V02-C23`, `V02-C24`, `V02-C25`, `V02-C26`, `V02-C27`, `V02-C28`, `V02-C30`, `V02-C29`*[Teacher/Infra]
- **Teacher / Infrastructure-only Elements (教师/底层参考)**：
  `V02-C29` 中的跨平台运行时插件发布管线；MaterialX 节点跨平台代码生成（ShaderGen）底层；复杂的像素处理器汇编。
- **Unresolved Assumptions**：
  具体实操宿主（Blender Shader Nodes vs Substance 3D Designer）留待 Gate 3B 根据总学时裁定。

---

### LO5: 多源材质获取、AI 转换质量评估与混合精修
*Acquisition Paradigm Selection, AI/Capture Evaluation & Hybrid Refinement*

- **Observable Student Performance (学生实际能做什么)**：
  面对具体的生产任务与资产类型，学生能建立清晰的范式选择意识，权衡何时从资产库检索、何时现场拍摄采集、何时调用生成式 AI、何时必须程序化或手绘创建；在使用图像或生成式工具获得贴图后，学生能针对不同 PBR 通道分别进行独立验证（不预设各通道可靠度一致），识别方向性强光阴影、过曝反照率或通道撕裂缺陷，并运用算法去光照结合视口修复工具，将其整理为可用的标准材质贴图。
- **Attainment Depth (达成深度)**：
  - `INDEPENDENT PRACTICE`：多范式选用权衡分析、受控环境光实物参考采集方法执行；
  - `SUPPORTED / TEMPLATE PRACTICE`：单图/多图材质转换工具调用、去光照（Delighting）缺陷排查与手动曲线/画笔精修；
  - `RECOGNIZE & EXPLAIN`：AI 生成模型在商业许可、可控性及空间结构依附上的适用范围；针对具体工具输出进行通道级质量验证。
- **Prerequisite / Practice Burden (前置与练习负担)**：
  - `Medium`。重点在于建立客观理性的质检评估能力，避免对 AI 工具产生一键完成的盲目预期。
- **Human vs AI Responsibility Split (人机责任分工)**：
  - **学生亲自负责**：制定参考采集方案、筛选优质输入、诊断生成贴图的通道级缺陷、进行艺术意图微调与物理合理性验收；
  - **AI / 自动化工具执行**：通道数据前向推测估计、色彩平铺重构、无缝拼接算法求解；
  - *职责边界*：外部生成或拍摄转换的贴图应经过通道级合规与光照解耦复核，防止将明显带有环境直射光阴影的素材直接投入管线。
- **Irreplaceable Teaching Gain (不可替代教学收益)**：
  使学生具备在现代工作流中理性评估与整合 AI 工具及多源数据的能力。删除此项，学生面对新技术易走向盲目抗拒或过度依赖两个极端。
- **Minimum Evidence of Attainment (最低达成证据)**：
  提供一张带有明显单向日光阴影的实拍或生成图像，学生能利用工具链分离大部分光照影响，生成基础 PBR 贴图，在视口中验证光照反向照射时不再出现原图光照伪影。
- **Minimal Hands-on Hypothesis (动手实验假说)**：
  使用手机拍摄一张生活中的粗糙材质，导入工具执行材质转换，对比观察开启与关闭去光照滤镜时 Base Color 贴图的明暗均匀度。
- **Supporting Candidate IDs (支撑候选能力)**：
  `V02-C31`, `V02-C32`, `V02-C33`, `V02-C34`, `V02-C41`, `V02-C47`
- **Teacher / Infrastructure-only Elements (教师/底层参考)**：
  多角度偏振光度立体采集设备硬件搭建；扩散模型底层隐空间数学原理。
- **Conditional Diagnostic Hypotheses (条件性诊断假说)**：
  - *通道可靠度假说*：在单图估计实践中，法线与粗糙度的空间几何线索相对直观，而金属度与深层凹凸在特定复杂光照下容易出现误判；此现象应作为**条件性诊断假说 (Conditional Diagnostic Hypothesis)**，指导学生对各通道逐一查验，而非固定不变的绝对真理。
- **Unresolved Assumptions**：无。

---

### LO6: 目标交付约束对齐、着色一致性调校与 LookDev 验证
*Target Delivery Constraints, LookDev Verification & Adaptation*

- **Observable Student Performance (学生实际能做什么)**：
  学生能将材质置于不同光照（如多角度或差异化环境光）与视角条件下重新验证其表现；当面对下游特定目标环境（如实时游戏引擎或离线渲染环境）的适配要求时，能识别主要技术约束与失配原因，完成一次受约束的目标格式适配；并能解释不同目标视口之间外观无法完全一致的残余差异成因。
- **Attainment Depth (达成深度)**：
  - `INDEPENDENT PRACTICE`：在改变光照与视角条件下重新验证材质着色反应；根据目标规范完成受约束的贴图通道打包与色彩空间设置；
  - `SUPPORTED / TEMPLATE PRACTICE`：在给定目标模板（如实时母材质实例或指定渲染上下文）下执行参数微调；
  - `RECOGNIZE & EXPLAIN`：核心管线认知：$\text{Valid Representation} \neq \text{Visual Equivalence} \neq \text{Production Deliverable}$；解释微表面散射模型、色调映射（Tone Mapping）与硬件性能约束对跨平台外观的影响；
  - `INFRASTRUCTURE / TEACHER REFERENCE`：底层着色器编译分支优化；GPU 硬件显存带宽底层瓶颈分析；深度 MaterialX/UsdShade 编程式绑定。
- **Prerequisite / Practice Burden (前置与练习负担)**：
  - `Medium`。重点在于建立生产交付与技术约束意识，理解资产跨平台流转的工程现实。
- **Human vs AI Responsibility Split (人机责任分工)**：
  - **学生亲自负责**：多视角/多光照下肉眼复核材质质感、调校参数以达到目标环境下的可接受视觉一致性；
  - **AI / 自动化工具代劳**：批量通道通道重组与命名、规范化文件格式导出；
  - *职责边界*：严禁仅在单一静态光照下确认材质；明确跨平台流转的目标是“达到可接受的视觉一致性并理解差异成因”，而非追求绝对毫无偏差的跨引擎像素级等同。
- **Minimum Evidence of Attainment (最低达成证据)**：
  学生能将一套材质资产适配并导入一个指定的下游目标环境中，使其在目标光照下展现出符合预期的视觉质感；并能书面或口头解释：“由于该目标引擎的微表面模型/色调映射与原创作视口存在差异，哪些细节表现已调整，哪些残余差异属于技术约束所致”。
- **Minimal Hands-on Hypothesis (动手实验假说)**：
  将资产放置于强对比日光与低对比漫射光两种环境光下旋转检视，验证粗糙度高光扩散与暗部阴影响应是否稳定自然。
- **Supporting Candidate IDs (支撑候选能力)**：
  `V02-C17`, `V02-C35`, `V02-C36`, `V02-C37`, `V02-C38`, `V02-C39`, `V02-C40`, `V02-C44`*, `V02-C46`*
- **Illustrative Implementation Candidates (供 Gate 3B 选用的示例技术，非当前强制约束)**：
  ORM 通道打包、BC7/BC5 压缩格式、视口着色复杂度视图、白炉无自发光测试、UsdShade 渲染上下文（Render Context）等，均作为后续教学设计的可选载体，不作为 Gate 3A 全量必修指标。
- **Teacher / Infrastructure-only Elements (教师/底层参考)**：
  MaterialX XML 手写与底层 NodeDef 编写；UsdShade C++ API 底层调用；实时引擎底层着色器源码级定制。
- **Unresolved Assumptions**：无。

---

## 4. 跨成效去重与平衡性检查 (Cross-outcome Redundancy & Balance Check)

确立上述 6 个成效后，对其结构独立性与职责划分进行核验：

| 审查维度 | 审查结论与设计防线 |
| :--- | :--- |
| **LO1 (观察) vs LO2 (光学因果) 是否重叠？** | **边界清晰，无需合并**。LO1 侧重于**宏观审美与艺术意图**（年代、故事、视觉层级、现实细节解构），属于“观察与分析”；LO2 侧重于**微观光学与物理因果**（反照率合理范围、金属度判定、能量守恒直觉、通道数据排错），属于“物理法则与诊断”。两者共同构筑材质感知基石。 |
| **LO3 (分层绘制) vs LO4 (程序化系统) 是否重叠？** | **范式独立，互补协作**。LO3 针对**特定资产空间维度的多通道分层修饰**（图层堆栈、几何遮罩与局部受控修订）；LO4 针对**连续无缝、基于数学逻辑与参数接口的母材质系统**（节点拓扑与参数化变体控制）。两者涵盖了现代材质制作的主干范式。 |
| **LO5 (获取与 AI) vs LO3 (分层绘制) 是否重叠？** | **素材前处理与资产装配的分工**。LO5 解决**输入源的多范式权衡、AI/转换前向估计与光照解耦初加工**；LO3 解决素材获得后**如何在资产表面构建可维护图层栈以进行受控局部迭代**。 |
| **艺术判断 (Artistic Judgment) 是否显式化？** | **充分显式，融入各层**。LO1 将“艺术意图与视觉层级”作为核心标准；LO3 将“依据艺术指导完成受控局部修订”作为实践准则；LO5 将“多范式权衡选择”作为人的决策判断。艺术判断作为贯穿全流程的评价维度。 |
| **管线工程超载防线是否稳固？** | **界限分明，安全隔离**。将 MaterialX XML 手写、UsdShade API 编程式绑定、ShaderGen 代码生成、Agent 闭环架构、GPU 汇编调优等工程深度全部剥离至“教师底层参考层”（详见第 6 节），确保学生直面直观、可视、可操作的创作与理解层。 |

---

## 5. 研究全集映射总表 (Research Inventory Mapping: LO $\to$ Candidates)

为维持研究全集的完整可追溯性，将 Candidate Set v2 (`V02-C01`–`V02-C47`) 全量 47 项映射至各 Learning Outcome 中。

> **映射原则声明**：
> - 47 项是已归档的证据全集，不是 47 个孤立教学任务；
> - 一个 Outcome 可由多个 Candidate 共同支撑；一个 Candidate 可在多个 Outcome 中交叉出现；
> - 标有 `[Teacher/Infra]` 的候选能力表明该能力的核心技术实现仅供教师演示或作为底层支持，不构成学生直面实操必修。

| Learning Outcome (成效单元) | 支撑的 Candidate Set v2 编号 | 涵盖的关键技术与实证要素 |
| :--- | :--- | :--- |
| **LO1: 材质观察与艺术意图解构** | `V02-C01`, `V02-C09` | 现实物理特征观察、人眼感知与成像动态范围、宏观/中观/微观多级频域细节尺度解构。 |
| **LO2: 光学因果与物理可信性** | `V02-C02`, `V02-C03`, `V02-C04`, `V02-C05`, `V02-C06`, `V02-C08`, `V02-C10`, `V02-C42` | 能量守恒概念、反照率参考区间、GGX 微表面粗糙度、金属度分布特征、切线空间法线坐标系、AO 漫反射解耦、线性与非色彩色彩管理、跨通道物理自洽性诊断。 |
| **LO3: 多通道分层受控修订** | `V02-C11`, `V02-C12`, `V02-C13`, `V02-C14`, `V02-C15`, `V02-C16`, `V02-C18`*, `V02-C19`*, `V02-C20`*, `V02-C21`*, `V02-C43` | 资产工程与通道架构、非破坏性图层与多通道同步混合、空间局部遮罩与投影绘制、自适应材质模板封装、底材-涂层-磨损物理工艺演化、环境接触风化模拟、扁平贴图分层重构与受控修订。<br>*(注：带 * 号的几何与烘焙支撑项 C18–C21 作为支撑 LO3 正常运转的前置必要技能，按支持深度纳入)* |
| **LO4: 参数化系统与变体控制** | `V02-C22`, `V02-C23`, `V02-C24`, `V02-C25`, `V02-C26`, `V02-C27`, `V02-C28`, `V02-C30`, `V02-C29`*[Teacher/Infra] | 结构化节点图与 DAG 拓扑、空间坐标系转换、分形噪波与 Voronoi 胞元合成、节点数学运算与范围重映射、物理尺度对齐、对象随机种子与平铺打散、参数接口设计与子图封装、程序化贴图烘焙。<br>*(C29 运行时插件集成主要作为架构演示)* |
| **LO5: 多源获取与 AI 评估精修** | `V02-C31`, `V02-C32`, `V02-C33`, `V02-C34`, `V02-C41`, `V02-C47` | 受控光照采集规程、单图多通道估计与通道独立验证、去光照缺陷诊断与手工精修、无缝平铺处理、空间几何条件生成心智、多范式权衡决策（生成 vs 检索 vs 参数化 vs 实拍）。 |
| **LO6: 目标交付约束与 LookDev** | `V02-C17`, `V02-C35`, `V02-C36`, `V02-C37`, `V02-C38`, `V02-C39`, `V02-C40`, `V02-C44`*, `V02-C46`* | 贴图导出模板配置、视口着色检验、引擎母材质与参数化实例概念、运行时通道打包、高保真着色（次表面/清漆/薄膜）物理特性、跨渲染环境着色差异调校、环境光旋转压力测试。<br>*(C44 与 C46 核心标准语义纳入学生理解，底层编程接口列入教师参考)* |
| **隔离层 (前沿/底层参考)** | `V02-C45`*[Teacher/Infra] | 机器可读材质图拓扑、XML 序列化与 Agent 自动化操作边界（作为教师前沿视野拓展，不设为学生实操必修）。 |

---

## 6. 显式非学生直面 / 教师底层参考清单 (Explicitly Non-Student-Facing / Teacher-Reference)

为了防止技术冒进与教学超载，特在此明确划定**非学生直面（Non-Student-Facing）**与**教师底层参考（Teacher Reference / Infrastructure-only）**的边界：

### 6.1 OpenPBR 与 MaterialX 的清晰角色切分 (V02-C44 深度实现)
- **概念职责切分（依据 Gate 2.5 审计定稿）**：
  - **OpenPBR**：定义**通用的表面材质物理语义**（Surface Shading Model、参数名称、数值范围与多层介质混合规则）；
  - **MaterialX**：提供**结构化的节点图与数据内容表示模式**（中立强类型图拓扑、XML 数据序列化规范、验证与跨平台着色器代码生成机制）。
- **学生直面层（教学定位）**：
  - 学生理解现代开放材质标准的价值（材质语义规范化与跨软件流转理念）；
  - *注：是否在特定 DCC 中直接打开或操作基于 MaterialX/OpenPBR 的节点，属于 Gate 3B 教学价值裁定事项，作为可选教学演示/练习候选，当前不锁定为强制必修要求。*
- **教师底层参考层（隔离，学生不直面）**：
  - 手写或直接修改 MaterialX XML 数据代码；
  - 编写自定义 `NodeDef`（节点定义）与数据模式；
  - MaterialX ShaderGen C++ 库集成与跨平台着色器代码生成管线开发。

### 6.2 OpenUSD / UsdShade 场景绑定与底层 API (V02-C46 深度实现)
- **概念职责切分**：
  - **UsdShade**：负责在三维场景层级中提供**材质与几何图元的绑定关系**（Material Binding）以及多渲染器上下文（Render Context）调度。
- **学生直面层（教学定位）**：
  - 理解 USD 在影视动画管线中的资产引用角色；理解材质作为独立资产与网格绑定的逻辑；理解不同渲染上下文带来的着色响应差异。
- **教师底层参考层（隔离，学生不直面）**：
  - 使用 Python / C++ 调用 `UsdShadeMaterialBindingAPI` 进行底层编程式绑定；
  - 编写复杂的 USD 几何子集继承逻辑与变体集合（VariantSets）管线脚本；
  - 多层 USD 合成弧（Composition Arcs）的底层拓扑解析。

### 6.3 智能体编排与自主图表自动化操作 (V02-C45 深度实现)
- **学生直面层（教学定位）**：
  - 理解结构化参数与节点图相比扁平图像更具备机器可读性与自动化修改优势的持久心智模型。
- **教师底层参考层（隔离，学生不直面）**：
  - 开发基于 LLM / VLM 的材质节点图自动生成 Agent 编排；
  - 编写无头（Headless）三维渲染与参数微调脚本服务器；
  - 工业级 API 调度与自动化构建流水线搭建。

### 6.4 游戏引擎底层着色器开发与硬件调优 (V02-C36 / V02-C37 深度实现)
- **学生直面层（教学定位）**：
  - 理解贴图尺寸与通道打包对运行时性能的意义，能在引擎视口中进行基础的可视化性能观察。
- **教师底层参考层（隔离，学生不直面）**：
  - 实时引擎底层 USF/HLSL 着色器代码模板编写；
  - 静态开关（Static Switch）引发的大规模着色器变体编译机器集群调度；
  - GPU 硬件级 Wavefront 占用率与底层显存架构瓶颈分析。

---

## 7. 后置 Gate 3B 待决技术候选 (Later Gate 3B Decision Candidates)

以下技术路径与具体软件选型在 Gate 3A 仅作为支撑假说的备选案例，**不构成当前 Gate 3A 的锁定决策**，留待 Gate 3B（最小内容选择）再做裁决：

### 候选议题 1：程序化材质的核心教学宿主选择 (Procedural Authoring Host)
- **选项备选**：
  - *选项 A*：以 **Blender Shader Nodes** 为主要实操环境（轻量、即时可视、通用节点拓扑），配合少量 Designer 架构概念演示；
  - *选项 B*：以 **Substance 3D Designer** 为主要实操环境（专业度高，但上手曲线陡峭）。
- **当前归类**：`Later Gate 3B Decision Candidate`（不阻塞 Gate 3A 学习成效的确立）。

### 候选议题 2：双出口评价权重的课程重心配置 (Dual-target Assessment Weighting)
- **选项备选**：
  - *选项 A*：以 **实时交互引擎约束** 为基础交付基准，影视离线 LookDev 作为高精度渲染特例；
  - *选项 B*：以 **离线高保真渲染** 为基础交付基准，实时引擎作为轻量优化特例。
- **当前归类**：`Later Gate 3B Decision Candidate`（不阻塞 Gate 3A 学习成效的确立）。

### 候选议题 3：具体技术工具与格式的最小组合 (Minimal Technical Toolset)
- 包括具体的常用节点清单（如 Noise/Voronoi/Map Range）、具体的运行时通道打包规范（如 ORM）、具体的 GPU 压缩格式（如 BC7/BC5/BC1）等，均作为 Gate 3B 最小组合筛选时的候选要素，不在 Gate 3A 提前固化为全量学生承诺。

---

## 8. Gate 3A 总结与推进建议 (Gate 3A Recommendation)

### 8.1 架构合理性自评
1. **成效规模聚焦**：将原本分散的 47 项研究清单收敛为 **6 个高内聚的学习成效**，清晰定义可观察的学生行为表现；
2. **人机权责分明**：明确观察、意图、因果逻辑与审美验收由人类主导，算法与工具承担初稿生成与辅助计算，确立能力的持久性；
3. **管线工程防线**：将底层 XML、API 编程与底层优化隔离至教师参考层，确保教学专注在质感创作的核心体验；
4. **去除绝对化表述**：纠正了将经验指南误写为物理硬定律、将可编辑性绝对化、将单图估计置信度作为既定事实的表述，保持学术与工程严谨性。

### 8.2 下一步行动路线 (Next Steps)
- **本轮交付**：固化本文档 `docs/research/teaching-layer-architecture.md`，提交 Commit 并推送到 GitHub，在 Issue #5 提交评审回复；
- **等待审查验收**：等待 Browser 针对本硬化版本进行 Gate 3A 验收；
- **后续 Gate（当前保持封冻）**：
  - **Gate 3B — Minimal Content Selection**：裁定实现 6 大成效所需的最小 Candidate 组合与软件宿主；
  - **Gate 3C — Representative Task Feasibility**：设计代表性任务检验成效闭环；
  - **Gate 3D — Teaching Action Backfill**：最终回填 47 项 Candidate 的教学处理状态。

---
*本文档生成并归档于 `docs/research/teaching-layer-architecture.md`，作为 Gate 3A 规范交付基线。*
