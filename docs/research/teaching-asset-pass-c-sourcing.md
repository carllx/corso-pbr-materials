# 外部实训资产定向采购调研报告 (Teaching Asset Pass C Sourcing Report)

> **文档性质**：外部练习案例资源权威技术调研与采纳决策报告（Issue #7 Pass C 最终交付成果）  
> **基线上下文**：`docs/research/teaching-asset-feasibility-matrix.md`（Pass A/B 持有资产核查与缺口映射）  
> **实施目标**：为高校 PBR 材质课程精准解决已确认的 2 大核心资产缺口（角色 1 与角色 3），杜绝版权法律风险、格式缺陷与过重备课负担。  
> **审查基准**：Blender 4.5.1 LTS 实测基准 / Blender 5.2 兼容预期；CC0 1.0 Universal / CC-BY 4.0 许可合规；原生 PBR 分层物理表现力。

---

## 目录

1. [执行摘要与核心采纳决策 (Executive Summary)](#1-执行摘要与核心采纳决策)
2. [角色 1：主工业练习资产候选库深度调查 (Role 1: Main Industrial Asset)](#2-角色-1主工业练习资产候选库深度调查)
   - 2.1 [首选采纳 (ADOPT)：Poly Haven Vintage Flashlight (复古手电筒)](#21-首选采纳-adoptpoly-haven-vintage-flashlight-复古手电筒)
   - 2.2 [备选采纳 (ADOPT_WITH_PREP)：Poly Haven Retro Multimeter (复古万用表)](#22-备选采纳-adopt_with_preppoly-haven-retro-multimeter-复古万用表)
   - 2.3 [可用备选 (ADOPT_WITH_PREP)：Poly Haven Signal Flashlight (三色信号手电筒)](#23-可用备选-adopt_with_preppoly-haven-signal-flashlight-三色信号手电筒)
   - 2.4 [拆解参考 (ADOPT_WITH_PREP / ADVANCED)：Poly Haven Camera 01 (旁轴相机)](#24-拆解参考-adopt_with_prep--advancedpoly-haven-camera-01-旁轴相机)
   - 2.5 [参考校验 (REFERENCE_ONLY)：Khronos glTF AntiqueCamera & FlightHelmet](#25-参考校验-reference_onlykhronos-gltf-antiquecamera--flighthelmet)
   - 2.6 [附带条件备选 (ADOPT_WITH_PREP)：Khronos glTF SciFiHelmet](#26-附带条件备选-adopt_with_prepkhronos-gltf-scifihelmet)
   - 2.7 [重大合规排除 (REJECT)：Khronos glTF DamagedHelmet (破损头盔)](#27-重大合规排除-rejectkhronos-gltf-damagedhelmet-破损头盔)
   - 2.8 [范围不适排除 (REJECT)：Blender Studio / Demo Assets 与 Smithsonian 3D 扫描](#28-范围不适排除-rejectblender-studio--demo-assets-与-smithsonian-3d-扫描)
3. [角色 3：W6 异质/非金属未知材质迁移载体深度调查 (Role 3: W6 Non-Metal Transfer Carrier)](#3-角色-3w6-异质非金属未知材质迁移载体深度调查)
   - 3.1 [首选采纳 (ADOPT)：Poly Haven Antique Ceramic Vase 01 (青花开片陶瓷瓶)](#31-首选采纳-adoptpoly-haven-antique-ceramic-vase-01-青花开片陶瓷瓶)
   - 3.2 [木质备选 (ADOPT_WITH_PREP)：Poly Haven Wooden Bowl 01 (手作粗陶木碗)](#32-木质备选-adopt_with_preppoly-haven-wooden-bowl-01-手作粗陶木碗)
   - 3.3 [轻量备选 (ADOPT_WITH_PREP)：Poly Haven Ceramic Vase 04 (单耳素烧陶罐)](#33-轻量备选-adopt_with_preppoly-haven-ceramic-vase-04-单耳素烧陶罐)
   - 3.4 [文博类排除分析 (REFERENCE_ONLY / REJECT)：Smithsonian 3D 与 Scan the World 开放藏品](#34-文博类排除分析-reference_only--rejectsmithsonian-3d-与-scan-the-world-开放藏品)
4. [全候选资产综合比对决策矩阵 (Comparative Decision Matrix)](#4-全候选资产综合比对决策矩阵)
5. [教学套件集成与教师备课实操流水线 (Implementation Workflow)](#5-教学套件集成与教师备课实操流水线)
   - 5.1 [Starter 与 Reference 工程分离策略](#51-starter-与-reference-工程分离策略)
   - 5.2 [W1–W9 课程教学主线资产落位图](#52-w1w9-课程教学主线资产落位图)

---

## 1. 执行摘要与核心采纳决策

在 Issue #7 Pass A 与 Pass B 中，课程七大必需角色已锁定 5 个（Bundle 1 教师石膏雕塑烘焙对、Bundle 2 通道正反例、Bundle 3 中性 HDR、Bundle 4 glTF 实时地砖、本地自研程序化节点）。本 Pass C 聚焦于通过第一方资源库定向补齐最后 2 个处于 `MISSING` 状态的核心教学角色。

### 核心采纳结论一览：

* **角色 1：主工业练习资产（贯穿 W1–W5、W7、W8–W9）**
  * **主选采纳 (`ADOPT`)**：**Poly Haven `Vintage Flashlight`**（作者：Omar M. El-Safy，**CC0 1.0**）。
    * *采纳理由*：纯正工业机械造型，体量紧凑（~11K 面），单套无重叠 UV；具备极清晰的“红色涂层外壳（绝缘漆面）→ 边缘磕碰露出裸露金属底材 → 黑色高阻尼手柄与滑块（橡胶/硬质塑料）→ 高反光镀铬反光碗（高反射金属）→ 纯净玻璃透镜（透光电介质）”多物理材质分层；官方直供 `.blend`、glTF 与 1K–8K 全套 PBR 贴图，教师预处理时间 < 1 小时。
  * **次选备用 (`ADOPT_WITH_PREP`)**：**Poly Haven `Retro Multimeter`**（作者：Elli Moeller，**CC0 1.0**）。具备极佳的科学仪器质感与表盘/旋钮细节，适合作为高阶实验或备选工业件。
  * **重大法律排除 (`REJECT`)**：**Khronos `DamagedHelmet`**。经第一方元数据审查，其实际许可为 **CC BY-NC 4.0 (NonCommercial)**，带有严格非商用条款，存在学生作品集展示与开源教学包商用边界纠纷隐患，予以彻底否决。

* **角色 3：W6 异质/非金属未知材质迁移载体（W6 近迁移评测）**
  * **主选采纳 (`ADOPT`)**：**Poly Haven `Antique Ceramic Vase 01`**（作者：James Ray Cock，**CC0 1.0**）。
    * *采纳理由*：完美脱离 W1–W5 的机械工业语义与 R8 的哑光石膏语义；包含完整的三维曲面形体（~9K 面，0.4m 高）；具有极具代表性的非金属物理特征——高反光玻璃质釉层（Dielectric F0 ~0.04）、开片釉微裂纹（Crackle Crazing Normal）、釉下青花颜料散射层（Underglaze）、底部露胎无釉粗陶（Porous Clay Bisque）；提供全套 1K–8K PBR 贴图与多重遮罩（Mask01/02/03），教师可直接拆解为釉面与陶胎分层教学 Starter。
  * **木质备选 (`ADOPT_WITH_PREP`)**：**Poly Haven `Wooden Bowl 01`**（作者：Oliver Harries，**CC0 1.0**）。手作雕刻木碗（~14K 面），具备明显的木质各向异性与纤维微磨损，可作为有机木质材质的对比练习。

---

## 2. 角色 1：主工业练习资产候选库深度调查

主工业练习资产要求支撑 W1 观察、W2 物理参数因果验证、W3–W5 材质纹理制作、W7 实时引擎交付与 W8–W9 多环境 LookDev 评测。必须具备非重叠展平 UV、清晰机械倒角，以及由裸露金属、涂层漆面、橡胶/塑料和微表面磨损构成的多物理层。

### 2.1 首选采纳 (ADOPT)：Poly Haven Vintage Flashlight (复古手电筒)
* **资产名称**：Vintage Flashlight
* **官方第一方链接**：`https://polyhaven.com/a/vintage_flashlight`
* **资产类别与创作者**：工业日用机械道具；作者为 **Omar M. El-Safy**（Poly Haven "Project Lighthouse" 原生资产）。
* **确切授权许可**：**CC0 1.0 Universal (Public Domain Dedication)**。
  * *再分发权限*：无条件允许商业与非商业使用、自由修改、再分发与教学套件打包，无需署名（课程为尊重版权仍将规范署名）。
* **技术几何与数据**：
  * **面数**：约 **11,000 三角面 (11K tris)**，尺寸长宽约 0.3 米。拓扑结构兼顾了机械边缘倒角（Bevels）与轻量化实时渲染效率。
  * **UV 展开**：单套高效非重叠 UV 布局（Non-overlapping UVs），接缝自然隐藏于机械部件缝隙与背部。
  * **支持格式**：官方提供 `.blend`（原生材质节点树）、`glTF`（`.gltf` / `.glb`）、`FBX`。
  * **贴图规格**：提供 1K、2K、4K、8K 格式（PNG/EXR/JPG），包含 Diffuse/Base Color、Roughness、Metallic、Normal (OpenGL & DirectX 双格式)、Ambient Occlusion。
* **物理材质分层表现力 (Material Stratification)**：
  1. **涂层绝缘体 (Painted Dielectric)**：主体电池盒外壳采用厚质红色油漆，表现中低粗糙度、无金属度（Metallic = 0）的电介质反射特性；
  2. **边缘磨损露金属 (Bare Metal Substrate Wear)**：箱体棱角与机械锁扣处呈现剧烈的油漆剥落（Paint Chipping），露出深色氧化冷轧钢板底材（Metallic = 1, F0 极高）；
  3. **塑料/橡胶绝缘件 (Hard Plastic / Rubber Seals)**：粗壮的黑色工程塑料提手与开关滑块，呈现出与金属完全不同的散射微观粗糙度与抗指纹质感；
  4. **镜面高反光金属 (Specular Metal Reflector)**：灯头内部呈抛光镀铬/铝制旋转曲面，粗糙度极低，展示金属近乎镜面的菲涅尔与环境反射；
  5. **透光玻璃与紧固件 (Clear Glass & Fasteners)**：正面平光透镜与内部灯珠（玻璃电介质折射率与穿透性），以及表面未涂装的固定螺栓。
* **教学角色适用性**：**全周期核心 Student Starter & Teardown 案例**。完美支撑 W1–W9 全部工业机械知识点，模型体量适中，学生不会因庞大面数产生硬件渲染卡顿。
* **教师备课负担**：**极低 (< 1 小时)**。下载 2K/4K 官方 `.blend`，保留几何体并清空着色器槽位生成 `W1_Flashlight_Starter.blend`，保留原材质作为 `_Reference.blend`。
* **最终判定**：**`ADOPT` (首选采纳)**

---

### 2.2 备选采纳 (ADOPT_WITH_PREP)：Poly Haven Retro Multimeter (复古万用表)
* **资产名称**：Retro Multimeter
* **官方第一方链接**：`https://polyhaven.com/a/retro_multimeter`
* **资产类别与创作者**：电子电气科学仪器；作者为 **Elli Moeller**（同样为 Project Lighthouse 贡献）。
* **确切授权许可**：**CC0 1.0 Universal**（自由分发与二次加工）。
* **技术几何与数据**：
  * **面数**：约 15K–25K 三角面，包含仪器外壳、旋钮、金属提手及卷曲的红黑绝缘测试表笔。
  * **UV 与格式**：无重叠 UV 布局；提供 `.blend`、`glTF`、`FBX`；提供 1K 至 8K 贴图全集。
* **物理材质分层表现力**：
  1. **酚醛树脂/胶木外壳**：哑光、带有微细颗粒感的深色绝缘机壳；
  2. **卷曲软质橡胶电缆**：柔性绝缘体表笔引线，展示高粗糙度橡胶材质；
  3. **透明表盘玻璃与印刷纸质刻度**：玻璃罩（透过与双重反射）与内部微细印刷表盘（无光漫反射纸张）；
  4. **滚花金属/塑料复合旋钮**：防滑机械滚花纹理与指示刻线；
  5. **镀铬表针、接线柱与金属探针**：小面积高精度裸露金属部件。
* **教学角色适用性**：**高级实训备选或大作业候选**。仪器细节极度精致，物理分层极其严密；微小部件稍多，对初学者初次展贴图稍有认知负担，更适合作为高阶对比。
* **教师备课负担**：**低 (~1.5 小时)**。需对表笔曲线与表盘玻璃层级在 Blender 中做轻度分组整理。
* **最终判定**：**`ADOPT_WITH_PREP` (优秀次选备用)**

---

### 2.3 可用备选 (ADOPT_WITH_PREP)：Poly Haven Signal Flashlight (三色信号手电筒)
* **资产名称**：Signal Flashlight
* **官方第一方链接**：`https://polyhaven.com/a/signal_flashlight`
* **资产类别与创作者**：军旅工业道具；作者为 **Jiří Ptáček**。
* **确切授权许可**：**CC0 1.0 Universal**。
* **技术几何与数据**：~12K 三角面，4K 纹理，支持 `.blend` / `glTF` / `FBX`。
* **物理材质分层表现力**：军绿色烤漆冲压金属外壳（冲压 "DAYMON" 凸起字样）、三个机械拨动滑块开关（黄铜/裸钢）、粗糙暗哑反光罩、挂载的开裂老旧皮革吊带（皮质电介质）与透镜。
* **教学角色适用性**：与 2.1 复古手电筒高度同构，且多了一条皮革吊带，是合格的对等备选。因 2.1 的红色漆面与镀铬反光碗在视觉对比上更为鲜明强烈，故本件作为备用。
* **最终判定**：**`ADOPT_WITH_PREP` (合格备选)**

---

### 2.4 拆解参考 (ADOPT_WITH_PREP / ADVANCED)：Poly Haven Camera 01 (旁轴相机)
* **资产名称**：Camera 01
* **官方第一方链接**：`https://polyhaven.com/a/camera_01`
* **资产类别与创作者**：精密光学机械；作者为 **Rajil Jose Macatangay**。
* **确切授权许可**：**CC0 1.0 Universal**。
* **技术几何与数据**：约 **27,000 三角面 (27K tris)**。分为机身（Body）、镜头筒（Lens Body）与背带（Strap）三大独立部件，对应 3 套材质通道与贴图系统。
* **物理材质分层表现力**：极为丰满——荔枝纹蒙皮（Pebbled Leatherette）、拉丝阳极氧化铝合金上下盖板、光学玻璃多层镀膜镜片、防滑金属滚轮与皮质背带扣。
* **教学角色适用性**：**进阶拆解与高阶 LookDev 典范 (Advanced Reference / Teardown)**。由于该资产天然采用了 3 套多材质贴图槽，若作为学生入门前几周的 Starter 会分散学生对单一 Principled BSDF 的聚焦度，但极适于 W5 或 W8 作为教师演示“多材质组合体”的标杆案例。
* **教师备课负担**：**中等 (~2 小时)**。需配置三组材质槽位的联动展示。
* **最终判定**：**`ADOPT_WITH_PREP` (高阶参考/拆解资产)**

---

### 2.5 参考校验 (REFERENCE_ONLY)：Khronos glTF AntiqueCamera & FlightHelmet
* **资产 1：AntiqueCamera**
  * *官方仓库*：`https://github.com/KhronosGroup/glTF-Sample-Assets/tree/main/Models/AntiqueCamera`
  * *作者与许可*：Maximilian Kamps & UX3D；**CC0 1.0 Universal**。
  * *技术规格*：经典木质三脚架老式大画幅相机，glTF 2.0 格式。包含木质支架（清漆电介质）、黄铜构件（金属度 1）、皮腔折页（吸光纤维/皮革）。
  * *局限性*：仅维护 glTF/GLB 交付文件，缺少 Blender 原生带有分层节点组织与修改器的源工程（.blend），不利于学生从基础贴图绘制开始介入。
  * *判定*：**`REFERENCE_ONLY` (glTF 导出与渲染器对照校验资产)**。
* **资产 2：FlightHelmet**
  * *官方仓库*：`https://github.com/KhronosGroup/glTF-Sample-Assets/tree/main/Models/FlightHelmet`
  * *作者与许可*：微软 (Microsoft) 捐赠；**CC0 1.0 Universal**。
  * *技术规格*：行业知名的 PBR 跑分黄金标杆，包含皮革飞行帽、氧气面罩橡胶管、透明遮阳板、金属铰链。
  * *局限性*：资产切分为多达 5–6 组独立的贴图集（LeatherParts, MetalParts, Glass 等），教学流程复杂度偏高。
  * *判定*：**`REFERENCE_ONLY / DEFER` (工业对照参考标杆)**。

---

### 2.6 附带条件备选 (ADOPT_WITH_PREP)：Khronos glTF SciFiHelmet
* **资产名称**：SciFiHelmet
* **官方仓库*：`https://github.com/KhronosGroup/glTF-Sample-Models/tree/master/2.0/SciFiHelmet`
* **作者与许可**：Michael Pavlovich (Quixel)；**CC-BY 4.0**（需显式保留署名）。
* **技术特征**：经典单套贴图科幻头盔（2048×2048），工业硬表面倒角与法线烘焙极佳。
* **局限性**：科幻幻想题材相比现实中的老式手电筒或仪器，对学生理解真实物理世界“电介质折射率、灰尘吸附规律、金属锈蚀因果”缺乏直观的生活经验参照。
* **判定**：**`ADOPT_WITH_PREP` (科幻风格可用备选，需维持 CC-BY 署名)**。

---

### 2.7 重大合规排除 (REJECT)：Khronos glTF DamagedHelmet (破损头盔)
* **官方仓库**：`https://github.com/KhronosGroup/glTF-Sample-Assets/tree/main/Models/DamagedHelmet`
* **原始作者与维护者**：theblueturtle_ (由 ctxwing 转换为 glTF)。
* **确切法律许可**：**Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**。
* **技术表现**：行业内最著名的 PBR 测试头盔，磨损、锈蚀、金属与发光通道一应俱全。
* **排除原因（一票否决）**：
  * **NonCommercial (NC) 严厉限制**：高校开源教学仓库若包含 CC-BY-NC 资产，不仅无法并入标准开源许可证分发包，更会导致学生将该模型渲染成果用于商业求职作品集、商业众筹或商业外包时面临侵权风险；
  * **与课程合规红线冲突**：本课程设计原则严格要求采购资产为 **CC0** 或无歧义商用允许的 **CC-BY**，绝不将带 NC 限制的资产作为核心练习包向学生分发。
* **最终判定**：**`REJECT` (因商业限制协议与法务风险彻底排除)**

---

### 2.8 范围不适排除 (REJECT)：Blender Studio / Demo Assets 与 Smithsonian 3D 扫描
* **Blender Studio & Demo Files (`blender.org/download/demo-files/`)**：
  * *现状*：全部为 Blender 各版本启动画面、毛发模拟或完整开源电影镜头（如 charge, spring）。工程文件多达数百 MB 至数 GB，包含复杂灯光动画绑定，没有针对单体工业 PBR 参数因果教学定制的独立硬表面道具。
  * *判定*：**`REJECT` (体量过载，教学针对性缺失)**。
* **Smithsonian 3D 工业/仪器扫描 (`3d.si.edu`)**：
  * *现状*：如阿波罗 11 号指令舱、历史电报机等，属于文博科研级原始摄影测量三角面网格（Photogrammetry Scans）。贴图为摄影漫反射光照贴图（带烘死的光影投影），无任何分离的 Roughness/Metallic 通道，无机械倒角拓扑，教师重拓扑烘焙预处理时间超过 20 小时。
  * *判定*：**`REJECT` (非 PBR 原始扫描，教师改装成本不可接受)**。

---

## 3. 角色 3：W6 异质/非金属未知材质迁移载体深度调查

角色 3 的核心使命是检验学生在 W6 时的**近迁移（near-transfer）能力**：当面对一个此前在 W1–W5 从未见过的纯非金属（Dielectric）、拥有丰富三维曲率与手工艺细节的有机/工艺器物时，能否摆脱“金属度滑块依赖”，准确运用菲涅尔、基础反射率 F0 (~0.04)、微观粗糙度分布与透明/半透明多层散射表现质感。

*特别排他原则*：严禁复用主工业手电筒（金属主体），严禁复用 R8 石膏雕塑胸像（学生在 W2/W3 法线烘焙微实验中已深度接触，不再具有“未知资产”测试效应）。

---

### 3.1 首选采纳 (ADOPT)：Poly Haven Antique Ceramic Vase 01 (青花开片陶瓷瓶)
* **资产名称**：Antique Ceramic Vase 01
* **官方第一方链接**：`https://polyhaven.com/a/antique_ceramic_vase_01`
* **资产类别与创作者**：古典手工艺陶瓷器皿；作者为 **James Ray Cock**。
* **确切授权许可**：**CC0 1.0 Universal (Public Domain Dedication)**（学生分发无任何法律门槛）。
* **技术几何与数据**：
  * **面数**：约 **9,000 三角面 (9K tris)**，高约 0.4 米。具备优美饱满的双曲率瓶身回转体形态。
  * **UV 展开**：标准、连续、无拉伸的单套无重叠 UV 展平。
  * **支持格式**：官方 `.blend`、`glTF`、`FBX`。
  * **贴图规格**：提供 1K 至 8K 贴图，涵盖 Diffuse、Roughness、Normal (GL/DX)、Metalness (纯黑/非金属校验)、AO，以及官方定制的三组分层遮罩贴图（`Mask01`, `Mask02`, `Mask03`）。
* **非金属物理特性与近迁移教学点 (Pedagogical Fit)**：
  1. **双层光学表现（清漆/釉面与釉下彩）**：
     * *表层*：高平滑度、低粗糙度的玻璃质釉面（Vitreous Glaze），展现纯电介质的镜面反射与清晰菲涅尔高光（F0 标定在 0.04 左右）；
     * *釉下层*：古董青花纹样（Cobalt Blue Pattern），展示颜料穿透透明玻璃质釉层后在陶瓷胎体表面的漫散射色彩；
  2. **开片微结构表征（Crackle Crazing）**：
     * 陶瓷烧制过程中釉面与胎体膨胀系数不一导致的微观龟裂网络，由 Normal Map 细腻刻画，直观展示“法线扰动与镜面高光断裂”在非金属表面的物理交互；
  3. **露胎素烧粗陶底圈（Unglazed Foot Rim）**：
     * 花瓶底部放置面无釉，露出高粗糙度、多孔吸光的陶土胎质（Porous Bisque），与瓶身釉面形成极其强烈的电介质粗糙度对比；
  4. **缝隙灰尘与微观磨损**：
     * 开片缝隙与瓶底凹槽的微脏污沉积（通过 AO 与 Mask 提取），考察学生对灰尘非金属材质叠加的掌控。
* **教学角色适用性**：**完美的 W6 迁移能力测试载体**。既彻底排除了任何金属反光成分，又具备高反光釉面与哑光露胎的极端对比，是考察学生对 Principled BSDF 非金属参数理解的理想教具。
* **教师备课负担**：**极低 (< 45 分钟)**。只需提供一个去除贴图的 Starter `.blend`，并保留开片法线贴图和遮罩，指导学生建立釉面/陶胎分层着色。
* **最终判定**：**`ADOPT` (首选采纳)**

---

### 3.2 木质备选 (ADOPT_WITH_PREP)：Poly Haven Wooden Bowl 01 (手作粗陶木碗)
* **资产名称**：Wooden Bowl 01
* **官方第一方链接**：`https://polyhaven.com/a/wooden_bowl_01`
* **资产类别与创作者**：木质器物；作者为 **Oliver Harries**。
* **确切授权许可**：**CC0 1.0 Universal**。
* **技术几何与数据**：约 **14,000 三角面 (14K tris)**；提供 `.blend`、`glTF`、`FBX`；全套 1K–8K PBR 贴图。
* **非金属物理特性与教学点**：
  1. **木质纤维各向异性与年轮纹理**：顺着碗壁年轮延展的粗糙度与凹凸纹理；
  2. **手工凿削刀痕与边缘磕碰**：展示有机材质独特的凹陷、钝角受损特征，区别于机械倒角；
  3. **孔隙吸水与表面抛光过渡**：碗内外壁由于经常使用造成的包浆（局部粗糙度降低）与底部的干燥木质对比。
* **教学角色适用性**：优秀的木质非金属案例，可作为学生自选练习题库，与陶瓷花瓶互为平行选项。
* **最终判定**：**`ADOPT_WITH_PREP` (木质材质优选备用)**

---

### 3.3 轻量备选 (ADOPT_WITH_PREP)：Poly Haven Ceramic Vase 04 (单耳素烧陶罐)
* **资产名称**：Ceramic Vase 04
* **官方第一方链接**：`https://polyhaven.com/a/ceramic_vase_04`
* **创作者与许可**：James Ray Cock；**CC0 1.0 Universal**。
* **技术几何与数据**：约 **2,000 三角面 (2K tris)**，单耳陶壶造型。
* **物理特征**：彩绘红陶与局部釉面，形态优雅，面数极简。适合作为性能受限机房的备用方案。
* **最终判定**：**`ADOPT_WITH_PREP` (极低面数轻量备选)**

---

### 3.4 文博类排除分析 (REFERENCE_ONLY / REJECT)：Smithsonian 3D 与 Scan the World 开放藏品
* **Smithsonian 3D 文博陶瓷/器皿扫描 (`3d.si.edu`)**：
  * *现状*：馆藏包含大量美洲原住民陶罐、中国古陶瓷等 CC0 资源。
  * *致命技术缺陷*：模型为摄影测量多边形包裹体，贴图为单张含有强烈博物馆布光阴影的漫反射摄影照片；缺失法线、粗糙度贴图，且底部通常闭合不全或有支撑座网格粘连。
  * *判定*：**`REFERENCE_ONLY` (仅适于视觉鉴赏与色彩参考，严禁作为实训工程分发)**。
* **Scan the World 开放非金属雕塑/文物**：
  * *现状*：主要分布于 MyMiniFactory 与 Wikimedia，绝大多数仅提供未展 UV 的 3D 打印用原始 `.stl` 三角面体，完全不具备纹理映射条件。
  * *判定*：**`REJECT` (缺失 UV 与纹理系统，改造成本巨大)**。

---

## 4. 全候选资产综合比对决策矩阵

| 目标角色 | 资产名称 | 第一方来源与作者 | 授权协议 | 几何面数 / UV 质量 | 格式支持 | 物理分层与材质特性 | 教师预处理 | 最终决策 |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- | :---: | :---: |
| **角色 1: 主工业资产** | **Vintage Flashlight** | **Poly Haven**<br>(Omar M. El-Safy) | **CC0 1.0** | **~11K tris**<br>高质量单套无重叠 | `.blend`<br>glTF, FBX | **裸露金属+油漆外壳+塑料手柄+镀铬反光罩+玻璃透镜**，分层极其完美 | **< 1 小时**<br>(打包 Starter/Ref) | **`ADOPT`<br>(主选推荐)** |
| 角色 1: 主工业资产 | Retro Multimeter | Poly Haven<br>(Elli Moeller) | CC0 1.0 | ~20K tris<br>高质量无重叠 | `.blend`<br>glTF, FBX | 胶木机壳+红黑橡胶导线+透明玻璃表盘+镀铬表针+旋钮 | ~1.5 小时 | `ADOPT_WITH_PREP`<br>(次选备用) |
| 角色 1: 主工业资产 | Signal Flashlight | Poly Haven<br>(Jiří Ptáček) | CC0 1.0 | ~12K tris<br>标准无重叠 | `.blend`<br>glTF, FBX | 军绿漆面+黄铜滑块+皮革吊带+透镜 | ~1 小时 | `ADOPT_WITH_PREP`<br>(可用备选) |
| 角色 1: 主工业资产 | Camera 01 | Poly Haven<br>(R. J. Macatangay) | CC0 1.0 | ~27K tris<br>3 套材质分块 | `.blend`<br>glTF, FBX | 荔枝纹蒙皮+阳极氧化金属件+多层镀膜镜头+皮背带 | ~2 小时 | `ADOPT_WITH_PREP`<br>(进阶/拆解) |
| 角色 1: 主工业资产 | AntiqueCamera | Khronos glTF<br>(M. Kamps / UX3D) | CC0 1.0 | ~30K tris<br>标准导出 | glTF, GLB | 木质脚架+黄铜构件+皮革折页；无原生 `.blend` 工程 | ~3 小时 | `REFERENCE_ONLY`<br>(交付对照) |
| 角色 1: 主工业资产 | FlightHelmet | Khronos glTF<br>(Microsoft 捐赠) | CC0 1.0 | 中等实时面数<br>5 套贴图集 | glTF, GLB | 皮革帽+橡胶管+金属扣+有机玻璃；多贴图集结构繁琐 | ~3 小时 | `REFERENCE_ONLY`<br>(行业标杆) |
| 角色 1: 主工业资产 | SciFiHelmet | Khronos glTF<br>(M. Pavlovich) | CC-BY 4.0 | 约 15K tris<br>单套 PBR 贴图 | glTF, GLB | 科幻喷漆+护目镜+橡胶垫密封；题材缺乏物理直观 | ~1.5 小时 | `ADOPT_WITH_PREP`<br>(科幻备选) |
| 角色 1: 主工业资产 | DamagedHelmet | Khronos glTF<br>(theblueturtle_) | **CC BY-NC 4.0** | 经典实时面数 | glTF, GLB | 经典战损头盔；**因含有 NonCommercial 限制被一票否决** | N/A | **`REJECT`<br>(协议风险排除)** |
| 角色 1: 主工业资产 | Smithsonian 工业设备 | Smithsonian 3D 馆藏 | CC0 1.0 | 100K–500K<br>无拓扑扫描 | OBJ, glTF | 摄影测量贴图（带死阴影），无分层 Rough/Metal 贴图 | > 20 小时 | `REJECT`<br>(非 PBR 原始扫描) |
| **角色 3: W6 迁移载体** | **Antique Ceramic Vase 01** | **Poly Haven**<br>(James Ray Cock) | **CC0 1.0** | **~9K tris**<br>单套无重叠 UV | `.blend`<br>glTF, FBX | **高光玻璃质釉面+开片法线微裂纹+青花釉下彩+底部粗陶露胎** | **< 45 分钟**<br>(配置 Starter) | **`ADOPT`<br>(主选推荐)** |
| 角色 3: W6 迁移载体 | Wooden Bowl 01 | Poly Haven<br>(Oliver Harries) | CC0 1.0 | ~14K tris<br>单套无重叠 | `.blend`<br>glTF, FBX | 手作原木刀痕+年轮各向异性+吸水孔隙微磨损 | ~1 小时 | `ADOPT_WITH_PREP`<br>(木质平行备选) |
| 角色 3: W6 迁移载体 | Ceramic Vase 04 | Poly Haven<br>(James Ray Cock) | CC0 1.0 | ~2K tris<br>轻量化单套 | `.blend`<br>glTF, FBX | 彩绘红陶罐+素烧胎底；面数极简 | ~30 分钟 | `ADOPT_WITH_PREP`<br>(轻量备选) |
| 角色 3: W6 迁移载体 | Smithsonian 陶器扫描 | Smithsonian 3D 馆藏 | CC0 1.0 | 50K–300K<br>未拓扑多边形 | OBJ, glTF | 照片级光影烘死，无材质通道分层 | > 15 小时 | `REFERENCE_ONLY`<br>(视觉参考) |
| 角色 3: W6 迁移载体 | Scan the World 扫描件 | Scan the World 社区 | 协议多样 | 仅 STL 纯模型 | STL | 无 UV、无贴图、仅适合 3D 打印 | > 20 小时 | `REJECT`<br>(严重缺失 UV) |

---

## 5. 教学套件集成与教师备课实操流水线

本轮定向采购完成后，所有 7 大角色资产全部落实且权属清晰。教师备课工作聚焦于标准工程构建，避免学生陷入复杂的贴图路径修复或技术环境配置错误中。

### 5.1 Starter 与 Reference 工程分离策略

对于采纳的外部资产（Vintage Flashlight 与 Antique Ceramic Vase 01），教师应遵循以下生产工序构建课程分发包：

1. **构建主工业练习套件 (`Flashlight_Package`)**：
   * **`W1_W5_Flashlight_Starter.blend`**：
     * 导入官方优化几何体，清除所有已连接的材质贴图；
     * 保留网格的材质插槽分配（例如 `mat_flashlight_body` 与 `mat_lens`）；
     * 挂载纯净的 `Principled BSDF` 初始默认值；
     * 将官方烘焙的 Ambient Occlusion 与 Curvature（曲率）贴图作为学生绘制或节点混合的基础辅助数据打包进 `.blend`。
   * **`W1_W5_Flashlight_Reference.blend`**：
     * 完整封装官方 2K 质感贴图网络（采用 Blender 原生相对路径 `//textures/` 打包）；
     * 设置标准转台动画（Turntable，72 帧一圈）与中性 HDRI 摄影棚布光，供学生作为质感标杆对照查看。
2. **构建 W6 迁移实训套件 (`W6_Ceramic_Package`)**：
   * **`W6_Ceramic_Starter.blend`**：
     * 保留花瓶几何体与 UV；
     * 节点树中预置两组基础参数：一组模拟表层透明高光釉质，一组模拟底部哑光陶胎；
     * 提供开片微裂纹法线贴图，要求学生运用 `Map Range`、`Mix Color` 或遮罩节点，自主实现由底至上的非金属双层材质表现。
   * **`W6_Ceramic_Reference.blend`**：
     * 完整的青花开片成品工程，用于作业评估标准展示。

---

### 5.2 W1–W9 课程教学主线资产落位图

通过本次 Pass C 采购成果的注资，高校 9 周课程体系中的实训教具全景闭环如下：

```
[W1 物理感知与观察]
  └─ 依托 Bundle 3 (中性摄影棚 HDRI) + Vintage Flashlight (初识漆面电介质与金属反光差异)
[W2 核心物理参数因果]
  ├─ 理论表征微实验：Bundle 1 (教师石膏胸像高低模对，完成 45 分钟切线法线烘焙实操)
  ├─ 排错对比：Bundle 2 (切线法线 Raw vs sRGB 撕裂对照球体)
  └─ 参数实验：Vintage Flashlight (单通道隔离调控：体验 Metallic 0/1 与 Roughness 变化)
[W3 微表面与几何表征]
  └─ Vintage Flashlight (微观法线细节与倒角观察)
[W4–W5 程序化纹理与分层着色]
  ├─ 基础算法：角色 5 本地自研节点微示范 (Noise/Voronoi/Map Range 快速生成磨损遮罩)
  └─ 工业实战：Vintage Flashlight (实现底漆剥落、手柄防滑微表面与反光碗反射)
[W6 近迁移能力测验 (Near-Transfer Challenge)]
  └─ 角色 3 外部采购：Antique Ceramic Vase 01 (完全脱离金属，考核青花开片釉与粗陶底胎表现)
[W7 实时交付与引擎适配]
  ├─ 实时规则验证：Bundle 4 (实时地砖 GLTF/GLB，掌握 ORM/Rough-Metal 打包规则)
  └─ 资产导出：将前述自制完成的 Vintage Flashlight 导出为标准化 glTF/GLB 并入库
[W8–W9 LookDev 评测与综合呈现]
  ├─ 标定环境：Bundle 3 摄影棚 + 多室外环境 HDRI 压力测试
  └─ 最终结课呈现：Vintage Flashlight (主作品) + Antique Ceramic Vase 01 (迁移作品)
```

---
*报告归档日期：2026-09-20 | 采购执行状态：Pass C 调研完成，建议正式采纳推荐方案。*
