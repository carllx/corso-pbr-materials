# 《三维数字材质制作》教材与学习资源调研图谱 (Textbook & Learning Source Map)

> **研究阶段**：Stage 1 — Textbook Closeout / 教材定稿与知识资源获取 (Issue #2)  
> **当前状态**：Gate 3 Evidence Revision  
> **审阅锚点**：基于 Course Knowledge Notebook (`e29f9644-03b2-4e1b-bcb0-b954b5bf08be`) 实际可访问语料与官方版本事实修正  
> **核心原则**：课程核心严格限定为 **Material / Texture Authoring（材质与纹理创作）**，建模、雕刻、拓扑重构与高低模资产全流程仅作为支撑性前置输入，不反客为主成为主体。

---

## 1. 知识库实际资源清单与状态 (Verified Source Inventory)

经 IDE 运行时对 Course Knowledge Notebook 进行全面核查与清理，已剔除抓取失败的死链，当前实际可访问资源生态如下：

### 1.1 核心已获取教材与专著 (Core Acquired Textbooks)
- **Primary Textbook Skeleton Candidate**：
  - 《Realistic Asset Creation with Adobe Substance 3D》— Zeeshan Jawed Shah (Packt Publishing, 2022)
  - *Provenance*: PDF 已就绪 (`6a26e0ee-71de-43cf-be7f-c39d2ad2da43`)。
- **Observation, Photorealism & LookDev Reference**：
  - 《The Complete Guide to Photorealism: Understanding the Principles of Photorealistic CG and VFX, 2nd Edition》— Eran Dinur (Routledge, 2026)
  - *Provenance*: ePub 已就绪 (`72abf6ec-8c3d-4c9d-83f7-9e5a80f79e43`)。
- **PBR Theory Authority**：
  - 《The PBR Guide (Part 1: The Theory of PBR & Part 2: Practical Guidelines for Substance 3D Authors)》— Wes McDermott / Adobe
  - *Provenance*: Part 1 (`93dd34e7-d6ca-4f55-a5f6-3d4dfc2c6458`) 与 Part 2 (`3b740455-7c40-426d-aeb2-a25688cce706`) 均已就绪。
- **Graphics Foundation Reference**：
  - 《Real-Time Rendering, 4th Edition (中英双语)》— Tomas Akenine-Möller et al.
  - *Provenance*: 中文版 ePub (`447efad6-aad8-4f44-bf86-e60f54d7c57f`) 与英文版 ePub (`e3bc8e81-2fda-4d66-b4bd-4ffefb1448dd`) 均已就绪。

### 1.2 持续演进官方技术体系 (Living Official Sources)
针对 Shah 2022 的版本时效性，直连 AdobeDocs 官方源文档与行业标准以建立活体事实基准：
- **Substance 3D Painter 活体权威源**:
  - Painter Getting Started (`192ed109-2b3d-4c27-bfc4-5c4e87cdf3f1`)
  - Smart Materials & Masks (`c55c2489-0e56-4f9b-9298-fe26a650380e`)
  - Generators (`863d665c-74b8-408e-a594-e66677073a5a`)
  - Baking & How to Bake Mesh Maps (`2651bfb7-6cf0-4fa7-a990-5b7c374ea7ce`, `c7e2f3d1-1326-4bf4-8d64-1295a5166c38`)
  - Export & Output Templates (`2ef5d089-f272-490a-bff5-0e09531686b7`, `cacb0263-59d8-4414-9530-1965717c9020`)
  - All Changes Release Notes & 2026 Innovations (`3372381e-11d8-45c4-a0c7-a57490f9d8d9`, `76f4e622-e1d0-40da-acc2-80e97b3ccba4`)
- **Substance 3D Designer 官方入门**:
  - Designer Getting Started & Workflow Overview (`53891efc-3d73-4a1b-995a-547461a2eb5a`, `07d44c9c-9e24-4ec1-8ca8-610fe1a4b7d8`)
- **Substance 3D Sampler 材质数字化**:
  - Sampler Image to Material (`32895b88-98e8-4e10-b192-a85398f2b8b4`)
  - Sampler Generative Workflows (`f8999918-65fc-4520-8957-f0999d72afdd`)
- **Blender 与开放标准**:
  - Blender 4.5/4.x Materials Intro, Shader Nodes & Principled BSDF (`e7660364-35b2-40e7-9edd-492c6dfc1e00`, `f3313ff9-aaf3-4814-bd0c-a91a97e93456`, `7e000672-195f-434d-8e1e-71d76f18d19a`)
  - ASWF OpenPBR 1.1.1 Specification (`32eb7bd7-aa57-4bfe-b291-d40d75f53095`)

### 1.3 期望但当前不可获取文献 (Desired but Currently Unavailable References)
保留在知识地图中作为教学思想对标与待解边缘价值参考，但不作为当前排课的物理依赖：
- 《Substance 3D Painter実践講座―テクスチャの作り方・考え方を学ぶ》— CafeGroup (Born Digital, 2025)
- 《作例で学ぶ Substance 3D Designerの教科書》— もんしょ 等 (Born Digital, 2022)

---

## 2. 实际语料 Gap Analysis 与审查证据 (Gap Register)

基于 Course Knowledge Notebook 实际检索与官方版本历史核验，形成以下收敛结论：

### 2.1 Shah (2022) 承担 Primary Textbook Skeleton 的证据判断
- **审计定位**：`Primary Textbook Skeleton — strong current candidate / provisionally sufficient on available corpus`。
- **事实依据 (Source-supported Facts)**：
  - *建模前置极低 (very low modeling overhead / modeling is not the instructional focus)*：全书 14 章中，前言明确假定读者具备 3D 建模基础知识，并直接以导入外部准备完毕的基础网格切入；不含多边形建模、拓扑重构、高模雕刻等教学。
  - *工具链章节结构清晰*：
    - Ch 1–6：聚焦 Substance 3D Painter 贴图绘制全流程（含 Texel Density 规划、多 Texture Set 管理、顶点颜色烘焙 ID Map、Fill/Paint 层级堆叠、Tri-planar 投影、Smart Materials、Anchor Points 锚点微细节动态传递、Position 贴图全场景归一化积灰、多贴图集实例化等）；
    - Ch 7–10：聚焦 Substance 3D Designer 程序化高度图与节点逻辑；
    - Ch 11：聚焦 Substance 3D Sampler 基于照片的材质提取与平铺；
    - Ch 12–14：聚焦 Substance 3D Stager 的场景排版、物理摆放、光照与最终渲染呈现。
- **阶段结论**：在现有可访问语料中，Shah (2022) 具备作为主教材骨架的强候选资格，且在现有资源下暂时充分（provisionally sufficient）。

### 2.2 官方版本更新事实与 Living Sources 修正清单
针对 Shah (2022) 的技术老化点，根据官方 Release Notes 核实准确版本事实，教学中需由 Living Sources 予以修正：

| 范畴 | 官方版本发布事实 (Version Facts) | Shah (2022) 老旧操作 | 教学执行修正方案 |
| :--- | :--- | :--- | :--- |
| **烘焙模式与偏斜修复** | **Painter 12.1 (2026)** 重构烘焙 UI，引入 **Paint Skew（视口涂抹偏斜修正法线）** 与自动重烘焙；此前自 **8.3.0** 起引入独立 Baking Mode (F8) 与隐式包围盒可视化预览。 | 依赖旧版模态对话框，需手动调整 Cage 距离以尝试修复倾斜变形。 | 采用独立 Baking Mode (F8)，直接在视口中使用 Paint Skew 笔刷涂抹修复螺丝孔等法线倾斜。 |
| **着色器标准对齐** | **Painter 12.1 (2026)** 正式将 **OpenPBR 1.1** 设定为默认工作流与默认着色器。 | 新建项目使用旧版 Adobe Standard Material (ASM) 或旧 PBR Metallic-Roughness。 | 新建工程对齐 OpenPBR 1.1 工业规范，与现代 USD 及 Blender 4.x/5.x Principled BSDF 1:1 互通。 |
| **曲面贴花自适应** | **Painter 12.0 (2026)** 引入 **Warp to Geometry** 几何体智能包裹投影算法。 | 传统平面投影或旧版 2D 变形在复杂起伏表面产生拉伸与边缘淡出。 | 贴花（Decals）与徽标贴附采用 Warp to Geometry 动态贴合复杂曲面。 |
| **网格重载流程** | **Painter 12.0 (2026)** 精简新建项目界面，并新增更符合迭代逻辑的 **Reload Mesh（重载网格）** 专用入口。 | 修改低模 UV 或布线需通过复杂的项目配置重新映射。 | 低模调整采用无损 Reload Mesh，完整保留图层栈与烘焙数据。 |
| **曲线带状路径工具** | **Painter 11.1 (2025-11 引入，非 2026 新功能)** 推出 **Ribbon Path（带状贝塞尔曲线路径工具）** 与 75 种专用预设。 | 规则纹理（缝线、焊缝、边饰）依赖笔刷手动涂刷或 Stencil 耗时印落。 | 规则连续细节采用 Ribbon Path 曲线绘制，单顶点调节宽度与不透明度。 |

### 2.3 CafeGroup 2025 缺失的影响评估
- **审计定位**：`Desired but currently unavailable / unresolved marginal value`。
- **客观判断**：
  - 由于该完整教材当前不可访问，没有直接文本证据证明现有语料“比它更深”或“完全替代且毫无损失”；
  - 但在实际教学可用性上，`available corpus currently provides a workable substitute for Material Observation / PBR / LookDev`：
    - Eran Dinur (2026)《The Complete Guide to Photorealism》提供了现实世界物理反向工程框架（人眼 vs 相机、六层色彩拆解、自然光学）；
    - Adobe《The PBR Guide》提供了光学守恒与安全色阶；
    - Shah (2022) 第 3–6 章落实了分层落地（底材 $\rightarrow$ 漆面 $\rightarrow$ 边缘磨损 $\rightarrow$ 凹陷藏污 $\rightarrow$ 重力积灰）。
  - 因此该书保留为高价值参考，但不阻塞当前课程骨架构建。

### 2.4 日本 Designer 教材缺失的影响评估
- **审计定位**：`Shah + Adobe Designer official sources + Blender Nodes appear sufficient for a bounded undergraduate procedural foundation`。
- **客观判断**：
  - 日本 576 页教材聚焦于极其深度的节点数学与原子逻辑，因当前不可获取，将其作为高价值备课参考；
  - 不能将“教材不可获得”混淆或合理化为“科学控制认知负荷的证据”；
  - 针对本科 8 周的程序化教学，Shah Ch 7–10 结合 Adobe 官方入门及 Blender Shader Nodes，足以支撑一个有限边界的程序化材质基础（高度驱动、多通道联动、平铺去重复）；
  - **但 Designer 在 8 周整体课程中的最终课时与教学深度仍未决（unresolved），属于后续 Stage 2 Teaching Value Matrix 的讨论范畴**。

### 2.5 中文实训落地缺口与采购状态
- **审计定位**：`Conditional Acquisition — student-facing practice gap confirmed; acquisition decision pending Step 4`。
- **客观判断**：
  - 确认存在真实缺口：普通高校艺术类本科生面对全英文教材确实存在“上机找按钮、专业术语理解偏差”的实操摩擦；
  - **项目工作假设 (Project Hypotheses - 待验证)**：
    - *假设 A*：Adobe 官方提供的简体中文帮助文档足以覆盖日常实操查阅；
    - *假设 B*：教师提取自制的《中文实训界面对照 Cheat Sheet》足以消除课堂摩擦；
    - *假设 C*：国内出版教材（郑琳 2024 / 伍福军 2024）可能因出版周期存在版本滞后或偏向食谱式点击，采购必要性较低。
  - **采购决议**：上述假设尚未通过与国内教材实体的全面对比验证。是否需要出资购买国内教材，**严格保留在 Step 4 由 User 决策**，不在此阶段强行关闭。

### 2.6 Eran Dinur《The Complete Guide to Photorealism》(2026) 角色定性
- **审计定位**：`Material Observation / Photorealism / LookDev / Generative AI Control Reference`。
- **客观判断**：
  - 本书特意避免了具体软件点击教学，专注底层物理原理、现实质感观察与摄影镜头光学缺陷（倒角捕光、景深散景、色差、颗粒感）；
  - 关于第 19 章生成式 AI：官方内容涵盖基于 ControlNet（深度图 Depth、法线图 Normal）等条件引导模型与 ComfyUI 流程在写实画面中的探索；
  - **纠偏**：不得将第 19 章扩写为其直接指导“无缝 PBR 贴图生成”；其准确角色为提供写实生成式控制与 AI 视觉工作流参考（photoreal generative-control / AI visual workflow reference）。

---

## 3. 成熟专业课程证据与教学先例 (Curriculum Precedents)

通过对具备明确公开大纲与教学记录的专业数字艺术课程进行逐项核查，建立以下课程先例证据矩阵：

### 3.1 Curriculum Precedent Evidence Matrix

| Source (课程来源) | Duration (周期) | PBR 理论 | UV / Baking | Texture / Painter | Procedural | LookDev / Engine | Prepared Assets | Evidence (可核查事实依据) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **CGMA: Character Texturing for Games in Substance** | 6 周 | 深入 (Week 1 专章) | 包含 (Week 3 头部 UV 拆分与 Painter 烘焙) | 核心主体 (Week 1-6 全程 Painter 材质定义与分层) | 实用级 (Smart Masks / Generators) | 包含 (Week 3 & Week 6 Marmoset Toolbag 着色器设置与呈现) | **是** (提供预制头部与角色模型) | CGMA 官方课程大纲：Week 1 Intro & PBR $\rightarrow$ Week 2 Material Definition $\rightarrow$ Week 3 UVs & Baking $\rightarrow$ Week 4-5 Texturing & Utility Maps $\rightarrow$ Week 6 Shader Setup |
| **Gnomon: Texturing & Shading 体系与游戏工坊** | 4 阶段学期体系 + 专题工坊 | 深入 (从基础光学到游戏引擎着色网络) | 包含 (高低模贴图烘焙与切线空间法线处理) | 核心主体 (Maya/PS $\rightarrow$ Substance Painter $\rightarrow$ Mari) | 涉及 (Substance Designer 节点材质与贴图合成) | 核心 (Unreal Engine, V-Ray, Marmoset 多环境渲染) | **是** (多门贴图/LookDev 工坊随课提供完整 3D 资产与工程文件) | Gnomon BFA 课程大纲（Texturing & Shading 1-4）及 The Gnomon Workshop 系列实战教程体系 |

### 3.2 事实与项目推断的区分 (Source Facts vs. Project Inferences)
1. **预制资产与前置知识边界**：
   - *Source Fact*：CGMA 与 Gnomon 贴图课程均提供 ready-to-import 3D 模型与已展开 UV 的项目文件，直接切入材质定义与着色器调整。
   - *Project Inference*：本科《三维数字材质制作》应坚持提供高质量预制模型/标准 UV 资产，避免学生因建模卡点压缩核心材质制作时间。
2. **材质分层演化逻辑**：
   - *Source Fact*：贴图绘制过程均呈现出 `底材固有属性铺设` $\rightarrow$ `局部破损与微变化` $\rightarrow$ `基于烘焙图的智能遮罩风化` $\rightarrow$ `微观手工细节刻画`。
   - *Project Inference*：该物理演变次序与 Shah 及 Dinur 的分层模型一致，作为本科图层组织的标准认知法则。
3. **最终多环境 LookDev 验证**：
   - *Source Fact*：CGMA 在 Week 3/6 设置 Marmoset Toolbag 着色器验证；Dinur 强调最终环境照明下的镜头真实感。
   - *Project Inference*：多环境与引擎 LookDev 是避免资产仅在 DCC 视口单向生效的必经闭环。

---

## 4. 建议资源分工架构 (Provisional Resource Architecture)

```
+-----------------------------------------------------------------------------------+
|                        物理理论与质感观察 (Theory & Observation)                    |
|  - Eran Dinur《The Complete Guide to Photorealism》(2026, 2nd ed.)                  |
|    (人眼 vs 相机、色彩解构、镜头光学缺陷、写实生成式 AI 控制参考)                    |
|  - Wes McDermott / Adobe《The PBR Guide (Part 1 & 2)》(光学理论与安全色阶基准)        |
|  - Akenine-Möller《Real-Time Rendering 4th (中英双语)》(教师图形学理论底座)          |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                  主教材实操骨架候选 (Primary Textbook Skeleton Candidate)           |
|  - Zeeshan Jawed Shah《Realistic Asset Creation with Adobe Substance 3D》(2022)  |
|    (以 Retro TV / TV Shelf 贯穿 Painter 绘制、Designer 基础节点、Sampler 与 Stager)  |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                     官方版本事实对齐 (Living Official Sources)                      |
|  - Painter 12.1 (2026): improved baking / skew painting / OpenPBR 1.1 default     |
|  - Painter 12.0 (2026): Warp to Geometry / improved mesh reimport                 |
|  - Painter 11.1 (2025-11): Ribbon Path 路径工具链                                 |
|  - Blender 4.5/4.x Principled BSDF & Shader Nodes (开源跨软件节点材质标准)         |
|  - Adobe 官方简体中文帮助文档 (中文界面名词支撑)                                    |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                  本土实训支撑与待决项 (Practical Support & Pending)                  |
|  - 教师自制中文实训 Cheat Sheet (工作假设，待检验)                                  |
|  - 国内中文教材 (郑琳 2024 / 伍福军 2024) 是否采购 (保留至 Step 4 由 User 决策)      |
+-----------------------------------------------------------------------------------+
```

---
*文档归档于 `docs/research/textbook-source-map.md`，由 Antigravity 自动化研究流水线基于 Course Knowledge Notebook 实际语料实证生成并经 Browser Review 严密修正。*
