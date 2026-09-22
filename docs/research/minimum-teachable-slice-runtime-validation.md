# Minimum Teachable Slice Runtime Validation: Poly Haven Vintage Flashlight

> **执行工单**：GitHub Issue #9 — WU1: Minimum Teachable Slice Runtime Validation  
> **验证目标**：验证核心候选资产 Poly Haven Vintage Flashlight 是否能在真实 Blender 5.2.2 环境中承载最小教学闭环（Teaching Slice）：`open → observe → bounded material edit → protected-area check → save → fully quit Blender → reopen → verify first edit → second edit → save → minimal external-output smoke test`  
> **执行日期**：2026-09-22  
> **执行分支**：`research/issue-9-minimum-teachable-slice-runtime-validation`  
> **判定结论 (Verdict)**：**PASS — TEACHING SLICE VIABLE**

---

## 1. 事实标签与证据纪律 (Evidence Discipline)

本报告所有数据与结论严格遵循以下四类标签体系：
- **`[VERIFIED]`**：本次在本机由真实命令、实际文件校验及 Blender 5.2.2 LTS 进程实机测量确证的事实；
- **`[REPORT / OWNER INPUT]`**：来自项目已确立规范或上游官方声明，本次未产生争议的输入项；
- **`[INFERRED]`**：基于已知测量事实与几何/材质拓扑推导出的结论；
- **`[NOT YET TESTED]`**：本次实机切片范围之外、尚未完成实测的项目（严禁偷换为已通过）。

> [!IMPORTANT]
> **关键边界纪律声明**：
> 1. **存在 UV ≠ UV 无重叠**：模型存在 UV 展开坐标，不等于在所有 LOD 或微小岛屿完全无重叠；
> 2. **教师干跑通过 ≠ 学生机房通过**：本机 macOS Apple Silicon 下测试通过，不代表全体跨平台（Windows/Linux）学生机房无环境差异；
> 3. **当前 5.2.2 通过 ≠ 未来版本全兼容**：仅代表特定构建版本下的物理成立性；
> 4. **自动化脚本/干跑耗时 ≠ 学生实际操作耗时**：教师干跑时间（秒级/分钟级）严禁直接作为 160 分钟课堂中初学者的完成时间预算。

---

## 2. 真实执行环境坐标 (Runtime Coordinates)

- **操作系统**：`[VERIFIED]` macOS Darwin 24.6.0 (arm64, Apple Silicon)
- **Blender 物理路径**：`[VERIFIED]` `/Applications/Blender 5.2.2 LTS.app/Contents/MacOS/Blender`
- **Blender 详细版本**：`[VERIFIED]` Blender 5.2.2 LTS
  - Build Date: `2026-09-15 01:49:19`
  - Build Commit Date: `2026-09-14 15:14`
  - Build Hash: `d13f752e3b9c`
  - Build Branch: `blender-v5.2-release`
  - Build Platform: `Darwin (Apple Silicon)`
- **备用版本（未作为主验证环境）**：`[VERIFIED]` `/Applications/Blender.app` (Blender 4.5.1 LTS)

---

## 3. 资产溯源与原型归档 (Asset Provenance & Local Prototype)

- **资产名称**：`[REPORT / OWNER INPUT]` Poly Haven — Vintage Flashlight
- **创作者**：`[REPORT / OWNER INPUT]` Omar M. El-Safy
- **官方主页**：`[REPORT / OWNER INPUT]` https://polyhaven.com/a/vintage_flashlight
- **官方 API 原型**：`[VERIFIED]` `https://api.polyhaven.com/files/vintage_flashlight`
- **版权协议**：`[REPORT / OWNER INPUT]` CC0 1.0 Universal Public Domain Dedication
- **下载规格**：`[VERIFIED]` 1K 分辨率最小完整版本（包含 `.blend` 与全部 5 张 PBR 贴图）
- **本地原型路径**：`[VERIFIED]` `.scratch/prototype/vintage_flashlight_1k/`（配置于 `.git/info/exclude`，不污染公共 git 提交树）
- **核心文件与哈希核验**：`[VERIFIED]`
  - `vintage_flashlight_1k.blend` (MD5: `204621d8a6c2b0c4fdc378abc1cf7017`, 330,005 字节)
  - `textures/vintage_flashlight_diff_1k.jpg` (MD5: `3a402729b84c43bcd4150dc93013d35a`, 550,114 字节)
  - `textures/vintage_flashlight_rough_1k.exr` (MD5: `dc5cfb63b5ce8eba6305c21b995616b0`, 560,523 字节)
  - `textures/vintage_flashlight_metal_1k.exr` (MD5: `6415e8b9c6f3af876731143e905d846c`, 515,419 字节)
  - `textures/vintage_flashlight_nor_gl_1k.exr` (MD5: `9221ec89ff0bb1d09c311f23b4ea0418`, 334,749 字节)
  - `textures/vintage_flashlight_alpha_1k.png` (MD5: `bb8cabe38ee1875a0aec28d99e48d600`, 30,022 字节)

---

## 4. 资产结构与教学接缝 (Asset Structure & Teaching Seam)

### 4.1 原始资产几何与材质结构 (Inspected Asset Structure)

- **场景对象**：`[VERIFIED]` 仅包含 1 个网格对象 `vintage_flashlight`（无预置摄像机与灯光）。
- **几何拓扑数据**：`[VERIFIED]`
  - 顶点数 (Vertices): 5,417
  - 边数 (Edges): 10,694
  - 多边形面数 (Polygons): 5,283
  - 估算三角面数 (Estimated Tris): 10,562（符合官方标称 ~11K tris）
  - UV 贴图层：`map1` (U=[0.0039, 0.9961], V=[0.0039, 0.8806])
- **网格连通分量 (Loose Parts)**：`[VERIFIED]` 包含 18 个物理连通组件（Loose Parts）。
- **官方原始材质槽分配**：`[VERIFIED]`
  - Slot 0: `vintage_flashlight` (5,227 面，涵盖 17 个部件)
  - Slot 1: `vintage_flashlight_glass` (56 面，涵盖 Comp 14 玻璃镜片)

### 4.2 教学接缝划分 (Teaching Seam)

官方原生资产存在一个教学摩擦点：除了玻璃镜片具有独立槽外，外壳与所有内部机械螺丝、开关、反光罩均共享同一个 Material Slot 0。若学生直接在 Slot 0 上修改参数，会导致受保护部件（如反光罩、螺栓、灯头）被全面意外污染。

因此，实验确定了清晰的材质槽隔离接缝（Material Slot Seam）：
- **STUDENT-OWNED / EDITABLE (学生有界编辑区域)**：`[VERIFIED]`
  - 部件范围：主体外壳 (Main Body Shell)，由 Comp 1（下底壳，812 面）与 Comp 3（顶盖，650 面）组成，共计 **1,462 面**（占总面数 27.67%）。
  - 接缝实现：新增第三个材质槽（Slot index 2）`vintage_flashlight_body`，复制自原始材质并将该 1,462 面指派给 Slot 2。
- **TEACHER/VENDOR-PROVIDED / PROTECTED (受保护部件区域)**：`[VERIFIED]`
  - 玻璃镜片 (Glass lens): Comp 14（56 面，Slot 1 `vintage_flashlight_glass`）；
  - 灯头反光罩与部件 (Reflector / collar / bulb socket): Comp 5（404 面）、Comp 13（128 面）；
  - 灯头外壳 (Head lamp bezel): Comp 2（800 面）；
  - 开关滑动组件 (Switch assembly): Comp 4、8、10、16、18（共 1,032 面）；
  - 手柄挂扣 (Handle & brackets): Comp 6、11（共 590 面）；
  - 铰链、螺栓与铆钉 (Screws, rivets & rings): Comp 7、9、12、15、17（共 811 面）；
  - 以上所有受保护部件严格保留在 Slot 0（3,765 面）与 Slot 1（56 面）中，维持官方 Vendor 原生状态。

---

## 5. 12步运行时验证全流程证据 (Runtime Execution Log)

| 步骤 | 操作目标 | 实际执行详情 | 结果与证据 | 状态 |
| :--- | :--- | :--- | :--- | :--- |
| **Step 1** | Open known starting state | 打开官方 `vintage_flashlight_1k.blend` | 5,417 顶点，5,283 面，2 个原生槽载入完好 | `[VERIFIED]` PASS |
| **Step 2** | Observe in stable environment | 搭建 `Cam_Obs` 与 `Light_Obs` (Sun 2.5) 稳定观测机位，渲染 Baseline | 成功生成 `render_baseline.png` (291KB) | `[VERIFIED]` PASS |
| **Step 3** | First bounded material edit | 在 `vintage_flashlight_body` (Slot 2) 节点树中，在 Base Color 贴图后串联 `ShaderNodeMix` (RGBA MULTIPLY, Factor=0.85, Color=`[0.32, 0.58, 0.22, 1.0]`) | 主体外壳呈现风化军绿涂层 | `[VERIFIED]` PASS |
| **Step 4** | Protected-area check | 检查 Slot 0 (3,765 面) 与 Slot 1 (56 面) 的节点树与面索引 | Slot 0 节点数 12，Slot 1 节点数 13，面归属零变动，未受任何篡改 | `[VERIFIED]` PASS |
| **Step 5** | Save state & render evidence | 保存工程为 `vintage_flashlight_step1.blend` (327KB)，并渲染图像 | 成功输出 `render_step1_first_edit.png` (281KB)；Step 1–5 干跑耗时 12.83s | `[VERIFIED]` PASS |
| **Step 6** | Fully quit Blender | 系统级完全终止 Blender 进程 | `pgrep` 检查确认系统零残留 Blender 进程 | `[VERIFIED]` PASS |
| **Step 7** | Relaunch Blender | 全新启动 Blender 5.2.2 LTS 独立进程 | 干净新进程启动成功 | `[VERIFIED]` PASS |
| **Step 8** | Reopen saved file | 重新载入 `vintage_flashlight_step1.blend` | 场景与几何数据正常解析完成 | `[VERIFIED]` PASS |
| **Step 9** | Verify first edit persistence | 核验 Slot 2 节点、参数与面指派 | Slot 2 1,462 面完好，`Body_Color_Tint` 节点 Factor=0.85/Color 精确持久化 | `[VERIFIED]` PASS |
| **Step 10** | Second bounded material edit | 在 Roughness 贴图与 Principled BSDF 之间插入 `ShaderNodeMath` (ADD 0.18, Clamped) | 主壳粗糙度提升 +0.18，呈现哑光磨砂质感；Slot 0/1 受保护区域依然完全未受损 | `[VERIFIED]` PASS |
| **Step 11** | Save again & render evidence | 保存为 `vintage_flashlight_step2.blend` (327KB)，渲染二次证据图 | 成功输出 `render_step2_second_edit.png` (282KB)；Step 7–11 干跑耗时 10.51s | `[VERIFIED]` PASS |
| **Step 12** | Minimal external-output smoke | 导出为 `vintage_flashlight_step2_export.glb` (4.2MB)，并在全新空白 Blender 场景重新导入渲染 | 导出耗时 1.11s，导入耗时 0.05s，3 个材质槽全部保留，网格 10,562 三角面完整，输出 `render_smoke_glb.png` (171KB)，无几何/材质崩溃 | `[VERIFIED]` PASS |

---

## 6. 耗时度量与认知负荷推断 (Timing & Friction Analysis)

### 6.1 教师干跑耗时 (Teacher Dry-run Time)
- **自动化脚本执行时间**：`[VERIFIED]`
  - Step 1–5: 12.83 秒
  - Step 7–11: 10.51 秒
  - Step 12 (Export & Reopen): 7.63 秒
  - 累计脚本干跑总时间：约 31 秒
- **教师手工操作干跑时间 (ESTIMATED)**：约 **4–6 分钟**（包含在 Blender GUI 中手动切面、添加材质槽、连线 MixRGB 与 Math 节点、保存、重启软件与导出 glTF）。

### 6.2 学生预计完成时间 (Inferred Student Completion Time)
- **预估耗时**：`[INFERRED]` **30–45 分钟**。
- **依据**：初学者在 Week 1 尚需熟悉三维视口导航、编辑模式选面（L 键连通选择）、新建材质槽与 Assign 操作、Shader Editor 节点连线与滑块调参。严禁将教师干跑时间等同于学生排课耗时。

### 6.3 观察到的摩擦与恢复路径 (Friction & Recovery Path)
1. **Friction 1: 原生资产材质槽未分离**
   - 现象：官方仅对玻璃独立分槽，外壳与反光罩/螺钉合并在单一材质中。
   - Recovery Path: 教师团队在准备 Week 1 教学资产包时，应提供脚手架版本（已预置好 `vintage_flashlight_body` 槽），或者在 Week 1 讲授中将“材质槽分配（Material Slot Assign）”作为 15 分钟核心技能讲授，避免学生误改全局贴图。
2. **Friction 2: 官方 blend 无预置灯光与相机**
   - 现象：打开原生 blend 后视口全黑或依赖默认 EEVEE 视口默认预览，无固定渲染视角。
   - Recovery Path: 教学包中应包含 `Lesson_Stage.blend`，内置标准三点光源与展示转台摄像机。
3. **Friction 3: Blender 5.2 节点接口变更**
   - 现象：`ShaderNodeMix` 的 RGBA 模式输出由旧版本的 `'Color'` 变更规范为 `'Result'`。
   - Recovery Path: 教学手册与排错指南必须以 Blender 5.2 LTS 为基准编写，明确新版节点插槽定义。

---

## 7. 局限性与尚未实测事项 (Limitations & What Remains Unverified)

1. **跨平台机房实测未完成**：`[NOT YET TESTED]` 本次仅在 macOS Apple Silicon 上通过实机验证，尚未在高校机房典型的 Windows 11 + NVIDIA RTX 环境上进行同构部署验证。
2. **微观 UV 重叠审计未穷尽**：`[INFERRED / NOT YET TESTED]` 虽经 Blender 内置 `uv.select_overlap` 检查未发现明显重叠循环，但未对所有低模接缝和高模烘焙进行微米级排查（按 Issue #9 Non-goals 保持有界范围）。
3. **未进行下游游戏引擎实时光照验证**：`[NOT YET TESTED]` GLB 导出通过了 Blender 重新导入渲染的 Smoke Test，但尚未导入 Unreal Engine 5.4 或 Unity 6 进行运行时 ORM / PBR 物理光照校准。

---

## 8. 最终判定 (Final Verdict)

**PASS — TEACHING SLICE VIABLE**

**判定理由**：
在真实目标运行时 **Blender 5.2.2 LTS** 下，Poly Haven Vintage Flashlight 资产通过了完整的 12 步最小教学切片实机验证：
1. 成功建立以手电筒主外壳（1,462 面）为学生编辑区、其余部件与玻璃为受保护区的教学接缝；
2. 第一次有界材质编辑与受保护区安全检查 100% 通过；
3. 退出重启后，第一次修改与材质拓扑完美持久化；
4. 第二次粗糙度微调编辑与再次保存验证无误；
5. 最小外部 glTF/GLB 输出与新进程重载 Smoke Test 结构完好，无灾难性表示失败；
6. 耗时与阻力已明确记录，具备向 Week 1 教学包（160-minute teaching package）推进的真实物理依据。
