# Lane F: Blender — Programmable Material Validation Environment — Source-Native Research & Technical Index

> **Artifact Status**: Official Documentation & API Reference Direct Extraction  
> **Primary Sources**:
> 1. Blender 5.2 LTS Official Manual (`docs.blender.org/manual/en/latest/`, Principled BSDF & Shader Nodes)
> 2. Blender Python API Documentation (`docs.blender.org/api/current/`, `bpy.data.materials`, `bpy.ops.render`)
> 3. Blender Command-Line Arguments Reference (`docs.blender.org/manual/en/latest/advanced/command_line/`)
> **Artifact Placement**: `docs/research/source-native/blender-official.md`  

---

## 1. Executive Summary & Purpose

本研究针对 **Lane F: Blender** 进行精准收口的材质技术解构，重点回答：
1. 现代材质节点架构（Shader Nodes）与 Principled BSDF 规范演进；
2. Python API、脚本化无头运行（Scripted / Headless Validation）与场景/相机/渲染管线能力；
3. 严格区分**一手官方事实（SOURCE FACT）**与**教学研判假说（INTERPRETIVE SUMMARY / GATE 3 HYPOTHESIS — NOT A DECISION）**；
4. 明确非目标：不扩展为 Blender 综合建模、绑定或通识全流程研究。

---

## 2. 材质体系与 Principled BSDF 规范演进 (SOURCE FACT)

### 2.1 现代 Principled BSDF 核心架构 (OpenPBR Alignment)
Blender 官方手册在 Principled BSDF 章节中对其物理着色模型做出了明确说明：
- **规范对齐声明**：
  - 官方文档明确指出：“**It is based on the OpenPBR Surface shading model**, and provides parameters compatible with similar PBR shaders found in other software, such as the Disney and Standard Surface models.”（它基于 OpenPBR Surface 着色模型，并提供与其它软件中类似 PBR 着色器兼容的参数）。
  - 支持将外部软件（如 Substance 3D Painter）烘焙或绘制的贴图直接连接到对应输入槽。
- **物理层级组织 (Layered Components)**：
  - **Base Layer**：Metal（导体纯反射）、Diffuse（全漫反射）、Subsurface（次表面体积散射）与 Transmission（透光折射）的分量混合。
  - **Specular Layer**：电介质菲涅尔基础高光反射，由 IOR 与 Roughness 控制。
  - **Thin Film Layer**：位于基底之上的薄膜干涉层，支持物理厚度（Thickness，纳米级）与 IOR 设置，用于呈现肥皂泡、氧化金属等彩虹色。
  - **Coat Layer**：位于基础层之上的独立透明涂层，具备独立的粗糙度与法线输入。
  - **Sheen Layer**：位于顶层的微纤维散射层，模拟布料边缘的光泽。
  - **Emission**：光线从 Coat 与 Sheen 层下方发射，用于模拟带涂层或积灰的发光表面。
  - **Thin Wall Mode (薄壁模式)**：布尔开关，用于无体积厚度的几何面（如树叶、纸张），在基底两侧镜像层级并假设厚度为零。

### 2.2 材质节点网络与色彩管理 (Shader Nodes & Color Space)
- **节点灵活性**：
  - 支持多坐标系输入（`Texture Coordinate`：Generated, Normal, UV, Object, Camera, Window, Reflection）；
  - 支持向量运算与色彩重映射（`Mapping`, `Vector Math`, `ColorRamp`, `Map Range`）；
  - 支持直接读取顶点几何属性（`Color Attribute`, `Attribute`）。
- **色彩空间绑定**：每个图像纹理节点（`ShaderNodeTexImage`）可显式指定色彩空间（如 `sRGB` 用于颜色，`Non-Color` 用于法线、粗糙度、金属度等数据贴图）。

---

## 3. 可编程与无头验证能力 (SOURCE FACT)

Blender 具备完全开源、免商业授权费用（GPL 协议）与完整 Python 绑定的特征：

### 3.1 脚本化自动化核心能力 (Python `bpy` Module)
通过标准 Python 脚本可控制材质创建与渲染：
1. **程序化材质节点构建与连线**：
   - 可通过 `bpy.data.materials.new()`、`node_tree.nodes.new()` 与 `node_tree.links.new()` 动态创建着色网络并建立连接。
2. **色彩空间自动化约束**：
   - 可通过脚本直接将数据贴图强制指定为 `Non-Color`，例如：
     ```python
     tex_node.image.colorspace_settings.name = "Non-Color"
     ```
3. **测试场景编排与渲染执行**：
   - 脚本可自动化创建包含标准色彩校准板（Macbeth Color Chart）与镜面反射球的测试场景；
   - 支持自动化配置 HDRI 环境贴图或多角度定向光源；
   - 脚本可直接调度 Cycles（物理光线追踪）或 EEVEE-Next（实时光栅化）渲染器，并将渲染输出保存至指定路径：
     ```python
     bpy.context.scene.render.engine = "CYCLES"
     bpy.ops.render.render(write_still=True)
     ```

### 3.2 命令行后台无头运行 (Headless CLI Execution)
官方手册命令行参数明确支持：
- `blender -b [file.blend] -P [script.py] -o [output_path] -f [frame_number]`
  - `-b, --background`：在后台运行，不弹出任何 GUI 窗口，不依赖桌面显示服务；
  - `-P, --python <filename>`：启动后自动执行指定的 Python 脚本；
  - `-f, --render-frame <frame>`：渲染指定帧并退出。
- **环境特性**：支持在无桌面环境的本地终端、服务器或容器中执行批处理测试脚本。

---

## 4. 解释性总结与教学研判假说 (INTERPRETIVE SUMMARY / GATE 3 HYPOTHESIS — NOT A DECISION)

> [!NOTE]
> 本节内容为基于一手文档形成的教学设计假说，用于为后续 Gate 3 决策提供讨论基础，**不构成当前阶段的最终教学裁决**。

### 4.1 教学定位假说：可编程验证环境 (Programmable Validation Hypothesis)
- **非通识课假说**：
  - 本课程不宜将 Blender 办成涵盖建模、雕刻、骨骼绑定与角色动画的大全式通识课，避免分散材质核心精力。
- **作为实验验证沙盒的潜力假说**：
  - 鉴于其 Principled BSDF 对齐 OpenPBR 规范，且具备完整的 Python 脚本与无头运行能力，Blender 具备作为**“可编程材质验证环境（Programmable Material Validation Sandbox）”**的技术潜力；
  - 学生或自动化脚本可将导出的 PBR 贴图输入 Blender，在标准打光与相机下自动渲染 Cycles/EEVEE 图像，进行物理正确性核查；
  - 这一机制是否适合引入本科 8 周课程、如何控制脚本环境复杂度与学生学习负荷，属于 Gate 3 需要具体研判的假说。

---

## 5. Evidence Register (Lane F)

| 证据条目 | 原始权威来源 | 证据类型 | 支撑事实 (SOURCE FACT) | 边界限定 (SOURCE FACT) |
| :--- | :--- | :--- | :--- | :--- |
| **Principled BSDF Specification** | Blender 5.2 LTS Manual `principled.html` | `Vendor Documentation` | 证实 Principled BSDF 官方声明基于 OpenPBR Surface 模型演进，包含 Thin Film, Coat, Sheen, SSS 与 Thin-Walled 模式 | 仅证明其着色器参数模型对齐，不代表包含全部高级影视材质特性 |
| **Blender Python API** | Blender API Documentation `bpy.data.materials` | `Vendor API Documentation` | 证实可通过 Python 脚本构建材质节点图、设置色彩空间与执行渲染循环 | 属于自动化接口能力，不代表学生必须手写复杂脚本 |
| **Headless CLI Arguments** | Blender Manual `command_line/arguments.html` | `Vendor Documentation` | 证实 `-b`（background）与 `-P`（python）支持完全脱机无头运行与渲染指定帧退出 | 提供脱机运行的技术事实依据 |

---
*Lane F Source-Native 提取校准完成，归档于 `docs/research/source-native/blender-official.md`。*
