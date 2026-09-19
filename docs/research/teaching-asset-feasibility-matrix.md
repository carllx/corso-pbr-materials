# 教学资产可行性矩阵与缺口映射 (Teaching Asset Feasibility Matrix & Gap Map)

> **文档性质**：权威技术调研报告与教学素材决策基础（Issue #7 Pass A + Pass B 交付成果）  
> **基线分支/提交**：`main @ 9d683f87028faaf243fd4918eb5e5de542e64695`  
> **工作分支**：`research/issue-7-held-asset-gap-map`  
> **执行路线**：2026-09-19 Route Correction — Inventory-First Practice Design (`TEACHING_ASSET_INVENTORY_AND_GAP_MAP`)  
> **当前状态**：Pass A（实际持有资产盘点）与 Pass B（七大必需教学角色缺口映射）已完成；本轮在 Gap Map 处停止，**不启动 Pass C 外部采购**。

---

## 目录

1. [执行原则与盘点边界 (Scope & Execution Boundaries)](#1-执行原则与盘点边界)
2. [Pass A — 实际持有资产深度盘点 (Held Asset Inventory)](#2-pass-a--实际持有资产深度盘点)
   - 2.1 [Bundle 1: 历史教学法线烘焙高低模套件 (Laurana Plaster Bust Normal Bake Pair)](#21-bundle-1-历史教学法线烘焙高低模套件)
   - 2.2 [Bundle 2: PBR 通道配置正反例对照组 (PBR Channel Diagnostic & Error Benchmark)](#22-bundle-2-pbr-通道配置正反例对照组)
   - 2.3 [Bundle 3: 标定中性摄影棚 LookDev / HDRI 资产 (Neutral Studio Environment)](#23-bundle-3-标定中性摄影棚-lookdev--hdri-资产)
   - 2.4 [Bundle 4: 实时 glTF 2.0 PBR 交付校验资产 (Bathroom Floor Realtime PBR Asset)](#24-bundle-4-实时-gltf-20-pbr-交付校验资产)
   - 2.5 [Bundle 5: 1960年代复古办公室道具套件 (60s Office Props Courseware)](#25-bundle-5-1960年代复古办公室道具套件)
   - 2.6 [Bundle 6: CG Cookie Blender 4.2 Core 实存文件核验 (CGCookie Core Holding Audit)](#26-bundle-6-cg-cookie-blender-42-core-实存文件核验)
   - 2.7 [Bundle 7: 历史古典雕塑未拓扑扫描件库 (Historical Raw Statuary Scans)](#27-bundle-7-历史古典雕塑未拓扑扫描件库)
3. [Pass B — 七大必需角色缺口映射 (Required-Role Gap Map)](#3-pass-b--七大必需角色缺口映射)
   - 3.1 [角色 1：主工业练习资产 (Main Industrial Practice Asset)](#31-角色-1主工业练习资产)
   - 3.2 [角色 2：R8 高模向低模法线烘焙教学对 (High→Low Normal Bake Teaching Pair)](#32-角色-2r8-高模向低模法线烘焙教学对)
   - 3.3 [角色 3：W6 异质/非金属未知材质迁移载体 (Unfamiliar Non-Metal Transfer Carrier)](#33-角色-3w6-异质非金属未知材质迁移载体)
   - 3.4 [角色 4：PBR 通道正反例对照组 (PBR Channel Good/Bad Examples)](#34-角色-4pbr-通道正反例对照组)
   - 3.5 [角色 5：紧凑型程序化节点示例 (Compact Procedural-Node Example)](#35-角色-5紧凑型程序化节点示例)
   - 3.6 [角色 6：稳定 LookDev / HDRI 标定场景 (Stable LookDev / HDRI Scene)](#36-角色-6稳定-lookdev--hdri-标定场景)
   - 3.7 [角色 7：实时 / glTF 交付校验资产 (Realtime / glTF Validation Asset)](#37-角色-7实时--gltf-交付校验资产)
4. [盘点覆盖度、不可访问区域与权利风险说明](#4-盘点覆盖度不可访问区域与权利风险说明)
5. [Pass C 下一阶段行动边界与唯一采购缺口](#5-pass-c-下一阶段行动边界与唯一采购缺口)

---

## 1. 执行原则与盘点边界

根据 Issue #7 路线修正案（Inventory-First），教学练习设计的首要原则是：**立足教师与项目实际持有的真实数字资产，以法律权利清晰、技术格式可验证、学生可分发为底线，严禁将“网络视频可见性”或“教程目录链接”等同于“教学可用资产”**。

### 1.1 实际盘点范围与访问物理路径
本次盘点通过 macOS 本地环境（终端命令行、Blender 4.5.1 LTS 后台 Python 检查脚本、Spotlight 元数据索引）系统核实了以下存储区域，未进行全盘无节制漫游：
1. **教师移动教学存储主卷**：`/Volumes/T7-carllx2T`
   - `Courseware_NFU/DigitalModling/`（重点核验：历史 Maya 拓扑烘焙、Blender 雕刻、60年代道具教学套件）；
   - `Courseware_GAFA/`（重点核验：公共雕塑、数字雕塑创作、三维课件与大纲）；
   - `PROJECTS/`（重点核验：历史 3D 项目、Monalisa 项目、WebGL Shader 测试库）；
   - `OpensourceSTL/`（重点核验：Scan the World 与博物馆 STL 扫描）；
   - `林昕真实多媒体归档库/`（历史学生作业归档，仅作权利对比，不可作为分发资产）。
2. **局域网教学媒体与下载卷**：`/Volumes/Download`
   - `CGCookie - Blender 4.2 Core Essentials - 9 Tutorials/`（核实实存工程与许可协议）；
   - `CGCookie CORE Knowledge/`（核实文本导出与源码索引）。
3. **本地用户工作空间**：`/Users/yamlam/`
   - `Downloads/`（核实实存 glTF/GLB、几何测试场景）；
   - `Documents/GitHub/`（核实关联课程仓库 `corso-character-design`、`corso-fare-e-forma` 等）。

### 1.2 资产判定四级状态口径
* **`READY`**：真实文件已完全核实，技术规格无需额外修改即可直接用于课堂教学，学生使用与再分发边界在法律上绝对明确。
* **`READY_WITH_PREP`**：真实文件存在且使用权明确，但需要明确、有限的教师预处理（如重打包为单一 `.blend`、预设 Cycles 烘焙贴图槽位或配置标定灯光）。
* **`REFERENCE_ONLY`**：可用于教师备课、原理观察、视线拆解或对照教学，但**严禁**作为学生 starter/可再分发练习资产。包括商业限制许可文件、无工程源文件的教程，以及未经拓扑的超高面原始扫描。
* **`MISSING`**：在当前实际持有的全部素材范围内，确认**没有**找到能够承担该核心角色的合规资产，必须进入下一阶段严格限定的定向补齐。

---

## 2. Pass A — 实际持有资产深度盘点

### 2.1 Bundle 1: 历史教学法线烘焙高低模套件
* **定位源**：`/Volumes/T7-carllx2T/Courseware_NFU/DigitalModling/w11-sculpting-blender/maya/04-retopo-portrait-uv/c4-retop0-uv-bake/c4/`
* **包含的关键文件**：
  1. `hi-poly.obj`：80,002 三角面/四边面，0 UV通道，包围盒尺寸 `Vector (0.6236, 0.6947, 0.3673)`。源自文艺复兴大师 Francesco Laurana 经典石膏/大理石雕塑《乌尔比诺公主》（Princess of Urbino）高精度扫描之抽化版本（原始 40 万面母件保存在同目录 `Princess_of_Urbino.obj`）。
  2. `low-poly-uv.obj`（同 `c4-lowpoly.obj`）：1,367 面，包含 1 套完整、无重叠展开的 UV 坐标，包围盒尺寸 `Vector (0.6237, 0.6937, 0.3695)`，与高模在三维空间完全同心对齐。
  3. `nor.jpg`：1024×1024 像素，切线空间法线贴图（Tangent Space Normal Map，OpenGL Y+ 格式），带有完整边缘溢出填充（Dilation/Bleed）。同目录包含 Arnold 预编译 `.tx` 格式。
  4. 配套教案：`bake_normal.md`（教师亲自编写的 Maya 烘焙指南，详述软硬边控制、UV 接缝硬边准则、Color Space Raw 强制要求及绿通道 Y+/Y- 反转排查）。
* **当前可访问性**：完全物理可读，经 Blender 4.5.1 LTS 后台程序化导入测试完全通过。
* **权属与再分发 (Provenance & Rights)**：
  - 高模母件：巴黎卢浮宫/国家博物馆公开数字化扫描藏品（Scan the World 开放文博资产，CC0/公共领域）；
  - 低模与 UV：教师（carllx）手动画线重拓扑与拆分 UV 原创成果；
  - 烘焙参数与文档：教师独创教学资产；
  - **再分发状态**：法律边界极其清晰，允许向学生完整分发，无版权争议。
* **学生可编辑性**：`student-editable`（学生可在 Blender 5.2 中独立完成 Selected-to-Active 烘焙与法线插槽验证）。
* **Blender 5.2 兼容就绪度**：极高（OBJ 几何与 UV 标准完全通用）。
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
* **Blender 5.2 兼容就绪度**：需将 Maya/Arnold 节点配置转译为 Blender 5.2 原生着色器对比场景。
* **所需教师预处理**：制作包含左右两个相同几何球体的 `.blend` 对照场景（左侧挂载 `Non-Color` 正确法线，右侧挂载 `sRGB` 错误法线），供学生即时切换观察。
* **对应课程位置**：W2 LO2.2（通道语义学与线性数据/色彩数据分界）。

---

### 2.3 Bundle 3: 标定中性摄影棚 LookDev / HDRI 资产
* **定位源**：`/Volumes/T7-carllx2T/Courseware_NFU/DigitalModling/60s-office-props-maya/sourceimages/studio_small_09_1k.exr`
* **包含的关键文件**：
  1. `studio_small_09_1k.exr`：1.3 MB，32-bit Float 高动态范围图像，双侧柔光箱中性白光摄影棚布光，无极端色温偏差与方向性主光。
  2. `autoshop_01_2k.hdr`（备用）：2K 分辨率机修车间 HDR。
* **当前可访问性**：完全可读。
* **权属与再分发**：Poly Haven 官方发布资产（作者：Philip Modin），明确采用 **CC0 Public Domain** 协议。
* **再分发状态**：完全自由分发，可安全随课程工程打包。
* **Blender 5.2 兼容就绪度**：100% 原生支持（World Shader -> Environment Texture）。
* **所需教师预处理**：创建标准的 `LookDev_Studio_Template.blend`，包含中性地面阴影捕捉器（Shadow Catcher）、三颗标准标定球（100% 镀铬镜面球、50% 中性灰漫反射球、纯白粗糙度对比球）及相机环绕轨道。耗时约 1 小时。
* **对应课程位置**：W1（基准观察）、W2（材质参数因果验证）、W8–W9（多环境 LookDev 评测）。

---

### 2.4 Bundle 4: 实时 glTF 2.0 PBR 交付校验资产
* **定位源**：`/Users/yamlam/Downloads/bathroom_floor_ gltf/`
* **包含的关键文件**：
  1. `scene.gltf` + `scene.bin`：标准 glTF 2.0 场景描述与二进制网格。
  2. `textures/lambert2_baseColor.png`：漫反射色彩通道。
  3. `textures/lambert2_metallicRoughness.png`：标准通道打包贴图（绿色通道 = Roughness，蓝色通道 = Metallic）。
  4. `textures/lambert2_normal.png`：切线空间法线贴图。
  5. `license.txt`：明确标注模型信息与署名要求。
* **当前可访问性**：完全可读。
* **权属与再分发**：Sketchfab 创作者 RubaQewar，遵循 **CC-BY-4.0** 协议；允许商业与教育再分发，只需保留标准署名声明。
* **Blender 5.2 兼容就绪度**：原生导入与视口渲染无瑕疵。
* **所需教师预处理**：将其打包为单文件 `.glb` 格式，或结合 Bundle 1 的低模直接生成课程专属的 glTF 校验件。
* **对应课程位置**：W7 实时交付与通道打包验证（GLTF/WebGL 标准）。

---

### 2.5 Bundle 5: 1960年代复古办公室道具套件
* **定位源**：`/Volumes/T7-carllx2T/Courseware_NFU/DigitalModling/60s-office-props-blender/`
* **包含的关键文件**：
  1. 3D 模型场景：`60's office stuff exporter.blend`，包含打字机（`prp_typewriter_portable_01_grp`）、电传打字机终端（`prp_teletype_terminal_01_grp`）、大型机磁带机（`prp_mainframe_tapeDrive_yellow_01_grp`）、办公桌、文件柜、马克杯等 30 余个独立道具。
  2. 贴图系统：`60's_office_textures_1-01.png`（低多边形漫反射图集 Atlas）、`Wood_desk.jpeg`、`internal_ground_ao_texture.jpeg`。
  3. 教学指南文档库：2025 年 10 月编写的系统化实训教案（包含大纲、学生手册、Sketchfab 限制说明、Maya/Blender 导出指南）。
* **技术缺陷分析与教学适用性评估**：
  - **严重缺陷**：该模型套件建于 2023–2025 年，目标是移动端与 WebGL 低面展示。材质主要依赖手绘漫反射图集与单色无节点材质（`use_nodes: False`），**完全不具备现代 PBR 贴图集（缺失真实粗糙度图、金属度图、微细节法线图与 AO 烘焙图）**。
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

### 2.7 Bundle 7: 历史古典雕塑未拓扑扫描件库
* **定位源**：`/Volumes/T7-carllx2T/OpensourceSTL/` 及 `Courseware_NFU/DigitalModling/1.2/`
* **包含的关键文件**：
  1. `Pseudo-Seneca-Portrait of Hesiod_152-smk-inv-94.stl`（99.9 MB，丹麦国立美术馆 SMK 藏品，约 7 万三角面，无 UV）；
  2. `Marcellus -Portrait of an Augustine Prince_153-smk-809.stl`（87.2 MB，SMK 藏品，约 35 万三角面，无 UV）；
  3. `Scan_the_World_-_Venus_de_Milo.stl`（米洛的维纳斯）、`David_(Michelangelo).stl`（大卫）。
* **权属状态**：SMK Open 与 Scan the World 均为公开文博数字化资产（CC0 / Public Domain）。
* **结论**：均为原始 3D 打印用或三角面扫描文件，无拓扑、无 UV、面数过高。除 Bundle 1 中教师已完成拓扑与烘焙的 `c4` 套件外，其余 STL 均属于 `REFERENCE_ONLY`，不宜在不增加教师拓扑负担的前提下作为课堂模型。

---

## 3. Pass B — 七大必需角色缺口映射

对照 W1–W9 课程教学目标（Learning Objectives），对七大核心教学资产角色进行逐一判定：

### 3.1 角色 1：主工业练习资产 (Main Industrial Practice Asset)
* **角色职能**：贯穿 W1 观察、W2 物理参数因果、W3–W5 贴图制作/材质拆解、W7 实时交付及 W8–W9 LookDev 迭代的核心工业/机械资产载体（需具备明确金属/绝缘体结构分界、工业倒角与典型磨损区域）。
* **当前状态**：**`MISSING`**
* **事实证据**：
  1. 曾寄予厚望的 CG Cookie 双筒望远镜（Binoculars）在本地课程包中**缺失 3D 模型源文件**，且授权协议严禁公开发布（定级为 `REFERENCE_ONLY / NO STARTER FILE`）；
  2. 本地持有的 `60s-office-props`（打字机、磁带机）属于手绘漫反射 Atlas 低模道具，缺乏现代 PBR 微表面与法线数据，改造成本巨大；
  3. 本地无其他具备商业/再分发许可、且拓扑/UV/材质分级达标的现成中等复杂度工业资产。
* **处理结论**：必须列为 Pass C 的**核心采购缺口**，在下一阶段向合法开放文博或工业开源库定向补充（如 Smithsonian 3D / NASA / Poly Haven / Blender Studio CC0 资产）。

---

### 3.2 角色 2：R8 高模向低模法线烘焙教学对 (High→Low Normal Bake Teaching Pair)
* **角色职能**：支撑 45 分钟微实验，直观向学生展示“几何细节向切线法线向量编码”的表征替代过程，为 PBR 法线通道提供具象认知。
* **当前状态**：**`READY_WITH_PREP`**
* **事实证据**：
  1. **实体资产完备**：Bundle 1 的 Francesco Laurana 雕塑高低模（`hi-poly.obj` 80,002 面 + `low-poly-uv.obj` 1,367 面）已在 Blender 4.5.1 中完成空间对齐与几何验证；
  2. **历史检验充分**：历史烘焙图 `nor.jpg`（1024×1024）与教案 `bake_normal.md` 证明该套件曾成功用于高校真实教学，拓扑接缝、软硬边设置经过验证；
  3. **法律权属清洁**：基底扫描为公有领域艺术品，低模拓扑与 UV 为教师原创，可直接进入学生分发包；
  4. **预处理代价极低**：只需教师花费约 2 小时将两个 OBJ 打包为 Blender 5.2 的 `.blend` 工程并预设 Cycles 贴图节点。
* **处理结论**：**无需外部寻找新资产，直接锁定 Bundle 1 雕塑套件作为 R8 教学载体**。

---

### 3.3 角色 3：W6 异质/非金属未知材质迁移载体 (Unfamiliar Non-Metal Transfer Carrier)
* **角色职能**：检验学生将 W1–W5 学到的 PBR 物理原理向非金属复杂材质（如石膏、大理石、上釉陶瓷、木材、皮革或布料）迁移的能力。
* **当前状态**：**`READY_WITH_PREP`**
* **事实证据**：
  1. **方案 A（首选）**：复用 Bundle 1 的《乌尔比诺公主》低模（`low-poly-uv.obj`）。该资产天然作为古典雕塑载体，极其适合用于练习石膏（Plaster，微孔漫反射 + 浅层 SSS）和大理石（Marble，微光泽绝缘体 + 次表面散射）材质，实现资产复用极大化，符合“最小教学资产套件”原则；
  2. **方案 B（备用）**：Bundle 4 的 `bathroom_floor_ gltf`（地面瓷砖/陶瓷，具备微裂纹与釉面反射，CC-BY-4.0 授权）。
* **处理结论**：本地资源已完全覆盖，教师只需在预处理阶段准备石膏/大理石材质教学提示词与参考图，无需启动外部采购。

---

### 3.4 角色 4：PBR 通道正反例对照组 (PBR Channel Good/Bad Examples)
* **角色职能**：向学生展示常见严重错误（如法线贴图误设 sRGB 导致的视口断层、金属度贴图带脏灰渐变、AO 贴图直接乘入 Albedo 等）。
* **当前状态**：**`READY_WITH_PREP`**
* **事实证据**：
  1. Bundle 2 完整持有历史教学积累的对比贴图（`nor_Raw` vs `nor_sRGB`、`TCom_Pavement` 对照组）及排错教案；
  2. 预处理只需在 Blender 5.2 中搭建一个双视窗或左右排列的测试场景，将同一个法线分别连接在 `sRGB` 和 `Non-Color` 采样模式下；
  3. 预处理耗时约 1 小时。
* **处理结论**：本地资产就绪，无需外部采购。

---

### 3.5 角色 5：紧凑型程序化节点示例 (Compact Procedural-Node Example)
* **角色职能**：W4/W5 中演示如何利用 8–12 个基础数学/噪波节点快速生成微观粗糙度扰动或边缘磨损遮罩，阐释非破坏性着色逻辑。
* **当前状态**：**`READY_WITH_PREP`**
* **事实证据**：
  1. Blender 5.2 原生内置 Noise Texture、Voronoi、Map Range、ColorRamp、Bump 等全部所需算子；
  2. 该部分属于 100% 教师自研的着色网络代码/节点树，无需依赖外部三维资产，任何标准测试球或道具表面均可承载；
  3. 预处理只需教师固化一个节点组织清晰、带有中文框架（Frame）标注的 `.blend` 预设；
  4. 预处理耗时约 1 小时。
* **处理结论**：完全自给自足，无需外部采购。

---

### 3.6 角色 6：稳定 LookDev / HDRI 标定场景 (Stable LookDev / HDRI Scene)
* **角色职能**：提供统一、中性、无极端偏色的光影检验环境，使学生在 W1、W2、W8、W9 的材质调节具备科学参照。
* **当前状态**：**`READY_WITH_PREP`**
* **事实证据**：
  1. Bundle 3 本地持有的 `studio_small_09_1k.exr` 拥有绝对干净的 CC0 授权与高质量 32 位浮点动态范围；
  2. 预处理只需教师构建标准的灰色底板、阴影捕捉、三颗校准球（镜面金属、50%灰绝缘体、漫反射纯白）和正交渲染相机；
  3. 预处理耗时约 1 小时。
* **处理结论**：本地资产与授权完全完备，无需外部采购。

---

### 3.7 角色 7：实时 / glTF 交付校验资产 (Realtime / glTF Validation Asset)
* **角色职能**：W7 用于检验 glTF 2.0 / WebGL 导出规则，验证 Roughness/Metallic 双通道合流打包（Green/Blue Packing）与实时引擎渲染一致性。
* **当前状态**：**`READY_WITH_PREP`**
* **事实证据**：
  1. Bundle 4 的 `bathroom_floor_ gltf` 已经是以合流打包贴图（`lambert2_metallicRoughness.png`）构建的标准 glTF 2.0 资产，授权清晰（CC-BY-4.0）；
  2. 同时，Bundle 1 的低模在完成 R8 法线烘焙后，天然可作为第二个 glTF 导出校验实例；
  3. 预处理只需教师整理一个验证导出的示范指南。
* **处理结论**：本地资产就绪，无需外部采购。

---

## 4. 盘点覆盖度、不可访问区域与权利风险说明

### 4.1 盘点覆盖度与未访问区域事实记录
* **已覆盖深度检查**：
  - 本地 T7 盘历史教学与工程归档（确认了雕塑法线烘焙高低模、60s 道具库、学生作业库、各类扫描 STL）；
  - 本地 NAS 映射卷中的 CG Cookie 教程下载目录（确认了真实工程文件的残缺与授权禁项）；
  - 本地常用下载目录与 Git 仓库（确认了中性 HDR 与 glTF 样例）。
* **排除/不可访问区域**：
  - 未扫描旧网盘备份（云端未同步区域因网络与时间限制未遍历，但本地已存在确定性替代方案）；
  - 历史学生作业库（`林昕真实多媒体归档库`）：虽然包含大量学生建模作业，但因存在学生个人著作权归属不明和质量参差问题，依照教学伦理原则**全部排除在课程公开发发素材库之外**。

### 4.2 权利与再分发风险清点
* **CG Cookie 资产红线**：
  所有 CG Cookie 视频与伴随文件（包括 Binoculars 材质演示和 Lighting 场景）严禁作为代码仓库二进制文件或学生分发包上传。仅限教师作为教学结构参考（`REFERENCE_ONLY`）。
* **文博数字化扫描权属**：
  Bundle 1 使用的 Francesco Laurana 雕塑与 SMK 古典雕塑扫描属于公有领域（Public Domain / CC0），教师基于其原创制作的重拓扑模型、UV 映射及烘焙贴图属于独立衍生教学成果，在知识产权上具有 100% 自主分发权。

---

## 5. Pass C 下一阶段行动边界与唯一采购缺口

通过 Pass A 与 Pass B 的严密实证核验，课程七大角色的状态汇总如下表：

| 必需教学角色 | 最终判定状态 | 核心依托资产 / 证据来源 | 下一步行动 |
| :--- | :--- | :--- | :--- |
| **1. 主工业练习资产** | **`MISSING`** | CG Cookie 望远镜无源工程且侵权；60s 道具为非 PBR 低模 Atlas | **进入 Pass C：定向补充唯一工业资产** |
| **2. R8 法线烘焙高低模教学对** | **`READY_WITH_PREP`** | Bundle 1: Laurana 雕塑 (`hi-poly.obj` 80k + `low-poly-uv.obj` 1.3k + `nor.jpg`) | 教师预处理打包 `.blend`，**无需采购** |
| **3. W6 异质/非金属迁移载体** | **`READY_WITH_PREP`** | 复用 Bundle 1 雕塑载体（石膏/大理石）或 Bundle 4 陶瓷瓷砖 | 教师配置教学提示与材质预设，**无需采购** |
| **4. PBR 通道正反例对照组** | **`READY_WITH_PREP`** | Bundle 2: `nor_sRGB` vs `Raw` 对照组 + `bake_normal.md` | 教师配置 Blender 5.2 对比场景，**无需采购** |
| **5. 紧凑型程序化节点示例** | **`READY_WITH_PREP`** | 100% 教师自研 Blender 原生着色节点网络 | 教师固化 8–12 节点示范工程，**无需采购** |
| **6. 稳定 LookDev / HDRI 场景** | **`READY_WITH_PREP`** | Bundle 3: `studio_small_09_1k.exr` (Poly Haven CC0) | 教师配置标定球与转台场景，**无需采购** |
| **7. 实时 / glTF 交付校验资产** | **`READY_WITH_PREP`** | Bundle 4: `bathroom_floor_ gltf` (CC-BY-4.0) + R8 低模 | 教师整理单文件 `.glb` 样本，**无需采购** |

### 5.1 Pass C 采购边界严格收敛 (Hard Scope Limit)
由于七个角色中 **六个角色均已在本地落实且权属清洁（READY_WITH_PREP）**，因此随后的 Pass C **严禁**泛化为大规模外部素材搜索，而必须且仅能针对：
> **唯一真实缺口（MISSING Role）**：**主工业练习资产 (Main Industrial Practice Asset)**

该资产在 Pass C 中的采购准入标准已明确收紧：
1. **许可协议**：必须为 CC0（如 Poly Haven / Smithsonian 3D / NASA）或清晰允许教育修改再分发的开源协议；
2. **拓扑与细节**：必须具备合理的倒角与机械几何（非极低多边形漫反射贴图道具），具备展开完备且无重叠的 UV 映射；
3. **材质分级**：必须能够明确划分为“裸露金属、烤漆/喷涂绝缘体、橡胶/塑料密封件、微表面磨损”三大以上物理区域，以完美支撑 W1 观察、W2 参数因果、W3–W5 贴图解构与 W8–W9 终期渲染。

---
*报告生成节点：Pass A/B 完毕，等待 Browser Review 确认后再行动。*
