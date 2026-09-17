# Gate 3B Blender 5.2 LTS 受控修订探针报告 (方法修正版)

> **探针阶段**：Stage 2 Gate 3B — Practice Implementation Re-baselining & Sufficiency Probe  
> **审查基准与依据**：GitHub Issue #5 (Comment ID: `5706879947`)、Browser Review Finding (2026-09-17)  
> **核心探针问题**：在工具中立（Tool-neutral）的受控修订要求下，Blender 5.2 LTS 是否已经足够形成清楚、可恢复、可解释的本科教学实现？

---

## 1. 方法修正与证据边界声明 (Method Correction & Evidence Scope)

> [!IMPORTANT]
> **方法边界修正 (Method Correction)**：  
> 本探针中 initial / revision #1 / save-reopen / revision #2 的核心操作实际通过 **Blender Python / headless automation** (`Blender -b -P run_blender_controlled_revision.py`) 执行。  
> **本探针已确证的边界 (What was validated)**：
> 1. 数据与节点拓扑的表达可行性 (Representation feasibility)；
> 2. 节点与通道依赖结构的物理完整性 (Node/data dependency structure)；
> 3. 保存、关闭与重开工程的数据持久性 (Save/reopen persistence)；
> 4. 渲染状态响应与参数隔离性 (Render-state changes & parameter isolation)。
> 
> **本探针明确未验证的边界 (What was NOT validated — Pending Manual GUI Gate)**：
> 1. 人工 GUI 界面控件的可发现性 (Manual GUI discoverability)；
> 2. 学生直面的真实 GUI 操作摩擦 (Student-visible editing friction)；
> 3. 教师端纯手工备课与调试负担 (Teacher manual preparation burden)；
> 4. 真实课堂排错与踩坑摩擦 (Real troubleshooting burden)；
> 5. 人类操作者的真实认知负荷 (Human cognitive load)；
> 6. 在脱离预先脚本逻辑的情况下，界面控件是否直观立等可寻。
> 
> 因此，本报告的证据结论严格定性为 **`BLENDER_SCRIPTED_CONTROLLED_REVISION_FEASIBILITY_POSITIVE`**，**不得等同于人类 GUI 教学充分性已达成**。教学充分性判定留待后续人工 GUI 门禁 (Human Manual GUI Gate)。

---

## 2. 证据状态与事实标签体系 (Fact Labels)

本报告严格区分客观事实、实测观察与教学推论：
- **`[VERIFIED LOCAL FACT]`**：本机实际执行命令、路径检查、版本输出与哈希校验确证的物理事实；
- **`[OBSERVED SCRIPTED RESULT]`**：在 Blender 5.2.2 LTS 运行环境下通过脚本自动化执行干跑所记录的数据与渲染状态；
- **`[TEACHING HYPOTHESIS]`**：基于脚本数据结构对教学认知负荷的初步假设（尚未经人工 GUI 验证）；
- **`[UNKNOWN / PENDING HUMAN GATE]`**：必须由真实人类操作者通过 Blender GUI 验证的体验事实。

---

## 3. 运行环境与基线资产事实 (Environment & Assets)

### 3.1 运行环境双版本并存核验
- `[VERIFIED LOCAL FACT]`: 本机原有 `/Applications/Blender.app` 保持完全未动，经 app 内可执行文件核验为 `Blender 4.5.1 LTS` (Hash: `b0a72b245dcf`, Built: 2025-07-29)；
- `[VERIFIED LOCAL FACT]`: 依据官方发布源 `https://download.blender.org/release/Blender5.2/` 下载官方 `blender-5.2.2-macos-arm64.dmg`；
- `[VERIFIED LOCAL FACT]`: DMG SHA256 校验值为 `dc4125399b8bfefe283cc1624d6cfc7809d1cac20ace51072127eb371f31f210`，与官方发布的 `blender-5.2.2.sha256` 100% 严格一致；
- `[VERIFIED LOCAL FACT]`: 部署为 `/Applications/Blender 5.2.2 LTS.app`，经 app 内可执行文件核验为 `Blender 5.2.2 LTS` (Hash: `d13f752e3b9c`, Built: 2026-09-14 15:14 / Release 2026-09-15)；
- `[VERIFIED LOCAL FACT]`: Substance 3D Painter 独立应用在本机未安装，本轮未执行任何 Painter 安装。

### 3.2 教师预置测试资产说明
- `[VERIFIED LOCAL FACT]`: 依据教学规范（建模与 UV 仅为支撑知识），由教师端预置极简、中性且规范展开 UV 的硬表面零件（倒角机械盖板 `BevelPlate`，尺寸 $2.0 \times 1.4 \times 0.3\,\text{m}$，边缘平滑倒角，Smart UV 投影展开，搭配三点面光源与摄像机）。
- 标记声明：`Teacher-provided setup / not part of tested student authoring workload`。
- 本地工程路径：`/Users/yamlam/.gemini/antigravity/brain/7be0ae4e-b9e2-409d-8be4-5d858898125e/scratch/gate3b/controlled_revision_base.blend`。

---

## 4. 脚本自动化受控修订流程数据 (Scripted Probe Execution)

### 阶段 1：初始材质搭建 (Initial Material Setup)
- **因果分层关系**：
  - 底层基底 (Base Metal)：`Principled BSDF`，铸钢色 (`RGB: 0.24, 0.25, 0.27`)，金属度 `1.0`，粗糙度 `0.25`；
  - 表层涂装 (Coating Paint)：`Principled BSDF`，安全橙漆 (`RGB: 0.82, 0.40, 0.05`)，非金属 `0.0`，粗糙度 `0.45`；
- **空间遮罩控制**：`Texture Coordinate (Object)` $\to$ `Noise Texture (Scale 4.5, Detail 4.0)` $\to$ `ColorRamp`（黑位 `0.42`，白位 `0.48`）；
- **混合输出**：`Mix Shader`（`Fac = ColorRamp`，`Shader1 = Coating`，`Shader2 = Base Metal`）$\to$ `Material Output`；
- `[OBSERVED SCRIPTED RESULT]`: 成功生成 `controlled_revision_initial.blend` (SHA256: `64749ee7fdc34504...`) 并渲染验证图 `probe_initial_render.png`。

### 阶段 2：第一次受控修订 (Revision #1 — 局部磨损扩大与表面粗化)
- **修订参数设定**：
  - 空间范围调整：`ColorRamp` 滑动色标调整为 `0.35` 与 `0.42`；
  - 属性物理联动：`Base_Metal` 节点 `Roughness` 从 `0.25` 调整为 `0.40`；
- `[OBSERVED SCRIPTED RESULT]`: 
  - 脚本检验确证涂层 Base Color 保持 `(0.82, 0.40, 0.05)`，Roughness 保持 `0.45`，Metallic 保持 `0.0`，非目标数据未受污染；
  - 成功保存 `controlled_revision_r1.blend` (SHA256: `af2a6d89c6abb598...`) 并渲染 `probe_revision1_render.png`。

### 阶段 3：保存、关闭进程与重新加载恢复 (Save / Close / Reopen Verification)
- **操作**：完全退出 Blender 进程，释放内存，重新启动 `Blender 5.2.2 LTS` 并打开 `controlled_revision_r1.blend`。
- `[OBSERVED SCRIPTED RESULT]`:
  - 材质 `M_Coated_Plate` 完整恢复；
  - 数据块中 `Mask_ColorRamp`、`Base_Metal`、`Coating_Enamel`、`Mix_Shader` 节点标识与位置完好；
  - `ColorRamp` 色标值 (`0.35/0.42`) 与 `Base_Metal` 粗糙度 (`0.40`) 读数一致。

### 阶段 4：第二次受控修订 (Revision #2 — 二次范围微调与属性独立解耦调整)
- **修订参数设定**：
  - 空间滑块微调至 `0.30/0.38`；
  - `Base_Metal` Base Color 调深至 `0.13, 0.14, 0.15`；
- `[OBSERVED SCRIPTED RESULT]`:
  - 涂层非目标通道数据再次核验证明保持 `0.45` 粗糙度与 `0.0` 金属度不变；
  - 成功保存 `controlled_revision_r2.blend` (SHA256: `f5dac7f30c66654d...`) 并渲染 `probe_revision2_render.png`。

---

## 5. 观察字段客观记录与边界修正 (Ten Observation Fields)

| 观察字段 | 脚本实测记录 (Scripted Fact) | 教学推论与待人工检验边界 (Human Gate Status) |
| :--- | :--- | :--- |
| **1. 教师准备负担 (Teacher Prep)** | 脚本建立中性零件与材质耗时数秒。 | **[PENDING HUMAN GATE]** 教师在无脚本辅助下纯手工在 GUI 中布置场景的实际分钟数与心智负担尚未检验。 |
| **2. 学生直面概念量 (Student Concepts)** | 涉及 BSDF、Mix Shader、ColorRamp、Texture Coordinate。 | **[TEACHING HYPOTHESIS]** 概念直接映射 PBR 物理分层；但界面中查找这些节点的路径需手工验证。 |
| **3. 需心智跟踪的表示形式 (Mental Reps)** | 2 个材质块 + 1 个遮罩流。 | **[TEACHING HYPOTHESIS]** 拓扑结构直观；但学生是否能轻易分清哪个节点控制哪层有待人工体验。 |
| **4. 编辑局部性 (Edit Locality)** | 脚本修改只触碰指定输入端口，未引发全局数据污染。 | **[OBSERVED SCRIPTED RESULT]** 节点结构具备天然的数据局部隔离能力。 |
| **5. 显式意图依赖 (Intentional Deps)** | 单一遮罩线同时驱动 BaseColor/Roughness/Metallic 边界切换。 | **[OBSERVED SCRIPTED RESULT]** 物理因果依赖在连线上显式可见。 |
| **6. 隐蔽/黑箱依赖 (Hidden Deps)** | 无隐藏图层通道或跨图层 Passthrough 混合。 | **[OBSERVED SCRIPTED RESULT]** 无黑箱隐蔽驱动。 |
| **7. 二次修订摩擦度 (Second-revision Friction)** | 脚本直接给对应属性赋值，无重构开销。 | **[PENDING HUMAN GATE]** 人工操作者通过鼠标拖动色标与滑块时的直观度与阻力尚未经过检验。 |
| **8. 保存与重新打开恢复度 (Save/Reopen)** | `.blend` 二进制文件成功保存并重开，数据块完全还原。 | **[OBSERVED SCRIPTED RESULT]** 底层持久化与序列化机制 100% 成立。 |
| **9. 排错与查阅文档需求 (Troubleshooting)** | 运行无崩溃、无 shader 报错。 | **[PENDING HUMAN GATE]** 真实学生误连连线或选错输入接口时的排错难度尚未实测。 |
| **10. 导出影响与第二工具动机 (Export/Second-tool)** | `Mix Shader` 跨引擎导出需烘焙或单 BSDF 混合。 | **[UNKNOWN / NOT TESTED]** 导出流水线与是否需要 Painter 仍保持待定 (Unresolved)。 |

---

## 6. 决策门禁裁决修正 (Corrected Decision Gate Finding)

### **`BLENDER_SCRIPTED_CONTROLLED_REVISION_FEASIBILITY_POSITIVE`**
- **当前定性**：脚本自动化验证证明 Blender 5.2.2 LTS 在数据表示、节点结构、受控修改与文件持久化上**在技术上完全可行**；
- **人类 GUI 教学充分性状态**：**`HUMAN_GUI_SUFFICIENCY: NOT YET TESTED`**；
- **Painter 探针决策状态**：**`PAINTER_PROBE_NEEDED: UNRESOLVED UNTIL HUMAN GUI GATE`**；
- **核心纪律约束**：在完成人类真实 GUI 手工门禁之前，严禁启动下游交付探针 (Downstream Delivery Probe)，严禁安装 Substance 3D Painter，严禁冻结实践主线。

---

## 7. 资产归档与哈希记录 (Artifact Ledger)

- **基线几何**：`controlled_revision_base.blend`
- **初始工程**：`controlled_revision_initial.blend` (SHA256: `64749ee7fdc3450410ff10a8c2f1f5166299b8ea0ea1d8ea83446bf4fc911f93`)
- **修订 1 工程**：`controlled_revision_r1.blend` (SHA256: `af2a6d89c6abb5985dc7321e25e9d9972bc58a0b0d6118aa95c0245bca532a82`)
- **修订 2 工程**：`controlled_revision_r2.blend` (SHA256: `f5dac7f30c66654df6bf532677ceb264e16ff7284da828fe539b56f2ec550785`)
- **人工 GUI 门禁起始工程**：`controlled_revision_manual_gui_start.blend`
