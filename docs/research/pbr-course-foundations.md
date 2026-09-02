# 《三维数字材质制作》第一阶段研究报告：PBR 教学基线与专业管线

> **报告版本**：v1.1 (Phase 1 Research - Revised)  
> **研究定位**：建立 2026 年本科《三维数字材质制作》（约 8 周）课程的专业技术与教学基线。本阶段聚焦于成熟游戏资产与实时 PBR 工业标准，不展开讨论 AI 替代流程。  
> **知识库调用声明**：当前 Runtime 已成功连接并核实外部能力 `Course Knowledge Notebook` (Locator: `e29f9644-03b2-4e1b-bcb0-b954b5bf08be`)。由于该知识库当前处于 0 来源初始状态，本报告基于第一手官方技术文档、技术规范与行业出版物进行引证。

---

## 目录
1. [PBR 基础理论与物理可信性原则](#1-pbr-基础理论与物理可信性原则)
2. [标准游戏材质生产 Pipeline](#2-标准游戏材质生产-pipeline)
3. [核心 DCC 与引擎软件角色比较](#3-核心-dcc-与引擎软件角色比较)
4. [国内外权威教材与课程候选清单剖析](#4-国内外权威教材与课程候选清单剖析)
5. [8 周本科课程教学价值矩阵](#5-8-周本科课程教学价值矩阵)
6. [尚未解决与进入下一阶段研究的问题](#6-尚未解决与进入下一阶段研究的问题)

---

## 1. PBR 基础理论与物理可信性原则

基于物理的渲染（Physically Based Rendering, PBR）是一套基于现代计算机图形学微表面理论（Microfacet Theory）与光学能量守恒定律的材质着色与资产制作体系。

### 1.1 核心贴图通道与技术规范

在实时渲染与资产交付管线中，**Metallic/Roughness 工作流** 是最通用的通道组织形式。各通道的物理意义与色彩空间规范如下：

| 通道名称 (Map Name) | 物理含义与功能 | 色彩空间与取值规范 | 典型错误认知 |
| :--- | :--- | :--- | :--- |
| **Base Color (Albedo)** | 表面漫反射与高光反射的基础反射率。[Adobe PBR Guide (Part 1)](https://substance3d.adobe.com/tutorials/courses/the-pbr-guide-part-1) 指出：非金属的 Base Color 代表漫反射颜色（Diffuse）；金属的 Base Color 代表高光反射率（Specular Reflectance）。 | **sRGB (Gamma 编码)**。根据 [Adobe PBR Guide (Part 2)](https://substance3d.adobe.com/tutorials/courses/the-pbr-guide-part-2)，电介质的明度需保持在安全区间（通常约为 30–240 sRGB 之间），严禁出现纯黑 `0` 或纯白 `255`。 | 将定向阴影、光照渐变或环境闭塞（AO）直接手绘在 Base Color 中。 |
| **Roughness** | 描述微观表面法线分布的离散程度（通常基于 GGX / Trowbridge-Reitz 分布模型，参见 [Brian Karis, SIGGRAPH 2013](https://cdn2.unrealengine.com/Resources/files/2013SiggraphPresentationsNotes-26915738.pdf)）。数值越小高光越锐利聚拢，数值越大高光越发散模糊。 | **Linear (Non-Color / Grayscale)**。取值范围 `0.0` 至 `1.0`。 | 混淆粗糙度（Roughness）与光泽度（Glossiness，二者为反向映射关系）。 |
| **Metallic** | 标记表面微观物理结构属于电介质（非金属，如绝缘体、木材、塑料、岩石）还是导体（金属）。 | **Linear (Non-Color / Grayscale)**。在绝大多数宏观表面应遵循严格的**二值化原则（`0.0` 或 `1.0`）**。中间灰度值仅用于粉尘微层、氧化腐蚀过渡、半导体或像素边缘抗锯齿。 | 将金属度作为“增强反射感”的渐变滑块使用。 |
| **Normal (法线贴图)** | 使用 RGB 向量在切线空间（Tangent Space）中编码微观表面法线方向（参见 [Blender Manual - Normal Map Node](https://docs.blender.org/manual/en/latest/render/shader_nodes/vector/normal_map.html)），在不增加顶点的前提下模拟高频凹凸。 | **Linear (Normal / Vector Data)**。中性平坦值为 `(0.5, 0.5, 1.0)` / 8-bit `(128, 128, 255)`。需注意 DirectX（Y- 反向）与 OpenGL（Y+ 正向）坐标轴差异。 | 误以为法线贴图能改变物体的实际几何外轮廓（Silhouette）。 |
| **Height / Displacement** | 描述表面沿几何法线方向的高度位移，用于视差贴图（Parallax Mapping）、曲面细分或着色器置换计算。 | **Linear (Non-Color / Grayscale)**。 | 与法线贴图混淆，未理解两者在几何重构层级上的差异。 |
| **Ambient Occlusion (AO)** | 预计算局部微几何结构（裂缝、拐角、孔洞）对间接漫反射环境光（IBL）的几何遮挡比例。 | **Linear (Non-Color / Grayscale)**。仅用于衰减间接光照，不应直接影响直接光源的强阴影。 | 强行将 AO 乘死在 Base Color 中，导致直接光照下暗部死黑。 |

### 1.2 物理可信性原则与标准分层

#### 1. 能量守恒定律（Energy Conservation）
根据图形学经典定义（参见 [*Real-Time Rendering, 4th Edition*, Chapter 9](https://www.realtimerendering.com/)），表面反射与散射光线的总能量不得超过入射总能量：
$$\text{Reflected Light} + \text{Refracted/Absorbed Light} \le \text{Incident Light}$$
金属导体具有大量自由电子，折射进入材质内部的光线会被迅速吸收并转化为热能，因此纯金属 **没有漫反射分量（Diffuse = 0）**，其视觉表现完全由带有特定波长选择性的镜面反射构成（即 Base Color 表达的高光颜色）。

#### 2. 电介质基础反射率（Dielectric $F_0$）的规范差异与教学基准
菲涅尔反射定律描述了光线反射率随观察视线与表面法线夹角变化的规律。当视线垂直于表面（0° 入射角）时的反射率记为 $F_0$：
- **[Khronos glTF 2.0 核心规范](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#materials)**：为了保障资产跨平台交换的轻量性与一致性，glTF 2.0 Metallic/Roughness 模型将所有电介质的 $F_0$ **硬编码固定为 `0.04`**（4% 反射率，对应折射率 $\text{IOR} \approx 1.5$）。
- **[Epic Games Unreal Engine 材质规范](https://dev.epicgames.com/documentation/en-us/unreal-engine/physically-based-materials-in-unreal-engine)**：Unreal 的 Metallic/Roughness 模型中，非金属的默认 $F_0$ 同样为 4%（对应 `Specular` 输入默认值 `0.5`，内部公式将 0~1 的 Specular 输入线性映射到 0%~8% 的 $F_0$ 范围），允许艺术家对极高折射率（如宝石）或极低折射率电介质进行微调。
- **教学基准**：在本科教学中，将“约 4% ($F_0 \approx 0.04$)”作为绝大多数常见非金属（塑料、木材、石材、水、皮肤）的基准认知，有助于学生建立直观的物理常识，避免学生随意手调反射率破坏物理一致性。

#### 3. 颜色空间与线性工作流（Linear Workflow vs. sRGB）
- **色彩贴图**：Base Color 表达人类色彩感知，制作与存储采用 sRGB（Gamma 2.2）编码，着色器采样时必须线性化（De-gamma）转换至 Linear 空间运算。
- **数据贴图**：Roughness、Metallic、AO、Normal 等通道承载的是具体的数学参数或向量，**必须在导入 DCC 和引擎时强制标记为 Linear / Non-Color**。若误按 sRGB 解码，伽马曲线会导致粗糙度严重偏亮、金属度灰度化以及法线凹凸方向畸变。

#### 4. PBR 材质标准的分层体系
在教学与技术选型中，不能将各类规范混为一谈，应清晰区分为四个层次：
1. **资产交换材质模型 (Interchange Material Models)**：如 [Khronos glTF 2.0](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#materials) 与 OpenUSD（UsdPreviewSurface），侧重跨平台最小公倍数的轻量化资产传递。
2. **着色模型标准 (Shading Models / Uber-shaders)**：如 [ASWF OpenPBR](https://academysoftwarefoundation.github.io/OpenPBR/) 与 Disney Principled BRDF，侧重于为影视与高质量工业渲染提供统一、完备的多层物理材质描述（Base, Specular, Transmission, Coat, Sheen 等）。
3. **DCC 工具端实现 (DCC Implementations)**：如 [Blender Principled BSDF v2](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/principled.html)（Blender 4.0+ 已向 OpenPBR 架构对齐）与 Substance 3D 渲染视图，侧重交互式资产制作与视口反馈。
4. **实时游戏引擎接口 (Game-Engine Material Interfaces)**：如 [Unreal Engine Material Graph](https://dev.epicgames.com/documentation/en-us/unreal-engine/physically-based-materials-in-unreal-engine) 与 [Unity URP Lit Shader](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest/index.html?subtopic=manual/lit-shader.html)，侧重于实时光栅化/光线追踪性能优化、G-Buffer 结构匹配与纹理通道打包（ORM）。

---

## 2. 标准游戏材质生产 Pipeline

现代游戏资产制作遵循高度严密的工业流水线：

$$\text{High/Low Poly Modeling} \longrightarrow \text{UV Unwrapping} \longrightarrow \text{Texel Density Planning} \longrightarrow \text{Baking} \longrightarrow \text{Texturing} \longrightarrow \text{Material/Shader} \longrightarrow \text{Engine Validation}$$

### 2.1 核心环节的技术逻辑与问题剖析

#### 1. 为什么独立游戏资产中 UV 仍然是核心环节？
- **映射机制与现代替代方案**：GPU 的纹理采样器（Texture Sampler）原生基于 2D 参数化坐标寻址。尽管在场景环境制作中广泛存在 **Triplanar（三向投影）**、**World-Space / Object-Space Procedural Mapping（世界/物体空间程序化纹理）** 等无 UV 依赖技术，但在**独立游戏道具、角色与机械资产（Unique Assets）**制作中，UV 展开依然具有不可替代的作用：
  1. **烘焙映射的唯一定位载体**：高模向低模传递切线空间法线、局部曲率等空间数据时，必须有唯一的 2D 坐标系；
  2. **接缝与硬边对应原则**：在硬表面资产中，模型的硬边（Hard Edges / Smoothing Group 切分处）必须在 UV 上切开接缝（Seam）。若硬边共用平滑 UV 岛，切线空间法线插值会导致明显的烘焙黑边与渐变伪影；
  3. **显存压缩与局部性**：BC 贴图压缩（Block Compression）基于 $4 \times 4$ 像素块工作，合理的 UV 打包能有效避免跨块瑕疵。

#### 2. Baking（烘焙）解决的核心问题
根据 [Adobe Substance 3D Painter Baking Documentation](https://experienceleague.adobe.com/en/docs/substance-3d-painter/using/baking/baking)，Baking 是通过射线投射（Ray Casting）将高模的复杂几何特征提取为低模二维贴图的过程。
- **传递高频几何细节**：将数百万面的高模细节以切线空间 Normal Map 形式附着在几千面的低模上；
- **提取材质绘制的“几何上下文”**：烘焙生成的辅助贴图（Curvature、Ambient Occlusion、World Space Normal、Position、Thickness）直接作为程序化图层与智能遮罩的数学输入：
  - **Curvature（曲率图）**：识别模型凸缘与凹陷，驱动边缘掉漆与磨损效果；
  - **Ambient Occlusion（AO 图）**：识别结构缝隙，驱动缝隙污垢（Dirt）与积灰积水；
  - **Position / World Space Normal**：识别物体顶部朝向与地面高度，驱动顶部积雪、底部泥渍。

#### 3. Texel Density（像素密度）的关键工程价值
参考 [Leonardo Iezzi 的经典指南 *All You Need to Know about Texel Density*](https://www.artstation.com/artwork/qbOqP)：
- **定义**：单位 3D 几何尺寸在 2D 纹理空间中所分配的像素分辨率（如 10.24 px/cm）。
- **工程必要性**：
  1. **视觉一致性**：保证相邻资产或同一物体的不同部件具有统一的清晰度，避免视口出现局部模糊局部锐利的失真；
  2. **显存预算分配**：通过 UV 缩放精确控制核心视觉焦点与次要结构的纹理分配比例。

#### 4. 为什么最终必须进入实时引擎（Engine Validation）验证？
- **DCC 视口着色的局限性**：外部 DCC 软件的视口着色与后处理无法完全复现运行时的光照与阴影计算。
- **环境光适应性**：资产必须在正午直射光、阴天漫反射、室内点光源等多种 IBL 场景下验证 PBR 反射行为；
- **通道打包与平台压缩**：验证通道打包（如 ORM: R=AO, G=Roughness, B=Metallic）在引擎中的采样逻辑，排查 BC7 / ASTC 纹理压缩算法对微细节带来的损失。

---

## 3. 核心 DCC 与引擎软件角色比较

| 软件工具 | 在现代材质管线中的主要角色 | 核心优势 | 局限性与短板 | 8 周课程定位判断 |
| :--- | :--- | :--- | :--- | :--- |
| **Blender** | 全流程 DCC 建模、UV 展开、烘焙与着色原型 | 开源免费；集成度高；[Principled BSDF](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/principled.html) 贴合 OpenPBR；节点材质适合逻辑探索。 | 缺乏工业级多通道 3D 涂鸦与智能蒙版系统；自带烘焙流程操作繁琐且易出错；非破坏性贴图层叠管理弱。 | **Core（核心工具：建模/UV/烘焙基础）** |
| **Adobe Substance 3D Painter** | 资产级 3D 贴图绘制工具 | 以烘焙贴图为驱动的 [Smart Materials & Smart Masks](https://experienceleague.adobe.com/en/docs/substance-3d-painter/using/smart-materials-masks/smart-materials-masks) 体系，直观的多通道图层混合，非破坏性绘制。 | 对跨资产的程序化无缝平铺纹理合成能力弱于 Designer。 | **Core（核心工具：资产贴图绘制）** |
| **Adobe Substance 3D Designer** | 2D 程序化纹理合成与材质母版制作 | 完全基于节点与图像数学算法生成无限分辨率、参数化的 PBR 纹理（参见 [Substance Graphs 文档](https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/getting-started-with-substance-graphs.html)）；输出 `.sbsar` 资产。 | 抽象思维要求极高，节点图逻辑学习曲线陡峭，初学者极易产生挫败感。 | **Optional / 进阶（概念展示或选修拓展）** |
| **Unreal Engine 5** | 实时游戏渲染、着色器开发与资产验证 | 强大的 [Material Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/physically-based-materials-in-unreal-engine) 与材质实例系统；Lumen 实时光照与 Nanite 几何体系验证。 | 仅负责着色与运行时呈现，不负责源贴图的绘制。 | **Core / Important（材质整合与验证）** |
| **Unity (URP/HDRP)** | 跨平台游戏材质验证与轻量级着色器开发 | [Shader Graph](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest/index.html) 节点式着色器设计；针对移动端/XR 的轻量级 PBR 验证。 | 运行时消费端环境；URP 与 HDRP 材质参数略有差异。 | **Important（可选验证引擎）** |

### 3.1 软件替代性与课程定位深度解答

#### Q1: Blender 能否取代 Substance 3D Painter？
- **分析**：Blender 的 Texture Paint 目前仅提供单通道位图绘制，缺乏同时对 Base Color、Roughness、Metallic、Normal 进行统一层级管理的多通道涂层系统，且缺乏基于模型几何烘焙图（Curvature/AO）自动计算的动态生成器机制。
- **课程判断**：在以培养学生掌握标准游戏资产贴图制作能力为目标的课程中，Blender 适合承担建模、UV 与基础着色教学，但贴图分层绘制环节仍推荐以 Substance 3D Painter 作为核心实战工具。

#### Q2: Blender 能否取代 Substance 3D Designer？
- **分析**：Blender 的 Shader Nodes 面向 3D 模型表面的逐像素/逐顶点着色求值，而 Substance 3D Designer 是一个专注于 **2D 图像处理与程序化模式合成**的引擎（其 Atomic Nodes 处理位图混合、方向模糊、距离变换等）。Designer 生成的是通用的 2D 贴图与参数化 `.sbsar`，可被多种引擎直接解析。
- **课程判断**：两者设计哲学与管线接口不同，不能简单互相替代。

#### Q3: Painter 与 Designer 是否都适合进入 8 周本科课程？
- **课程判断**：**强烈建议以 Painter 为主轴，Designer 仅作为原理演示或进阶选修引入。**  
  在约 8 周的紧凑教学周期内，学生需要吸收 PBR 理论、UV 规范、Baking 烘焙以及完整的 Painter 分层材质绘制与引擎联调。Painter 的“图层+蒙版+笔刷”心智模型符合视觉艺术直觉；若强行平分学时给高度抽象数学化的 Designer，极易造成学生认知超载，无法在有限时间内交付完整的高质量资产作品。

---

## 4. 国内外权威教材与课程候选清单剖析

本轮调研对国内外公开出版物与权威教材进行了严格的逐项核查，剔除了无法追溯具体书目信息的泛化描述。

### 4.1 国际权威教材与第一手官方规范

#### 1. *Real-Time Rendering, Fourth Edition*
- **作者**：Tomas Akenine-Möller, Eric Haines, Naty Hoffman, Angelo Pesce, Michał Iwanicki, Sébastien Hillaire
- **出版社 / 出版年份**：A K Peters / CRC Press, 2018
- **ISBN**：978-1138627000
- **官方来源**：[realtimerendering.com](https://www.realtimerendering.com/)
- **内容覆盖**：实时渲染管线、图形硬件、微表面 BRDF 理论、基于物理的材质光照模型、阴影与环境光照。
- **适配度评价**：图形学界的权威圣经。理论极其严谨扎实，深度剖析了 PBR 数学推导与光线交互原理。
- **主要局限**：属于高阶计算机图形学理论著作，不包含具体美术软件（DCC）实操步骤，适合作为教师备课理论参考，不适合作为本科艺术类学生的操作教材。

#### 2. *Physically Based Rendering: From Theory to Implementation, Fourth Edition*
- **作者**：Matt Pharr, Wenzel Jakob, Greg Humphreys
- **出版社 / 出版年份**：The MIT Press, 2023
- **ISBN**：978-0262048026
- **官方来源**：[pbr-book.org](https://pbr-book.org/) (开源可查阅)
- **内容覆盖**：辐射度学、蒙特卡洛积分、反射模型、次表面散射、体积渲染与基于物理的离线渲染实现。
- **适配度评价**：光线追踪与离线物理渲染领域的顶级经典理论参考书。
- **主要局限**：面向渲染引擎开发者与图形工程师，偏重离线光线追踪算法与 C++ 源码实现，与游戏资产实时材质绘制实操脱节。

#### 3. Adobe Substance 3D 官方权威指南：*The PBR Guide (Part 1 & Part 2)*
- **作者**：Wes McDermott
- **发布机构 / 形式**：Adobe Substance 3D (Allegorithmic), 官方免费公开教程与规范文档
- **官方来源**：[Part 1: Light and Matter](https://substance3d.adobe.com/tutorials/courses/the-pbr-guide-part-1) | [Part 2: Practical Guidelines](https://substance3d.adobe.com/tutorials/courses/the-pbr-guide-part-2)
- **内容覆盖**：光线传播理论、吸收与散射、微表面理论、BRDF、Metallic/Roughness 与 Specular/Glossiness 双工作流对比、通道安全值规范、Texel Density 考量。
- **适配度评价**：**现代 PBR 美术教学最顶级的核心参考材料**。兼顾物理光学原理与资产制作规范，语言通俗且高度专业。

---

### 4.2 中国大陆出版教材现状核查与评估

经针对中国大陆近五年相关出版物的具体检索与核查，代表性实操书目评估如下：

#### 1. 《Blender+Substance 3D Painter 建模与材质制作实战》
- **作者**：来阳
- **出版社 / 出版年份**：人民邮电出版社，2024 年
- **ISBN**：978-7-115-70061-2
- **官方页面**：[人民邮电出版社](https://www.ptpress.com.cn/)
- **内容覆盖**：涵盖三维模型制作、低模/高模拓扑、UV 展开、Substance 3D Painter 常见材质（木纹、金属、皮革等）多通道绘制，并简要提及引擎展示。
- **适配度评价**：紧跟国内主流软硬件结合趋势，实战案例完整，步骤详细，适合学生课后参照操作。
- **主要局限**：定位于操作手册与案例实战，对微表面理论推导、色彩空间底层差异（sRGB vs Linear）、Texel Density 严格计算以及引擎着色器架构的深度讲解相对薄弱。

#### 2. 《Substance Painter 次世代 PBR 材质制作》
- **作者**：谢怀民、林鑫、蔡毅
- **出版社 / 出版年份**：北京理工大学出版社，2021 年
- **ISBN**：978-7-5682-9860-5
- **官方页面**：北京理工大学出版社图书检索系统
- **内容覆盖**：次世代游戏贴图概念、Substance Painter 界面工具、烘焙贴图流程、智能材质应用与实战道具案例。
- **适配度评价**：国内较早专注于 Substance Painter PBR 贴图制作的专业教材，案例结构贴合游戏美术专业。
- **主要局限**：出版时间较早，基于早期 Substance 版本编写，部分工作流夹杂了过时的 Specular 流程说明，且对最新 OpenPBR 标准及现代实时引擎联调机制覆盖不足。

> **国内教材调查结论**：  
> **本轮未找到足以单独作为主教材的高可信中国大陆出版候选。** 国内现有书籍主要偏向软件菜单与特定案例的操作步骤复现，缺乏贯穿“光学物理原理 $\rightarrow$ 严格几何/烘焙工程规范 $\rightarrow$ 引擎实时渲染”的完整知识架构。因此建议在教学中以 **Adobe 官方 *The PBR Guide*** 和 **Epic Games 官方技术文档** 作为核心理论纲领，辅以高质量实战案例书目开展教学。

---

## 5. 8 周本科课程教学价值矩阵

针对约 8 周的本科教学周期，将材质知识体系划分为四个价值层级：

```
┌────────────────────────────────────────────────────────┐
│                   Core (必须掌握)                       │
│  - PBR 基础理论与光学可信性 (BaseColor/Rough/Metal)       │
│  - UV 展开、接缝切分与 Texel Density 规划               │
│  - 高低模烘焙技术 (Normal, Curvature, AO 等)            │
│  - Substance 3D Painter 多通道分层与智能遮罩材质绘制     │
│  - 实时游戏引擎 (Unreal/Unity) 材质组装与多光照验证      │
└───────────────────────────▲────────────────────────────┘
                            │ 支撑进阶
┌───────────────────────────┴────────────────────────────┐
│                Important (应该理解)                     │
│  - 色彩空间机制 (sRGB vs Linear)                        │
│  - 纹理通道打包 (ORM: Occlusion/Roughness/Metallic)     │
│  - 烘焙图驱动生成器的底层数学逻辑                       │
│  - 引擎 Material Editor / Shader Graph 基础节点逻辑     │
└───────────────────────────▲────────────────────────────┘
                            │ 拓展视野
┌───────────────────────────┴────────────────────────────┐
│                 Optional (可选/进阶)                    │
│  - Substance 3D Designer 程序化无缝纹理与 .sbsar 制作    │
│  - 高级光学属性 (SSS, Clearcoat, Anisotropy)           │
│  - UDIM 多象限贴图工作流                                │
│  - 虚幻引擎 Nanite 与 Virtual Texturing 机制            │
└───────────────────────────▲────────────────────────────┘
                            │ 工具载体
┌───────────────────────────┴────────────────────────────┐
│              Tool-specific (软件操作性知识)             │
│  - 特定软件界面的菜单排布与快捷键                       │
│  - 特定烘焙面板的采样滑块配置                           │
│  - 导出预设模板 (Export Preset) 的配置文件定制           │
└────────────────────────────────────────────────────────┘
```

### 5.1 各层级设定理由

1. **Core（必须掌握）**：
   - 构成了现代三维资产与材质生产的不可分割基石。缺少任何一环（如不会算 Texel Density、烘焙出现严重法线错误、或无法在引擎中正确着色），均无法交付符合工业标准的合格资产。
2. **Important（应该理解）**：
   - 决定了学生是“只懂照猫画虎的软件操作工”还是“具备技术排错能力的专业技术美术”。理解通道打包与色彩空间能从根本上避免资产在跨平台部署时的性能与渲染瑕疵。
3. **Optional（可选/进阶）**：
   - 为学有余力或有志于深入程序化材质、影视级资产方向的学生提供拓展路径，但在 8 周基础课内不作全员强制考核要求，以防认知过载。
4. **Tool-specific（软件操作性知识）**：
   - 软件 UI 界面随版本快速更新，教学应着重培养学生通过官方文档自学功能的能力，而非死记硬背软件按钮。

---

## 6. 尚未解决与进入下一阶段研究的问题

本阶段确立了专业级传统 PBR 材质教学的基线。以下核心议题明确保留至后续阶段专项攻关：

1. **AI 生产力工作流对材质管线的重塑评估（Phase 2 核心）**：
   - 生成式 AI（AI 纹理生成、AI 材质无缝平铺、AI 辅助法线与曲率提取）在当前游戏与影视资产生产中的实际落地能力与精度边界；
   - 评估 AI 工具对“传统手绘修贴图”、“程序化节点搭建”等具体技能环节的替代程度与教学整合方案。
2. **8 周教学大纲的模块结构与课时划分**：
   - 待确定软件栈与教学目标后，进一步细化各周的知识讲解、课堂练习与阶段成果验收节点。
3. **最终课程教学软件栈与机房授权评估**：
   - 综合评估商业软件（Substance / Unreal）与开源方案（Blender / Godot）在高校机房环境中的部署可行性与授权成本。
4. **课程作业标准与考核指标（Rubrics）开发**：
   - 制定兼顾“PBR 物理合规性”、“Texel Density 统一性”、“烘焙精度”与“艺术表现力”的客观评分量表。

---
*报告归档于 `docs/research/pbr-course-foundations.md`，由 Antigravity 自动化研究流水线生成并核查。*
