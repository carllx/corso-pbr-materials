# 外部源素材治理与派生视图规范 (Source Material Governance & Traceable View Specification)

> **定位**：本规范定义面向第三方/商业视频教程、配套资产与工程文件包（如 CG Cookie CORE 系列）的通用源治理架构。确保在**绝对不改动原始素材**、**严格遵守版权红线**的前提下，建立对人类教师高度可读、对 AI Agent 可通过 Cue 级时码准确回溯、且可无缝对接下游持久化知识库与 NotebookLM 的标准化派生流水线。
> **参考契约**：GitHub Issue #6，已在 CORE V1 (Blender 4.2) 574 个真实文件与覆盖 2 门课程的 6 个代表性课时原型中完成验证。

---

## 一、 四层核心架构 (Canonical Architecture)

治理流水线严格执行“四层分离”模型，严禁跨层污染或将格式转换与知识综合混为一谈：

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Immutable Source (不可变源层)                            │
│    原始视频 / SRT / VTT / PDF / .blend / 贴图 / 专有资产    │
│    • 绝对只读 • 原始路径/大小写/命名即 Provenance • 零原地改动 │
└──────────────────────────────┬──────────────────────────────┘
                               │ 源保真/可追溯派生 (Source-faithful / Traceable Derivation)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. Traceable Source View (可追溯源视图层)                   │
│    语义块稀疏时间戳 Markdown + 精确时码侧车 (.cues.jsonl)  │
│    + 统一课程/案例清单 (Manifest)                          │
│    • 人类高可读 • 机器 Cue 级时码检索 • 严禁擅自加入教学结论  │
└──────────────────────────────┬──────────────────────────────┘
                               │ 知识提炼与概念综合 (Synthesis)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. Persistent Wiki (持久维基层)                             │
│    领域概念 (Concepts) / 工作流 (Workflows) / 跨源对比表     │
│    • 永久知识资产 • 显式区别于逐字稿 • 标注源视图引用锚点     │
└──────────────────────────────┬──────────────────────────────┘
                               │ 认知投影与消费适配 (Projections)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. Consumer Views (消费视图层)                              │
│    • NotebookLM 宽域研究中心捆绑包 (Coarse Cognitive Bundles)│
│    • CORE 深度研读 Notebook 专题包 (Finer Reading Bundles)  │
│    • corso-pbr-materials 选课与大纲映射视图                 │
└─────────────────────────────────────────────────────────────┘
```

### 层级职责定义

1. **不可变源层 (Immutable Source)**：原始交付物是法理证据与最终事实来源（Raw Truth）。任何文件系统的重命名、格式转码、目录扁平化均被严格禁止。
2. **可追溯源视图层 (Traceable Source View)**：将原始难以阅读的 SRT 碎片转换为人类可轻松通读的技术文稿，同时通过侧车文件保障机器可进行 Cue 级时间戳检索 (cue-level timestamp lookup)。本层必须保持客观忠实，不添加外围教学观点。
3. **持久维基层 (Persistent Wiki)**：从源视图中提炼并结构化的领域知识。**逐字稿（Transcript）不是知识（Wiki）**；Wiki 沉淀的是可复用的三维概念、节点逻辑与版本演进。
4. **消费视图层 (Consumer Views)**：针对特定工具或受众的下游导出视图。消费层只是临时或衍生的认知投影，不是真实数据源。

---

## 二、 稳定身份模型 (Stable Identity Model)

为避免对物理挂载点（如 `/Volumes/...`、盘符、本地绝对路径）和厂商混乱命名的依赖，系统引入两级稳定语义标识符：

### 1. 源资产包标识符 (`source_id`)
代表整个外部教程或教材版本包：
- **格式**：`{vendor}-{series}-{version}`（全部小写，短横线连接）
- **范例**：`cgcookie-core-v1-blender-4.2`

### 2. 课程/课时标识符 (`lesson_id`)
代表包内单一具体课时，由全名课程域、章节号与课时类型序号构成：
- **格式**：`{course-slug}-c{chapter:02d}-{type}{num:02d}`
- **类型标识符 (`type`)**：
  - `l`：普通课时（Lesson，如 `l01`, `l13`）
  - `e`：随堂练习/考核（Exercise，如 `e01`）
  - `b`：拓展/附赠课时（Bonus，如 `b01`）
- **规范范例**：
  - `materials-shading-c02-l13`（材质与着色第 2 章第 13 课：Principled BSDF）
  - `materials-shading-c04-e01`（材质与着色第 4 章练习 1：玻璃还是瓷器）
  - `texturing-c04-l19`（纹理第 4 章第 19 课：望远镜着色）
  - `texturing-c07-b02`（纹理第 7 章附赠 2：通道打包）

### 3. 全局唯一标识符 (Global Canonical ID)
由源标识符与课时标识符联合派生：
`{source_id}:{lesson_id}`（例如 `cgcookie-core-v1-blender-4.2:materials-shading-c02-l13`）

> [!IMPORTANT]
> **身份与定位分离纪律**：
> - 严禁在规范 ID 中使用模糊缩写（如禁止 `mat`、`tex` 作为规范标识符）。
> - 严禁将 `/Volumes/...`、文件名大小写、文件扩展名编码进 ID。
> - 物理路径仅作为 Manifest 中的定位器（Locators）。

---

## 三、 逐字稿 Markdown 规范 (Transcript Schema)

人类可读逐字稿文件采用 Markdown 格式，命名为 `{lesson_id}.transcript.md`。

### 1. 结构化元数据 (Frontmatter)
每篇逐字稿顶部必须包含严格的 YAML Frontmatter：

```yaml
---
schema_version: "source-view-v1"
source_id: "cgcookie-core-v1-blender-4.2"
lesson_id: "materials-shading-c02-l13"
title: "The Principled BSDF"
course: "Materials & Shading"
chapter: 2
lesson_num: 13
lesson_type: "lesson"  # lesson | exercise | bonus
duration_formatted: "00:10:39"
duration_seconds: 640.0
source_video_rel: "Materials-and-Shading-Videos-01/SHADING_C02_L13_PrincipledShaders.mp4"
source_caption_rel: "Materials-and-Shading-Videos-01/captions/SHADING_C02_L13_PrincipledShaders.mp4 (eng).srt"
caption_status: "AVAILABLE"  # 字幕状态域: AVAILABLE | NOT_PROVIDED | DESYNCED
cue_map_rel: "materials-shading-c02-l13.cues.jsonl"
related_assets: []
asset_relation_status: "HIGH_CONFIDENCE_NO_EXTERNAL_ASSET"  # 资产关联状态域: DIRECT_MATCH | HIGH_CONFIDENCE_NO_EXTERNAL_ASSET | NOT_PROVIDED | UNRESOLVED
last_derived_at: "2026-09-18"
---
```

### 2. 语义稀疏时间戳正文原则 (Semantic-Block Principle)
- **核心原则**：**一个语义块对应一个源派生时间锚点 (`one semantic block → one source-derived start-time anchor`)**。
- **排版结构**：
  ```markdown
  # [Title] 课程标题

  > 元数据导读块（所属课程、章节、总时长、视频源位置）

  ## [00:00:00] Part 1: 导论与背景

  **[00:00:00]** 讲师阐述该小节核心概念的连贯段落文本……

  ## [00:04:39] Part 7: 肥皂泡薄膜干涉实操

  **[00:04:39]** 讲师切入具体案例演示，操作 Principled BSDF Thin Film 参数……
  ```
- **纪律约束**：
  - 严禁机械式“每 60 秒硬切一个时间戳”。
  - 时间锚点应跟随自然语意转折、操作步骤切换、案例示范开始。
  - 具体的分段启发式算法（如每段包含多少个 cue、停顿秒数判断）属于派生执行细节，不写死在架构规范中。

---

## 四、 机器可读精确时码侧车规范 (Exact Timing Schema)

为确保在提高人读体验的同时不丢失任何精确时码证据，必须伴生生成机器可读的侧车文件：`{lesson_id}.cues.jsonl`。

### 1. 单行记录格式
采用行分隔 JSON（JSON Lines），每条记录对应原始字幕中的一个完整 Cue：

```json
{"cue": 153, "start_ms": 505240, "end_ms": 508100, "start_time": "00:08:25.240", "end_time": "00:08:28.100", "text": "Cycle will ignore this value because we have set it."}
```

### 2. 语义与证据约定
- **保留规范化字幕时码**：侧车文件严格保留源字幕中规范化的 cue 序号、起止时码与文本。除非经过专门的音视频对齐测量，不臆断字幕时码与音频轨绝对一致；源字幕本身可能包含厂商制作或封装引入的同步误差。
- **文本忠实**：保留字幕原始英文词句，仅去除 HTML 换行标签与多余空格。
- **终极真实来源**：原始 SRT/VTT 始终作为底层权威 Raw Timing 证据归档。当出现解析争议时，以原始字幕文件为准。

---

## 五、 状态域正交拆分与资产关系规范 (Status Domains & Asset Relations)

为避免状态混淆，规范严格解耦**字幕可用性状态**与**资产关联状态**两个正交域，严禁互相穿插：

### 1. 字幕状态域 (`caption_status`)
描述源字幕文件的供给与可用性情况：
- `AVAILABLE`：原厂提供了对应字幕，且完成结构化对齐。
- `NOT_PROVIDED`：原厂归档中明确未配发字幕（如 <50s 的导言预告或练习片头）。
- `DESYNCED`：字幕存在但发现严重脱节或时间轴损坏。

### 2. 资产关联状态域 (`asset_relation_status`)
描述课时与工程文件、材质贴图、参考图之间的客观证据关联，**严禁猜测或臆造不存在的资产**：

| 状态枚举值 | 判定定义 | 典型场景 |
| :--- | :--- | :--- |
| `DIRECT_MATCH` | 存在显式对应的工程文件或目录 | Texturing Ch03 L09 明确对应 `autoshop_01_2k.hdr` 所在文件夹 |
| `HIGH_CONFIDENCE_NO_EXTERNAL_ASSET` | 经抽样审计确认该课时使用会话内简单/默认几何体，且厂商归档未配发外部工程文件，无需外部资产 | Materials & Shading 抽样课时在视频中使用简单内建几何体演示，厂商 CourseFiles 仅有许可说明 |
| `NOT_PROVIDED` | 视频内容明确依赖外部工程资产，但厂商归档中明确缺失 | 视频演示了专用资产，但厂商包未提供对应工程文件 |
| `UNRESOLVED` | 资产关系模糊、名称不匹配或部分缺失 | Texturing Ch04 L19 提供了望远镜的 2 张 PNG 贴图，但在归档中未发现对应的三维网格/工程文件 |

### 3. 健壮性规则
- 缺少字幕的课时是**有效课时**（`caption_status: "NOT_PROVIDED"`）。
- 无 `.blend` 文件的课时是**有效课时**（`asset_relation_status: "HIGH_CONFIDENCE_NO_EXTERNAL_ASSET"`）。
- 仅提供部分辅助贴图的课时是**有效课时**（列出实际贴图，缺失资产记入 `unresolved_relations`）。

---

## 六、 伴生工作区物理存储架构 (Companion Workspace Model)

为彻底贯彻源文件不动与容量隔离原则，派生工作区与原始只读素材目录分离。

### 1. 逻辑目录布局
```text
<knowledge-root>/
└── cgcookie-core-v1-blender-4.2/
    ├── source-registry/                 # 源清单映射表与路径定位器 (Locators)
    │   └── registry.json
    ├── source-views/                    # 忠实派生层
    │   ├── transcripts/                 # *.transcript.md
    │   ├── cue-maps/                    # *.cues.jsonl
    │   ├── manifests/                   # lesson_manifest.json, case_manifest.json
    │   └── case-assets/                 # 提取或符号链接的高频案例辅助资源
    ├── wiki/                            # 提炼知识层 (概念/工作流/对比)
    │   ├── index.md
    │   ├── log.md
    │   ├── concepts/
    │   ├── workflows/
    │   └── comparisons/
    └── exports/                         # 下游消费导出层
        ├── notebooklm/                  # 粗粒度捆绑导出包
        └── project-views/               # corso-pbr-materials 选课视图
```

### 2. 引用约束
- 原始 15GB 素材包（无论位于 NAS `/Volumes/...` 还是本地只读盘）**绝不整体拷贝**到本工作区内，仅在 `source-registry/registry.json` 中保存相对或可配置的定位器路径。
- 工作区内仅产生文本、元数据与必要的轻量衍生索引。

---

## 七、 边缘场景兼容性验证 (Edge-Case Verification)

本规范在制定时已对真实审计中发现的 6 大边缘场景完成形式验证，无需针对特殊情况打补丁：

1. **标准音视频 + 字幕配对**：
   - 映射为 `caption_status: "AVAILABLE"`，正常生成双视图。
2. **低于 50 秒的导言或练习片头（无官方字幕）**：
   - 映射为 `caption_status: "NOT_PROVIDED"`，Markdown 保留 Frontmatter 与时长，正文标记无字幕，manifest 中正常保留课时节点。
3. **无外部课程资产（使用简单/内建网格演示）**：
   - 映射为 `asset_relation_status: "HIGH_CONFIDENCE_NO_EXTERNAL_ASSET"`，`related_assets: []`，消除对缺失文件的报错。
4. **显式关联单一外部资产（如独立 HDR）**：
   - 映射为 `asset_relation_status: "DIRECT_MATCH"`，`related_assets` 记录原厂相对路径。
5. **贴图存在但底层 3D 几何模型缺失（如望远镜着色实操）**：
   - 贴图记入 `related_assets`，缺失网格记入 `unresolved_relations: ["No corresponding 3D mesh/project file was found in the provided archive"]`，状态标记为 `UNRESOLVED`。
6. **厂商目录与文件名大小写/标点混乱**：
   - `captions` 与 `Captions`、文件名空格、逗号或特殊符号均被封闭在不可变源层与 Manifest 定位器中；上层逻辑与导出文件名一律采用标准化 `lesson_id`，实现彻底解耦。

---

## 八、 下游接口与版权红线 (Interfaces & Boundaries)

### 1. NotebookLM 消费接口 (`Source Views → Bundled NotebookLM Export`)
- **接口定位**：NotebookLM 是认知消费工具与研究交互界面，绝非事实存储库。
- **核心原则**：
  - NotebookLM 消费的是捆绑认知源（Bundled Cognitive Sources），而非机械镜像文件系统层面的单课时颗粒度。
  - Course Research Hub 倾向于粗粒度捆绑；CORE Deep Reading 可使用更细致的章节级捆绑；当针对特定技术疑难进行定向调研时，单个代表性课时亦可作为独立源导出。
  - 具体的捆绑边界与切分方案留待 Gate D 决策。

### 2. 公共代码仓库安全红线 (Public Repo Copyright Boundary)
- **绝对禁止提交到公共仓库**：
  - 任何原始视频与音频文件；
  - 任何原始字幕文件（SRT/VTT）；
  - 任何完整的派生逐字稿全文（Full derived transcripts）；
  - 任何商业工程文件、材质贴图及二进制资产。
- **允许且推荐提交到公共仓库**：
  - 本治理规范方法论文档；
  - 统计汇总档案（Source Profile）与不含版权正文的元数据清单；
  - 课程选型决议、架构决策（ADR）与学术分析笔记。
