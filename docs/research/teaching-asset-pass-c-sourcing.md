# 外部实训资产定向采购调研报告 (Teaching Asset Pass C Sourcing Report)

> **文档性质**：外部练习案例资源技术调研与试制候选报告（Issue #7 Pass C 成果与最终收口）  
> **基线上下文**：`docs/research/teaching-asset-feasibility-matrix.md`（Pass A/B 持有资产核查与缺口映射）  
> **实施目标**：为高校 PBR 材质课程提供经过第一方源核实、许可清晰、足以停止搜索并进入试制验证（Teaching Prototype）的外部资产候选（角色 1 与角色 3）。  
> **状态声明**：**Issue #7 asset discovery / sourcing resolved**；**Teaching Kit build / runtime validation not yet complete**。本报告不宣称最终教学工程已就绪或最终作业已冻结。

---

## 目录

1. [执行摘要与候选选定结论 (Executive Summary)](#1-执行摘要与候选选定结论)
2. [角色 1：主工业练习资产候选库调查 (Role 1: Main Industrial Asset)](#2-角色-1主工业练习资产候选库调查)
   - 2.1 [选定试制候选 (ADOPT_WITH_PREP — SELECTED FOR TEACHING PROTOTYPE)：Poly Haven Vintage Flashlight](#21-选定试制候选-adopt_with_prep--selected-for-teaching-prototypepoly-haven-vintage-flashlight)
   - 2.2 [备选候选 (ADOPT_WITH_PREP)：Poly Haven Retro Multimeter](#22-备选候选-adopt_with_preppoly-haven-retro-multimeter)
   - 2.3 [备选候选 (ADOPT_WITH_PREP)：Poly Haven Signal Flashlight](#23-备选候选-adopt_with_preppoly-haven-signal-flashlight)
   - 2.4 [高阶参考 (REFERENCE_ONLY / ADVANCED)：Poly Haven Camera 01](#24-高阶参考-reference_only--advancedpoly-haven-camera-01)
   - 2.5 [格式校验参考 (REFERENCE_ONLY)：Khronos glTF AntiqueCamera & FlightHelmet](#25-格式校验参考-reference_onlykhronos-gltf-antiquecamera--flighthelmet)
   - 2.6 [备选候选 (ADOPT_WITH_PREP)：Khronos glTF SciFiHelmet](#26-备选候选-adopt_with_prepkhronos-gltf-scifihelmet)
   - 2.7 [排除候选 (REJECT)：Khronos glTF DamagedHelmet](#27-排除候选-rejectkhronos-gltf-damagedhelmet)
   - 2.8 [排除候选 (REJECT)：Blender Studio Demo Files 与 Smithsonian 3D 原始扫描](#28-排除候选-rejectblender-studio-demo-files-与-smithsonian-3d-原始扫描)
3. [角色 3：W6 异质/非金属未知材质迁移载体调查 (Role 3: W6 Non-Metal Transfer Carrier)](#3-角色-3w6-异质非金属未知材质迁移载体调查)
   - 3.1 [选定试制候选 (ADOPT_WITH_PREP — SELECTED FOR TEACHING PROTOTYPE)：Poly Haven Antique Ceramic Vase 01](#31-选定试制候选-adopt_with_prep--selected-for-teaching-prototypepoly-haven-antique-ceramic-vase-01)
   - 3.2 [木质备选候选 (ADOPT_WITH_PREP)：Poly Haven Wooden Bowl 01](#32-木质备选候选-adopt_with_preppoly-haven-wooden-bowl-01)
   - 3.3 [轻量备选 (ADOPT_WITH_PREP)：Poly Haven Ceramic Vase 04](#33-轻量备选-adopt_with_preppoly-haven-ceramic-vase-04)
   - 3.4 [排除分析 (REFERENCE_ONLY / REJECT)：文博原始扫描与 3D 打印 STL](#34-排除分析-reference_only--reject文博原始扫描与-3d-打印-stl)
4. [全候选资产比对矩阵 (Comparative Sourcing Matrix)](#4-全候选资产比对矩阵)
5. [Pass D / 教学原型实施设想 (Implementation Hypothesis — Not Accepted)](#5-pass-d--教学原型实施设想-implementation-hypothesis--not-accepted)
6. [后续工作边界与验证 Gate (Next Steps & Sufficiency Stop)](#6-后续工作边界与验证-gate-next-steps--sufficiency-stop)

---

## 1. 执行摘要与候选选定结论

在 Issue #7 Pass A 与 Pass B 中，七大教学角色已完成本地实存盘点与缺口映射。Pass C 针对仅存的 2 个外部缺失角色（角色 1 与角色 3）开展了第一方来源与真实许可调查。

本轮外部资产调研已达到**充分性停止点 (Sufficiency Stop)**，不再开展通用候选搜索。

### 核心候选选定结论：

* **角色 1：主工业练习资产**
  * **选定试制候选 (`ADOPT_WITH_PREP — SELECTED FOR TEACHING PROTOTYPE`)**：**Poly Haven `Vintage Flashlight`**（作者：Omar M. El-Safy，**CC0 1.0 Universal**）。
    * *判定依据*：第一方来源确凿，明确 CC0 许可；几何形态适中（~11K 面），提供 `.blend`、glTF、FBX 及标准 PBR 贴图；具备适合做教学材质分层的外观特征。
    * *待验证项*：其 UV 教学可编辑性（是否存在接缝撕裂或局部拉伸）、在 Blender 真实教学流程中的分层修改便利度、依赖完整性，留待后续试制阶段验证。
  * **主要备选 (`ADOPT_WITH_PREP`)**：**Poly Haven `Retro Multimeter`**（作者：Elli Moeller，CC0 1.0）。科学仪器形态，备选备用。
  * **排除项 (`REJECT`)**：**Khronos `DamagedHelmet`**。该资产包含受 CC BY-NC-4.0 约束的许可组件，因此不满足本项目希望核心学生资产具备简单、宽松 reuse / redistribution 边界的要求，故不作为核心练习资产。

* **角色 3：W6 异质/非金属未知材质迁移载体**
  * **选定试制候选 (`ADOPT_WITH_PREP — SELECTED FOR TEACHING PROTOTYPE`)**：**Poly Haven `Antique Ceramic Vase 01`**（作者：James Ray Cock，**CC0 1.0 Universal**）。
    * *判定依据*：第一方来源确凿，明确 CC0 许可；具备独立的三维回转体曲面（~9K 面），形态与前期工业资产及石膏胸像完全区分；具备玻璃质釉面、开片微结构与粗陶胎底等非金属材质特征。
    * *待验证项*：贴图包内包含的 `Mask01/02/03` 实际通道定义尚待试制解析，实际教学中是否需要教师重新生成遮罩待定。
  * **木质备选 (`ADOPT_WITH_PREP`)**：**Poly Haven `Wooden Bowl 01`**（作者：Oliver Harries，CC0 1.0）。手作原木碗形态，可作为有机木质材质备选。

---

## 2. 角色 1：主工业练习资产候选库调查

### 2.1 选定试制候选 (ADOPT_WITH_PREP — SELECTED FOR TEACHING PROTOTYPE)：Poly Haven Vintage Flashlight
* **资产名称**：Vintage Flashlight
* **官方第一方链接**：`https://polyhaven.com/a/vintage_flashlight`
* **创作者与来源**：Omar M. El-Safy（Poly Haven 官方收录资产）。
* **确切授权许可**：**CC0 1.0 Universal (Public Domain Dedication)**。允许商业与非商业使用、自由修改、再分发与教学打包。
* **技术数据 (第一方核实)**：
  * **面数**：约 11,000 三角面 (11K tris)，单体手持工具尺寸；
  * **UV 状态**：包含 UV；是否存在重叠以及目标教学区域是否适合局部独立编辑，留待 MINIMUM_TEACHABLE_SLICE_RUNTIME_VALIDATION 实测；
  * **格式支持**：提供 `.blend`、`glTF`（`.gltf` / `.glb`）、`FBX`；
  * **贴图规格**：提供 1K、2K、4K 分辨率（PNG/EXR/JPG），包含 Diffuse/Base Color、Roughness、Metallic、Normal (OpenGL & DirectX)、Ambient Occlusion（注：官方未提供预烘焙 Curvature 贴图，8K 贴图不作承诺亦非教学必要）。
* **物理材质表现力 (Pedagogical Interpretation，教学解读)**：
  1. *外壳主体*：可解读为带磨损的有色电介质涂层漆面（低金属度、受控粗糙度）；
  2. *磨损区域*：边缘露出底层金属基底（高金属度）；
  3. *握柄/滑块*：可解读为工程塑料或橡胶绝缘件（高粗糙度电介质）；
  4. *反光碗*：高反光金属反射曲面；
  5. *前端透镜*：透明电介质折射材质。
* **试制关注点**：需在后续独立工单中实际导入 Blender 检查网格层级、UV 孤岛分布，并确认贴图相对路径封装稳定性。
* **判定状态**：**`ADOPT_WITH_PREP — SELECTED FOR TEACHING PROTOTYPE`**

---

### 2.2 备选候选 (ADOPT_WITH_PREP)：Poly Haven Retro Multimeter
* **资产名称**：Retro Multimeter
* **官方第一方链接**：`https://polyhaven.com/a/retro_multimeter`
* **创作者与许可**：Elli Moeller；**CC0 1.0 Universal**。
* **技术数据**：约 15K–25K 三角面；提供 `.blend`、`glTF`、`FBX` 与 1K–4K 贴图。
* **材质表现力**：胶木机壳质感、橡胶绝缘表笔导线、表盘玻璃与镀铬指针。
* **定位**：适合作为高阶实验备选。部件稍多，初学者初次接触时复杂度略高。
* **判定状态**：**`ADOPT_WITH_PREP`**

---

### 2.3 备选候选 (ADOPT_WITH_PREP)：Poly Haven Signal Flashlight
* **资产名称**：Signal Flashlight
* **官方第一方链接**：`https://polyhaven.com/a/signal_flashlight`
* **创作者与许可**：Jiří Ptáček；**CC0 1.0 Universal**。
* **技术数据**：~12K 三角面，提供 `.blend`、`glTF`、`FBX`。
* **材质表现力**：军绿色涂装金属盒、黄铜滑块、挂载皮革带与透镜。
* **定位**：与复古手电筒高度同构的备用选项。
* **判定状态**：**`ADOPT_WITH_PREP`**

---

### 2.4 高阶参考 (REFERENCE_ONLY / ADVANCED)：Poly Haven Camera 01
* **资产名称**：Camera 01
* **官方第一方链接**：`https://polyhaven.com/a/camera_01`
* **创作者与许可**：Rajil Jose Macatangay；**CC0 1.0 Universal**。
* **技术数据**：约 27K 三角面；模型分为机身、镜头与背带三大部件，对应 3 套材质贴图集。
* **材质表现力**：荔枝纹皮革贴皮、阳极氧化铝合金盖板、光学镀膜镜片。
* **定位**：多材质贴图集结构较为复杂，不适合作为前几周单一材质入门 Starter，但适合作为多材质组合体的进阶参考或拆解案例。
* **判定状态**：**`REFERENCE_ONLY / ADVANCED`**

---

### 2.5 格式校验参考 (REFERENCE_ONLY)：Khronos glTF AntiqueCamera & FlightHelmet
* **AntiqueCamera** (`glTF-Sample-Assets`)：Maximilian Kamps / UX3D，**CC0**。木质脚架与黄铜构件。缺少 Blender 原生 `.blend` 工程分层，仅作为 glTF 交付比对参考。定级为 `REFERENCE_ONLY`。
* **FlightHelmet** (`glTF-Sample-Assets`)：Microsoft 捐赠，**CC0**。行业知名 PBR 标杆，但切分为 5 套贴图集，流程偏重。定级为 `REFERENCE_ONLY`。

---

### 2.6 备选候选 (ADOPT_WITH_PREP)：Khronos glTF SciFiHelmet
* **官方仓库**：`https://github.com/KhronosGroup/glTF-Sample-Models/tree/master/2.0/SciFiHelmet`
* **创作者与许可**：Michael Pavlovich (Quixel)；**CC-BY 4.0**（需显式保留原作者署名）。
* **技术特征**：约 15K 面，单套贴图，硬表面倒角良好。
* **定位**：题材偏科幻，缺乏生活常识中的物理材质因果对照，作为 CC-BY 风格备选保留。
* **判定状态**：**`ADOPT_WITH_PREP`**

---

### 2.7 排除候选 (REJECT)：Khronos glTF DamagedHelmet
* **官方仓库**：`https://github.com/KhronosGroup/glTF-Sample-Assets/tree/main/Models/DamagedHelmet`
* **原始作者与许可**：theblueturtle_；包含受 **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** 约束的许可组件。
* **排除原因**：该资产包含受 CC BY-NC-4.0 约束的许可组件，因此不满足本项目希望核心学生资产具备简单、宽松 reuse / redistribution 边界的要求，故不作为核心练习资产。
* **判定状态**：**`REJECT`**

---

### 2.8 排除候选 (REJECT)：Blender Studio Demo Files 与 Smithsonian 3D 原始扫描
* **Blender Studio & Demo Files**：工程体量庞大（数百 MB 至数 GB 开源电影镜头），包含复杂角色绑定与动画，缺乏单体硬件材质因果教学聚焦度。判定为 `REJECT`。
* **Smithsonian 3D 扫描件**：多数为摄影测量三角网格，带有现场布光固定阴影，无分离的粗糙度/金属度通道，重拓扑烘焙改造成本过重。判定为 `REJECT`。

---

## 3. 角色 3：W6 异质/非金属未知材质迁移载体调查

### 3.1 选定试制候选 (ADOPT_WITH_PREP — SELECTED FOR TEACHING PROTOTYPE)：Poly Haven Antique Ceramic Vase 01
* **资产名称**：Antique Ceramic Vase 01
* **官方第一方链接**：`https://polyhaven.com/a/antique_ceramic_vase_01`
* **创作者与许可**：James Ray Cock；**CC0 1.0 Universal**。
* **技术数据 (第一方核实)**：
  * **面数**：约 9,000 三角面 (9K tris)，高约 0.4 米；
  * **形态**：饱满的双曲率回转体瓶身；
  * **UV 状态**：包含 UV；教学区域的 overlap / distortion / local-edit suitability 尚未验证；
  * **格式支持**：提供 `.blend`、`glTF`、`FBX`；
  * **贴图规格**：提供 1K 至 4K 贴图（Diffuse, Roughness, Normal GL/DX, Metalness, AO），并包含官方附加的遮罩文件（`Mask01`, `Mask02`, `Mask03`）。
* **非金属物理特性 (Pedagogical Interpretation，教学解读)**：
  1. *表层玻璃质感*：光滑低粗糙度的釉面反射（纯电介质 F0 基础反射率）；
  2. *微观破损*：法线贴图表现的釉面开片微裂纹（Crackle Crazing）；
  3. *图案层*：釉下青花颜料散射特征；
  4. *底胎*：瓶底圈足露出无釉粗陶土（高粗糙度电介质）。
* **试制关注点**：贴图包中自带的 `Mask01/02/03` 尚未做具体通道语义绑定验证，后续试制需核实其是否可直接用于控制釉面与陶胎混合。
* **判定状态**：**`ADOPT_WITH_PREP — SELECTED FOR TEACHING PROTOTYPE`**

---

### 3.2 木质备选候选 (ADOPT_WITH_PREP)：Poly Haven Wooden Bowl 01
* **资产名称**：Wooden Bowl 01
* **官方第一方链接**：`https://polyhaven.com/a/wooden_bowl_01`
* **创作者与许可**：Oliver Harries；**CC0 1.0 Universal**。
* **技术数据**：约 14K 三角面；提供 `.blend`、`glTF`、`FBX` 与 1K–4K 贴图。
* **材质表现力**：手作木质刀痕、年轮纹理、吸水微孔。可作为有机木质材质备选。
* **判定状态**：**`ADOPT_WITH_PREP`**

---

### 3.3 轻量备选 (ADOPT_WITH_PREP)：Poly Haven Ceramic Vase 04
* **资产名称**：Ceramic Vase 04
* **官方第一方链接**：`https://polyhaven.com/a/ceramic_vase_04`
* **创作者与许可**：James Ray Cock；**CC0 1.0 Universal**。
* **技术数据**：约 2K 三角面，单耳素烧陶罐。
* **判定状态**：**`ADOPT_WITH_PREP` (轻量备选)**

---

### 3.4 排除分析 (REFERENCE_ONLY / REJECT)：文博原始扫描与 3D 打印 STL
* **Smithsonian 3D 文博器皿**：摄影测量贴图带有严重摄影光照阴影，无材质通道分层。定级为 `REFERENCE_ONLY`。
* **Scan the World 社区 STL 扫描**：绝大部分为未展 UV 的纯 3D 打印三角网格，无法直接进行纹理绘制。定级为 `REJECT`。

---

## 4. 全候选资产比对矩阵 (Comparative Sourcing Matrix)

| 目标角色 | 资产名称 | 来源与作者 | 授权协议 | 几何面数 / UV 状态 | 格式支持 | 材质层级表现 (教学解读) | 备课预处理预估 | 判定状态 |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- | :---: | :---: |
| **角色 1: 主工业资产** | **Vintage Flashlight** | **Poly Haven**<br>(Omar M. El-Safy) | **CC0 1.0** | **~11K tris**<br>包含展开 UV | `.blend`<br>glTF, FBX | 涂层电介质外壳+磨损露底金属+塑料握柄+镀铬反光碗+透镜 | 需制作剥离贴图 Starter 与封装 Reference | **`ADOPT_WITH_PREP`<br>(选定试制候选)** |
| 角色 1: 主工业资产 | Retro Multimeter | Poly Haven<br>(Elli Moeller) | CC0 1.0 | ~20K tris<br>包含展开 UV | `.blend`<br>glTF, FBX | 胶木外壳+绝缘表笔导线+玻璃表盘+指针 | 需整理表笔曲线与玻璃层级 | `ADOPT_WITH_PREP`<br>(次选备用) |
| 角色 1: 主工业资产 | Signal Flashlight | Poly Haven<br>(Jiří Ptáček) | CC0 1.0 | ~12K tris<br>包含展开 UV | `.blend`<br>glTF, FBX | 军绿漆面+黄铜滑块+皮革吊带+透镜 | 需配置基础材质槽 | `ADOPT_WITH_PREP`<br>(可用备选) |
| 角色 1: 主工业资产 | Camera 01 | Poly Haven<br>(R. J. Macatangay) | CC0 1.0 | ~27K tris<br>3 套材质分块 | `.blend`<br>glTF, FBX | 荔枝纹蒙皮+阳极氧化盖板+镀膜镜头 | 需配置多槽位联动 | `REFERENCE_ONLY`<br>(高阶参考) |
| 角色 1: 主工业资产 | AntiqueCamera | Khronos glTF<br>(M. Kamps / UX3D) | CC0 1.0 | ~30K tris<br>glTF 标准 | glTF, GLB | 木质脚架+黄铜构件+皮革折页；无 `.blend` | 需自建工程 | `REFERENCE_ONLY`<br>(交付对照) |
| 角色 1: 主工业资产 | FlightHelmet | Khronos glTF<br>(Microsoft 捐赠) | CC0 1.0 | 中等实时面数<br>5 套贴图集 | glTF, GLB | 皮革飞行帽+橡胶面罩管+金属扣；贴图分散 | 结构繁琐需重组 | `REFERENCE_ONLY`<br>(行业标杆) |
| 角色 1: 主工业资产 | SciFiHelmet | Khronos glTF<br>(M. Pavlovich) | CC-BY 4.0 | 约 15K tris<br>单套 PBR | glTF, GLB | 科幻喷漆外壳+护目镜+橡胶密封垫 | 需核验材质槽与署名 | `ADOPT_WITH_PREP`<br>(科幻备选) |
| 角色 1: 主工业资产 | DamagedHelmet | Khronos glTF<br>(theblueturtle_) | **包含 CC BY-NC-4.0 组件** | 经典实时面数 | glTF, GLB | 经典战损头盔；**因包含受 NC 约束组件排除** | N/A | **`REJECT`<br>(不满足宽松再分发要求)** |
| 角色 1: 主工业资产 | Smithsonian 工业扫描 | Smithsonian 3D 馆藏 | CC0 1.0 | 100K–500K<br>原始摄影测量 | OBJ, glTF | 贴图带死阴影，无 PBR 分离通道 | 需重拓扑 (>20h) | `REJECT`<br>(非 PBR 原始扫描) |
| **角色 3: W6 迁移载体** | **Antique Ceramic Vase 01** | **Poly Haven**<br>(James Ray Cock) | **CC0 1.0** | **~9K tris**<br>包含展开 UV | `.blend`<br>glTF, FBX | 玻璃质光滑釉面+开片微裂纹+青花层+粗陶露胎底圈 | 需核实自带遮罩语义与 Starter 配置 | **`ADOPT_WITH_PREP`<br>(选定试制候选)** |
| 角色 3: W6 迁移载体 | Wooden Bowl 01 | Poly Haven<br>(Oliver Harries) | CC0 1.0 | ~14K tris<br>包含展开 UV | `.blend`<br>glTF, FBX | 手作原木刀痕+年轮各向异性+表面微磨损 | 需配置木质着色预设 | `ADOPT_WITH_PREP`<br>(木质平行备选) |
| 角色 3: W6 迁移载体 | Ceramic Vase 04 | Poly Haven<br>(James Ray Cock) | CC0 1.0 | ~2K tris<br>轻量单套 | `.blend`<br>glTF, FBX | 彩绘红陶罐+素烧胎底；面数极简 | 需配置基础材质槽 | `ADOPT_WITH_PREP`<br>(轻量备选) |
| 角色 3: W6 迁移载体 | Smithsonian 陶器扫描 | Smithsonian 3D 馆藏 | CC0 1.0 | 50K–300K<br>未拓扑多边形 | OBJ, glTF | 照片级光影烘死，无材质通道分层 | 需手工改模烘焙 | `REFERENCE_ONLY`<br>(视觉参考) |
| 角色 3: W6 迁移载体 | Scan the World 扫描件 | Scan the World 社区 | 协议多样 | 仅 STL 纯模型 | STL | 无 UV、无贴图、仅适合 3D 打印 | 需拆 UV 制作贴图 | `REJECT`<br>(严重缺失 UV) |

---

## 5. Pass D / 教学原型实施设想 (Implementation Hypothesis — Not Accepted)

> [!NOTE]
> **重要边界声明**：本节记录的内容属于后续教学实施的**初步设计假说 (Implementation Hypothesis — Not Accepted)**，仅用于说明选定候选资产具备支撑后续教学设计的潜在可能性。**本节内容在 Issue #7 中未经实操验证，不构成已冻结的课程标准或教学执行指令**。Issue #7 仅负责确立素材搜索的充分性，不负责规定学生的具体实训动作。

### 5.1 Starter 与 Reference 初步设想 (Hypothesis Only)
* *主工业练习套件设想*：后续可能考虑将 Vintage Flashlight 剥离贴图生成未连接贴图的起始工程，同时保留一份带有 2K 相对路径贴图的参考工程供学生比对。
* *W6 迁移实训套件设想*：后续可能考虑基于 Antique Ceramic Vase 01 配置分层遮罩混合练习，供学生尝试非金属釉面与陶胎的表现。

### 5.2 宏观落位设想 (Hypothesis Only)
* 主工业手电筒具备贯穿观察、参数调控、分层绘制、实时导出与最终评测的潜在承载力；
* 陶瓷花瓶具备作为后期近迁移测试载体的潜在承载力；
* 具体的周次排布、实验时长及节点结构留待后续课程大纲专门阶段审定。

---

## 6. 后续工作边界与验证 Gate (Next Steps & Sufficiency Stop)

1. **外部搜索充分性停止 (Sufficiency Stop)**：
   本报告已提供足够的一手证据证明存在高可用度、明确 CC0 许可且质量达标的外部资产候选。**Issue #7 针对外部素材的发现与调研阶段正式结束，后续不再开展通用候选搜寻**。
2. **下一阶段独立工单**：
   下一阶段应在独立的验证工单（如 `MINIMUM_TEACHABLE_SLICE_RUNTIME_VALIDATION`）中，实际在 Blender 运行时环境中检验主资产的网格可编辑性、贴图封装稳定性与实际预处理负担。**本工单不启动该运行时验证**。

---
*报告更新日期：2026-09-20 | 状态：Pass C 调研充分性停止，候选已选定待后续试制验证。*
