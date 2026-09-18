# CG Cookie CORE V1 (Blender 4.2) NotebookLM 导出视图架构设计 (NotebookLM Export Design)

> **归属任务**：GitHub Issue #6 (CORE V1 Source Governance & NotebookLM Export Architecture)  
> **所处阶段**：Gate D — NotebookLM 导出/视图设计 (Export Architecture Freeze)  
> **前置依赖**：Gate A/B 审计实证、Gate C 治理规范规范化提交 (`6ce18cd`)  
> **核心定位**：解决“**NotebookLM 应当将什么作为认知源 (Cognitive Source)**”，在保持对原始本地证据毫秒级可追溯的前提下，为宽域课程研究中心（Course Research Hub）及后续专精研读提供高信噪比、符合认知单元的导出规范。

---

## 一、 实证基线与现有语料库背景 (Evidence Baseline & Context)

### 1. 真实源体量证据 (Source Size Evidence)
基于 Gate A/B 的只读审计与 Gate C 固化的档案数据：
- **材质与着色 (Materials & Shading)**：
  - 23 视频，22 篇带字幕课时，1 篇无字幕练习片头（27.9s）
  - 词量规模：1,465 个 SRT Cues，**约 12,516 个英文单词**
  - 视频时长：**约 1.48 小时**
  - 配套资产：仅许可 PDF，经核查样本课时使用内建几何体，无外部 `.blend` 依赖
- **纹理绘制 (Texturing)**：
  - 38 视频，35 篇带字幕课时，3 篇无字幕导言/练习片头（<50s）
  - 词量规模：3,990 个 SRT Cues，**约 35,478 个英文单词**
  - 视频时长：**约 4.58 小时**
  - 配套资产：1 个 HDR 独立资产，2 张望远镜 PNG 贴图（望远镜三维网格在归档中未发现）
- **两门课总计**：57 个有效带字幕课时，**共 47,994 个英文单词**，视频总长约 6.06 小时。

### 2. 现有 Course Research Hub 语料库背景
用户现有的 NotebookLM **Course Research Hub** 是一个跨学科、多流派的宏观研究中心，已经收录了：
- 理论与标准：*Adobe PBR Guide*、*Real-Time Rendering 4*、*The Complete Guide to Photorealism*、*OpenPBR* 规范；
- 软件与手册：Blender 5.2 官方手册重点页、Principled BSDF / Shader Nodes 官方文档；
- 工业软件文档：Adobe Substance 3D (Painter / Designer / Sampler) 官方指南；
- 教学与实战证据：高校数字媒体课程大纲、Substance → Unreal/USD 工业流水线媒体等。

**设计结论**：CORE V1 进入该研究中心时，**绝对不能**机械地将 57 个课时文件逐一作为独立 Source 上传，否则会严重稀释学术理论与工业标准的权重，造成源面板拥挤与跨源检索噪音。CORE V1 必须以少数几个**高内聚认知源 (Cognitive Sources)** 的形态注入。

---

## 二、 语料库粒度方案对比与权衡 (Granularity Candidates & Trade-offs)

针对 Course Research Hub 的实际需求，评估三类不同粒度的候选导出架构：

| 评估维度 | Candidate A: Minimal (极简 3 篇) | Candidate B: Moderate (中度 4–5 篇，推荐) | Candidate C: Fine (细粒度 11–13 篇) |
| :--- | :--- | :--- | :--- |
| **文档构成** | • Overview<br>• Materials & Shading<br>• Texturing 全课 | • Overview<br>• Materials & Shading<br>• Texturing Foundations (Ch1-4)<br>• Texturing Workflows (Ch5-7)<br>• Case Locator Index | • Overview<br>• 4 个 Materials 章节源<br>• 7 个 Texturing 章节源<br>• Case Index |
| **源面板整洁度** | 极佳 (仅占 3 个源位置) | 优秀 (占 4~5 个源位置) | 较差 (一次性消耗 12~13 个源位置，占满面板) |
| **跨源课程设计查询** | 良好，但 Texturing 跨度过大 | **最佳**：基础理论与高级工作流泾渭分明 | 碎片化严重，单次查询容易丢失跨章节上下文 |
| **检索信噪比与切片** | Texturing 3.5 万词可能触发边缘切片稀释 | **最佳**：单文档 1.2~2.1 万词，贴合模型最优上下文检索窗口 | 章节过短，容易产生低置信度孤立命中 |
| **引用精确度** | 引用只能标到 Texturing 全书 | **极佳**：一眼看出是基础阶段还是实战工作流 | 虽精细但跨章综合论述时引用过于分散 |
| **4.2→5.2 版本差异比对** | 需在超大文本中全文比对 | **清晰**：材质特性与着色器接入在特定两卷内对齐 | 需跨多个章节源逐一比对，操作繁琐 |
| **维护与同步成本** | 最低 | 适中且结构清晰 | 高，章节零碎容易导致同步遗漏 |

### 决议：采用 Candidate B (中度阶段拆分模型)
- Materials & Shading 全课仅 1.25 万词，结构高度内聚，作为**单一认知源**最为合理；
- Texturing 全课达 3.55 万词，且教学工作流存在天然的“基础输入 vs 创作实战”分水岭，拆分为 **2 个阶段性认知源 (Phase Bundles)** 最能兼顾检索专注度与上下文连贯性；
- 补充 1 份结构化 `CORE42_CASE_INDEX.md`，提供不掺杂分析的纯客观资产与实操定位地图。

---

## 三、 Texturing 认知阶段边界划分 (Texturing Phase Boundaries)

基于对 Texturing 全部 7 个 Chapter、38 节课时的真实文本量、教学步骤与时长审计，确定以下两阶段认知边界：

```
Texturing 课程全景 (38 课 / 35.5k 词)
  │
  ├── [Phase 1: Foundations & Coordinates] ──── Chapter 01: 课程导言 (片头预告)
  │                                        ├── Chapter 02: 纹理概念、空间坐标与色彩数学
  │                                        ├── Chapter 03: UV 编辑器、展开缝合与贴图管理
  │                                        └── Chapter 04: PBR 流程与初阶贴图赋予 (望远镜初探)
  │
  └── [Phase 2: Workflows, Painting & Baking] ─ Chapter 05: 程序化纹理与灰尘污渍节点网络
                                           ├── Chapter 06: 纹理绘制模式、笔刷系统与图层思路
                                           └── Chapter 07: 综合实操——望远镜低模展开、绘制、程序化收尾与烘焙
```

### 1. Bundle 1: `CORE42_TEXTURING_FOUNDATIONS.md`
- **涵盖范围**：Chapter 01 至 Chapter 04（共 20 节课，19 节带字幕，1 节无字幕导言）
- **规模统计**：**14,339 个英文单词**，视频时长 **98.9 分钟** (~1.65 小时)
- **一句话认知目标**：建立三维纹理空间坐标（Generated / UV / Object）、颜色数学与节点通道、UV 展开缝合规范及 PBR 贴图接入的输入端基础认知体系。
- **边界划分依据**：Chapter 01–04 聚焦于“**如何理解并准备贴图数据**”。讲师在此阶段着重讲解坐标系的数学本质、UV 投影避免拉伸的几何逻辑，以及外部已有贴图的色彩空间匹配。第 4 章末尾以望远镜贴图导入作为 PBR 概念的收尾，构成了自洽的基础教学闭环。

### 2. Bundle 2: `CORE42_TEXTURING_WORKFLOWS.md`
- **涵盖范围**：Chapter 05 至 Chapter 07（共 18 节课，16 节带字幕，2 节练习片头）
- **规模统计**：**21,139 个英文单词**，视频时长 **176.1 分钟** (~2.93 小时)
- **一句话认知目标**：掌握在 Blender 内部利用节点生成程序化纹理、视口笔刷手绘材质以及将综合材质烘焙为生产级贴图的创作与输出全流程。
- **边界划分依据**：Chapter 05–07 跃升为“**主动创作与贴图落地**”。从第 5 章的程序化数学纹理，到第 6 章的手绘笔刷工具，再到第 7 章对望远镜完整资产进行“展 UV → 视口手绘 → 程序化细节叠合 → 纹理烘焙导出”的完整工业级 Pipeline。该阶段内聚性极高，是学生实践操作与课程作业设计的直接对应区。

---

## 四、 独立 CORE Deep Reading Notebook 决策 (Deep Reading Evaluation)

### 决策：当前不创建独立 Notebook (NO / CONDITIONAL)

#### 权衡评估
1. **研究重心不匹配**：当前课程设计团队的核心诉求是“横向课程决策”——比对 CG Cookie、Substance 官方、学术教材及 Blender 5.2 之间的理念契合度。在 Course Research Hub 中消费粗粒度捆绑包是最优解。
2. **避免双轨维护与认知碎片**：如果在前期就开设两个 Notebook，团队在查询同一概念（如 Principled BSDF 的 Clearcoat 处理）时，需要在两个窗口间往返，且后续提炼的 4.2→5.2 Delta 笔记需要双向同步，徒增认知摩擦。
3. **条件化触发机制 (Conditional Trigger)**：
   - 触发条件：未来当课程推进至“具体实训周逐课讲义研发”或“针对某复杂资产（如第 7 章望远镜烘焙）进行长达几十轮微观技术审查”时；
   - 实施方式：届时直接以 Gate D 确立的**章节级粒度 (Chapter Bundles)**，一键导出 11 个章节源，开辟独立的 `CORE 4.2 Deep Reading` 研读专区，无需对现有架构做任何返工。

---

## 五、 CASE INDEX 职责边界与治理纪律 (Case Index Scope & Boundary)

依据 Gate C 确立的 `Source View != Wiki` 根本原则，严格厘定案例索引的职责：

```
┌─────────────────────────────────────────────────────────────┐
│ 1. CASE INDEX (本层: Source View / 客观资产定位索引)        │
│    • 课时 ID (lesson_id)                                    │
│    • 案例/实操标准名称                                      │
│    • 原始视频相对路径与起始时间锚点 [HH:MM:SS]              │
│    • 配套资产定位 (HDR / PNG / 3D网格)                      │
│    • 客观资产状态 (DIRECT_MATCH / NO_EXTERNAL / UNRESOLVED) │
│    • 厂商归档客观缺失说明 (事实记录，不带推论)              │
└──────────────────────────────┬──────────────────────────────┘
                               │ 严禁直接伪装混入！
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. PERSISTENT WIKI (提炼知识层 / 教学配方与原理)            │
│    • 节点物理参数配方 (肥皂泡 Thin Film: IOR=1.4, d=800nm)  │
│    • 节点连接逻辑最佳实践 (AO 0.75 Multiply 到 Base Color) │
│    • 教学设计提示、难点预警与学生常见报错                   │
│    • Blender 4.2 到 5.2 节点参数演进比对                    │
└─────────────────────────────────────────────────────────────┘
```

- **结论**：NotebookLM 消费的 `CORE42_CASE_INDEX.md` 定位为**纯客观的资产与案例定位器 (Asset Locator Index)**。
- 具体的参数配方（Parameter Recipes）与节点设置属于知识综合（Wiki），由 Wiki 层形成专题文档后再按需导出，绝不将综合知识混装在源定位索引中误导模型将其当成原厂事实。

---

## 六、 NotebookLM 导出文档骨架规范 (Export Document Schema)

所有面向 NotebookLM 的导出 Markdown 必须采用统一的 Provenance 头部与正文层级：

### 1. 结构化导出头部 (Export Frontmatter)
```yaml
---
source_id: "cgcookie-core-v1-blender-4.2"
export_view: "notebooklm-cognitive-bundle"
bundle_id: "core42-tex-workflows"
title: "CORE V1 Texturing — Phase 2: Procedural, Painting & Baking"
source_courses:
  - "Texturing"
chapter_range: "05-07"
lesson_count: 18
word_count: 21139
duration_formatted: "02:56:06"
blender_reference_version: "4.2 LTS"
generated_at: "2026-09-18"
provenance_status: "DERIVED_TRACEABLE_VIEW"
---
```

### 2. 文档正文层次规范
```markdown
# CORE V1 Texturing — Phase 2: Procedural, Painting & Baking

> **Cognitive Scope**: 本卷覆盖 Blender 4.2 纹理绘制、程序化节点生成与贴图烘焙落地的高级创作工作流。
> **Provenance**: 派生自本地只读源包 `Texturing-Videos-01`，各小节均附带原始课时 ID 与视频时间锚点。

## Cognitive Source Map (本卷章节全景)
- Chapter 05: Procedural Texturing (程序化纹理与灰尘污渍)
- Chapter 06: Texture Paint Mode (视口手绘模式与笔刷系统)
- Chapter 07: LowPoly Binoculars Production Pipeline (望远镜全流程实战与烘焙)

---

## Chapter 05: Procedural Texturing

### [texturing-c05-l020] Intro to Procedural Texturing
> **Lesson**: Ch05 L20 | **Duration**: 00:12:41 | **Video**: `TEXTURES_C05L020_IntroToProceduralTexturing.mp4`  
> **Assets**: `HIGH_CONFIDENCE_NO_EXTERNAL_ASSET`

#### [00:00:00] Part 1: 程序化纹理核心理念与数学纹理
**[00:00:00]** 讲师阐述程序化纹理相对于位图贴图的无限分辨率优势……

#### [00:04:12] Part 2: Noise 纹理与 ColorRamp 映射控制
**[00:04:12]** 在着色器编辑器中连接 Noise 纹理并调整色彩渐变节点……
```

---

## 七、 严密溯源调用链 (Traceability Chain)

当人类教师或 Agent 在 NotebookLM 中与模型交互并获得回答时，必须能够顺畅反向追溯至一手音视频：

```
NotebookLM 界面生成回答 (LLM Synthesis)
       │
       ▼ [引用标记 Citation, 例如 "[1]"]
NotebookLM 侧边栏指向文档及锚点 (Bundle H2/H3 Heading)
       │
       ▼ [识别规范 Lesson ID, 例如 "texturing-c05-l020"]
本地伴生工作区对应逐字稿 `<source-views>/transcripts/texturing-c05-l020.transcript.md`
       │
       ▼ [读取语义块时间戳, 例如 "## [00:04:12] Part 2"]
可读时间定位：教师直接在视频播放器中拉动进度条至 04:12 查看实操
       │
       ▼ [高精度机器检索 (可选)]
查询伴生侧车 `<source-views>/cue-maps/texturing-c05-l020.cues.jsonl`
       │  (通过 start_ms / end_ms 获取台词所在绝对时码)
       ▼
底层事实验证：读取原始 `/Volumes/.../Texturing-Videos-01/...mp4` 与原始 `.srt`
```

此溯源链满足：
1. **人读友好**：教师不需要查 JSON，直接根据 `[00:04:12]` 在 1 秒内定位视频；
2. **机器严谨**：Agent 可通过 `lesson_id` 瞬时检索 `cues.jsonl` 精确定位对应台词；
3. **证据绝对**：最终裁决权始终属于原始未变动的音视频与字幕。

---

## 八、 Gate E 建议迁移与执行范围 (Proposed Scope for Gate E)

当本 Gate D 架构设计通过审查后，Gate E 的执行范围严格限定于：
1. **处理范围**：
   - 仅处理 Materials & Shading（22 课时）与 Texturing（35 课时）共计 **57 个带字幕课时**；
   - 4 个无字幕短片头按 `caption_status: "NOT_PROVIDED"` 纳入元数据登记，不生成虚假字幕。
2. **输出产物清单**：
   - `source-registry/registry.json`：建立全量 574 个文件的原始路径定位索引；
   - `source-views/transcripts/`：生成 57 篇规范化 `*.transcript.md`；
   - `source-views/cue-maps/`：生成 57 篇规范化 `*.cues.jsonl`；
   - `source-views/manifests/`：生成课程与案例总清单；
   - `exports/notebooklm/`：合并生成 5 份标准 Markdown 捆绑源文档：
     1. `CORE42_OVERVIEW.md`
     2. `CORE42_MATERIALS_AND_SHADING.md`
     3. `CORE42_TEXTURING_FOUNDATIONS.md`
     4. `CORE42_TEXTURING_WORKFLOWS.md`
     5. `CORE42_CASE_INDEX.md`
3. **红线执行**：
   - 全程对 NAS 源素材保持只读；
   - 派生的大文本不提交至 GitHub 公共仓库，保存在本地 companion workspace；
   - 不进行自动化上传，等待显式授权。
