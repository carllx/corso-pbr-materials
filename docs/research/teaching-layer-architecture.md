# 《三维数字材质制作》教学层架构 (Teaching Layer Architecture)

> **研究阶段**：Stage 2 Gate 3A — Teaching Layer Architecture  
> **审查基线锚点**：`c309218624f574a10a3798c8f49d29bd605d8b9f` (Gate 2.5 最终审阅收口锚点)  
> **治理规范**：依据 GitHub Issue #5 (Gate 3 契约) 与 Issue #3 (Stage 2 总体策略)。  
> **核心使命**：为 8 周本科《三维数字材质制作》课程确立一套紧凑、可观察、可评估的学生学习成效（Learning Outcomes）体系。将 Candidate Set v2 (`V02-C01`–`V02-C47`) 从“研究审查全集（Research Inventory）”转化为“学生核心学习层（Student-Facing Layer）”与“教师/底层参考层（Teacher / Infrastructure Layer）”的双层教学架构。

---

## 目录
1. [定位与门禁边界声明 (Purpose & Gate Boundary)](#1-定位与门禁边界声明-purpose--gate-boundary)
2. [学生画像与课时负荷假设 (Student Profile & Capacity Assumptions)](#2-学生画像与课时负荷假设-student-profile--capacity-assumptions)
3. [拟定的可观察核心学习成效 (Proposed Observable Learning Outcomes)](#3-拟定的可观察核心学习成效-proposed-observable-learning-outcomes)
   - [LO1: 材质物理观察、艺术意图与情绪板多维解构](#lo1-材质物理观察艺术意图与情绪板多维解构)
   - [LO2: 光学因果推理与微表面物理可信性认知](#lo2-光学因果推理与微表面物理可信性认知)
   - [LO3: 多通道分层创作与空间局部受控修订](#lo3-多通道分层创作与空间局部受控修订)
   - [LO4: 参数化/程序化系统思维与变体控制](#lo4-参数化程序化系统思维与变体控制)
   - [LO5: 多源材质获取、AI 转换质量评估与混合精修](#lo5-多源材质获取ai-转换质量评估与混合精修)
   - [LO6: 目标交付约束对齐、着色一致性调校与 LookDev 验证](#lo6-目标交付约束对齐着色一致性调校与-lookdev-验证)
4. [跨成效去重与冗余度检查 (Cross-outcome Redundancy & Balance Check)](#4-跨成效去重与冗余度检查-cross-outcome-redundancy--balance-check)
5. [研究全集映射总表 (Research Inventory Mapping: LO $\to$ Candidates)](#5-研究全集映射总表-research-inventory-mapping-lo--candidates)
6. [显式非学生直面 / 教师底层参考清单 (Explicitly Non-Student-Facing / Teacher-Reference)](#6-显式非学生直面--教师底层参考清单-explicitly-non-student-facing--teacher-reference)
7. [Gate 3A 未决决策与用户决策清单 (Gate 3A Unresolved Decisions)](#7-gate-3a-未决决策与用户决策清单-gate-3a-unresolved-decisions)
8. [Gate 3A 总结与推进建议 (Gate 3A Recommendation)](#8-gate-3a-总结与推进建议-gate-3a-recommendation)

---

## 1. 定位与门禁边界声明 (Purpose & Gate Boundary)

### 1.1 核心问题与决策顺序
Gate 3 彻底打破“按 47 个 Candidate 逐个排课”的惯性，严格遵循以下决策顺序：
$$\text{Observable Student Performance} \longrightarrow \text{Required Depth} \longrightarrow \text{Minimum Content Combination} \longrightarrow \text{Candidate Mapping}$$

本报告（Gate 3A）唯一且专注地回答：
> **对一个 8 周本科《三维数字材质制作》课程，学生最终应该能够表现出哪些少量、可观察、可评估的综合能力？**

### 1.2 绝对纪律与非目标边界 (Non-goals)
- **47 项是 Research Inventory，不是 47 个教学课时单元**：不存在“每一项 Candidate 必须在学生端分配课时”的约束，允许大量 Candidate 仅作为支撑依据、概念背书、教师参考或底层基础设施；
- **禁止排定 Week 1–8 具体周课表**：课程周程、具体课时切分属于 Stage 4 任务，本阶段严禁越界；
- **禁止编写完整作业题或打分量表 (Rubrics)**：本 Gate 仅定义可观察表现与达成最低证据，不设计期末大作业细节；
- **禁止重新打开 Gate 2.5 来源研究或修改 47 项分类结构**：Candidate Set v2 保持严格冻结；
- **不进行 47 项 Teaching Action 回填**：`KEEP / COMPRESS / REFRAME / REPLACE / ADD` 属于 Gate 3D 事项，本 Gate 只做粗粒度映射。

---

## 2. 学生画像与课时负荷假设 (Student Profile & Capacity Assumptions)

在缺乏校方绝对排课大纲前，必须将已知事实、合理推导假设与未决事项严格隔离，禁止捏造精确课时。

### 2.1 已知事实 (Known Facts)
1. **课程周期**：标准本科教学周期为 **8 周**（短期高强度专业实训课模态）；
2. **前置支撑管线定位**：`course-design-ledger.md` 明确规定建模、高低模、拓扑与 UV 为**支撑性知识**，严禁喧宾夺主成为课程主体；
3. **创作范式覆盖要求**：必须涵盖纹理贴图分层绘制（Texture-based）、程序化参数化生成（Procedural/Parametric）与 AI/采集转换（AI/Acquisition）；
4. **出口定位**：实时游戏（Game Realtime）与动画/视觉开发（Animation / LookDev）统一在材质能力底座下，作为两个出口约束，而非开设两门独立全流程课程。

### 2.2 工作假设 (Working Assumptions)
1. **学生前置能力假设**：
   - 学生具备基础的数字媒体/三维软件操作经验（如熟悉基础三维视口导航、简单多边形编辑与基本材质球赋予概念）；
   - **PBR 物理着色体系是第一次系统化接触**，对其微表面原理、通道解耦及数学逻辑缺乏系统认知；
   - 学生具备基础的美术素描/色彩感知能力，但缺乏将“真实世界表面不完美性”转化为“多通道物理数据”的结构化观察经验。
2. **课时负荷工作模型 (Weekly Workload Assumption)**：
   - 设单周面授课时为 **4 课时**（合 3 实际小时），单周课外练习与自主作业为 **4–6 小时**；
   - 8 周总有效学习负荷约为 **56–72 实际人时 (Gross Student Hours)**；
   - 这一负荷决定了：学生绝无可能同时精通 Substance 3D 官方全家桶、大型程序化 Designer 深度节点、Unreal 材质底层 C++ 与 MaterialX XML 手写；教学必须高度聚焦于“因果推理、审美判断与可控修订”的核心直觉。

### 2.3 未决事项标记 (Unresolved / User Decision Needed)
- `[CAPACITY ASSUMPTION — UNRESOLVED 01]`: 课程是否配备具有专用 GPU 算力的标准化机房（影响实时视口 LookDev 与离线烘焙的复杂度上限）；
- `[CAPACITY ASSUMPTION — UNRESOLVED 02]`: 学生专业流向（偏向游戏引擎交互 vs 偏向影视特效渲染）的实际比例是否偏置（影响出口验收权重）。

---

## 3. 拟定的可观察核心学习成效 (Proposed Observable Learning Outcomes)

经审查，独立审查提出的 6 项假设方向合理，但需强化“艺术审美判断”与“人机分工中不可替代的心智直觉”。最终确立 **6 个高内聚、可评估的学习成效 (LO1–LO6)**：

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
  面对实物参考照片或艺术概念设计，学生能用专业语言撰写材质艺术意图说明（明确材质年龄、经历的工艺加工、环境暴露史及视觉主次重点），并能将非结构化的参考图像，准确解构为结构化的四维特征清单：固有色基准、微表面光泽分布、宏观/微观法线凹凸特征、以及表层风化/污损因果演变。
- **Attainment Depth (达成深度)**：
  - `INDEPENDENT PRACTICE`：独立完成资产材质参考解构情绪板（Moodboard）与物理特征分析报告；
  - `RECOGNIZE & EXPLAIN`：解释视觉层级（Visual Hierarchy）如何通过粗糙度对比与细节频率对比建立，防止画面“碎、脏、乱”。
- **Prerequisite / Practice Burden (前置与练习负担)**：
  - `Low`。无需复杂三维软件技巧，重点在于感知训练、素描明度理解与视觉分析规范。
- **Human vs AI Responsibility Split (人机责任分工)**：
  - **学生必须亲自**：用眼睛观察、建立艺术意图假设、判断视觉中心、定义资产故事背景；
  - **AI / 辅助工具可代劳**：色彩提取、相似材质参考图检索、关键词描述补全；
  - *核心红线*：艺术意图与主次平衡严禁交由 AI 随机决定。
- **Irreplaceable Teaching Gain (不可替代教学收益)**：
  如果删除此项，学生将沦为“无目的的滤镜与参数乱调者”，做出技术指标看似合格但视觉平庸、缺乏灵魂与故事感的塑料化资产。
- **Minimum Evidence of Attainment (最低达成证据)**：
  学生能拿出一份包含主客观拆解的资产参考分析表，清楚指出：“为什么这个磨损必须出现在这里，而不是由生成器随机铺满整个物体”。
- **Minimal Hands-on Hypothesis (动手实验假说)**：
  给定一个工业旧物（如生锈的铁皮油壶），学生手绘标注其 Macro（结构分件）、Medium（磕碰凹陷）、Micro（拉丝微孔）三级频域细节分布图。
- **Supporting Candidate IDs (支撑候选能力)**：
  `V02-C01`, `V02-C09`
- **Teacher / Infrastructure-only Elements (教师/底层参考)**：
  高阶感知心理学实验、复杂的辐射度量化测色仪操作。
- **Unresolved Assumptions**：无。

---

### LO2: 光学因果推理与微表面物理可信性认知
*Appearance Causality & Microfacet Physical Plausibility*

- **Observable Student Performance (学生实际能做什么)**：
  在动态光照与多视角观察下，学生能独立识别并纠正材质的物理矛盾。具体表现为：能迅速诊断出“固有色死黑或过曝”、“金属度伪灰阶过渡”、“环境遮挡（AO）烘死在固有色中”、“法线贴图坐标系翻转导致凹凸颠倒”、“色彩空间误设（Data 贴图被当成 sRGB 引起粗糙度泛白）”，并能清晰解释其背后的光学与数学因果。
- **Attainment Depth (达成深度)**：
  - `INDEPENDENT PRACTICE`：通道独立审查（Channel Isolation）、反照率安全范围排查、数据贴图色彩空间矫正；
  - `RECOGNIZE & EXPLAIN`：微表面微观几何分布（GGX NDF）、菲涅尔效应（Fresnel F0）、能量守恒的定性直方图关系；
  - `INFRASTRUCTURE / TEACHER REFERENCE`：微表面 BRDF 双向反射分布函数的积分推导与辐射度代码实现。
- **Prerequisite / Practice Burden (前置与练习负担)**：
  - `Medium`。需要克服对传统数字绘图“所见即所得随意涂抹”的直觉依赖，建立物理严密的数据通道直觉。
- **Human vs AI Responsibility Split (人机责任分工)**：
  - **学生必须亲自**：在视口中旋转灯光，切到各个单通道模式下进行因果归因与逻辑矛盾排查；
  - **AI / 自动化可代劳**：自动直方图安全范围警报脚本、自动通道打包工具；
  - *核心红线*：学生必须理解“为什么反射率不能超过 240 sRGB”背后的能量守恒因果，不能盲目依赖一键修复按钮。
- **Irreplaceable Teaching Gain (不可替代教学收益)**：
  这是现代数字材质与传统手绘贴图的本质分水岭。删除此项，学生将永远无法理解为什么自己的材质在当前视口看着还行、一进游戏引擎或换个 HDRI 场景就彻底穿帮崩溃。
- **Minimum Evidence of Attainment (最低达成证据)**：
  教师给出一组故意包含 3 处物理错误（如：Base Color 含强阴影、Metallic 通道呈现大面积渐变灰、Normal 绿通道反转）的材质资产，学生能在 5 分钟内准确圈出错误、说明原因并完成参数修正。
- **Minimal Hands-on Hypothesis (动手实验假说)**：
  在保持粗糙度为固定值的前提下，仅调整高光色和灯光角度，亲手验证非金属（F0 4%）与金属（F0 对应固有色）的高光反射差异。
- **Supporting Candidate IDs (支撑候选能力)**：
  `V02-C02`, `V02-C03`, `V02-C04`, `V02-C05`, `V02-C06`, `V02-C08`, `V02-C10`, `V02-C42`
- **Teacher / Infrastructure-only Elements (教师/底层参考)**：
  `V02-C02` 中的复杂微表面积分求解；`V02-C10` 底层 OCIO 配置文件的 XML 结构定义。
- **Unresolved Assumptions**：无。

---

### LO3: 多通道分层创作与空间局部受控修订
*Multi-channel Layered Authoring & Controlled Local Revision*

- **Observable Student Performance (学生实际能做什么)**：
  在资产级三维纹理绘制环境中，学生能遵循工业制造与时间演化的真实物理因果，自底向上构建“基底材质 $\to$ 表面涂层 $\to$ 机械接触磨损 $\to$ 环境风化与浮尘”的非破坏性图层堆栈；能熟练运用遮罩、几何投影与空间特征生成器；当面临艺术指导（Art Direction）的具体修改意见（例如：“把把手边缘的掉漆收窄 30%，但保留金属底材的高光和底层的轻微铁锈”）时，能在 **5–10 分钟内精准执行局部修订**，而绝不破坏其他通道或引发全图重绘。
- **Attainment Depth (达成深度)**：
  - `INDEPENDENT PRACTICE`：非破坏性多通道图层架构搭建、基于模型几何贴图（Curvature/AO/Position）的自适应遮罩调配、局部手绘修饰与受控版本迭代；
  - `SUPPORTED / TEMPLATE PRACTICE`：智能材质模板（Smart Materials）的参数定制与资产间复用；
  - `RECOGNIZE & EXPLAIN`：从无图层信息的扁平贴图中逆向提取遮罩并重构成可编辑图层栈的方法论。
- **Prerequisite / Practice Burden (前置与练习负担)**：
  - `High`。这是 8 周课程中耗时最长、实操比重最高的核心能力，要求学生熟练驾驭 3D 视口绘制环境的图层逻辑与通道交互。
- **Human vs AI Responsibility Split (人机责任分工)**：
  - **学生必须亲自**：规划图层架构、设定局部修改边界、精细控制遮罩权重、进行审美把控；
  - **AI / 算法生成器可代劳**：根据曲率自动生成初始破损遮罩底稿、智能填充底材纹理、程序化生成噪波斑痕；
  - *核心红线*：生成模型输出的“扁平死图”绝对不能直接作为最终交付物，学生必须具备将其图层化或在三维空间中进行精准局部修补的能力（Edit Locality）。
- **Irreplaceable Teaching Gain (不可替代教学收益)**：
  工业生产管线对技术人员最核心的要求是“可修改性与版本迭代能力”。如果缺乏此项，学生只能做出一锤子买卖的 Demo，一旦面对总监或甲方的修改需求就只能推倒重来。
- **Minimum Evidence of Attainment (最低达成证据)**：
  给定一个已完成材质的模型，要求学生在保留原有污垢和划痕空间关系的前提下，仅将表面车漆由“崭新红色光面”改为“剥落的哑光黄色”，并在转折处增加指定位置的手绘文字喷漆，修改过程中图层逻辑严密清晰。
- **Minimal Hands-on Hypothesis (动手实验假说)**：
  在特定模型上使用 Black Mask + Paint Effect + Anchor Point，实现下层铁锈图案动态跟随上层剥落遮罩边缘移动的交互链条。
- **Supporting Candidate IDs (支撑候选能力)**：
  `V02-C11`, `V02-C12`, `V02-C13`, `V02-C14`, `V02-C15`, `V02-C16`, `V02-C18`*, `V02-C19`*, `V02-C20`*, `V02-C21`*, `V02-C43`
- **Teacher / Infrastructure-only Elements (教师/底层参考)**：
  底层 Painter 自定义 Shader（QML/GLSL）编写；复杂自动化脚本批处理导出插件开发。
- **Unresolved Assumptions**：
  学生是否能在前 2 周内快速消化 Substance 3D Painter 的 UI 逻辑与烘焙贴图配合（需要高效率的模板工程支持）。

---

### LO4: 参数化/程序化系统思维与变体控制
*Parametric System Thinking & Meaningful Procedural Variation*

- **Observable Student Performance (学生实际能做什么)**：
  学生能脱离纯手工涂抹思维，建立基于“输入 $\to$ 运算 $\to$ 输出”的有向无环图（DAG）数据流思维。能运用常用程序化噪波（Perlin/Simplex 连续分形、Voronoi 晶体胞元）与数学映射节点（Map Range, Mix, Math），构建具有真实物理尺度的无缝表面材质系统；能将内部复杂网络封装为包含语义参数（如“锈蚀密度”、“平铺比例”、“表面粗糙度偏移”）的模块化母版（Master Graph / Node Group），并通过调节随机种子（Seed）或暴露参数，快速生成一系列风格自洽但细节不重复的材质变体。
- **Attainment Depth (达成深度)**：
  - `SUPPORTED / TEMPLATE PRACTICE`：在精选的有限节点集（Noise, Voronoi, Math, ColorRamp, Normal Map, Mix）内搭建小型程序化材质子图；
  - `INDEPENDENT PRACTICE`：在主材质中调节并暴露有意义的参数接口，消除平铺重复感（Tiling Breakup）；
  - `RECOGNIZE & EXPLAIN`：程序化动态算力开销与静态贴图烘焙之间的工程权衡（CPU/GPU 运行时生成 vs 显存带宽占用）；
  - `INFRASTRUCTURE / TEACHER REFERENCE`：庞大复杂的跨上百个节点的完整商业级 Substance 3D Designer 宏图表搭建；底层 HLSL/GLSL 节点数学算法实现。
- **Prerequisite / Practice Burden (前置与练习负担)**：
  - `Medium-High`。节点逻辑对非理工科背景艺术生具有一定的认知门槛。必须严格限制节点数量，通过模板化引导。
- **Human vs AI Responsibility Split (人机责任分工)**：
  - **学生必须亲自**：理解节点间的数据类型匹配（标量 vs 向量 vs 色彩）、推导数值重映射逻辑、设计暴露给外界的参数接口边界；
  - **AI / 节点助手可代劳**：通过文字生成简单节点链原型（如 Blender Shader Python 脚本生成初始连接）、根据描述推荐噪波类型；
  - *核心红线*：学生必须看懂节点数据拓扑流向，当材质在边界处出现拉伸或数值溢出时，能定位到具体数学节点进行纠偏。
- **Irreplaceable Teaching Gain (不可替代教学收益)**：
  程序化思维是数字艺术资产工业化、自动化与智能体化的核心底座。删除此项，学生将停留在低维的位图作坊阶段，无法理解母材质架构、环境大面积材质铺设与游戏/影视大型资产管线。
- **Minimum Evidence of Attainment (最低达成证据)**：
  学生提交一个小型材质节点图（或 Node Group），包含清晰的 3–5 个外部暴露参数（滑块）；教师随机调整滑块数值或更改 Object Random ID，材质外观能产生符合物理常理的自然演化，且着色器绝不出现破面、纯黑截断或报错。
- **Minimal Hands-on Hypothesis (动手实验假说)**：
  使用一个 Voronoi 节点配合 Distance 运算与 Map Range，亲手构建出一个裂纹深度可控的岩石地表高度图。
- **Supporting Candidate IDs (支撑候选能力)**：
  `V02-C22`, `V02-C23`, `V02-C24`, `V02-C25`, `V02-C26`, `V02-C27`, `V02-C28`, `V02-C30`, `V02-C29`*[Teacher/Infra]
- **Teacher / Infrastructure-only Elements (教师/底层参考)**：
  `V02-C29` 中的工业级 SBSAR 编译集成管线；MaterialX NodeDef 跨平台代码生成（ShaderGen）底层实现；复杂的 Pixel Processor 汇编代码。
- **Unresolved Assumptions**：
  `[CAPACITY ASSUMPTION — UNRESOLVED 03]`: 本科 8 周内究竟以 Blender Shader Nodes 为轻量入口，还是以 Substance 3D Designer 为专项环境（建议：两者保持节点逻辑相通，以轻量清晰为原则，避免陷入 Designer 软件功能迷宫）。

---

### LO5: 多源材质获取、AI 转换质量评估与混合精修
*Acquisition Paradigm Selection, AI/Capture Evaluation & Hybrid Refinement*

- **Observable Student Performance (学生实际能做什么)**：
  面对具体的生产任务与资产类型，学生能建立清晰的范式决策意识，合理权衡“何时从开源/商用库检索（Retrieval）”、“何时实地拍照转换（Capture）”、“何时调用生成式 AI（Generation）”、“何时必须程序化或手绘创建”；在使用手机/单反拍摄照片或使用生成式 AI 获得输入后，学生能准确诊断其致命缺陷（如强烈的方向性假阴影、过曝高光、法线模糊、伪金属噪点），并运用去光照算法滤镜结合三维投射克隆画笔，将其转化为一套符合 PBR 规范的无缝标准材质贴图。
- **Attainment Depth (达成深度)**：
  - `INDEPENDENT PRACTICE`：多范式选用权衡决策判断、基于平阴天/受控漫射光的实物参考采集规程执行；
  - `SUPPORTED / TEMPLATE PRACTICE`：单图/多图 AI 材质生成工具调用（如 Sampler Image to Material / 生成式功能）、去光照（Delighting）缺陷排查与手动反向曲线/画笔补偿修补；
  - `RECOGNIZE & EXPLAIN`：AI 生成模型在商业版权、可控性及拓扑依附上的边界；通道级置信度层级（法线/粗糙度相对可靠，金属度与深度凹凸极易误判）。
- **Prerequisite / Practice Burden (前置与练习负担)**：
  - `Medium`。重点在于建立严密的“质检工程师”眼光，打破对 AI 工具“一键生成即完成”的幻觉。
- **Human vs AI Responsibility Split (人机责任分工)**：
  - **学生必须亲自**：制定拍摄方案、筛选优质参考、诊断生成结果的通道级破损、进行艺术意图微调与物理合规验收；
  - **AI / 自动化工具执行**：前向贴图估计、色彩重构、无缝边缘拼接算法解算；
  - *核心红线*：绝不允许直接将未经质检与去光照的 AI/照片生成贴图直接贴上模型交付。
- **Irreplaceable Teaching Gain (不可替代教学收益)**：
  使学生具备在 2026 年现代工业环境中整合前沿 AI 工具与真实数据资产的能力。删除此项，学生要么对新技术产生盲目恐惧与抗拒，要么沦为被低劣 AI 生成贴图牵着鼻子走的被动操作工。
- **Minimum Evidence of Attainment (最低达成证据)**：
  提供一张带有强烈侧向阳光阴影的砖墙实拍照片（或 AI 生成图），学生能利用工具链剥离阴影与高光，生成 Base Color / Normal / Roughness / Height 贴图，在 LookDev 视口中验证其在相反光照方向下不再出现反向假光照穿帮。
- **Minimal Hands-on Hypothesis (动手实验假说)**：
  在手机拍摄一张生活中的粗糙材质（如树皮或石地），导入 Sampler 执行 Image-to-Material，手动对比开启和关闭 Delighting 时的 Base Color 纯度直方图。
- **Supporting Candidate IDs (支撑候选能力)**：
  `V02-C31`, `V02-C32`, `V02-C33`, `V02-C34`, `V02-C41`, `V02-C47`
- **Teacher / Infrastructure-only Elements (教师/底层参考)**：
  多角度偏振光度立体采集设备搭建（Photometric Stereo Rig）；扩散模型底层注意力机制（Attention Latent）代码研究。
- **Unresolved Assumptions**：无。

---

### LO6: 目标交付约束对齐、着色一致性调校与 LookDev 验证
*Target Delivery Constraints, LookDev Verification & Adaptation*

- **Observable Student Performance (学生实际能做什么)**：
  学生能将完成的材质资产置于标准的 LookDev 检验环境中，在多套高动态范围环境光（HDRI：高对比直射烈日、低对比阴天漫射、室内暖色复杂光）下进行 360 度旋转光照压力测试与白炉无自发光测试；面对下游目标引擎的物理限制，能独立完成贴图通道转译打包（如游戏引擎 ORM：Occlusion $\to$ R, Roughness $\to$ G, Metallic $\to$ B，正确配置 sRGB/Linear 开关）；能识别并调校材质在不同渲染视口（实时光追视口 vs 离线路径追踪渲染器）之间的外观差异与微表面衰减偏差。
- **Attainment Depth (达成深度)**：
  - `INDEPENDENT PRACTICE`：LookDev 多环境视口旋转验证、游戏运行时 ORM 通道打包与导出配置、色彩空间（sRGB vs Linear）严格绑定；
  - `SUPPORTED / TEMPLATE PRACTICE`：母材质实例继承体系调用（Material Instances）、实时引擎贴图压缩格式（BC7/BC5/BC1）设置；
  - `RECOGNIZE & EXPLAIN`：影视动画出口 UsdShade 材质绑定逻辑（网格绑定 vs 几何子集 GeomSubsets 局部绑定）及多渲染上下文机制；跨引擎（Filmic vs ACES vs AgX）色调映射对材质外观的影响；
  - `INFRASTRUCTURE / TEACHER REFERENCE`：Unreal Engine 底层 Shader 变体分支（Permutations）代码优化；GPU 渲染管线带宽瓶颈分析；深度 MaterialX/UsdShade API 编程式绑定。
- **Prerequisite / Practice Burden (前置与练习负担)**：
  - `Medium`。需要建立严谨的交付意识与格式标准，理解下游管线的真实痛点。
- **Human vs AI Responsibility Split (人机责任分工)**：
  - **学生必须亲自**：在不同极端光照下肉眼审查材质响应、调校参数使资产在不同视口中保持视觉一致性；
  - **AI / 脚本工具代劳**：批量通道合成与文件重命名、自动化模型 LOD 导出；
  - *核心红线*：资产必须经过全光照压力测试，禁止仅在单一默认环境光下确认资产。
- **Irreplaceable Teaching Gain (不可替代教学收益)**：
  连接艺术创作与生产落地的最后一公里。删除此项，学生做出的材质只能存在于自己的单一软件视口中，一旦放入真实游戏关卡或影视镜头合成中就会彻底崩溃失真。
- **Minimum Evidence of Attainment (最低达成证据)**：
  学生提交一套包含三张不同 HDRI 光照下同一资产渲染截图的“LookDev 验证画板”，并导出一套在目标实时引擎（如 UE5 / Blender EEVEE）中赋予资产后外观完全一致、无显存通道浪费的 ORM 贴图集。
- **Minimal Hands-on Hypothesis (动手实验假说)**：
  将一个资产放入烈日与阴天两个反差极大的 HDRI 视口中旋转，观察并记录其粗糙度高光扩散与暗部环境遮挡是否符合自然规律。
- **Supporting Candidate IDs (支撑候选能力)**：
  `V02-C17`, `V02-C35`, `V02-C36`, `V02-C37`, `V02-C38`, `V02-C39`, `V02-C40`, `V02-C44`*, `V02-C46`*
- **Teacher / Infrastructure-only Elements (教师/底层参考)**：
  `V02-C44` 中 MaterialX XML 语法手写与 NodeDef 编写；`V02-C46` 中 UsdShade C++ API 底层调用；实时引擎 Substrate 材质节点系统底层集成。
- **Unresolved Assumptions**：无。

---

## 4. 跨成效去重与冗余度检查 (Cross-outcome Redundancy & Balance Check)

在确立上述 6 个成效后，必须进行严苛的结构性去重与边界防膨胀审查：

| 审查维度 | 审查结论与设计防线 |
| :--- | :--- |
| **LO1 (观察) vs LO2 (光学因果) 是否重叠？** | **边界清晰，无需合并**。LO1 侧重于**宏观审美与艺术意图**（故事、年代、视觉层级、现实细节感知），属于“看与解构”；LO2 侧重于**微观光学与物理自洽性**（反照率范围、金属度判定、能量守恒、数据通道排错），属于“理与诊断”。两者共同构筑材质感知基石。 |
| **LO3 (分层绘制) vs LO4 (程序化系统) 是否重叠？** | **范式独立，各自闭环**。LO3 针对**三维模型特定空间位置的资产级多通道分层修饰**（以 Painter 为代表的图层栈与遮罩局部修订）；LO4 针对**连续无缝、基于数学规则与参数暴露的母材质系统**（以 Shader Nodes / Designer 为代表的节点拓扑与变体控制）。两者是现代材质制作不可分割的互补能力。 |
| **LO5 (获取与 AI) vs LO3 (分层绘制) 是否重叠？** | **输入端与加工端的明确分工**。LO5 解决的是**素材来源的多范式获取、AI 前向预测与缺陷去光照初加工**；LO3 解决的是获取之后**如何在资产空间上建立可控图层栈进行受控局部修订**。LO5 生成的扁平位图通过 LO3 完成分层重构。 |
| **是否遗漏艺术判断 (Artistic Judgment)？** | **未遗漏，且已显式制度化**。LO1 将“艺术意图与视觉层级”作为核心评估指标；LO3 将“遵循艺术指导进行局部受控修改”作为实践标准；LO5 将“多范式决策权衡”作为非量化的人类审美决断。艺术判断不再是空洞口号，而是融入每次作业的具体依据。 |
| **是否滑向了繁琐的管线工程学 (Pipeline Engineering Overload)？** | **严格防御，成功隔离**。坚决将 MaterialX XML 手写、UsdShade API 编程式绑定、ShaderGen 驱动、Agent 闭环架构、GPU 硬件级汇编等高门槛工程内容全部剥离至“教师底层参考层”（详见第 6 节），确保学生端保持在直观、可视、可操作的艺术设计核心层。 |

---

## 5. 研究全集映射总表 (Research Inventory Mapping: LO $\to$ Candidates)

为维持研究全集的完整可追溯性，将 Candidate Set v2 (`V02-C01`–`V02-C47`) 全量 47 项映射至各 Learning Outcome 及对应教学层角色中。

> **映射原则声明**：
> - 47 项是已归档的证据全集，不是教学任务单；
> - 一个 Outcome 可由多个 Candidate 共同支撑；一个 Candidate 可在多个 Outcome 中作为背景知识交叉出现；
> - 标有 `[Teacher/Infra]` 的候选能力表明该能力的核心技术实现仅供教师演示或作为平台底座，不构成学生上机实操考核。

| Learning Outcome (成效单元) | 支撑的 Candidate Set v2 编号 | 涵盖的关键技术与实证要素 |
| :--- | :--- | :--- |
| **LO1: 材质观察与艺术意图解构** | `V02-C01`, `V02-C09` | 现实物理特征观察、人眼感知与成像动态范围、宏观/中观/微观多级频域细节尺度解构。 |
| **LO2: 光学因果与物理可信性** | `V02-C02`, `V02-C03`, `V02-C04`, `V02-C05`, `V02-C06`, `V02-C08`, `V02-C10`, `V02-C42` | 能量守恒定律、反照率安全范围（30–240 sRGB）、GGX 微表面粗糙度、金属度二值法则、切线空间法线坐标系（OpenGL vs DirectX）、AO 漫反射解耦、线性与非色彩色彩管理、跨通道物理自洽性诊断。 |
| **LO3: 多通道分层受控修订** | `V02-C11`, `V02-C12`, `V02-C13`, `V02-C14`, `V02-C15`, `V02-C16`, `V02-C18`*, `V02-C19`*, `V02-C20`*, `V02-C21`*, `V02-C43` | 资产工程与通道架构、非破坏性图层与多通道同步混合、空间局部遮罩与投影绘制、自适应智能材质模板封装、底材-涂层-磨损物理工艺演化、环境接触风化因果、扁平贴图分层重构与受控修订。<br>*(注：带 * 号的几何与烘焙支撑项 C18–C21 作为支撑 LO3 正常运转的前置必要技能，按支持深度纳入)* |
| **LO4: 参数化系统与变体控制** | `V02-C22`, `V02-C23`, `V02-C24`, `V02-C25`, `V02-C26`, `V02-C27`, `V02-C28`, `V02-C30`, `V02-C29`*[Teacher/Infra] | 结构化节点图与 DAG 拓扑、空间坐标系转换（UV/Object/World/Triplanar）、分形连续噪波与 Voronoi 胞元合成、节点数学运算与 Map Range 重映射、真实物理尺度对齐（Metric Scale）、对象随机种子与平铺打散、参数接口设计与子图封装、程序化静态位图烘焙。<br>*(C29 运行时插件集成主要作为架构演示)* |
| **LO5: 多源获取与 AI 评估精修** | `V02-C31`, `V02-C32`, `V02-C33`, `V02-C34`, `V02-C41`, `V02-C47` | 真实世界材质漫射拍摄光学规程、单图多通道算法估计与置信度层级判定、去光照残留缺陷诊断与手工曲线/画笔精修、无缝平铺与宏观大色块消除、空间几何条件生成心智、多范式权衡决策树（生成 vs 检索 vs 参数化 vs 实拍）。 |
| **LO6: 目标交付约束与 LookDev** | `V02-C17`, `V02-C35`, `V02-C36`, `V02-C37`, `V02-C38`, `V02-C39`, `V02-C40`, `V02-C44`*, `V02-C46`* | 贴图导出模板配置、交互式视口物理着色检验、实时引擎母材质与参数化实例、运行时贴图开销与 ORM 打包、高保真多层着色（次表面/清漆/薄膜）物理特性、跨渲染引擎着色差异与色调映射调校、多环境 IBL 旋转压力测试与白炉测试。<br>*(C44 与 C46 核心标准语义纳入学生理解，底层编程接口列入教师参考)* |
| **隔离层 (纯前沿/底层参考)** | `V02-C45`*[Teacher/Infra] | 机器可读材质图拓扑、XML 序列化与 Agent 自动化操作边界（保持为教师前沿视野拓展，不设为学生必修实操）。 |

---

## 6. 显式非学生直面 / 教师底层参考清单 (Explicitly Non-Student-Facing / Teacher-Reference)

为了坚决防止“因为概念在工业上先进或机器可读，就盲目塞给本科生上机实操”的技术冒进错误，特在此明确划定**非学生直面（Non-Student-Facing）**与**教师底层参考（Teacher Reference / Infrastructure-only）**的能力边界：

### 6.1 MaterialX 深度技术实现与 XML 编程 (V02-C44 深度实现)
- **学生直面层（保留）**：学生必须理解 MaterialX 倡导的“通用物理着色语义”与“结构化节点图逻辑”，能够在支持的 DCC 软件中打开并调节基于 MaterialX/OpenPBR 规范的着色节点。
- **教师底层参考层（隔离，学生不直面）**：
  - 手写或修改 MaterialX XML 文件代码；
  - 编写自定义 `NodeDef`（节点定义）与数据类型模式；
  - MaterialX 跨平台着色器生成管线（ShaderGen C++ 库集成与 GLSL/HLSL/MSL 代码生成）。

### 6.2 OpenUSD / UsdShade 编程式绑定与底层 API (V02-C46 深度实现)
- **学生直面层（保留）**：学生必须理解 USD 的跨平台资产交付角色；理解材质在动画流程中是如何作为一个独立的组件与网格进行引用的；理解 `outputs:surface` 与特定渲染器上下文（Render Context）的外观差异。
- **教师底层参考层（隔离，学生不直面）**：
  - 使用 Python / C++ 调用 `UsdShadeMaterialBindingAPI` 进行编程式图元绑定；
  - 编写复杂的 USD 几何子集继承关系与变体集合（VariantSets）管线配置；
  - 多层 USD 层级覆盖（Layer Stacking & Sublayer Composition Arcs）的复杂解析逻辑。

### 6.3 智能体编排与自主图表自动化操作 (V02-C45 深度实现)
- **学生直面层（保留）**：学生需要理解为什么结构化的参数和节点相比一张死图更容易被程序或 AI 识别和受控修改（Durable Concept）。
- **教师底层参考层（隔离，学生不直面）**：
  - 开发基于 LLM / VLM 的材质节点图自动生成 Agent；
  - 编写无头（Headless）Blender Python 自动化材质渲染与参数微调服务器；
  - 工业级 API 编排与自动化构建流水线搭建。

### 6.4 游戏引擎底层 Shader 变体与汇编级性能调优 (V02-C36 / V02-C37 深度实现)
- **学生直面层（保留）**：学生必须遵守贴图尺寸预算，掌握 ORM 贴图打包（BC7/BC5/BC1），并在引擎视口中检查 Shader Complexity（着色器复杂度视图）。
- **教师底层参考层（隔离，学生不直面）**：
  - 实时引擎底层 USF/HLSL 着色器模板编写；
  - 静态开关（Static Switch）引发的万级 Shader 变体编译机器集群调度；
  - GPU 硬件级 Wavefront 占用率与微架构显存带宽瓶颈深度 Profiling。

---

## 7. Gate 3A 未决决策与用户决策清单 (Gate 3A Unresolved Decisions)

在本阶段推进中，发现以下需要用户（课程主管）在进入后续教学设计（Gate 3B/3C）前进行战略拍板的事项：

### 决策点 1：程序化材质的核心教学环境定位 (Procedural Authoring Host)
- **背景**：LO4 确立了程序化/参数化材质思维的必要性，但 8 周时间极度有限。
- **选项 A（推荐）**：以 **Blender Shader Nodes** 为主实操平台（免费开源、即时可视、学生零门槛安装、与 Python/通用节点逻辑天然亲和），辅以少量 Substance 3D Designer 核心概念演示；
- **选项 B**：坚持以 **Substance 3D Designer** 为主要上机实操环境，开设 1–2 周专项 Designer 训练（专业度极高，但软件上手门槛陡峭，可能挤压多通道绘制和 AI 转换的课时）。
- **当前状态**：`USER DECISION NEEDED`。

### 决策点 2：双出口评价权重的课程重心 (Dual-target Assessment Weighting)
- **背景**：课程已确定兼顾实时游戏与影视动画，但两者在终期作业中如何分配精力。
- **选项 A（推荐）**：以 **实时游戏/交互引擎（UE5/Blender EEVEE）** 约束为基准交付标准（涵盖严格的贴图打包、尺寸预算与烘焙），将影视离线 LookDev 作为审美与高阶着色特例；
- **选项 B**：以 **影视高保真渲染（Arnold/Cycles/USD）** 为基准交付标准（侧重次表面、复杂分层与高位深），将实时打包作为压缩简化出口。
- **当前状态**：`USER DECISION NEEDED`。

---

## 8. Gate 3A 总结与推进建议 (Gate 3A Recommendation)

### 8.1 架构合理性自评
1. **规模精炼**：从原本无序的 47 项技术点收敛为 **6 个高内聚的学习成效**，完全适配 8 周本科实训课程的心智负荷；
2. **直面人机分工**：明确确立了“观察、意图、因果逻辑、审美验收必须由人类主导，低层重复性计算与初稿可由工具代劳”的原则，保证了教学在 AI 时代的长期持久性（Durability）；
3. **消除工程学膨胀**：将工业底层 XML、API 编程与复杂管线基础设施严格隔离到教师参考层，守护了“材质艺术与质感创作”的纯正教学边界。

### 8.2 下一步行动路线 (Next Steps)
- **本轮交付**：固化本文档 `docs/research/teaching-layer-architecture.md`，提交 Commit 并推送到 GitHub，在 Issue #5 回复评审摘要；
- **等待外部审查**：等待 Browser 针对本架构文档进行 Gate 3A 审查并获取 PASS；
- **后续 Gate（暂不展开）**：
  - **Gate 3B — Minimal Content Selection**：为上述 6 个成效挑选最紧凑的候选技术子集；
  - **Gate 3C — Representative Task Feasibility**：设计一个具体的综合代表性材质作业，检验 6 项成效的串联可行性；
  - **Gate 3D — Teaching Action Backfill**：最终完成 47 项 Candidate 的状态回填。

---
*本文档生成并归档于 `docs/research/teaching-layer-architecture.md`，作为 Gate 3A 正式交付基线。*
