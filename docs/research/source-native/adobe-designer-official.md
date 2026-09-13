# Lane D: Adobe Substance 3D Designer — Source-Native Research & Technical Index

> **Artifact Status**: Official Documentation Direct Extraction & Technical Index  
> **Primary Sources**:
> 1. Adobe Substance 3D Designer User Guide (`substance3d.adobe.com/documentation/sddoc/`, Updated 2026-09-11)
> 2. Adobe Substance 3D Designer Python API Reference (`sd.api` / Substance Automation Toolkit documentation)
> 3. Zeeshan Jawed Shah (2022) Chapters 7–10 (Verified hands-on execution baseline in `source-native-knowledge-index.md`)
> **Artifact Placement**: `docs/research/source-native/adobe-designer-official.md`  

---

## 1. Executive Summary & Purpose

本研究针对 **Lane D: Substance 3D Designer** 进行技术解构，重点回答：
1. 程序化节点图架构（Procedural Graph）与参数化系统（Parametric Systems）；
2. 有意义的参数暴露（Meaningful Exposed Controls）与资产复用机制；
3. SBS（源工程文件）与 SBSAR（分发资产包）的工业界限及宿主集成方式；
4. Python 脚本与 Substance Automation Toolkit (SAT) 的自动化覆盖范围；
5. 严格区分**一手官方事实（SOURCE FACT）**与**教学研判假说（INTERPRETIVE SUMMARY / GATE 3 HYPOTHESIS — NOT A DECISION）**。

---

## 2. 核心架构与程序化系统 (SOURCE FACT)

Substance 3D Designer 是基于数学函数与图像算子的程序化纹理合成环境：

### 2.1 程序化图表与数据类型 (Compositing Graphs & Data Types)
- **图像分辨率独立性 (Relative to Parent Resolution)**：
  - 节点的输出尺寸默认采用 `Relative to Parent`，动态继承父级图表或宿主环境指定的渲染尺寸（如 $256 \times 256$ 到 $4096 \times 4096$）。
  - 特点：图表逻辑自身与特定位图分辨率解耦，允许在分发端动态缩放。
- **数据流与通道分离 (Grayscale vs. Color)**：
  - 严格区分灰度图（Grayscale，单通道）与彩色图（Color，RGBA）。
  - 灰度算子常用于高度（Height）、粗糙度（Roughness）、金属度（Metallic）与混合蒙版；彩色算子负责底色（Base Color）与法线（Normal）运算。

### 2.2 原子节点与算法重现性 (Atomic Nodes & Reproducibility)
- **核心原子算子体系 (Atomic Nodes)**：
  - `Blend`：多图层数学混合（Add, Multiply, Overlay, Max, Min 等，带不透明度控制）。
  - `Transformation 2D`：坐标平移、旋转、缩放与平铺寻址（Wrap Modes）。
  - `Curve / Levels / Histogram Scan`：灰度数值区间重映射与直方图对比度调整。
  - `Warp / Directional Warp`：利用一张灰度梯度图驱动采样偏移，产生扭曲或侵蚀形态。
  - `Tile Sampler / Tile Generator`：基于图案图元阵列排布。
- **算法计算的重现性 (Procedural Reproducibility)**：
  - 在固定参数、相同输入数据与指定随机种子（Random Seed）下，图表计算过程遵循确定的程序化数学公式。

### 2.3 参数暴露与接口设计 (Exposed Controls & Interface Design)
- **参数暴露机制 (Expose Parameters)**：
  - 节点内部属性（如图案数量、磨损强度、颜色、粗糙度偏移）可被提升并暴露为图表级参数（Graph Parameters）。
  - 暴露参数可配置标签（Label）、分组（Group）、数据类型（Float, Integer, Boolean, Color）、默认值以及数值区间（Min/Max/Step）。
- **函数图（Function Graphs）驱动高级逻辑**：
  - 暴露参数不仅是静态常量，还可通过内嵌函数图（数学运算符、条件分支逻辑）驱动内部多个节点参数联动。

### 2.4 资产交付格式与集成边界：SBS vs. SBSAR (File Formats & Integration Boundaries)
- **`.sbs` (Substance 3D File / Source Project)**：
  - 基于 XML 结构的源工程文件，包含完整的节点连接网络、图表依赖关系与外部资源引用，供艺术家在 Designer 中进行创作、检查与编辑。
- **`.sbsar` (Substance 3D Asset File / Archive)**：
  - **编译分发包**：通过 Substance 编译器生成的只读归档文件，封装了优化后的算法指令与暴露的参数接口，不直接暴露原始编辑图表拓扑。
  - **宿主集成方式 (Host Integration Boundary)**：
    - SBSAR 文件可在 Substance 原生软件（如 Painter, Sampler）中直接加载；
    - 在第三方外部软件（如 Unreal Engine, Unity, Blender, Maya, 3ds Max）中，SBSAR 是**通过专用的 Substance 插件或官方集成的运行时引擎（Substance Engine Plugin / Runtime）进行解析和参数交互**，而非所有第三方工具的底层完全原生原生内置支持。

---

## 3. 自动化与 API 覆盖边界 (SOURCE FACT)

### 3.1 Python API (`sd.api`) 与 Substance Automation Toolkit (SAT)
- **内嵌 Python API (`sd.api`)**：
  - 支持程序化创建图表（`createGraph()`）；
  - 支持程序化实例化节点与属性赋值（`createNode()`, `setInputPropertyValue()`）；
  - 支持程序化连线（`connect()`）与节点自动排版。
- **Substance Automation Toolkit (SAT 命令行工具集)**：
  - `sbscooker`：在无 GUI 环境下将 `.sbs` 工程文件批处理编译为 `.sbsar`；
  - `sbsrender`：在命令行或后台利用 `.sbsar` 渲染并导出指定参数组合的位图贴图；
  - `sbsmutator`：在脱机状态下程序化批量替换图表内的输入贴图或调整参数默认值。

---

## 4. 解释性总结与教学研判假说 (INTERPRETIVE SUMMARY / GATE 3 HYPOTHESIS — NOT A DECISION)

> [!NOTE]
> 本节内容为基于一手文档形成的教学设计假说，用于为后续 Gate 3 决策提供讨论基础，**不构成当前阶段的最终教学裁决**。

### 4.1 程序化思维与手工连线熟练度分离假说
- **程序化系统理解价值假说 (Procedural Literacy Hypothesis)**：
  - 理解参数暴露、父级相对分辨率、数学混合及“以高度/轮廓驱动派生全通道贴图（Height-driven derivation）”的结构化逻辑，对培养学生严谨的数字材质心智模型具有较高潜在价值。
  - 掌握将材质封装为带交互接口的资产包（SBSAR）思想，有助于理解工业生产中材质库的规范化复用。
- **手动连线熟练度权重假说 (Manual Graph Proficiency Weight Hypothesis)**：
  - 熟练手工搭建包含上百个原子节点的高度复杂自定义图表，需要深入的数学噪波混合技巧，在生产中常为专门的技术艺术家（TA）技能。
  - 对于本科阶段宽口径的 8 周材质课程，是否需将大量学时投入于训练手工连接复杂节点图，抑或应以理解核心逻辑与受限实操（Bounded Hands-on）为主，是 Gate 3 需要审慎权衡的假说。

---

## 5. Evidence Register (Lane D)

| 证据条目 | 原始权威来源 | 证据类型 | 支撑事实 (SOURCE FACT) | 边界限定 (SOURCE FACT) |
| :--- | :--- | :--- | :--- | :--- |
| **Designer Graph & Format Docs** | Substance 3D Designer User Guide (2026-09-11) | `Vendor Documentation` | 证实 Relative to Parent 分辨率机制，区分开发态 XML 工程（SBS）与编译分发态归档（SBSAR） | 明确 SBSAR 在第三方 DCC/引擎中依赖专用插件或运行时引擎集成 |
| **Parameter Exposure Mechanics** | Designer Docs `values-in-substance-compositing-graphs` | `Vendor Documentation` | 证实参数暴露（Expose Parameters）与函数图驱动机制，构建面向宿主软件的调参接口 | 属于资产接口设计层级，不改变底层原子节点公式 |
| **Substance Automation Toolkit** | Adobe SAT & `sd.api` Official Reference | `Vendor Developer Docs` | 证实通过 Python 与 CLI 工具（sbscooker, sbsrender, sbsmutator）可实现完整的脱机批处理图表创建、编译与贴图烘焙 | 证明其具备一流的 Pipeline 嵌入度，但面向管线开发而非单纯手绘创作 |

---
*Lane D Source-Native 提取校准完成，归档于 `docs/research/source-native/adobe-designer-official.md`。*
