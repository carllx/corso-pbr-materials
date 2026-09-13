# Lane E: Adobe Substance 3D Sampler — Source-Native Research & Technical Index

> **Artifact Status**: Official Documentation Direct Extraction & Technical Index  
> **Primary Sources**:
> 1. Adobe Substance 3D Sampler Official Documentation (`substance3d.adobe.com/documentation/sadoc/`, Updated 2026-04-07)
> 2. Adobe Substance 3D Sampler Image-to-Material & Generative Features Guides (`helpx.adobe.com/substance-3d-sampler/`)
> 3. Adobe Creative Cloud Generative Credits FAQ (`helpx.adobe.com/creative-cloud/apps/generative-ai/generative-credits-faq.html`)
> 4. Zeeshan Jawed Shah (2022) Chapter 11 (Verified hands-on execution baseline in `source-native-knowledge-index.md`)
> **Artifact Placement**: `docs/research/source-native/adobe-sampler-official.md`  

---

## 1. Executive Summary & Purpose

本研究针对 **Lane E: Substance 3D Sampler** 进行技术解构，重点回答：
1. 图像转材质（Image-to-Material）与无缝平铺（Tiling）算法架构；
2. 材质采集（Material Acquisition）与生成式工作流（Generative Workflows）的官方现状；
3. 严格区分**一手官方事实（SOURCE FACT）**与**教学研判假说（INTERPRETIVE SUMMARY / GATE 3 HYPOTHESIS — NOT A DECISION）**；
4. 明确审慎建立针对“真实测量”、“采集”、“算法估算”与“AI生成”的分类学边界，防止将推断贴图误导为实验室物理真值。

---

## 2. 核心功能与算法架构 (SOURCE FACT)

Substance 3D Sampler 是 Adobe 针对现实资产数字化与材质转换的工具：

### 2.1 Image-to-Material 官方记录的两套算法分支
根据官方滤镜文档，Image-to-Material 提供了截然不同的技术方案：
1. **AI Powered (机器学习分支)**：
   - 基于深度学习模型，专门用于从单张照片中剥离直射与环境光照（De-lighting），生成漫反射反照率（Base Color），并估算生成 **Normal、Height、Roughness** 贴图；
   - 官方文档说明该算法专注于表面去光照和法线/高度推断，对于金属度（Metallic）通常需人工介入或补充指定。
2. **Bitmap to Material (B2M - 传统程序化分支)**：
   - 采用 Substance 经典图像处理算子与程序化技术（Procedural / photometric filter techniques）；
   - 从位图明暗与色彩阈值中估算生成 Base Color、Normal、Metallic、Roughness、Ambient Occlusion 等通道；
   - 属于基于图像规则的确定性处理，但容易受原始照片中的硬高光反光干扰。

### 2.2 无缝平铺与图像处理 (Seamless Tiling & Utilities)
- **Tiling 滤镜**：提供边缘交叉混合（Edge Blending）与偏移拼合（Offset Wrap），消除大面积重复平铺时的明显接缝；
- **智能修补与图层混合**：支持通过图层堆栈添加 Dirt（污垢）、Water（积水）、Embroidery（刺绣）等程序化效果滤镜。

### 2.3 物理尺寸工作流 (End-to-End Physical Size Workflow)
- **Scale Calibration (物理尺度标定)**：
  - 允许艺术家在 2D 视图中指定一段已知物理长度的参考物（如地砖边长 $30\,\text{cm}$）；
  - 软件将贴图像素分辨率与公制单位（Centimeters / Meters）进行关联，并将物理尺寸作为元数据记录在导出的材质资产中。
  - **边界说明**：此功能提供的是尺寸元数据与参考对齐工具，实际在第三方引擎或视口中仍需着色器或三平面投影参数进行相应配合。

### 2.4 生成式 AI 特性与 Beta 计费政策 (Generative Features & Credit Status)
- **Beta 状态**：Sampler 内集成的 Firefly 驱动功能（如 `Text to Texture`、`Text to Pattern`）在官方界面与文档中明确标为 **`Generative (Beta)`**；
- **计费与账户政策 (Generative Credits Policy)**：
  - 根据 Adobe 官方 Generative Credits FAQ，**生成式 AI 特性在处于 Beta 测试期间不消耗商业 Generative Credits（生成式积分）**（"Generative AI features do not consume credits while in Beta"）；
  - 但使用此类功能仍须登录具备有效授权的 Adobe 账户并需要云端网络连接。

---

## 3. 解释性总结：材质精度四级阶梯假说 (INTERPRETIVE SUMMARY / PROJECT TAXONOMY)

> [!NOTE]
> 本节提出的“四级阶梯”为本项目在教学设计中用于防止概念混淆而构建的**解释性分类学模型（Interpretive Taxonomy）**，而非 Adobe 官方的原生术语分类。

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                   材质获取与生成的四层物理精度分类假说                           │
├───────────────────────────────┬──────────────────────────────────────────────────┤
│ 1. Measurement (物理测量)     │ 基于光学实验室专用仪器（分光光度计、测角仪、BTF  │
│                               │ 扫描台），测定精确的物理真值（Ground Truth）。    │
├───────────────────────────────┼──────────────────────────────────────────────────┤
│ 2. Acquisition (数字化采集)   │ 在受控光照环境下进行偏振摄影（Polarized Capture）│
│                               │ 或多视角摄影测量，消除直接反射并采集高精度原图。 │
├───────────────────────────────┼──────────────────────────────────────────────────┤
│ 3. Estimation (算法估算)      │ 单张照片输入，通过图像算子、梯度与传统滤镜       │
│                               │ （如 B2M）根据明暗线索推断法线与粗糙度。         │
├───────────────────────────────┼──────────────────────────────────────────────────┤
│ 4. Generation (生成式推断)    │ 基于扩散模型等先验概率分布预测生成的通道数据。   │
│                               │ 本质为统计推断，绝非真实物理测量数据。           │
└───────────────────────────────┴──────────────────────────────────────────────────┘
```

> **教学防错要点**：  
> 在课程设计中，应引导学生理解 AI 估算生成的 Roughness / Normal / Metallic 贴图属于推断结果，不能当作物理实验测量真值，必须通过标准打光环境（LookDev）进行物理合法性检验。

---

## 4. 解释性总结与教学研判假说 (INTERPRETIVE SUMMARY / GATE 3 HYPOTHESIS — NOT A DECISION)

> [!NOTE]
> 本节内容为基于一手文档形成的教学设计假说，用于为后续 Gate 3 决策提供讨论基础，**不构成当前阶段的最终教学裁决**。

### 4.1 工具链定位与课时比重假说
- **作为工作流桥梁的价值假说 (Workflow Bridge Hypothesis)**：
  - Substance 3D Sampler 在展示“照片参考转贴图（Image-to-Material）”、“无缝平铺（Tiling）”与“去光照（De-lighting）”等概念上，具备直观且低门槛的操作流程；
  - 它能够有效帮助初学者建立现实世界纹理与数字 PBR 贴图之间的物理联系。
- **课时安排与独立课程必要性假说**：
  - 鉴于其采用向导式面板与滤镜堆叠设计，操作复杂度显著低于 Painter 或 Designer；
  - 该工具更适合作为材质课程中的一个**支撑性专题单元或前置桥梁（Supporting Unit / Workflow Bridge）**，是否需要为其分配大跨度的独立长周期教学周，应在 Gate 3 依据整体课时负荷进行审慎决策。

---

## 5. Evidence Register (Lane E)

| 证据条目 | 原始权威来源 | 证据类型 | 支撑事实 (SOURCE FACT) | 边界限定 (SOURCE FACT) |
| :--- | :--- | :--- | :--- | :--- |
| **Sampler Image-to-Material Docs** | Substance 3D Sampler Official User Guide (2026-04) | `Vendor Documentation` | 证实明确存在 AI Powered 与 B2M 两种算法，分别用于单目去光照与传统程序化算子估算 | 单张照片提取属于估算推断，不等于实验室物理测量 |
| **Generative Beta & Credits Policy** | Adobe Sampler Docs & Generative Credits FAQ | `Vendor Documentation` | 证实生成式功能处于 Beta 状态；官方明确在 Beta 期间不消耗生成式积分，但需登录账户与云端连接 | 属于实验性辅助特性，不可断言为固定不变的成熟基石 |
| **Physical Size Workflow** | Sampler Docs `end-to-end-physical-size-workflow` | `Vendor Documentation` | 证实软件提供标尺工具将贴图像素与公制厘米单位关联并存入元数据 | 属于尺寸标定与元数据记录，下游引擎落地仍需着色器配合 |

---
*Lane E Source-Native 提取校准完成，归档于 `docs/research/source-native/adobe-sampler-official.md`。*
