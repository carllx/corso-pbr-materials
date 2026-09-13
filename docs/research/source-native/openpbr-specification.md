# Lane A: OpenPBR Surface Specification — Source-Native Research & Technical Index

> **Artifact Status**: Official Specification Direct Extraction & Technical Index  
> **Source**: Academy Software Foundation (ASWF) / OpenPBR Official Specification  
> **Fixed Release Anchor**: OpenPBR Surface Specification v1.1.1 (Dated 2026-04-17), ASWF Git Tag `v1.1.1`  
> **Official Authors & Contributors** (per Specification Acknowledgements):
> - *Core Authors*: Zap Andersson, Paul Edmondson, Julien Guertault, Adrien Herubel, Alan King, Peter Kutz, Andréa Machizaud, Jamie Portsmouth, Frédéric Servant, Jonathan Stone.
> - *Institutional Sponsors / Development*: Autodesk & Adobe joint initiative under ASWF governance, synthesizing Autodesk Standard Surface and Adobe Standard Material (ASM).
> **Artifact Placement**: `docs/research/source-native/openpbr-specification.md`  

---

## 1. Executive Summary & Purpose

本研究针对 **Lane A: OpenPBR** 进行直接规范提取（Direct Specification Extraction），旨在回答：
1. OpenPBR 定义了什么材质语义？
2. 它的模型边界是什么？
3. 它明确**不负责**什么？
4. 严格区分 `OpenPBR ≠ Graph Language`、`OpenPBR ≠ Asset Format` 与 `OpenPBR ≠ Target-Engine Material Implementation`。
5. 严格区分**一手规范事实（SOURCE FACT）**与**教学研判假说（INTERPRETIVE SUMMARY / GATE 3 HYPOTHESIS — NOT A DECISION）**。

---

## 2. 规范定义与材质语义 (SOURCE FACT)

### 2.1 核心定义与设计意图 (Core Definition & Intent)
根据 OpenPBR Surface Specification v1.1.1 正文引言：
- OpenPBR Surface 是一种面向计算机图形表面着色模型的开放行业规范（"intended as a standard for computer graphics: the OpenPBR Surface model"），设计为一种 **Über-shader（超级着色器）**。
- 目标是能够精确模拟在实际影视视效（VFX）与动画长片制作中绝大多数常见 CG 材质外观（"capable of accurately modeling the vast majority of CG materials used in practical visual effects and feature animation productions"）。
- 该模型是 **Autodesk Standard Surface** 与 **Adobe Standard Material** 模型的综合演进成果。

### 2.2 形式化结构：平板与算子 (Formalism: Slabs & Operators)
OpenPBR 采用物理介质平板（Slabs）及在其上定义的相互作用算子来组织材质模型：
- **平板 (Slab)**：表示介质内部均质、上下界面具有已知 BSDF 的薄层或半无限大体介质 $S = \mathrm{Slab}(f, V)$。
- **混合算子 ($\mathbf{mix}$)**：沿表面切向进行基于权重的凸组合线性混合：
  $$\mathbf{mix}(M_0, M_1, w) \equiv (1-w)M_0 + wM_1$$
- **层叠算子 ($\mathbf{layer}$)**：沿表面法线垂直堆叠，上层介质对下层介质产生光强透射衰减、菲涅尔遮挡及比尔-朗伯定律吸收。

### 2.3 核心层级拓扑树 (Layer Graph)
在非薄壁（Non-thin-walled）常规模式下，OpenPBR 的结构自顶向下由以下平板与算子形式化合成：
```
                       [Emission] (自发光)
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

规范定义的严格形式化表达式：
1. $M_\textrm{glossy-diffuse} = \mathbf{layer}(S_\textrm{diffuse}, S_\textrm{gloss})$
2. $M_\textrm{opaque-base} = \mathbf{mix}(M_\textrm{glossy-diffuse}, S_\textrm{subsurface}, \mathtt{subsurface\_weight})$
3. $M_\textrm{dielectric-base} = \mathbf{mix}(M_\textrm{opaque-base}, S_\textrm{translucent-base}, \mathtt{transmission\_weight})$
4. $M_\textrm{base-substrate} = \mathbf{mix}(M_\textrm{dielectric-base}, S_\textrm{metal}, \mathtt{base\_metalness})$
5. $M_\textrm{coated-base} = \mathbf{layer}(M_\textrm{base-substrate}, S_\textrm{coat}, \mathtt{coat\_weight})$
6. $M_\textrm{surface} = \mathbf{layer}(M_\textrm{coated-base}, S_\textrm{fuzz}, \mathtt{fuzz\_weight})$
7. $M_\textrm{PBR} = \mathbf{mix}(S_\textrm{ambient-medium}, M_\textrm{surface}, \mathtt{geometry\_opacity})$

### 2.4 各物理层参数语义 (Parameter Semantics)
- **Base (底基)**：`base_weight`（权重），`base_color`（RGB 反照率），`base_roughness`（漫反射粗糙度），`base_metalness`（金属度 $[0, 1]$）。
- **Specular (镜面高光)**：`specular_weight`，`specular_color`（高光染色），`specular_roughness`（GGX 微表面粗糙度），`specular_ior`（折射率，默认 $1.5$），`specular_roughness_anisotropy`（高光各向异性）。
- **Transmission (透射)**：`transmission_weight`（透射权重），`transmission_color`，`transmission_depth` / `transmission_scatter`（体积衰减与散射）。
- **Subsurface (次表面散射)**：`subsurface_weight`，`subsurface_color`，`subsurface_radius`（均值自由程 MFP），`subsurface_scatter_anisotropy`（散射相位函数各向异性）。
- **Coat (清漆涂层)**：`coat_weight`，`coat_color`，`coat_roughness`，`coat_ior`（默认 $1.6$）。
- **Fuzz (织物绒毛)**：`fuzz_weight`，`fuzz_color`，`fuzz_roughness`（基于微薄片理论 Microflake Theory）。
- **Thin Film (薄膜干涉)**：`thin_film_weight`，`thin_film_thickness` ($[0, 2000]\,\text{nm}$)，`thin_film_ior`。
- **Emission (自发光)**：`emission_luminance`，`emission_color`。
- **Geometry (几何控制)**：`geometry_opacity`，`geometry_normal`，`geometry_coat_normal`，`geometry_thin_walled`。

---

## 3. 模型边界与明确排除项 (SOURCE FACT)

OpenPBR Specification v1.1.1 正文在 "Historical background and objectives"、"Flexibility of implementation" 与 "Metadata" 章节中对模型边界做出了严格限定：

### 3.1 明确边界三原则 (Three Distinct Boundaries)
1. **OpenPBR $\neq$ Graph Language (非节点图语言)**：
   - OpenPBR 本身是一个**参数化表面着色数学模型与方程规范（Surface Shading Formulation）**，不是类似于 MaterialX Nodegraph、Blender Shader Nodes 或 Unreal Material Graph 的节点连接语言。
   - 规范没有定义节点连线（Connections）、输入输出插槽（Ports）、算术运算节点（Math Nodes）或程序化噪波发生器。
2. **OpenPBR $\neq$ Asset Format (非资产或场景格式)**：
   - OpenPBR 不定义 3D 资产包装、网格几何体绑定、UV 贴图集（UDIM）寻址或纹理文件存储格式。
   - 规范正文（Section "Metadata"）指出：“As in practice OpenPBR will be integrated within data exchange frameworks such as MaterialX and USD, the specific form and content of this metadata is outside the scope of this specification.”（由于实践中 OpenPBR 将集成在如 MaterialX 和 USD 等数据交换框架中，元数据的具体形式和内容超出本规范范围）。规范将此类功能留给数据交换框架，自身不提供资产管理。
3. **OpenPBR $\neq$ Target-Engine Material Implementation (非目标引擎专属实现)**：
   - 规范正文（Section "Flexibility of implementation"）明确指出：“The specification focuses solely on defining the target appearance. The choice of the final BSDF implementation and its associated trade-off is left entirely to the implementer.”（规范仅专注于定义目标外观。最终 BSDF 实现的选择及其权衡完全留给实现者）。
   - 规范不强制要求所有实时或离线渲染器采用完全相同的代码；实现者可依据性能约束采取近似（如混合波瓣近似 Reduction to a mixture of lobes、拆分积分 Split-Integral，甚至在极端受限场景下近似为单 Lambert BRDF）。
   - 规范只定义了理想物理外观与白炉测试（White Furnace Testing）能量守恒基准（$E(\omega_o) + T(\omega_o) \le 1$）。

---

## 4. 解释性总结与教学研判假说 (INTERPRETIVE SUMMARY / GATE 3 HYPOTHESIS — NOT A DECISION)

> [!NOTE]
> 本节内容为基于一手规范形成的教学设计假说，用于为后续 Gate 3 决策提供讨论基础，**不构成当前阶段的最终教学裁决**。

### 4.1 教师参考深度 vs 学生概念价值假说
- **教师参考深度 (Teacher Reference Depth)**：
  - 微表面散射微积分与波瓣还原（BSDF Lobe Reduction）：理解多层介质反射方程如何通过方向反射率积分解耦为独立波瓣。
  - 白炉测试（White Furnace Testing）：作为检验能量守恒与物理自洽性的严格判定准则。
  - 微薄片理论（Microflake Theory）：解释 Fuzz 绒毛层为何脱离标准微表面法线分布（NDF）。
- **面向学生的核心概念价值假说 (Student-Facing Conceptual Hypothesis)**：
  - **通用材质解构心智模型**：学生可借此建立分层分析习惯（底基金属/电介质 $\to$ 透射/次表面 $\to$ 粗糙高光 $\to$ 透明涂层 $\to$ 表面绒毛/薄膜）。
  - **跨 DCC 语义映射参考**：OpenPBR 的参数命名与物理概念为理解现代着色器（如 Blender Principled BSDF、Arnold Standard Surface、Substance ASM 及 Unreal Substrate）提供了标准化的概念对照框架。但由于各引擎实现细节、近似策略与专用扩展不同，**不宜断言所有 DCC 间均能实现绝对无缝的通用理解**。
  - **无需学生手写底层着色代码**：由于规范定位为外观与参数模型，教学价值应聚焦于参数物理机理与诊断直觉，而非编写底层着色器算法。

---

## 5. Evidence Register (Lane A)

| 证据条目 | 原始权威来源 | 证据类型 | 支撑事实 (SOURCE FACT) | 边界限定 (SOURCE FACT) |
| :--- | :--- | :--- | :--- | :--- |
| **OpenPBR Specification v1.1.1** | ASWF GitHub `OpenPBR` (Release Tag: `v1.1.1`, 2026-04-17) | `Technical Specification` | 确立基于 Slab 与 layer/mix 算子的现代标准材质语义，定义 base, coat, fuzz, thin-film, transmission, subsurface 参数层级 | 仅定义外观标准与物理参考方程，不包含节点图实现或资产打包 |
| **Flexibility of Implementation** | OpenPBR Spec Section "Flexibility of implementation" | `Technical Specification` | 证实规范允许不同引擎采用不同精度近似（如 LOD 理念），最终实现选择与权衡完全留给实现者 | 规范不强制单一固定底层代码实现 |
| **Metadata & Scope Boundary** | OpenPBR Spec Section "Metadata" | `Technical Specification` | 确认元数据与资产存储超出规范范围，实践中通过外部数据交换框架（如 MaterialX 与 USD）集成 | 证明 OpenPBR $\neq$ Graph Language $\neq$ Asset Format |

---
*Lane A Source-Native 提取校准完成，归档于 `docs/research/source-native/openpbr-specification.md`。*
