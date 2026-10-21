# Substance 3D Painter 自动化能力与第二讲旧工程复用事实探针报告 (Automation & Asset Reuse Probe)

> **治理与门禁定位 (Governance & Status)**：  
> - **承载工单**：[Issue #40](https://github.com/carllx/corso-pbr-materials/issues/40)（关联 [Roadmap #1](https://github.com/carllx/corso-pbr-materials/issues/1)）  
> - **输入依据**：本机环境实测、Adobe 官方开发者文档、学院课件源归档目录  
> - **状态**：`PROBE COMPLETE / BOUNDED FINDINGS`  
> - **纪律遵守**：严格区分官方文档核实、本地 GUI 实测与运行门禁，不伪称实验通过，不破解二进制格式，不增加冗余长期 SSOT。

---

## 1. 探针一：MeetMat / Painter Python API 能力与运行门禁核实

### 1.1 本地宿主环境事实核验 (`LOCAL HOST FACT`)
- **排查范围**：本地 macOS `/Applications`、`~/Applications`、Spotlight 元数据、系统 PATH 及 Python 环境；
- **排查结果**：
  - 本地宿主机器虽然曾挂载安装镜像，但**尚未安装 Substance 3D Painter 独立应用程序**；
  - 本地无可执行的 `substance_painter` 独立二进制，亦无外部 Python 模块支持；
- **门禁定界**：**`RUNTIME GATE OPEN / UNVERIFIED ON LOCAL HOST`**。根据纪律，明确报告本地无运行环境，绝不谎称本地脚本测试通过。

### 1.2 官方文档确认的核心能力与架构边界 (`DOCUMENT VERIFIED`)
依据 Adobe Substance 3D Painter 官方 Python API 规范核实：
1. **执行宿主限制**：
   - Painter 的 Python API **绝非独立的外部 pip 库**；它仅驻留于 Substance 3D Painter 应用程序内部的嵌入式解释器（In-App Embedded Python 3.9/3.10），或通过 Painter CLI 批处理模式驱动。外部独立的 Miniconda/系统 Python 无法直接 `import substance_painter`。
2. **工程生命周期控制 (Project Management)**：
   - 官方模块 `substance_painter.project` 具备完善的工程级管理能力：
     - `create(mesh_file_path, settings=...)`：基于网格创建新工程；
     - `open(file_path)`：打开已有 `.spp`；
     - `save()` / `save_as(file_path)`：保存/另存为工程；
     - `close()`：关闭工程。
3. **图层堆栈与遮罩操作的严重受限性 (Layer & Mask Editing Limits)**：
   - **关键事实**：与 Blender 开放着色器节点网络的灵活性不同，Painter 官方 Python API 的初衷是**工作室管线批处理（批量导入网格、导出贴图、配置纹理集）与 UI 插件扩展**。
   - API 对图层内部微观结构（如动态新建指定通道数值的 Fill Layer、直接添加 Black Mask 并执行通道级参数绘制）的暴露极其有限，官方明确不支持也不建议通过脚本去“程序化合成材质”。
4. **Starter 脚手架方案推论**：
   - **无需重复 Blender 式脚本脚手架**：Blender 必须用脚本搭建预连节点是因为其节点网络复杂；而在 Painter 中，标准教学方案是直接分发 **`.spp` 模板工程** 或 **`.spsm` 智能材质预设包**；
   - **第 1 讲 MeetMat 天然免摩擦**：`MeetMat` 是 Painter 官方内置的 Sample（`File -> Open Sample... -> MeetMat`），机房开课时学生只需一键打开内置示例，**开局零依赖、零摩擦**。

---

## 2. 探针二：第二讲不倒翁旧工程 (`塑料案例.spp`) 复用价值与判断

### 2.1 只读检查事实 (`READ-ONLY PROVENANCE`)
- **文件物理定位**：`[LOCAL_ARCHIVE]/gzus-数字材质课件/课程案例源文件/2/塑料案例.spp`
- **文件体积**：**213.83 MB** (224,213,888 字节)
- **底层格式**：**Hierarchical Data Format (version 5 / HDF5)** 复合二进制容器
- **同目录资产情况**：包含 `第2周-塑料材质.pdf` (1.5MB) 与 `参考/` 目录；**彻底缺失独立的白模 FBX/OBJ 几何文件**。

### 2.2 是否值得继续复用的明确判断 (`DEFINITIVE DISPOSITION`)
- **结论**：**明确否定——绝不建议将原 213.8MB 的 `.spp` 直接下发给学生复用！**
- **核心风险诊断**：
  1. **向下兼容阻断风险 (Downstream Version Mismatch)**：Painter 的 `.spp` 文件存在严格的单向版本约束。若该工程是在较高版本（如 2022/2023）保存，而学院机房电脑安装的是较低版本（如 2020），Painter 会直接弹窗报错拒绝加载；
  2. **教学认知倒错 (Pedagogical Inversion)**：该工程已包含全部制作完成的图层与脏迹，学生只能在其上“逆向修改”。这破坏了从白模起步建立通道的认知连续性，且易因隐藏图层导致做旧穿帮；
  3. **分发负荷沉重**：35 人班同时拷贝 214MB 大文件，容易在机房网络引发阻塞。

### 2.3 最低成本替代路径 (`RECOMMENDED ACTIONABLE PATH`)
- **首选路径（机房单次导出白模）**：
  - 开课前由主讲教师在机房具备 Painter 的机器上打开该 `塑料案例.spp` **一次**；
  - 执行菜单命令 `File -> Export Mesh...`（导出网格），导出干净的 `budao-lowpoly.fbx`（通常仅几十至几百 KB）；
  - 以此干净白模作为学生第 2 讲开局资产，让学生亲身经历“新建工程 $\to$ 导入白模 $\to$ 建立塑料填充层”的正向流程；
- **保底路径（选用规范开源塑料白模）**：
  - 若机房低版本 Painter 无法打开该 `.spp`，教师无需纠结，直接选用任何带规范 UV 的开源塑料玩具/不倒翁小模型替代，教学逻辑 100% 等价。

---

## 3. 三分类能力与门禁综合判定表 (Summary Gate Table)

| 能力 / 资产项 | 官方文档核实状态 | 本地宿主实测状态 | 最终判定与后续动作 |
| :--- | :---: | :---: | :--- |
| **项目生命周期控制** (Create/Open/Save) | **已证实支持** | 未安装本地应用 | 依赖真实机房环境；可用于批量脚本 |
| **图层与遮罩脚本化构建** (Fill/Mask) | **证实极其受限** | 未安装本地应用 | **不采用脚本生成图层**；采用 `.spp` 模板或手绘教学 |
| **第 1 讲 MeetMat 开局** | **已证实内置** | 未安装本地应用 | 学生直接打开 Painter 内置 Sample，零摩擦开局 |
| **第 2 讲 `塑料案例.spp` 直接复用** | 格式已核验 (HDF5) | 外部挂载已定位 | **否决直接复用**；建议机房导出网格或替换白模 |

---
*报告编制完成，归档于 `docs/research/painter-automation-and-asset-reuse-probe.md`。*
