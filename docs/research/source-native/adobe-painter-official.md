# Lane C: Adobe Substance 3D Painter — Source-Native Research & Technical Index

> **Artifact Status**: Official Documentation & API Reference Direct Extraction  
> **Primary Sources**:
> 1. Adobe Substance 3D Painter Official Documentation (`helpx.adobe.com/substance-3d-painter/`, `substance3d.adobe.com/documentation/spdoc/`, Updated 2026-07/2026-09)
> 2. Adobe Substance 3D Painter Python API Reference (`substance_painter` module documentation)
> 3. Zeeshan Jawed Shah (2022) Chapters 1–6 (Verified hands-on execution baseline in `source-native-knowledge-index.md`)
> **Artifact Placement**: `docs/research/source-native/adobe-painter-official.md`  

---

## 1. Executive Summary & Purpose

本研究针对 **Lane C: Substance 3D Painter** 进行技术解构，重点回答：
1. 3D 空间与局部修订机制（3D Spatial & Local Revision）；
2. 图层、蒙版、锚点（Anchor Points）与图层依赖关系（Layer Dependencies）；
3. 跨通道同步编辑（Cross-Channel Editing）与物理烘焙贴图驱动机制；
4. Python API 与工作流自动化覆盖边界（Automation Boundary）；
5. 严格区分**一手官方事实（SOURCE FACT）**与**教学研判假说（INTERPRETIVE SUMMARY / GATE 3 HYPOTHESIS — NOT A DECISION）**。

---

## 2. 核心架构与空间修订机制 (SOURCE FACT)

Substance 3D Painter 在数字材质管线中的能力建立在**以多边形网格拓扑为基础的多通道三维空间投影与非破坏性分层计算架构**上：

### 2.1 3D/2D 视口与视差投影 (Viewport & Projections)
- **投射模式 (Fill Projection Modes)**：
  - `UV Projection`：基于网格 UV 坐标进行贴图采样。
  - `Tri-planar Projection`（三平面投射）：沿网格几何空间 X, Y, Z 三轴投射，带有可调的过渡硬度（Hardness），用于在复杂曲面或接缝处消除拉伸。
  - `Planar / Spherical / Cylindrical / Warp`：视口操纵器驱动的定向三维投影，支持深度剔除（Depth Culling）与背面剔除（Backface Culling），限制投射厚度与法线夹角。
- **2D/3D 联动视口**：支持分屏同步查看 3D 网格着色与 2D UV 瓦片展开形态。

### 2.2 图层堆栈与多通道同步 (Layer Stack & Multi-Channel Evaluation)
- **非破坏性图层类型**：
  - `Fill Layer`（填充图层）：由参数（颜色、粗糙度、外部纹理输入）全局驱动，分辨率无损，支持在工程生命周期内随时切换贴图工作分辨率（如 1K $\leftrightarrow$ 4K）。
  - `Paint Layer`（绘制图层）：存储笔刷在局部空间涂抹的像素数据。
- **多通道同时求值 (Multi-Channel Evaluation)**：
  - 单个图层或笔刷可同时激活并向多个通道写入数据：Base Color、Roughness、Metallic、Normal、Height、Emissive、Opacity 等。
  - 各通道拥有**独立的混合模式（Blending Mode）与透明度控制**（例如同一图层在 Base Color 采用 Normal 模式，在 Height 采用 Linear Dodge/Add 模式，在 Roughness 采用 Multiply 模式）。

### 2.3 遮罩体系与锚点单向引用依赖 (Masks & Anchor Point Dependencies)
- **遮罩堆栈 (Mask Stacks)**：
  - 允许在同一个蒙版下叠加多种效果算子：`Add Generator`（几何驱动生成器）、`Add Fill`（噪波填充）、`Add Paint`（手工笔刷修饰）、`Add Levels`（灰度阈值调整）、`Add Filter`（模糊/滤镜）。
- **锚点系统 (Anchor Points) 的依赖模型**：
  - 官方文档对 Anchor Points 的定义为：**单向层级引用与数据暴露机制（Directional Reference Model）**。
  - 艺术家可以将图层堆栈中处于较低位置的图层、蒙版或特定通道信息注册为一个“锚点”（Anchor Point）。
  - 堆栈中处于较高位置的图层或遮罩效果（如通过 `Add fill` 或 `Generator` 的输入端口），可以引用该低层锚点的数据。
  - **更新机制**：当底层的源数据（如手绘细节或高度图案）发生修改时，所有引用了该锚点的上层效果会依据依赖关系重新求值并更新。但依赖是单向由下至上引用的，**并非双向任意循环图依赖**。

### 2.4 网格贴图烘焙驱动 (Baking-Driven Workflows)
- 智能材质（Smart Materials）与生成器（Generators）依赖基于 GPU 射线投射烘焙的网格几何贴图：
  - **Curvature (曲率图)**：区分边缘凸起与凹陷缝隙；
  - **Ambient Occlusion (环境遮挡图)**：标识几何体深层闭塞；
  - **Position (空间位置图)**：提供三维世界坐标（常用于 Y 轴重力沉降效果）；
  - **World Space Normal / Thickness**：提供宏观法线朝向与半透光厚度。

---

## 3. Python API 与自动化覆盖边界 (SOURCE FACT)

Substance 3D Painter 提供了官方 Python 模块 `substance_painter`：

### 3.1 经官方文档验证的 API 自动化能力
- **工程管理与文件 I/O (Project Lifecycle)**：
  - 支持通过脚本创建工程、打开工程、保存工程、另存以及关闭工程；
  - 支持查询当前工程状态与网格文件路径。
- **资源导入与管理 (Resource Management)**：
  - 支持通过脚本将外部位图贴图、自定义网格导入至 Shelf / Assets 资产库，并指定其作用范围（Session, Project, Shelf）。
- **烘焙自动化 (Baking Automation)**：
  - 支持通过 API 配置烘焙参数、设置 By Mesh Name 命名匹配、触发 Texture Set 的全套网格贴图批处理烘焙。
- **贴图导出 (Export Automation)**：
  - 支持枚举 Texture Sets、应用指定的 Export Preset（导出预设）、批量导出不同分辨率与位深度的 PBR 贴图集。

### 3.2 自动化能力边界 (Documented API Boundaries)
- **无交互式笔刷模拟 API**：在已审阅的官方 `substance_painter` API 文档中，**未发现可用于通过代码模拟压感画笔笔触轨迹、视口涂抹（Smudge）或克隆图章（Clone）操作的公开 API**。
- **自动化范围定位**：官方 Python API 主要面向管线集成、工程批处理设置、烘焙与导出流程自动化，不面向替代实时视口手工交互绘制。

---

## 4. 解释性总结与教学研判假说 (INTERPRETIVE SUMMARY / GATE 3 HYPOTHESIS — NOT A DECISION)

> [!NOTE]
> 本节内容为基于一手文档形成的教学设计假说，用于为后续 Gate 3 决策提供讨论基础，**不构成当前阶段的最终教学裁决**。

### 4.1 教学价值分离假说 (Teaching Value Separation Hypothesis)
- **GUI 手工重复操作价值假说**：
  - 传统教学中耗费大量课时从空白图层手工涂抹基础噪波、手动摆放材质底料的训练方式，受程序化与生成式工具冲击，其边际教学收益可能呈下降趋势。
- **3D 空间修订与局部诊断价值假说**：
  - 扁平生成的 2D PBR 贴图在贴合复杂网格时常面临 UV 接缝拉伸、法线凹凸朝向反转等几何失配问题。
  - Substance 3D Painter 具备以三维几何体为依托的实时多通道视口与分层遮罩能力，在作为资产“局部精确修补、接缝消除与艺术终审平台”方面具有显著的工作流价值。
  - *注：Mari、Substance Designer 或特定 DCC 着色器网络同样具备空间着色能力，不宜将 Painter 绝对断言为行业“唯一”成熟环境，但其作为成熟交互环境的代表性得到广泛认可。*

---

## 5. Evidence Register (Lane C)

| 证据条目 | 原始权威来源 | 证据类型 | 支撑事实 (SOURCE FACT) | 边界限定 (SOURCE FACT) |
| :--- | :--- | :--- | :--- | :--- |
| **Painter Layer & Mask Docs** | Adobe Substance 3D Painter Documentation (2026-07/09) | `Vendor Documentation` | 证实多通道独立混合模式、三平面投影与 Fill/Paint 图层堆栈架构 | 确立其多通道非破坏性编辑架构 |
| **Anchor Point Architecture** | Substance 3D Painter Official Docs `anchor-points` | `Vendor Documentation` | 证实锚点为由下至上的单向数据暴露与引用机制，底层更新驱动上层效果重算 | 依赖堆栈先后顺序，非无向自由循环图 |
| **Painter Python API** | `substance_painter` Official API Reference | `Vendor API Documentation` | 证实工程管理、资产导入、网格贴图烘焙与纹理导出具备完整的脚本化批处理接口 | 在审阅文档中未发现模拟视口笔刷轨迹与手绘修饰的公开 API |

---
*Lane C Source-Native 提取校准完成，归档于 `docs/research/source-native/adobe-painter-official.md`。*
