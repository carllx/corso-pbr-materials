# Lane E: Adobe Substance 3D Sampler — Source-Native Research & Technical Index

> **Artifact Status**: Official Documentation Direct Extraction & Technical Index  
> **Primary Sources**:
> 1. Adobe Substance 3D Sampler Official Documentation (`substance3d.adobe.com/documentation/sadoc/`, Updated 2026-04-07)
> 2. Adobe Substance 3D Sampler Image-to-Material & Generative Features Guides (`helpx.adobe.com/substance-3d-sampler/`)
> 3. Zeeshan Jawed Shah (2022) Chapter 11 (Verified hands-on execution baseline in `source-native-knowledge-index.md`)
> **Artifact Placement**: `docs/research/source-native/adobe-sampler-official.md`  

---

## 1. Executive Summary & Purpose

本研究针对 **Lane E: Substance 3D Sampler** 进行技术解构，重点回答：
1. 图像转材质（Image-to-Material）与无缝平铺（Tiling）算法架构；
2. 材质采集（Material Acquisition）与生成式工作流（Generative Workflows）的技术实现；
3. 严格确立并区分四个具有本质物理差异的维度：
   $$\text{Measurement (真实测量)} \quad \neq \quad \text{Acquisition (采集提取)} \quad \neq \quad \text{Estimation (算法估算)} \quad \neq \quad \text{Generation (AI 生成)}$$
4. 明确禁止将 AI 推断出来的 Normal / Roughness 贴图误描述为真实物理测量数据，为 Gate 3 提供严密的事实边界。

---

## 2. 核心功能与算法架构 (Core Architecture & Workflows)

Substance 3D Sampler（前身为 Substance Alchemist）是 Adobe 面向真实物理材质数字化（Digitization of Physical Assets）的核心环境：

### 2.1 Image-to-Material 双算法分支 (Dual-Engine Architecture)
官方文档明确记录了工具内部截然不同的两套贴图提取算法引擎：
1. **AI Powered (Machine Learning Branch)**：
   - 采用深度学习卷积网络，专用于从单张普通摄影照片中进行**反光剥离与阴影消除（De-lighting Albedo）**；
   - 依赖图像上下文估算并输出基础 **Normal、Height、Roughness** 贴图通道；
   - **特点**：对于漫反射去除阴影效果突出，但生成的微表面粗糙度往往偏向平滑或缺乏极端对比度。
2. **Bitmap to Material (B2M - Classical Procedural / Photometric Branch)**：
   - 采用经典图像高通滤波（High-pass Filter）、灰度阈值计算与 Sobel 梯度边缘提取算法；
   - 从位图中基于算法逻辑估算生成 **Base Color、Normal、Metallic、Roughness、Ambient Occlusion** 等全套通道；
   - **特点**：完全确定性，但无法区分照片中的真实反光（Specular Highlight）与固有色反照率（Albedo），容易将高光误判定为漫反射死白。

### 2.2 无缝平铺与图像修复 (Seamless Tiling & Inpainting)
- **Tiling 滤镜**：
  - 支持边界淡入混合（Threshold Blending）、合成偏移（Offset Wrap）与边缘交叉渐变；
  - 智能修复大面积重复平铺时的明显接缝（Seams）。
- **Clone / Inpainting (智能修补)**：
  - 利用算法消除照片中的杂物、落叶、临时反光暗斑，保证纹理的纯净性。

### 2.3 物理尺寸校准 (End-to-End Physical Size Workflow)
- **Scale Calibration (物理尺度标定)**：
  - 允许艺术家在 2D 照片中指定一段已知物理长度的参考物（例如地砖的 $30\,\text{cm}$ 宽度、硬币直径或标尺）；
  - 软件自动将贴图的像素分辨率（Pixels）与真实物理世界米制单位（Centimeters / Meters）进行精确绑定（Physical Size Metadata）；
  - 导入 Substance 3D Painter 或游戏引擎后，三平面投影或着色器平铺滑块能够自动按照 1:1 真实世界比例进行贴合，杜绝纹理缩放失真。

### 2.4 生成式 AI 特性与生产成熟度 (Generative Features & Beta Status)
- 集成 Adobe Firefly 驱动的 `Text to Texture`、`Text to Pattern` 与智能扩图功能；
- **官方成熟度边界**：
  - 截至 2026 年，官方技术面板中相关生成式特性**仍明确标为 `Generative (Beta)`**；
  - 依赖 Adobe 云端算力与商业积分订阅，主要用于前期灵感草稿生成与快速图案变体探索，不能定性为不变的工业既定绝对事实。

---

## 3. 核心概念辨析：四层物理边界 (Critical Conceptual Boundaries)

在教学设计与技术审计中，必须严格区分以下四个层级，严禁概念混淆：

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                   材质获取与生成的四层物理精度阶梯                               │
├───────────────────────────────┬──────────────────────────────────────────────────┤
│ 1. Measurement (真实物理测量) │ 基于严格光学实验室仪器（分光光度计、测角反射仪   │
│                               │ Goniophotometer、BTF 扫描台或多角度偏振光照球）。│
│                               │ 数据为客观物理真值（Ground Truth），非算法猜测。 │
├───────────────────────────────┼──────────────────────────────────────────────────┤
│ 2. Acquisition (数字化采集)   │ 在控制光照环境下进行多重交叉偏振摄影（Cross-     │
│                               │ polarized Photometry）或摄影测量（Photogrammetry）│
│                               │ 去除直接镜面反射，提取高质量原始多视角图像数据。 │
├───────────────────────────────┼──────────────────────────────────────────────────┤
│ 3. Estimation (算法估算)      │ 利用单张照片，通过图像梯度、Sobel 滤镜或单目深度 │
│                               │ 估算算法（B2M / 基础法线滤镜）推断凹凸与明暗。   │
├───────────────────────────────┼──────────────────────────────────────────────────┤
│ 4. Generation (生成式推断)    │ 基于扩散模型（Diffusion）或对抗网络（GAN）的先验 │
│                               │ 概率分布“脑补”出来的 Normal、Roughness 贴图。    │
│                               │ **本质是统计幻觉预测，绝非真实物理测量！**       │
└───────────────────────────────┴──────────────────────────────────────────────────┘
```

> **教学防错准则**：  
> 绝不能在课程中向学生灌输“AI 拍一张照就能全自动获取完美真实物理 PBR 贴图”的错误推断。AI 生成的 Roughness 与 Metallic 贴图必须经过人工在标准 LookDev 视口中的物理检验（如检查金属二值性、排除高光残留暗斑）。

---

## 4. 教学价值研判支撑：强力辅助桥梁 vs 课程核心定位

通过官方事实梳理，为后续 Gate 3 决策提供明确输入：
- **作为“连接现实摄影、传统 PBR 贴图与 AI 生成的强力实践桥梁”**：
  - Sampler 在让学生直观建立“物理尺寸（Physical Size）”、“无缝平铺（Tiling）”与“去光照（De-lighting）”概念上具有极高的低门槛演示价值。
- **软件学习成本极低**：
  - Sampler 为向导式面板操作（Wizard-style panels），学生通常在 1–2 小时内即可掌握全部核心功能，**完全不需要开设长周期的独立软件课程**。
  - 应作为支撑性工具单元或工作流桥梁，而非膨胀为主要考核支柱。

---

## 5. Evidence Register (Lane E)

| 证据条目 | 原始权威来源 | 证据类型 | 支撑事实 | 边界限定 |
| :--- | :--- | :--- | :--- | :--- |
| **Sampler Image-to-Material Docs** | Substance 3D Sampler Official User Guide (2026-04) | `Vendor Documentation` | 证实明确存在 AI Powered 与 B2M 两种算法，分别负责单目去光照与传统图像滤波估算 | 证明单张照片提取并非物理实验室测量 |
| **Physical Size Workflow** | Sampler Docs `end-to-end-physical-size-workflow` | `Vendor Documentation` | 证实物理尺度（Scale Calibration）标定功能，将像素与公制厘米单位绑定 | 属于元数据与缩放校准，不提升贴图物理采集精度 |
| **Generative Beta Status** | Sampler Generative Features Documentation | `Vendor Documentation` | 证实 Firefly 驱动的 Text-to-Texture 在 2026 仍处于 Beta 状态并依赖云端积分 | 证明生成式功能为实验性辅助，不可断言为成熟固定工业基石 |

---
*Lane E Source-Native 提取完成，归档于 `docs/research/source-native/adobe-sampler-official.md`。*
