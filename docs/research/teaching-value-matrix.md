# 《三维数字材质制作》教学价值矩阵 (Teaching Value Matrix)

> **研究阶段**：Stage 2 — AI 后材质能力保留、压缩与重构 (Issue #3)  
> **当前进度**：**Gate 1 (Normalize the Baseline) & Gate 2 (AI Impact Join) COMPLETED**  
> **审阅锚点**：基于 Phase 1 基线 [`curriculum-coverage-matrix.md`](curriculum-coverage-matrix.md)、教材定稿图谱 [`textbook-source-map.md`](textbook-source-map.md)、动态台账 [`course-design-ledger.md`](course-design-ledger.md) 与 AI 影响深度报告 [`ai-impact-on-material-workflows.md`](ai-impact-on-material-workflows.md) 构建。  
> **核心原则与纪律**：
> 1. **操作替代 ≠ 知识替代**：工具层面的手工操作自动化，绝不等于背后支撑知识与物理概念的贬值；相反，操作越自动化，对“诊断、校验与控制”心智模型的要求越高。
> 2. **证据严格定级**：严格区分 Vendor Capability、Academic / Demonstrated、Technical Specification / Platform Documentation、Production / Deployment、Limitation Evidence、Non-AI Workflow Automation 与 Project Inference，严禁把厂商宣传或 Demo 直接等同于成熟生产落地（Production-Ready）。
> 3. **Gate 纪律严格执行**：本阶段仅完成 **Gate 1 基线规范化** 与 **Gate 2 AI 证据逐项 Join**。所有教学决策字段（`Teaching Action`、`What to Teach Instead / Retain`、价值定级等）统一保持 `PENDING GATE 3`，等待 Browser 审阅通过后再行裁定。

---

## 目录
1. [矩阵维护原则与字段规范](#1-矩阵维护原则与字段规范)
2. [Gate 1：能力单元全集规范化定义 (Normalized Unit Baseline)](#2-gate-1能力单元全集规范化定义-normalized-unit-baseline)
3. [Gate 1 & Gate 2 主矩阵：传统 6 大模块逐项 AI Impact Join (44 单元)](#3-gate-1--gate-2-主矩阵传统-6-大模块逐项-ai-impact-join-44-单元)
   - [3.1 模块一：Material Literacy (材质素养与物理光学基础)](#31-模块一material-literacy-材质素养与物理光学基础)
   - [3.2 模块二：Texture-based Authoring (基于贴图的资产级材质创作)](#32-模块二texture-based-authoring-基于贴图的资产级材质创作)
   - [3.3 模块三：Supporting Pipeline Knowledge (材质支撑管线前置知识)](#33-模块三supporting-pipeline-knowledge-材质支撑管线前置知识)
   - [3.4 模块四：Procedural / Parametric Materials (程序化与参数化材质创作)](#34-模块四procedural--parametric-materials-程序化与参数化材质创作)
   - [3.5 模块五：Material Acquisition & Conversion (材质采集、图像转换与平铺)](#35-模块五material-acquisition--conversion-材质采集图像转换与平铺)
   - [3.6 模块六：LookDev & Multi-environment Validation (视觉开发与跨引擎验证)](#36-模块六lookdev--multi-environment-validation-视觉开发与跨引擎验证)
4. [Gate 2 补充矩阵：新兴 AI 原生材质技能池分级映射 (13 单元)](#4-gate-2-补充矩阵新兴-ai-原生材质技能池分级映射-13-单元)
5. [双出口应用分化特征总结 (Game Realtime vs. Animation / LookDev)](#5-双出口应用分化特征总结-game-realtime-vs-animation--lookdev)
6. [未决议题与证据缺口清单 (Genuinely Unresolved & Caveats)](#6-未决议题与证据缺口清单-genuinely-unresolved--caveats)

---

## 1. 矩阵维护原则与字段规范

### 1.1 字段定义 (Matrix Schema)
- **Unit (能力单元)**：规范化命名后的知识与技能单元（中英双语对齐）。
- **Baseline Teaching Necessity (传统教学必要性基线)**：继承自 Phase 1 基线（`Likely Core` / `Likely Important` / `Likely Optional` / `Supporting prerequisite` / `New Candidate`）。
- **AI / Automation Impact (AI 与自动化影响概述)**：截至 2026 年该单元受到的技术冲击、自动化现状或 AI 赋能边界。
- **Evidence Type & Source Link (证据类型与一手引证)**：
  - `Vendor Capability`：厂商明确提供的产品功能/Beta 特性；
  - `Academic / Demonstrated`：学术顶会/论文原型或演示流；
  - `Technical Specification / Platform Documentation`：平台/标准组织技术规范（非生产落地证明）；
  - `Production / Deployment`：真实商业项目/工作室管线落地案例；
  - `Limitation Evidence`：实测或行业指出的缺陷与失效点；
  - `Non-AI Workflow Automation`：传统确定性计算几何或光线追踪算法自动化；
  - `Project Inference`：基于实证形成的推断。
- **Game Realtime Relevance (实时游戏出口关联度)**：关注通道打包（ORM/Packed）、纹理压缩（BC7/ASTC）、Draw Call/着色器复杂度与动态光照稳定性。
- **Animation / LookDev Relevance (影视动画出口关联度)**：关注高阶物理材质（OpenPBR、次表面散射 SSS、清漆涂层 Coat、微位移置换）、ACES 色彩管理与光线追踪离线表现。
- **Gate 3 Status (Gate 3 决策占位)**：强制保持 `PENDING GATE 3`。
- **Caveat / Unresolved (特例说明与未决点)**：记录该单元目前在工具链支持、生产成熟度或课时冲突上的特定限制。

---

## 2. Gate 1：能力单元全集规范化定义 (Normalized Unit Baseline)

### 2.1 结构清洗与脱耦说明
在 Phase 1 的 [`curriculum-coverage-matrix.md`](curriculum-coverage-matrix.md) 中，表格横向列包含了大量特定教材列（如 *Born Digital 2022/2025*、*来阳 2026* 等）。根据 Stage 1 教材定稿（[`textbook-source-map.md`](textbook-source-map.md)），部分未购入或已淘汰教材不再作为课程依赖。
**Gate 1 规范化原则**：
1. **完整保留 44 项传统基线能力单元**，不因教材变更而发生遗漏；
2. **剔除特定教材的横向列耦合**，转向以“能力概念本身”为中心的规范化描述；
3. **保留并标准化 6 大核心模块**；
4. **并入在 Phase 2 调研中识别出的 13 项新兴 AI 原生材质候选技能**（划分为 Tier 1 / Tier 2 / Tier 3），形成总计 57 项完整审查全集；
5. **不修改旧 `curriculum-coverage-matrix.md` 的历史归档内容**。

---

## 3. Gate 1 & Gate 2 主矩阵：传统 6 大模块逐项 AI Impact Join (44 单元)

### 3.1 模块一：Material Literacy (材质素养与物理光学基础)

| Unit | Baseline Teaching Necessity | AI / Automation Impact (2026) | Evidence Type & Source Link | Game Realtime Relevance | Animation / LookDev Relevance | Gate 3 Status | Caveat / Unresolved |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **现实材质观察与参考分析**<br>*(Material Observation & Reference Analysis)* | `Likely Core` | 多模态大模型可提供材质语义标签、色彩提取与形态描述，但无法代替人眼对微观风化、触感质地与时间沉淀痕迹的深度感知。 | `Academic / Demonstrated`<br>[[Dinur 2026 Ch 1-4]](textbook-source-map.md) | 核心：决定资产在关卡光照下的第一眼可信度与叙事感。 | 核心：决定影视特写镜头下是否产生 CG“塑料感”。 | `PENDING GATE 3` | AI 可快速搜集情绪板，但艺术指导对微观质感的鉴赏力无法外包。 |
| **PBR 物理可信性与能量守恒**<br>*(PBR Physical Plausibility & Energy Conservation)* | `Likely Core` | 生成式 AI 缺乏内嵌的严格辐射度反射方程求解，AI 生成贴图频繁发生能量不守恒、漫反射反弹超标等问题。 | `Limitation Evidence` & `Technical Specification`<br>[[Karis 2013]](https://cdn2.unrealengine.com/Resources/files/2013SiggraphPresentationsNotes-26915738.pdf) / [[McDermott PBR Guide]](textbook-source-map.md) | 极高：光照环境突变（如进出室内外）时保证材质不自发光或突兀变黑。 | 极高：离线多跳全局光照（GI）计算中防止噪点爆炸与能量发散。 | `PENDING GATE 3` | 目前无任何黑盒 AI 能自动保证物理守恒，必须依赖理论验收。 |
| **Base Color 反射率与安全色阶**<br>*(Base Color Reflectance & Safe Values)* | `Likely Core` | 神经网络 De-lighting（去光照）模型可剥离光照，但经常残留环境漫射暗斑、死黑（<30 sRGB）或死白（>240 sRGB）。 | `Academic / Demonstrated`<br>[[IntrinsiX, NeurIPS 2025]](https://arxiv.org/abs/2410.22378) / [[LumiTex, ICLR 2026]](https://arxiv.org/abs/2501.03875) | 极高：UE/Unity 引擎材质合规性检查（Albedo Validation）的核心硬指标。 | 极高：影响离线次表面与漫射着色积分的准确性。 | `PENDING GATE 3` | 需重点训练“肉眼+直方图”识别去光照瑕疵与色偏。 |
| **Roughness 微表面粗糙度模型**<br>*(Roughness & Microfacet Theory)* | `Likely Core` | 单目深度与纹理模型可预测粗糙度图，但往往对比度过弱、高频磨损细节平坦，或呈现全图均匀高光。 | `Academic / Demonstrated`<br>[[Material Anything, CVPR 2025]](https://arxiv.org/abs/2411.15138) | 极高：直接决定实时视口高光倒影分布、粗糙度衰减与屏幕空间反射。 | 极高：决定 GGX/OpenPBR 镜面微表面分布与各向异性基础。 | `PENDING GATE 3` | AI 难以准确把握“干/湿”、“光滑/磨损”的微观接触过渡。 |
| **Metallic 金属度二值准则**<br>*(Metallic Binary Classification)* | `Likely Core` | AI 生成模型在金属边界频繁预测出过渡灰度噪点（0.2–0.7），破坏物理世界导体与电介质的绝对划分。 | `Technical Specification` & `Limitation Evidence`<br>[[Unreal Engine Physically Based Materials]](https://dev.epicgames.com/documentation/en-us/unreal-engine/physically-based-materials-in-unreal-engine) | 极高：中间灰度在实时渲染中会导致边缘出现发黑、假高光或着色错误。 | 极高：OpenPBR 规范要求严格分离 Dielectric 与 Conductor 菲涅尔。 | `PENDING GATE 3` | 需强化：纯材质必须严格近 0 或近 1，仅杂质过渡允许微弱过度。 |
| **Normal 切线空间法线原理**<br>*(Tangent Space Normal Principles)* | `Likely Core` | 2D 扩散模型生成的法线贴图无法理解 3D 网格切线空间基底，跨 UV 接缝处频繁发生法线反转与凹凸错位。 | `Academic / Demonstrated` & `Limitation Evidence`<br>[[MatLat, CVPR 2026]](https://github.com/matlat-pbr/matlat) / [[Tripo 80 Level Interview]](https://80.lv/articles/how-tripo-is-tackling-clean-topology-for-its-3d-asset-pipeline/) | 极高：实时光照依赖切线法线与顶点法线点积，方向错误直接导致阴影颠倒。 | 极高：影视级多边形平滑渲染不可或缺的微起伏表达。 | `PENDING GATE 3` | DirectX 与 OpenGL 绿通道（Y+/Y-）翻转仍是 AI 输出常见故障点。 |
| **Height / Displacement 几何置换**<br>*(Height & Displacement Mapping)* | `Likely Important` | 深度估算模型可快速生成置换图，但往往缺乏精确绝对几何位移标定，容易导致极端破面或几何撕裂。 | `Vendor Capability`<br>[[Adobe Sampler Generative Features]](https://helpx.adobe.com/substance-3d-sampler/generative-workflows/generative-features.html) | 中高：虚幻引擎 Nanite 网格置换、视差贴图（POM）的核心输入。 | 极高：离线渲染细分微多边形置换（Microdisplacement）的基石。 | `PENDING GATE 3` | 置换高度的绝对世界尺度（米制缩放）仍需人工匹配。 |
| **Ambient Occlusion 环境遮挡作用**<br>*(Ambient Occlusion Role & Limits)* | `Likely Core` | 传统烘焙与神经渲染均能自动生成 AO，但常被错误地直接叠加进 Base Color，破坏天光漫反射。 | `Non-AI Workflow Automation` & `Technical Specification`<br>[[McDermott PBR Guide]](textbook-source-map.md) | 极高：实时引擎漫反射间接光阴影模拟，通常打包进 ORM 的 Red 通道。 | 中等：离线光线追踪依靠精确多反弹 GI，AO 主要用于风格化或烘焙缓存。 | `PENDING GATE 3` | 强化认知：AO 仅用于调制间接光漫反射，严禁直接乘在固有色贴图上。 |
| **表面细节尺度与频率认知**<br>*(Detail Scales: Macro, Medium, Micro)* | `Likely Important` | 生成模型擅长填充随机中高频杂波，但缺乏针对三维资产体量的大（Macro）、中（Medium）、小（Micro）三级构图逻辑。 | `Academic / Demonstrated`<br>[[Dinur 2026 Ch 3]](textbook-source-map.md) | 高：关卡远景、中景与近距离持握视角下的视觉层级清晰度。 | 极高：电影级视效资产在大银幕上的多级视觉焦点与细节丰富度。 | `PENDING GATE 3` | 需防止学生直接使用 AI 生成贴图导致的“全屏高频噪点失控”。 |
| **sRGB 与 Linear 色彩空间规范**<br>*(Color Space: sRGB vs. Linear/Non-Color)* | `Likely Important` | AI 工具链在输出贴图时经常混淆色彩空间标签，导致粗糙度、法线等物理数据贴图被错误赋予 sRGB 伽马矫正。 | `Limitation Evidence` & `Technical Specification`<br>[[ASWF OpenPBR Spec v1.1.1]](https://academysoftwarefoundation.github.io/OpenPBR/) | 极高：引擎将 Normal/Roughness 识别为 sRGB 会彻底破坏着色计算。 | 极高：ACES 影视色彩管理管线中的致命混淆项。 | `PENDING GATE 3` | 必须建立刚性原则：色彩图进 sRGB/ACEScg，数据图强制 Non-Color/Raw。 |

---

### 3.2 模块二：Texture-based Authoring (基于贴图的资产级材质创作)

| Unit | Baseline Teaching Necessity | AI / Automation Impact (2026) | Evidence Type & Source Link | Game Realtime Relevance | Animation / LookDev Relevance | Gate 3 Status | Caveat / Unresolved |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Painter 工程设置与色彩管理**<br>*(Painter Project Setup & OCIO/ACES)* | `Likely Core` | 现代 Painter 已支持一键模板与预设色彩配置文件（包括 OpenPBR 1.1 默认设置），手工配置被大幅精简。 | `Non-AI Workflow Automation`<br>[[Substance 3D Painter 12.1 Release Notes]](textbook-source-map.md) | 极高：对齐引擎色彩曲线，防止工程从第一步就发生色彩偏差。 | 极高：支持 OCIO 与 ACES 色彩空间，保证与影视合成管线对齐。 | `PENDING GATE 3` | 12.1 已将 OpenPBR 设为默认，教学工程模板应紧跟活体版本。 |
| **图层结构与多通道同步管理**<br>*(Layer Stack & Multi-channel Sync)* | `Likely Core` | 当前生成式 AI 仅输出单层扁平贴图（Flattened Bitmaps），完全不具备非破坏性、多通道联动的图层栈组织。 | `Limitation Evidence` & `Project Inference`<br>[[Meshy Docs — AI Texturing]](https://docs.meshy.ai/texturing) / [[Tripo 80 Level Interview]](https://80.lv/articles/how-tripo-is-tackling-clean-topology-for-its-3d-asset-pipeline/) | 极高：美术主管（Lead Artist）评审资产时要求必须保持图层可修改性。 | 极高：后期根据视效总监意见单通道调整光泽度或污迹的核心结构。 | `PENDING GATE 3` | 图层栈是非破坏性编辑与团队协作的工业基石，AI 短期内无法颠覆。 |
| **遮罩体系与手绘特征细节**<br>*(Mask Hierarchy & Feature Hand-painting)* | `Likely Core` | AI 辅助选择与智能补全（Inpainting）可加速底模遮罩，但关键叙事特征（划痕深浅、文字喷涂、角色特定磨损）仍需手工刻画。 | `Vendor Capability` & `Academic / Demonstrated`<br>[[Node To Talk]](https://superhivemarket.com/products/node-to-talk) / [[Shah 2022 Ch 3-5]](textbook-source-map.md) | 高：主角持握道具、关卡叙事性关键资产的独特视觉特征。 | 极高：特写道具与生物表面具有叙事动机的手工遮罩细节。 | `PENDING GATE 3` | 教学应引导学生将手绘精力从“机械涂抹大面积脏迹”转向“刻画关键特征”。 |
| **智能材质 (Smart Materials) 组织**<br>*(Smart Materials System & Encapsulation)* | `Likely Core` | 智能材质预设生态持续膨胀，AI 可辅助生成智能材质内部的基础图层，但整体结构封装与跨资产复用仍需人工构建。 | `Vendor Capability`<br>[[Substance 3D Painter Smart Materials]](https://helpx.adobe.com/substance-3d-painter/features/smart-materials.html) | 极高：大型游戏项目保持全关卡道具材质风格与制作效率一致的规范工具。 | 极高：影视工作室通用材质资产库（Asset Library）的标准载体。 | `PENDING GATE 3` | 学生需学会将自己制作的复合多层材质打包为 Smart Material 沉淀为资产。 |
| **智能生成器 (Generators) 驱动逻辑**<br>*(Generators Driven by Mesh Maps)* | `Likely Core` | 传统基于网格烘焙图（Curvature/AO/World Space）的生成器高度成熟，参数化调整几乎代替了所有底层磨损绘制。 | `Non-AI Workflow Automation`<br>[[Substance 3D Painter Generators]](https://helpx.adobe.com/substance-3d-painter/features/generators.html) | 极高：批量生产环境中最迅速生成边缘磨损、夹缝积尘的标准操作。 | 高：影视资产底料与中频杂质快速分布的主要手段。 | `PENDING GATE 3` | 操作虽简单，但理解其背后“曲率图驱动白边、AO 图驱动黑边”的逻辑不可动摇。 |
| **材质分层逻辑 (Base $\rightarrow$ Detail)**<br>*(Material Stratification: Substrate to Wear)* | `Likely Core` | AI 贴图生成缺乏对物理世界工艺构造的理解；真实世界资产包含“底材（金属/木材）$\rightarrow$ 漆面/涂层 $\rightarrow$ 氧化锈蚀 $\rightarrow$ 灰尘油渍”。 | `Limitation Evidence`<br>[[Dinur 2026 Ch 5-8]](textbook-source-map.md) / [[Shah 2022 Ch 4]](textbook-source-map.md) | 极高：决定实时光照变化下资产质感是否具备真实的厚度与剥落层次。 | 极高：影视级特写资产实现照片级真实（Photorealism）的灵魂法则。 | `PENDING GATE 3` | 无论使用何种工具，该思维模型是区分业余与专业材质师的核心分水岭。 |
| **风化与磨损物理逻辑 (Weathering)**<br>*(Weathering, Aging & Contact Logic)* | `Likely Core` | AI 生成的磨损通常是空间随机均匀分布的噪波，缺乏基于重力下沉、雨水冲刷、手部频繁接触与物理碰撞的真实动力学规律。 | `Limitation Evidence` & `Academic / Demonstrated`<br>[[Tripo 80 Level Interview]](https://80.lv/articles/how-tripo-is-tackling-clean-topology-for-its-3d-asset-pipeline/) | 高：关卡环境道具与世界观叙事（如废弃年限、使用频率）的逻辑自洽。 | 极高：影视级视效中表达道具历史感与环境互动关系的刚性要求。 | `PENDING GATE 3` | 教学重心需从“怎样画出磨损”升级为“为什么这里会有磨损”。 |
| **贴图导出模板与通道配置**<br>*(Export Presets & Channel Packing)* | `Likely Core` | 传统 DCC 导出预设高度成熟（如 UE Packed、Unity HDRP、glTF），通道打包属于标准自动化输出操作。 | `Non-AI Workflow Automation`<br>[[Substance 3D Painter Export]](https://helpx.adobe.com/substance-3d-painter/export/export-presets.html) | 极高：必须精确匹配引擎通道组合（如 R=AO, G=Roughness, B=Metallic）。 | 高：匹配 RenderMan/Arnold/Karma 的着色网络输入规范。 | `PENDING GATE 3` | 操作虽可自动化，但学生必须深刻理解不同引擎对贴图通道打包的诉求差异。 |

---

### 3.3 模块三：Supporting Pipeline Knowledge (材质支撑管线前置知识)

| Unit | Baseline Teaching Necessity | AI / Automation Impact (2026) | Evidence Type & Source Link | Game Realtime Relevance | Animation / LookDev Relevance | Gate 3 Status | Caveat / Unresolved |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **UV 参数化展开与接缝切分**<br>*(UV Parameterization & Seam Layout)* | `Supporting prerequisite` | 现代 DCC 与 Painter 内置计算几何自动图割（Auto Unwrap）已高度成熟，常规资产可实现一键秒级展开与装箱。 | `Non-AI Workflow Automation`<br>[[Substance 3D Painter Auto Unwrap]](https://helpx.adobe.com/substance-3d-painter/features/auto-unwrap.html) | 极高：UV 拉伸与接缝位置直接影响贴图像素利用率与接缝瑕疵。 | 极高：影视 UDIM 多象限规划与微多边形置换的前提条件。 | `PENDING GATE 3` | 自动化极高，手工切缝学时应大幅压缩，但学生需保留“识别 UV 严重拉伸与接缝死角隐藏”的验收能力。 |
| **接缝与硬边对应原则**<br>*(UV Seams vs. Hard Edges Matching)* | `Supporting prerequisite` | 几何算法已能自动将网格平滑组硬边对应切开为 UV 接缝，避免光照法线插值错误。 | `Non-AI Workflow Automation`<br>[[McDermott PBR Guide Part 2]](textbook-source-map.md) | 极高：游戏法线烘焙产生“黑边/黑线”的最主要元凶，必须严格对齐。 | 中等：离线渲染细分后接缝影响减弱，但贴图接缝处仍有插值风险。 | `PENDING GATE 3` | 这是连接建模与材质的最关键排错知识点，操作可自动，但黑边排错诊断不可丢。 |
| **像素密度规划 (Texel Density)**<br>*(Texel Density Planning & Scaling)* | `Supporting prerequisite` | 现代 UV 工具可一键对齐全部 UV 岛的像素密度，或按统一像素/厘米标准缩放。 | `Non-AI Workflow Automation`<br>[[Shah 2022 Ch 2]](textbook-source-map.md) | 极高：游戏关卡中不同资产若像素密度不均，会导致场景贴图清晰度割裂。 | 高：确保特写资产具备足够分辨率预算，避免近景模糊。 | `PENDING GATE 3` | 规划属于宏观生产预算问题，操作由工具执行，人类把控预算指标。 |
| **高低模映射关系与拓扑准备**<br>*(High-to-Low Poly Mapping & Topology)* | `Supporting prerequisite` | 自动重拓扑与形变包裹算法可用，但复杂资产仍存在投射穿插、边缘错位与极度凌乱拓扑。 | `Academic / Demonstrated` & `Limitation Evidence`<br>[[Tripo 80 Level Interview]](https://80.lv/articles/how-tripo-is-tackling-clean-topology-for-its-3d-asset-pipeline/) | 极高：游戏低模必须控制顶点开销与轮廓剪影。 | 中高：动画角色要求极其严格的运动拓扑流向。 | `PENDING GATE 3` | 课程边界刚性约束：本科材质课不应让学生从零雕高模、手工画拓扑，应大量使用预制工业网格。 |
| **关键贴图烘焙**<br>*(Mesh Maps Baking: Normal/AO/Curvature)* | `Supporting prerequisite` | GPU 光线投射与 By Mesh Name 命名匹配烘焙高度成熟（Painter 12.1 更引入 Paint Skew 与 Auto Rebake），大幅消除传统射线穿插。 | `Non-AI Workflow Automation`<br>[[Substance 3D Painter 12.1 Release Notes]](textbook-source-map.md) / [[Painter Baking Docs]](https://helpx.adobe.com/substance-3d-painter/baking/baking.html) | 极高：驱动 Painter 智能生成器与底层光影映射的命脉。 | 高：离线渲染中亦常利用烘焙曲率/AO 驱动底层着色网络。 | `PENDING GATE 3` | 烘焙操作已极简化，重点应转向“烘焙穿插排错、包裹盒笼子调整与法线偏斜修复”。 |

---

### 3.4 模块四：Procedural / Parametric Materials (程序化与参数化材质创作)

| Unit | Baseline Teaching Necessity | AI / Automation Impact (2026) | Evidence Type & Source Link | Game Realtime Relevance | Animation / LookDev Relevance | Gate 3 Status | Caveat / Unresolved |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **节点着色器架构 (Shader Nodes)**<br>*(Node-based Shader Graph Architecture)* | `Likely Important` | Text-to-Nodes 与 LLM 脚本可生成简单节点拓扑，但在复杂拓扑（如多层三向投影、混合逻辑）中极易出现幻觉死循环。 | `Academic / Demonstrated`<br>[[DD3M, arXiv 2024/2025]](https://arxiv.org/abs/2410.05432) / [[Node To Talk]](https://superhivemarket.com/products/node-to-talk) | 极高：UE 材质编辑器（Material Editor）与自定义 Shader 的共通底层。 | 极高：Blender Cycles / Arnold / Karma 着色器网络的核心搭建方式。 | `PENDING GATE 3` | 机械连线负担被压缩，但阅读、诊断与微调节点数据流向的能力价值剧增。 |
| **纹理坐标系**<br>*(Texture Coordinates: Generated, Object, UV)* | `Likely Important` | AI 工具生成着色器时常机械套用默认 UV，在未展 UV 或复杂非刚体网格上导致严重贴图拉伸变形。 | `Limitation Evidence` & `Technical Specification`<br>[[Blender 5.2/4.5 Manual]](textbook-source-map.md) | 极高：实时世界坐标投射（World Position）、三向贴图（Triplanar）的基础。 | 极高：影视场景中大量环境岩石/地形依赖 Object 空间无缝贴图。 | `PENDING GATE 3` | 区分 Generated、Object、UV 与 Window 坐标系是程序化材质不失真的基本功。 |
| **算法纹理与噪声**<br>*(Procedural Noise & Patterns: Perlin/Voronoi)* | `Likely Important` | 算法噪波高度成熟，AI 可直接建议噪波类型，但细分尺寸、畸变度与粗糙度参数仍需人工精确调配。 | `Vendor Capability`<br>[[Blender Shader Nodes Docs]](textbook-source-map.md) / [[Shah 2022 Ch 7-8]](textbook-source-map.md) | 高：游戏实时材质常利用低开销程序化噪波扰动打破贴图平铺重复感。 | 极高：影视 LookDev 中构建破损、杂色与微表面粗糙度变化的取之不尽源泉。 | `PENDING GATE 3` | 噪波参数调校需结合现实物理尺度，避免失真。 |
| **数学运算与混合遮罩**<br>*(Math Operations & Mix Masks)* | `Likely Important` | AI 模型能写出基础数学节点连接，但在阈值截断（Clamp）、范围重映射与高阶非线性混合上常出现逻辑漏洞。 | `Academic / Demonstrated`<br>[[DD3M, arXiv 2024/2025]](https://arxiv.org/abs/2410.05432) | 极高：实时材质节省贴图采样的核心手段（用算力换带宽）。 | 极高：高阶 LookDev 精确控制分层混合因子（Blend Factor）的数学工具。 | `PENDING GATE 3` | 加减乘除、Smoothstep、Power 等基础数学操作是程序化思维的坚实内核。 |
| **色彩映射与区间重映射**<br>*(ColorRamp & Range Remapping)* | `Likely Important` | AI 可快速提取调色板生成色标，但对极端输出值（如导致反射率超出安全范围的死黑死白）缺乏自发约束。 | `Academic / Demonstrated`<br>[[Blender Shader Nodes Docs]](textbook-source-map.md) | 极高：将单通道灰度噪波重映射为合规 Base Color 与 Roughness 范围。 | 极高：离线渲染中精细调整微表面菲涅尔衰减曲线的关键节点。 | `PENDING GATE 3` | 重点掌握通过 Map Range 或 ColorRamp 约束物理安全区间。 |
| **映射缩放与平铺控制**<br>*(Mapping, Scale & Tiling Control)* | `Likely Important` | 现代工具与 AI 插件可自动生成 Mapping 节点，但实际平铺比例是否匹配真实世界米制单位全靠人工肉眼校准。 | `Vendor Capability`<br>[[Shah 2022 Ch 8]](textbook-source-map.md) | 极高：游戏关卡地面、墙面材质平铺尺寸必须严格符合 1:1 人体工学比例。 | 极高：影视布景材质物理尺度的真实性底线。 | `PENDING GATE 3` | 操作虽简单，但尺度失调是学生作品最常见的“业余破绽”。 |
| **随机化与多变异质感**<br>*(Randomization & Multi-variation)* | `Likely Important` | 可通过 Object Info / Geometry 节点引入随机种子，AI 亦能辅助生成种子逻辑，但整体变异跨度需人眼平衡。 | `Academic / Demonstrated`<br>[[Blender Shader Nodes Docs]](textbook-source-map.md) | 极高：大批量植被、砖块、地砖道具避免视觉复制感（Tile repetition）的核心。 | 高：集群资产与场景散布道具的质感微变异。 | `PENDING GATE 3` | 掌握利用随机 ID 驱动色相与粗糙度偏移的程序化技巧。 |
| **节点组封装与参数暴露**<br>*(Node Group Encapsulation & Interface)* | `Likely Important` | 脚本虽能打包节点，但对外暴露哪些关键控制滑块（Sliders）、参数命名与默认值设定属于人机交互设计范畴。 | `Academic / Demonstrated` & `Project Inference`<br>[[Shah 2022 Ch 10]](textbook-source-map.md) | 极高：制作供关卡美术使用的材质母版（Master Material）的标准规范。 | 极高：影视管线中向照明组交付可调着色器资产的行业标准。 | `PENDING GATE 3` | 重点培养“黑盒封装思维”：隐藏复杂内部网络，只暴露必要艺术控制参数。 |
| **独立程序化纹理与 `.sbsar` 母版生成**<br>*(Standalone Procedural Texture & `.sbsar`)* | `Likely Optional` | 纯自然语言目前极难生成包含复杂原子节点、数学变换的 Substance Designer 图；该领域目前仍为高壁垒专家领域。 | `Limitation Evidence`<br>[[Adobe Substance 3D Designer Docs]](textbook-source-map.md) | 中等：游戏工业技术美术（TA）制作跨项目通用材质母版的利器。 | 中等：影视管线制作可动态调整分辨率的程序化纹理库。 | `PENDING GATE 3` | 维持 `Likely Optional`。本科 8 周不宜重度强求全流程 Designer，聚焦节点通用思维。 |
| **程序化结果烘焙为 PBR 贴图包**<br>*(Baking Procedural to PBR Texture Set)* | `Likely Important` | 将复杂程序化着色网络一键烘焙为标准离线贴图集的技术高度自动化。 | `Non-AI Workflow Automation`<br>[[Blender Manual Baking]](textbook-source-map.md) / [[Shah 2022 Ch 10]](textbook-source-map.md) | 极高：将离线复杂节点网络降级为移动端或实时引擎可运行贴图的必要流程。 | 中等：影视资产在不同 DCC（如 Houdini/Maya/Katana）间流转的标准化手段。 | `PENDING GATE 3` | 重点关注烘焙位深度（32-bit/16-bit 法线与置换，防止出现色阶断层）。 |

---

### 3.5 模块五：Material Acquisition & Conversion (材质采集、图像转换与平铺)

| Unit | Baseline Teaching Necessity | AI / Automation Impact (2026) | Evidence Type & Source Link | Game Realtime Relevance | Animation / LookDev Relevance | Gate 3 Status | Caveat / Unresolved |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **照片/扫描参考转 PBR 材质原理**<br>*(Photometric / Scan Reference to PBR)* | `Likely Important` | 传统光度立体法原理已被部分集成进神经网络 De-lighting 与反射率估算模型中，理论门槛大幅降低。 | `Academic / Demonstrated`<br>[[IntrinsiX, NeurIPS 2025]](https://arxiv.org/abs/2410.22378) / [[Adobe Sampler Image-to-Material]](https://helpx.adobe.com/substance-3d-sampler/filters/image-to-material.html) | 高：快速将现实世界表面纹理转为游戏可用贴图。 | 高：低成本获取真实世界脏迹与微结构参考。 | `PENDING GATE 3` | 需培养学生识别“合规拍摄样本”（避免强直射阴影与反光溢出）的拍摄能力。 |
| **Substance 3D Sampler 工具链工作流**<br>*(Substance 3D Sampler Workflow)* | `Likely Important` | Sampler 深度整合了 AI Powered 与 B2M 滤镜，并引入 Firefly 生成功能（截至 2026-04 标为 Beta），成为连接现实与 AI 的强力桥梁。 | `Vendor Capability`<br>[[Adobe Sampler Generative Features]](https://helpx.adobe.com/substance-3d-sampler/generative-workflows/generative-features.html) | 高：游戏环境材质资产库（如地砖、树皮、沥青）的快速生成通道。 | 高：快速建立质感接近的离线渲染基础材质母版。 | `PENDING GATE 3` | 维持 `Unresolved / Recommended Candidate`。受限于课时与机房授权，是否作为必修待 Stage 3/4 决定。 |
| **Image-to-Material 智能通道提取**<br>*(Image-to-Material AI/B2M Extraction)* | `Likely Important` | AI 模型与 B2M 算法已实现单图一键提取 Normal/Roughness/Height/Ambient Occlusion 通道，生产可用度高。 | `Vendor Capability`<br>[[Adobe Sampler Image to Material Filters]](https://helpx.adobe.com/substance-3d-sampler/filters/image-to-material.html) | 极高：极大地加速了无缝材质的初稿制备流程。 | 高：快速生成高分辨率置换与微表面粗糙度底贴图。 | `PENDING GATE 3` | 必须人工校验：AI 提取的 Roughness 往往对比度失真，Metallic 需手动指定。 |
| **图像无缝平铺处理 (Seamless Tiling)**<br>*(Seamless Tiling & AI Outpainting)* | `Likely Important` | 传统边缘包裹混合与现代 AI 智能扩图（Outpainting）平铺几乎实现 100% 全自动无缝化。 | `Vendor Capability`<br>[[Adobe Sampler Generative Features]](https://helpx.adobe.com/substance-3d-sampler/generative-workflows/generative-features.html) | 极高：建筑与地形等大面积复用材质彻底消除接缝边缘。 | 极高：影视场景延伸与背景资产平铺的刚性需求。 | `PENDING GATE 3` | 自动化极高，传统手工盖印修接缝操作应大幅压缩；重点转为“排查宏观特征斑块重复”。 |
| **真实物理尺寸校准 (Scale Calibration)**<br>*(Real-world Physical Scale Calibration)* | `Likely Important` | AI 模型无法自动获知图像拍摄时的绝对空间比例；尺寸标定完全依赖人工依据参照物（如标尺、手足）精确设定。 | `Academic / Demonstrated` & `Project Inference`<br>[[Adobe Sampler Docs]](https://helpx.adobe.com/substance-3d-sampler/) / [[Shah 2022 Ch 6]](textbook-source-map.md) | 极高：关卡中地砖、布料纹理若物理尺寸失调，直接摧毁空间沉浸感。 | 极高：影视资产必须精确对齐真实物理尺寸，确保置换与景深计算正确。 | `PENDING GATE 3` | 必须作为关键验收标准保留：每张材质贴图必须拥有明确的世界空间尺寸（米/厘米）。 |

---

### 3.6 模块六：LookDev & Multi-environment Validation (视觉开发与跨引擎验证)

| Unit | Baseline Teaching Necessity | AI / Automation Impact (2026) | Evidence Type & Source Link | Game Realtime Relevance | Animation / LookDev Relevance | Gate 3 Status | Caveat / Unresolved |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Blender 材质视口与基础着色验证**<br>*(Blender Viewport & Basic Shading Validation)* | `Likely Important` | 视口渲染引擎（EEVEE-Next 与 Cycles）已实现极速无缝切换，但跨视口光照平衡与材质解析仍需人工目视评定。 | `Vendor Capability`<br>[[Blender 5.2/4.5 Manual]](textbook-source-map.md) | 高：作为通识三维平台，快速检验材质基本通道连接与光影响应。 | 极高：低成本建立影视级 Cycles 离线渲染 LookDev 预览环境。 | `PENDING GATE 3` | 杜绝“单一视口自嗨”，必须养成在真实着色器环境中检验材质的习惯。 |
| **Unreal Engine 实时材质实例组装**<br>*(Unreal Engine Master & Material Instances)* | `Likely Core` | 支持脚本批量生成材质实例，但母版材质架构（Master Material）设计、参数暴露与动态实例组装仍为纯人工工程。 | `Technical Specification`<br>[[Unreal Engine Physically Based Materials]](https://dev.epicgames.com/documentation/en-us/unreal-engine/physically-based-materials-in-unreal-engine) | 核心支柱：游戏工业生产中 99% 的资产均通过材质实例（Material Instance）交付。 | 中等：现代影视虚拟制片（Virtual Production）实时 LED 墙着色核心。 | `PENDING GATE 3` | 必须保留完整的“贴图导入 $\rightarrow$ 材质实例组装 $\rightarrow$ 参数调优”实操流程。 |
| **游戏运行时材质性能与约束 (ORM/BC7)**<br>*(Runtime Performance, BC7 & Texture Packing)* | `Likely Important` | 引擎可自动压缩，但通道混合（Channel Packing）策略与贴图尺寸优化仍需人工根据显存预算（VRAM Budget）规划。 | `Technical Specification`<br>[[Karis 2013]](https://cdn2.unrealengine.com/Resources/files/2013SiggraphPresentationsNotes-26915738.pdf) / [[UE Docs]](https://dev.epicgames.com/documentation/en-us/unreal-engine/) | 核心支柱：直接决定游戏帧率（FPS）、显存占用与 Draw Call 开销。 | 低：影视离线渲染关注精度胜于带宽，通常使用散装 16/32-bit EXR。 | `PENDING GATE 3` | 游戏出口的核心刚性指标，AI 生成的分散散装贴图必须经过打包规范化。 |
| **影视/动画高保真着色差异 (SSS/Coat)**<br>*(Cinematic High-fidelity Shading: SSS, Coat)* | `Likely Optional` | 当前 AI 材质生成几乎全部停留在基础电介质/金属模型，对多层薄膜干涉、次表面散射（SSS）等高阶光学参数无能为力。 | `Technical Specification` & `Limitation Evidence`<br>[[ASWF OpenPBR Spec v1.1.1]](https://academysoftwarefoundation.github.io/OpenPBR/) | 低：实时开销极其昂贵，游戏通常使用简化近似模型。 | 核心支柱：影视角色皮肤、玉石、车漆清漆层等照片级真实感的决定性通道。 | `PENDING GATE 3` | 维持 `Likely Optional`。作为拔高或分流专题，不强加给全部学生。 |
| **跨渲染器着色表现差异对比**<br>*(Cross-renderer Shading Discrepancies)* | `Likely Important` | AI 无法解决跨渲染器（UE vs Cycles vs Marmoset）因 BRDF 微表面实现、微几何遮蔽函数差异导致的视觉异化。 | `Limitation Evidence`<br>[[Akenine-Möller Real-Time Rendering 4th]](textbook-source-map.md) / [[McDermott PBR Guide]](textbook-source-map.md) | 高：确保资产从 DCC 导出后在游戏引擎内不发生质感崩塌。 | 极高：确保资产在离线渲染农场跨平台渲染时的一致性。 | `PENDING GATE 3` | 重点培养“多环境对比排错”思维，理解为什么同一套贴图在不同引擎看起来不同。 |
| **多环境 IBL 与极端光照压力测试**<br>*(Multi-environment IBL & Lighting Stress Testing)* | `Likely Core` | 可通过自动化脚本旋转 HDR 环境贴图，但材质在极端强光/弱光/多色温下的物理合理性裁决完全依赖人眼。 | `Non-AI Workflow Automation` & `Technical Specification`<br>[[Dinur 2026 Ch 12-15]](textbook-source-map.md) / [[McDermott PBR Guide]](textbook-source-map.md) | 极高：保证资产在游戏中经历昼夜交替、洞穴阴影时始终可信不破绽。 | 极高：影视资产 LookDev 标准流程（Chrome Ball / Grey Ball + 至少 3 套不同 HDRI 旋转验证）。 | `PENDING GATE 3` | 核心验收法则：未经至少 3 种极端环境光（晴空直射、多云阴天、室内暖光）测试的材质不是合格资产。 |

---

## 4. Gate 2 补充矩阵：新兴 AI 原生材质技能池分级映射 (13 单元)

根据 [`ai-impact-on-material-workflows.md`](ai-impact-on-material-workflows.md) 第 6 节的研究结论，2026 年涌现出 13 项 AI 原生材质技能候选。本矩阵完成其基线属性规范化与证据类型 Join。

### 4.1 Tier 1：高置信度核心候选 (High-confidence Emerging Skills — 4 项)

| Unit | Baseline Teaching Necessity | AI / Automation Capability & Impact (2026) | Evidence Type & Source Link | Game Realtime Relevance | Animation / LookDev Relevance | Gate 3 Status | Caveat / Unresolved |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **材质语义提示词工程**<br>*(Material Semantic Prompting)* | `New Candidate (Tier 1)` | 现代多模态与纹理生成模型能精准响应专业光学与物理工艺术语（如“Anodized Aluminum”、“Weathered Oak with Lichen”），取代模糊艺术词汇。 | `Academic / Demonstrated` & `Vendor Capability`<br>[[Adobe Sampler Generative Features]](https://helpx.adobe.com/substance-3d-sampler/generative-workflows/generative-features.html) / [[Meshy AI Texturing]](https://docs.meshy.ai/texturing) | 高：快速生成特定风格与时代背景的概念贴图底料。 | 高：快速探索不同材质方案并形成一致性情绪板。 | `PENDING GATE 3` | 严禁滥用模糊空泛词汇（如“8k photorealistic”），必须精准使用物理与工艺实体词。 |
| **参考图像条件约束与风格锚定**<br>*(Reference Conditioning & ControlNet)* | `New Candidate (Tier 1)` | 通过 ControlNet（深度/法线）、IP-Adapter 与参考图引导生成，极大提升了材质生成的空间几何对应与风格可控性。 | `Academic / Demonstrated`<br>[[Dinur 2026 Ch 19]](textbook-source-map.md) / [[IntrinsiX, NeurIPS 2025]](https://arxiv.org/abs/2410.22378) | 高：确保生成纹理精确贴合模型既有轮廓与结构特征。 | 极高：确保概念设计稿或现场实拍参考的色彩质感被精准继承。 | `PENDING GATE 3` | 教师与学生需掌握使用真实参考图作为强约束引导生成的核心方法。 |
| **跨通道 PBR 物理诊断**<br>*(Cross-channel PBR Physical Diagnosis)* | `New Candidate (Tier 1)` | AI 工具往往各自生成单通道或缺乏物理耦合，极易产生“法线有深坑但粗糙度无变化”、“金属表面出现高漫反射”等跨通道精神分裂现象。 | `Limitation Evidence` & `Project Inference`<br>[[Tripo 80 Level Interview]](https://80.lv/articles/how-tripo-is-tackling-clean-topology-for-its-3d-asset-pipeline/) / [[McDermott PBR Guide]](textbook-source-map.md) | 极高：跨通道穿帮在动态光照下会产生剧烈的着色假象。 | 极高：离线多层渲染中导致高光与漫反射严重脱节。 | `PENDING GATE 3` | **AI 时代最具核心价值的纯人类新技能**：通道间自洽性审计。 |
| **人机协同分层迭代与局部微调**<br>*(Human-in-the-Loop Layer Structuring)* | `New Candidate (Tier 1)` | 将 AI 生成的扁平贴图重新解构导入 Substance 3D Painter，通过遮罩、图层混合模式与手绘笔刷进行非破坏性受控整合。 | `Academic / Demonstrated` & `Project Inference`<br>[[Shah 2022 Ch 4]](textbook-source-map.md) / [[Meshy Docs]](https://docs.meshy.ai/texturing) | 极高：游戏团队协作必须保留图层栈以应对策划与美术总监的反复修改。 | 极高：影视资产迭代中精细微调特定区域光泽度的绝对保障。 | `PENDING GATE 3` | 克服 AI 贴图“黑盒不可编辑性”的核心工业工作流。 |

---

### 4.2 Tier 2：成熟中/推荐候选 (Candidate Skills — 4 项)

| Unit | Baseline Teaching Necessity | AI / Automation Capability & Impact (2026) | Evidence Type & Source Link | Game Realtime Relevance | Animation / LookDev Relevance | Gate 3 Status | Caveat / Unresolved |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **光照残留剥离与去光照修正**<br>*(De-lighting Inspection & Correction)* | `New Candidate (Tier 2)` | 自动化 De-lighting 算法常残留方向性漫射阴影或环境色温偏色，需人工利用高反差保留、曲线与通道画笔进行二次剥离修正。 | `Academic / Demonstrated`<br>[[IntrinsiX, NeurIPS 2025]](https://arxiv.org/abs/2410.22378) / [[LumiTex, ICLR 2026]](https://arxiv.org/abs/2501.03875) | 极高：残留阴影的贴图在游戏动态光照下产生“二次重影”致命穿帮。 | 极高：破坏影视级打光自由度，导致资产在不同光照角度下显假。 | `PENDING GATE 3` | 需掌握使用滤镜或手绘修复 Albedo 去光照瑕疵的实战方法。 |
| **AI 材质变体策展与筛选**<br>*(AI Material Variation Curation)* | `New Candidate (Tier 2)` | AI 能在数分钟内生成数十种不同风化、色彩与纹理走向的材质变体，材质师角色部分演化为高效的审美方案策展人与过滤器。 | `Vendor Capability`<br>[[Adobe Sampler Generative Features]](https://helpx.adobe.com/substance-3d-sampler/generative-workflows/generative-features.html) / [[Meshy AI Texturing]](https://docs.meshy.ai/texturing) | 高：快速为关卡不同区域道具配置多样化变体（Avoid repetition）。 | 高：概念阶段向导演与艺术指导提供丰富的质感选型提案。 | `PENDING GATE 3` | 策展能力建立在深厚的艺术审美与物理规律理解之上，非盲目随机抽奖。 |
| **版本控制与随机种子管理**<br>*(Seed & Workflow Version Reproducibility)* | `New Candidate (Tier 2)` | AI 生成具备随机性；工业资产生产要求 100% 可复现性，必须系统记录 Prompt、Seed、采样步数、模型版本与工作流节点文件。 | `Vendor Capability` & `Project Inference`<br>[[Adobe Sampler Docs]](https://helpx.adobe.com/substance-3d-sampler/) | 极高：版本迭代时若无法复现原材质参数，将导致整套资产资产断代。 | 极高：大型视效项目管线（VFX Pipeline）严苛的资产版本追踪（Asset Tracking）。 | `PENDING GATE 3` | 培养工程化素养，严禁“无法复现的偶得一次性贴图”进入工程。 |
| **AI 纹理接缝与伪影修复**<br>*(AI Artifact & Seam Inpainting)* | `New Candidate (Tier 2)` | 生成模型在 UV 边界或复杂几何凹陷处常生成模糊斑块、伪拉伸或缝隙伪影，需借助智能局部修补（Inpainting）与克隆画笔修复。 | `Academic / Demonstrated`<br>[[Tripo 80 Level Interview]](https://80.lv/articles/how-tripo-is-tackling-clean-topology-for-its-3d-asset-pipeline/) | 极高：UV 接缝处的伪影在引擎视口中格外扎眼，必须彻底消除。 | 极高：特写镜头下伪影直接导致镜头报废。 | `PENDING GATE 3` | 结合 Painter 的无缝投影工具（Projection）与智能修补高效清障。 |

---

### 4.3 Tier 3：实验性/前沿观察池 (Experimental / Watchlist — 5 项)

| Unit | Baseline Teaching Necessity | AI / Automation Capability & Impact (2026) | Evidence Type & Source Link | Game Realtime Relevance | Animation / LookDev Relevance | Gate 3 Status | Caveat / Unresolved |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **材质母版提示词驱动调参**<br>*(Prompt-to-Parameter Control)* | `New Candidate (Tier 3)` | 探索通过 LLM 直接解析自然语言指令调节复杂着色器内部参数（如“让锈斑扩散 30% 并增加粗糙度”），目前多为原型演示。 | `Vendor Capability / Demonstrated`<br>[[Node To Talk]](https://superhivemarket.com/products/node-to-talk) | 中等：未来可能成为实时关卡着色器参数快速调控的辅助工具。 | 中等：影视复杂着色网络快速批量调参原型。 | `PENDING GATE 3` | 依赖专用插件或 API，尚不属于工业标准化工作流，列入视野观察。 |
| **资产血统与商用合规判断**<br>*(Asset Provenance & Licensing Judgment)* | `New Candidate (Tier 3)` | 评估生成式 AI 材质训练集来源、版权归属（如 Firefly 商业安全承诺 vs 开源模型不可控版权）及知识产权合规性。 | `Vendor Capability` & `Project Inference`<br>[[Adobe Sampler Generative Features]](https://helpx.adobe.com/substance-3d-sampler/generative-workflows/generative-features.html) | 高：商业游戏发布面临严峻的第三方版权与合规审查风险。 | 极高：好莱坞/主流流媒体对生成式内容版权有极其严苛的法务限制。 | `PENDING GATE 3` | 属于行业法律与伦理通识，不列入贴图实操硬技能考核。 |
| **智能体节点图编排**<br>*(Agentic Graph Orchestration)* | `New Candidate (Tier 3)` | 探索由多智能体（Agent）协作进行着色网络分析、连线排错与资产转换（如 Blender 到 UE 自动转译），前沿学术与工具活跃。 | `Academic / Demonstrated`<br>[[DD3M, arXiv 2024/2025]](https://arxiv.org/abs/2410.05432) / [[Node To Talk]](https://superhivemarket.com/products/node-to-talk) | 中等：未来技术美术自动化流水线的前沿方向。 | 中等：大型视效管线自动化批处理。 | `PENDING GATE 3` | 超出本科基础课程范围，作为技术前沿讲座或教师参考。 |
| **跨平台物理材质标准化映射**<br>*(Standardized MaterialX/OpenPBR Translation)* | `New Candidate (Tier 3)` | 推动材质超越特定软件私有格式，基于 OpenPBR 1.1 / MaterialX 实现游戏引擎与影视渲染器之间的无损互通与 AI 自动转译。 | `Technical Specification`<br>[[ASWF OpenPBR Spec v1.1.1]](https://academysoftwarefoundation.github.io/OpenPBR/) | 高：打通跨引擎（UE/Unity/自定义引擎）通用材质描述。 | 极高：现代视效工作室跨 DCC（Houdini/Maya/Unreal）资产共享的通用基准。 | `PENDING GATE 3` | Painter 12.1 已原生支持 OpenPBR 1.1，是极有潜力的标准化方向，保持紧密跟踪。 |
| **视觉特征约束规范制定**<br>*(Visual Constraint Specification)* | `New Candidate (Tier 3)` | 为 AI 生产管线制定严密的机器可读风格规范（如饱和度区间、磨损上限、法线深度范围），约束生成模型输出一致性。 | `Academic / Demonstrated` & `Project Inference`<br>[[Dinur 2026 Ch 19]](textbook-source-map.md) | 高：大型项目利用 AI 批量辅助生产时的质检工业准则。 | 高：影视资产外包质检自动化规范。 | `PENDING GATE 3` | 属于高阶生产管理与技术美术范畴，本科阶段以人眼质检为主。 |

---

## 5. 双出口应用分化特征总结 (Game Realtime vs. Animation / LookDev)

通过 Gate 2 的逐项 Join，双应用出口对材质能力的工业诉求呈现出清晰的结构性分化：

```
┌────────────────────────────────────────────────────────────────────────────┐
│                    两大下游应用出口的工业诉求与壁垒分化                    │
├──────────────────────┬─────────────────────────────────────────────────────┤
│ 维度                 │ 实时游戏 (Game Realtime)                            │
├──────────────────────┼─────────────────────────────────────────────────────┤
│ **核心瓶颈**         │ 运行帧率（FPS）、GPU 显存带宽、Draw Call 开销       │
│ **着色模型**         │ 简化微表面模型（GGX/Smith）、电介质 4% 基础反射率   │
│ **贴图格式**         │ 强制通道打包（ORM: AO+Roughness+Metallic）、BC7 压缩│
│ **材质架构**         │ 材质母版（Master Material）与高度参数化材质实例     │
│ **光照鲁棒性**       │ 必须经受动态昼夜交替、强局部点光源与各种后处理穿帮考验│
│ **AI 落地最大障碍**  │ AI 散装贴图格式不符、通道未打包、法线轴向混淆       │
├──────────────────────┼─────────────────────────────────────────────────────┤
│ 维度                 │ 影视动画 (Animation / LookDev)                      │
├──────────────────────┼─────────────────────────────────────────────────────┤
│ **核心瓶颈**         │ 镜头特写真实感、多跳物理全局光照（GI）、色彩空间一致│
│ **着色模型**         │ 高阶多层模型（OpenPBR: SSS、Coat、Thin Film、置换） │
│ **贴图格式**         │ 独立高位宽贴图（16/32-bit EXR/TIFF）、UDIM 多象限   │
│ **材质架构**         │ 节点图着色网络（Cycles/Arnold/Karma/RenderMan）     │
│ **光照鲁棒性**       │ 标准化 LookDev 流程（标准色球灰球、多套极端 HDRI）  │
│ **AI 落地最大障碍**  │ AI 无法端到端生成高保真多层散射（SSS/Coat）参数     │
└──────────────────────┴─────────────────────────────────────────────────────┘
```

---

## 6. 未决议题与证据缺口清单 (Genuinely Unresolved & Caveats)

在 Gate 1 与 Gate 2 完成后，登记以下**真实存在且直接影响后续 Gate 3 决策**的未决问题：

1. **Substance 3D Sampler 必修深度未决 (UNRES-S2-01)**：
   - *证据现状*：Sampler 提供了成熟的 AI/B2M 图像转材质工作流，且整合了 Firefly 生成特性（2026-04 官方标为 Beta）。
   - *教学矛盾*：在 8 周有限课时与机房授权成本约束下，将其设为“必修实操模块”还是“快速体验与拓展推荐”，需在 Gate 3 权衡。
2. **Substance Designer 教学深度未决 (UNRES-S2-02)**：
   - *证据现状*：AI 极难生成工业级复杂 `.sbsar` 图；Blender Shader Nodes 零门槛且能覆盖 90% 的程序化核心思维。
   - *教学矛盾*：是否在本科 8 周内完全用 Blender 节点替代 Designer 的底层操作，仅将 Designer 作为概念展示？
3. **AI 生成多通道贴图的量化验收门槛未决 (UNRES-S2-03)**：
   - *证据现状*：AI 去光照（De-lighting）残留与金属度灰度噪点是普遍存在的 Limitation Evidence。
   - *教学矛盾*：如何为学生制定简洁、可量化操作的 PBR 质检法则（例如“反射率必须处于什么区间”、“金属度非 0 即 1 的容差范围”）？
4. **Game 与 LookDev 期末大作业出口的分流形式未决 (UNRES-S2-04)**：
   - *教学矛盾*：期末考核是要求所有学生必须同时提交“UE 材质实例运行包”与“Blender/Cycles LookDev 离线渲染图”，还是允许学生二选一分流专精？

---
*本矩阵由 Antigravity 自动化流水线生成并核查，作为 Stage 2 阶段 Gate 1/2 的审阅基线。*
