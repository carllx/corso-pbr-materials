# Lane F: Blender — Programmable Material Validation Environment — Source-Native Research & Technical Index

> **Artifact Status**: Official Documentation & API Direct Extraction  
> **Primary Sources**:
> 1. Blender 5.2 LTS Official Manual (`docs.blender.org/manual/en/latest/`, Principled BSDF & Shader Nodes)
> 2. Blender Python API Documentation (`docs.blender.org/api/current/`, `bpy.data.materials`, `bpy.ops.render`)
> 3. Blender Command-Line Reference (`docs.blender.org/manual/en/latest/advanced/command_line/`)
> **Artifact Placement**: `docs/research/source-native/blender-official.md`  

---

## 1. Executive Summary & Purpose

本研究针对 **Lane F: Blender** 进行精准收口的材质技术解构，重点回答：
1. 现代材质节点架构（Shader Nodes）与 Principled BSDF（基于 OpenPBR 规范演进）；
2. Python API、脚本化无头渲染（Scripted / Headless Validation）与场景/相机/渲染循环能力；
3. 仅调查与材质课程直接相关的能力，重点评估：
   $$\text{Blender 是否可以成为低成本、开源可编程的【Agent + Material + Scene + Render Validation】实验验证环境}$$
4. 明确非目标：不扩展为 Blender 综合建模、动画或全流程课程。

---

## 2. 材质体系与 Principled BSDF 规范演进 (Materials & Principled BSDF)

### 2.1 现代 Principled BSDF 核心架构 (OpenPBR Alignment)
Blender 官方手册在 Principled BSDF 章节中明确阐述了其现代物理材质架构：
- **规范对齐声明**：
  - 官方文档明确指出：“**It is based on the OpenPBR Surface shading model**, and provides parameters compatible with similar PBR shaders found in other software, such as the Disney and Standard Surface models.”
  - 直接支持将 Substance Painter 等外部软件绘制或烘焙的 PBR 贴图（Base Color, Roughness, Metallic, Normal）直接无缝连入。
- **物理层级组织 (Layered Components)**：
  - **Base Layer**：Metal（导体纯反射）、Diffuse（全漫反射）、Subsurface（次表面体积散射）与 Transmission（玻璃/透光折射）四个分量的混合。
  - **Specular Layer**：电介质菲涅尔基础高光反射，受 IOR 与 Roughness 控制。
  - **Thin Film Layer**：位于基础层之上的薄膜干涉层，支持纳米级物理厚度（Thickness）与 IOR 设置，生成肥皂泡、高温氧化金属彩虹色。
  - **Coat Layer**：位于顶层的独立光泽清漆涂层，具备独立的粗糙度与法线输入（例如汽车金属漆外层的透明清漆）。
  - **Sheen / Fuzz Layer**：位于所有层级之上的微纤维绒毛层，模拟布料边缘的光泽（Sheen）。
  - **Emission**：光线从 Coat 与 Sheen 层下方穿透发射，精确模拟表面落灰或带透明外壳的发光屏幕。
  - **Thin-Walled Mode (薄壁模式)**：布尔开关，用于树叶、窗帘、纸张等无体积厚度薄片，自动镜像双面光照。

### 2.2 着色器节点网络 (Shader Node Architecture)
- Blender 的 Shader Nodes 具有极高的数据灵活性：
  - 原生支持坐标转换（`Texture Coordinate`：Generated, Normal, UV, Object, Camera, Window, Reflection）；
  - 矢量映射与重投影（`Mapping`, `Vector Rotate`, `Vector Math`）；
  - 色彩与灰度重映射（`ColorRamp`, `Map Range`, `Math`）；
  - 属性输入（`Attribute`, `Color Attribute`）：直接读取模型网格上的顶点色或自定义几何数据。

---

## 3. 可编程与无头验证环境评估 (Headless Validation & Python API)

Blender 具备其他商业闭源 DCC 不具备的独特生态优势：**完全开源、无需许可证（No License Costs）、支持纯命令行无头（Headless）自动化运行与完整的 Python 脚本绑定**。

### 3.1 脚本化自动化核心能力 (Python `bpy` Module)
通过标准 Python 脚本可以完全控制整个材质与渲染验证流程：
1. **程序化材质创建与连线 (Automated Node Graph Construction)**：
   ```python
   import bpy

   mat = bpy.data.materials.new(name="PBR_Validation_Material")
   mat.use_nodes = True
   nodes = mat.node_tree.nodes
   links = mat.node_tree.links

   bsdf = nodes.get("Principled BSDF")
   tex_node = nodes.new(type="ShaderNodeTexImage")
   tex_node.image = bpy.data.images.load("/path/to/base_color.png")
   links.new(tex_node.outputs["Color"], bsdf.inputs["Base Color"])
```
2. **多通道色彩空间自动化配置 (Color Space Enforcement)**：
   - 可通过脚本强制指定法线、粗糙度贴图的色彩空间为 `Non-Color`，杜绝人工误操作：
   ```python
   tex_node.image.colorspace_settings.name = "Non-Color"
```
3. **测试场景、相机与打光编排 (Scene & Camera Orchestration)**：
   - 脚本可自动创建标准 LookDev 场景：导入标准灰球/银球（Macbeth Chart / Chrome Ball）、创建三点光源或载入测试 HDRI 环境天光（IBL）。
4. **触发渲染与结果保存 (Render Execution)**：
   - 切换渲染引擎为 Cycles（物理光线追踪）或 EEVEE-Next（实时光栅化/光线步进）；
   - 执行渲染并将测试切片保存为磁盘图像，供视觉对比或自动化排错：
   ```python
   bpy.context.scene.render.engine = "CYCLES"
   bpy.context.scene.render.filepath = "/path/to/output_render.png"
   bpy.ops.render.render(write_still=True)
```

### 3.2 命令行无头执行与 CI/CD 兼容性 (Command-Line Headless Mode)
官方手册明确记录了命令行参数：
- `blender -b [file.blend] -P [script.py] -o [output_path] -f [frame_number]`
  - `-b, --background`：后台无头运行，不启动任何 GUI 界面或显卡桌面上下文。
  - `-P, --python <filename>`：启动时自动执行指定的 Python 验证脚本。
  - `-f, --render-frame <frame>`：直接渲染指定帧并退出。
- **环境价值**：可以在本地终端、Docker 容器或云端 Linux 服务器中，以秒级启动自动化材质回归测试。

---

## 4. 教学价值研判支撑：Agent + Material + Scene + Render 实验基座

通过对官方文档的实证梳理，为后续 Gate 3 提供了极其关键的定位论据：

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                   Blender 在材质课程中的定位跃迁模型                             │
├───────────────────────────────┬──────────────────────────────────────────────────┤
│ 1. 传统定位 (避坑认知)        │ **严禁办成“Blender 大全通识课”**                  │
│    (General 3D Curriculum)    │ - 不展开讲授 Blender 复杂建模工具、骨骼绑定、    │
│                               │   动画曲线、几何节点粒子系统或影视合成。         │
├───────────────────────────────┼──────────────────────────────────────────────────┤
│ 2. 现代定位 (核心升权价值)    │ **开源低成本的【自动化材质与渲染验证实验室】**    │
│    (Programmable Validation)  │ - 作为学生和 AI 智能体（Agent）可共同操作的沙盒： │
│                               │ - 学生/脚本输出贴图 $\to$ 自动组装 Principled    │
│                               │   BSDF $\to$ 放置于标准测试打光场景 $\to$ 自动   │
│                               │   渲染 Cycles/EEVEE 图像 $\to$ 诊断物理正确性。  │
│                               │ - 零商业授权门槛，机房与学生个人笔记本均可部署。 │
└───────────────────────────────┴──────────────────────────────────────────────────┘
```

---

## 5. Evidence Register (Lane F)

| 证据条目 | 原始权威来源 | 证据类型 | 支撑事实 | 边界限定 |
| :--- | :--- | :--- | :--- | :--- |
| **Principled BSDF Specification** | Blender 5.2 LTS Manual `principled.html` | `Vendor Documentation` | 证实其全面对齐 OpenPBR Surface 模型架构，包含 Thin Film, Coat, Sheen, SSS 与 Thin-Walled 模式 | 证明其参数语义与工业前沿标准一致 |
| **Blender Python API** | Blender API Documentation `bpy.data.materials` | `Vendor API Documentation` | 证实可通过 Python 脚本全自动构建着色器节点拓扑、连接端口并设置色彩空间 | 证明其完全具备被 Agent/脚本调用的能力 |
| **Headless CLI Execution** | Blender Manual `command_line/arguments.html` | `Vendor Documentation` | 证实 `-b`（background）与 `-P`（python）支持完全脱机无头运行与批量渲染 | 证明其可作为极低成本的自动化测试环境 |

---
*Lane F Source-Native 提取完成，归档于 `docs/research/source-native/blender-official.md`。*
