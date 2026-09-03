# 《三维数字材质制作》教材与学习资源调研图谱 (Textbook & Learning Source Map)

> **研究阶段**：Stage 1 — Textbook Closeout / 教材定稿与知识资源获取 (Issue #2)  
> **当前状态**：COMPLETED (Step 5 Final Textbook Decision & Closeout)  
> **审阅锚点**：基于 Course Knowledge Notebook (`e29f9644-03b2-4e1b-bcb0-b954b5bf08be`) 实际可访问语料与 Step 4B Browser 终审决策  
> **核心原则**：课程核心严格限定为 **Material / Texture Authoring（材质与纹理创作）**，建模、雕刻、拓扑重构与高低模资产全流程仅作为支撑性前置输入，不反客为主成为主体。

---

## 1. 知识库实际资源清单与状态 (Verified Source Inventory)

经 IDE 运行时与 NotebookLM 清理（完成 Step 4A 语料瘦身，由 30 个精简为 24 个高纯度核心源，清空死链与实质重复源），当前实际知识库配置如下：

### 1.1 核心已获取教材与专著 (Core Acquired Textbooks)
- **Primary Textbook Skeleton**：
  - 《Realistic Asset Creation with Adobe Substance 3D》— Zeeshan Jawed Shah (Packt Publishing, 2022)
  - *Provenance*: PDF 已就绪 (`6a26e0ee-71de-43cf-be7f-c39d2ad2da43`)。
- **Observation, Photorealism & LookDev Reference**：
  - 《The Complete Guide to Photorealism: Understanding the Principles of Photorealistic CG and VFX, 2nd Edition》— Eran Dinur (Routledge, 2026)
  - *Provenance*: ePub 已就绪 (`72abf6ec-8c3d-4c9d-83f7-9e5a80f79e43`)。
- **PBR Theory Authority**：
  - 《The PBR Guide, Third Edition (2018)》— Wes McDermott / Adobe (Allegorithmic)
  - *Provenance*: 完整双篇连排 PDF 已就绪 (`7b3dde6d-a06c-42b1-9814-3bed5617c315`，含 Part 1 理论、Part 2 实战及附录反射率表；旧网页镜像源已去重删除)。
- **Graphics Foundation Reference**：
  - 《Real-Time Rendering, 4th Edition (中英双语)》— Tomas Akenine-Möller et al.
  - *Provenance*: 中文版 ePub (`447efad6-aad8-4f44-bf86-e60f54d7c57f`) 与英文原版 ePub (`e3bc8e81-2fda-4d66-b4bd-4ffefb1448dd`) 均已就绪。

### 1.2 持续演进官方技术体系 (Living Official Sources)
针对 Shah 2022 的版本时效性，直连 AdobeDocs 官方源文档与行业标准以建立活体技术基准：
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
  - Blender 5.2/4.5 LTS Materials Intro, Shader Nodes & Principled BSDF (`e7660364-35b2-40e7-9edd-492c6dfc1e00`, `f3313ff9-aaf3-4814-bd0c-a91a97e93456`, `7e000672-195f-434d-8e1e-71d76f18d19a`)
  - ASWF OpenPBR 1.1.1 Specification (`32eb7bd7-aa57-4bfe-b291-d40d75f53095`)

### 1.3 期望但当前不可获取文献 (Desired but Currently Unavailable References)
保留在知识地图中作为教学思想对标与待解边际价值参考，不得列为实际课程依赖：
- 《Substance 3D Painter実践講座―テクスチャの作り方・考え方を学ぶ》— CafeGroup (Born Digital, 2025)
- 《作例で学ぶ Substance 3D Designerの教科書》— もんしょ 等 (Born Digital, 2022)

---

## 2. 最终教材体系决议与角色定性 (Final Role-based Resource Decision)

经多模型独立发现、第一方元数据查验、Notebook 语料清洗、可用语料 Gap Analysis 及 Step 4B 采购权衡，确立《三维数字材质制作》最终七层角色化资源体系：

### 2.1 Primary Textbook Skeleton（主教材骨架）
- **选定文献**：**Zeeshan Jawed Shah —《Realistic Asset Creation with Adobe Substance 3D》(Packt Publishing, 2022)**
- **决策状态**：`Selected Primary Textbook Skeleton`
- **核准依据与边界说明**：
  - 本书并非 2026 最新出版物，但其章节架构与教学逻辑高度契合本科“纯材质/贴图创作”目标；
  - 建模前置负担极低（`very low modeling overhead / modeling is not the instructional focus`），全书以预制资产导入切入，系统覆盖 Painter 资产贴图绘制、Designer 程序化纹理、Sampler 数字化与 Stager 场景呈现；
  - 其软件版本老化点严格由 2026 Living Official Sources 予以升级修正。

### 2.2 PBR Theory Foundation（物理理论基石）
- **选定文献**：**Wes McDermott / Adobe —《The PBR Guide, Third Edition》(2018)**
- **决策状态**：`Selected PBR Theory Foundation`
- **核准依据与边界说明**：
  - 知识库中已完整收录 2018 年印刷第 3 版 PDF 全本；
  - 作为全球 CG 工业界最权威的微表面与能量守恒经典读物，为学生建立坚实的物理光学理论与金属/非金属反射率参数色阶（Reflectance Values Chart）；
  - 明确注明：属于底层稳定 PBR 理论源，而非 2026 软件操作版本事实源。

### 2.3 Material Observation / Photorealism / LookDev（质感观察与审美拔高）
- **选定文献**：**Eran Dinur —《The Complete Guide to Photorealism, 2nd Edition》(Routledge, 2026)**
- **决策状态**：`Selected Observation / LookDev Reference`
- **核准依据与边界说明**：
  - 承担三大角色：① 教师前两周理论讲义与色彩解构源泉；② 学生第 7–8 周渲染 LookDev“消除 CG 塑料感”的审美红宝书（倒角捕光、镜头色差、景深散景、胶片噪点）；③ 第 19 章作为生成式 AI 条件控制（ControlNet Depth/Normal）的视觉工作流拓展参考（photoreal generative-control / AI visual workflow reference）。

### 2.4 Procedural / Parametric Foundation（程序化材质基石）
- **选定组合**：**Shah Ch 7–10 + Adobe Substance 3D Designer 官方入门源 + Blender Shader Nodes / Principled BSDF**
- **决策状态**：`Selected bounded procedural foundation`
- **核准依据与边界说明**：
  - 满足本科 8 周建立“高度图驱动 (Height-driven)”、“多通道物理联动”与“参数化平铺去重复”的有限边界程序化思维；
  - 与 Blender 5.2/4.5 节点材质实现跨软件通识互通；
  - Designer 在课程整体中的最终课时占比与考核深度，按规定留待 Stage 2 Teaching Value Matrix 裁定。

### 2.5 Living Technical Authority（活体技术权威源）
- **选定组合**：**Substance 3D Painter 2026 官方文档/更新说明 + Designer 官方文档 + Sampler 官方文档 + Blender 官方手册 + ASWF OpenPBR 1.1.1 规范**
- **决策状态**：`Living technical authority`
- **修正核心事实**：
  - **Painter 12.1 (2026)**：带来独立 Baking Mode (F8) 视口重构、Paint Skew 法线偏斜涂抹修复，并正式将 **OpenPBR 1.1** 设定为默认工作流与着色器；
  - **Painter 12.0 (2026)**：带来 Warp to Geometry 几何体智能包裹投影算法与 Reload Mesh 无损网格重载工作流；
  - **Painter 11.1 (2025-11 引入)**：带来 Ribbon Path 曲线带状路径工具链与专用预设。

### 2.6 Chinese Student Companion（中文学生实操伴随）
- **推荐候选**：**郑琳 —《Substance 3D Painter游戏贴图绘制与材质制作》(清华大学出版社, 2024)**
- **决策状态**：`Preferred Chinese Student Companion Candidate / Optional Acquisition`
- **核准依据与采购约束**：
  - **绝不列为已获得或必买教材**；
  - Step 4B 事实审计表明其仅 127 页、聚焦 PBR+Painter 绘制，且具备上海师范大学天华学院等高校采用证据，若 User 只购买一册样书进行学生端中文实操支持验证，**郑琳优先于伍福军**；
  - 伍福军、张巧玲《Adobe Substance 3D Painter案例教程》(2024) 保持 `Secondary Chinese Candidate`，仅当郑琳资源不足或未来转向竞赛训练时再作评估；
  - 明确结论：中文教材采购属于可选验证项（optional future validation），不阻塞课程骨架定稿与后续 Stage 推进。

### 2.7 Teacher Graphics Reference（教师图形学参考）
- **选定文献**：**Tomas Akenine-Möller et al. —《Real-Time Rendering, 4th Edition (中英双语)》**
- **决策状态**：`Teacher Reference`
- **核准依据**：不作为学生核心教材，作为授课教师查阅微表面 BRDF 数学推导与光照算法的学术底座。

---

## 3. 最终教材与资源架构矩阵 (Final Course Resource Architecture)

```
+-----------------------------------------------------------------------------------+
|                        物理理论与质感观察 (Theory & Observation)                    |
|  - Eran Dinur《The Complete Guide to Photorealism》(2026, 2nd ed.)                  |
|    [Selected Observation / LookDev Reference]                                     |
|  - Wes McDermott / Adobe《The PBR Guide, 3rd ed.》(2018)                          |
|    [Selected PBR Theory Foundation]                                               |
|  - Akenine-Möller《Real-Time Rendering 4th (中英双语)》                             |
|    [Teacher Reference]                                                            |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                  主教材实操骨架 (Selected Primary Textbook Skeleton)                 |
|  - Zeeshan Jawed Shah《Realistic Asset Creation with Adobe Substance 3D》(2022)  |
|    (以 Retro TV 资产贯穿 Painter 绘制、Designer 基础节点、Sampler 与 Stager)         |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                  程序化基石 (Selected Bounded Procedural Foundation)               |
|  - Shah Ch 7–10 + Adobe Designer 官方文档 + Blender 5.2/4.5 Shader Nodes           |
|    (深度留待 Stage 2 Teaching Value Matrix 决定)                                  |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                     活体技术权威 (Living Technical Authority)                       |
|  - Painter 12.1 (2026): improved baking / skew painting / OpenPBR 1.1 default     |
|  - Painter 12.0 (2026): Warp to Geometry / improved mesh reimport                 |
|  - Painter 11.1 (2025-11): Ribbon Path 路径工具链                                 |
|  - Blender 5.2/4.5 LTS Principled BSDF & Shader Nodes (开源跨软件节点材质标准)     |
|  - ASWF OpenPBR 1.1.1 规范                                                        |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|           中文伴随教材候选 / 可选验证项 (Chinese Companion / Optional)              |
|  - 郑琳《Substance 3D Painter游戏贴图绘制与材质制作》(2024) [Preferred Candidate]  |
|  - 伍福军《Adobe Substance 3D Painter案例教程》(2024) [Secondary Candidate]       |
|    (购买属 User choice 可选验证，不阻塞课程设计)                                  |
+-----------------------------------------------------------------------------------+
```

---
*文档归档于 `docs/research/textbook-source-map.md`，由 Antigravity 自动化研究流水线基于 Course Knowledge Notebook 实证分析与 Browser 评审定稿。*
