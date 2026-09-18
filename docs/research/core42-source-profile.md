# CG Cookie CORE V1 (Blender 4.2) 源资产概况与审计档案 (Source Profile & Audit Record)

> **归属任务**：GitHub Issue #6 (CORE V1 Source Governance & NotebookLM Export Architecture)  
> **审计范围**：本地 NAS 挂载路径 `/Volumes/198.168.10.5/Download/CGCookie - Blender 4.2 Core Essentials - 9 Tutorials`  
> **审计时间**：2026-09-18 (Gate A / Gate B 实证)  
> **合规申明**：本档案仅记录元数据、统计聚合事实与架构分析，**不包含任何厂商受版权保护的视频、原始字幕全文或三维模型资产**。

---

## 一、 源标识与全量资产概览 (Source Overview)

- **规范源标识 (`source_id`)**：`cgcookie-core-v1-blender-4.2`
- **文件总数**：574 个文件
- **总存储容量**：16,223,406,914 字节（约 15.11 GB）
- **0 字节异常文件**：0 个（无不完整传输损坏文件）
- **检测到课程**：CG Cookie CORE V1 完整 9 门教程，分布于 20 个顶层目录中

### 顶层目录与容量分布表

| 目录名称 | 类别 | 文件数 | 总容量 | 核心扩展名构成 |
| :--- | :--- | :---: | :---: | :--- |
| `Animation-Videos-01` | 视频+字幕 | 26 | 358.1 MB | `.mp4`: 13, `.srt`: 13 |
| `Compositing-CourseFiles-01` | 配套资产 | 2 | 0.2 MB | `.pdf`: 2 |
| `Compositing-Videos-01` | 视频+字幕 | 34 | 694.1 MB | `.mp4`: 17, `.srt`: 17 |
| `Digital-Sculpting-CourseFiles-01` | 配套资产 | 4 | 2.2 MB | `.pdf`: 1, `.jpg`: 2, `.png`: 1 |
| `Digital-Sculpting-Videos-01` | 视频+字幕 | 40 | 2.16 GB | `.mp4`: 20, `.srt`: 20 |
| `Lighting-CourseFiles-01` | 配套资产 | 9 | 415.7 MB | `.blend`: 5, `.blend1`: 2, `.pdf`: 1, `.jpg`: 1 |
| `Lighting-Videos-01` | 视频+字幕 | 51 | 1.78 GB | `.mp4`: 26, `.srt`: 25 |
| `Materials-and-Shading-CourseFiles-01` | 配套资产 | 1 | 0.04 MB | `.pdf`: 1 |
| `Materials-and-Shading-Videos-01` | 视频+字幕 | 45 | 531.4 MB | `.mp4`: 23, `.srt`: 22 |
| `Mesh-Modeling-CourseFiles-01` | 配套资产 | 1 | 0.04 MB | `.pdf`: 1 |
| `Mesh-Modeling-Videos-01` | 视频+字幕 | 28 | 1.13 GB | `.mp4`: 14, `.srt`: 14 |
| `Mesh-Modeling-Videos-02` | 视频+字幕 | 28 | 1.02 GB | `.mp4`: 14, `.srt`: 14 |
| `Physics-CourseFiles-01` | 配套资产 | 27 | 228.0 MB | `.blend`: 25, `.pdf`: 2 |
| `Physics-Videos-01` | 视频+字幕 | 56 | 1.59 GB | `.mp4`: 28, `.srt`: 28 |
| `Physics-Videos-02` | 视频+字幕 | 26 | 686.7 MB | `.mp4`: 13, `.srt`: 13 |
| `Physics-Videos-03` | 视频+字幕 | 34 | 635.4 MB | `.mp4`: 17, `.srt`: 17 |
| `Rigging-CourseFiles-01` | 配套资产 | 1 | 0.04 MB | `.pdf`: 1 |
| `Rigging-Videos-01` | 视频+字幕 | 84 | 1.98 GB | `.mp4`: 42, `.srt`: 42 |
| `Texturing-CourseFiles-01` | 配套资产 | 4 | 6.2 MB | `.hdr`: 1, `.png`: 2, `.pdf`: 1 |
| `Texturing-Videos-01` | 视频+字幕 | 73 | 1.97 GB | `.mp4`: 38, `.srt`: 35 |

---

## 二、 重点课程实证深度审计 (Deep Audit: Materials & Texturing)

### 1. 材质与着色 (Materials & Shading)
- **视频总数**：23 个（全部为 `.mp4`）
- **字幕总数**：22 个（全部为 `.srt`，存放于 `captions/` 目录）
- **总播放时长**：约 1.48 小时（5,331 秒）
- **字幕容量统计**：共 1,465 个 SRT Cues，12,516 个英文单词
- **视频 ↔ 字幕配对**：22 对实现 1:1 配对
- **未配对视频 (1 个)**：
  - `SHADING_C04_E01_IsItGlassOrPorcelain.mp4`：时长 27.90 秒，大小 4.18 MB。经音视频流分析，为练习题先导过渡片头，原厂未配发字幕（判定为 `caption_status: "NOT_PROVIDED"`）。
- **配套资产实测**：
  - 目录 `Materials-and-Shading-CourseFiles-01` 中仅有 1 个文件：`cgc-license-sourcefile.pdf`（CG Cookie 官方教育许可免责协议），**不包含任何 `.blend` 或贴图等工程资产**。
  - 在抽样核查的代表性课时中，观察到讲师在视频中主要使用 Blender 默认/简单的会话内几何体（如 Suzanne 猴头、默认材质球、立方体或平面）演示参数。
  - 因此对于已核查的样本课时，外部工程资产非必需关联（标记为 `HIGH_CONFIDENCE_NO_EXTERNAL_ASSET`）。

### 2. 纹理绘制 (Texturing)
- **视频总数**：38 个（全部为 `.mp4`）
- **字幕总数**：35 个（全部为 `.srt`，存放于 `Captions/` 目录）
- **总播放时长**：约 4.58 小时（16,493 秒）
- **字幕容量统计**：共 3,990 个 SRT Cues，35,478 个英文单词
- **视频 ↔ 字幕配对**：35 对实现 1:1 配对
- **未配对视频 (3 个)**：
  - `TEXTURES_C01L00_IntroToTextures.mp4`：时长 49.17 秒，11.75 MB。整课导言宣传片，原厂无字幕（`caption_status: "NOT_PROVIDED"`）。
  - `TEXTURES_C05E01_ProceduralRustAndMetal.mp4`：时长 29.85 秒，5.31 MB。练习片头，原厂无字幕（`caption_status: "NOT_PROVIDED"`）。
  - `TEXTURES_CH07E01_Let’sTextureShadeAndRenderTheRobot!.mp4`：时长 29.31 秒，5.78 MB。实战练习片头，原厂无字幕（`caption_status: "NOT_PROVIDED"`）。
- **配套资产实测**：
  - `Texturing-Chapter-03-Files/CH03_Lesson09-ManagingTextureData/autoshop_01_2k.hdr`（6.1 MB，直接匹配 Ch03 L09 课时，`DIRECT_MATCH`）。
  - `Texturing-Chapter-04-Files/CH04 Lesson 19-ThePrincipledShader-ShadingBinoculars/Binoculars_Opacity.png`（8.5 KB）与 `Sand_Metallic.png`（4.1 KB）。
  - **关键事实**：原厂提供了望远镜的 2 张测试贴图，但在所提供的归档中未发现对应的三维网格/工程文件（标记为 `UNRESOLVED`）。

---

## 三、 格式特征与命名异常实录 (Anomalies & Provenance Friction)

在只读审计过程中，发现原厂包存在以下非规范化特征，必须在治理规范中予以容错与解耦：

### 1. 字幕目录大小写冲突 (Case Inconsistency)
- 全小写 `captions/`：`Materials-and-Shading-Videos-01`、`Lighting-Videos-01`、`Animation-Videos-01`
- 首字母大写 `Captions/`：`Texturing-Videos-01`、`Compositing-Videos-01`、`Digital-Sculpting-Videos-01`、`Mesh-Modeling-Videos-01/02`、`Rigging-Videos-01`
- 分章节子目录：`Physics-Videos` 未使用独立字幕目录，而是按 `Chapter-01` 至 `Chapter-08` 组织。

### 2. 标点符号与特殊字符
- **空格**：如 `SHADING_C03_L17_All the good stuff.mp4`、`CH04 Lesson 19-ThePrincipledShader-ShadingBinoculars`
- **逗号**：如 `SHADING_C02_L08_Refraction,GlassShaders.mp4`
- **智能弯引号与感叹号**：如 `TEXTURES_CH07E01_Let’sTextureShadeAndRenderTheRobot!.mp4`

### 3. 课程序号命名风格不一致
- 材质课采用标准下划线分隔：`SHADING_C02_L01_...`
- 纹理课采用无下划线或三位数字混杂：`TEXTURES_C02L01_...`、`TEXTURES_C03L010_...`、`TEXTURES_C03L09_...`
- 含有附赠课与练习前缀：`TEXTURES_C06B01_...`（Bonus）、`TEXTURES_CH07E01_...`（Exercise 采用 CH07 而非 C07）

---

## 四、 Gate B 代表性原型样本清单 (Prototype Sample Register)

在 Gate B 原型阶段验证的 6 个代表性样本课时（覆盖两门核心课程）覆盖了概念、高密度实操、物理渲染、环境管理与贴图导入：

| 规范 Lesson ID | 课程与课时原名 | 视频时长 | Cue 计数 | 英文词量 | 资产关联状态判定 |
| :--- | :--- | :---: | :---: | :---: | :--- |
| `materials-shading-c02-l01` | What is a Shader and How to Use It | 00:01:24 | 28 | 246 | `HIGH_CONFIDENCE_NO_EXTERNAL_ASSET` |
| `materials-shading-c02-l13` | The Principled BSDF | 00:10:39 | 185 | 1,548 | `HIGH_CONFIDENCE_NO_EXTERNAL_ASSET` |
| `materials-shading-c04-l20` | Rendering Glass: Dispersion and Caustics | 00:07:09 | 109 | 937 | `HIGH_CONFIDENCE_NO_EXTERNAL_ASSET` |
| `texturing-c02-l01` | Intro to Textures and Texture Coordinates | 00:07:53 | 135 | 1,175 | `HIGH_CONFIDENCE_NO_EXTERNAL_ASSET` |
| `texturing-c03-l09` | Managing Texture Data | 00:06:29 | 102 | 918 | `DIRECT_MATCH` (`autoshop_01_2k.hdr`) |
| `texturing-c04-l19` | Principled Shader: Shading Binoculars | 00:03:23 | 51 | 438 | `UNRESOLVED` (贴图存在，3D 模型未在归档中发现) |

---

## 五、 NotebookLM 导出容量估算依据 (Export Capacity Evidence)

基于两门重点课程的实际英文词量与时长数据，为 Gate D 提供严密的设计基线：

1. **Materials & Shading 全课规模**：
   - 22 节带字幕课时，共计 **12,516 个英文单词**，视频总长 1.48 小时。
   - **实测参考**：全课词量规模约为 1.25 万词。基于所观察到的体量，单文档捆绑是 Gate D 的一个可行候选方案（single-document bundling is a plausible Gate D candidate given the observed size），具体切分方案留待 Gate D 决定。
2. **Texturing 全课规模**：
   - 35 节带字幕课时，共计 **35,478 个英文单词**，视频总长 4.58 小时。
   - **实测参考**：全课词量约为 3.5 万词。在 Course Research Hub 中可作为 1 份完整源或 2 份阶段性源候选；在专精的 CORE Deep Reading Notebook 中，可考虑按章节或专题进行更细致的捆绑（如按 Chapter 组织）。具体的认知单元边界留待 Gate D 决定；平台当前的配额或产品限制属于部署层事实，应在导出时动态校验，不作为规范层的刚性证据。
