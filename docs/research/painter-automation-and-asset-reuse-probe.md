# Substance 3D Painter 自动化能力与第二讲旧工程复用事实探针报告 (Automation & Asset Reuse Probe)

> **治理与门禁定位 (Governance & Status)**：  
> - **承载工单**：[Issue #40](https://github.com/carllx/corso-pbr-materials/issues/40)（关联 [Roadmap #1](https://github.com/carllx/corso-pbr-materials/issues/1)）  
> - **输入依据**：本机环境实测、Adobe 官方开发者文档、挂载源卷 `/Volumes/198.168.10.5/...`  
> - **状态**：`PROBE COMPLETE / BOUNDED FINDINGS`  
> - **纪律遵守**：严格区分官方文档核实、本地 GUI 实测与运行门禁，不伪称实验通过，不破解二进制格式，不增加冗余长期 SSOT。

---

## 1. 探针一：MeetMat / Painter Python API 能力与运行门禁核实

### 1.1 本地宿主环境事实核验 (`LOCAL HOST FACT`)
- **排查范围**：本地 macOS `/Applications`、`~/Applications`、Spotlight 元数据、系统 PATH 及 Python 环境；
- **排查结果**：
  - 本地宿主机器虽然挂载了安装镜像 `/Volumes/Adobe Substance_3D_Painter`，但**尚未安装 Substance 3D Painter 应用程序**；
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
3. **图层堆栈与遮罩脚本化构建能力 (Layer & Mask Editing API — 2026-09-17 Doc Verified)**：
   - **官方文档事实修正**：依据 Adobe 2026-09-17 官方 `substance_painter.layerstack` API 文档，现代版本的 Substance 3D Painter 已经正式开放了对图层堆栈的丰富编程接口，**支持通过 Python 脚本插入图层、创建填充图层 (Fill Layer)、配置物理通道参数、添加遮罩 (Mask) 以及设置图层混合模式**。因此，技术上“脚本创建 Fill Layer 和 Mask”已由官方文档确认为**可行支持项 (`OFFICIAL DOCUMENT VERIFIED`)**。
   - **版本与运行时门禁 (`RUNTIME GATE OPEN`)**：该 API 高度依赖具体 Painter 版本特性（现代版本通常为 9.x / 10.x 及以后版本）。由于当前学校教学机房安装的实际软件版本尚待实机核查（若机房仍为老旧版本则可能不支持该 API），且本地 macOS 环境未安装运行实体，因此**“目标机房 Painter 版本是否支持该 API 以及脚本自动化运行可行性”继续保持为开放门禁 (`RUNTIME GATE OPEN / PENDING LAB PROBE`)**。
   - **教学策略推论**：在教学法层面，第 1 讲的核心使命是帮助学生在 GUI 视口中建立图层堆栈与遮罩的直观空间心智；官方内置的 `MeetMat` 结合 GUI 动手操作已足以提供最低摩擦的学习闭环，无需将脚本脚手架强制前置。
4. **Starter 脚手架方案推论**：
   - **无需重复 Blender 式脚本脚手架**：Blender 必须用脚本搭建预连节点是因为其节点网络复杂；而在 Painter 中，标准教学方案是直接分发 **`.spp` 模板工程** 或 **`.spsm` 智能材质预设包**；
   - **第 1 讲 MeetMat 天然免摩擦**：`MeetMat` 是 Painter 官方内置的 Sample（`File -> Open Sample... -> MeetMat`），机房开课时学生只需一键打开内置示例，**开局零依赖、零摩擦**。

---

## 2. 探针二：第二讲不倒翁旧工程 (`塑料案例.spp`) 复用价值与判断

### 2.1 只读检查事实 (`READ-ONLY PROVENANCE`)
- **文件物理定位**：`/Volumes/198.168.10.5/Download/gzus-数字材质课件/课程案例源文件/2/塑料案例.spp`
- **文件体积**：**213.83 MB** (224,213,888 字节)
- **底层格式**：**Hierarchical Data Format (version 5 / HDF5)** 复合二进制容器
- **同目录资产情况**：包含 `第2周-塑料材质.pdf` (1.5MB) 与 `参考/` 目录；**彻底缺失独立的白模 FBX/OBJ 几何文件**。

### 2.2 是否值得继续复用的明确判断 (`DEFINITIVE DISPOSITION`)
- **结论**：**不建议直接下发给学生作为开局 Starter，但保留其作为教师参考成品及提取白模的价值，具体待 GUI 验证 (`PENDING GUI VERIFICATION`)**。
- **核心考量与分析**：
  1. **不作为学生 Starter 的理由**：
     - **向下兼容阻断风险**：Painter 的 `.spp` 单向版本约束极严。若该工程在较高版本保存，而机房电脑安装的是较低版本，Painter 会直接弹窗报错拒绝加载；
     - **教学认知倒错**：工程已包含全部制作完成的图层与脏迹，学生只能在其上“逆向修改”，破坏了从白模起步建立通道的认知连续性；
     - **分发负荷沉重**：35 人班同时拷贝 214MB 大文件，容易在机房网络引发阻塞；
  2. **保留教师参考成品与提取白模的可能**：
     - 该工程包含完整的塑料材质做旧工艺与层叠参数，**是极佳的教师备课参考成品与终态对照依据**；
     - 开课前可由主讲教师在机房具备 Painter 的机器上尝试打开该工程，若能正常加载，可通过菜单 `File -> Export Mesh...` 导出干净的 `budao-lowpoly.fbx`（仅数百 KB），低成本解决白模缺失问题；
     - 若机房低版本软件无法打开，则启动保底方案，选用带规范 UV 的开源塑料玩具/不倒翁小模型替代。

### 2.3 最低成本替代路径 (`RECOMMENDED ACTIONABLE PATH`)
- **首选路径（机房 GUI 验证并单次导出白模）**：
  - 开课前由主讲教师在机房具备 Painter 的机器上打开该 `塑料案例.spp` 进行 GUI 验证；
  - 验证成功则执行 `File -> Export Mesh...` 导出干净白模，作为学生正向制作的 Starter 资产；
- **保底路径（选用规范开源塑料白模）**：
  - 若机房 Painter 打开报错，教师直接选用规范开源塑料玩具白模替代，教学目标与物理因果 100% 等价。

---

## 3. 三分类能力与门禁综合判定表 (Summary Gate Table)

| 能力 / 资产项 | 官方文档核实状态 | 本地宿主实测状态 | 最终判定与后续动作 |
| :--- | :---: | :---: | :--- |
| **项目生命周期控制** (Create/Open/Save) | **已证实支持** | 未安装本地应用 | 依赖真实机房环境；可用于批量脚本 |
| **图层与遮罩脚本化构建** (Fill/Mask) | **2026-09-17 官方文档证实支持** | 未安装本地应用 | **技术证实可行**；但机房实际版本与运行时待核，第 1 讲以官方 MeetMat GUI 教学为主 |
| **第 1 讲 MeetMat 开局** | **已证实内置** | 未安装本地应用 | 学生直接打开 Painter 内置 Sample，零摩擦开局 |
| **第 2 讲 `塑料案例.spp` 直接复用** | 格式已核验 (HDF5) | 外部挂载已定位 | **不建议作为学生 Starter**；保留教师参考及提取白模价值，待机房 GUI 验证 |

---
*报告编制完成，归档于 `docs/research/painter-automation-and-asset-reuse-probe.md`。*
