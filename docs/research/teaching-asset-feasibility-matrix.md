# 教学资产可行性矩阵与缺口映射 (Teaching Asset Feasibility Matrix & Gap Map)

> **文档性质**：权威技术调研报告与教学素材决策基础（Issue #7 Pass A + Pass B + Pass C 完整交付成果）  
> **基线分支/提交**：`main @ 9d683f87028faaf243fd4918eb5e5de542e64695`  
> **工作分支**：`research/issue-7-held-asset-gap-map`  
> **执行路线**：2026-09-19 Route Correction — Inventory-First Practice Design (`TEACHING_ASSET_INVENTORY_AND_GAP_MAP`)  
> **当前状态**：Pass A（持有资产核查）、Pass B（角色缺口映射）与 Pass C（外部资源定向采购调研）全部完成；详见配套研究报告 [`teaching-asset-pass-c-sourcing.md`](teaching-asset-pass-c-sourcing.md)。七大必需角色已形成权威采纳与闭环方案。

---

## 目录

1. [执行原则与盘点边界 (Scope & Execution Boundaries)](#1-执行原则与盘点边界)
2. [Pass A — 实际持有资产深度盘点 (Held Asset Inventory)](#2-pass-a--实际持有资产深度盘点)
   - 2.1 [Bundle 1: 教师提供石膏雕塑法线烘焙高低模套件 (Teacher-Provided Plaster Bust Normal Bake Pair)](#21-bundle-1-教师提供石膏雕塑法线烘焙高低模套件)
   - 2.2 [Bundle 2: PBR 通道配置正反例对照组 (PBR Channel Diagnostic & Error Benchmark)](#22-bundle-2-pbr-通道配置正反例对照组)
   - 2.3 [Bundle 3: 标定中性摄影棚 LookDev / HDRI 资产 (Neutral Studio Environment)](#23-bundle-3-标定中性摄影棚-lookdev--hdri-资产)
   - 2.4 [Bundle 4: 实时 glTF 2.0 PBR 交付校验资产 (Bathroom Floor Realtime PBR Asset)](#24-bundle-4-实时-gltf-20-pbr-交付校验资产)
   - 2.5 [Bundle 5: 1960年代复古办公室道具套件 (60s Office Props Courseware)](#25-bundle-5-1960年代复古办公室道具套件)
   - 2.6 [Bundle 6: CG Cookie Blender 4.2 Core 实存文件核验 (CGCookie Core Holding Audit)](#26-bundle-6-cg-cookie-blender-42-core-实存文件核验)
   - 2.7 [Bundle 7: 历史独立古典雕塑未拓扑扫描件库 (Historical Raw Statuary Scans)](#27-bundle-7-历史独立古典雕塑未拓扑扫描件库)
3. [Pass B — 七大必需角色缺口映射 (Required-Role Gap Map)](#3-pass-b--七大必需角色缺口映射)
   - 3.1 [角色 1：主工业练习资产 (Main Industrial Practice Asset)](#31-角色-1主工业练习资产)
   - 3.2 [角色 2：R8 高模向低模法线烘焙教学对 (High→Low Normal Bake Teaching Pair)](#32-角色-2r8-高模向低模法线烘焙教学对)
   - 3.3 [角色 3：W6 异质/非金属未知材质迁移载体 (Unfamiliar Non-Metal Transfer Carrier)](#33-角色-3w6-异质非金属未知材质迁移载体)
   - 3.4 [角色 4：PBR 通道正反例对照组 (PBR Channel Good/Bad Examples)](#34-角色-4pbr-通道正反例对照组)
   - 3.5 [角色 5：紧凑型程序化节点示例 (Compact Procedural-Node Example)](#35-角色-5紧凑型程序化节点示例)
   - 3.6 [角色 6：稳定 LookDev / HDRI 标定场景 (Stable LookDev / HDRI Scene)](#36-角色-6稳定-lookdev--hdri-标定场景)
   - 3.7 [角色 7：实时 / glTF 交付校验资产 (Realtime / glTF Validation Asset)](#37-角色-7实时--gltf-交付校验资产)
4. [盘点覆盖度、不可访问区域与权利风险说明](#4-盘点覆盖度不可访问区域与权利风险说明)
5. [Pass C 下一阶段行动边界与精确采购缺口](#5-pass-c-下一阶段行动边界与精确采购缺口)

---

## 1. 执行原则与盘点边界

根据 Issue #7 路线修正案（Inventory-First），教学练习设计的首要原则是：**立足教师与项目实际持有的真实数字资产，以法律权利清晰、技术格式可验证、学生可分发为底线，严禁将“网络视频可见性”或“教程目录链接”等同于“教学可用资产”**。

### 1.1 实际盘点范围与访问物理路径
本次盘点通过 macOS 本地环境（终端命令行、Blender 4.5.1 LTS 后台 Python 检查脚本、Spotlight 元数据索引）系统核实了以下存储区域，未进行全盘无节制漫游：
1. **教师移动教学存储主卷**：`/Volumes/T7-carllx2T`
   - `Courseware_NFU/DigitalModling/`（重点核验：历史 Maya 拓扑烘焙、Blender 雕刻、60年代道具教学套件）；
   - `Courseware_GAFA/`（重点核验：公共雕塑、数字雕塑创作、三维课件与大纲）；
   - `PROJECTS/`（重点核验：历史 3D 项目、Monalisa 项目、WebGL Shader 测试库）；
   - `OpensourceSTL/`（重点核验：独立 STL 扫描归档）；
   - `林昕真实多媒体归档库/`（历史学生作业归档，仅作权利对比，排除于分发库外）。
2. **局域网教学媒体与下载卷**：`/Volumes/Download`
   - `CGCookie - Blender 4.2 Core Essentials - 9 Tutorials/`（核实实存工程与许可协议）；
   - `CGCookie CORE Knowledge/`（核实文本导出与源码索引）。
3. **本地用户工作空间**：`/Users/yamlam/`
   - `Downloads/`（核实实存 glTF/GLB、几何测试场景）；
   - `Documents/GitHub/`（核实关联课程仓库 `corso-character-design`、`corso-fare-e-forma` 等）。

### 1.2 资产判定状态口径（严谨分层）
* **`READY`**：真实文件已完全核实，技术规格无需额外修改即可直接用于课堂教学，学生使用与再分发边界在法律上绝对明确。
* **`READY_WITH_PREP`**：真实文件存在且使用权明确，但需要明确、有限的教师预处理（如重打包为单一 `.blend`、预设 Cycles 烘焙贴图槽位或配置标定灯光）。
* **`MISSING — LOCAL AUTHORING`**：本地教师可低成本自行制作的教学缺口（如基于软件原生节点编写示范着色器）；**不要求 Pass C 外部 sourcing**，但在实际文件产出前不得算作 `READY`。
* **`REFERENCE_ONLY`**：可用于教师备课、原理观察、视线拆解或对照教学，但**严禁**作为学生 starter/可再分发练习资产。包括商业限制许可文件、无工程源文件的教程，以及未经拓扑的超高面原始扫描。
* **`MISSING`**：在当前实际持有的全部素材范围内，确认**没有**找到能够承担该核心角色的合规资产，必须进入下一阶段严格限定的定向补齐（Pass C）。

### 1.3 运行环境测试口径说明 (Blender 4.5.1 实测 vs Blender 5.2 预期)
本报告所有基于 Python 脚本的 `.blend`、OBJ 及贴图网格读取测试均在本地环境已安装的 **Blender 4.5.1 LTS** 中执行。对于目标课程环境 **Blender 5.2**，其兼容性基于标准 OBJ/glTF/HDRI 语义及 Cycles/Principled BSDF 规范予以预期，**尚未进行 Blender 5.2 运行时实机验证 (compatibility expected from standard OBJ/glTF/HDRI semantics, but not yet runtime-verified)**。

---

## 2. Pass A — 实际持有资产深度盘点

### 2.1 Bundle 1: 教师提供石膏雕塑法线烘焙高低模套件
* **定位源**：`/Volumes/T7-carllx2T/Courseware_NFU/DigitalModling/w11-sculpting-blender/maya/04-retopo-portrait-uv/c4-retop0-uv-bake/c4/`
* **包含的关键文件**：
  1. `hi-poly.obj`：80,002 三角面/四边面，0 UV通道，包围盒尺寸 `Vector (0.6236, 0.6947, 0.3673)`。为授课教师直接提供的一件古典石膏胸像（历史档案标记为 Laurana 风格古典胸像）的高精度扫描抽化件。
  2. `low-poly-uv.obj`（同 `c4-lowpoly.obj`）：1,367 面，包含 1 套完整、无重叠展开的 UV 坐标，包围盒尺寸 `Vector (0.6237, 0.6937, 0.3695)`，与高模在三维空间完全同心对齐。
  3. `nor.jpg`：1024×1024 像素，切线空间法线贴图（Tangent Space Normal Map，OpenGL Y+ 格式），带有完整边缘溢出填充（Dilation/Bleed）。同目录包含 Arnold 预编译 `.tx` 格式。
  4. 配套教案：`bake_normal.md`（教师亲自编写的法线烘焙指南，详述软硬边控制、UV 接缝硬边准则、Color Space Raw 强制要求及绿通道 Y+/Y- 反转排查）。
* **当前可访问性**：完全物理可读，经 Blender 4.5.1 LTS 后台程序化导入测试完全通过。
* **权属与再分发 (Provenance & Rights)**：
  - **高模母件**：**授课教师直接提供的石膏雕塑扫描 OBJ 文件（Teacher-provided plaster sculpture scan OBJ）**；对本课程而言属于已获授权的课程教学资产，不存在外部版权准入障碍。
  - **低模与 UV**：教师（carllx）手动画线重拓扑与拆分 UV 原创成果；
  - **再分发状态**：**经课程主讲教师明确授权用于课堂教学与学生工程分发（Authorized for classroom/student distribution by the course instructor）**。
* **学生可编辑性**：`student-editable`（学生可在 Blender 中独立完成 Selected-to-Active 烘焙与法线插槽验证）。
* **Blender 5.2 兼容性预估**：Verified in Blender 4.5.1; Blender 5.2 compatibility expected from standard OBJ semantics, but not yet runtime-verified.
* **所需教师预处理 (Teacher Prep)**：
  1. 将分离的 `hi-poly.obj` 与 `low-poly-uv.obj` 组装为单一规范的 `W2_R8_Normal_Bake_Starter.blend`；
  2. 低模材质预挂载 `Principled BSDF` 与未填充的 1024×1024 32-bit Float 贴图节点（色彩空间锁定为 `Non-Color`）；
  3. 预设 Cycles Bake 选项（Bake Type: Normal, Selected to Active 勾选, Extrusion 设为 0.005m）；
  4. 预计预处理耗时：2 小时以内。
* **对应课程位置**：W2（或 W3）核心概念微实验 / R8 映射表征基石。
* **技术风险**：Blender Cycles GPU 烘焙需要学生具备基础算力（Metal/OptiX/CUDA）；必须严格提醒将贴图节点设为 `Non-Color`，否则 sRGB Gamma 曲线会导致边缘严重发黑。

---

### 2.2 Bundle 2: PBR 通道配置正反例对照组
* **定位源**：`/Volumes/T7-carllx2T/Courseware_NFU/DigitalModling/60s-office-props-maya/sourceimages/` 与 `w11-sculpting-blender/maya/04-retopo-portrait-uv/`
* **包含的关键文件**：
  1. `nor_Raw_ACEScg.jpg.tx` vs `nor_sRGB_ACEScg.jpg.tx`：标准对比组。实证展示将切线空间法线贴图错误赋予 sRGB 后的表面光照撕裂现象。
  2. `TCom_Pavement_PaintedConcrete3_1K_normal_Raw_ACEScg.png.tx` vs `..._sRGB_ACEScg.png.tx`：硬表面工业材质法线色彩空间错误对照。
  3. `sampledNormals_Raw_ACEScg.jpg.tx` vs `sampledNormals_sRGB_ACEScg.jpg.tx`：采样法线对照组。
  4. 故障说明教案：`bake_normal.md` 第 4 节《常见问题排查 Checklist》。
* **当前可访问性**：完全可访问。
* **权属与再分发**：教师历史教学调试归档；可自由提取为教学演示素材。
* **Blender 5.2 兼容性预估**：Verified in Blender 4.5.1; 节点网络转译至 Blender 5.2 原生着色器预期完全兼容。
* **所需教师预处理**：制作包含左右两个相同几何球体的 `.blend` 对照场景（左侧挂载 `Non-Color` 正确法线，右侧挂载 `sRGB` 错误法线），供学生即时切换观察。耗时约 1 小时。
* **对应课程位置**：W2 LO2.2（通道语义学与线性数据/色彩数据分界）。

---

### 2.3 Bundle 3: 标定中性摄影棚 LookDev / HDRI 资产
* **定位源**：`/Volumes/T7-carllx2T/Courseware_NFU/DigitalModling/60s-office-props-maya/sourceimages/studio_small_09_1k.exr`
* **包含的关键文件**：
  1. `studio_small_09_1k.exr`：1.3 MB，32-bit Float 高动态范围图像，双侧柔光箱中性白光摄影棚布光，无极端色温偏差与方向性主光。
  2. `autoshop_01_2k.hdr`（备用）：2K 分辨率机修车间 HDR。
* **第一方来源与真实权属**：
  - **官方作者**：**Sergej Majboroda**（Poly Haven 官方元数据已确认，此前简报曾误记为 Philip Modin，现已纠正）；
  - **Canonical Pointer**：`https://polyhaven.com/a/studio_small_09`；
  - **授权许可**：**CC0 1.0 Universal (Public Domain Dedication)**；
  - **再分发状态**：完全自由分发，无版权争议。
* **当前可访问性**：完全可读。
* **Blender 5.2 兼容性预估**：Verified in Blender 4.5.1; Blender 5.2 compatibility expected from standard OpenEXR / World shader semantics.
* **所需教师预处理**：创建标准的 `LookDev_Studio_Template.blend`，包含中性地面阴影捕捉器（Shadow Catcher）、三颗标准标定球（100% 镀铬镜面球、50% 中性灰漫反射球、纯白粗糙度对比球）及相机环绕轨道。耗时约 1 小时。
* **对应课程位置**：W1（基准观察）、W2（材质参数因果验证）、W8–W9（多环境 LookDev 评测）。

---

### 2.4 Bundle 4: 实时 glTF 2.0 PBR 交付校验资产
* **定位源**：`/Users/yamlam/Downloads/bathroom_floor_ gltf/`
* **包含的关键文件**：
  1. `scene.gltf` + `scene.bin`：标准 glTF 2.0 场景描述与二进制网格（单片平面地砖几何）。
  2. `textures/lambert2_baseColor.png`：漫反射色彩通道。
  3. `textures/lambert2_metallicRoughness.png`：标准通道打包贴图（绿色通道 = Roughness，蓝色通道 = Metallic）。
  4. `textures/lambert2_normal.png`：切线空间法线贴图。
  5. `license.txt`：标明作者 RubaQewar，遵循 **CC-BY-4.0** 协议。
* **当前可访问性**：完全可读。
* **权属与再分发**：CC-BY-4.0 明确允许教育与商业再分发，只需保留标准署名。
* **Blender 5.2 兼容性预估**：Verified in Blender 4.5.1; Blender 5.2 glTF 2.0 importer/exporter 规范完全一致。
* **所需教师预处理**：将其打包为单文件 `.glb` 格式，作为 W7 实时引擎交付与贴图打包排错的教学样例。耗时约 30 分钟。
* **对应课程位置**：W7 实时交付与通道打包验证（GLTF/WebGL 标准）。

---

### 2.5 Bundle 5: 1960年代复古办公室道具套件
* **定位源**：`/Volumes/T7-carllx2T/Courseware_NFU/DigitalModling/60s-office-props-blender/`
* **包含的关键文件**：
  1. 3D 模型场景：`60's office stuff exporter.blend`，包含打字机（`prp_typewriter_portable_01_grp`）、电传打字机终端（`prp_teletype_terminal_01_grp`）、大型机磁带机（`prp_mainframe_tapeDrive_yellow_01_grp`）、办公桌、文件柜、马克杯等 30 余个独立道具。
  2. 贴图系统：`60's_office_textures_1-01.png`（低多边形漫反射图集 Atlas）、`Wood_desk.jpeg`、`internal_ground_ao_texture.jpeg`。
* **技术缺陷分析与教学适用性评估**：
  - **严重缺陷**：该模型套件建于 2023–2025 年，目标是移动端与 WebGL 低面展示。材质依赖手绘漫反射图集与无节点单色材质，**完全不具备现代 PBR 贴图集（缺失真实粗糙度图、金属度图、微细节法线图与 AO 烘焙图）**。
  - **结论**：虽然拥有打字机等工业外形，但若用于 W1–W5 的“参数因果关系教学”，教师必须从零重新进行高模倒角烘焙、重解 UV 与绘制整套 PBR 贴图，预处理负担极重（数十小时），无法作为高品质主工业资产直接使用。

---

### 2.6 Bundle 6: CG Cookie Blender 4.2 Core 实存文件核验
* **定位源**：`/Volumes/Download/CGCookie - Blender 4.2 Core Essentials - 9 Tutorials/`
* **实存文件清查结果**：
  1. `Materials-and-Shading-CourseFiles-01/`：**仅包含 `cgc-license-sourcefile.pdf`，没有任何三维模型或 `.blend` 工程文件**！
  2. `Texturing-CourseFiles-01/`：包含 `autoshop_01_2k.hdr`、`Binoculars_Opacity.png`、`Sand_Metallic.png`，**望远镜主体三维模型完全缺失**！
  3. 法律许可限制：`cgc-license-sourcefile.pdf` 明确写明：*“These source files and/or any other included material... is meant for personal and educational use only. You may not distribute or use these files for commercial use without prior permission.”* 明确禁止对外公开分发与仓库传播。
* **结论**：确凿证实了 Issue #7 路线修正的判断——**CG Cookie 的双筒望远镜（Binoculars）在本地只有教学视频和两张残缺贴图，无合法可分发的学生 Starter 模型**，必须定级为：
  `REFERENCE_ONLY / NO STARTER FILE`。

---

### 2.7 Bundle 7: 历史独立古典雕塑未拓扑扫描件库
* **定位源**：`/Volumes/T7-carllx2T/OpensourceSTL/` 及 `Courseware_NFU/DigitalModling/1.2/`
* **包含的关键文件**：
  1. `Pseudo-Seneca-Portrait of Hesiod_152-smk-inv-94.stl`（99.9 MB，丹麦国立美术馆 SMK 藏品，约 7 万三角面，无 UV）；
  2. `Marcellus -Portrait of an Augustine Prince_153-smk-809.stl`（87.2 MB，SMK 藏品，约 35 万三角面，无 UV）；
  3. `Scan_the_World_-_Venus_de_Milo.stl`（米洛的维纳斯）、`David_(Michelangelo).stl`（大卫）。
* **独立性说明**：这些 STL 文件均为原始 3D 打印用或三角面扫描文件，无拓扑、无 UV。它们属于独立的文博开放扫描存档，**与 Bundle 1 中教师直接提供用于教学的石膏胸像 OBJ 高低模不属同一套资产链条**。全库定级为 `REFERENCE_ONLY`。

---

## 3. Pass B — 七大必需角色缺口映射

对照 W1–W9 课程教学目标（Learning Objectives），对七大核心教学资产角色进行逐一判定：

### 3.1 角色 1：主工业练习资产 (Main Industrial Practice Asset)
* **角色职能**：贯穿 W1 观察、W2 物理参数因果、W3–W5 贴图制作/材质拆解、W7 实时交付及 W8–W9 LookDev 迭代的核心工业/机械资产载体（需具备明确金属/绝缘体结构分界、工业倒角与典型磨损区域）。
* **当前状态**：**`RESOLVED VIA PASS C` (`ADOPT`)**
* **事实证据与采纳结论**（详见配套调研报告 [`teaching-asset-pass-c-sourcing.md`](teaching-asset-pass-c-sourcing.md)）：
  1. **主选采纳 (`ADOPT`)**：**Poly Haven `Vintage Flashlight` (复古手电筒)**（第一方链接：`https://polyhaven.com/a/vintage_flashlight`，作者：Omar M. El-Safy，**CC0 1.0 Universal**）。约 11K 三角面，单套高质量无重叠 UV；具备极清晰的“红色涂层外壳（绝缘漆面）→ 边缘磕碰露出裸露金属底材 → 黑色高阻尼手柄与滑块（橡胶/工程塑料）→ 高反光镀铬反光碗（高反射镜面金属）→ 纯净玻璃透镜（透光电介质）”完备物理层；官方直供 `.blend`、glTF 与全套 1K–8K PBR 贴图，教师预处理时间 < 1 小时。
  2. **备选采纳 (`ADOPT_WITH_PREP`)**：**Poly Haven `Retro Multimeter` (复古万用表)**（作者：Elli Moeller，CC0 1.0）。具备胶木机壳、橡胶表笔线、印刷表盘与镀铬表针，适合高阶对比或备选。
  3. **重大排除**：Khronos `DamagedHelmet` 因协议实为 **CC BY-NC 4.0 (NonCommercial)** 商业限制被一票否决；Smithsonian 3D 原始扫描因照片级死阴影与缺失 PBR 通道被排除。
* **处理结论**：**已通过 Pass C 确定性解决，采纳 Vintage Flashlight 作为全课程主工业练习资产**。

---

### 3.2 角色 2：R8 高模向低模法线烘焙教学对 (High→Low Normal Bake Teaching Pair)
* **角色职能**：支撑 45 分钟微实验，直观向学生展示“几何细节向切线法线向量编码”的表征替代过程，为 PBR 法线通道提供具象认知。
* **当前状态**：**`READY_WITH_PREP`**
* **事实证据**：
  1. **实体资产完备**：Bundle 1 的石膏胸像高低模（`hi-poly.obj` 80,002 面 + `low-poly-uv.obj` 1,367 面）已在 Blender 4.5.1 中完成空间对齐与几何验证；
  2. **历史检验充分**：历史烘焙图 `nor.jpg`（1024×1024）与教案 `bake_normal.md` 证明该套件曾成功用于高校真实教学，拓扑接缝、软硬边设置经过验证；
  3. **法律权属明确**：**高模为教师直接提供的石膏雕塑扫描 OBJ，明确授权用于课程课堂教学与学生工程分发；低模与 UV 均为教师原创教学成果**。无需外部版权准入调查；
  4. **预处理代价极低**：只需教师花费约 2 小时将两个 OBJ 打包为 Blender 启动 `.blend` 工程并预设 Cycles 贴图节点。
* **Blender 5.2 兼容性预估**：Verified in Blender 4.5.1; Blender 5.2 compatibility expected from standard OBJ semantics, but not yet runtime-verified.
* **处理结论**：**无需外部寻找新资产，直接锁定 Bundle 1 石膏雕塑套件作为 R8 教学载体**。

---

### 3.3 角色 3：W6 异质/非金属未知材质迁移载体 (Unfamiliar Non-Metal Transfer Carrier)
* **角色职能**：检验学生将 W1–W5 学到的 PBR 物理原理向**未接触过的非金属复杂三维资产**（如木质器具、皮具、陶瓷器皿、石雕）迁移的近迁移（near-transfer）能力。
* **当前状态**：**`RESOLVED VIA PASS C` (`ADOPT`)**
* **事实证据与采纳结论**（详见配套调研报告 [`teaching-asset-pass-c-sourcing.md`](teaching-asset-pass-c-sourcing.md)）：
  1. **排他前置约束**：严禁复用主工业手电筒（金属主体），严禁复用 R8 石膏雕塑（前期已熟悉失去陌生度）；独立评估 `bathroom_floor_ gltf` 仅为水平地砖单片，缺失三维曲率与体积手工艺细节，无法承载 W6 近迁移任务。
  2. **主选采纳 (`ADOPT`)**：**Poly Haven `Antique Ceramic Vase 01` (青花开片陶瓷瓶)**（第一方链接：`https://polyhaven.com/a/antique_ceramic_vase_01`，作者：James Ray Cock，**CC0 1.0 Universal**）。约 9K 三角面，饱满回转体双曲率形态，单套无重叠 UV；纯电介质物理特征极具代表性——高反光玻璃质釉面（Dielectric F0 ~0.04）、开片釉微裂纹法线（Crackle Crazing Normal）、青花釉下彩漫散射、底部露胎素烧粗陶（Porous Clay Bisque）与微脏污沉积。官方直供 `.blend`、glTF 与全套贴图+分层遮罩（Mask01/02/03），教师预处理时间 < 45 分钟。
  3. **木质备选 (`ADOPT_WITH_PREP`)**：**Poly Haven `Wooden Bowl 01` (手作木碗)**（作者：Oliver Harries，CC0 1.0）。原木粗陶碗（~14K 面），具备木质纤维各向异性与年轮微孔。
* **处理结论**：**已通过 Pass C 确定性解决，采纳 Antique Ceramic Vase 01 作为 W6 材质近迁移测评载体**。

---

### 3.4 角色 4：PBR 通道正反例对照组 (PBR Channel Good/Bad Examples)
* **角色职能**：向学生展示常见严重错误（如法线贴图误设 sRGB 导致的视口断层、金属度贴图带脏灰渐变、AO 贴图直接乘入 Albedo 等）。
* **当前状态**：**`READY_WITH_PREP`**
* **事实证据**：
  1. Bundle 2 完整持有历史教学积累的对比贴图（`nor_Raw` vs `nor_sRGB`、`TCom_Pavement` 对照组）及排错教案；
  2. 预处理只需在 Blender 中搭建一个双视窗或左右排列的测试场景，将同一个法线分别连接在 `sRGB` 和 `Non-Color` 采样模式下；
  3. 预处理耗时约 1 小时。
* **Blender 5.2 兼容性预估**：Verified in Blender 4.5.1; 预期着色器节点在 Blender 5.2 完全通用。
* **处理结论**：本地资产就绪，无需外部采购。

---

### 3.5 角色 5：紧凑型程序化节点示例 (Compact Procedural-Node Example)
* **角色职能**：W4/W5 中演示如何利用 8–12 个基础数学/噪波节点快速生成微观粗糙度扰动或边缘磨损遮罩，阐释非破坏性着色逻辑。
* **当前状态**：**`MISSING — LOCAL AUTHORING`**
* **审阅修正事实分析**：
  1. **窄范围清查结果**：经系统检索本地 `/Volumes/T7-carllx2T/Courseware_NFU/` 与 `Downloads/` 下的所有 `.blend` 文件（包括 `60's office stuff exporter-designsysterm.blend`、`NodeGroup.blend`、`Rock.blend`），**确认当前并不存在任何已打包、已验证的独立程序化着色材质或节点组资产文件**；
  2. **定级严格收正**：依照“持有素材盘点（Held-material inventory）”的客观定义，不能把“未来可用原生节点制作”提前视为 `READY`。在实际物理工程产生前，必须严格定级为缺口；
  3. **性质界定**：这是一个**本地教师极低成本即可自研补齐的缺口**（基于 Blender 内置 Noise Texture、Voronoi、Map Range、ColorRamp 编写仅需约 1 小时），**绝不要求且严禁扩大为 Pass C 外部采购**。
* **处理结论**：定为 `MISSING — LOCAL AUTHORING`，作为教师内部备课任务，不纳入外部采购清单。

---

### 3.6 角色 6：稳定 LookDev / HDRI 标定场景 (Stable LookDev / HDRI Scene)
* **角色职能**：提供统一、中性、无极端偏色的光影检验环境，使学生在 W1、W2、W8、W9 的材质调节具备科学参照。
* **当前状态**：**`READY_WITH_PREP`**
* **事实证据**：
  1. Bundle 3 本地持有的 `studio_small_09_1k.exr` 拥有绝对干净的 CC0 授权（作者：Sergej Majboroda, Poly Haven）与高质量 32 位浮点动态范围；
  2. 预处理只需教师构建标准的灰色底板、阴影捕捉、三颗校准球（镜面金属、50%灰绝缘体、漫反射纯白）和正交渲染相机；
  3. 预处理耗时约 1 小时。
* **Blender 5.2 兼容性预估**：Verified in Blender 4.5.1; Blender 5.2 compatibility expected from standard OpenEXR semantics.
* **处理结论**：本地资产与授权完全完备，无需外部采购。

---

### 3.7 角色 7：实时 / glTF 交付校验资产 (Realtime / glTF Validation Asset)
* **角色职能**：W7 用于检验 glTF 2.0 / WebGL 导出规则，验证 Roughness/Metallic 双通道合流打包（Green/Blue Packing）与实时引擎渲染一致性。
* **当前状态**：**`READY_WITH_PREP`**
* **事实证据**：
  1. Bundle 4 的 `bathroom_floor_ gltf` 已经是以合流打包贴图（`lambert2_metallicRoughness.png`）构建的标准 glTF 2.0 资产，授权清晰（CC-BY-4.0）；
  2. 同时，Bundle 1 的低模在完成 R8 法线烘焙后，天然可作为第二个模型导出校验实例；
  3. 预处理只需教师整理一个单文件 `.glb` 样本。
* **Blender 5.2 兼容性预估**：Verified in Blender 4.5.1; Blender 5.2 glTF 导出规范完全兼容。
* **处理结论**：本地资产就绪，无需外部采购。

---

## 4. 盘点覆盖度、不可访问区域与权利风险说明

### 4.1 盘点覆盖度与未访问区域事实记录
* **已覆盖深度检查**：
  - 本地 T7 盘历史教学与工程归档（确认了雕塑法线烘焙高低模、60s 道具库、学生作业库、各类扫描 STL）；
  - 本地 NAS 映射卷中的 CG Cookie 教程下载目录（确认了真实工程文件的残缺与授权禁项）；
  - 本地常用下载目录与 Git 仓库（确认了中性 HDR 与 glTF 样例）。
* **排除/不可访问区域**：
  - 历史学生作业库（`林昕真实多媒体归档库`）：虽然包含大量学生建模作业，但因存在学生个人著作权归属不明和质量参差问题，依照教学伦理原则**全部排除在课程公开发发素材库之外**。

### 4.2 权利与再分发风险清点
* **R8 雕塑法线套件权属**：
  高模为授课教师直接提供的石膏雕塑扫描 OBJ，教师享有完备的教学分发授权；低模、UV 与烘焙参数均为教师自研成果。**整体套件在课程内部可安全合法向学生分发**。
* **CG Cookie 资产红线**：
  所有 CG Cookie 视频与伴随文件（包括 Binoculars 材质演示和 Lighting 场景）严禁作为代码仓库二进制文件或学生分发包上传。仅限教师作为教学结构参考（`REFERENCE_ONLY`）。

---

## 5. Pass C 外部资源调研成果与七大角色最终决策闭环 (Final Teaching Kit Closure)

通过 Pass A/B 持有资产实证清查与 Pass C 第一方开放资源库深度穿透调研（详见配套调研报告 [`teaching-asset-pass-c-sourcing.md`](teaching-asset-pass-c-sourcing.md)），课程七大必需角色的最终状态矩阵与闭环落地方案全部确立：

| 必需教学角色 | 最终判定状态 | 核心依托资产 / 证据来源 | 授权许可 | 预处理负担 | 落地实施动作 |
| :--- | :---: | :--- | :---: | :---: | :--- |
| **1. 主工业练习资产** | **`RESOLVED VIA PASS C`**<br>(`ADOPT`) | Poly Haven: `Vintage Flashlight`<br>(备选: `Retro Multimeter`) | **CC0 1.0** | < 1 小时 | 剥离贴图构建 Starter，保留 2K 相对路径全套贴图构建 Reference |
| **2. R8 法线烘焙教学对** | **`READY_WITH_PREP`** | Bundle 1: 教师提供石膏胸像扫描 (`hi-poly.obj` 80k + `low-poly-uv.obj` 1.3k + `nor.jpg`) | 教师授权 | ~2 小时 | 将 OBJ 对打包为 `.blend`，预设 Cycles Selected-to-Active 距离 |
| **3. W6 未知非金属载体** | **`RESOLVED VIA PASS C`**<br>(`ADOPT`) | Poly Haven: `Antique Ceramic Vase 01`<br>(备选: `Wooden Bowl 01`) | **CC0 1.0** | < 45 分钟 | 配置釉面与露胎分层 Shader 框架，提供开片法线与遮罩供实训调用 |
| **4. PBR 通道正反例组** | **`READY_WITH_PREP`** | Bundle 2: `nor_sRGB` vs `Raw` 对照组 + `bake_normal.md` 排错教案 | 教师自研 | ~1 小时 | 在 Blender 搭建双球并排对比视窗，直观演示 sRGB 断层黑边 |
| **5. 紧凑程序化节点示例** | **`MISSING — LOCAL AUTHORING`** | 基于 Blender 原生算子 (Noise, Voronoi, Map Range) 自研 8–12 节点 | 教师自研 | ~1 小时 | 教师在本地固化磨损遮罩/粗糙度扰动节点组示范工程（**严禁外部采购**） |
| **6. 稳定 LookDev 场景** | **`READY_WITH_PREP`** | Bundle 3: `studio_small_09_1k.exr`<br>(Sergej Majboroda, Poly Haven) | **CC0 1.0** | ~1 小时 | 配置中性灰地面阴影捕捉器、三标定球与 72 帧转台相机 |
| **7. 实时 glTF 校验资产** | **`READY_WITH_PREP`** | Bundle 4: `bathroom_floor_ gltf` (CC-BY-4.0) + R8 低模 glTF 直出 | CC-BY 4.0 | ~30 分钟 | 固化单文件 `.glb` 样本，用于 W7 ORM 绿色/蓝色通道打包验证 |

### 5.1 最终实践教学套件特征总结 (Teaching Kit Characteristics)
1. **零商业许可风险 (Zero Licensing Risk)**：
   除明确采用 CC-BY-4.0 的辅助校验地砖与教师自研成果外，所有核心主资产（手电筒、花瓶、摄影棚 HDRI）均统一在 **CC0 1.0 Universal** 协议下，完全杜绝版权纠纷与学生作品集展示障碍；
   *特别排除项记要*：Khronos `DamagedHelmet` 因带有 CC BY-NC 4.0 (NonCommercial) 商业限制被一票否决；Smithsonian 3D 原始扫描因带照片死阴影且无 PBR 分离通道被排除。
2. **极轻教师维护负担 (Low Preparation Burden)**：
   所有引入资产均为工业级标准拓扑与单套无重叠 UV，免除从零建模、重拓扑与拆 UV 负担，全套 7 个角色教师总预处理时间累计 **< 8 小时**；
3. **分层物理表现力完备 (Complete Physical Diversity)**：
   - 涵盖金属（裸钢、镀铬、黄铜）、涂层电介质（红漆、油墨）、橡胶塑料、纯透明玻璃、双层玻璃质釉面、微裂纹开片、多孔粗陶露胎与各向异性木质；
   - 完整支撑从 W1 观察、W2 因果、W4 程序化、W6 迁移、W7 实时交付到 W8–W9 LookDev 的全部技术链条。

---
*报告归档节点：Pass A/B/C 全部完成，七大教学角色完全闭环，等待 Browser Review 确认。*
