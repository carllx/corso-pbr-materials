# Lane A: OpenPBR Surface Specification — Source-Native Research & Technical Index

> **Artifact Status**: Official Specification Direct Extraction & Technical Index  
> **Source**: Academy Software Foundation (ASWF) / OpenPBR GitHub Repository & Specification  
> **Version & Date**: OpenPBR Surface Specification v1.1.1 (2026-04-17) / GitHub `AcademySoftwareFoundation/OpenPBR` (Release Tag: `v1.1.1`)  
> **Authors / Contributors**: Autodesk & Adobe joint development (Luca Fascione, Emmanuel Turquin, Petr Kmoch, et al., synthesizing Autodesk Standard Surface and Adobe Standard Material)  
> **Artifact Placement**: `docs/research/source-native/openpbr-specification.md`  

---

## 1. Executive Summary & Purpose

本研究针对 **Lane A: OpenPBR** 进行直接规范提取（Direct Specification Extraction），旨在回答：
1. OpenPBR 定义了什么材质语义？
2. 它的模型边界是什么？
3. 它明确**不负责**什么？
4. 区分 `OpenPBR ≠ Graph Language`、`OpenPBR ≠ Asset Format` 与 `OpenPBR ≠ Target-Engine Material Implementation`。
5. 区分教师参考深度（Teacher Reference Depth）与面向学生的核心概念价值（Student-Facing Conceptual Value）。

---

## 2. 规范定义与材质语义 (Material Semantics)

### 2.1 核心定义 (Core Definition)
OpenPBR Surface 是一种面向计算机图形表面着色模型的开放工业规范（"intended as a standard for computer graphics: the OpenPBR Surface model"），设计为一种 **Über-shader（超级着色器）**。它的目标是能够精确模拟影视视效（VFX）与动画长片制作中绝大多数 CG 材质表面外观，是 **Autodesk Standard Surface** 与 **Adobe Standard Material (ASM)** 的官方合成与演进标准。

### 2.2 形式化结构：平板与算子 (Formalism: Slabs & Operators)
OpenPBR 采用物理介质平板（Slabs）及在其上定义的相互作用算子来组织材质模型：
- **平板 (Slab)**：表示介质内部均质、上下界面具有特定 BSDF 的薄层或半无限大体介质 $S = \mathrm{Slab}(f, V)$。
- **混合算子 ($\mathbf{mix}$)**：沿表面切向进行基于权重的凸组合线性混合，$\mathbf{mix}(M_0, M_1, w) = (1-w)M_0 + wM_1$。
- **层叠算子 ($\mathbf{layer}$)**：沿表面法线垂直堆叠，上层介质对下层介质产生光强透射衰减、菲涅尔遮挡及比尔-朗伯定律吸收。

### 2.3 核心层级拓扑树 (Layer Graph & Shading Components)
在非薄壁（Non-thin-walled）常规模式下，OpenPBR 的结构自顶向下由以下平板构成：
```
                       [Emission] (发光)
                           ^
[Ambient Medium]           |
+--------------------------|----------------------------------------------------+
|                          |                   fuzz (绒毛层)                    |
+--------------------------|----------------------------------------------------+
|                          |                   coat (透明涂层)                  |
+--------------------------+---------------------+-------------------+----------+ <-- thin-film (薄膜干涉)
|                          |                     |                   |          |
|                          |                     |                   |  gloss   |
|         metal            |  translucent base   |    subsurface     | (高光)   |
|        (导体)            |    (透光介质/玻璃)  |  (次表面散射体)   +----------+
|                          |                     |                   | diffuse  |
|                          |                     |                   | (漫反射) |
+--------------------------+---------------------+-------------------+----------+
```

模型形式化合成公式：
1. $M_\textrm{glossy-diffuse} = \mathbf{layer}(S_\textrm{diffuse}, S_\textrm{gloss})$
2. $M_\textrm{opaque-base} = \mathbf{mix}(M_\textrm{glossy-diffuse}, S_\textrm{subsurface}, \mathtt{subsurface\_weight})$
3. $M_\textrm{dielectric-base} = \mathbf{mix}(M_\textrm{opaque-base}, S_\textrm{translucent-base}, \mathtt{transmission\_weight})$
4. $M_\textrm{base-substrate} = \mathbf{mix}(M_\textrm{dielectric-base}, S_\textrm{metal}, \mathtt{base\_metalness})$
5. $M_\textrm{coated-base} = \mathbf{layer}(M_\textrm{base-substrate}, S_\textrm{coat}, \mathtt{coat\_weight})$
6. $M_\textrm{surface} = \mathbf{layer}(M_\textrm{coated-base}, S_\textrm{fuzz}, \mathtt{fuzz\_weight})$
7. $M_\textrm{PBR} = \mathbf{mix}(S_\textrm{ambient-medium}, M_\textrm{surface}, \mathtt{geometry\_opacity})$

### 2.4 各物理层参数语义 (Detailed Parameter Semantics)
- **Base (底基)**：
  - `base_weight`：底色漫反射/基础能量权重 $[0, 1]$。
  - `base_color`：底色反照率（Albedo / Diffuse Reflectance，RGB）。
  - `base_roughness`：漫反射微表面粗糙度（Oren-Nayar 散射模型拓展）。
  - `base_metalness`：金属度 $[0, 1]$，在电介质与导体之间线性混合。
- **Specular (镜面高光反射)**：
  - `specular_weight`：镜面反射权重 $[0, 1]$。
  - `specular_color`：高光染色（默认白色 $(1,1,1)$，电介质高光通常不带颜色）。
  - `specular_roughness`：微表面粗糙度 $[0, 1]$（GGX NDF 分布）。
  - `specular_ior`：折射率（Index of Refraction，电介质基础默认 $1.5$）。
  - `specular_roughness_anisotropy`：高光各向异性程度 $[0, 1]$。
- **Transmission (透射与折射)**：
  - `transmission_weight`：透射权重 $[0, 1]$（控制玻璃/透明流体）。
  - `transmission_color`：透射穿透色彩。
  - `transmission_depth` / `transmission_scatter`：体积吸收与散射参数。
- **Subsurface (次表面散射)**：
  - `subsurface_weight`：次表面散射混合权重 $[0, 1]$。
  - `subsurface_color` / `subsurface_radius`：散射均值自由程（Mean Free Path, MFP）与穿透距离。
  - `subsurface_scatter_anisotropy`：散射相位函数各向异性（Henyey-Greenstein 相位）。
- **Coat (清漆涂层)**：
  - `coat_weight`：清漆层权重 $[0, 1]$。
  - `coat_color`：清漆层比尔-朗伯吸收染色。
  - `coat_roughness`：清漆独立微表面粗糙度。
  - `coat_ior`：清漆层折射率（默认 $1.6$）。
- **Fuzz (织物绒毛层)**：
  - `fuzz_weight`：绒毛层权重 $[0, 1]$。
  - `fuzz_color`：微纤维散射反照率。
  - `fuzz_roughness`：基于微薄片理论（Microflake Theory）的纤维朝向发散度。
- **Thin Film (薄膜干涉)**：
  - `thin_film_weight`：薄膜层干涉权重 $[0, 1]$。
  - `thin_film_thickness`：纳米级薄膜厚度 $[0, 2000]\,\text{nm}$。
  - `thin_film_ior`：薄膜折射率。
- **Emission (自发光)**：
  - `emission_luminance` / `emission_color`：位于 coat 与 fuzz 层之下发射的光通量辐射度。
- **Geometry (几何控制)**：
  - `geometry_opacity`：整体裁切透空度。
  - `geometry_normal` / `geometry_coat_normal`：底基与涂层的独立切线空间法线。
  - `geometry_thin_walled`：薄壁模式布尔开关（叶片、纸张、气泡）。

---

## 3. 模型边界与明确排除项 (Model Boundary & What It Does NOT Provide)

规范正文在“Historical background and objectives”、“Flexibility of implementation”及“Metadata”章节中，对边界做出了严格的技术限定：

### 3.1 明确边界三原则 (Three Distinct Non-Equivalences)
1. **OpenPBR $\neq$ Graph Language (非节点图语言)**：
   - OpenPBR 本身是一个**参数化着色数学模型与方程规范（Parametric Shading Formulation）**，不是类似于 MaterialX Nodegraph、Blender Shader Nodes、Unreal Material Graph 的“节点连接语言”。
   - 它没有定义节点连线（Connections）、输入输出插槽（Ports）、算术运算节点（Math Nodes）或程序化噪波生成器。
2. **OpenPBR $\neq$ Asset Format (非资产或场景格式)**：
   - OpenPBR 不负责定义 3D 资产包装、网格几何体绑定（Geometry Binding）、UV 贴图集（UDIM）寻址、纹理文件引用的物理存储格式。
   - 规范正文明确指出：数据交换、元数据与场景资产引用依赖外部框架，如 **MaterialX** 与 **OpenUSD (UsdShade)**。
3. **OpenPBR $\neq$ Target-Engine Material Implementation (非目标引擎专属实现)**：
   - 规范正文明确说明：“The specification focuses solely on defining the target appearance. The choice of the final BSDF implementation and its associated trade-off is left entirely to the implementer.”
   - 规范不强制要求某个实时渲染器或离线路径追踪器必须采用完全相同的着色代码；实现者可以采用混合波瓣近似（Reduction to a mixture of lobes）、拆分积分（Split-Integral）、甚至极端情况下降级为单 Lambert BRDF（LOD 理念）。
   - 规范只定义了物理外观基准和白炉测试（White Furnace Testing）能量守恒检验准则。

### 3.2 OpenPBR 明确不包含的内容清单
- ❌ **不包含可编辑的创作图层历史 (Authoring History / Layers / Masks)**：没有类似 Substance 3D Painter 的图层混合栈、蒙版链、笔刷手绘数据。
- ❌ **不包含程序化纹理生成逻辑 (Procedural Generation Logic)**：没有类似 Substance 3D Designer 的图案平铺、SDF 混合或噪波算法。
- ❌ **不包含运行时着色器性能与变体策略 (Runtime Performance & Shader Permutations)**：不管理 Draw Call、Shader Keywords、GBuffer 打包格式（如 ORM / BC7）或平台着色器常数缓冲。

---

## 4. 教师参考深度 vs. 学生核心概念价值

### 4.1 教师参考深度 (Teacher Reference Depth)
- **微表面散射微积分与波瓣还原 (BSDF Lobe Reduction)**：理解多层介质反射方程如何通过方向反射率积分 $E(\omega_o) = \int_{\mathcal{H}_+} f(\omega_i, \omega_o)\,\mathrm{d}\omega^\perp_i$ 近似解耦为独立 Specular, Diffuse, Coat 波瓣。
- **白炉测试 (White Furnace Testing)**：理解物理能量守恒的严格判定标准——在各向同性全白辐射度环境下，任何微表面粗糙度、各向异性或薄膜参数下的整体反照率均不得超过 1.0（$E + T \le 1$）。
- **微薄片理论 (Microflake Theory)**：理解 Fuzz 绒毛层为何脱离标准微表面法线分布（NDF），改用体积定向微薄片散射模型。

### 4.2 学生核心概念价值 (Student-Facing Conceptual Value)
- **通用材质解构心智模型 (Universal Material Decomposition)**：
  - 任何现实复杂材质都可以被结构化拆解为：**基底（金属 vs 绝缘体）$\to$ 次表面散射/透射 $\to$ 表面高光粗糙度 $\to$ 透明涂层（Clearcoat）$\to$ 微绒毛（Fuzz）$\to$ 几何法线/薄膜**。
- **标准参数语义通用性 (Semantic Consistency Across DCCs)**：
  - 学生学懂 OpenPBR 的参数命名与物理意义，就能无缝迁移理解 Blender 4.x/5.x 的 Principled BSDF v2、Autodesk Arnold 的 Standard Surface、Substance 3D 的 Adobe Standard Material 以及 Unreal Engine 5 的 Substrate 框架。
  - **不需要强迫学生手动编写 OpenPBR 着色器代码**，重点是掌握这套参数语义背后的物理机理与诊断直觉。

---

## 5. Evidence Register (Lane A)

| 证据条目 | 原始权威来源 | 证据类型 | 支撑事实 | 边界限定 |
| :--- | :--- | :--- | :--- | :--- |
| **OpenPBR Specification v1.1.1** | ASWF GitHub `OpenPBR/documents/` (2026-04-17) | `Technical Specification` | 确立基于 Slab 与 layer/mix 算子的现代标准材质语义，包含 base, coat, fuzz, thin-film, transmission, subsurface | 仅定义外观标准与物理参考方程，不包含节点图实现或资产打包 |
| **Flexibility of Implementation** | OpenPBR Spec Section "Flexibility of implementation" | `Technical Specification` | 证实规范允许不同引擎采用不同精度近似（如 LOD 理念），甚至极端情况降级为单 Lambert | 证明规范不是强制单一底层代码实现 |
| **Metadata & Framework Boundary** | OpenPBR Spec Section "Metadata" | `Technical Specification` | 明确指出元数据、资产存储与数据交换属于 MaterialX 与 USD 的职责范围 | 证明 OpenPBR $\neq$ Graph Language $\neq$ Asset Format |

---
*Lane A Source-Native 提取完成，归档于 `docs/research/source-native/openpbr-specification.md`。*
