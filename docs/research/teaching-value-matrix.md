# 《三维数字材质制作》教学价值矩阵 (Teaching Value Matrix)

> **研究阶段**：Stage 2 — AI 后材质能力保留、压缩与重构 (Issue #3)  
> **当前进度**：**Gate 1 (Normalize the Baseline) & Gate 2 (AI Impact Join - Evidence Scope Tightened) COMPLETED**  
> **审阅锚点**：基于 Phase 1 基线 [`curriculum-coverage-matrix.md`](curriculum-coverage-matrix.md)、教材定稿图谱 [`textbook-source-map.md`](textbook-source-map.md)、动态台账 [`course-design-ledger.md`](course-design-ledger.md) 与 AI 影响深度报告 [`ai-impact-on-material-workflows.md`](ai-impact-on-material-workflows.md) 构建，并经 Browser Review 实施严密证据范围收敛。  
> **核心原则与纪律**：
> 1. **操作替代 ≠ 知识替代**：工具层面的手工操作自动化，绝不等于背后支撑知识与物理概念的贬值；相反，操作越自动化，对“诊断、校验与控制”心智模型的要求越高。
> 2. **证据严格定级**：严格区分 Vendor Capability、Academic / Demonstrated、Technical Specification / Platform Documentation、Production / Deployment、Limitation Evidence、Non-AI Workflow Automation 与 Project Inference，严禁把厂商宣传、产品文档或演示流直接等同于成熟生产落地（Production-Ready）。
> 3. **Gate 纪律严格执行**：本阶段仅完成 **Gate 1 基线规范化** 与 **Gate 2 AI 证据逐项 Join（证据范围收缩版）**。所有教学决策字段（`Teaching Action`、`What to Teach Instead / Retain`、价值定级等）统一保持 `PENDING GATE 3`，不得擅自做出提前决策。

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
- **AI / Automation Impact (AI 与自动化影响概述)**：截至 2026 年该单元受到的技术冲击、自动化现状或 AI 赋能边界（限定于实际已审计的工作流与明确证据）。
- **Evidence Type & Source Link (证据类型与一手引证)**：
  - `Vendor Capability`：厂商明确提供的产品功能/Beta 特性；
  - `Academic / Demonstrated`：学术顶会/论文原型或演示流；
  - `Technical Specification / Platform Documentation`：平台/标准组织技术规范（说明结构要求，非生产落地证明）；
  - `Production / Deployment`：真实商业项目/工作室管线落地案例（若无独立实证则明确缺省）；
  - `Limitation Evidence`：实测或行业指出的缺陷与失效点；
  - `Non-AI Workflow Automation`：传统确定性计算几何或光线追踪算法自动化；
  - `Project Inference`：基于实证形成的课程教学推断或行业上下文示例。
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
| **现实材质观察与参考分析**<br>*(Material Observation & Reference Analysis)* | `Likely Core` | 多模态模型可提供材质语义标签、色彩提取与形态描述，但真实物理微观风化、触感质地与时间沉淀痕迹的深度感知仍需人工观察。 | `Academic / Demonstrated`<br>[[Dinur 2026 Ch 1-4]](textbook-source-map.md) | 高：关卡光照下资产的第一眼可信度与叙事感（Project Inference 上下文示例）。 | 极高：特写镜头下避免 CG“塑料感”（Project Inference 上下文示例）。 | `PENDING GATE 3` | AI 可快速搜集情绪板，但艺术指导对微观质感的鉴赏力无法外包。 |
| **PBR 物理可信性与能量守恒**<br>*(PBR Physical Plausibility & Energy Conservation)* | `Likely Core` | 当前被引用的生成式模型缺乏内嵌的严格辐射度反射方程主动验证求解，生成贴图仍频繁出现能量不守恒、漫反射反弹过亮等问题。 | `Limitation Evidence` & `Technical Specification`<br>[[Karis 2013]](https://cdn2.unrealengine.com/Resources/files/2013SiggraphPresentationsNotes-26915738.pdf) / [[McDermott PBR Guide]](textbook-source-map.md) | 极高：光照环境变化（如室内外过渡）时防止材质出现非自然自发光或突兀变黑。 | 极高：离线多跳全局光照（GI）计算中防止噪点发散。 | `PENDING GATE 3` | 当前被引用的 AI 工具链仍显示出物理能量校验的局限，必须依赖理论验收。 |
| **Base Color 反射率与安全色阶**<br>*(Base Color Reflectance & Safe Values)* | `Likely Core` | 神经网络 De-lighting（去光照）模型可辅助剥离光照，但实测与学术报告显示其常残留环境漫射暗斑、死黑（<30 sRGB）或死白（>240 sRGB）。 | `Academic / Demonstrated`<br>[[IntrinsiX, NeurIPS 2025]](https://arxiv.org/abs/2410.22378) / [[LumiTex, ICLR 2026]](https://arxiv.org/abs/2501.03875) | 极高：虚幻引擎官方文档明确要求的 Albedo 物理反射率合规性范围。 | 极高：影响离线次表面与漫射着色积分的准确性。 | `PENDING GATE 3` | 需重点训练“肉眼+直方图”识别去光照瑕疵与色偏。 |
| **Roughness 微表面粗糙度模型**<br>*(Roughness & Microfacet Theory)* | `Likely Core` | 单目深度与纹理模型可预测粗糙度图，但当前被审计工作流生成的粗糙度往往对比度不足、高频磨损细节平坦，或呈现全图均匀高光。 | `Academic / Demonstrated`<br>[[Material Anything, CVPR 2025]](https://arxiv.org/abs/2411.15138) | 极高：直接决定视口高光倒影分布、粗糙度衰减与屏幕空间反射。 | 极高：决定 GGX/OpenPBR 镜面微表面分布与各向异性基础。 | `PENDING GATE 3` | 单目估算在复杂材质的“干/湿”、“光滑/磨损”微观接触过渡上仍显示出局限。 |
| **Metallic 金属度二值准则**<br>*(Metallic Classification & Boundary Rules)* | `Likely Core` | 纯材质表面通常接近 0 或 1；中间值主要用于 material mixtures（如表面覆尘、轻微泥渍）、corrosion（氧化锈蚀过渡）或抗锯齿过滤像素，不应用于表达物理不存在的“半金属电介质”。生成模型在金属边界常预测出非物理过渡噪点。 | `Technical Specification` & `Limitation Evidence`<br>[[Unreal Engine Physically Based Materials]](https://dev.epicgames.com/documentation/en-us/unreal-engine/physically-based-materials-in-unreal-engine) | 极高：非物理中间灰度在实时光照下可能导致边缘发黑、假高光或着色错误。 | 极高：OpenPBR 规范要求严格分离 Dielectric 与 Conductor 菲涅尔。 | `PENDING GATE 3` | 需培养排查伪过渡灰度的能力，同时理解合法混合物/锈蚀过渡允许中间值。 |
| **Normal 切线空间法线原理**<br>*(Tangent Space Normal Principles)* | `Likely Core` | 2D 扩散模型从图像估算法线时无法直接解析 3D 网格切线空间基底，在跨 UV 接缝处已观测到法线方向失真与凹凸反转等局限。 | `Academic / Demonstrated` & `Limitation Evidence`<br>[[MatLat, CVPR 2026]](https://github.com/matlat-pbr/matlat) / [[Tripo 80 Level Interview]](https://80.lv/articles/how-tripo-is-tackling-clean-topology-for-its-3d-asset-pipeline/) | 极高：实时光照依赖切线法线与顶点法线点积，方向错误直接导致阴影颠倒。 | 极高：影视级多边形平滑渲染不可或缺的微起伏表达。 | `PENDING GATE 3` | DirectX 与 OpenGL 绿通道（Y+/Y-）翻转仍是被审计 AI 输出常见故障点。 |
| **Height / Displacement 几何置换**<br>*(Height & Displacement Mapping)* | `Likely Important` | 深度估算与视差图生成工具成熟可用，但多视角生成时精确绝对几何位移标定仍显示局限，需人工调节位移缩放以防网格穿刺。 | `Vendor Capability`<br>[[Adobe Sampler Generative Features]](https://helpx.adobe.com/substance-3d-sampler/generative-workflows/generative-features.html) | 中高：虚幻引擎 Nanite 网格置换、视差贴图（POM）的核心输入。 | 极高：离线渲染细分微多边形置换（Microdisplacement）的基石。 | `PENDING GATE 3` | 置换高度的绝对世界尺度（米制缩放）仍需人工匹配。 |
| **Ambient Occlusion 环境遮挡作用**<br>*(Ambient Occlusion Role & Limits)* | `Likely Core` | 传统光线投射烘焙与算法自动合成微缝隙闭塞成熟，但生成的 AO 贴图常被误乘入 Base Color。 | `Non-AI Workflow Automation` & `Technical Specification`<br>[[McDermott PBR Guide]](textbook-source-map.md) | 极高：实时引擎漫反射间接光阴影模拟，通常打包进 ORM 的 Red 通道。 | 中等：离线光线追踪依靠精确多反弹 GI，AO 主要用于风格化或烘焙缓存。 | `PENDING GATE 3` | 强化认知：AO 仅用于调制间接光漫反射，严禁直接乘在固有色贴图上。 |
| **表面细节尺度与频率认知**<br>*(Detail Scales: Macro, Medium, Micro)* | `Likely Important` | 生成模型擅长填充中高频杂波，但通常缺乏针对三维资产体量的大（Macro）、中（Medium）、小（Micro）三级构图逻辑。 | `Academic / Demonstrated`<br>[[Dinur 2026 Ch 3]](textbook-source-map.md) | 高：关卡远景、中景与近距离持握视角下的视觉层级清晰度。 | 极高：视效资产在大银幕上的多级视觉焦点与细节丰富度。 | `PENDING GATE 3` | 需防止直接套用生成贴图导致的“全屏高频噪点失控”。 |
| **sRGB 与 Linear 色彩空间规范**<br>*(Color Space: sRGB vs. Linear/Non-Color)* | `Likely Important` | 工具链在导出或处理贴图时经常混淆色彩空间标签，导致粗糙度、法线等物理数据贴图被错误赋予 sRGB 伽马矫正。 | `Limitation Evidence` & `Technical Specification`<br>[[ASWF OpenPBR Spec v1.1.1]](https://academysoftwarefoundation.github.io/OpenPBR/) | 极高：引擎将 Normal/Roughness 识别为 sRGB 会彻底破坏着色计算。 | 极高：ACES 影视色彩管理管线中的致命混淆项。 | `PENDING GATE 3` | 必须建立刚性原则：色彩图进 sRGB/ACEScg，数据图强制 Non-Color/Raw。 |

---

### 3.2 模块二：Texture-based Authoring (基于贴图的资产级材质创作)

| Unit | Baseline Teaching Necessity | AI / Automation Impact (2026) | Evidence Type & Source Link | Game Realtime Relevance | Animation / LookDev Relevance | Gate 3 Status | Caveat / Unresolved |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Painter 工程设置与色彩管理**<br>*(Painter Project Setup & OCIO/ACES)* | `Likely Core` | 现代 Painter 已支持一键模板与预设色彩配置文件（包括 OpenPBR 1.1 默认设置），手工配置被大幅精简。 | `Non-AI Workflow Automation`<br>[[Substance 3D Painter 12.1 Release Notes]](textbook-source-map.md) | 极高：对齐引擎色彩曲线，防止工程从第一步就发生色彩偏差。 | 极高：支持 OCIO 与 ACES 色彩空间，保证与影视合成管线对齐。 | `PENDING GATE 3` | 12.1 已将 OpenPBR 设为默认，教学工程模板应紧跟活体版本。 |
| **图层结构与多通道同步管理**<br>*(Layer Stack & Multi-channel Sync)* | `Likely Core` | 当前被引用的 Meshy 等 AI texturing workflow 输出标准 PBR bitmap maps；这些 cited workflows 未提供 Painter-style editable layer stack。 | `Limitation Evidence` & `Project Inference`<br>[[Meshy Docs — AI Texturing]](https://docs.meshy.ai/texturing) / [[Tripo 80 Level Interview]](https://80.lv/articles/how-tripo-is-tackling-clean-topology-for-its-3d-asset-pipeline/) | 极高：在团队资产制作与多轮反馈中，保持图层可修改性是常见的工程诉求（Project Inference）。 | 极高：影视资产迭代中支持单通道微调（如根据总监意见调整光泽度或污渍）。 | `PENDING GATE 3` | 非破坏性图层栈仍是支持多轮迭代调整的成熟手段，被审计 AI 工具未提供该结构。 |
| **遮罩体系与手绘特征细节**<br>*(Mask Hierarchy & Feature Hand-painting)* | `Likely Core` | AI 辅助选择与智能补全（Inpainting）可加速底模遮罩，但特定叙事特征（关键划痕、文字标识、特定角色磨损）仍需人工绘制或指定。 | `Vendor Capability` & `Academic / Demonstrated`<br>[[Node To Talk]](https://superhivemarket.com/products/node-to-talk) / [[Shah 2022 Ch 3-5]](textbook-source-map.md) | 高：主角持握道具、关卡关键资产的独特视觉特征。 | 极高：特写道具与生物表面具有叙事动机的手工遮罩细节。 | `PENDING GATE 3` | 引导手绘精力从“大面积机械涂抹”转向“关键特征刻画与控制”。 |
| **智能材质 (Smart Materials) 组织**<br>*(Smart Materials System & Encapsulation)* | `Likely Core` | 智能材质预设库持续演进，AI 可辅助生成智能材质内部的基础图层底料，但整体结构封装与跨资产复用规范仍需人工构建。 | `Vendor Capability`<br>[[Substance 3D Painter Smart Materials]](https://helpx.adobe.com/substance-3d-painter/features/smart-materials.html) | 极高：游戏项目中保持道具材质风格与制作效率一致的常见复用工具。 | 极高：工作室通用材质资产库（Asset Library）的常用载体。 | `PENDING GATE 3` | 掌握将复合多层材质打包为 Smart Material 沉淀为资产库的结构化组织能力。 |
| **智能生成器 (Generators) 驱动逻辑**<br>*(Generators Driven by Mesh Maps)* | `Likely Core` | 传统基于网格烘焙图（Curvature/AO/World Space）的生成器高度成熟，参数化调整已大幅接管底层磨损分布。 | `Non-AI Workflow Automation`<br>[[Substance 3D Painter Generators]](https://helpx.adobe.com/substance-3d-painter/features/generators.html) | 极高：快速生成边缘磨损、夹缝积尘的标准操作。 | 高：影视资产底料与中频杂质快速分布的主要手段。 | `PENDING GATE 3` | 操作虽简单，但理解其背后“曲率图驱动白边、AO 图驱动黑边”的驱动逻辑不可动摇。 |
| **材质分层逻辑 (Base $\rightarrow$ Detail)**<br>*(Material Stratification: Substrate to Wear)* | `Likely Core` | 被审计的 AI 贴图生成工作流主要输出最终合成贴图，未显式体现真实物理工艺构造（底材 $\rightarrow$ 漆面 $\rightarrow$ 氧化 $\rightarrow$ 灰尘油渍）。 | `Limitation Evidence`<br>[[Dinur 2026 Ch 5-8]](textbook-source-map.md) / [[Shah 2022 Ch 4]](textbook-source-map.md) | 极高：实时光照变化下资产质感是否具备真实的物理厚度与剥落层级。 | 极高：特写资产实现照片级真实（Photorealism）的结构法则。 | `PENDING GATE 3` | 分层思维模型是资产级材质创作的底层逻辑，不随工具形态改变而贬值。 |
| **风化与磨损物理逻辑 (Weathering)**<br>*(Weathering, Aging & Contact Logic)* | `Likely Core` | 生成模型预测的磨损常呈现随机噪波分布，往往缺乏重力下沉、雨水冲刷流向与物理碰撞接触的动力学自洽性。 | `Limitation Evidence` & `Academic / Demonstrated`<br>[[Tripo 80 Level Interview]](https://80.lv/articles/how-tripo-is-tackling-clean-topology-for-its-3d-asset-pipeline/) | 高：关卡环境道具与世界观叙事（使用频率、暴露年限）的合理性。 | 极高：影视级视效中表达道具历史感与环境互动的合理性。 | `PENDING GATE 3` | 教学重心需从“怎样画出磨损”升级为“为什么这里会有磨损的逻辑推演”。 |
| **贴图导出模板与通道配置**<br>*(Export Presets & Channel Packing)* | `Likely Core` | 传统 DCC 导出预设高度成熟（如 UE Packed、Unity HDRP、glTF），通道打包属于标准自动化输出操作。 | `Non-AI Workflow Automation`<br>[[Substance 3D Painter Export]](https://helpx.adobe.com/substance-3d-painter/export/export-presets.html) | 极高：匹配引擎通道组合（如 R=AO, G=Roughness, B=Metallic）。 | 高：匹配 RenderMan/Arnold/Karma 的着色网络输入规范。 | `PENDING GATE 3` | 操作虽可自动化，但学生必须理解不同引擎对贴图通道打包的诉求差异。 |

---

### 3.3 模块三：Supporting Pipeline Knowledge (材质支撑管线前置知识)

| Unit | Baseline Teaching Necessity | AI / Automation Impact (2026) | Evidence Type & Source Link | Game Realtime Relevance | Animation / LookDev Relevance | Gate 3 Status | Caveat / Unresolved |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **UV 参数化展开与接缝切分**<br>*(UV Parameterization & Seam Layout)* | `Supporting prerequisite` | 现代 DCC 与 Painter 内置计算几何自动图割（Auto Unwrap）已高度成熟，常规资产可实现一键展开与装箱。 | `Non-AI Workflow Automation`<br>[[Substance 3D Painter Auto Unwrap]](https://helpx.adobe.com/substance-3d-painter/features/auto-unwrap.html) | 极高：UV 拉伸与接缝位置直接影响贴图像素利用率与接缝瑕疵。 | 极高：影视 UDIM 多象限规划与微多边形置换的前提条件。 | `PENDING GATE 3` | 传统手工切缝学时应予压缩，但学生需保留“识别 UV 严重拉伸与接缝隐藏”的验收能力。 |
| **接缝与硬边对应原则**<br>*(UV Seams vs. Hard Edges Matching)* | `Supporting prerequisite` | 几何算法已能自动将网格平滑组硬边对应切开为 UV 接缝，避免光照法线插值错误。 | `Non-AI Workflow Automation`<br>[[McDermott PBR Guide Part 2]](textbook-source-map.md) | 极高：游戏法线烘焙产生“黑边/黑线”的最主要元凶，硬边处 UV 必须切开。 | 中等：离线渲染细分后接缝影响减弱，但贴图接缝处仍有插值风险。 | `PENDING GATE 3` | 连接建模与材质的排错知识点，操作可自动，但黑边排错诊断不可丢。 |
| **像素密度规划 (Texel Density)**<br>*(Texel Density Planning & Scaling)* | `Supporting prerequisite` | 现代 UV 工具可一键对齐全部 UV 岛的像素密度，或按统一像素/厘米标准缩放。 | `Non-AI Workflow Automation`<br>[[Shah 2022 Ch 2]](textbook-source-map.md) | 极高：场景中不同资产若像素密度不均，会导致贴图清晰度割裂。 | 高：确保特写资产具备足够分辨率预算，避免近景模糊。 | `PENDING GATE 3` | 规划属于宏观生产预算问题，操作由工具执行，人类把控预算指标。 |
| **高低模映射关系与拓扑准备**<br>*(High-to-Low Poly Mapping & Topology)* | `Supporting prerequisite` | 自动重拓扑与形变包裹算法可用，但复杂资产仍存在投射穿插、边缘错位与极度凌乱拓扑。 | `Academic / Demonstrated` & `Limitation Evidence`<br>[[Tripo 80 Level Interview]](https://80.lv/articles/how-tripo-is-tackling-clean-topology-for-its-3d-asset-pipeline/) | 极高：游戏低模必须控制顶点开销与轮廓剪影。 | 中高：动画角色要求极其严格的运动拓扑流向。 | `PENDING GATE 3` | 课程边界刚性约束：本科材质课不应让学生从零雕高模、手工画拓扑，应大量使用预制工业网格。 |
| **关键贴图烘焙**<br>*(Mesh Maps Baking: Normal/AO/Curvature)* | `Supporting prerequisite` | GPU 光线投射与 By Mesh Name 命名匹配烘焙高度成熟（Painter 12.1 引入 Paint Skew 与 Auto Rebake），大幅消除传统射线穿插。 | `Non-AI Workflow Automation`<br>[[Substance 3D Painter 12.1 Release Notes]](textbook-source-map.md) / [[Painter Baking Docs]](https://helpx.adobe.com/substance-3d-painter/baking/baking.html) | 极高：驱动 Painter 智能生成器与底层光影映射的基础。 | 高：离线渲染中亦常利用烘焙曲率/AO 驱动底层着色网络。 | `PENDING GATE 3` | 烘焙操作已极简化，重点转向“烘焙穿插排错、包裹盒笼子调整与法线偏斜修复”。 |

---

### 3.4 模块四：Procedural / Parametric Materials (程序化与参数化材质创作)

| Unit | Baseline Teaching Necessity | AI / Automation Impact (2026) | Evidence Type & Source Link | Game Realtime Relevance | Animation / LookDev Relevance | Gate 3 Status | Caveat / Unresolved |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **节点着色器架构 (Shader Nodes)**<br>*(Node-based Shader Graph Architecture)* | `Likely Important` | Text-to-Nodes 与 LLM 脚本可生成简单节点拓扑，但在复杂拓扑（如多层三向投影、混合逻辑）中仍显示逻辑错误或连接幻觉。 | `Academic / Demonstrated`<br>[[DD3M, arXiv 2024/2025]](https://arxiv.org/abs/2410.05432) / [[Node To Talk]](https://superhivemarket.com/products/node-to-talk) | 极高：UE 材质编辑器（Material Editor）与自定义 Shader 的共通底层。 | 极高：Blender Cycles / Arnold / Karma 着色器网络的核心搭建方式。 | `PENDING GATE 3` | 机械连线负担被压缩，但阅读、诊断与微调节点数据流向的能力价值更加凸显。 |
| **纹理坐标系**<br>*(Texture Coordinates: Generated, Object, UV)* | `Likely Important` | 生成式着色器原型常机械套用默认 UV，在未展 UV 或复杂网格上仍易出现贴图拉伸变形。 | `Limitation Evidence` & `Technical Specification`<br>[[Blender 5.2/4.5 Manual]](textbook-source-map.md) | 极高：实时世界坐标投射（World Position）、三向贴图（Triplanar）的基础。 | 极高：影视场景中大量环境岩石/地形依赖 Object 空间无缝贴图。 | `PENDING GATE 3` | 区分 Generated、Object、UV 与 Window 坐标系是程序化材质不失真的基本功。 |
| **算法纹理与噪声**<br>*(Procedural Noise & Patterns: Perlin/Voronoi)* | `Likely Important` | 算法噪波高度成熟，AI 工具可推荐噪波组合，但细分尺寸、畸变度与粗糙度参数仍需人工精确调配。 | `Vendor Capability`<br>[[Blender Shader Nodes Docs]](textbook-source-map.md) / [[Shah 2022 Ch 7-8]](textbook-source-map.md) | 高：游戏实时材质常利用低开销程序化噪波扰动打破贴图平铺重复感。 | 极高：影视 LookDev 中构建破损、杂色与微表面粗糙度变化的取之不尽源泉。 | `PENDING GATE 3` | 噪波参数调校需结合现实物理尺度，避免失真。 |
| **数学运算与混合遮罩**<br>*(Math Operations & Mix Masks)* | `Likely Important` | AI 脚本能生成基础数学节点，但在阈值截断（Clamp）、范围重映射与高阶非线性混合上仍经常出现逻辑缺陷。 | `Academic / Demonstrated`<br>[[DD3M, arXiv 2024/2025]](https://arxiv.org/abs/2410.05432) | 极高：实时材质节省贴图采样的核心手段（用算力换带宽）。 | 极高：高阶 LookDev 精确控制分层混合因子（Blend Factor）的数学工具。 | `PENDING GATE 3` | 加减乘除、Smoothstep、Power 等基础数学操作是程序化思维的坚实内核。 |
| **色彩映射与区间重映射**<br>*(ColorRamp & Range Remapping)* | `Likely Important` | AI 可快速提取调色板生成色标，但对极端输出值（如导致反射率超出安全范围的死黑死白）缺乏自发物理约束。 | `Academic / Demonstrated`<br>[[Blender Shader Nodes Docs]](textbook-source-map.md) | 极高：将单通道灰度噪波重映射为合规 Base Color 与 Roughness 范围。 | 极高：离线渲染中精细调整微表面菲涅尔衰减曲线的关键节点。 | `PENDING GATE 3` | 重点掌握通过 Map Range 或 ColorRamp 约束物理安全区间。 |
| **映射缩放与平铺控制**<br>*(Mapping, Scale & Tiling Control)* | `Likely Important` | 工具与 AI 插件可自动生成 Mapping 节点，但实际平铺比例是否匹配真实世界米制单位全靠人工肉眼校准。 | `Vendor Capability`<br>[[Shah 2022 Ch 8]](textbook-source-map.md) | 极高：游戏关卡地面、墙面材质平铺尺寸必须严格符合人体工学比例。 | 极高：影视布景材质物理尺度的真实性底线。 | `PENDING GATE 3` | 操作虽简单，但尺度失调是学生作品最常见的“业余破绽”。 |
| **随机化与多变异质感**<br>*(Randomization & Multi-variation)* | `Likely Important` | 可通过 Object Info / Geometry 节点引入随机种子，AI 亦能辅助编写逻辑，但整体变异跨度需人眼平衡。 | `Academic / Demonstrated`<br>[[Blender Shader Nodes Docs]](textbook-source-map.md) | 极高：大批量道具避免视觉重复感（Tile repetition）的核心。 | 高：集群资产与场景散布道具的质感微变异。 | `PENDING GATE 3` | 掌握利用随机 ID 驱动色相与粗糙度偏移的程序化技巧。 |
| **节点组封装与参数暴露**<br>*(Node Group Encapsulation & Interface)* | `Likely Important` | 脚本虽能打包节点，但对外暴露哪些关键控制滑块（Sliders）、参数命名与默认值设定属于人机交互设计范畴。 | `Academic / Demonstrated` & `Project Inference`<br>[[Shah 2022 Ch 10]](textbook-source-map.md) | 极高：制作供关卡美术使用的材质母版（Master Material）的常见规范（Project Inference）。 | 极高：影视管线中向照明组交付可调着色器资产的常用做法。 | `PENDING GATE 3` | 重点培养“黑盒封装思维”：隐藏复杂内部网络，只暴露必要艺术控制参数。 |
| **独立程序化纹理与 `.sbsar` 母版生成**<br>*(Standalone Procedural Texture & `.sbsar`)* | `Likely Optional` | 当前被引用的学术与工业工具未显示能由纯自然语言直接生成工业级复杂 Substance Designer（`.sbsar`）图；该领域仍显示极高专业门槛。 | `Limitation Evidence`<br>[[Adobe Substance 3D Designer Docs]](textbook-source-map.md) | 中等：技术美术（TA）制作跨项目通用材质母版的利器。 | 中等：影视管线制作可动态调整分辨率的程序化纹理库。 | `PENDING GATE 3` | 维持 `Likely Optional`。本科 8 周不宜重度强求全流程 Designer，聚焦通用节点思维。 |
| **程序化结果烘焙为 PBR 贴图包**<br>*(Baking Procedural to PBR Texture Set)* | `Likely Important` | 将复杂程序化着色网络一键烘焙为标准离线贴图集的技术高度自动化。 | `Non-AI Workflow Automation`<br>[[Blender Manual Baking]](textbook-source-map.md) / [[Shah 2022 Ch 10]](textbook-source-map.md) | 极高：将离线复杂节点网络转换为实时引擎可运行贴图的必要流程。 | 中等：影视资产在不同 DCC（如 Houdini/Maya/Katana）间流转的标准化手段。 | `PENDING GATE 3` | 重点关注烘焙位深度（32-bit/16-bit 法线与置换，防止出现色阶断层）。 |

---

### 3.5 模块五：Material Acquisition & Conversion (材质采集、图像转换与平铺)

| Unit | Baseline Teaching Necessity | AI / Automation Impact (2026) | Evidence Type & Source Link | Game Realtime Relevance | Animation / LookDev Relevance | Gate 3 Status | Caveat / Unresolved |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **照片/扫描参考转 PBR 材质原理**<br>*(Photometric / Scan Reference to PBR)* | `Likely Important` | 传统光度立体法原理已被部分集成进神经网络 De-lighting 与反射率估算模型中，理论门槛大幅降低。 | `Academic / Demonstrated`<br>[[IntrinsiX, NeurIPS 2025]](https://arxiv.org/abs/2410.22378) / [[Adobe Sampler Image-to-Material]](https://helpx.adobe.com/substance-3d-sampler/filters/image-to-material.html) | 高：快速将现实世界表面纹理转为可用贴图。 | 高：低成本获取真实世界脏迹与微结构参考。 | `PENDING GATE 3` | 需培养学生识别“合规拍摄样本”（避免强直射阴影与反光溢出）的拍摄能力。 |
| **Substance 3D Sampler 工具链工作流**<br>*(Substance 3D Sampler Workflow)* | `Likely Important` | Sampler 整合了 AI Powered 与 B2M 滤镜，并引入 Firefly 生成功能（截至 2026-04 官方明确标为 Beta）。证明了厂商功能（Vendor Capability），但尚无独立生产部署实证（Production Readiness Unresolved）。 | `Vendor Capability`<br>[[Adobe Sampler Generative Features]](https://helpx.adobe.com/substance-3d-sampler/generative-workflows/generative-features.html) | 高：游戏环境材质资产库（如地砖、树皮、沥青）的快速生成通道。 | 高：快速建立质感接近的离线渲染基础材质母版。 | `PENDING GATE 3` | 维持 `Unresolved / Recommended Candidate`。生产就绪度与 8 周必修课时权衡均未决。 |
| **Image-to-Material 智能通道提取**<br>*(Image-to-Material AI/B2M Extraction)* | `Likely Important` | 官方产品文档证明其具备单图提取 Normal/Roughness/Height 通道的能力（Vendor-supported / Usable Workflow），但不能直接等同于已在工业生产中成熟部署。 | `Vendor Capability`<br>[[Adobe Sampler Image to Material Filters]](https://helpx.adobe.com/substance-3d-sampler/filters/image-to-material.html) | 极高：极大地加速了无缝材质的初稿制备流程。 | 高：快速生成高分辨率置换与微表面粗糙度底贴图。 | `PENDING GATE 3` | 必须人工校验：AI 提取的 Roughness 往往对比度失真，Metallic 需手动指定。 |
| **图像无缝平铺处理 (Seamless Tiling)**<br>*(Seamless Tiling & AI Outpainting)* | `Likely Important` | 高度自动化，但不同输入仍可能出现 seam artifacts / macro repetition，需要人工检查并借助 Clone Stamp 或专用滤镜修复。 | `Vendor Capability`<br>[[Adobe Sampler Generative Features]](https://helpx.adobe.com/substance-3d-sampler/generative-workflows/generative-features.html) | 极高：大面积复用材质消除接缝边缘。 | 极高：场景延伸与背景资产平铺的刚性需求。 | `PENDING GATE 3` | 自动化程度高，但人工质检排查接缝伪影与宏观斑块重复仍不可省略。 |
| **真实物理尺寸校准 (Scale Calibration)**<br>*(Real-world Physical Scale Calibration)* | `Likely Important` | AI 模型无法自动获知图像拍摄时的绝对空间比例；尺寸标定完全依赖人工依据参照物（如标尺、手足）设定。 | `Academic / Demonstrated` & `Project Inference`<br>[[Adobe Sampler Docs]](https://helpx.adobe.com/substance-3d-sampler/) / [[Shah 2022 Ch 6]](textbook-source-map.md) | 极高：地砖、布料纹理若物理尺寸失调，直接破坏空间尺度真实感。 | 极高：资产必须精确对齐物理尺寸，确保置换与景深计算正确。 | `PENDING GATE 3` | 必须作为关键验收标准保留：每张材质贴图必须拥有明确的世界空间尺寸（米/厘米）。 |

---

### 3.6 模块六：LookDev & Multi-environment Validation (视觉开发与跨引擎验证)

| Unit | Baseline Teaching Necessity | AI / Automation Impact (2026) | Evidence Type & Source Link | Game Realtime Relevance | Animation / LookDev Relevance | Gate 3 Status | Caveat / Unresolved |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Blender 材质视口与基础着色验证**<br>*(Blender Viewport & Basic Shading Validation)* | `Likely Important` | 视口渲染引擎（EEVEE-Next 与 Cycles）支持实时快速切换，但跨视口光照平衡与材质解析仍需人工目视评定。 | `Vendor Capability`<br>[[Blender 5.2/4.5 Manual]](textbook-source-map.md) | 高：作为通识三维平台，快速检验材质基本通道连接与光影响应。 | 极高：低成本建立影视级 Cycles 离线渲染 LookDev 预览环境。 | `PENDING GATE 3` | 养成在真实着色器环境中检验材质的习惯，避免单一视口假象。 |
| **Unreal Engine 实时材质实例组装**<br>*(Unreal Engine Master & Material Instances)* | `Likely Core` | 支持脚本批量生成材质实例，但母版材质架构（Master Material）设计、参数暴露与动态实例组装仍为常见的人工作业流程（Project Inference）。 | `Technical Specification`<br>[[Unreal Engine Physically Based Materials]](https://dev.epicgames.com/documentation/en-us/unreal-engine/physically-based-materials-in-unreal-engine) | 核心：游戏项目中大量资产通常通过材质实例（Material Instance）交付（Project Inference 上下文示例）。 | 中等：现代影视虚拟制片（Virtual Production）实时 LED 墙着色常用方式。 | `PENDING GATE 3` | 建议保留完整的“贴图导入 $\rightarrow$ 材质实例组装 $\rightarrow$ 参数调优”实操流程。 |
| **游戏运行时材质性能与约束 (ORM/BC7)**<br>*(Runtime Performance, BC7 & Texture Packing)* | `Likely Important` | 引擎可自动压缩，但通道混合（Channel Packing）策略与贴图尺寸优化仍需人工根据显存预算规划。 | `Technical Specification`<br>[[Karis 2013]](https://cdn2.unrealengine.com/Resources/files/2013SiggraphPresentationsNotes-26915738.pdf) / [[UE Docs]](https://dev.epicgames.com/documentation/en-us/unreal-engine/) | 核心：直接影响运行帧率（FPS）、显存占用与带宽开销。 | 低：影视离线渲染关注精度胜于带宽，通常使用散装 16/32-bit 格式。 | `PENDING GATE 3` | 游戏出口的核心指标，散装贴图进入引擎前必须经过规范化打包。 |
| **影视/动画高保真着色差异 (SSS/Coat)**<br>*(Cinematic High-fidelity Shading: SSS, Coat)* | `Likely Optional` | 当前被引用的 AI 材质生成工具主要针对基础电介质/金属模型；audited workflows 在多层薄膜干涉、次表面散射（SSS）等高阶光学参数生成上仍显示局限。 | `Technical Specification` & `Limitation Evidence`<br>[[ASWF OpenPBR Spec v1.1.1]](https://academysoftwarefoundation.github.io/OpenPBR/) | 低：实时开销昂贵，游戏通常使用简化近似模型。 | 核心：角色皮肤、玉石、车漆清漆层等照片级真实感的关键通道。 | `PENDING GATE 3` | 维持 `Likely Optional`。作为拔高或分流专题，不强加给全部学生。 |
| **跨渲染器着色表现差异对比**<br>*(Cross-renderer Shading Discrepancies)* | `Likely Important` | 当前被引用的 AI 工具链未解决跨渲染器（UE vs Cycles vs Marmoset）因 BRDF 微表面实现、微几何遮蔽函数差异导致的视觉异化。 | `Limitation Evidence`<br>[[Akenine-Möller Real-Time Rendering 4th]](textbook-source-map.md) / [[McDermott PBR Guide]](textbook-source-map.md) | 高：确保资产从 DCC 导出后在游戏引擎内不发生质感崩塌。 | 极高：确保资产在离线渲染农场跨平台渲染时的一致性。 | `PENDING GATE 3` | 重点培养“多环境对比排错”思维，理解为什么同一套贴图在不同引擎看起来不同。 |
| **多环境 IBL 与极端光照压力测试**<br>*(Multi-environment IBL & Lighting Stress Testing)* | `Likely Core` | 可通过自动化脚本旋转 HDR 环境贴图，但材质在极端强光/弱光/多色温下的物理合理性裁决仍依赖人工目视检验。 | `Non-AI Workflow Automation` & `Technical Specification`<br>[[Dinur 2026 Ch 12-15]](textbook-source-map.md) / [[McDermott PBR Guide]](textbook-source-map.md) | 极高：保证资产在动态昼夜交替、洞穴阴影时始终可信不破绽。 | 极高：影视资产 LookDev 标准流程（Chrome Ball / Grey Ball + 多套不同 HDRI 旋转验证）。 | `PENDING GATE 3` | 验收准则：材质应在多种环境光（直射光、阴天漫射、室内环境）下进行压力测试。 |

---

## 4. Gate 2 补充矩阵：新兴 AI 原生材质技能池分级映射 (13 单元)

根据 [`ai-impact-on-material-workflows.md`](ai-impact-on-material-workflows.md) 第 6 节的研究结论，2026 年涌现出 13 项 AI 原生材质技能候选。本矩阵完成其基线属性规范化与证据类型 Join。

### 4.1 Tier 1：高置信度核心候选 (High-confidence Emerging Skills — 4 项)

| Unit | Baseline Teaching Necessity | AI / Automation Capability & Impact (2026) | Evidence Type & Source Link | Game Realtime Relevance | Animation / LookDev Relevance | Gate 3 Status | Caveat / Unresolved |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **材质语义提示词工程**<br>*(Material Semantic Prompting)* | `New Candidate (Tier 1)` | 厂商文档与学术演示支持通过更具体的材质与工艺实体术语（如“Anodized Aluminum”、“Weathered Oak”）提升生成的受控性与约束表达（more specific material/process terminology can improve controllability and constraint expression）。 | `Academic / Demonstrated` & `Vendor Capability`<br>[[Adobe Sampler Generative Features]](https://helpx.adobe.com/substance-3d-sampler/generative-workflows/generative-features.html) / [[Meshy AI Texturing]](https://docs.meshy.ai/texturing) | 高：辅助生成特定风格与质感的概念贴图底料。 | 高：探索不同材质方案并辅助形成情绪板。 | `PENDING GATE 3` | Adobe 文档证明“具象提示词带来更多控制”，不等于模型能精准理解全部物理光学方程。 |
| **参考图像条件约束与风格锚定**<br>*(Reference Conditioning & ControlNet)* | `New Candidate (Tier 1)` | 借助通用条件生成技术（ControlNet Depth/Normal、IP-Adapter 与参考图像引导）提高空间几何对应与风格收敛度。该证据证明的是通用 conditioning/control 机制，不直接等同于材质生产落地实证。 | `Academic / Demonstrated`<br>[[Dinur 2026 Ch 19]](textbook-source-map.md) / [[IntrinsiX, NeurIPS 2025]](https://arxiv.org/abs/2410.22378) | 高：提升生成纹理与网格几何结构的宏观对应。 | 极高：辅助概念设计稿或现场实拍参考的色彩质感继承。 | `PENDING GATE 3` | 属于通用 AI 控制机制在材质中的迁移应用，不能断言其为成熟材质生产标准。 |
| **跨通道 PBR 物理诊断**<br>*(Cross-channel PBR Physical Diagnosis)* | `New Candidate (Tier 1)` | 现存被引用的生成工具往往各自生成单通道或缺乏物理耦合约束，容易产生“法线凹凸强烈但粗糙度无响应”、“金属表面存在异常高漫反射”等跨通道不自洽现象。 | `Limitation Evidence` & `Project Inference`<br>[[Tripo 80 Level Interview]](https://80.lv/articles/how-tripo-is-tackling-clean-topology-for-its-3d-asset-pipeline/) / [[McDermott PBR Guide]](textbook-source-map.md) | 极高：跨通道穿帮在动态光照下容易暴露着色假象。 | 极高：离线多层渲染中容易导致高光与漫反射严重脱节。 | `PENDING GATE 3` | 人工跨通道自洽性审计能力价值显著提升。 |
| **人机协同分层迭代与局部微调**<br>*(Human-in-the-Loop Layer Structuring)* | `New Candidate (Tier 1)` | 将 AI 生成的扁平贴图导入 Substance 3D Painter 等工具，通过遮罩、图层混合模式与手绘笔刷进行分层重构与局部微调。 | `Academic / Demonstrated` & `Project Inference`<br>[[Shah 2022 Ch 4]](textbook-source-map.md) / [[Meshy Docs]](https://docs.meshy.ai/texturing) | 极高：团队协作中保持图层栈结构以应对后续迭代修改（Project Inference）。 | 极高：影视资产迭代中精细微调局部区域光泽度的常用做法。 | `PENDING GATE 3` | 应对生成贴图缺乏图层栈局限的一种人机协同工作流尝试。 |

---

### 4.2 Tier 2：成熟中/推荐候选 (Candidate Skills — 4 项)

| Unit | Baseline Teaching Necessity | AI / Automation Capability & Impact (2026) | Evidence Type & Source Link | Game Realtime Relevance | Animation / LookDev Relevance | Gate 3 Status | Caveat / Unresolved |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **光照残留剥离与去光照修正**<br>*(De-lighting Inspection & Correction)* | `New Candidate (Tier 2)` | 自动化 De-lighting 算法常残留方向性漫射阴影或环境色温偏色，需人工利用高反差保留、曲线或通道画笔进行二次剥离修正。 | `Academic / Demonstrated`<br>[[IntrinsiX, NeurIPS 2025]](https://arxiv.org/abs/2410.22378) / [[LumiTex, ICLR 2026]](https://arxiv.org/abs/2501.03875) | 极高：残留阴影的贴图在动态光照下容易产生“重影”穿帮。 | 极高：破坏打光自由度，导致资产在不同光照角度下显假。 | `PENDING GATE 3` | 掌握识别并修补 Albedo 去光照瑕疵的基本方法。 |
| **AI 材质变体策展与筛选**<br>*(AI Material Variation Curation)* | `New Candidate (Tier 2)` | 借助生成工具可在短时间内批量生成多种风化或色彩倾向的变体草稿，材质师需承担审美方案筛选与合规过滤工作。 | `Vendor Capability`<br>[[Adobe Sampler Generative Features]](https://helpx.adobe.com/substance-3d-sampler/generative-workflows/generative-features.html) / [[Meshy AI Texturing]](https://docs.meshy.ai/texturing) | 高：快速为环境道具配置多样化变体以减少重复感。 | 高：概念阶段向艺术指导提供质感选型参考。 | `PENDING GATE 3` | 策展能力依赖艺术审美与物理常识把关，避免随机无序抽奖。 |
| **版本控制与随机种子管理**<br>*(Seed & Workflow Version Reproducibility)* | `New Candidate (Tier 2)` | 生成模型具备随机性；工业资产生产注重可复现性，需系统记录 Prompt、Seed、采样参数、模型版本与工作流节点文件（Project Inference）。 | `Vendor Capability` & `Project Inference`<br>[[Adobe Sampler Docs]](https://helpx.adobe.com/substance-3d-sampler/) | 极高：资产版本迭代中若无法追溯参数，会导致资产风格断代。 | 极高：大型视效管线对资产版本追踪（Asset Tracking）的常见规范。 | `PENDING GATE 3` | 培养工程化素养，避免无法复现的一次性资产进入管线。 |
| **AI 纹理接缝与伪影修复**<br>*(AI Artifact & Seam Inpainting)* | `New Candidate (Tier 2)` | 生成模型在 UV 边界或复杂凹陷处仍可能产生拉伸、模糊或缝隙伪影，需借助智能局部修补（Inpainting）或克隆画笔修复。 | `Academic / Demonstrated`<br>[[Tripo 80 Level Interview]](https://80.lv/articles/how-tripo-is-tackling-clean-topology-for-its-3d-asset-pipeline/) | 极高：UV 接缝处的伪影在视口中较为明显，需予以消除。 | 极高：特写镜头下伪影直接影响最终成像质量。 | `PENDING GATE 3` | 结合投影画笔与智能修补滤镜高效修复接缝伪影。 |

---

### 4.3 Tier 3：实验性/前沿观察池 (Experimental / Watchlist — 5 项)

| Unit | Baseline Teaching Necessity | AI / Automation Capability & Impact (2026) | Evidence Type & Source Link | Game Realtime Relevance | Animation / LookDev Relevance | Gate 3 Status | Caveat / Unresolved |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **材质母版提示词驱动调参**<br>*(Prompt-to-Parameter Control)* | `New Candidate (Tier 3)` | 探索通过语言指令调节着色器参数（如“让锈斑扩散并增加粗糙度”），目前属于工具插件或原型演示。 | `Vendor Capability / Demonstrated`<br>[[Node To Talk]](https://superhivemarket.com/products/node-to-talk) | 中等：未来可能用于关卡着色器参数快速调控的原型探索。 | 中等：影视复杂着色网络快速批量调参原型。 | `PENDING GATE 3` | 依赖专用插件，尚非标准化工业管线，列入视野观察。 |
| **资产血统与商用合规判断**<br>*(Asset Provenance & Licensing Judgment)* | `New Candidate (Tier 3)` | 评估生成模型训练集来源、版权归属（如商业授权承诺 vs 开源模型许可）及知识产权合规性。 | `Vendor Capability` & `Project Inference`<br>[[Adobe Sampler Generative Features]](https://helpx.adobe.com/substance-3d-sampler/generative-workflows/generative-features.html) | 高：商业产品发布面临的版权与法务审查风险。 | 极高：主流影视制片对生成式内容版权的法务限制。 | `PENDING GATE 3` | 属于行业法律与伦理通识，不列入贴图实操技能考核。 |
| **智能体节点图编排**<br>*(Agentic Graph Orchestration)* | `New Candidate (Tier 3)` | 探索由多智能体协作进行着色网络分析、连线排错与资产转译，属于前沿学术与工具实验。 | `Academic / Demonstrated`<br>[[DD3M, arXiv 2024/2025]](https://arxiv.org/abs/2410.05432) / [[Node To Talk]](https://superhivemarket.com/products/node-to-talk) | 中等：技术美术自动化流水线的前沿探索方向。 | 中等：视效管线自动化批处理实验。 | `PENDING GATE 3` | 超出本科基础课程范围，作为技术前沿讲座或教师参考。 |
| **跨平台物理材质标准化映射**<br>*(Standardized MaterialX/OpenPBR Translation)* | `New Candidate (Tier 3)` | 推动材质超越特定软件私有格式，基于 OpenPBR 1.1 / MaterialX 规范探索跨引擎与渲染器的材质互通与转译。 | `Technical Specification`<br>[[ASWF OpenPBR Spec v1.1.1]](https://academysoftwarefoundation.github.io/OpenPBR/) | 高：跨引擎通用材质描述与转译。 | 极高：视效工作室跨 DCC 资产共享的行业通用规范。 | `PENDING GATE 3` | Painter 12.1 已原生支持 OpenPBR 1.1 规范，保持紧密跟踪。 |
| **视觉特征约束规范制定**<br>*(Visual Constraint Specification)* | `New Candidate (Tier 3)` | 探索为生成管线制定结构化风格规范（如饱和度区间、磨损上限、法线深度范围），约束生成输出一致性。 | `Academic / Demonstrated` & `Project Inference`<br>[[Dinur 2026 Ch 19]](textbook-source-map.md) | 高：大型项目利用 AI 辅助生产时的质检参考准则。 | 高：影视资产外包质检规范参考。 | `PENDING GATE 3` | 属于高阶生产管理范畴，本科阶段以人眼质检把关为主。 |

---

## 5. 双出口应用分化特征总结 (Game Realtime vs. Animation / LookDev)

通过 Gate 2 的逐项 Join，双应用出口对材质能力的工业诉求呈现出清晰的结构性分化：

```
┌────────────────────────────────────────────────────────────────────────────┐
│                    两大下游应用出口的工业诉求与壁垒分化                    │
├──────────────────────┬─────────────────────────────────────────────────────┤
│ 维度                 │ 实时游戏 (Game Realtime)                            │
├──────────────────────┼─────────────────────────────────────────────────────┤
│ **核心关注**         │ 运行帧率（FPS）、GPU 显存带宽、Draw Call 开销       │
│ **着色模型**         │ 简化微表面模型（GGX/Smith）、电介质 4% 基础反射率   │
│ **贴图格式**         │ 通道打包（ORM: AO+Roughness+Metallic）、BC7 压缩    │
│ **材质架构**         │ 材质母版（Master Material）与参数化材质实例         │
│ **光照鲁棒性**       │ 适应动态昼夜交替、局部点光源与各种后处理穿帮考验    │
│ **AI 落地主要障碍**  │ 散装贴图格式不符、通道未打包、法线轴向混淆等工程痛点│
├──────────────────────┼─────────────────────────────────────────────────────┤
│ 维度                 │ 影视动画 (Animation / LookDev)                      │
├──────────────────────┼─────────────────────────────────────────────────────┤
│ **核心关注**         │ 镜头特写真实感、多跳物理全局光照（GI）、色彩空间一致│
│ **着色模型**         │ 高阶多层模型（OpenPBR: SSS、Coat、Thin Film、置换） │
│ **贴图格式**         │ 独立高位宽贴图（16/32-bit EXR/TIFF）、UDIM 多象限   │
│ **材质架构**         │ 节点图着色网络（Cycles/Arnold/Karma/RenderMan）     │
│ **光照鲁棒性**       │ 标准化 LookDev 流程（标准色球灰球、多套不同 HDRI 验证│
│ **AI 落地主要障碍**  │ 难以端到端直接生成高保真多层散射（SSS/Coat）参数    │
└──────────────────────┴─────────────────────────────────────────────────────┘
```

---

## 6. 未决议题与证据缺口清单 (Genuinely Unresolved & Caveats)

在 Gate 1 与 Gate 2 完成后，登记以下**真实存在且直接影响后续 Gate 3 决策**的未决问题：

1. **Substance 3D Sampler 必修深度未决 (UNRES-S2-01)**：
   - *证据现状*：Sampler 提供了 Vendor-supported 的 AI/B2M 图像转材质工作流，且整合了 Firefly 生成特性（2026-04 官方文档仍明确标为 Beta）。目前缺乏独立的生产部署（Production/Deployment）实证，其 Production Readiness 保持 Unresolved。
   - *教学矛盾*：在 8 周有限课时与机房授权成本约束下，将其设为“必修实操模块”还是“快速体验与拓展推荐”，需在 Gate 3 权衡。
2. **Substance Designer 教学深度未决 (UNRES-S2-02)**：
   - *证据现状*：AI 极难生成工业级复杂 `.sbsar` 图；Blender Shader Nodes 零门槛且可覆盖大量基础节点/参数化思维。
   - *教学矛盾*：具体替代 Designer 的教学边界仍 unresolved，是否在本科 8 周内主要由 Blender 节点承担程序化思维训练，仅将 Designer 作为概念展示？
3. **AI 生成多通道贴图的量化验收门槛未决 (UNRES-S2-03)**：
   - *证据现状*：AI 去光照（De-lighting）残留与金属度灰度噪点是普遍存在的 Limitation Evidence。
   - *教学矛盾*：如何为学生制定简洁、可量化操作的 PBR 质检法则（例如“反射率必须处于什么区间”、“金属度非 0 即 1 的容差范围与合法混合物界定”）？
4. **Game 与 LookDev 期末大作业出口的分流形式未决 (UNRES-S2-04)**：
   - *教学矛盾*：期末考核是要求所有学生必须同时提交“UE 材质实例运行包”与“Blender/Cycles LookDev 离线渲染图”，还是允许学生二选一分流专精？

---
*本矩阵由 Antigravity 自动化流水线生成并核查，作为 Stage 2 阶段 Gate 1/2 的审阅基线。*
