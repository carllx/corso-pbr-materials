# 《三维数字材质制作》教材与学习资源调研图谱 (Textbook & Learning Source Map)

> **研究阶段**：Phase 1B — Textbook & Learning Source Selection  
> **审阅锚点**：基于 `7e6bafe44ca6613739456c76e8e9588b58f9fe45` 确立的课程边界开展  
> **核心原则**：课程核心严格限定为 **Material / Texture Authoring（材质与纹理创作）**，建模、雕刻、拓扑重构与高低模资产全流程仅作为支撑性前置输入，不反客为主成为主体。

---

## 目录
1. [国外最新教材与专业出版物调研 (2024–2026)](#1-国外最新教材与专业出版物调研-20242026)
2. [中国大陆教材调研与客观评估](#2-中国大陆教材调研与客观评估)
3. [持续演进的官方学习体系与技术规范 (Living Official Sources)](#3-持续演进的官方学习体系与技术规范-living-official-sources)
4. [成熟专业课程证据与教学先例 (Curriculum Precedents)](#4-成熟专业课程证据与教学先例-curriculum-precedents)
5. [统一教材与学习资源比较矩阵](#5-统一教材与学习资源比较矩阵)
6. [综合分析与教材组合策略推荐](#6-综合分析与教材组合策略推荐)

---

## 1. 国外最新教材与专业出版物调研 (2024–2026)

针对国外（重点为日本与欧美）近三年出版的专业材质书籍，经对实际目录（TOC）、作者制作背景及内容权重的逐项核查，重点分析如下：

### 1.1 《Substance 3D Painter実践講座 ― テクスチャの作り方・考え方を学ぶ》
- **著者**：CafeGroup株式会社（日本知名 CG/VFX 与游戏美术实战制作团队）
- **出版社 / 出版年份**：[株式会社ボーンデジタル (Born Digital)](https://www.borndigital.co.jp/)，2025 年
- **完整核查目录 (TOC)**：
  - **Part 1 基礎編**：Chapter 1 贴图绘制概述 (テクスチャリングとは)；Chapter 2 Substance 3D Painter 软件架构；Chapter 3 PBR 材质与贴图理论；Chapter 4 UI 解析；Chapter 5 视口设置；Chapter 6 材质制作基本流程；Chapter 7 材质思考模型 (テクスチャ制作においての大切な考え方)。
  - **Part 2 初級編**：Chapter 1 模型导入；Chapter 2 素材库资产调用；Chapter 3 烘焙功能 (Baking)；Chapter 4 贴图绘制实战解析；Chapter 5 质感提升技巧；Chapter 6 Painter 视口简易渲染；Chapter 7 贴图导出。
  - **Part 3 中級編**：Chapter 1 基于 Material ID 的烘焙；Chapter 2 三面投影（Triplanar）技巧；Chapter 3 橡胶轮胎质感制作；Chapter 4 皮革座椅制作；Chapter 5 金属车身制作；Chapter 6 引擎机械结构材质；Chapter 7 多部件分层管理规范。
  - **Part 4 応用編**：Chapter 1 复杂模型准备；Chapter 2 神社建筑复合材质制作 (木材风化、瓦片磨损、青苔与泥垢)。
  - **Part 5 番外編**：Chapter 1 各渲染器差异对比 (Cycles, Arnold, Unreal 渲染特性)；Chapter 2 贴图导出模板创建与跨团队共享。
- **深度评估**：
  - *材质聚焦度*：高度聚焦 Material / Texture Authoring，没有独立建模教学主线；仅包含模型导入、模型准备以及 UV/Baking 相关的材质前置知识。
  - *PBR 与理论*：Part 1 深入讲解 PBR 光学常识，Part 5 专门探讨不同渲染器着色差异，理论与实战结合紧密。
  - *教学适配度*：结构完全符合“理论 $\rightarrow$ 基础道具 $\rightarrow$ 复杂多材质机械 $\rightarrow$ 场景建筑 $\rightarrow$ 渲染导出”的循序渐进认知规律，非常适合作为本科实操主教材候选（Core Textbook Candidate）。
  - *局限与许可风险 (Limitation)*：出版社提供大量 downloadable study data，但公开许可包含个人使用/禁止再分发等限制；若未来将这些素材作为全班教学资产，需要单独核查 classroom / educational distribution 许可，不应默认教师可以重新分发素材包。

### 1.2 《Adobe Substance 3D 1日で完成テクスチャ制作》
- **著者**：株式会社ボーンデジタル テクニカルサポート部 (Born Digital Technical Support)
- **出版社 / 出版年份**：[Born Digital](https://www.borndigital.co.jp/)，2025 年 (PDF / 官方培训教材)
- **内容覆盖**：以极短周期帮助初学者建立对 Substance 3D 生态的全局认知。重点讲解 PBR 基本概念（2-1 节）、Substance 3D Painter 基础图层绘制，以及 Substance 3D Sampler 的照片转材质（Image-to-Material / AI 贴图提取）与快速参数化材质生成。
- **深度评估**：
  - *定位判断*：篇幅精炼，适合作为课程第一周破冰与快速入门的 **Practical Companion**，特别是其对 Sampler 的涉及，可作为连接传统贴图绘制与 AI 图像转材质的轻量级桥梁。

### 1.3 《作例で学ぶ Substance 3D Designerの教科書》
- **著者**：もんしょ (Monsho)、黒澤 徹太郎、mino
- **出版社 / 出版年份**：[Born Digital](https://www.borndigital.co.jp/)，2022 年 3 月
- **ISBN**：978-4-86246-526-9（共 576 页）
- **完整核查目录 (TOC)**：
  - **第 1 章**：Substance 3D Designer 基础、UI、Graph View、参数暴露 (Exposing Parameters)。
  - **第 2 章**：程序化材质创建全流程（石头、土壤、枯草生成 $\rightarrow$ 算子合成 Normal / Height / Roughness / AO / BaseColor 通道 $\rightarrow$ 输出 `.sbsar` 并在外部引擎中调用）。
  - **第 3 章**：节点深度进阶（原子节点行为、数学函数 Function Graph、子图拆分）。
  - **第 4 章**：与 Substance 3D Painter 及 Sampler 的工业级协同管线。
- **深度评估**：
  - *定位判断*：程序化/参数化材质领域的权威教材。但由于其厚达近 600 页且包含大量数学与函数图逻辑，在 8 周本科通识/专业基础课中若全盘讲授会导致学生严重认知过载。保留其作为教师备课与程序化材质演示的 **Teacher Reference** 定位。

### 1.4 Blender 4.x 现代程序化材质资源 (Packt / CG Cookie / Blender Studio)
- **代表资源**：
  1. *Material Fundamentals - Procedural Textures in Blender 4.4* ([Packt Publishing, 2025](https://www.packtpub.com/))
  2. *Fundamentals of Blender Materials and Shading* ([CG Cookie, 2024–2025 更新](https://cgcookie.com/))
  3. [Blender 4.x Manual - Shader Nodes & Principled BSDF v2](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/principled.html)
- **内容覆盖**：Texture Coordinates（物体/生成/UV）、Noise/Voronoi/Wave 算法纹理、ColorRamp 与 Map Range 映射、Math/Mix 蒙版运算、微表面粗糙度扰动、Node Groups 节点组封装与参数暴露、Cycles 烘焙程序化纹理为 PBR 贴图。
- **深度评估**：
  - *定位判断*：针对 Blender 4.x 现代 Shader Editor 的系统化训练，门槛低、可视化强、免额外商业授权，是培养学生“程序化材质抽象思维”的最佳 **Practical Companion**。

---

## 2. 中国大陆教材调研与客观评估

针对国内高校近五年出版的相关教材进行查验，重点判断其是否聚焦于材质本身以及是否具有过多建模冗余：

### 2.1 《Blender+Substance 3D Painter 建模与材质制作实战》
- **作者**：来阳
- **出版社 / 出版年份**：[人民邮电出版社](https://www.ptpress.com.cn/)，2026-07
- **ISBN**：9787115700612
- **内容结构剖析**：
  - 前半部分（基础与建模，占较大篇幅）：Blender 基础操作、多边形建模、高低模制作、UV 展开；
  - 中间核心（材质绘制实战，属主要章节）：Substance 3D Painter 贴图绘制实战，按木纹、金属、皮革、玻璃、布料等常见真实物理材质分类讲解分层绘制技巧；
  - 后续拓展（少量篇幅）：包含腾讯混元 3D（Hunyuan3D）等 AI 辅助建模介绍与 Unreal Engine 资产呈现。
- **深度评估**：
  - *优点*：软件版本新，结合了目前最主流的 Blender + Painter + UE 组合，材质案例贴合国内教学环境，包含 AI 与引擎展示。
  - *局限*：由于是一本涵盖建模到材质的“全流程实战书”，建模与拓扑占据了较多篇幅，导致其对 PBR 物理原理底层、Texel Density 计算、通道打包与复杂着色器逻辑的理论阐述较浅。
  - *定位建议*：适合作为国内机房实训的中文配套 **Practical Companion**，但不宜单独作为纯材质理论的主教材。

### 2.2 《Substance Painter 次世代 PBR 材质制作》
- **编著信息**：谢怀民、林鑫 等（ISBN、出版社和出版年份已核实；第三编者公开元数据存在冲突，待出版社版权页确认）
- **出版社 / 出版时间**：北京理工大学出版社，2021-10
- **ISBN**：9787568290227
- **内容结构剖析**：系统介绍次世代贴图概念、Painter 软件界面、烘焙贴图流程、智能材质与智能遮罩应用，并通过刀剑武器与道具案例展示绘制流程。
- **深度评估**：
  - *优点*：作为国内较早聚焦 Painter 的教材，其项目化实训框架被国内部分院校采纳为参考书。
  - *局限*：出版时间较早（基于早期 Substance 版本），缺少近年来 OpenPBR、虚幻 5 Lumen/Nanite 协同、通道打包（ORM）及 AI 辅助材质工作流等新内容，部分插图与界面已与当前软件脱节。
  - *定位建议*：可作为高校历史教学案例参考（**Teacher Reference**），不建议作为 2026 年学生主教材。

> **国内教材客观现状总结**：  
> 目前中国大陆出版物中，绝大多数贴图教材均被打包在《次世代游戏模型制作》《三维游戏美术全流程》等大而全的建模教材中，“材质/纹理”常被压缩为后半段的几个章节；而专讲材质的书籍多为软件菜单操作手册，缺乏贯穿“微表面理论 $\rightarrow$ 严格几何烘焙工程 $\rightarrow$ 引擎实时渲染”的独立高可信教材。

---

## 3. 持续演进的官方学习体系与技术规范 (Living Official Sources)

纸质出版物受制于出版周期，必须依托官方持续更新的数字化文档构建教学底层事实基准：

| 官方学习体系 / 规范 | 维护机构 | 核心价值与内容 | 在课程中的建议角色 |
| :--- | :--- | :--- | :--- |
| **[Adobe Substance 3D The PBR Guide (Part 1 & 2)](https://substance3d.adobe.com/tutorials/courses/the-pbr-guide-part-1)** | Adobe (Wes McDermott) | PBR 光学理论、微表面散射、Metallic/Roughness 规范与安全色阶。 | **Student Core Reading（学生必读理论文献）** |
| **[Substance 3D Painter Official Documentation](https://experienceleague.adobe.com/en/docs/substance-3d-painter/using/baking/baking)** | Adobe | 烘焙算子（Bakers）、Smart Materials / Masks 原理与图层通道管理。 | **Classroom Reference（课堂与实操速查手册）** |
| **[Substance 3D Sampler Official Docs](https://helpx.adobe.com/substance-3d-sampler/)** | Adobe | 图像转材质（Image-to-Material）、AI 污渍滤镜与快速贴图平铺。 | **Practical Companion（AI/图像材质实验参考）** |
| **[Substance 3D Designer Graph Docs](https://helpx.adobe.com/substance-3d-designer/)** | Adobe | 程序化纹理合成、节点数学逻辑与 `.sbsar` 制作。 | **Teacher Reference（教师备课/进阶演示参考）** |
| **[Blender Manual - Principled BSDF & Shading](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/principled.html)** | Blender Foundation | 现代 OpenPBR 对齐着色器、节点材质与 Cycles 烘焙管线。 | **Student Core Reading（开源着色器标准参考）** |
| **[Epic Games Unreal Engine PBR Materials Docs](https://dev.epicgames.com/documentation/en-us/unreal-engine/physically-based-materials-in-unreal-engine)** | Epic Games | 实时 PBR 接口、材质实例（Material Instances）、着色器优化与验证。 | **Student Core Reading（引擎交付与验证标准）** |
| **[Unity URP Lit Shader Documentation](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest/index.html?subtopic=manual/lit-shader.html)** | Unity Technologies | 跨平台移动端与通用 PBR 着色器、Shader Graph 节点。 | **Classroom Reference（备选引擎参考）** |
| **[ASWF OpenPBR](https://academysoftwarefoundation.github.io/OpenPBR/) / [Khronos glTF 2.0 Spec](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#materials)** | ASWF / Khronos Group | 工业级材质交换与底层多层着色规范。 | **Technical Specification（技术规范底座/教师参考）** |

---

## 4. 成熟专业课程证据与教学先例 (Curriculum Precedents)

通过对具备明确公开大纲与教学记录的专业数字艺术课程进行逐项核查，建立以下课程先例证据矩阵：

### 4.1 Curriculum Precedent Evidence Matrix

| Source (课程来源) | Duration (周期) | PBR 理论 | UV / Baking | Texture / Painter | Procedural | LookDev / Engine | Prepared Assets | Evidence (可核查事实依据) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **CGMA: Character Texturing for Games in Substance** | 6 周 | 深入 (Week 1 专章) | 包含 (Week 3 头部 UV 拆分与 Painter 烘焙) | 核心主体 (Week 1-6 全程 Painter 材质定义与分层) | 实用级 (Smart Masks / Generators) | 包含 (Week 3 & Week 6 Marmoset Toolbag 着色器设置与呈现) | **是** (提供预制头部与角色模型) | CGMA 官方课程大纲：Week 1 Intro & PBR $\rightarrow$ Week 2 Material Definition $\rightarrow$ Week 3 UVs & Baking $\rightarrow$ Week 4-5 Texturing & Utility Maps $\rightarrow$ Week 6 Shader Setup |
| **Gnomon: Texturing & Shading 体系与游戏工坊** | 4 阶段学期体系 + 专题工坊 | 深入 (从基础光学到游戏引擎着色网络) | 包含 (高低模贴图烘焙与切线空间法线处理) | 核心主体 (Maya/PS $\rightarrow$ Substance Painter $\rightarrow$ Mari) | 涉及 (Substance Designer 节点材质与贴图合成) | 核心 (Unreal Engine, V-Ray, Marmoset 多环境渲染) | **是** (多门贴图/LookDev 工坊随课提供完整 3D 资产与工程文件) | Gnomon BFA 课程大纲（Texturing & Shading 1-4）及 The Gnomon Workshop 系列实战教程体系 |
| **Born Digital: 《Substance 3D Painter 実践講座》配套实训体系** | 5 篇章 (23 章节) | 深入 (Part 1 专章讲解 PBR 理论与光学常识) | 包含 (Part 2 & Part 3 详解烘焙功能与 ID 烘焙) | 核心主体 (Part 1-4 覆盖道具、机械车辆、建筑材质绘制) | 涉及 (Triplanar 三面投影与智能生成器) | 包含 (Part 5 专章对比 Cycles, Arnold, Unreal 渲染器差异) | **是** (提供全套实训模型与项目数据包) | Born Digital 出版目录与随书资源包结构：Part 1 基础 $\rightarrow$ Part 2 初级 $\rightarrow$ Part 3 中级 $\rightarrow$ Part 4 进阶 $\rightarrow$ Part 5 渲染器对比 |

### 4.2 事实与项目推断的区分 (Source Facts vs. Project Inferences)

#### 1. 预制资产与前置知识边界
- **Source Fact（客观事实）**：
  在 CGMA《Character Texturing for Games in Substance》与 Gnomon 相关贴图工坊中，课程均提供了 ready-to-import 3D model 与已展开 UV 的项目文件，使学员能够直接进入材质定义、贴图烘焙与着色器调整环节。
- **Project Inference（项目推断）**：
  对于本项目这种明确聚焦 **Material / Texture Authoring** 的本科课程，采用“提供高质量预制模型/标准 UV 资产”的模式，构成了值得重点借鉴的教学策略，可避免学生在有限学时内因前期建模卡点而压缩核心材质制作时间。

#### 2. 材质分层与风化逻辑
- **Source Fact（客观事实）**：
  在已核查的 CGMA 与 Born Digital 教学案例中，贴图绘制过程均呈现出 `底材固有属性铺设 (Base Color / Roughness)` $\rightarrow$ `局部破损与微变化 (Color/Roughness Breakup)` $\rightarrow$ `基于烘焙图的智能遮罩风化 (Generators/Masks)` $\rightarrow$ `微观手工细节刻画` 的推进次序。
- **Project Inference（项目推断）**：
  该逻辑反映了物理世界中材质随时间演变的客观层次，应作为本科阶段材质图层组织与审美分析的基础教学逻辑。

#### 3. 最终多环境验证
- **Source Fact（客观事实）**：
  CGMA 课程在后期（Week 3 与 Week 6）设置了 Marmoset Toolbag 着色器组装与呈现环节；Born Digital 教材在 Part 5 专门设置了“各渲染器差异（Cycles, Arnold, Unreal）”对比章节。
- **Project Inference（项目推断）**：
  在不同光照环境和实时引擎中进行 LookDev 验证，是避免资产仅在 DCC 视口单向生效的关键闭环，应列为学生作业验收的核心评估点之一。

---

## 5. 统一教材与学习资源比较矩阵

| 书名 / 资源名称 | 作者 / 出版机构 | 年份 | 对应软件 | 材质重点 | PBR | Painter | Procedural | Designer | Sampler | AI关联 | 建模负担 | 游戏/影视应用 | 练习资产 | 建议角色 (Proposed Role) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Substance 3D Painter実践講座** | CafeGroup / Born Digital | 2025 | Painter 10.x | 资产贴图绘制、烘焙、PBR物理 | 深度 | 深度 | 涉及(Triplanar) | 无 | 涉及 | 间接 | **极低 (仅材质前置)** | 游戏+影视通用 | 完整提供 (需注意二次分发许可) | **Core Textbook Candidate** |
| **The PBR Guide (Part 1 & 2)** | Wes McDermott / Adobe | 持续更新 | 通用 | PBR光学、微表面、安全色阶 | **极其深入** | 深度结合 | 原理级 | 原理级 | 原理级 | 原理级 | **无** | 全行业基准 | 提供样例 | **Living Official Source** |
| **Blender+SP建模与材质实战** | 来阳 / 人民邮电出版社 | 2026-07 | Blender+SP | 道具建模、UV、Painter实战 | 中等 | 深度 | 基础 | 无 | 无 | 涉及 (混元3D) | **较重 (含较多建模)** | 游戏为主 | 完整提供 | **Practical Companion** |
| **Adobe Substance 3D 1日で完成** | Born Digital Tech Support | 2025 | Painter+Sampler | 快速贴图绘制、图像转材质 | 基础 | 基础 | 基础 | 无 | 深度 | 较高 (AI滤镜) | **无** | 快速入门 | 提供 | **Practical Companion** |
| **作例で学ぶ Designerの教科書** | もんしょ等 / Born Digital | 2022-03 | Designer 11.x/12.x | 程序化2D纹理、.sbsar | 深度 | 接口结合 | **极其深入** | **完全核心** | 结合 | 间接 | **无** | 游戏+影视通用 | 完整提供 | **Teacher Reference** |
| **Material Fundamentals (Packt)** | Packt Publishing | 2025 | Blender 4.4 | 节点材质、噪声、Cycles烘焙 | 深度 | 无 | **深度** | 无 | 无 | 间接 | 极低 | 通用着色 | 提供工程 | **Practical Companion** |
| **Real-Time Rendering 4th** | Akenine-Möller / CRC Press | 2018 | 理论无软件 | 图形渲染、BRDF、光照计算 | **殿堂级** | 无 | 无 | 无 | 无 | 无 | 无 | 实时渲染 | 算法源码 | **Teacher Reference** |
| **CGMA: Texturing for Games** | 3A 行业导师 / CGMA | 长期更新 | Painter+Engine | 资产多通道绘制、烘焙、LookDev | 深度 | **极其深入** | 实用级 | 涉及 | 结合 | 适度 | **无 (全提供资产)** | 3A 游戏标准 | 完整提供 | **Curriculum Precedent** |

---

## 6. 综合分析与教材组合策略推荐

### 6.1 国内外教材的结构性差异
- **国外出版物特征（尤其是日本 Born Digital 与欧美行业课程）**：专业垂直度高，高度聚焦于材质本身，较少掺杂大量建模教学，依托提供的工业级模型资产，集中篇幅讲解 PBR 原理、分层逻辑、烘焙算子与多渲染器差异。
- **国内出版物特征**：倾向于“大而全全流程”与“案例步骤驱动”，建模与基础操作占比相对较高，对 PBR 微表面物理推导、Texel Density 计算与引擎着色器架构的深度剖析相对欠缺。

### 6.2 当前教材体系的缺失点（Gaps）
1. **生成式 AI 与传统 PBR 结合的体系化教材尚属空白**：市面教材对 AI 的涉及仅停留在“用 AI 生成一个 3D 模型”或“用 Sampler 转一张贴图”，缺乏在完整工业材质管线中如何利用 AI 提效（如 AI 无缝平铺、AI 辅助法线微细节生成）并维持 PBR 物理一致性的系统论述。
2. **现代 OpenPBR 标准的普及教材滞后**：大部分教程仍在沿用早期 Disney BRDF 或旧版标准，未能充分体现 Blender 4.0+ 和最新渲染器向 OpenPBR 对齐后的材质组织方式。

### 6.3 教材组合策略推荐 (Recommended Candidate Strategy)

*注：以下为本阶段调研给出的**候选组合推荐**，供后续大纲设计时参考，不作为最终课程采用决定。*

1. **核心教材候选 (Core Textbook Candidate)**：
   - 推荐评估 **《Substance 3D Painter実践講座》(Born Digital, 2025)** 作为课程主干案例与材质思考模型的蓝本（其“理论 $\rightarrow$ 基础道具 $\rightarrow$ 机械 $\rightarrow$ 建筑 $\rightarrow$ 跨引擎渲染”五段式结构科学紧凑）。
2. **官方理论底座 (Living Official Source)**：
   - 推荐以 Adobe **《The PBR Guide (Part 1 & Part 2)》** 和 **Epic Games / Blender 官方 PBR 文档** 作为学生的必读理论纲领，保证物理原理的严谨性。
3. **中文实操伴随教材 (Practical Companion)**：
   - 推荐来阳 **《Blender+Substance 3D Painter 建模与材质制作实战》(2026-07)** 作为学生课后中文实操速查与机房实操伴随参考书，但在课程教学中应重点取其材质绘制与实训篇章。
4. **程序化与教师参考 (Teacher References & Precedents)**：
   - 教师备课推荐以 **《作例で学ぶ Substance 3D Designerの教科書》(2022-03)**、**《Real-Time Rendering, 4th》** 与 **CGMA / Gnomon 课程先例** 为质量基准。

---
*报告归档于 `docs/research/textbook-source-map.md`，由 Antigravity 自动化研究流水线生成并核查。*
