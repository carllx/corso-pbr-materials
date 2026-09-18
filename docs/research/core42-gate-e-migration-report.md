# CG Cookie CORE V1 (Blender 4.2) Gate E 迁移执行与双向验证报告 (数据完整性修复版)

> **Authoritative Contract**: GitHub Issue #6 (`CORE V1 Source Governance & NotebookLM Export Architecture`)  
> **Mission Frontier**: Gate E — Bounded Migration (Data Integrity Repair)  
> **Status**: REPAIRED / READY FOR BROWSER REVIEW  
> **Review Anchors**: Comment ID `5723958348` (Revision Required) & Comment ID `5724260174` (Repair Plan Approved)  
> **Execution Date**: 2026-09-18  

---

## 1. 迁移执行概览与边界陈述

根据 GitHub Issue #6 针对 Gate E 的审查意见（Comment ID `5723958348` 与 `5724260174`），本轮任务对 Gate E 的派生物料及公开迁移报告实施了严格的**数据完整性修复与物理对账**。本次执行严格恪守以下治理红线：

1. **真实物理素材基准 (Authoritative Physical Raw Inventory)**：
   - 彻底废除并清除上一轮报告中因人工编写失误产生的污染条目与虚构文件名；
   - 课时清单、逐字稿、时间切片与导出包完全以 NAS 原始文件系统物理存在的文件名为唯一绝对真理（Single Source of Truth）。
2. **素材库不可变性客观记录 (Raw Invariant Accounting)**：
   - 原始素材库 574 个原厂文件无任何重命名、移动、删除、转码或原位修改；
   - 针对访问期间 macOS Finder 自动生成的 `.DS_Store` 元数据文件作显式客观隔离记录，不使用“绝对不可变/零环境副作用”等过于绝对的表述，严禁通过删除 `.DS_Store` 进行形式上的“回退”。
3. **哈希基准客观陈述 (Hash Evidence Discipline)**：
   - 纠正此前“与 Gate A/B 历史基准哈希一致”的不实表述。Gate A/B 未建立全量 574 文件的 SHA-256 基准；本轮由 Gate E 在 `source-registry/registry.json` 中正式建立了首套字幕文件的 SHA-256 基准。
4. **迁移范围严格受限 (Bounded Scope)**：
   - 仅限 `Materials & Shading`（22 个带字幕课时）与 `Texturing`（35 个带字幕课时），共计 57 个有效字幕课时；
   - 4 个真实存在的无字幕原厂视频严格登记为元数据实体（`NOT_PROVIDED`），严禁伪造文本。
5. **公有仓库零侵入与版权隔离 (Zero Copyright Infiltration)**：
   - 任何原厂音视频、字幕原文、派生逐字稿（Transcripts）、时间轴切片（Cue-maps）以及 NotebookLM 导出包均严格存放在本地/NAS 隔离伴随工作区，绝不提交至 Git 仓库。本仓库仅提交本份治理与验证报告。
6. **NotebookLM 未上传**：按照契约要求，未进行任何自动化上传或 API 调用。

---

## 2. 物理与逻辑路径映射

### 2.1 原始只读素材路径 (Immutable Raw Source Root)
```text
/Volumes/198.168.10.5/Download/CGCookie - Blender 4.2 Core Essentials - 9 Tutorials
```

### 2.2 伴随工作区路径 (Companion Workspace Root)
```text
/Volumes/198.168.10.5/Download/CGCookie CORE Knowledge/cgcookie-core-v1-blender-4.2
```

### 2.3 伴随工作区目录结构
```text
cgcookie-core-v1-blender-4.2/
├── source-registry/
│   └── registry.json                      # 原始素材全集文件级索引与 SHA-256 校验
├── source-views/
│   ├── transcripts/
│   │   ├── materials-shading/             # 22 个规范逐字稿 (.transcript.md)
│   │   └── texturing/                     # 35 个规范逐字稿 (.transcript.md)
│   ├── cue-maps/
│   │   ├── materials-shading/             # 22 个高精时间轴对齐切片 (.cues.jsonl)
│   │   └── texturing/                     # 35 个高精时间轴切片 (.cues.jsonl)
│   └── manifests/
│       ├── lesson_manifest.json           # 61 个课时（57 available + 4 not provided）事实清单
│       └── case_manifest.json             # 4 个实测案例资产客观映射表 (明确定位器类别)
├── wiki/
│   └── README.md                          # 知识沉淀层边界陈述（当前冻结为空骨架）
└── exports/
    └── notebooklm/                        # 认知源导出视图（5 大标准导出包）
        ├── README.md                      # 导出包说明与摄入指引
        ├── CORE42_OVERVIEW.md             # 架构概览与课时索引
        ├── CORE42_MATERIALS_AND_SHADING.md# 材质与着色全套逐字稿与元数据
        ├── CORE42_TEXTURING_FOUNDATIONS.md# 纹理基础 (Ch1–4)
        ├── CORE42_TEXTURING_WORKFLOWS.md  # 纹理进阶与实战 (Ch5–7)
        └── CORE42_CASE_INDEX.md           # 客观案例资产索引（三类定位器，零推测配方）
```

---

## 3. 原始数据不可变性对账 (Raw Source Invariant Reconciliation)

在执行迁移与本次数据对账中，对原始素材目录进行了完整的物理遍历核验：

| 校验指标 | 契约基准值 (Baseline) | 物理测得值 (Post-Migration) | 状态 | 备注 |
| :--- | :--- | :--- | :--- | :--- |
| **Vendor 核心文件数** | 574 | 574 | **PASS** | 严格一致 |
| **Vendor 核心字节数** | 16,223,406,914 字节 | 16,223,406,914 字节 | **PASS** | 严格一致 (~15.11 GiB) |
| **OS 产生元数据文件** | 0 | 1 (`.DS_Store`) | **RECORDED** | 12,292 字节，显式隔离登记 |

> [!IMPORTANT]
> **关于系统元数据文件 `.DS_Store` 的规范记录**：  
> `Vendor payload invariant preserved; source-root filesystem immutability was not absolute because OS metadata (.DS_Store) appeared during access.`  
> 经核验，原厂 574 个文件未发生任何重命名、移动、删除或转码。根目录下出现的 `.DS_Store`（12,292 字节）由 macOS 访问过程产生，已在 `registry.json` 中作为 OS 元数据专门记录，严禁通过删除该文件来做虚假的“零变动”粉饰。

> [!NOTE]
> **关于哈希基准的客观声明**：  
> Gate A/B 阶段仅对文件数量、体积与字幕配对进行了统计验证，并未建立全量 574 个大文件的 SHA-256 历史哈希基准。因此，Gate E 在 `registry.json` 中计算的哈希值被定义为**当前建立的全新哈希基准 (current hash baseline)**，而非历史前后哈希不变性的证明。

---

## 4. 派生物料统计与规范性校验 (Derivation Metrics)

### 4.1 物理文件系统课时与字幕分布真相
经对 NAS 原始视频目录的直接物理扫描与对账，课时与字幕的真实分布如下：

```text
Materials & Shading:
  total videos: 23
  AVAILABLE (带字幕): 22
  NOT_PROVIDED (无字幕): 1

Texturing:
  total videos: 38
  AVAILABLE (带字幕): 35
  NOT_PROVIDED (无字幕): 3

Combined (两门核心课程汇总):
  manifest rows: 61
  AVAILABLE: 57
  NOT_PROVIDED: 4
```

### 4.2 真实无字幕视频清单 (Caption Status = NOT_PROVIDED)
NAS 磁盘上**真实存在**且原厂确实未附带字幕的 4 个视频为：
1. `Materials-and-Shading-Videos-01/SHADING_C04_E01_IsItGlassOrPorcelain.mp4` (Ch4 练习)
2. `Texturing-Videos-01/TEXTURES_C01L00_IntroToTextures.mp4` (Ch1 导览)
3. `Texturing-Videos-01/TEXTURES_C05E01_ProceduralRustAndMetal.mp4` (Ch5 练习)
4. `Texturing-Videos-01/TEXTURES_CH07E01_Let’sTextureShadeAndRenderTheRobot!.mp4` (Ch7 练习)

> [!CAUTION]
> **对上一轮报告中 4 个污染/虚构文件名的纠偏声明**：  
> 上一轮报告文本中列出的以下 4 个文件名已被彻底废除并证实为非原厂事实：
> - `TEXTURES_C01L000_Introduction.mp4` ❌（虚构命名，真实文件名为 `TEXTURES_C01L00_IntroToTextures.mp4`）
> - `TEXTURES_C04L019.5_Exercise-AddingDirtToCeramic.mp4` ❌（完全虚构，磁盘不存在）
> - `TEXTURES_C05L020_Important-HowToFollowAlong.mp4` ❌（完全虚构；磁盘实际为 `TEXTURES_C05L020_IntroToProceduralTexturing.mp4` 且包含正常可用字幕）
> - `TEXTURES_C07L036_Exercise_TexturingAFlashlight.mp4` ❌（完全虚构，磁盘不存在）  
> 经全量磁盘与伴生工作区扫描，上述 4 个虚构名称未渗入任何生成的逐字稿或 Cue-map，当前伴生工作区清单与导出包已 100% 保持纯洁。

### 4.2 派生逐字稿与 Cue-Map 规模
- **Transcripts 总数**: 57 个 Markdown 文件 (全部通过物理 1:1 映射核验)
  - `materials-shading`: 22
  - `texturing`: 35
- **Cue-Maps 总数**: 57 个 JSONL 文件 (全部通过物理 1:1 映射核验)
  - `materials-shading`: 22
  - `texturing`: 35
- **总字幕 Cue 数量**: 5,455 条独立时间轴对齐片段
- **总派生字词数 (Word Count)**: 47,994 词
  - `Materials & Shading`: 1,465 cues / 12,516 words
  - `Texturing`: 3,990 cues / 35,478 words

---

## 5. CASE INDEX 证据审计与分类细化 (Case Evidence Audit)

按照 Browser Review 绑定指令，对所有潜在案例实施了严格的证据链审计，将案例定位器严格限定为三类标准事实类目：
1. `asset-backed demo`：包含原厂归档资产且在视频中演示的定位器；
2. `demo-only`：无外部归档资产（默认网格），但在视频中存在明确起始时码和完整演示的定位器；
3. `UNRESOLVED asset relation`：原厂资产不全（例如仅有贴图缺失 3D 模型工程）的未决定位器。

### 5.1 案例审计与保留/剔除结果表

| 案例名称 | 对应课时 ID | 定位器类别 (Locator Class) | 真实源视频 | 源时码锚点 | 资产状态与审计判定 |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **Managing Texture Data (HDR)** | `texturing-c03-l09` | `asset-backed demo` | `TEXTURES_C03L09_ManagingTextureData.mp4` | `00:00:13` | **RETAINED** (`DIRECT_MATCH`)。归档资产 `autoshop_01_2k.hdr` 真实存在。 |
| **Shading Binoculars with PBR Textures** | `texturing-c04-l19` | `UNRESOLVED asset relation` | `TEXTURES_C04L019_PrincipledShaderShadingBinoculars.mp4` | `00:00:19` | **RETAINED** (`UNRESOLVED`)。提供 `Binoculars_Opacity.png` 与 `Sand_Metallic.png`，但原厂归档缺失 3D 模型网格。 |
| **Soap Bubble Thin Film Demo** | `materials-shading-c02-l13` | `demo-only` | `SHADING_C02_L13_PrincipledShaders.mp4` | `00:04:19` | **RETAINED** (`HIGH_CONFIDENCE_NO_EXTERNAL_ASSET`)。讲师在 00:04:19 明确演示肥皂泡 Thin Film，默认网格。 |
| **Glass Dispersion and Caustics Demo** | `materials-shading-c04-l20` | `demo-only` | `SHADING_C04_L20_RenderingGlassUnderstandingDispersionAndCaustics.mp4` | `00:01:21` | **RETAINED** (`HIGH_CONFIDENCE_NO_EXTERNAL_ASSET`)。讲师在 00:01:21 明确演示玻璃色散与焦散，默认网格。 |
| *Car Paint* | `materials-shading-c02-l13` | *(无)* | — | — | **REMOVED**。字幕中仅为讲师随口举例（clear coat 类比），无独立案例演示，无工程资产。 |
| *Gold* | `materials-shading-c02-l07` | *(无)* | — | — | **REMOVED**。仅为调节颜色滑块的临时操作，无独立工程资产。 |
| *Table Wood* | `texturing-c06-l024` | *(无)* | — | — | **REMOVED**。经核实为对手绘板 "tablet pen" 及颜色色板命名 "wood" 的严重误读，原厂根本无木桌资产。 |

---

## 6. NotebookLM 导出包体积与认知负荷对账

导出的 5 个核心 Markdown 文档位于伴生工作区 `exports/notebooklm/`：

| 导出文件名 | 字节数 (Bytes) | 涵盖范围与课时数 | 设计考量与负荷评估 |
| :--- | :--- | :--- | :--- |
| `CORE42_OVERVIEW.md` | 6,876 B | 架构总览、课程背景、全 61 课时索引 | ~7 KB 极轻量，提供全局导航图谱 |
| `CORE42_MATERIALS_AND_SHADING.md` | 85,735 B | 23 课时 (22 逐字稿 + 1 练习元数据存根) | ~84 KB，完整覆盖材质与着色理论/节点系统 |
| `CORE42_TEXTURING_FOUNDATIONS.md` | 92,695 B | Ch1–4 共 20 课时 (19 逐字稿 + 1 导览存根) | ~91 KB，专注纹理基础、UV 投射与烘焙基础 |
| `CORE42_TEXTURING_WORKFLOWS.md` | 130,519 B | Ch5–7 共 18 课时 (16 逐字稿 + 2 练习存根) | ~128 KB，专注实战手绘、材质绘制与望远镜全流程 |
| `CORE42_CASE_INDEX.md` | 2,498 B | 4 大实测客观案例定位器 (三类标准定义) | ~2.5 KB，纯客观资产与源字幕时码定位，零参数配方 |

**验证结论**：两份 Texturing 切分包实现了精确互斥且完全覆盖（20 + 18 = 38 课时，重叠度为 0）；Materials 完整收录 23 课时；所有 uncaptioned 存根均精确引用 NAS 真实文件名；Case Index 绝无推测配方或幻觉条目。

---

## 7. 强化版自动化检验流水线通过记录 (Automated Verification Results)

通过新编写的强化版专用验证脚本 `verify_gate_e_repaired.py`，对物理文件系统、元数据清单、57 份逐字稿及导出包执行了 7 大深度断言，全数通过（PASS）：

```text
==========================================================
GATE E REPAIRED AUTOMATED STRUCTURAL & INTEGRITY VERIFIER
==========================================================

[Check 1] Raw Source Integrity & OS Metadata Accounting:
   Vendor payload files: 574 (expected: 574)
   Vendor payload bytes: 16223406914 (expected: 16223406914)
   OS metadata files:    1 (recorded: .DS_Store)

[Check 2] Ground Truth Scan from NAS Disk:
   Materials raw videos on disk:   23 (expected: 23)
   Materials raw captions on disk: 22 (expected: 22)
   Texturing raw videos on disk:   38 (expected: 38)
   Texturing raw captions on disk: 35 (expected: 35)

[Check 3] Lesson Manifest Integrity & Exact Distribution:
   Total manifest rows:           61 (expected: 61)
   Materials manifest rows:       23 (expected: 23)
     - AVAILABLE:                 22 (expected: 22)
     - NOT_PROVIDED:              1 (expected: 1)
   Texturing manifest rows:       38 (expected: 38)
     - AVAILABLE:                 35 (expected: 35)
     - NOT_PROVIDED:              3 (expected: 3)
   Actual NOT_PROVIDED paths match expected 4 exactly: True

[Check 4] Transcripts & Cue Maps 1:1 Exhaustive Resolution:
   Materials transcripts: 22 (expected: 22)
   Materials cue-maps:    22 (expected: 22)
   Texturing transcripts: 35 (expected: 35)
   Texturing cue-maps:    35 (expected: 35)
   Total transcripts:     57 (expected: 57)
   Total cue-maps:        57 (expected: 57)
   Consumed unique videos across transcripts:   57 (expected: 57)
   Consumed unique captions across transcripts: 57 (expected: 57)

[Check 5] Cues & Word Counts Aggregate Reconciliation:
   Total cues:  5455 (expected: 5455)
   Total words: 47994 (expected: 47994)

[Check 6] NotebookLM Export Bundles Verification:
   Texturing Foundations lessons: 20 (expected: 20)
   Texturing Workflows lessons:   18 (expected: 18)
   Texturing Overlap:             0 (expected: 0)
   Materials bundle lessons:      23 (expected: 23)

[Check 7] CASE INDEX Audit & Strict Schema Enforcement:
   Total cases in case_manifest: 4

==========================================================
ALL 7 REPAIRED INTEGRITY & STRUCTURAL CHECKS PASSED PERFECTLY!
==========================================================
```

---

## 8. 交付状态与终态标记

Gate E 迁移产物的数据完整性修复与物理对账全部完成，污染条目已清除，所有映射经强化验证流水线检验 100% 严密。

**TERMINAL STATUS**: `CORE42_GATE_E_MIGRATION_REPAIRED_READY_FOR_BROWSER_REVIEW`
