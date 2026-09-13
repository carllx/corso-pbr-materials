# Lane C: Adobe Substance 3D Painter — Source-Native Research & Technical Index

> **Artifact Status**: Official Documentation Direct Extraction & Technical Index  
> **Primary Sources**:
> 1. Adobe Substance 3D Painter Official Documentation (`helpx.adobe.com/substance-3d-painter/`, `substance3d.adobe.com/documentation/spdoc/`, Updated 2026-07/2026-09)
> 2. Adobe Substance 3D Painter Python API Reference (`substance_painter` module)
> 3. Zeeshan Jawed Shah (2022) Chapters 1–6 (Verified hands-on execution baseline in `source-native-knowledge-index.md`)
> **Artifact Placement**: `docs/research/source-native/adobe-painter-official.md`  

---

## 1. Executive Summary & Purpose

本研究针对 **Lane C: Substance 3D Painter** 进行技术解构，重点回答：
1. 3D 空间与局部修订机制（3D Spatial & Local Revision）；
2. 图层、蒙版、锚点（Anchor Points）与跨图层依赖关系（Cross-Layer Dependencies）；
3. 跨通道同步编辑（Cross-Channel Editing）与物理烘焙贴图驱动机制；
4. Python API 与工作流自动化覆盖边界（Automation Boundary）；
5. 明确哪些任务仍然绝对依赖原生三维视觉交互与手绘介入，支持后续 Gate 3 研判：
   $$\text{软件工具手工操作课时可压缩，但 3D 空间修订与局部诊断价值不可替代}$$

---

## 2. 核心架构与空间修订机制 (Spatial Revision Mechanics)

Substance 3D Painter 在工业管线中的不可替代性，根本上建立在**以网格拓扑为基础的多通道三维空间投影与非破坏性分层计算架构**上，而非简单的 2D 位图修图：

### 2.1 3D/2D 联动视口与视差投影 (Viewport & Projections)
- **投射模式 (Fill Projection Modes)**：
  - `UV Projection`：基于参数化网格 UV 坐标进行贴图采样。
  - `Tri-planar Projection`（三平面投射）：沿网格几何空间 X, Y, Z 三轴投射，带有可调的混合过渡硬度（Hardness），用于在未展 UV 或极度复杂几何表面消除接缝与拉伸。
  - `Planar / Spherical / Cylindrical / Warp`：视口操纵器驱动的定向三维投影，支持深度剔除（Depth Culling）与背面剔除（Backface Culling），防止贴图穿透模型内部。
- **2D/3D 分屏无缝绘制 (F1 Split View)**：
  - 允许艺术家在 3D 空间直观感知光影遮挡，并在 2D UV Tile 上消除曲率形变进行平整印盖（如 Stencil 贴花）。

### 2.2 图层堆栈与多通道同步 (Layer Stack & Cross-Channel Management)
- **非破坏性图层类型**：
  - `Fill Layer`（填充图层）：由参数（颜色、粗糙度数值、平铺度、外部纹理输入）全局驱动，分辨率无损，支持后续随时任意修改贴图分辨率（从 1K 无缝切换至 4K）。
  - `Paint Layer`（绘制图层）：存储笔刷在局部空间涂抹的位图像素。
- **多通道同时求值 (Multi-Channel Evaluation)**：
  - 单个图层或笔刷可同时激活并写入多个独立通道：Base Color、Roughness、Metallic、Normal、Height、Emissive、Opacity 等。
  - 各通道拥有**独立的混合模式（Blending Mode）与透明度滑块**（例如：同一图层在 Base Color 采用 Normal 模式，但在 Height 采用 Linear Dodge/Add 模式，在 Roughness 采用 Multiply 模式）。

### 2.3 遮罩体系与高级依赖链 (Masks & Anchor Point Dependencies)
- **遮罩分层堆栈 (Mask Stacks)**：
  - 允许在同一个蒙版下堆叠多个效果：`Add Generator`（几何驱动生成器）、`Add Fill`（噪波填充）、`Add Paint`（局部笔刷手工涂抹修正）、`Add Levels`（阈值截断）、`Add Filter`（模糊与侵蚀）。
- **锚点联动系统 (Anchor Points — Critical Architecture)**：
  - 锚点是 Painter 实现**“类程序化双向依赖”**的关键架构。它允许艺术家将任意底层图层、手绘笔刷蒙版或高度细节注册为一个“数据源点”（Anchor Point）。
  - 上层图层（如边缘磨损生成器、铁锈填充层、微观污垢层）可以通过 `Add fill` 或 `Generator` 的微观高度输入端口，直接引用该锚点。
  - **核心价值**：当艺术家在底层手绘或修改一颗螺丝、一道凹痕时，上层由生成器驱动的磨损、锈蚀、污垢与高度差法线会自动实时重新计算并环绕该凹痕分布，完全保持非破坏性。

### 2.4 网格贴图烘焙驱动 (Baking-Driven Workflows)
- Painter 的智能材质（Smart Materials）与生成器（Generators）高度依赖基于 GPU 射线投射烘焙的 7 组网格贴图：
  - **Curvature (曲率图)**：分离凸角（Cavity/Edge）与凹槽；
  - **Ambient Occlusion (环境遮挡图)**：标识自遮挡裂隙；
  - **Position (空间位置图)**：标识三维全局坐标（Y 轴高度沉降）；
  - **World Space Normal / Thickness**：法线朝向与透光厚度。
- 这决定了生成器是“空间拓扑自适应的”，能够将材质母版无缝复用到不同外形的资产上。

---

## 3. 自动化与 API 覆盖边界 (Python / Automation Boundary)

Substance 3D Painter 提供了内嵌 Python 解释器与官方 API 模块 `substance_painter`：

### 3.1 Python API 的实际能力范围 (What It CAN Automate)
- **工程全生命周期批处理 (Project Lifecycle & Batch Pipeline)**：
  - 自动化创建工程（`project.create()`）、指定网格资产路径与工作流模板；
  - 自动化保存、另存与关闭工程（`project.save()`, `project.close()`）；
  - 自动化导入外部资源（贴图、自定义网格）到 Shelf/Assets 资源库。
- **烘焙贴图自动化 (Headless/Scripted Baking)**：
  - 配置烘焙参数、匹配高低模命名规则（By Mesh Name）、触发全套网格贴图批处理烘焙（`baking.bake()`）。
- **贴图导出与通道重打包 (Texture Export & Channel Packing)**：
  - 遍历 Texture Sets，指定导出预设（Export Preset，如 Unreal Packed / Unity HD / ORM），批量导出指定分辨率的 PBR 贴图序列（`export.export_project_textures()`）。
- **材质模板与智能材质应用**：
  - 可以通过脚本在 Texture Set 上自动赋予现成的 Smart Material 或 Material 预设。

### 3.2 Python API 的明确局限与空白 (What It CANNOT Safely Do)
- ❌ **无法通过代码执行连续的三维空间交互笔刷绘制 (No Continuous Spatial Painting via API)**：
  - API 不支持模拟画笔压感、动态笔触轨迹、涂抹（Smudge）、克隆图章（Clone）在复杂曲面上的手绘动作。
- ❌ **无法自动化代替艺术审美驱动的叙事性局部修正**：
  - AI 或脚本无法感知游戏角色盔甲上的战斗擦痕是否符合特定叙事动机；
  - 无法完全自动判断视线焦点的材质对比度微调。

---

## 4. 教学价值研判支撑：操作价值 vs 空间修订与诊断价值

通过对官方架构的实证梳理，为后续 Gate 3 提供了坚实的事实依据：

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                   Substance 3D Painter 教学价值分离模型                          │
├───────────────────────────────┬──────────────────────────────────────────────────┤
│ 1. 软件手工操作价值           │ **显著下降 / 可大幅压缩**                         │
│    (Manual GUI Operation)     │ - 传统的“从空白图层纯手工刷几百层贴图”耗时过大；  │
│                               │ - 基础底料混合、常规噪波、自动 UV 与批处理导出   │
│                               │   已被 Sampler、生成器与脚本高度接管。           │
├───────────────────────────────┼──────────────────────────────────────────────────┤
│ 2. 3D 空间修订与局部诊断价值  │ **依然极其关键 / 不可替代**                       │
│    (Spatial Revision & QA)    │ - 生成式 AI 输出的贴图是扁平且非结构化的；       │
│                               │ - 当资产在实际光照下出现局部接缝拉伸、法线凹凸反 │
│                               │   转、特定边缘需要补绘磨损时，Painter 是当前唯   │
│                               │   一成熟的“多通道实时非破坏性空间手术刀”。       │
└───────────────────────────────┴──────────────────────────────────────────────────┘
```

---

## 5. Evidence Register (Lane C)

| 证据条目 | 原始权威来源 | 证据类型 | 支撑事实 | 边界限定 |
| :--- | :--- | :--- | :--- | :--- |
| **Painter Layer & Mask Docs** | Adobe Substance 3D Painter Documentation (2026-07/09) | `Vendor Documentation` | 证实多通道独立混合模式、三平面投影与 Fill/Paint 图层堆栈架构 | 确立其多通道非破坏性编辑本质，非单纯 2D 修图 |
| **Anchor Point Architecture** | Substance 3D Painter Official Docs `anchor-points` | `Vendor Documentation` | 证实通过锚点实现底层手绘细节向上层生成器的非破坏性双向联动 | 依赖内部计算架构，不向外部开放通用节点图源码 |
| **Painter Python API** | `substance_painter` Official API Reference | `Vendor API Documentation` | 证实工程创建、贴图烘焙、配置应用与贴图导出可被完全脚本化批处理 | 明确无法通过脚本替代复杂三维曲面手绘交互与叙事微调 |

---
*Lane C Source-Native 提取完成，归档于 `docs/research/source-native/adobe-painter-official.md`。*
