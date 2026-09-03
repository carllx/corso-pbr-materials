# 《三维数字材质制作》教材与学习资源调研图谱 (Textbook & Learning Source Map)

> **研究阶段**：Stage 1 — Textbook Closeout / 教材定稿与知识资源获取 (Issue #2)  
> **审阅锚点**：基于 Course Knowledge Notebook (`e29f9644-03b2-4e1b-bcb0-b954b5bf08be`) 实际可访问 Corpus 实证分析  
> **核心原则**：课程核心严格限定为 **Material / Texture Authoring（材质与纹理创作）**，建模、雕刻、拓扑重构与高低模资产全流程仅作为支撑性前置输入，不反客为主成为主体。

---

## 1. 知识库实际资源清单与状态 (Verified Source Inventory)

经由 IDE 运行时对 Course Knowledge Notebook 进行全面核实与补充，当前已建立的实际可访问资源生态如下：

### 1.1 核心主教材与专著资产 (Core Acquired Textbooks)
- **Primary Textbook Skeleton**：
  - 《Realistic Asset Creation with Adobe Substance 3D》— Zeeshan Jawed Shah (Packt Publishing, 2022)
  - *Provenance*: PDF 已就绪 (`6a26e0ee-71de-43cf-be7f-c39d2ad2da43`)。
- **Observation & LookDev Reference / Teacher Reference**：
  - 《The Complete Guide to Photorealism: Understanding the Principles of Photorealistic CG and VFX, 2nd Edition》— Eran Dinur (Routledge, 2026)
  - *Provenance*: ePub 已就绪 (`72abf6ec-8c3d-4c9d-83f7-9e5a80f79e43`)。
- **PBR Theory Authority**：
  - 《The PBR Guide (Part 1: The Theory of PBR & Part 2: Practical Guidelines for Substance 3D Authors)》— Wes McDermott / Adobe
  - *Provenance*: Part 1 (`93dd34e7-d6ca-4f55-a5f6-3d4dfc2c6458`) 与 Part 2 (`3b740455-7c40-426d-aeb2-a25688cce706`) 均已就绪。
- **Graphics Foundation Reference**：
  - 《Real-Time Rendering, 4th Edition (中英双语)》— Tomas Akenine-Möller et al.
  - *Provenance*: 中文版 ePub (`447efad6-aad8-4f44-bf86-e60f54d7c57f`) 与英文版 ePub (`e3bc8e81-2fda-4d66-b4bd-4ffefb1448dd`) 均已就绪。

### 1.2 2026 持续演进官方技术体系 (Living Official Sources)
针对 Shah 2022 的版本时效性，通过 AdobeDocs 官方源文档与行业标准直连补齐 2026 权威：
- **Substance 3D Painter 2026**:
  - Painter Getting Started (`192ed109-2b3d-4c27-bfc4-5c4e87cdf3f1`)
  - Smart Materials & Masks (`c55c2489-0e56-4f9b-9298-fe26a650380e`)
  - Generators (`863d665c-74b8-408e-a594-e66677073a5a`)
  - Baking & How to Bake Mesh Maps (`2651bfb7-6cf0-4fa7-a990-5b7c374ea7ce`, `c7e2f3d1-1326-4bf4-8d64-1295a5166c38`)
  - Export & Output Templates (`2ef5d089-f272-490a-bff5-0e09531686b7`, `cacb0263-59d8-4414-9530-1965717c9020`)
  - All Changes Release Notes & 2026 Innovations (`3372381e-11d8-45c4-a0c7-a57490f9d8d9`, `76f4e622-e1d0-40da-acc2-80e97b3ccba4`)
- **Substance 3D Designer**:
  - Designer Getting Started & Workflow Overview (`53891efc-3d73-4a1b-995a-547461a2eb5a`, `07d44c9c-9e24-4ec1-8ca8-610fe1a4b7d8`)
- **Substance 3D Sampler / Material Acquisition**:
  - Sampler Image to Material (`32895b88-98e8-4e10-b192-a85398f2b8b4`)
  - Sampler Generative Workflows (`f8999918-65fc-4520-8957-f0999d72afdd`)
- **Blender / Open Standard**:
  - Blender 4.5/4.x Materials Intro, Shader Nodes & Principled BSDF (`e7660364-35b2-40e7-9edd-492c6dfc1e00`, `f3313ff9-aaf3-4814-bd0c-a91a97e93456`, `7e000672-195f-434d-8e1e-71d76f18d19a`)
  - ASWF OpenPBR 1.1.1 Specification (`32eb7bd7-aa57-4bfe-b291-d40d75f53095`)

### 1.3 期望但当前不可获取文献 (Desired but Currently Unavailable References)
保留在知识地图中作为教学思想对标，但不计入课程实际依赖：
- 《Substance 3D Painter実践講座―テクスチャの作り方・考え方を学ぶ》— CafeGroup (Born Digital, 2025)
- 《作例で学ぶ Substance 3D Designerの教科書》— もんしょ 等 (Born Digital, 2022)

---

## 2. 实际语料 Gap Analysis 与审查证据 (Gap Register)

基于 Course Knowledge Notebook 实际检索与交叉对比，对 6 大核心决策问题形成证据闭环：

### 2.1 Shah (2022) 承担 Primary Textbook Skeleton 的证据判断
- **结论**：**完全足以承担课程的主教材知识骨架**。
- **支撑证据**：
  1. *严格契合课程边界*：全书 0% 建模与拓扑教学，前言明确要求使用预制资产直接导入；
  2. *内容比重高度聚焦*：Substance 3D Painter 占 ~45% 篇幅，Designer 占 ~35%，Sampler 占 ~8%，Stager/Rendering 占 ~12%；
  3. *工业级实战技术完备*：全面覆盖 Texel Density、多 Texture Set 规划、顶点颜色烘焙 ID Map、Fill/Paint 层级堆叠、Tri-planar 投影、Smart Materials vs Materials 差异、Anchor Points（锚点非破坏性细节传递）、Position 贴图全场景归一化物理积灰，以及跨贴图集实例化（Instantiate Across Texture Sets）。

### 2.2 Shah (2022) 的 5 大版本老化点与 2026 Living Sources 修正对齐表
在保留 Shah 扎实主干的同时，大纲与讲义必须由 2026 Living Sources 修正以下 5 个技术断层：

| 教学模块 | Shah (2022) 过时操作/认知 | 2026 Living Sources 修正规范 | 教学执行方案 |
| :--- | :--- | :--- | :--- |
| **1. 烘焙模式** | 点击弹出旧版 `Pt Baking` 模态对话框，软件界面冻结，需手动调 Cage 距离 | **独立 Baking Mode (F8, Croissant 图标)**，视口实时显示 Implicit Cage，提供 **Paint Skew 偏斜视口涂抹工具** | 彻底废除手动拉扯 Cage 调歪斜的老方法，教学直接引入视口可视化烘焙与 Skew 笔刷修复法线 |
| **2. 着色器标准** | 默认采用旧版 Adobe Standard Material (ASM) 与标准 Metallic-Roughness | **OpenPBR 1.1 正式被设定为 Painter 12.1.0 默认工作流与着色器** | 新建工程统一采用 OpenPBR 1.1，与 Blender 4.x/5.x Principled BSDF 及 USD 工业管线 1:1 无缝对齐 |
| **3. 复杂曲面贴花** | 传统 2D 平面投影或旧版 Warp 投影，复杂曲面与孔洞处出现明显拉伸与淡出 | **Warp to Geometry（GDC 2026 几何体包裹算法）** | 贴花（Decals）与徽标教学直接使用网格动态自适应包裹，消除边缘形变 |
| **4. 规则细节绘制** | 依赖手工涂刷或 Stencil（印落模板）配合笔刷耗时涂抹缝线、焊缝 | **Ribbon Path（带状路径贝塞尔曲线工具链）**与 75 种专用预设 | 硬表面焊缝、铆钉、布料边饰全面改用 Ribbon 曲线绘制，单顶点控制宽度与透明度 |
| **5. 资产迭代流程** | 修改低模布线需经由复杂 Project Configuration 重映射 | **Painter 12.0 精简项目配置与专用 Reload Mesh（重载网格）** | 实训迭代采用无损重载低模，保留全部图层与烘焙缓存 |

### 2.3 缺失 CafeGroup 2025 是否导致 Material Thinking 教学断层？
- **结论**：**否，完全不会构成断层**。
- **支撑证据**：
  - Eran Dinur (2026)《The Complete Guide to Photorealism》提供了更深、更具世界级视角的物理逆向拆解框架（人眼 vs 相机、六层色彩拆解模型、自然光米氏/瑞利散射、次表面微缺陷）；
  - Adobe《The PBR Guide (Part 1&2)》划定了严格的光能守恒与材质安全色阶（Albedo Ranges）；
  - Shah (2022) 第 3–6 章清晰落实了“底材 $\rightarrow$ 漆面 $\rightarrow$ 拐角磨损 (Curvature) $\rightarrow$ 死角藏污 (AO) $\rightarrow$ 表面重力沉降积灰 (Position)”的物理分层落地；
  - “Dinur 审美眼界 + PBR Guide 数据边界 + Shah 工业实操”已形成闭环，无需依赖日系教材。

### 2.4 缺失 576 页日本 Designer 大部头教材是否导致 Procedural 教学缺口？
- **结论**：**否，非但不是缺口，反而是对本科 8 周认知负荷的科学控制**。
- **支撑证据**：
  - 8 周课程无法也不应塞入几百个数学算子与复杂函数图，否则极易导致普通本科生产生节点畏难情绪；
  - 本科阶段真正需要的“程序化材质思维”为三大支柱：**高度图驱动 (Height-Driven)**、**多通道物理联动**、**参数化平铺去重复**；
  - Shah Ch 7–10 涵盖了 Tile Generator、Flood Fill、Height Blend、Histogram Scan 等核心节点及完整电视机架实战，与 Blender 现代 Shader Nodes / 节点材质完全互通，深度刚刚好。

### 2.5 中文实训缺口评估与购买必要性决议
- **结论**：**存在客观的语言与界面执行力缺口，但无需额外付费购买国内教材**。
- **支撑证据与权衡**：
  - *国内教材硬伤*：出版周期长导致技术严重滞后（普遍无 F8 烘焙视口、Paint Skew、OpenPBR 1.1、Ribbon Path），且多为“参数食谱式”点击，缺乏底层思维；
  - *零成本最佳解决方案*：Adobe 官方已提供 100% 汉化且持续更新的官方中文文档；教师在备课时利用官方中文对照，自制一份 5–10 页的《8周中文实训界面对照与避坑指南 (Cheat Sheet)》（点对点对照中英文菜单与节点名称），即可彻底解决学生上机操作障碍。

### 2.6 《The Complete Guide to Photorealism》(2026) 的课程角色定位
- **定位**：**教师备课讲义源泉 + 学生 LookDev 拔高读物 + 前沿 AI 探索指南**。
  - *教师端*：主导前两周光学物理、色彩解构与质感观察理论课件；
  - *学生端*：第 7–8 周 LookDev/渲染阶段指导学生添加倒角高光与镜头缺陷（色差、散景、Film Grain）以消除“CG 塑料感”；
  - *前沿拓展*：第 19 章指导学生使用 ComfyUI + ControlNet (Depth/Normal) 引导生成无缝 PBR 贴图。

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

## 4. 最终教材与资源架构矩阵 (Final Course Resource Architecture)

```
+-----------------------------------------------------------------------------------+
|                            课程理论与审美顶层 (Theory & Vision)                      |
|  - Eran Dinur《The Complete Guide to Photorealism》(2026, 2nd ed.)                  |
|  - Wes McDermott / Adobe《The PBR Guide (Part 1 & 2)》                             |
|  - Akenine-Möller《Real-Time Rendering 4th (中英双语)》 (教师理论底座)              |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                        课程主干实操骨架 (Primary Textbook Skeleton)                   |
|  - Zeeshan Jawed Shah《Realistic Asset Creation with Adobe Substance 3D》(2022)  |
|    (以 Retro TV 道具为核心实战，贯穿 Painter 绘制、Designer 节点、Sampler 与 Stager)  |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                       2026 规范与工具升级 (Living Official Sources)                 |
|  - Substance 3D Painter 2026 (OpenPBR 1.1 默认规范、F8 Baking Mode、Paint Skew、    |
|    Warp to Geometry、Ribbon Path 路径工具链、无损 Reload Mesh)                     |
|  - Blender 4.5/4.x Principled BSDF & Shader Nodes (开源跨软件节点材质标准)         |
|  - Adobe Substance 3D 官方汉化帮助手册 (提供中文界面对照)                            |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                         本土实训落地支撑 (Practical Companion)                      |
|  - 教师自制《8周中文实训界面对照与避坑指南 (Cheat Sheet)》(免额外商业教材采购)        |
+-----------------------------------------------------------------------------------+
```

---
*文档归档于 `docs/research/textbook-source-map.md`，由 Antigravity 自动化研究流水线基于 Course Knowledge Notebook 实际语料实证生成。*
