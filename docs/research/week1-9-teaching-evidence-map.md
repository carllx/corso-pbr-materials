# W1–W9 Teaching Evidence Map & Research Gap Register (全课教学证据地图与研究缺口台账)

> **治理定位**：本文件是《三维数字材质制作》W1–W9 课程设计的**薄路由与关联层 (Thin Routing & Join Layer)**。它向上连接不可变源素材（教材、规范、视频教程与已部署知识库），向下为周次排课（v0.4 草案）、可执行教学包与期末大作业架构（Issue #22）提供实证路由支撑，防止智能体脱离源素材凭空脑补、私自冻结周历或将教学推论与文献事实混淆。  
> **所属任务**：GitHub Issue #28 (Governance — W1–W9 Teaching Evidence Map & Research Gap Register)  
> **状态**：`POINTER-INTEGRITY PASS COMPLETE — EXISTING EVIDENCE ONLY — PENDING BROWSER REVIEW`  
> **基线分支约束**：严格基于 `origin/main` (`ecb50e9`)，继承已合并的 Issue #19 (PR #26) 与 Issue #20 (PR #23) 成果。  
> **课程状态纪律**：
> - **W1**：已验收锁定之可执行教学基线 (`TEACHER ACCEPTED WITH DELTAS`)，学生端内容严格遵循 `week1-executable-teaching-package-v0.1.md`；
> - **W1–W6**：课程负责人正式采纳的“有限主案例 + 有界代表性微案例模型”（`TEACHER ACCEPTED — BOUNDED HYBRID`），具体排课周次与分钟数**尚未冻结 (NOT YET FROZEN)**；
> - **Normal Bake / 高低模石膏对**：活跃教学候选 (`Active Teaching Candidate`)，其实操组织形式保持未决 (`UNRESOLVED / CONDITIONAL`)；
> - **W7–W9**：全新独立综合期末大作业 (`New Comprehensive Final Project`)，其具体架构、任务书与交付规范权威归属于 **Issue #22**，当前条目均为输入性候选；
> - **排课草案 v0.4**：**尚未生成 (NOT YET GENERATED)**，严禁在本工单中提前排定。

---

## 1. 证据消费与正交分类说明 (Evidence Consumption Typology)

依据 `AGENTS.md` 与 `docs/methods/source-material-governance.md`，承重课程主张遵循以下非互斥的正交维度分类：

- **依据来源与溯源维度 (Grounding / Provenance)**：
  - **`DIRECT SOURCE FACT`**：教材、官方规范或学术专著中明确给出的原理、公式、通道定义或物理法则；
  - **`COURSE PRECEDENT`**：权威商业课程（如 CORE42）或专业教程（如 Shah 2022）中采用的教学范式、道具组织或实操片段；
  - **`PROJECT INFERENCE`**：基于单师 35/17 人大班教学容量、机房条件与认知规律做出的项目教学法剪裁与结构综合。
- **覆盖状态维度 (Coverage Status)**：
  - **`STRONG`**：现有语料具备直接详尽的一手文献、课时视频或官方规范支持；
  - **`PARTIAL`**：现有语料具备宏观原则或邻近案例支持，但缺乏针对本项目受控大班教学的具象实操设计；
  - **`MISSING`**：现有语料库未包含有效支撑证据（标记为 `NOT FOUND IN CURRENT CORPUS`）；
  - **`RUNTIME REQUIRED`**：理论依据充分，但真实软件操作（如 Blender 交互路径）、资产拓扑或机房环境可行性必须经受控探针闭环。
- **项目决策与教学定性 (Project Disposition & Teaching Status)**：
  - 由当前 Project Authority 决定（如 `TEACHER ACCEPTED` / `candidate` / `optional` / `unresolved`）。负责人采纳的项目决策属于 Project Authority，**严禁伪装为外部文献来源事实**。

---

## 2. 宏观阶段与周次候选总览 (Macro Stages & Week Candidates Overview)

```
┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│ Stage 1: W1 已验收教学实施基线 (Accepted Executable Baseline, 已由 Course Owner 验收锁定)      │
│ • Week 1: 观察解构、材质属性与光影剥离、外壳涂装变体调节、Material Preview 视口与数据持久化验证 │
├──────────────────────────────────────────────────────────────────────────────────────────────┤
│ Stage 2: W2–W6 教学演练与核心能力构建 (Teaching / Practice Capability Construction, 候选周次)   │
│ • W1–W6 拓扑已锁定为有界混合模型 (Vintage Flashlight 主干 + Classical Bust 微案例 + Vase 近迁移) │
│ • Candidate W2: 节点网络拓扑与纯电介质/抛光金属构建 (Node Shading & Pure Material Foundations)  │
│ • Candidate W3: 表面几何细节扰动与凹凸/法线映射 (Normal & Bump Representation: Texture vs Mesh) │
│ • Candidate W4: 空间特征提取与程序化分层遮罩 (Procedural Texturing & Mask Generation)           │
│ • Candidate W5: UV 坐标解析、图像贴图与视口局部绘制 (UV Texture Coordinates, Image & Painting)   │
│ • Candidate W6: 复杂介电质（清漆/透射）与跨载体近迁移评测 (Complex Dielectrics & Near-Transfer) │
├──────────────────────────────────────────────────────────────────────────────────────────────┤
│ Stage 3: W7–W9 全新独立综合期末大作业 (New Comprehensive Final Project, 严格归属 Issue #22 权威)│
│ • 彻底解耦原则：W7–W9 开启全新资产，严禁机械续用手电筒；共 12 课节 / 480 分钟 / 8 接触学时     │
│ • Candidate W7: 期末独立资产解构、材质规划与底座通道搭建 (Final Asset Brief & Baseline Shading) │
│ • Candidate W8: 复杂质感纵深推进、大班流动辅导与形成性讲评 (Advanced Detailing & Studio Review) │
│ • Candidate W9: 跨光照环境 LookDev 校验与实时/离线双通道交付 (LookDev Verification & Dual Exit)  │
└──────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. W1–W9 教学证据路由地图 (Teaching Evidence Map)

### 3.1 Stage 1: Week 1 教学实施包（已验收基线，严格对齐可执行教学包）

| 知识单元 ID 与名称 | 学生端学习目标与教学用途 | 主要一手证据指针 (Primary Evidence Pointer) | 实践演示参考 (Practice / Demo) | 教师精读/观看指针 (Teacher Read / Watch) | 证据类型 | 覆盖状态 | 已知局限与客观边界 | 当前定性 | 下一步建议研究关键词与领域 |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :--- | :---: | :--- |
| **KU-W01-1**<br>课程全景导入与材质认知<br>(Orientation & Perception) | 建立 9 周能力发展预期与认知，区分物理固有属性与环境光影/附着脏污；破除“调参数靠猜、反光即金属”等初学者误区 | • Dinur (2026) Ch 1 (pp. 9–21)<br>• Week 1 package Block 1 (Orientation 15min) & Block 2 (15min) | 手电筒实物参考图剖析（区分 5 项视觉现象的物理因果归属） | Dinur (2026) Ch 1; Week 1 Executable Package v0.1 §1.2 LO1 | `DIRECT SOURCE FACT` + `PROJECT INFERENCE` | **`STRONG`** | 15 分钟导学严格遵循占位段规范，不预设未经验证的考核比例与微观物理细节 | `required` | 3D material course orientation, cognitive scaffolding |
| **KU-W01-2**<br>材质属性与光影解构基石<br>(Property vs Lighting Decomposition) | 建立“材质固有属性 vs 外部光影”因果观念，识别高光光斑与表面阴影为外部环境光照结果，不得作为 Base Color 固有属性（剥离假高光与假阴影） | • Dinur (2026) Ch 5 (pp. 57–68)<br>• Week 1 package Block 2 (Observation & Decomposition) | 手电筒曲面高光光斑（外部光源反射）与 Base Color 固有属性剥离演示 | The PBR Guide (2018) Part 1 (教师背景与 W2 路由：Energy Conservation p. 30, 微表面 pp. 24–27, 菲涅尔 pp. 30–32, 导体/绝缘体 pp. 33–37 不下放 W1 学生端); Dinur (2026) Ch 5 | `DIRECT SOURCE FACT` | **`STRONG`** | W1 学生端以光影解构（SEE vs IS）为度，严禁下放微观能量守恒公式或微表面 GGX 参数；原理性推导留待后续周次 | `required` | PBR light decomposition, intrinsic material vs illumination |
| **KU-W01-3**<br>预置外壳涂装变体调节<br>(Scaffolded Base Color Tint) | 在预置节点中检视并调节外壳固有色（Base Color Tint），完成“检视 $\to$ 调节 $\to$ 反馈 $\to$ 修订”闭环，验证受保护区零污染 | • Week 1 package Block 5 & 6 (Option B Scaffolded Shader Editor)<br>• The PBR Guide (2018) Part 2 (Base Color albedo, pp. 50–52) | Slot 2 (`vintage_flashlight_body`) 中检视 `Body_Color_Tint`，调节 Factor 与 Color B 实施外壳变体 | Week 1 Package v0.1 §2.2 (教师背景与 W2/W5 路由：线性空间 Part 1 pp. 38–39, 通道组装 CORE42 `texturing-c04-l16` Connecting PBR Image Textures) | `DIRECT SOURCE FACT` + `PROJECT INFERENCE` | **`STRONG`** | 坚决执行 Option B 支架策略：W1 学生严禁从零新建节点连线（B = DEFER, NOT OMIT）；严密色彩空间打包留待后续 | `required` | scaffolded shader editor, inspect adjust feedback revise |
| **KU-W01-4**<br>视口环境与数据持久化验证<br>(Material Preview & Persistence) | 掌握 Material Preview 材质预览模式下的中性环境光自检，在课内完成“保存工程 $\to$ 完全退出 Blender 进程 $\to$ 重新打开”数据持久化验证 | • Week 1 package Block 8 (§1.2 LO3, §2.3)<br>• Dinur (2026) Ch 11 (pp. 113–130)<br>• Blender 5.2 Manual: Viewport Shading | Starter 资产在固定机位 (`Cam_Obs`) 与 Material Preview 下观察，完全退出进程重开验证持久化 | Week 1 Package v0.1 §2.3; Dinur (2026) Ch 11 | `COURSE PRECEDENT` + `PROJECT INFERENCE` | **`STRONG`** | Material Preview 内置环境作为中性观察基准，不等同于多环境 LookDev 演播室渲染评测 | `required` | Viewport Shading Material Preview, Blender process persistence |

---

### 3.2 Stage 2: Week 2–Week 6 教学演练与能力构建（候选周次，周历未冻结）

| 知识单元 ID 与名称 | 学生端学习目标与教学用途 | 主要一手证据指针 (Primary Evidence Pointer) | 实践演示参考 (Practice / Demo) | 教师精读/观看指针 (Teacher Read / Watch) | 证据类型 | 覆盖状态 | 已知局限与客观边界 | 当前定性 | 下一步建议研究关键词与领域 |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :--- | :---: | :--- |
| **KU-W02-1**<br>着色节点网络基础拓扑<br>(Shader Node Graph Logic) | 掌握着色器编辑器基础数据流（Float/Vector/Color 连线规则与 ColorRamp/Math） | • CORE42: `materials-shading-c01-l01~l06` (Shader Editor 基础；注：课时范围在当前清单属 NOT FULLY ANCHORED IN REVIEWED MANIFEST，以 Blender 5.2 Manual 为标准基准)<br>• Blender 5.2 Manual: Nodes Overview | 单一平面/立方体节点连接快速实验 | CORE42 `materials-shading-c01-l03/l04`; Blender 5.2 Manual: Nodes Overview | `COURSE PRECEDENT` | **`PARTIAL`** | 纯连线逻辑对无编程基础学生有认知门槛，缺乏针对大班防呆脚手架 | `required` | shader nodes beginner scaffolding, visual dataflow |
| **KU-W02-2**<br>纯电介质与镜面金属构建<br>(Dielectric M1 & Metal M3) | 掌握 Base Color、Metallic（0/1 二分法）与 Roughness 基础配合，攻坚 M1 塑料与 M3 抛光金属 | • The PBR Guide (2018) Part 1 (Conductors & Insulators, pp. 33–37)<br>• CORE42: `materials-shading-c02-l13` (The Principled BSDF: Thin Film, Coat, Metalness)<br>• Shah (2022) Ch 3 (pp. 63–102) | Vintage Flashlight 筒身与反射反光杯基础着色槽分配 | PBR Guide Part 1 pp. 33–37; Shah Ch 3; CORE42 `materials-shading-c02-l13` | `DIRECT SOURCE FACT` + `COURSE PRECEDENT` | **`STRONG`** | 仅覆盖均匀表面，尚未引入破损与细节 | `required` | metalness workflow, dielectric vs conductor |
| **KU-W02-3**<br>粗糙度与微表面粗糙金属<br>(Roughness & Conductor M4) | 掌握微表面粗糙度对高光展宽与反射模糊的影响，制作工业车削磨砂金属 M4 | • OpenPBR v1.1.1 §3.2 Specular Roughness<br>• The PBR Guide (2018) Part 2 (Roughness, pp. 60–61; Metal/Roughness, pp. 47–61)<br>• CORE42: `texturing-c04-l18` (PBR Energy Conservation, F0 0.04, Fresnel) | Vintage Flashlight 外壳滚花与工业车削金属调试 | OpenPBR Spec §3.2; PBR Guide Part 2 pp. 60–61; CORE42 `texturing-c04-l18` | `DIRECT SOURCE FACT` | **`STRONG`** | 宏观各向异性仅作概念提及，不作为大班考核主体 | `required` | roughness mapping, microfacet specular spread |
| **KU-W03-1**<br>凹凸、法线与网格置换对比<br>(Bump vs Normal vs Displacement) | 深刻理解法线贴图仅扰动着色法线（掠射角剪影不变）与真实置换（改变顶点）的物理差异 | • Dinur (2026) Ch 13 (pp. 143–156)<br>• The PBR Guide (2018) Part 2 (Height/Normal, pp. 78–79)<br>• CORE42: `texturing-c02-l06` (Bump and Normal Maps) & `texturing-c02-l07` (Displacement Maps)<br>• OpenPBR v1.1.1 §10 | 边缘球体/平面剪影凹凸测试 | Dinur (2026) Ch 13; PBR Guide Part 2 pp. 78–79; CORE42 `texturing-c02-l06/l07` | `DIRECT SOURCE FACT` | **`STRONG`** | 置换网格细分对机房硬件显存有压力，课内以法线扰动为主 | `required` | normal map vs bump vs displacement, shading normals |
| **KU-W03-2**<br>高低模法线微案例探索<br>(High-to-Low Normal Representation) | 探索高模细节（雕刻/倒角）映射到低模法线贴图的几何表现，作为活跃教学候选探索 | • Shah (2022) Ch 2 (pp. 35–62, baking fundamentals)<br>• CORE42: `texturing-c03-l11` (UV Packing & Normal Baking Limitations)<br>• Classical Bust 资产事实对 | Classical Bust 浮雕法线微案例展示（演示 vs 引导微实验待定） | Shah (2022) Ch 2; CORE42 `texturing-c03-l11` | `COURSE PRECEDENT` + `PROJECT INFERENCE` | **`PARTIAL`** | 35 人大班从零卡模烘焙极易大面积报错卡死，实操形态与时间待排课确定 | `candidate` | classroom normal baking friction, bust micro-lab |
| **KU-W04-1**<br>程序化数学纹理与噪波控制<br>(Procedural Noise & Texturing) | 掌握 Noise (4D), Voronoi 与 Wave 节点的尺度、细节与粗糙度参数控制，打破 CG 机械均匀感 | • CORE42: `texturing-c05-l20` (Intro to Procedural Texturing: Noise 4D, Voronoi, Wave)<br>• Blender 5.2 Manual: Noise Texture Node | 节点视口直连查看灰度场分布，调试污迹噪波 | CORE42 `texturing-c05-l20` | `COURSE PRECEDENT` | **`STRONG`** | 缺乏具象边缘控制力，复杂网格上易出现三维投影拉伸 | `required` | procedural noise textures, Voronoi scale mapping |
| **KU-W04-2**<br>空间特征提取与环境光遮蔽遮罩<br>(Ambient Occlusion & Spatial Grime Mask) | 掌握利用 Ambient Occlusion（凹缝环境光遮蔽）与空间位置特征（Z 轴落灰/Separate XYZ）提取模型空间特征，构建自动化积灰遮罩 | • The PBR Guide (2018) Part 2 (Ambient Occlusion, pp. 74–77)<br>• CORE42: `texturing-c05-l21` (Procedural Dirt & Grime: Ambient Occlusion and Object Position Texturing)<br>• Blender 5.2 Manual: Ambient Occlusion Node | Vintage Flashlight 螺纹凹缝积灰与顶面 Z 轴落灰遮罩调试 | PBR Guide Part 2 pp. 74–77 (AO 原理与阴影解耦); CORE42 `texturing-c05-l21` (AO 与物体空间 Z 轴落灰节点组装) | `DIRECT SOURCE FACT` + `COURSE PRECEDENT` | **`STRONG`** | 纯程序化 AO 需网格流形良好，非封闭模型易产生黑斑；现有语料明确支持 AO 与 Z 轴位置遮罩，未包含经核实的着色器曲率提取节点（几何曲率提取不作一手断言） | `required` | ambient occlusion node, procedural grime mask, spatial position texturing |
| **KU-W04-3**<br>复合涂层与磨损物理分层<br>(Layered Shading & Weathering M5) | 理解“基底材质 $\to$ 底漆/表面漆 $\to$ 磨损污渍”的物理因果分层网络（M5 复合漆面） | • Dinur (2026) Ch 13 (Combining Workflows: Procedural & Image Textures, pp. 143–156)<br>• CORE42: `texturing-c07-l32` (Procedural Edge Wear & Leather Finishing on Binoculars)<br>• Shah (2022) Ch 4 (pp. 103–116) | Vintage Flashlight 掉漆露铜与复合涂层混合着色器组装 | Dinur (2026) Ch 13 pp. 143–156 (程序化与图像贴图组合工作流); Shah Ch 4; CORE42 `texturing-c07-l32` (望远镜边缘磨损与做旧先例) | `COURSE PRECEDENT` + `PROJECT INFERENCE` | **`STRONG`** | 手电筒网格对 M6/M7 承载性仍属条件性候选 (`GATE-ASSET-01`)；Dinur Ch 13 支持程序化与图像混合工作流，具象掉漆剥落分层主要由商业先例 (CORE42 / Shah) 与项目推论支持 | `required` | layered PBR materials, paint chipping cause-and-effect |
| **KU-W05-1**<br>UV 展开规范与 Texel 密度<br>(UV Coordinates & Texel Density) | 理解 UV 展开接缝标记原则、拉伸率控制与 Texel Density（像素密度一致性） | • Shah (2022) Ch 1 (Texel Density, pp. 3–6)<br>• CORE42: `texturing-c03-l10~l13` (Hammer UV Unwrapping, Seams & Texel Density)<br>• Blender 5.2 Manual: UV Unwrapping | 简单道具缝合线标记与棋盘格检查贴图拉伸排查 | CORE42 `texturing-c03-l10~l13` (缝合线切分与展开实操); Shah (2022) Ch 1 pp. 3–6 (Texel Density 原理；注：Shah 全书使用预展模型，不讲授 UV 切缝展开，Ch 2 为 Painter 资产面板操作); Blender 5.2 Manual: UV Unwrapping | `DIRECT SOURCE FACT` + `COURSE PRECEDENT` | **`STRONG`** | 本课以材质为主，UV 深度以读懂接缝与修整为限，不扩张为复杂拓扑课；明确 Shah (2022) 不讲授展开，展 UV 依赖 CORE42 铁锤实操与 Blender 手册 | `required` | UV seams marking, texel density consistency |
| **KU-W05-2**<br>图像贴图通道封装接入<br>(Image Texture Channel Setup) | 掌握外置贴图（Base Color, Roughness, Normal, Metallic）在节点树的规范接入与色彩空间匹配 | • The PBR Guide (2018) Part 1 (Linear Space, pp. 38–39) & Part 2 (pp. 47–61)<br>• CORE42: `texturing-c04-l16` (Connecting PBR Image Textures) & `texturing-c04-l19` (Principled Shader Shading Binoculars)<br>• Shah (2022) Ch 3 (pp. 63–102) | Vintage Flashlight 外部贴图集批量接入与通道混合 | PBR Guide Part 1 pp. 38–39; CORE42 `texturing-c04-l19` | `DIRECT SOURCE FACT` | **`STRONG`** | 贴图丢失重连与相对路径管理是机房高发排错痛点 | `required` | image texture node setup, channel packing routing |
| **KU-W05-3**<br>视口局部绘制与无损修饰<br>(Viewport Texture Paint & Revise) | 在 Blender 视口中利用画笔与遮罩进行空间局部修复与个性化手绘污迹，达成 LO3 | • CORE42: `texturing-c06-l25~l27` (Texture Painting in Blender; 注：视口手绘课时范围在当前清单属 NOT FULLY ANCHORED IN REVIEWED MANIFEST，以 Blender 5.2 Manual Texture Paint 为实测基准)<br>• Blender 5.2 Manual: Texture Paint<br>• Gate 3B probe 2026-09-17 | 手电筒特定表面局部编号绘制与污垢无损叠加测试 | CORE42 `texturing-c06-l25~l27`; Gate 3B report; Blender 5.2 Manual: Texture Paint | `COURSE PRECEDENT` | **`RUNTIME REQUIRED`** | Blender 贴图绘制未保存图像缓存直接退出会丢失数据；受 `[PENDING GATE 01]` 约束 | `required` | Blender texture paint dirty buffer, LO3 spatial locality |
| **KU-W06-1**<br>双层高光与清漆涂层机制<br>(Clearcoat / Dual-Specular M2) | 掌握电介质表面透明光亮涂层（Clearcoat）的次级高光反射机制与粗糙度解耦 | • OpenPBR v1.1.1 §5 Coat Layer<br>• Dinur (2026) Ch 9 & 12 (pp. 92–96, 131–142)<br>• CORE42: `materials-shading-c02-l13` (The Principled BSDF: Coat Layer) | 粗糙哑光基底上覆盖高光清漆/光滑施釉反射实验 | OpenPBR Spec §5; Dinur (2026) Ch 9 & 12; CORE42 `materials-shading-c02-l13` | `DIRECT SOURCE FACT` | **`STRONG`** | 清漆与底层粗糙度关系若未理清易产生假反光感 | `required` | clearcoat shading layer, dual-specular PBR |
| **KU-W06-2**<br>跨载体近迁移三分类因果评测<br>(Near-Transfer 3-Way Causal Audit) | 在陌生模型载体（Antique Ceramic Vase 01）上辨识规律：直接适用/经调整后适用/不适用误导；完成有界课内近迁移测试（课时预算待定） | • Dinur (2026) Ch 9 & 12 (pp. 92–142)<br>• `case-topology-join.md` §3.3<br>• Vase 01 资产事实 | 花瓶免配置工程导入，学生独立完成陶瓷光滑施釉参数迁移与评价 | `case-topology-join.md` §3.3; Dinur Ch 9 | `PROJECT INFERENCE` | **`PARTIAL`** | 物理材质理论依据充足，但跨载体近迁移评测设计在现有语料中属于项目推论（`PROJECT INFERENCE / PARTIAL`），且花瓶零摩擦模板依赖 `[GATE-ASSET-02]` 验证 | `candidate` | near-transfer assessment rubric, ceramic glaze template |
| **KU-W06-3**<br>平时阶段工件归档与自检闭环<br>(Practice Evidence Bundle Archival) | 完成 W1–W6 练习工件归档（手电筒主干 + 花瓶判定表），完成阶段形成性证据自检，轻装进入期末 | • `case-topology-join.md` §4.1<br>• `course-design-ledger.md` §2.4<br>• Week 1–9 conditional draft v0.2 §4 | 学生提交工程目录自查 Checklist，教师异步抽检 | `case-topology-join.md` §4.1; `course-design-ledger.md` §2.4 | `PROJECT INFERENCE` | **`STRONG`** | 归档即闭环，严禁将未完手电筒包袱拖入 W7 | `required` | formative portfolio archival, checklist verification |

---

### 3.3 Stage 3: Week 7–Week 9 全新独立综合期末大作业（候选周次，Issue #22 权威，非冻结交付）

| 知识单元 ID 与名称 | 学生端学习目标与教学用途 | 主要一手证据指针 (Primary Evidence Pointer) | 实践演示参考 (Practice / Demo) | 教师精读/观看指针 (Teacher Read / Watch) | 证据类型 | 覆盖状态 | 已知局限与客观边界 | 当前定性 | 下一步建议研究关键词与领域 |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :--- | :---: | :--- |
| **KU-W07-1**<br>期末独立资产解构与材质规划<br>(Final Asset Brief Decomposition) | 面向全新独立资产任务书（候选形式待 Issue #22 裁定），独立拆解材质需求、收集参考图并制定分层规划蓝图 | • Shah (2022) Ch 6 (pp. 153–203)<br>• Dinur (2026) Ch 1 & 13 (pp. 9–156)<br>• Issue #22 planning scope | 教师发布期末任务包（严禁 Flashlight），学生绘制材质分层思维导图 | Shah Ch 6 pp. 153–160; Dinur Ch 13 | `COURSE PRECEDENT` + `PROJECT INFERENCE` | **`PARTIAL`** | 具体资产供给模式（统一下发 vs 有界三选一）与考核规范由 Issue #22 独立裁决 | `unresolved` | authentic capstone assessment 3D, material moodboard |
| **KU-W07-2**<br>新资产基础通道组装与 UV 校验<br>(New Mesh Shading Pipeline Setup) | 学生将候选新资产导入 Blender，核验网格流形与 UV 象限，搭建标准化 Principled BSDF 基础槽（候选流程待 #22 确定） | • CORE42: `texturing-c07-l28` (Binoculars UV & Base Materials Setup)<br>• Blender 5.2 Manual: Material Slots | 学生独立完成新资产基础着色槽分配与环境自检 | CORE42 `texturing-c07-l28` | `COURSE PRECEDENT` | **`STRONG`** | 资产由校方/教师预置，严禁现场要求学生从零拓扑建模 | `candidate` | multi-material slot setup, new asset pipeline verification |
| **KU-W08-1**<br>具象细节与老化磨损综合深化<br>(Advanced Weathering Integration) | 综合运用程序化噪波、环境光遮蔽边缘磨损与视口手绘遮罩，独立在新资产上完成高级质感表现（候选实操） | • Shah (2022) Ch 6 (pp. 153–203)<br>• CORE42: `texturing-c07-l29~l32` (Advanced Detailing & Finishing on Binoculars)<br>• Dinur (2026) Ch 13 | 新资产磨损、划痕、积灰与光泽渐变综合制作实操 | Shah Ch 6; CORE42 `texturing-c07-l32` | `COURSE PRECEDENT` | **`STRONG`** | 需严格控制学生复杂度发散，避免陷入无休止调噪波陷阱 | `candidate` | advanced weathering layering, hard surface texturing |
| **KU-W08-2**<br>大班工作室流动辅导与形成性讲评<br>(Large-Class Studio Review) | 开展课堂阶段性进度互查与教师共性投屏讲评，依据 Checklist 诊断物理违规并现场修正（候选组织机制） | • `course-offering-impact-analysis-2026-2027-1.md`<br>• Issue #5 教师反馈漏斗机制 | 教师大屏幕共性问题纠偏示范；四级反馈漏斗运作 | course-offering-impact-analysis §3; Issue #5 | `PROJECT INFERENCE` | **`PARTIAL`** | 35 人单师辅导带宽极紧，无法做 35 人课内逐一评审，依赖结构化检查点 | `candidate` | studio critique 35 students, formative defect triage |
| **KU-W09-1**<br>多 HDRI 演播室 LookDev 校验<br>(Cross-Environment Studio LookDev) | 在预置 HDRI 下检验材质表现一致性（候选 LookDev 流程，以 Cycles/EEVEE 视口为安全基准） | • Dinur (2026) Ch 11 (pp. 113–130)<br>• CORE42: `materials-shading-c04-l18` (Cycles Light Bounces & Fast GI)<br>• PolyHaven LookDev HDRIs | 演播室三点光与 HDRI 快速切换对比观察 | Dinur (2026) Ch 11; CORE42 `materials-shading-c04-l18` | `DIRECT SOURCE FACT` + `COURSE PRECEDENT` | **`STRONG`** | 偏重 Cycles 离线预置演播室，外部 WebGL 光照一致性仍受运行时门禁约束 | `candidate` | LookDev studio turntable, multi-environment consistency |
| **KU-W09-2**<br>离线渲染与实时导出双通道交付<br>(Dual Export Delivery & Archival) | 完成离线演播室 LookDev 静帧渲染，并根据运行时门禁状态执行 glTF 2.0 导出（候选双通道交付） | • Issue #21 / PR #25 (glTF PBR export)<br>• Blender 5.2 glTF 2.0 Manual<br>• Week 1–9 conditional draft v0.2 §6 | glTF 导出参数配置（Packed Roughness/Metallic）与交付自查 | Issue #21 specs; Blender glTF documentation | `DIRECT SOURCE FACT` + `PROJECT INFERENCE` | **`RUNTIME REQUIRED`** | 外部 Web viewer 机房端到端门禁保持 OPEN (`GATE-RT-01`)，未通过前以 EEVEE/Cycles 为权威基准，非强制必选 | `candidate` | glTF 2.0 PBR export Blender, WebGL offline runtime |

---

## 4. 研究缺口台账 (Research Gap Register)

本台账记录在全课知识映射与技术链路梳理中识别的真实缺口。缺口严格依据性质分类，并明确标注阻断决策与闭环证据要求。

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              Research Gap Severity & Blocking Path                     │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ • Blocks Issue #22 (Final Project): GAP-W07-ASSGN                                      │
│ • Blocks v0.4 Synthesis: GAP-W02-PED, GAP-W03-BAKE, GAP-W04-PROC, GAP-W08-FEED        │
│ • Blocks Executable Package Prep: GAP-W05-GUI, GAP-W06-TRANS, GAP-ASSET-FLASHLIGHT    │
│ • Blocks Delivery Exit: GAP-W09-VIEW                                                  │
│ • Later Course Polish: GAP-AI-WORKFLOW                                                 │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 4.1 缺口明细卡片清单

#### [GAP-W02-PED] W2 节点网络初学者认知负荷与脚手架设计缺口
- **缺口分类**：`PEDAGOGY GAP`
- **重要性阐述**：从 W1 的 Option B 预置节点调节跨越到 W2 原始节点连线（Math、ColorRamp、Vector Mapping），对零编程/零节点基础的艺术设计学生存在陡峭认知悬崖。大班授课极易出现“连错接口不显色”导致的群体性求助卡顿。
- **阻断决策**：阻断 Week 2 课时切分方案与练习设计（是否必须提供预置防呆节点脚手架 / Starter Node Groups，还是从空白网格搭建）。
- **闭环所需证据**：面向三维设计初学者的着色器节点渐进教学脚手架方案，验证 3–4 步极简连线训练法（例如基于 Blender 5.2 内置 Node Wrangler 的极速通道搭接法）。
- **建议检索词与领域**：`shader nodes beginner pedagogy`, `cognitive load in visual programming for 3D art`, `Blender shader node scaffolding`.
- **阻断范围**：**Blocks v0.4 课时分配**，**Blocks Week 2 executable package**；不阻断 #22。

#### [GAP-W03-BAKE] W3 高低模法线微实验课堂组织形态缺口
- **缺口分类**：`PEDAGOGY GAP` / `RUNTIME GAP`
- **重要性阐述**：Normal Bake 已确定为活跃教学候选（`Active Teaching Candidate`），且确定不作为默认 45 分钟全员完整烘焙。但具体是采纳“教师大屏示范”、“预置包裹的受控学生微实验”、“课外可选拓展”还是“延期/移除”，在现有语料中缺乏针对 35 人单师课堂排错摩擦的实证量化支持。
- **阻断决策**：阻断 Classical Bust 资产的具体工程处理深度、W3 课内时间预算与学生实操配额。
- **闭环所需证据**：机房真实环境下的法线烘焙耗时实测、高低模光影对比与贴图投影报错率对比，或低模直读法线工程的教学响应数据。
- **建议检索词与领域**：`normal map baking classroom friction`, `high-to-low poly baking pedagogy`, `Blender cage vs ray distance beginner lab`.
- **阻断范围**：**Blocks v0.4 最终排定**，**Blocks Week 3 executable package**；不阻断 #22。

#### [GAP-W04-PROC] W4 程序化噪波节点复杂度上限与非规则曲面防拉伸配方缺口
- **缺口分类**：`PEDAGOGY GAP` / `PRACTICE REFERENCE GAP`
- **重要性阐述**：程序化噪波理论在文献（CORE42 / Blender Manual）中已非常坚实（`STRONG`），但面向初学者艺术生缺乏有界的复杂度控制标准。程序化纹理（4D Noise, Voronoi, Wave）与三维空间坐标（Generated vs Object vs UV）结合时，学生经常遇到非规则曲面上的拉伸与尺度失真，且容易堆叠过深的数学节点树导致排错失控。
- **阻断决策**：阻断 W4 程序化练习的节点深度上限规范（Max Node Depth）与标准遮罩子网络模板。
- **闭环所需证据**：面向艺术类学生的受控程序化磨损/积灰节点配方（不超过 4 个核心节点的标准模块，如 `AO + Noise $\to$ ColorRamp $\to$ Factor`）。
- **建议检索词与领域**：`bounded procedural texturing recipes`, `procedural noise scale mapping non-uniform mesh`, `Blender procedural wear student cognitive limits`.
- **阻断范围**：**Blocks v0.4 课内时间估算**，**Blocks Week 4 package**；不阻断 #22。

#### [GAP-W05-GUI] W5 Blender 视口纹理绘制界面交互摩擦与贴图未保存丢件风险验证缺口
- **缺口分类**：`RUNTIME GAP` / `PEDAGOGY GAP`
- **重要性阐述**：根据 Blender 5.2 Manual (Texture Paint Workspace)，视口绘制修改的外部贴图图像存在独立脏缓存（Dirty Buffer），需显式执行图像保存（Save All Images），`.blend` 主工程保存并不自动写回贴图文件。该交互特性在 35 人初学者机房存在操作疏漏致使手绘数据丢失的实操风险（`risk/hypothesis to verify → RUNTIME REQUIRED`）。
- **阻断决策**：阻断 LO3 空间局部性教学路径决议（即 `[PENDING GATE 01]` 判定：是否必须因 Blender 原生缺陷触发向 Substance Painter 的窄对比）。
- **闭环所需证据**：Blender 5.2 Texture Paint 丢件防范教学规范实测（通过脚本自动打包贴图或强制弹窗），或 LO3 受控探针数据。
- **建议检索词与领域**：`Blender texture paint unsaved image data loss mitigation`, `Blender dirty image buffer save prompt`, `LO3 spatial locality probe Blender 5.2`.
- **阻断范围**：**Blocks Week 5 executable package**，**Blocks `[PENDING GATE 01]` 核销**；不阻断 #22。

#### [GAP-W06-TRANS] W6 跨载体近迁移评测法与花瓶模板工程零摩擦验证缺口
- **缺口分类**：`PEDAGOGY GAP` / `ASSET GAP` / `RUNTIME GAP`
- **重要性阐述**：W6 安排花瓶近迁移测试，核心是考察学生对物理规律的三分类因果判断（直接适用 / 调整后适用 / 不适用误导）。物理材质理论依据充足，但跨载体近迁移评测设计在现有语料中属于项目推论（`PROJECT INFERENCE / PARTIAL`）。该测试要求作为有界课内近迁移练习完成（具体时间预算待排课综合确定，不冻结分钟数），必须依赖“零摩擦”的预置工程；若花瓶资产有轴心错位、材质槽未分或缺少光照，将完全阻塞测试。
- **阻断决策**：阻断 `[GATE-ASSET-02]`（Vase 01 零摩擦工程闭环核销）与 W6 教学时序切分。
- **闭环所需证据**：Antique Ceramic Vase 01 的 `.blend` 模板文件在干净环境下的加载与一键测试实证；三分类判断教学评分量表（Rubric）的设计范例。
- **建议检索词与领域**：`near-transfer assessment rubric in 3D design`, `zero-friction blend template verification`, `ceramic glaze PBR evaluation standard`.
- **阻断范围**：**Blocks Week 6 executable package**，**Blocks `[GATE-ASSET-02]`**；不阻断 #22。

#### [GAP-W07-ASSGN] W7–W9 全新期末大作业真实任务书架构与资产供给模型缺口
- **缺口分类**：`ASSESSMENT GAP` / `ASSET GAP`
- **重要性阐述**：W7–W9 已经确立为与 W1–W6 彻底解耦的全新综合期末项目，总接触学时严格锁定为 8 小时（12 课节 / 480 分钟）。然而，期末大作业的具体任务形式（统一下发单一高质量中型工业/科幻资产 vs 有界三选一主题资产包）、个人独立完成还是小组分工、评分维度权重分布等核心架构，目前完全空白。
- **阻断决策**：**直接阻断 Issue #22（期末大作业架构设计）的方案选择与终审**。
- **闭环所需证据**：行业真实标准与高校 24 实际学时相匹配的 PBR 考核任务书范式；版权干净、拓扑规范、UV 展开就绪的高保真候选用期末资产清单。
- **建议检索词与领域**：`authentic assessment rubric 3D game art capstone`, `PBR texture painting final exam briefs`, `undergraduate 3D asset supply model`.
- **阻断范围**：**DIRECT BLOCKER FOR Issue #22**；阻断 v0.4 终期排定。

#### [GAP-W08-FEED] W8 单师 35 人大班流动辅导与形成性讲评吞吐率缺口
- **缺口分类**：`PEDAGOGY GAP` / `ASSESSMENT GAP`
- **重要性阐述**：在 160 分钟面授时间内，35 人单师辅导若采用逐人面对面逐行检查，每人仅能分得 4.5 分钟，且产生严重的排队等待与课堂摸鱼。必须有高吞吐率的“共性投屏讲评 + 结构化红线自查互查 + 流动抽检”机制。
- **阻断决策**：阻断 W8 期末冲刺阶段的课堂流程规范与阶段检查点（Milestone Checkpoint）的评分权重定位。
- **闭环所需证据**：大班设计工作室教学中的群体反馈漏斗（Feedback Funnel）与轻量自查 Checklist 实践数据。
- **建议检索词与领域**：`large class studio critique strategies`, `formative assessment in 3D art classrooms`, `peer review checklist for PBR texturing`.
- **阻断范围**：**Blocks v0.4 W8 流程细化**，**Blocks Week 8 package**；不阻断 #22。

#### [GAP-W09-VIEW] W9 WebGL 实时查看器离线机房环境兼容性与交付规范缺口
- **缺口分类**：`RUNTIME GAP`
- **重要性阐述**：Issue #21 审定结论明确指出：WebGL 外部查看器由于机房网络离线与老旧显卡硬件兼容性未知，其门禁保持 OPEN (`GATE-RT-01`)，绝不可作为强制交付要求。若无法在现场验证其鲁棒性，期末大作业交付必须严格保留 Blender 原生视口渲染兜底。
- **阻断决策**：阻断期末交付物清单中是否包含 Web 端交互式 3D 文件的强制性判定。
- **闭环所需证据**：在机房典型 PC 配置上对独立 glTF 查看器（如单 HTML 离线打包版 Three.js / Model-Viewer）的离线渲染与 GPU 帧率实测报告。
- **建议检索词与领域**：`offline WebGL delivery in campus computer labs`, `glTF viewer hardware compatibility`, `Blender glTF export validation offline`.
- **阻断范围**：**Blocks `[GATE-RT-01]` 核销**，**Blocks W9 最终交付规格**；为 #22 提供约束边界。

#### [GAP-ASSET-FLASHLIGHT] Vintage Flashlight 几何对风化与积灰行为的承载性缺口 (`[GATE-ASSET-01]`)
- **缺口分类**：`ASSET GAP` / `RUNTIME GAP`
- **重要性阐述**：老式手电筒（~11K tris）作为 W1–W6 练习主干，被寄予承载 M3/M4/M5 以及条件性承载 M6 (风化锈蚀) / M7 (缝隙积灰) 的期望。但如果手电筒的 UV 分辨率不足或螺纹缝隙过于平整，将导致积灰与风化无法通过 AO 遮罩自然呈现。
- **阻断决策**：阻断手电筒在 W4/W5 承载 M6/M7 的可行性（即 `[GATE-ASSET-01]` 判定：若不理想，是否需要针对 M6/M7 引入额外微案例或修模）。
- **闭环所需证据**：在 Blender 5.2 中对手电筒原模网格曲率、烘焙 AO 贴图与着色器节点连通的直接网格检查报告。
- **建议检索词与领域**：`Vintage Flashlight asset curvature analysis`, `AO baking resolution on 11k hard-surface mesh`.
- **阻断范围**：**Blocks `[GATE-ASSET-01]`**，**Blocks Week 4/5 详细案例实施方案**；不阻断 #22。

#### [GAP-AI-WORKFLOW] 生成式 AI 在三维材质初学者教学中的融合边界与学术诚信缺口
- **缺口分类**：`THEORY GAP` / `PEDAGOGY GAP`
- **重要性阐述**：虽然 `ai-impact-on-material-workflows.md` 梳理了生成式 AI 材质工具（Text-to-PBR / Diffusion 辅助纹理），但在本科基础材质课程中，学生必须首先建立物理通道因果与底层节点控制力。AI 工具在 W1–W9 中的角色（是完全屏蔽、仅在 W1 导学演示、还是在 W7 期末脑暴时作为参考生成）尚未形成明确规范。
- **阻断决策**：阻断课程大纲中关于 AI 工具使用的政策陈述（Course AI Policy）与期末作业考核诚信边界。
- **闭环所需证据**：设计类高校关于生成式 AI 工具在数字艺术基础课中的使用指南与防沉迷/防代写评价策略。
- **建议检索词与领域**：`generative AI academic integrity 3D design education`, `AI texturing tools foundational pedagogy`.
- **阻断范围**：**Later Course Polish**；不阻断 v0.4 基础课表排定，不阻断 #22。

---

## 5. 首轮覆盖率统计与合成结论 (First-Pass Synthesis & Backlog Summary)

### 5.1 覆盖状态全量统计 (Coverage Statistics)

在全课梳理的 **24 个核心知识单元行 (Knowledge Units Rows)** 中，机械统计如下：

| 覆盖状态 (Coverage Status) | 数量 | 占比 | 对应知识单元清单 |
| :---: | :---: | :---: | :--- |
| **`STRONG`** | 17 | 70.8% | KU-W01-1, KU-W01-2, KU-W01-3, KU-W01-4, KU-W02-2, KU-W02-3, KU-W03-1, KU-W04-1, KU-W04-2, KU-W04-3, KU-W05-1, KU-W05-2, KU-W06-1, KU-W06-3, KU-W07-2, KU-W08-1, KU-W09-1 |
| **`PARTIAL`** | 5 | 20.8% | KU-W02-1 (节点入门), KU-W03-2 (高低模探索), KU-W06-2 (近迁移), KU-W07-1 (期末任务解构), KU-W08-2 (大班讲评) |
| **`RUNTIME REQUIRED`** | 2 | 8.3% | KU-W05-3 (视口绘制与防丢件), KU-W09-2 (离线渲染与 glTF 交付) |
| **`MISSING` (未检索到证据)** | 0 | 0.0% | *(核心原理均有一手或二级证据，但教学法与运行时缺口显式沉淀入台账)* |
| **总计 (Total)** | **24** | **100.0%** | **Stage 1 (4) + Stage 2 (14) + Stage 3 (6)** |

### 5.2 最坚实证据支撑领域 (Strongest Existing Evidence Areas)
1. **光学物理与 Principled BSDF v2 参数语义**：由 Adobe PBR Guide (2018) Part 1 (pp. 18–40) & Part 2 (pp. 45–63) 与 OpenPBR v1.1.1 规范形成双重锁死，定义清晰，无概念争议；
2. **硬表面材质分层与程序化噪波构建**：由 CORE42 `texturing-c05/c07` 与 Shah (2022) Ch 3–6 提供极为详尽的课时时码、节点接法与分层因果逻辑先例；
3. **视口外观开发 (LookDev) 与中性环境照明**：由 Dinur (2026) Ch 11 与 CORE42 工业车间 HDRI 流程提供扎实的观察与自检支撑；
4. **W1 教学包课时结构**：已由 Course Owner 验收锁定（`TEACHER ACCEPTED WITH DELTAS`），包含开局 15 分钟导学占位，逻辑闭环。

### 5.3 真正的承重缺口与决策分流 (Load-Bearing Gaps & Action Backlog)

#### 分流 1：阻断 Issue #22 的设计缺口（立即作为 #22 核心输入）
- **`[GAP-W07-ASSGN]`**：全新综合期末项目的任务书范式、资产供给模式（统一下发 vs 有界三选一）与评价维度。这是当前排课体系进入 W7–W9 的**第一核心阻塞点**，需由 Issue #22 独立论证并输出架构决策。

#### 分流 2：阻断 v0.4 综合排课的教学法缺口（下阶段靶向调研候选）
- **`[GAP-W02-PED]`**：W2 节点思维极简脚手架（防止艺术生大面积连线卡顿）；
- **`[GAP-W03-BAKE]`**：W3 高低模法线微案例实操形态选择（演示 vs 引导微实验 vs 拓展，不等于已锁定为纯观察）；
- **`[GAP-W04-PROC]`**：W4 噪波节点复杂度上限与防拉伸配方；
- **`[GAP-W08-FEED]`**：W8 单师 35 人工作室流动讲评漏斗机制。

#### 分流 3：阻断周课件包发布的受控技术探针（机房现场 Runtime Probes）
- **`[GAP-W05-GUI] / [PENDING GATE 01]`**：Blender 5.2 Texture Paint 局部绘制与防丢件探针；
- **`[GAP-W06-TRANS] / [GATE-ASSET-02]`**：Antique Ceramic Vase 01 零摩擦 `.blend` 模板加载与评测探针；
- **`[GAP-ASSET-FLASHLIGHT] / [GATE-ASSET-01]`**：Vintage Flashlight 网格曲率与 M6/M7 承载性切片解构；
- **`[GAP-W09-VIEW] / [GATE-RT-01]`**：离线机房环境 glTF / WebGL 实时查看器端到端兼容性探针。

---

*本文件作为项目全局教学证据路由地图与研究缺口登记表，归档于 `docs/research/week1-9-teaching-evidence-map.md`。*
