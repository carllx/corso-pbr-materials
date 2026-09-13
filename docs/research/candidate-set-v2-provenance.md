# Candidate Set v2 来源归属与实证对齐审计 (Candidate Set v2 Provenance Alignment Audit)

> **研究阶段**：Stage 2 Gate 2.5B — Candidate Provenance Alignment (Evidence-Hardened Revision)  
> **审查锚点 (Review Anchor)**：`ce814f76ac2cea97c140a073b8279b3416ee7e47` (Gate 2.5B Initial Delivery) $\to$ 本轮修订锚点  
> **权威候选集依据**：`docs/research/candidate-set-rebaselining-audit.md` (全量 47 项：`V02-C01`–`V02-C47`，保持严格冻结)  
> **治理约束**：Governed by Issue #3 (Stage 2 Strategy Clarification) 与 Issue #4 (Comment ID: `5652269980`)。本 Gate 职责仅为“逐项建立来源归属与证据充分性”，回答“各项能力由哪些教材、官方规范、研究证据或项目推论支撑”；**严禁包含任何 Gate 3 教学动作裁决（KEEP / COMPRESS / REFRAME / REPLACE / ADD_NEW_SKILL 等），严禁设计 Week 1–8 排课或软件课时分配，严禁修改候选集分类结构（ADD/REMOVE/MERGE/SPLIT/REDEFINE）**。

---

## 目录
1. [审计原则、来源分类与匹配标准](#1-审计原则来源分类与匹配标准)
2. [Candidate Set v2 (47 项) 来源实证对齐总表](#2-candidate-set-v2-47-项-来源实证对齐总表)
   - [2.1 模块一：物理光学与因果素养 (V02-C01 ~ V02-C10)](#21-模块一物理光学与因果素养-v02-c01--v02-c10)
   - [2.2 模块二：三维多通道创作与受控修订 (V02-C11 ~ V02-C17)](#22-模块二三维多通道创作与受控修订-v02-c11--v02-c17)
   - [2.3 模块三：几何支撑与细节烘焙管线 (V02-C18 ~ V02-C21)](#23-模块三几何支撑与细节烘焙管线-v02-c18--v02-c21)
   - [2.4 模块四：程序化系统与参数化节点 (V02-C22 ~ V02-C29)](#24-模块四程序化系统与参数化节点-v02-c22--v02-c29)
   - [2.5 模块五：材质采集转换与范式选择 (V02-C30 ~ V02-C34, V02-C47)](#25-模块五材质采集转换与范式选择-v02-c30--v02-c34-v02-c47)
   - [2.6 模块六：高保真着色、LookDev 与严苛验证 (V02-C35 ~ V02-C40)](#26-模块六高保真着色lookdev-与严苛验证-v02-c35--v02-c40)
   - [2.7 模块七：结构化表达、生成受控与智能体交互 (V02-C41 ~ V02-C46)](#27-模块七结构化表达生成受控与智能体交互-v02-c41--v02-c46)
3. [统计与证据分布诊断总结](#3-统计与证据分布诊断总结)
4. [特殊清单与边界隔离声明](#4-特殊清单与边界隔离声明)
   - [4.1 Project Inference (含 E 类推导) 单元隔离说明](#41-project-inference-含-e-类推导-单元隔离说明)
   - [4.2 仅依赖官方文档 (OFFICIAL-DOC ONLY) 单元说明](#42-仅依赖官方文档-official-doc-only-单元说明)
   - [4.3 时间敏感性官方证据 (Version-Sensitive Evidence) 记录](#43-时间敏感性官方证据-version-sensitive-evidence-记录)
   - [4.4 Freeze-Reopen Finding 专项核查](#44-freeze-reopen-finding-专项核查)

---

## 1. 审计原则、来源分类与匹配标准

### 1.1 核心任务与边界
本审计只回答一个核心问题：
> **Candidate Set v2 的每一项能力，究竟由哪些教材、官方规范、研究/行业证据或项目推论支撑？**

不回答“应不应该教”、“教多少课时”、“哪个软件最重要”。47 项候选能力是本 Gate 的固定输入。

### 1.2 来源权威等级定义 (Source Classes)
严格按照 Issue #3 与 Gate 2.5B 规范划分为 5 类来源（可多选）：

* **`A — Primary Textbook`**：
  主教材正文有明确章节、小节或完整案例直接支持。
  * **唯一主教材**：Zeeshan Jawed Shah — *Realistic Asset Creation with Adobe Substance 3D* (Packt, 2022)。
* **`B — Selected Supporting Text`**：
  选定辅助专著正文有明确对应章节或小节直接支持。
  * **选定支撑文献**：
    1. Wes McDermott — *The PBR Guide, 3rd ed.* (Allegorithmic / Adobe, 2018; Part 1 & Part 2)；
    2. Eran Dinur — *The Complete Guide to Photorealism, 2nd ed.* (Routledge, 2026)；
    3. Tomas Akenine-Möller et al. — *Real-Time Rendering, 4th Edition* (CRC Press, 2018；**RTR4 统一标定为 Class B**)。
* **`C — Living Official Source`**：
  第一手活体官方技术规范与官方开发文档直接条款支持。
  * **覆盖范围**：ASWF OpenPBR Surface Specification v1.1.1、ASWF MaterialX Specification v1.39、Pixar OpenUSD / UsdShade 规范、Adobe Substance 3D Painter 官方文档、Adobe Substance 3D Designer 官方文档、Adobe Substance 3D Sampler 官方文档、Blender 5.2/4.5 LTS 官方手册及 Python API、Epic Games Unreal Engine 5.8 官方技术文档。
* **`D — Research / Industry Evidence`**：
  已审核登记的真实一手学术顶会论文（NeurIPS/CVPR/ICLR）、技术演讲规范（如 Brian Karis SIGGRAPH 2013）或一手行业深度访谈（如 80 Level Tripo 访谈）。
  * **纪律要求**：不得将综合报告 `ai-impact-on-material-workflows.md` 本身标为 D 类 authority，必须解析回溯到其中登记的真实一手学术论文与行业证据。
* **`E — Project Inference Only`**：
  由本项目根据教学法延伸、跨系统集成或流程组织进行综合推导设立的概念、作业规范或决策模型，在现有审核文献中无点对点直接支持。必须显式隔离。

### 1.3 证据匹配状态定义 (Match Status)
对全量 47 项 Candidate 严格指定唯一主匹配状态：

* **`DIRECT MATCH`**：已审核来源明确且直接支持 Candidate 的核心能力与技术定义。
* **`PARTIAL MATCH`**：来源仅支持 Candidate 的一部分（如基础物理原理或工具功能），其余实操流程或质检标准依赖项目综合。
* **`OFFICIAL-DOC ONLY`**：在传统出版教材（A/B 类）中缺乏专章支持，主要且直接依托 C 类活体官方规范与技术文档。
* **`RESEARCH ONLY`**：主要依赖 D 类学术论文或行业证据支持，缺乏传统教材与成熟官方软件文档直接支撑。
* **`PROJECT INFERENCE`**：核心决策树或结构模型目前主要由 E 类综合推导形成，来源仅提供离散事实切片。
* **`NOT FOUND`**：当前已审核来源中找不到足够依据（严禁为了掩盖而凭空捏造来源；如实暴露为 0 或具体项）。

---

## 2. Candidate Set v2 (47 项) 来源实证对齐总表

### 2.1 模块一：物理光学与因果素养 (V02-C01 ~ V02-C10)

| Candidate ID | Candidate Capability | Source Class | Owning Source | Exact Evidence Pointer | Match Status | Source Actually Supports | Project Synthesis / Boundary |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **V02-C01** | 现实材质物理属性观察与多维参考解构 *(Physical Material Observation & Multi-attribute Reference Decomposition)* | `B` | Dinur (2026); RTR4 | Dinur (2026) Ch 1 (pp. 1–25), Ch 3 (pp. 45–70); RTR4 Ch 9.1 (pp. 317–323) | `DIRECT MATCH` | 人眼感知与相机成像差异、动态范围控制、色彩空间知觉、宏观到微观的多级物理特征与材质表面不完美性观察模型。 | 将观察模型系统化为数字材质实训的前置参考解构维度（固有色/粗糙度/法线几何扰动/风化分层）与情绪板规范。 |
| **V02-C02** | PBR 物理可信性与辐射度能量守恒 *(PBR Physical Plausibility & Radiometric Energy Conservation)* | `B`, `C` | McDermott (2018); RTR4; OpenPBR 1.1.1 | McDermott (2018) Part 1 (pp. 29–30); RTR4 Ch 9.2–9.3 (pp. 323–345); OpenPBR Spec §1.1, §2.1 | `DIRECT MATCH` | 辐射度能量守恒定律：出射辐射通量不得超过入射通量；漫反射与镜面反射能量互斥权衡（$1 - \text{Specular}$）；微表面 BRDF 能量守恒公式。 | 针对零数学基础学习者提炼免积分推导的“直方图能量守恒定性检验方法”与排查生成式贴图反射率过曝的质检规则。 |
| **V02-C03** | 漫反射/镜面反射率安全区间与去光照纯度判定 *(Reflectance Safe Ranges & Albedo Delighting Purity)* | `B`, `C` | McDermott (2018); OpenPBR 1.1.1; Dinur (2026) | McDermott (2018) Part 2 (pp. 48–52, Appendix pp. 89–92); OpenPBR Spec §3.1; Dinur (2026) Ch 3 (pp. 55–65) | `DIRECT MATCH` | 常见电介质固有色反射率区间（30–240 sRGB，严禁纯黑 0 与过曝 255）；非金属 F0 约 2%–5%（中心参考 4%）；金属固有色即为其镜面 F0（反射率通常 > 180 sRGB）；Base Color 必须剥离方向性光照与投射阴影。 | 提炼“反照率安全区间红线”作为作业质检刚性标准，并建立排查单张照片固有色中暗斑死黑的检测依据。 |
| **V02-C04** | 微表面粗糙度理论与微观几何法线分布 *(Microfacet Theory & Roughness NDF)* | `B`, `C` | McDermott (2018); RTR4; OpenPBR 1.1.1; Blender Manual | McDermott (2018) Part 1 (pp. 22–27), Part 2 (pp. 56–57); RTR4 Ch 9.2.2 (pp. 325–333); OpenPBR Spec §3.2; Blender 5.2 Manual ("Principled BSDF - Roughness") | `DIRECT MATCH` | 微表面法线分布函数（GGX / Cook-Torrance NDF）；微观几何遮蔽-阴影因子（Smith G 项）；粗糙度灰度值对高光斑扩散与反射模糊度的感知/线性映射。 | 明确微观粗糙度（控制高光雾化与微表面散射）与宏观法线/高度贴图（控制结构凹凸）在图层栈与着色网络中的结构分工。 |
| **V02-C05** | 金属导体与电介质光学分类与金属度边界准则 *(Conductor vs. Dielectric Optical Classification & Metallic Boundary Rules)* | `B`, `C` | McDermott (2018); RTR4; OpenPBR 1.1.1; UE 5.8 Docs | McDermott (2018) Part 1 (pp. 33–37), Part 2 (pp. 53–55); RTR4 Ch 9.4 (pp. 345–350); OpenPBR Spec §3.1; UE 5.8 Docs ("Physically Based Materials") | `DIRECT MATCH` | 纯物质常温下非导体即绝缘体，金属度贴图在物理意义上接近二值（0 或 1）；中间过渡灰阶仅在化学腐蚀氧化、极薄表面尘土混合物及 UV 抗锯齿插值像素中合法。 | 建立“金属度伪中间值灰度警报”教学检测表，专门排查 AI 生成模型与非标准采集贴图中的伪金属噪点。 |
| **V02-C06** | 切线空间法线几何扰动原理与跨坐标系对齐 *(Tangent Space Normal Principles & Coordinate Alignment)* | `A`, `B`, `C` | Shah (2022); McDermott (2018); Blender Manual; Painter Docs | Shah (2022) Ch 2 (pp. 45–48); McDermott (2018) Part 2 (pp. 76–79); Blender 5.2 Manual ("Normal Map Node"); Painter Docs ("Baking & Project Normal Format") | `DIRECT MATCH` | 切线空间（TBN 矩阵）下利用 RGB 扰动表面几何法线向量；DirectX (Y- 绿通道反转) 与 OpenGL (Y+ 绿通道基准) 格式差异及其跨 DCC/引擎转换。 | 针对 Blender、Painter 与 Unreal Engine 之间资产互导最常出现的法线凹凸颠倒、裂缝与接缝发黑建立排错清单。 |
| **V02-C07** | 视差映射与几何置换原理 *(Parallax Occlusion & Geometric Displacement Mapping)* | `A`, `B`, `C` | Shah (2022); McDermott (2018); Sampler Docs | Shah (2022) Ch 9–10 (pp. 240–270); McDermott (2018) Part 2 (p. 75); Sampler Official Docs ("Physical Size & Height") | `DIRECT MATCH` | 灰度高度图（Height Map）；基于着色器的视差遮蔽映射（POM）伪立体效果与微多边形曲面细分真实置换（Displacement）的几何形变差异；中点基准设置。 | 明确区分着色视差技巧（实时性能开销低、无模型轮廓改变）与几何细分置换（高显存算力、改变几何剪影）的生产适用场景。 |
| **V02-C08** | 环境光遮蔽物理意义与漫反射解耦 *(Ambient Occlusion Role & Diffuse Decoupling)* | `B`, `C` | McDermott (2018); Painter Baking Docs | McDermott (2018) Part 2 (p. 74); Painter Official Docs ("Baking - Ambient Occlusion") | `DIRECT MATCH` | 模拟微观几何缝隙/接触面对半球间接漫反射环境光的几何遮挡；AO 仅用于调制漫反射环境光，绝不可直接烘死在 Base Color 贴图中。 | 提炼教学诊断标准：排查“新手及自动化工具将环境遮挡与直接阴影错误乘入固有色贴图”的穿帮现象。 |
| **V02-C09** | 表面细节多级频率与空间尺度解构 *(Multi-frequency Surface Detail Decomposition: Macro/Medium/Micro)* | `A`, `B` | Shah (2022); Dinur (2026) | Dinur (2026) Ch 1 (pp. 12–18), Ch 3 (pp. 52–60); Shah (2022) Ch 3–6 (Multi-frequency Layering) | `DIRECT MATCH` | 表面细节分为 Macro（体量与宏观分件）、Medium（转折边角磨损、裂痕、装配缝隙）、Micro（微观粗糙、气孔颗粒、拉丝）三级频域认知模型。 | 将三级频域尺度直接映射到图层栈分层（底材-过渡-高频噪波）与程序化噪波频率阶数（Octaves/Scale）的设计与评估量表。 |
| **V02-C10** | 色彩管理与线性管线规范 *(Color Management & Linear Workflow Specification: sRGB vs. Linear/Data)* | `B`, `C` | McDermott (2018); RTR4; OpenPBR 1.1.1; Painter Docs | McDermott (2018) Part 1 (pp. 38–39); RTR4 Ch 5.6 (pp. 143–149); OpenPBR Spec §1.2; Painter 12.1 Docs ("Color Management / OCIO") | `DIRECT MATCH` | 人眼非线性感知 Gamma 2.2 矫正与计算机线性物理光照空间转换；色彩贴图（Base Color）采用 sRGB/ACES 色彩管理，数值数据贴图（Normal, Roughness, Metallic, Height, AO）强制使用 Linear / Non-Color / Raw。 | 总结跨软件流转中贴图被误标为 sRGB 导致粗糙度变白、金属度失效的一键排错操作规范。 |

---

### 2.2 模块二：三维多通道创作与受控修订 (V02-C11 ~ V02-C17)

| Candidate ID | Candidate Capability | Source Class | Owning Source | Exact Evidence Pointer | Match Status | Source Actually Supports | Project Synthesis / Boundary |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **V02-C11** | 贴图工程架构、通道配置与色彩管理绑定 *(Texture Project Architecture, Channel Setup & Color Management Binding)* | `A`, `C` | Shah (2022); Painter Official Docs | Shah (2022) Ch 1 (pp. 15–30); Painter Official Docs ("Project configuration", "Texture Set Settings", "Color Management / OCIO") | `DIRECT MATCH` | 资产贴图工程初始化；导入 3D 网格、识别多材质球并划分材质集（Texture Set List）；配置工程所需的物理通道（Base Color, Rough, Metal, Normal, Height）；绑定 OCIO 色彩配置环境。 | 从特定软件界面初次点击向导，抽象为通用的“网格-材质集-物理通道-色彩管理”工程初始化架构。 |
| **V02-C12** | 非破坏性图层系统与多物理通道同步求值 *(Non-destructive Layer Stacking & Synchronized Multi-channel Evaluation)* | `A`, `C` | Shah (2022); Painter Official Docs | Shah (2022) Ch 3 (pp. 65–88); Painter Official Docs ("Layer Stack", "Channel Blending Modes") | `DIRECT MATCH` | 填充层（Fill Layer）、绘制层（Paint Layer）、图层组与锚点（Anchor Points）；单一图层内多物理通道（Color, Rough, Metal, Normal, Height）相互独立求值与混合模式运算；非破坏性局部微调。 | 确立“资产级材质创作必须保持多物理通道同步绑定运算，严禁纯单通道破坏性涂抹”的工程纪律。 |
| **V02-C13** | 空间局部遮罩体系、投影绘制与特征细节修饰 *(Spatial Mask Hierarchy, Viewport Projection Painting & Feature Detailing)* | `A`, `C`, `D` | Shah (2022); Painter Official Docs; Yanpei Cao (Tripo) 80 Level Interview (2026-08-28) | Shah (2022) Ch 4–5 (pp. 95–145); Painter Official Docs ("Masking", "Projection Tool", "Geometry Fill", "Clone Tool"); 80 Level Interview (2026-08-28) | `DIRECT MATCH` | 黑白遮罩、几何多边形填充（Polygon Fill）、三维视口投影绘制（Stencil / Projection）、笔刷手绘与克隆工具；定位空间特征细节并修补 UV 接缝拉伸伪影与烘焙瑕疵。 | 将手绘特征细节修饰与生成式贴图接缝拉伸/伪影修复（吸收原 AI-U08）合并为统一的空间局部受控修饰能力。 |
| **V02-C14** | 几何特征驱动的自适应材质分层封装与模板复用 *(Geometry-driven Adaptive Material Encapsulation & Template Reuse)* | `A`, `C` | Shah (2022); Painter Official Docs | Shah (2022) Ch 4 (pp. 102–115), Ch 6 (pp. 150–175); Painter Official Docs ("Generators", "Smart Materials & Smart Masks") | `DIRECT MATCH` | 利用烘焙派生的网格贴图（Curvature 边缘曲率、AO 缝隙暗角、World Normal 朝向、Position 空间位置），通过算法生成器自适应驱动遮罩；将多通道图层栈打包封装为自适应材质模板（`.spsm`）以跨模型复用。 | 将原 M02-U04（智能材质）与 M02-U05（智能生成器）合并为一个高阶封装复用逻辑，消除软件菜单的人为碎片化。 |
| **V02-C15** | 材质物理工艺分层与底材-涂层-风化因果演变 *(Material Stratification & Substrate-to-Wear Physical Chronology)* | `A`, `B` | Shah (2022); Dinur (2026) | Shah (2022) Ch 4–6 (TV Case Study Layering); Dinur (2026) Ch 5 (pp. 95–120), Ch 13 (pp. 210–230) | `DIRECT MATCH` | 真实制造工艺与时间演化分层：基底材质（Substrate：裸金属/原木/工程塑料）$\to$ 底漆与防锈层 $\to$ 表面面漆/涂层 $\to$ 机械划伤与面漆剥落 $\to$ 环境侵蚀与氧化锈迹 $\to$ 表层浮尘与指纹油脂。 | 将工业工艺学分层逻辑固化为材质作业评估与物理真实感验收的核心准则。 |
| **V02-C16** | 环境风化、接触磨损与空间位置因果模拟 *(Environmental Weathering, Contact Abrasion & Spatial Position Causality)* | `A`, `B` | Shah (2022); Dinur (2026) | Shah (2022) Ch 6 (pp. 165–170); Dinur (2026) Ch 5 (pp. 100–118) | `DIRECT MATCH` | 机械力学接触（突出边角磨损、抓握受力部位脱漆）、重力场沉积（Position Y 朝上表面积尘积灰、凹陷滞水）、流体冲刷与环境交互进行因果演变模拟。 | 将软件做旧滤镜参数调节升华为结合资产世界观设定与空间物理规律的“因果演变模拟与受控修调”。 |
| **V02-C17** | 目标引擎贴图格式转译与通道映射配置 *(Target Engine Texture Export Translation & Channel Mapping Configuration)* | `A`, `C` | Shah (2022); Painter Official Docs | Shah (2022) Ch 6 (pp. 175–180); Painter Official Docs ("Exporting Textures", "Output Templates") | `DIRECT MATCH` | 根据下游目标引擎（Unreal Engine 4/5 Packed, Unity HDRP, glTF）或离线渲染器（Arnold, V-Ray）接口规范配置导出模板；将多物理通道重新排列映射至单张位图的 RGB 通道（如 ORM 打包），并指定位深度与色彩空间。 | 从 Painter 专属点击导出预设，抽象为面向通用渲染目标的“资产交付协议与通道转译映射规范”。 |

---

### 2.3 模块三：几何支撑与细节烘焙管线 (V02-C18 ~ V02-C21)

| Candidate ID | Candidate Capability | Source Class | Owning Source | Exact Evidence Pointer | Match Status | Source Actually Supports | Project Synthesis / Boundary |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **V02-C18** | UV 参数化质量评估、接缝布局与拉伸诊断 *(UV Parameterization Quality Assessment, Seam Layout & Distortion Diagnosis)* | `A`, `B`, `C` | Shah (2022); McDermott (2018); Painter Docs | Shah (2022) Ch 1 (pp. 16–20); McDermott (2018) Part 2 (pp. 60–63); Painter Official Docs ("Auto Unwrap", "UV Tiles / UDIM") | `DIRECT MATCH` | UV 坐标展开与空间参数化对纹理贴图采样的几何映射影响；接缝（Seams）隐蔽放置于视觉盲区或自然分件接缝；棋盘格/网格拉伸诊断与重叠排查；自动算法展开与装箱的质量评估。 | 严格界定“非建模课”教学边界：核心在于诊断、评估与指导自动/外部展开质量，而非从零手撕复杂拓扑展开。 |
| **V02-C19** | 模型光滑组硬边与 UV 接缝拓扑协同准则 *(Hard Edges vs. UV Seams Topological Alignment & Artifact Prevention)* | `B` | McDermott (2018); RTR4 | McDermott (2018) Part 2 (pp. 60–63); RTR4 Ch 6 (pp. 160–165) | `DIRECT MATCH` | 多边形网格平滑组/硬边（Hard Edges / Smoothing Group Splits）处必须切开 UV 接缝；若硬边未切开 UV 接缝，光线投射烘焙时在顶点法线非连续插值处必出现严重黑线伪影与渐变穿帮。 | 建立“烘焙法线边缘黑斑的拓扑协同诊断法则”，用于快速排查低模法线硬边未切开接缝的几何拓扑错误。 |
| **V02-C20** | 纹素密度规划、一致性分配与跨资产对齐 *(Texel Density Planning, Consistency Budgeting & Asset Alignment)* | `A`, `B` | Shah (2022); McDermott (2018) | Shah (2022) Ch 1 (pp. 18–21); McDermott (2018) Part 2 (pp. 58–60) | `DIRECT MATCH` | 纹素密度（Texel Density，像素/厘米）的定义与度量；单资产各 UV 岛以及同场景多资产间纹素密度必须保持一致，防止局部清晰、局部模糊的精度失配。 | 制定资产交付标准中的纹素密度预算量化检验规程与分辨率分配准则。 |
| **V02-C21** | 几何细节投影烘焙、网格贴图派生与烘焙伪影诊断 *(Geometric Detail Baking, Mesh Map Derivation & Artifact Diagnosis)* | `A`, `C` | Shah (2022); Painter Official Docs | Shah (2022) Ch 1 (pp. 20–30); Painter Official Docs ("Baking", "Baking Mode F8", "Baking Parameters & Cage", "Paint Skew") | `DIRECT MATCH` | 高低模（High-to-Low Poly）映射关系与包裹笼（Cage）射线投射原理；烘焙派生网格贴图（Normal, Curvature, Position, AO, Thickness）；利用 Paint Skew 修正法线射线偏斜，排查投射穿插、漏射黑边与法线反转。 | 将高低模拓扑匹配（原 M03-U04）与网格贴图烘焙及排错（原 M03-U05）合并为一个完整的几何投影工程闭环。 |

---

### 2.4 模块四：程序化系统与参数化节点 (V02-C22 ~ V02-C29)

| Candidate ID | Candidate Capability | Source Class | Owning Source | Exact Evidence Pointer | Match Status | Source Actually Supports | Project Synthesis / Boundary |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **V02-C22** | 结构化节点图架构与数据流拓扑原理 *(Structured Shader Graph Architecture & Directed Dataflow Topology)* | `A`, `C` | Shah (2022); Blender Manual; Designer Docs; MaterialX Spec | Shah (2022) Ch 7 (pp. 185–205); Blender 5.2 Manual ("Shader Nodes - Overview"); Designer Docs ("Graph architecture"); MaterialX Spec v1.39 §2.1–2.2 | `DIRECT MATCH` | 有向无环图（DAG）单向数据流拓扑；强类型系统（标量 Float/Boolean、向量 Vector2/3/4、色彩 Color3/4、着色表面 Shader/Surface）；节点输入-处理-输出架构与子图嵌套。 | 跨 Designer、Blender 与 MaterialX 抽象出通用的结构化着色器图表拓扑模型，为程序化创作与 Agent 机器读写提供统一认知框架。 |
| **V02-C23** | 多维空间纹理坐标系转换与映射逻辑 *(Texture Coordinate Systems & Spatial Mapping: UV, Object, World, Triplanar)* | `A`, `C` | Shah (2022); Blender Manual; Designer Docs | Blender 5.2 Manual ("Texture Coordinate Node"); Designer Docs ("Coordinates and Transform"); Shah (2022) Ch 7–8 (pp. 205–225) | `DIRECT MATCH` | 纹理坐标系的数学转换：展开 UV 空间、Generated（模型包围盒 0–1 归一化空间）、Object（以物体中心为原点的三维度量空间）、Camera 空间；三平面投影（Triplanar Mapping）免展 UV 贴合原理。 | 总结在复杂有机模型或快速铺底阶段摆脱模型展开 UV 依赖、实现无拉伸程序化纹理投射的应用模式。 |
| **V02-C24** | 程序化算法噪波与自然图案合成 *(Procedural Noise Generators & Mathematical Pattern Synthesis)* | `A`, `C` | Shah (2022); Blender Manual; Designer Docs | Shah (2022) Ch 8 (pp. 210–230); Blender 5.2 Manual ("Noise Texture Node", "Voronoi Texture Node"); Designer Docs ("Noise and Patterns") | `DIRECT MATCH` | 数学算法生成无分辨率限制的程序化图案：Perlin/Simplex 分形连续噪波（模拟有机污迹、自然斑驳）、Voronoi/Cells 沃罗诺伊图（模拟泥土干裂、晶体切面、细胞微观表面）、Musgrave 多重分形。 | 提炼“频率尺度（Scale）+ 分形细节（Detail）+ 粗糙对比度（Roughness/Contrast）”三元参数因果调控法则。 |
| **V02-C25** | 节点数学运算、通道混合与数值区间重映射 *(Node Mathematics, Channel Blending & Range Remapping)* | `A`, `C` | Shah (2022); Blender Manual; Designer Docs | Shah (2022) Ch 9 (pp. 235–255); Blender 5.2 Manual ("Math Node", "Mix Node", "ColorRamp Node", "Map Range Node"); Designer Docs ("Pixel Processor", "Transformation 2D") | `DIRECT MATCH` | 标量与向量数学算术运算（Add, Subtract, Multiply, Min/Max, Clamp, Power）；混合因子遮罩（Fac / Alpha Blending）；渐变映射（ColorRamp）与数值区间重映射（Map Range / Levels）将 0–1 连续灰阶映射到物理安全区间或特定渐变。 | 将数学运算（原 M04-U04）与区间重映射（原 M04-U05）合并为一个连续的数据调理与通道塑造能力。 |
| **V02-C26** | 纹理空间变换、真实物理尺度对齐与平铺控制 *(Texture Spatial Transformation, Metric Scale Calibration & Tiling Control)* | `A`, `C` | Shah (2022); Sampler Docs; Blender Manual; Designer Docs | Shah (2022) Ch 8 (pp. 215–225), Ch 11 (pp. 302–304); Sampler Docs ("Physical Size"); Blender 5.2 Manual ("Mapping Node"); Designer Docs ("Transformation 2D") | `DIRECT MATCH` | 纹理平铺 UV 比例（Tiling U/V）、平移与旋转；Sampler 中的真实世界物理尺寸标定（Physical Size，如 2.0m × 2.0m），使虚拟纹理映射与现实米制单位对齐以避免比例失真。 | 将映射缩放平铺（原 M04-U06）与物理尺寸校准（原 M05-U05）合并为一个完整的真实空间物理尺度校准规范。 |
| **V02-C27** | 对象随机变体、种子控制与重复感消除 *(Object-level Variation, Seed Randomization & Tiling Pattern Breaking)* | `C` | Blender Manual; Designer Docs | Blender 5.2 Manual ("Object Info Node - Random", "Geometry Node"); Designer Official Docs ("Tile Sampler", "Random Seed Parameter") | `OFFICIAL-DOC ONLY` | 提取对象实例随机值（Random ID / Object Info）驱动色相微调、粗糙度偏移与 UV 坐标随机扰动；基于随机种子（Seed）的大规模阵列排布与贴图重复感打散。 | 总结“宏观低频噪波加权 + 微观对象随机种子偏移”双层打散大面积铺设重复痕迹的技术模式。 |
| **V02-C28** | 模块化子图封装与有意义的参数接口暴露 *(Modular Subgraph Encapsulation & Meaningful Parameter Interface Design)* | `A`, `C` | Shah (2022); Designer Docs; Blender Manual; MaterialX Spec | Shah (2022) Ch 7 (pp. 200–205); Designer Docs ("Creating and Exposing Parameters", "Subgraphs"); Blender 5.2 Manual ("Node Groups"); MaterialX Spec v1.39 §2.3 ("NodeGraph & Interface") | `DIRECT MATCH` | 将内部复杂的节点网络封装为复合子图（Node Groups / Subgraphs）；对外暴露有意义的控制参数接口（Sliders/Toggles），定义参数名称、数据类型、合法极值范围（Min/Max）与默认值，提供黑盒模块化调用。 | 提炼“母材质（Master Material）设计规范”，强调为下游艺术家或自动化脚本暴露语义明确、不可损坏内部拓扑的参数面板。 |
| **V02-C29** | 可复用参数化材质资产打包与动态运行时集成 *(Reusable Parametric Material Packaging & Dynamic Runtime Integration)* | `A`, `C` | Shah (2022); Designer Official Docs | Shah (2022) Ch 7 (pp. 202–205), Ch 10 (pp. 260–280); Designer Official Docs ("Publishing SBSAR", "Substance Integration Plugins") | `DIRECT MATCH` | 参数化材质图表编译与发布为独立资产包（如 `.sbsar`）；跨软件与游戏引擎运行时（Unreal / Unity / Blender Substance Plugin）集成，并在运行时通过插件或 API 动态实时调整暴露参数并重新烘焙贴图。 | 剔除单一商业格式限制，从可复用参数化材质资产包架构与跨宿主动态集成调用的系统高度进行解构。 |

---

### 2.5 模块五：材质采集转换与范式选择 (V02-C30 ~ V02-C34, V02-C47)

| Candidate ID | Candidate Capability | Source Class | Owning Source | Exact Evidence Pointer | Match Status | Source Actually Supports | Project Synthesis / Boundary |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **V02-C30** | 程序化节点网络向标准位图集的静态烘焙与精度控制 *(Procedural Graph Baking to Static Bitmap Sets & Bit-depth Precision Control)* | `A`, `C` | Shah (2022); Blender Manual; Designer / SAT Docs | Shah (2022) Ch 10 (pp. 275–280); Blender 5.2 Manual ("Render - Baking"); Designer Docs ("Baking Nodes", "SAT commandline baking") | `DIRECT MATCH` | 将高计算开销的动态程序化节点图解算烘焙为静态标准 PBR 贴图集（Albedo, Normal, Roughness 等）；控制烘焙分辨率与位深度（Normal / Height 强制 16-bit/32-bit 以防阶梯状量化断层，数据贴图保持非色彩色彩管理）。 | 建立程序化动态算力开销与静态位图交付之间的性能折衷权衡模型。 |
| **V02-C31** | 真实世界材质采集光学原理与数字化反向推导 *(Photometric Capture Principles & Reverse Material Estimation)* | `B`, `C` | Dinur (2026); Sampler Official Docs | Dinur (2026) Ch 13 (pp. 210–225 "Scan and Reference Processing"); Sampler Official Docs ("Material Acquisition", "Multiangle to Material", "Physical Size") | `DIRECT MATCH` | 真实世界多角度光照采集（Multiangle to Material）实拍反向求解原理；偏振镜消除直射高光与阴天均匀漫射光下拍摄以最大程度解耦环境阴影在 Dinur Ch 13 中作为实拍扫描基准。 | 制定手机/单反实地材质参考拍摄的“漫射光照与标定球辅助采集指南”作业标准。 |
| **V02-C32** | 单张图像/照片多通道 PBR 属性算法推导与置信度评估 *(Single-image Multi-channel PBR Estimation & Confidence Evaluation)* | `C`, `D`, `E` | Sampler Official Docs; IntrinsiX (NeurIPS 2025); LumiTex (ICLR 2026) | Sampler Official Docs ("Image to Material: AI-Powered vs. B2M Filters"); IntrinsiX (NeurIPS 2025, arXiv:2504.01008); LumiTex (ICLR 2026, arXiv:2511.19437) | `PARTIAL MATCH` | 基于前向神经网络（如 Sampler AI-Powered、IntrinsiX、LumiTex）从单张未受控 RGB 图像预测生成 Base Color, Normal, Roughness, Height 贴图的算法能力与去光照分解机制。 | 来源直接证明了多通道算法前向生成，但“法线/粗糙度估算相对可靠，而金属度与深层凹凸极易误判”的通道级置信度层级判定规则属于项目综合推导（含 E）。 |
| **V02-C33** | 漫反射光照残留诊断与反照率手工/算法去光照精修 *(De-lighting Inspection, Albedo Purity QA & Manual/Algorithmic Correction)* | `C`, `D`, `E` | Sampler Docs; IntrinsiX (NeurIPS 2025); LumiTex (ICLR 2026); Painter Docs | Sampler Docs ("Delighting Filter"); IntrinsiX (NeurIPS 2025, arXiv:2504.01008); LumiTex (ICLR 2026, arXiv:2511.19437 §4.2); Painter Docs ("Clone Tool", "Curves") | `PARTIAL MATCH` | 算法去光照在深阴影、几何自遮挡与复杂间接光照下的失效事实（漫反射贴图中残留暗斑死黑导致重新打光穿帮）；官方提供的自动去光照滤镜工具（Delighting）。 | 来源指出去光照缺陷并提供基础滤镜，但“利用高反差保留、通道曲线反向补偿与 Painter 空间画笔手工剥离阴影死黑”的完整精修实操规程属于项目综合推导（含 E）。 |
| **V02-C34** | 纹理图像无缝平铺处理与宏观大色块重复消除 *(Seamless Texture Tiling & Macro Clumping Elimination)* | `A`, `C` | Shah (2022); Sampler Docs | Shah (2022) Ch 11 (pp. 298–302); Sampler Official Docs ("Tiling Filter", "Generative Tiling Beta") | `DIRECT MATCH` | 纹理位图边缘重叠混合与对称淡化以消除贴图 UV 边界缝隙；宏观特征点与显著色斑在周期性平铺时的重复感排查与消除。 | 总结在自动化平铺生成后人工消除宏观大色块集聚（Macro Clumping）的标准质检流程。 |
| **V02-C47** | 材质获取范式权衡决策：生成、检索、参数化复用与实拍转换 *(Material Acquisition Paradigm Selection: Generation vs. Retrieval vs. Procedural Reuse vs. Capture)* | `B`, `C`, `D`, `E` | Dinur (2026); Tripo 80 Level Interview (2026); Adobe Firefly Licensing Docs; Sampler Docs | Dinur (2026) Ch 1, 13, 19; 80 Level Interview (2026-08-28); Firefly Licensing FAQ; Sampler Docs §2.4, §3.1 | `PROJECT INFERENCE` | 来源分别证明：AI 生成快但难微调且有商用版权合规限制（Firefly Docs / Tripo 访谈）；资产库检索保真度高但难完美匹配特定非标需求；参数化母材质灵活但开发成本高；照片扫描真实但光照解耦难。 | 将分散于商业、版权、拓扑、物理和工期各维度的独立事实，归纳整合为通用的“多范式权衡决策树（何时生成、何时检索、何时参数化、何时实拍）”属于项目综合推导（含 E）。 |

---

### 2.6 模块六：高保真着色、LookDev 与严苛验证 (V02-C35 ~ V02-C40)

| Candidate ID | Candidate Capability | Source Class | Owning Source | Exact Evidence Pointer | Match Status | Source Actually Supports | Project Synthesis / Boundary |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **V02-C35** | 交互式视口物理着色检验与快速环境响应验证 *(Interactive Viewport Shading Inspection & Rapid Environmental Response Validation)* | `C` | Blender Manual; Painter Docs | Blender 5.2 Manual ("Viewport Shading - Material Preview & Rendered", "EEVEE Next Shading"); Painter Official Docs ("Viewport Shading", "Render Mode - Iray") | `OFFICIAL-DOC ONLY` | 在实时光栅化/混合光追视口中快速观察 Principled / OpenPBR 材质对多方向光照、粗糙度变化与金属度响应的交互反馈；快速排查通道连接断裂与着色黑斑。 | 构建用于快速上机检查的轻量化 LookDev 交互视口自检模板。 |
| **V02-C36** | 实时引擎材质母版架构与参数化材质实例体系 *(Realtime Engine Master Material Architecture & Parameterized Material Instancing)* | `C`, `D` | UE 5.8 Docs; Brian Karis (SIGGRAPH 2013) | UE 5.8 Docs ("Material Instances", "Creating and Using Material Instances", "Physically Based Materials"); Karis (2013) pp. 1–10 | `DIRECT MATCH` | 实时引擎中母材质（Master Material）静态拓扑设计、暴露标量/向量/纹理参数；通过材质实例（Material Instances / MIC）实现无需重新编译着色器的高速参数调优；静态开关参数（Static Switch Parameters）引发着色器变体（Permutations）代码分支编译的底层机制。 | 提炼跨实时引擎通用的母版着色拓扑与实例化继承树设计方法。 |
| **V02-C37** | 实时游戏运行时材质性能开销、通道打包与硬件压缩 *(Realtime Runtime Material Performance, Channel Packing & Hardware Compression)* | `B`, `C`, `D` | McDermott (2018); UE 5.8 Docs; Brian Karis (SIGGRAPH 2013) | McDermott (2018) Part 2 (pp. 60–63); UE 5.8 Docs ("Texture Compression Settings and Formats: BC7, BC5, BC1", "Material Performance Guidelines"); Karis (2013) | `DIRECT MATCH` | 游戏运行时性能开销控制：将 Occlusion(R)、Roughness(G)、Metallic(B) 合并为单一纹理采样器以减少带宽占用；GPU 块压缩格式（BC7 针对高质量色彩与高保真贴图，BC5 针对双通道法线 RG，BC1/DXT1 针对电介质 Base Color）；Draw Call、采样器上限与显存预算约束。 | 将工业级显存与贴图带宽预算规范转化为教学端可执行的“运行时贴图开销计算与质检清单”。 |
| **V02-C38** | 高保真多层着色模型物理特性与因果表达 (次表面/清漆/薄膜) *(High-fidelity Multilayer Shading Physics: Subsurface, Clear Coat & Thin Film)* | `B`, `C` | OpenPBR Spec 1.1.1; Dinur (2026); RTR4 | OpenPBR Spec §3.3 ("Clear Coat Subsystem"), §3.4 ("Subsurface Scattering Subsystem"), §3.5 ("Thin Film Subsystem"); Dinur (2026) Ch 11–12 (pp. 175–195); RTR4 Ch 9.6 (pp. 355–365) | `DIRECT MATCH` | 半透光材质的次表面散射（Subsurface Scattering / BSSRDF：透光深度、各向异性、平均自由程）；多层介质表面清漆涂层（Clear Coat：独立粗糙度与双层反射高光）；薄膜干涉（Thin Film Interference：微米级油膜与金属氧化变色物理计算）。 | 基于 OpenPBR 规范将高阶光学参数提炼为可直观调节的因果层级控制模型。 |
| **V02-C39** | 跨渲染引擎着色差异分析与视觉一致性调校 *(Cross-renderer Shading Discrepancy Diagnosis & Visual Consistency Alignment)* | `B`, `C` | McDermott (2018); RTR4; OpenPBR Spec 1.1.1 | McDermott (2018) Part 2 (pp. 80–88); RTR4 Ch 9.10 (pp. 375–385); OpenPBR Spec §1.1 ("Scope and Motivation") | `DIRECT MATCH` | 相同一套 PBR 贴图在不同渲染器中外观差异的根本原因：微表面微观几何遮蔽模型差异（Smith vs. Kelemen）、漫反射环境光球谐积分近似差异、色调映射（Tone Mapping / ACES vs. AgX vs. Filmic）与曝光曲线差异。 | 建立跨软件/跨渲染器外观对比实验设计，帮助学生形成“没有一套贴图在所有引擎里天然长得一模一样”的主动调校思维。 |
| **V02-C40** | 多环境 IBL 旋转压力测试与严苛物理一致性验证 *(Multi-environment IBL Rotation Stress Testing & Rigorous Physical Consistency QA)* | `B`, `C` | Dinur (2026); McDermott (2018); OpenPBR Spec 1.1.1; Painter Docs | Dinur (2026) Ch 12 (pp. 185–198); McDermott (2018) Part 1 (pp. 38–40); OpenPBR Spec §2.1 (White Furnace Test); Painter Docs ("LookDev Viewport Environments") | `DIRECT MATCH` | 利用高动态范围图像（HDRI）在差异化光照环境（室内暖光、室外高动态烈日、阴天漫射光）下 360 度旋转照射，检验材质光照响应；白炉测试（White Furnace Test）验证无自发光与能量耗散异常。 | 吸收原 AI-U13 约束清单，制定 LookDev 多环境三联验证截图验收标准（烈日/阴天/室内三场景）。 |

---

### 2.7 模块七：结构化表达、生成受控与智能体交互 (V02-C41 ~ V02-C46)

| Candidate ID | Candidate Capability | Source Class | Owning Source | Exact Evidence Pointer | Match Status | Source Actually Supports | Project Synthesis / Boundary |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **V02-C41** | 几何条件引导与多模态参考约束的材质生成控制 *(Geometry-conditioned & Multimodal Reference-guided Material Generation)* | `B`, `D` | Dinur (2026); Material Anything (CVPR 2025); MatLat (CVPR 2026); ControlNet (2023) | Dinur (2026) Ch 19 (pp. 310–335); Material Anything (CVPR 2025, arXiv:2411.15138); MatLat (CVPR 2026); ControlNet (ICCV 2023, arXiv:2302.05543) | `DIRECT MATCH` | 针对 3D 网格几何特征（深度、法线、表面坐标与专用材质隐空间）生成解耦 PBR 材质贴图的专用生成架构（Material Anything, MatLat）；ControlNet 先验与图像嵌入提供通用空间保形与风格约束；Dinur 论述 ControlNet 条件生成在写实管线中的应用。 | 提炼基于空间几何与图像参考双条件约束生成的心智模型，摆脱对特定单点工具面板的依赖。 |
| **V02-C42** | 跨通道 PBR 物理自洽性诊断与多贴图逻辑矛盾排查 *(Cross-channel PBR Consistency Diagnosis & Inter-map Logical Conflict Auditing)* | `B`, `D`, `E` | McDermott (2018); Yanpei Cao (Tripo) 80 Level Interview (2026-08-28) | McDermott (2018) Part 2 Appendix (pp. 89–92); 80 Level Interview (2026-08-28) | `PARTIAL MATCH` | PBR 各通道之间的物理对应关系（法线凹凸应伴随粗糙度变化与接触阴影）；工业实测表明当前 AI 生成材质在多通道自洽性上存在断裂（如法线存在深凹槽但粗糙度完全平滑无积垢、金属度为 1 但固有色亮度严重偏低）。 | 来源指出了 PBR 规范和 AI 通道矛盾现象，但将其整理为系统的“跨通道多贴图物理体检排错清单与量化诊断规则”属于项目综合推导（含 E）。 |
| **V02-C43** | 扁平生成纹理的非破坏性分层重构与局部受控修订 *(Non-destructive Layer Reconstruction & Localized Controlled Revision from Flat Textures)* | `A`, `C`, `E` | Shah (2022); Meshy Docs; Painter Docs | Shah (2022) Ch 3–4 (pp. 65–120); Meshy Texturing Docs (Outputting Flat PBR Textures); Painter Official Docs ("Anchor Points", "Mask from Color") | `PARTIAL MATCH` | 生成式 AI 工具（如 Meshy 等）输出的是扁平无图层信息的烘焙位图，无法提供可修改的参数化图层；Painter 拥有完整的图层栈、遮罩提取与锚点系统。 | 提出“将生成式扁平位图导入 DCC $\to$ 提取色彩/高频遮罩 $\to$ 拆解为底材-涂层-磨损的非破坏性图层堆栈 $\to$ 实现局部受控修订（Edit Locality）”的人机协同分层重构方法论属于项目综合推导（含 E）。 |
| **V02-C44** | 开放标准材质语义与结构化表示: OpenPBR 材质语义 + MaterialX 图元模式 *(Open Material Semantics & Structured Representation: OpenPBR Semantics + MaterialX Graph/Schema)* | `C` | OpenPBR Spec 1.1.1; MaterialX Spec 1.39 | OpenPBR Surface Specification v1.1.1 (§1.1 Scope, §2 Architecture, §3 Parameters); MaterialX Specification v1.39 (§2 Core Elements, §2.1 NodeGraphs, §2.2 NodeDefs, §2.3 Interfaces) | `OFFICIAL-DOC ONLY` | 明确区分现代开放材质的两大支柱：OpenPBR 定义标准表面着色物理语义（Surface Shading Model、参数名称、数据范围与多层介质混合规则）；MaterialX 提供中立的强类型节点图拓扑、XML 数据序列化模式、NodeDef 规范与跨平台代码生成（ShaderGen）。 | 提炼“标准物理着色语义（OpenPBR）”与“结构化中立图数据模式（MaterialX）”的分层解耦认知框架。 |
| **V02-C45** | 机器可读材质图表拓扑、序列化协议与智能体可操作性 *(Machine-readable Material Graph Topology, Serialization Protocols & Agent Operability)* | `C`, `D`, `E` | MaterialX Spec 1.39; Blender Python API; Designer Python API; VLMaterial (ICLR 2025); Node To Talk Docs | MaterialX Spec v1.39 (XML Serialization Schema); Blender Python API (`bpy.data.materials`, `nodes.new`); Designer Python API; VLMaterial (ICLR 2025, arXiv:2501.18623); Node To Talk Docs | `PARTIAL MATCH` | 材质节点图支持结构化 XML（MaterialX）与 Python API 脚本化解析/读写/无头构建；VLMaterial 证实通过大型视觉-语言模型（VLM）直接生成 Blender 程序化材质 Python 代码与节点图；Node To Talk 演示将视口节点树导出为拓扑有序文本供 AI 排错。 | 来源直接证明了节点图的机器可读性与 VLM 代码生成原型，但“自主 Agent 安全读写、修改并校验任意工业级复杂材质图”目前超出直接实证范围，属于未来技术框架推导（含 E）。 |
| **V02-C46** | 双出口表示转换损失认知与目标交付适配 (影视动画 USD/渲染上下文绑定 + 实时游戏原生转换约束) *(Dual-target Representation Conversion Loss Awareness & Delivery Adaptation: Animation/VFX USD Binding + Realtime Engine Constraints)* | `C`, `D` | OpenUSD UsdShade Spec; UE 5.8 Docs; MaterialX Developer Guide; Karis (2013) | OpenUSD Documentation ("UsdShade Schema", `UsdShadeMaterialBindingAPI`, Render Contexts `outputs:surface` / `outputs:arnold:surface`); UE 5.8 Official Docs ("Interchange Framework - MaterialX Support Matrix", "Material Instances", "Permutations"); Karis (2013) | `DIRECT MATCH` | 影视动画出口：UsdShade 材质绑定规范（直接网格绑定、集合 Collection 绑定与几何子集 GeomSubsets 局部绑定），多渲染器上下文终端机制与外观对齐；实时游戏出口：MaterialX/OpenPBR 导入实时引擎（如 UE 5.8）时的转换损失（未连接/透传节点 Pass-through、Unsupported BSDFs 退化）、着色器变体（Permutations）膨胀开销、ORM 通道打包与性能预算。 | 确立核心认知三位一体判定准则：$$\text{Valid Representation} \neq \text{Visual Equivalence} \neq \text{Production Deliverable}$$。 |

---

## 3. 统计与证据分布诊断总结

### 3.1 总体规模
- **Candidate Set v2 总项数**：**47 项** (`V02-C01`–`V02-C47`，全量覆盖，无遗漏)

### 3.2 来源类别分布统计 (Source Class Counts)
*(注：同一 Candidate 可由多个来源类别共同支持，类别间非互斥)*

| 来源类别 (Source Class) | 支撑项数 (Count) | 占比 (47 项基准) | 主要集中分布模块 |
| :--- | :--- | :--- | :--- |
| **Class A — Primary Textbook** (Shah 2022) | **23 项** | 48.9% | 模块二 (贴图绘制 7 项)、模块三 (烘焙支撑 3 项)、模块四 (程序化 7 项)、模块五 (采集 2 项)、模块一 (光学 3 项)、模块七 (1 项) |
| **Class B — Supporting Texts** (McDermott / Dinur / RTR4) | **23 项** | 48.9% | 模块一 (物理光学基础 10 项全部覆盖)、模块三 (3 项)、模块六 (LookDev 4 项)、模块七 (2 项)、模块二 (2 项)、模块五 (2 项) |
| **Class C — Living Official Sources** (官方文档与开放规范) | **39 项** | 83.0% | 模块四 (程序化 8 项)、模块一 (8 项)、模块二 (5 项)、模块五 (5 项)、模块六 (6 项)、模块七 (4 项)、模块三 (2 项)、决策项 (1 项) |
| **Class D — Research / Industry Evidence** (顶会论文/行业访谈) | **10 项** | 21.3% | 模块五 (去光照 2 项)、模块七 (生成/Agent/双出口 4 项)、模块六 (实时性能 2 项)、模块二 (接缝修复 1 项)、决策项 (1 项) |
| **Class E — Project Inference Only** (含项目综合推导边界) | **6 项** | 12.8% | `V02-C32` (通道置信度层级), `V02-C33` (去光照手工精修), `V02-C42` (跨通道体检表), `V02-C43` (扁平图层重构), `V02-C45` (Agent 闭环边界), `V02-C47` (范式决策树) |

### 3.3 证据匹配状态分布统计 (Match Status Counts)
*(注：每项根据其主要证据模式严格指定唯一状态，互斥统计)*

| 匹配状态 (Match Status) | 项数 (Count) | 对应 Candidate 列表 |
| :--- | :--- | :--- |
| **`DIRECT MATCH`** | **38 项** | `V02-C01`–`V02-C26`, `V02-C28`–`V02-C31`, `V02-C34`, `V02-C36`–`V02-C41`, `V02-C46` |
| **`PARTIAL MATCH`** | **5 项** | `V02-C32` (单图通道估算置信度), `V02-C33` (去光照手工精修), `V02-C42` (跨通道体检表), `V02-C43` (扁平贴图分层重构), `V02-C45` (机器可读图与 Agent 边界) |
| **`OFFICIAL-DOC ONLY`** | **3 项** | `V02-C27` (对象随机变体), `V02-C35` (交互视口着色), `V02-C44` (开放标准材质语义) |
| **`RESEARCH ONLY`** | **0 项** | *(无；所有涉 D 研究项均已与 B 类教材或 C 类官方规范形成协同支撑)* |
| **`PROJECT INFERENCE`** | **1 项** | `V02-C47` (材质获取范式权衡决策树) |
| **`NOT FOUND`** | **0 项** | *(无；全量 47 项均拥有可核验的一手文献与规范条款支撑，无凭空捏造项)* |
| **数学核算校验** | **47 项** | $$38 (\text{DIRECT}) + 5 (\text{PARTIAL}) + 3 (\text{OFFICIAL}) + 0 + 1 (\text{INFERENCE}) + 0 = 47$$ |

---

## 4. 特殊清单与边界隔离声明

### 4.1 Project Inference (含 E 类推导) 单元隔离说明
在全量 47 项中，**没有任何一项是纯 E 构成的无源空想单元（E-Only = 0）**。以下 6 项单元含有 E 类项目综合推导，均已显式划定事实与推导的边界：

1. **`V02-C32: 单张图像/照片多通道 PBR 属性算法推导与置信度评估`**
   - *底层客观事实 (C, D)*：Sampler AI-Powered、IntrinsiX (2025) 与 LumiTex (2026) 证实从单图预测 PBR 多通道及去光照分解算法的存在。
   - *项目推导边界 (E)*：“法线/粗糙度估算相对可靠，而金属度与深层凹凸极易误判”的通道级置信度层级判定规则属于项目教学法实测归纳。
2. **`V02-C33: 漫反射光照残留诊断与反照率手工/算法去光照精修`**
   - *底层客观事实 (C, D)*：LumiTex (2026) 与 IntrinsiX (2025) 证实算法去光照在深阴影处仍有残留；官方工具提供 Delighting 基础滤镜。
   - *项目推导边界 (E)*：结合通道反向曲线补偿与 Painter 空间克隆画笔的手工去光照修补操作规程属于项目教学法综合。
3. **`V02-C42: 跨通道 PBR 物理自洽性诊断与多贴图逻辑矛盾排查`**
   - *底层客观事实 (B, D)*：McDermott (2018) 确立通道对应规则；80 Level Tripo 访谈揭示 AI 生成贴图跨通道撕裂（凹凸无粗糙度响应）。
   - *项目推导边界 (E)*：将上述撕裂现象整理为系统化的“跨通道多贴图物理体检排错清单与量化验收表”属于项目综合推导。
4. **`V02-C43: 扁平生成纹理的非破坏性分层重构与局部受控修订`**
   - *底层客观事实 (A, C)*：Meshy 等生成工具输出扁平位图；Shah (2022) 与 Painter 提供图层栈与遮罩提取能力。
   - *项目推导边界 (E)*：“导入扁平贴图 $\to$ 提取色彩/高频遮罩 $\to$ 逆向重构底材-涂层-磨损图层栈”的人机协同局部受控修订方法论属于项目综合推导。
5. **`V02-C45: 机器可读材质图表拓扑、序列化协议与智能体可操作性`**
   - *底层客观事实 (C, D)*：MaterialX Spec 与 Blender/Designer API 证明节点图支持结构化 XML 序列化与 Python 读写；VLMaterial (2025) 演示 VLM 生成材质代码原型；Node To Talk 演示节点树导出为文本。
   - *项目推导边界 (E)*：“自主 Agent 安全读写、修改并校验任意工业级复杂生产材质图”超出当前实证，属于前沿架构推导。
6. **`V02-C47: 材质获取范式权衡决策：生成、检索、参数化复用与实拍转换`**
   - *底层客观事实 (B, C, D)*：Dinur (2026)、Tripo 访谈、Firefly 许可规范分别确立生成、检索、参数化与实拍各自在速度、控制力、拓扑质量与商用合规上的边界。
   - *项目推导边界 (E)*：将离散事实提炼为统一的“多范式权衡决策树”属于项目综合推导。

### 4.2 仅依赖官方文档 (OFFICIAL-DOC ONLY) 单元说明
以下 3 项单元在传统纸质出版教材（Shah / McDermott / Dinur / RTR4）中缺乏专章阐述，其权威性完全由 **Class C (Living Official Sources)** 支撑：
1. **`V02-C27: 对象随机变体、种子控制与重复感消除`**：直接依托 Blender 5.2 官方手册（Object Info Random）与 Designer 官方文档（Tile Sampler Random Seed）。
2. **`V02-C35: 交互式视口物理着色检验与快速环境响应验证`**：直接依托 Blender 5.2 官方手册（Viewport Shading / EEVEE Next）与 Painter 官方文档（Viewport Shading）。
3. **`V02-C44: 开放标准材质语义与结构化表示: OpenPBR 材质语义 + MaterialX 图元模式`**：直接依托 ASWF OpenPBR 1.1.1 规范全文与 ASWF MaterialX 1.39 规范全文。

### 4.3 时间敏感性官方证据 (Version-Sensitive Evidence) 记录
在本次审计过程中，核实并记录以下具有明确版本锁定与时间演进特征的官方技术事实：
1. **OpenPBR 规范版本**：ASWF OpenPBR Surface Specification 当前稳定锚点为 `v1.1.1` (2026-04-17)；Substance 3D Painter 在 12.1 版本中已将 OpenPBR 1.1 设为默认材质着色模型。
2. **MaterialX 与 UE 集成独立事实**：
   - MaterialX 官方稳定发布版本为 `v1.39.5`；
   - Unreal Engine 5.8 官方 Interchange 文档集成为 `1.39.4`；
   - 两者作为独立客观技术事实记录。UE Interchange 支持矩阵中关于部分节点分类为 Pass-through（输入未连接）属于引擎独立的支持度策略，严禁将其表述为“因版本落差而导致的因果关系”。
3. **Substance 3D Sampler 生成式功能状态**：官方文档（2026-04）将生成式功能（Generative Features）标为 Beta；且 Generative Credits 计费政策与高校订阅免除条款在不同文档页面存在细微口径差异。
4. **Blender 渲染管线演进**：Blender 5.2 LTS / 4.5 LTS 的 Principled BSDF 持续向 OpenPBR 参数语义靠拢（重构了 Coat、Sheen 与 SSS）；EEVEE-Next 视口管线全面引入屏幕空间光追与实时位移。
5. **Unreal Engine Substrate 框架状态**：UE 5.8 中 Substrate 材质框架官方状态明确标为 **Beta**。

### 4.4 Freeze-Reopen Finding 专项核查
依据 Gate 2.5B Freeze Rule 严格复核：
* 是否有 Candidate 与来源事实实质矛盾？—— **无**。
* 是否有 Candidate 只能依赖纯 E 构成且无任何客观事实基础？—— **无**。
* 是否有 Candidate 在已审核证据库中完全找不到依据（NOT FOUND）？—— **无**。
* 是否有 Candidate 需要结构性变化（增删改并）才能成立？—— **无**。
* **结论**：`FREEZE-REOPEN FINDING: NONE (0)`。47 项 Candidate taxonomy 保持严格冻结。

---

*报告生成并归档于 `docs/research/candidate-set-v2-provenance.md`，作为 Gate 2.5B 唯一权威证据对齐基准。*
