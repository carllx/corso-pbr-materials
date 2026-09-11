# Source-Native Knowledge Index: Shah (2022), The PBR Guide (2018) & Dinur (2026)

> **审计状态声明（Gate 2.5A Deliverable）**：
> 本文档是严格遵循 **Gate 2.5A** 要求自下而上建立的“教材一手知识索引”（Source-First Artifact）。
> 
> * **绝对遵循准则**：仅基于 Course Knowledge Notebook (`e29f9644-03b2-4e1b-bcb0-b954b5bf08be`) 内真实教材源（Shah 2022 `6a26e0ee-71de-43cf-be7f-c39d2ad2da43`、The PBR Guide `7b3dde6d-a06c-42b1-9814-3bed5617c315` 与 Dinur 2026 `72abf6ec-8c3d-4c9d-83f7-9e5a80f79e43`）的 Direct Retrieval 与提取文本。
> * **不采用任何二手证据**：绝不引用旧 transcript、旧 task log、`curriculum-coverage-matrix.md`、`textbook-source-map.md` 或现有 draft 作为事实证据。
> * **严禁凭空拟造页码**：所有章节名称、层级标题与页码均来自于教材正文目录（TOC）与正文检索。针对 EPUB 源（Dinur 2026），已严格验证正文内嵌的实体印刷页码标识（Inline Print Page Markers, pp. 1–230），并附注 NotebookLM source pointer。
> * **严格区分一手事实与归纳总结（Source Interpretation Discipline）**：每项条目严格归入以下四类之一，严禁将归纳措辞、代数推演或工具总结伪装为作者原生术语：
>   1. `EXPLICITLY TAUGHT`：教材正文明确给出概念定义、公式、参数原理或系统性讲授的内容；
>   2. `PRACTICALLY DEMONSTRATED`：教材未提供形式化理论定义，而是通过具体软件操作步骤与案例进行示范的实践技能；
>   3. `MENTIONED / USED ONLY`：教材仅在界面中掠过、使用默认预设或仅作为已知前提提及，未做深入教学；
>   4. `INTERPRETIVE SUMMARY`：对教材工作流的概括性归纳、补充性数学化表达或跨教材总结；若涉及未在正文明确给出的数学代数推演，必须注明 `INTERPRETIVE SUMMARY — independent math verification required`。

---

## 目录

1. [Source 1: Zeeshan Jawed Shah (2022) - Material-Relevant Extraction (Ch 1–11 of 16)](#source-1-zeeshan-jawed-shah-2022)
   - [Chapter 1: Getting Started with Adobe Substance 3D Painter](#ch-1-getting-started-with-adobe-substance-3d-painter-pp-133)
   - [Chapter 2: Working with Assets in Adobe Substance 3D Painter](#ch-2-working-with-assets-in-adobe-substance-3d-painter-pp-3562)
   - [Chapter 3: Working with Layers and Maps in Adobe Substance 3D Painter](#ch-3-working-with-layers-and-maps-in-adobe-substance-3d-painter-pp-63102)
   - [Chapter 4: Working with Masks in Adobe Substance 3D Painter](#ch-4-working-with-masks-in-adobe-substance-3d-painter-pp-103116)
   - [Chapter 5: Working with Advanced Tools in Adobe Substance 3D Painter](#ch-5-working-with-advanced-tools-in-adobe-substance-3d-painter-pp-117151)
   - [Chapter 6: Working with Materials and Smart Materials in Adobe Substance 3D Painter](#ch-6-working-with-materials-and-smart-materials-in-adobe-substance-3d-painter-pp-153203)
   - [Chapter 7: Getting Started with Adobe Substance 3D Designer](#ch-7-getting-started-with-adobe-substance-3d-designer-pp-205245)
   - [Chapter 8: Nodes in Adobe Substance 3D Designer](#ch-8-nodes-in-adobe-substance-3d-designer-pp-247294)
   - [Chapter 9: Blending Modes in Adobe Substance 3D Designer](#ch-9-blending-modes-in-adobe-substance-3d-designer-pp-295320)
   - [Chapter 10: Creating a Television Shelf in Adobe Substance 3D Designer](#ch-10-creating-a-television-shelf-in-adobe-substance-3d-designer-pp-321366)
   - [Chapter 11: Adobe 3D Sampler at a Glance](#ch-11-adobe-3d-sampler-at-a-glance-pp-367401)
   - [Shah (2022) 教学范围与未教授盲区总结](#shah-2022-教学范围与未教授盲区总结)
2. [Source 2: Wes McDermott - The PBR Guide (2018, 3rd Edition)](#source-2-wes-mcdermott---the-pbr-guide-2018-3rd-edition)
   - [文献版本与结构概览](#文献版本与结构概览)
   - [Part 1: The Theory of Physically Based Rendering and Shading](#part-1-the-theory-of-physically-based-rendering-and-shading-pp-1840)
   - [Part 2: Practical Guidelines for Creating PBR Textures](#part-2-practical-guidelines-for-creating-pbr-textures-pp-4588)
   - [Appendix: PBR Charts & Comparisons](#appendix-pbr-charts--comparisons-pp-8992)
3. [Source 3: Eran Dinur (2026) - Material-Relevant Extraction (8 Chapters of 19)](#source-3-eran-dinur-2026)
   - [文献版本与范围界定说明](#文献版本与范围界定说明)
   - [Chapter 1: Reality and Photorealism (pp. 9–21)](#ch-1-reality-and-photorealism-pp-921)
   - [Chapter 3: Color (pp. 32–48)](#ch-3-color-pp-3248)
   - [Chapter 5: Light Interaction (pp. 57–68)](#ch-5-light-interaction-pp-5768)
   - [Chapter 9: Basic Material Properties (pp. 92–96)](#ch-9-basic-material-properties-pp-9296)
   - [Chapter 11: Rendering and Lighting (pp. 113–130)](#ch-11-rendering-and-lighting-pp-113130)
   - [Chapter 12: Shading (pp. 131–142)](#ch-12-shading-pp-131142)
   - [Chapter 13: Texturing (pp. 143–156)](#ch-13-texturing-pp-143156)
   - [Chapter 19: Photorealism with Generative AI (pp. 207–227)](#ch-19-photorealism-with-generative-ai-pp-207227)
   - [Dinur (2026) 教学范围与未教授盲区总结](#dinur-2026-教学范围与未教授盲区总结)
4. [Source Complementarity and Coverage Boundaries](#source-complementarity-and-coverage-boundaries)

---

## Source 1: Zeeshan Jawed Shah (2022)

* **书名**：*Realistic Asset Creation with Adobe Substance 3D: Create materials, textures, filters, and 3D models using Substance 3D Painter, Designer, and Stager*
* **作者**：Zeeshan Jawed Shah
* **出版年份**：2022 (Packt Publishing)
* **Paperback ISBN-13**：`9781803233406`
* **eBook ISBN**：`9781803240206`
* **总页数**：486 pages
* **全书结构**：16 chapters
* **提取范围说明**：`Material-relevant source-native extraction: Chapters 1–11 of 16`（聚焦于 Substance 3D Painter, Designer 与 Sampler 材质与纹理制作，未抽取后续 Stager/三维排版及渲染章节；全书共 16 章）。

---

### Ch 1: Getting Started with Adobe Substance 3D Painter (pp. 1–33)

#### 原生章节目录与页码
* Technical requirements (p. 2)
* What is texel density? (pp. 3–6)
* Creating texture lists and ID maps in Adobe Substance 3D Painter (pp. 7–26)
  * Creating texture sets (pp. 7–16)
  * Creating ID maps with vertex color (pp. 17–26)
* Baking textures in Adobe Substance 3D Painter (pp. 26–33)
* Summary (p. 33)

#### 知识分类解析
1. **EXPLICITLY TAUGHT（显式讲授与概念定义）**：
   * **Texel Density（纹素密度）**（pp. 3–6）：显式定义纹素与世界坐标尺寸比例概念，解释分辨率均衡的重要性。
   * **Texture Sets（纹理集机制）**（pp. 7–16）：定义 Texture Set List 面板在多材质模型管理中的角色与视口通道孤立功能。
   * **ID Maps via Vertex Color（顶点色 ID 图）**（pp. 17–26）：解释如何在 Maya 中分配顶点着色（Color Set / Vertex Color），并在 Painter 中作为遮罩隔离依据。
   * **Baking Mesh Maps（烘焙网格贴图）**（pp. 26–33）：明确解释 7 种核心 Mesh Maps 的物理与空间用途（Normal, World Space Normal, Curvature, Position, Thickness, Ambient Occlusion, ID）。
2. **PRACTICALLY DEMONSTRATED（手把手软件演练）**：
   * 在 Maya 中检查模型顶点色与分块。
   * 在 Painter 中导入带顶点色与多材质球的 `Retro_Tv.FBX` 资产。
   * 打开 Baking 对话框，配置烘焙参数（烘焙分辨率、High Poly 网格配置、射线距离、采样）。
   * 成功烘焙出全套网格贴图并检查。
3. **MENTIONED / USED ONLY（仅提及使用，未深入教学）**：
   * **PBR 物理着色底层方程**：直接套用软件默认的 Metallic/Roughness 着色器模板，完全未解释 Fresnel、微表面散射或 BRDF。
   * **UV 拆分与展开算法**：直接使用已有 UV 的模型，未讲授 UV 展开技巧。
   * **Maya 导出管线参数细节**：未深入探讨 FBX 导出版本兼容性及 Tangent/Binormal 勾选项的数学影响。

---

### Ch 2: Working with Assets in Adobe Substance 3D Painter (pp. 35–62)

#### 原生章节目录与页码
* Familiarizing ourselves with the Assets panel (pp. 35–37)
* Importing resources and creating custom tabs in the Assets panel (pp. 38–51)
  * Importing resources (pp. 38–44)
  * Creating custom tabs inside the Assets panel (pp. 45–51)
* Understanding the different types of assets in the Assets panel (pp. 51–53)
* Applying assets to 3D meshes (pp. 53–62)
  * Using normal maps to apply assets (pp. 53–54)
  * Changing the Brush attributes (pp. 55–57)
  * Using alpha maps to apply assets (pp. 58–61)
* Summary (p. 62)

#### 知识分类解析
1. **EXPLICITLY TAUGHT**：
   * **Assets Panel 资产结构**：明确划分 Materials, Smart Materials, Smart Masks, Filters, Brushes, Alphas, Textures, Environments 资产类型。
   * **导入范围域生命周期**：当前会话（Current Session）、项目（Project）、全局货架（Library/Assets）的区别。
   * **Alpha 通道与 Height 浮雕映射**：解释 Alpha 灰度值（-1 到 +1）如何直接在画笔通道中转化为深度凹凸。
2. **PRACTICALLY DEMONSTRATED**：
   * 导入自定义 Normal 贴图与 Alpha 图片并分配标签（Tags）。
   * 创建 Custom Tabs 整理特定项目资产。
   * 使用 Basic Hard 笔刷，绑定 Alpha 图案在电视表面涂刷浮雕效果。
   * 将 Normal 印章贴图赋予笔刷 Normal 槽，直接在无几何细分的表面压印螺丝与凹槽细节。
3. **MENTIONED / USED ONLY**：
   * **SBSAR 格式内部结构**：仅作为预打包材质直接使用，未解释其由 Designer 生成的原理。
   * **环境贴图 HDR 采样格式**：直接拖拽预置 HDR 环境球，未深入色温、照度值与色彩位深。

---

### Ch 3: Working with Layers and Maps in Adobe Substance 3D Painter (pp. 63–102)

#### 原生章节目录与页码
* Understanding the layer stack in Adobe Substance 3D Painter (pp. 64–69)
  * Type of layers (pp. 64–65)
  * Paint layer (p. 65)
  * Viewmode (p. 66)
  * Actions (pp. 66–69)
* Applying materials to 3D models and meshes in Adobe Substance 3D Painter (pp. 69–75)
  * UV projection (p. 71)
  * Fill (match per UV Tile) (p. 71)
  * Tri-planar projection (p. 72)
  * Planar projection (p. 72)
  * Spherical projection (p. 72)
  * Cylindrical projection (p. 72)
  * Warp projection (p. 72)
* Applying materials on 3D models using ID maps in Adobe Substance 3D Painter (pp. 75–89)
* Creating LED lights in Substance Painter (pp. 89–93)
* Creating a television screen in Adobe Substance Painter (pp. 93–102)
* Summary (p. 102)

#### 知识分类解析
1. **EXPLICITLY TAUGHT**：
   * **图层堆栈计算机制（Layer Stack Rendering）**：从底层至顶层逐层计算渲染，支持混合模式与通道独立调整。
   * **图层类型区分**：Paint Layer（位图手绘图层，带通道像素）、Fill Layer（参数化填充图层，由属性面板全局驱动）、Folder（文件夹组织）。
   * **通道隔离视口显示（Viewmode）**：快捷键 `C` 轮询各单通道（Base Color, Roughness, Metallic, Normal, Height），快捷键 `M` 返回完整材质（Material）视图。
   * **图层效果（8 种 Actions）**：Add generator, Add paint, Add fill, Add levels, Add compare mask, Add filter, Add color selection, Add anchor point。
   * **6 大投影模式详解**：UV projection, Tri-planar projection（三平面投射，带 Hardness 平滑过渡防拉伸）, Planar, Spherical, Cylindrical, Warp。
   * **自发光通道（Emissive Channel）**：如何在 Texture Set Settings 中手动激活软件默认未启用的 Emissive 通道，并在材质中赋予发光强度。
2. **PRACTICALLY DEMONSTRATED**：
   * 在 `TV_Middle_Casing` 上赋予 `Black_Plastic` 材质，配置三平面投影与锁长宽比缩放。
   * 在 Texture Set Settings 添加 Emissive 通道。
   * 为电视前置面板的 LED 信号灯创建自发光红/绿微弱光晕效果。
   * 为电视屏幕制作玻璃内凹与复古显像管扫描线底纹。
   * 使用 Add color selection 拾取 ID 贴图色块，精准限定图层作用区域。
3. **MENTIONED / USED ONLY**：
   * **Post-processing 辉光渲染物理方程**：开启视口 Bloom 效果增强发光质感，但未讲解光晕阈值与色散物理。
   * **通道混合的数学矩阵**：仅演示在图层上选 Multiply/Overlay，未展开通道代数原理。

---

### Ch 4: Working with Masks in Adobe Substance 3D Painter (pp. 103–116)

#### 原生章节目录与页码
* Creating complex masks in Adobe Substance 3D Painter (pp. 103–111)
* Creating planar masks in Substance Painter (pp. 111–116)
* Summary (p. 116)

#### 知识分类解析
1. **EXPLICITLY TAUGHT**：
   * **复杂遮罩堆叠（Complex Mask Stacks）**：Black Mask（全黑反向蒙版）作为载体，嵌套多个 Fill Effect 载入位图噪波（`grunge rough dirty`）。
   * **Planar Masking（平面裁剪遮罩机制）**：三维视口投影操作，空间对齐与切片。
   * **Depth Culling（深度剔除）**：限制投射厚度，防止投影穿透模型或在垂直侧面产生拖尾拉伸。
   * **Backface Culling（背面剔除）**：剔除表面法线与投影方向夹角大于 90° 的面，避免背面出现幽灵重影。
2. **PRACTICALLY DEMONSTRATED**：
   * 在电视中壳上建立磨损反光图层，添加 Black Mask。
   * 在蒙版上叠加 Add fill 效果并引入脏迹贴图，调整对比度实现局部高光剥蚀。
   * 激活 Planar Mask，使用操纵杆在 3D 视口对准电视侧壁，精确设定 Depth 与 Backface Culling 切出分界线。
3. **MENTIONED / USED ONLY**：
   * **Generator Mask**：第四章特意将 Generator 留给后文，本章专注于位图灰度填充与视口空间平面裁切。
   * **手绘涂抹蒙版**：未在本章使用手绘 Paint Mask。

---

### Ch 5: Working with Advanced Tools in Adobe Substance 3D Painter (pp. 117–151)

#### 原生章节目录与页码
* Applying bitmap textures in Adobe Substance 3D Painter (pp. 117–123)
* Creating a 3D logo from scratch in Adobe Substance 3D Painter (pp. 123–128)
* Making a custom brush in Adobe Substance 3D Painter (pp. 128–137)
* Working with stencils and projection in Adobe Substance 3D Painter (pp. 137–144)
* Using text, fonts, and the Clone and Smudge tools in Adobe Substance 3D Painter (pp. 144–150)
* Summary (p. 151)

#### 知识分类解析
1. **EXPLICITLY TAUGHT**：
   * **Stencil（手绘印花模板）**：视口屏幕空间锁定遮罩原理，快捷键操作流（`S` + 左键旋转、`S` + 右键等比缩放、`S` + 中键平移）。
   * **3D/2D 分屏视口绘制（F1 切换）**：利用 2D UV Tiles 平整无形变特性，在平展开的 UV 瓦片上绘制 Stencil，避免 3D 起伏曲面拉伸。
   * **Brush Tool Preset 打包**：配置好 Color, Roughness, Metallic, Height, Normal 后，在笔刷图标右键 `Create tool preset` 存入资产货架。
   * **Clone Tool（克隆仿制图章）**：明确区分 Absolute（绝对坐标）与 Relative（相对坐标）采样模式，快捷键 `V` + 左键点击拾取源点。
   * **Smudge Tool（涂抹工具）**：对已存在图层通道像素进行物理拖拽位移，模拟流痕、融化及风化腐蚀边缘。
   * **Text & Font Stencil 绘制**：将内置矢量字体 `Font Libre Baskerville` 放入画笔 Stencil 槽，配置 Text, Size, Alignment 参数进行印盖。
2. **PRACTICALLY DEMONSTRATED**：
   * 在电视后盖局部导入电路板贴图 `servlet.jpg`，通过 ID 蒙版限制在绿色接口槽，微调 UV Scale/Offset 完成对齐。
   * 制作 3D 浮雕金属 Logo（EMINEM）：Height = 1, Roughness = 0.22, Metallic = 1，三平面投影对齐左下角。
   * 制作螺丝印章笔刷（Screw Stamp Brush）：载入内置法线图 `Screw Cross Round` 并保存为 Tool Preset。
   * 在 F1 分屏视口的 2D 瓦片上，使用 Stencil 绘制绿色 Substance Pt 图标。
   * 盖印 "Made in Substance" 字体，用 Clone 工具在下方复制副本，再用 Smudge 工具拉扯边缘模拟老旧斑驳风化痕迹。
3. **MENTIONED / USED ONLY**：
   * **克隆工具在 UV 缝合线跨缝映射的数学限制**：实操避开了接缝，未讲解跨接缝克隆时的向量插值。
   * **外部矢量字体（TTF/OTF）编译**：仅调用内置字体，未讲解外置字体的装载机制。
4. **重大发现（教材实际未覆盖）**：
   * ❌ **Geometry Mask（几何体蒙版）**：**全章乃至全书完全未提及**（2022 年书写时尚未将其作为实战核心）。
   * ❌ **Symmetry Tool（对称工具）**：**全书此章完全未提及**，无对称绘制教学。

---

### Ch 6: Working with Materials and Smart Materials in Adobe Substance 3D Painter (pp. 153–203)

#### 原生章节目录与页码
* Creating a material or Smart Material from scratch in Adobe Substance 3D Painter (pp. 154–163)
* Creating a material or Smart Material from an existing material in Adobe Substance 3D Painter (pp. 163–170)
* Applying stickers and decals in Adobe Substance 3D Painter (pp. 170–175)
* Adding an overall layer effect with the position map in Adobe Substance 3D Painter (pp. 176–181)
  * Adding an anchor point (pp. 176–181)
* Using Position maps to add an overall dust effect on multi-Texture Set 3D models and 3D meshes (pp. 181–189)
* Exporting textures from Adobe Substance 3D Painter (pp. 190–195)
* Rendering in Adobe Substance 3D Painter using Iray (pp. 195–202)
* Summary (p. 203)

#### 知识分类解析
1. **EXPLICITLY TAUGHT**：
   * **Smart Materials 原理与结构**：对比普通 Material（单一材质预设）与 Smart Material（`.spsm` 复合图层包），解释智能材质如何依赖烘焙的网格贴图（Curvature, AO, Position）自适应贴合不同模型。
   * **Anchor Points（锚点联动机制）**：将底层图层/蒙版的信息（如手绘高度、滤镜模糊）暴露为锚点，供上层图层通过 Fill 效果或 Generator 跨图层调用，实现非破坏性双向联动。
   * **Position Map 全局落灰（Multi-Set Dust Effect）**：利用场景空间 Y 轴渐变，配合 `Instantiate across texture sets`（跨纹理集实例化），在多纹理集模型上生成统一沉降灰尘。
   * **贴图导出位深建议（Export Bit Depths Workflow）**：Shah 在其实操流程中演示与推荐的导出设置中，Normal/Height 贴图指定为 16-bit 以减少阶梯断层伪影，Base Color/Roughness 指定为 8-bit（此为 Shah 演示/推荐的导出设置，而非跨引擎的通用绝对法则）。
   * **Iray 离线写实渲染流程**：地面贴合（Ground plane 勾选与 Y 轴偏移）、HDRI 旋转（`Shift` + 右键拖拽）、景深（DOF Aperture 0.5，`Ctrl/Cmd` + 中键拾取焦平面）、色彩校正与炫光（Glare, Vignette）。
2. **PRACTICALLY DEMONSTRATED**：
   * 从零搭建包含磨损边缘的金属与塑料智能材质并导出至货架。
   * 贴花与贴纸（Decals）：设置 Height = 0.02、Roughness = 0.1497、Metallic = 0.1463，使用快捷键旋转/等比缩放盖印。
   * 锚点实战：在 TV Logo 蒙版上添加 Blur 滤镜与 Levels，创建 `TV Logo mask` 锚点；新建图层仅开启 Height=1，引用该锚点实现双重高度浮雕。
   * 全局落灰：Position Generator 结合 `Grunge Dust Spread` 噪波，跨所有纹理集实例化，统一降低透明度至 50%。
   * 导出贴图：选择 `Substance 3D Stager` 输出模板，Padding 设置为 `Dilation infinite`，分辨率 4096×4096。
   * Iray 渲染：设置采样阈值、地面高度、相机景深与调色参数并输出渲染图。
3. **MENTIONED / USED ONLY**：
   * **Path Tracing 光线追踪数学算法**：演示了采样点逐步收敛过程，未展开蒙特卡洛积分理论。
   * **自定义通道打包导出模板的脚本编写**：直接使用预设模板导出，未深入讲解自定义 Output Template 内部通道打包语法。

---

### Ch 7: Getting Started with Adobe Substance 3D Designer (pp. 205–245)

#### 原生章节目录与页码
* Substance Designer panels (pp. 206–210)
* The Adobe Substance 3D Designer EXPLORER window (pp. 210–226)
  * Creating and closing a new package (pp. 210–212)
  * Creating and closing Substance graphs (pp. 212–214)
  * Importing and linking resources (pp. 214–217)
  * Deleting the resources (pp. 217–219)
  * Saving packages (pp. 219–222)
  * Exporting nodes as separate images (pp. 222–224)
  * Exporting Substance 3D Asset files (pp. 224–226)
* Adobe Substance 3D Designer GRAPH window (pp. 227–238)
  * Atomic nodes (pp. 227–229)
    * Placing atomic nodes (pp. 227–229)
  * Links (pp. 229–230)
  * Disabling nodes (pp. 230–232)
  * Manipulating 2D and 3D views (pp. 232–233)
  * Graph view toolbar (pp. 233–236)
    * Main toolbar (pp. 233–235)
    * Node toolbar (p. 235)
    * Parent toolbar (pp. 235–236)
  * The Substance Designer PROPERTIES panel (pp. 236–238)
* Substance Designer 2D and 3D views (pp. 238–243)
  * 2D VIEW (pp. 238–242)
  * 3D VIEW (pp. 242–243)
* The Substance Designer LIBRARY panel (pp. 243–245)
  * The Categories section (p. 244)
  * The Content section (pp. 244–245)
* Summary (p. 245)

#### 知识分类解析
1. **EXPLICITLY TAUGHT**：
   * **包（Package）与图表（Graph）关系**：一个 `.sbs` 资源包内可容纳多个独立的 Substance Graphs，支持资源内嵌（Import）与外部链接（Link）。
   * **Atomic Nodes 基础定位**：底层硬编码原子节点，无法双击展开内部网络，是构筑所有复合逻辑的基石。
   * **节点连接端口语法**：灰色端口代表单通道灰度（Grayscale），黄色端口代表 4 通道彩色（Color），黄灰相间代表兼容双输入；不同类型直接相连会出现红色虚线报错。
   * **资产发布（Publish SBSAR）**：如何将 `.sbs` 源文件编译发布为通用的 `.sbsar` 格式以供 Painter/Stager 跨软件调用。
2. **PRACTICALLY DEMONSTRATED**：
   * 新建空 Package，基于 Metallic Roughness 模板创建新 Graph。
   * 导入外部位图 `logo.png` 并拖入 Graph 视口。
   * 节点连接、断开、禁用（Disable 状态切换）、导出节点为独立图像文件。
3. **MENTIONED / USED ONLY**：
   * **MDL Graphs**：界面有选项但未教学。
   * **相对父级分辨率算法（Relative to Parent）**：勾选继承父级，但未深入分辨率倍率计算体系。

---

### Ch 8: Nodes in Adobe Substance 3D Designer (pp. 247–294)

#### 原生章节目录与页码
* Working with nodes and understanding the basics in Adobe Substance 3D Designer (pp. 248–261)
  * Atomic nodes (pp. 258–259)
  * Library nodes (pp. 259–261)
* The Tile Generator node (pp. 261–265)
* The Flood Fill node (pp. 265–269)
* The Quad Transform node (pp. 269–273)
* The Height Blend node (pp. 273–276)
* The Curve node (pp. 276–279)
* The Dirt and Dust nodes (pp. 279–285)
* The Shape Mapper node (pp. 286–288)
* The Shape Splatter node (pp. 288–293)
* Histogram Scan (pp. 293–294)
* Summary (p. 294)

#### 知识分类解析
1. **EXPLICITLY TAUGHT**：
   * **原子节点 vs 复合库节点**：Atomic nodes（Blend, Uniform Color, Bitmap, Levels, Normal, Curve, Output 等）不可进入内部；Library nodes（Tile Generator, Dirt, Blur HQ 等）是官方基于原子节点封装的复合图。
   * **灰度与彩色类型处理规范（Grayscale vs. Color Handling）**：作者强调灰度计算开销低于彩色，演示了使用 `Gradient Map` 将灰度信息映射为彩色、使用 `Grayscale Conversion` 将彩色转为灰度的工作流。
   * **核心节点功能与参数**：
     * `Tile Generator`：程序化阵列生成器（控制 X/Y 数量、偏移 Offset Random、间距与形变）。
     * `Flood Fill`：连通域分析节点，为分割区域赋予独立索引，配合 `Flood Fill to Random Grayscale` / `Gradient` 产生随机高度或倾角。
     * `Height Blend`：根据高度深度优先关系混合两套高度图，同时输出混合蒙版。
     * `Curve`：贝塞尔曲线精确重映射，用于打磨边缘剖面（Bevel Profile）与缝隙切割。
     * `Dirt / Dust`：依赖 Normal、Curvature、AO 网格贴图的物理积垢与天顶落灰节点。
     * `Histogram Scan`：通过 Position 与 Contrast 快速扩展或收缩灰度蒙版边缘。
2. **PRACTICALLY DEMONSTRATED**：
   * **完整程序化红砖墙案例（Procedural Brick Wall）**：
     * 使用 `Plane (hi-res)` 并开启 Tessellation Displacement（细分系数 16）。
     * 搭建 Tile Generator 生成交错砖块（X=5, Y=15, Offset=0.5）。
     * 接入 Flood Fill，生成随机构件高度并倾斜砖块表面。
     * 使用 Curve 节点修整砖缝，消除模糊过渡。
     * 从外部真实照片使用 `Pick Gradient` 拾取自然真实色阶驱动 Gradient Map。
     * 计算 HBAO 与 Curvature，接入 Dirt 节点在砖缝积灰，完成 Base Color, Normal, Roughness 输出。
3. **MENTIONED / USED ONLY**：
   * **Tessellation vs Parallax Occlusion 视口算法原理**：仅做视口选项切换，未解释着色器底层实现。
   * **Pixel Processor / Function Graphs**：仅在界面节点列表中掠过，**完全未教授数学自定义函数**。

---

### Ch 9: Blending Modes in Adobe Substance 3D Designer (pp. 295–320)

#### 原生章节目录与页码
* Understanding the Transformation 2D node, the Levels node, and the grayscale height values (pp. 296–304)
  * Transformation 2D (pp. 296–298)
  * The Levels node (pp. 298–301)
  * Grayscale height values (pp. 301–304)
* The Copy blending mode (pp. 305–307)
* The Add and Subtract blending modes (pp. 307–308)
* The Min (darkened) and Max (lightened) blending modes (pp. 308–310)
* The Multiply and Divide blending modes (pp. 310–312)
* The Screen and Soft Light blending modes (pp. 312–314)
* The Add Sub and Overlay blending modes (pp. 314–317)
* The Switch blending mode (pp. 317–320)
* Summary (p. 320)

#### 知识分类解析
1. **EXPLICITLY TAUGHT（原书明确讲授与行为定义）**：
   * **逐像素归一化计算**：所有混合模式均在 `[0, 1]` 归一化区间内对输入像素进行操作，输出数值钳位（Clamped）在 `[0, 1]`。
   * **交换律文本分类（Commutative vs. Non-commutative）**：作者正文明确且贯穿使用 `commutative`（交换 Foreground 与 Background 连接不影响输出结果）与 `non-commutative`（交换连接顺序会改变输出结果）术语对全部 12 种模式进行定性分类：
     1. **Copy**（pp. 305–307）：前景直接覆盖背景（Non-commutative）。
     2. **Add**（pp. 307–308）：前景与背景像素数值相加，溢出 1 的部分被截断（Commutative）。
     3. **Subtract**（pp. 307–308）：从背景像素数值中减去前景数值，低于 0 被截断（Non-commutative）。
     4. **Min (Darken)**（pp. 308–310）：逐像素比较两层并保留较小/较暗的数值（Commutative）。
     5. **Max (Lighten)**（pp. 308–310）：逐像素比较两层并保留较大/较亮的数值（Commutative）。
     6. **Multiply**（pp. 310–312）：前景与背景像素数值相乘，整体变暗（Commutative）。
     7. **Divide**（pp. 310–312）：背景数值除以前景数值，产生提亮效果（Non-commutative）。
     8. **Screen**（pp. 312–314）：概念上先反转两层像素数值、相乘后再反转，实现防过曝的提亮（Commutative）。
     9. **Soft Light**（pp. 312–314）：柔光对比混合，根据输入亮度产生平滑的提亮或压暗（Non-commutative）。
     10. **Add Sub**（pp. 314–317）：以 0.5 为基准阈值，大于 0.5 提亮/相加，小于 0.5 压暗/相减（Non-commutative）。
     11. **Overlay**（pp. 314–317）：组合正片叠底与滤色，底层像素低于 0.5 时应用 Multiply，高于 0.5 时应用 Screen（Non-commutative）。
     12. **Switch**（pp. 317–320）：依靠 Opacity 属性在前景与背景间过渡（Opacity 接近 0 显示背景，接近 1 显示前景），并支持 Cropping Area（Left/Right/Top/Bottom）裁切控制（作者正文文本定性为 Commutative，见下文归纳分析）。
2. **PRACTICALLY DEMONSTRATED**：
   * 使用 Transformation 2D 平移/缩放纹理。
   * 使用 Levels 控制灰度白平衡与黑阶截断。
   * 观察灰度高度相加与相减在 3D 视口细分网格上的实际隆起与凹陷物理表现。
3. **MENTIONED / USED ONLY**：
   * 颜色通道混合时的色彩空间感知加权（如感知亮度加权未作展开）。
4. **INTERPRETIVE SUMMARY — independent math verification required**：
   * **代数公式形式化表达**：原书正文主要使用自然语言（plain English）描述计算逻辑，并未提供统一的代数公式（如 $F + B$, $1 - (1-F)(1-B)$ 等）。此类公式属于行业技术文档的常见代数归纳，并非作者原书排版内容。
   - **Switch 模式交换律的数学与代码核实**：原书文本虽明确将 Switch 模式定性为 "commutative"，但其实际操作由 Opacity 滑条与 Cropping 裁切边界控制（Opacity=0 显背景，Opacity=1 显前景）。在严格代数意义上，若保持 Opacity 不变且不等于 0.5，交换 Foreground 与 Background 的输入端口会导致输出反转，并不满足严格数学交换律 $f(A, B) = f(B, A)$。此处反映了原书文本分类与严谨数学定义之间的概念争议，建议在代码实现或深度教学中予以独立核对澄清。

---

### Ch 10: Creating a Television Shelf in Adobe Substance 3D Designer (pp. 321–366)

#### 原生章节目录与页码
* Creating the top and bottom profiles of the television shelf (pp. 322–333)
* Creating the side profiles of the television shelf (pp. 333–338)
* Creating the front doors of the television shelf (pp. 338–340)
* Creating the door vents and knobs of the television shelf (pp. 340–349)
* Creating Albedo Maps, Roughness Maps, and other textures for the television shelf (pp. 349–366)
* Summary (p. 366)

#### 知识分类解析
1. **EXPLICITLY TAUGHT**：
   * **大型家具资产程序化构筑流程**：分块规划顶部/底部台面、侧边立柱、前面板柜门、通风百叶窗与金属把手。
   * **高度轮廓优先与贴图派生流程（Height-First Texturing Workflow）**：Shah 演示了先集中构建高度/轮廓混合，再基于高度图节点派生 Curvature、AO、Normal 并驱动全通道材质细节的制作流程（注：“Height-Driven Pipeline”为现代技术总结性概括，非作者原生术语，归入 INTERPRETIVE SUMMARY）。
   * **材质通道融合**：木纹主体（Wood Grain）与金属构件（Metallic 1.0, 低粗糙度）通过蒙版合并为一套完整的 PBR 输出贴图。
2. **PRACTICALLY DEMONSTRATED**：
   * 使用 Shape, Transformation 2D 与 Blend 节点雕刻柜台斜角截面。
   * 使用 Tile Generator 制作百叶窗栅格，使用 Disc 制作门把手凸起。
   * 制作木纹 Base Color 并叠加磨损。
   * 整理输出节点（Base Color, Normal, Roughness, Metallic, Ambient Occlusion, Height）。
3. **MENTIONED / USED ONLY**：
   * **自定义参数暴露（Expose Parameters）**：❌ **Shah 本章完全未讲授如何将内部参数 Expose 给 Substance Player 或 Painter 作为滑条**！整个电视架图表采用的是固定参数搭建材质图，未进行动态参数发布。这是其作为入门教材的一大界限。
   * **复杂子图封装（Subgraphs）**：未将构件封装为独立子节点。

---

### Ch 11: Adobe 3D Sampler at a Glance (pp. 367–401)

#### 原生章节目录与页码
* Getting started with Adobe Substance 3D Sampler (pp. 368–374)
  * A – the top bar (the application menu bar) (pp. 368–369)
  * B – the left sidebar (the 2D modification tool) (pp. 369–374)
* Settings panels (pp. 375–380)
  * C – VIEWER SETTINGS (pp. 375–378)
  * D – SHADER SETTINGS (pp. 378–379)
  * E – CHANNEL SETTINGS (pp. 379–380)
* Assets panels (pp. 380–383)
  * F – The PROJECT and ASSETS panels (pp. 381–383)
* Adobe Substance 3D Sampler viewports (pp. 383–385)
  * G – the 3D view (pp. 383–384)
  * H – the 2D view (pp. 384–385)
* Right side panels and the toolbar (pp. 385–388)
  * I – the right sidebar (p. 386)
  * J – the LAYERS panel (pp. 386–387)
  * K – the PROPERTIES panel (pp. 387–388)
* Case study – creating a dirty old pavement (pp. 389–400)
* Sharing and exporting materials (pp. 400–401)
* Summary (p. 401)

#### 知识分类解析
1. **EXPLICITLY TAUGHT**：
   * **Sampler（原 Substance Alchemist）界面与管线定位**：图层式滤镜堆叠架构，桥接真实摄影照片与 Substance PBR 材质。
   * **Image-to-Material 转换**：载入单张自然照片，自动解析并估算 Base Color, Normal, Roughness, Height 贴图通道。
   * **无缝平铺化（Tiling Filter）**：消除照片边缘接缝，生成四方连续平铺贴图。
2. **PRACTICALLY DEMONSTRATED**：
   * **破旧石板路实战（Dirty Old Pavement Case Study）**：
     * 导入石板路照片，通过 Image to Material 生成初始 PBR 贴图。
     * 应用 Tiling 滤镜消除四角拼缝。
     * 叠加 Water 滤镜与 Dirt 滤镜，使低洼处积水反光、石缝嵌垢。
     * 导出为 Smart Material / 独立贴图集供 Painter 调用。
3. **MENTIONED / USED ONLY**：
   * **AI/机器学习估计模型底层数学**：直接调用 AI 功能，未深入卷积神经网络去光影（Delighting）算法细节。

---

### Shah (2022) Chapters 1–11 知识范围与未覆盖边界总结

基于一手正文核查，确认 Shah (2022) Chapters 1–11 存在以下明确未覆盖边界（Source Boundaries / Not Covered）：

1. **未教授 PBR 底层理论**：全书仅把 PBR 作为默认软件模板，完全未解释 Fresnel 反射率、微表面散射分布、能量守恒定律及金属/绝缘体微观反射差异。
2. **未教授 UV 拆分与展平工艺**：全书直接提供预展平的 FBX 资产，完全不涉及拓扑与接缝切割展开。
3. **未教授 Painter 中的 Geometry Mask 与 Symmetry Tool**：第 5 章的高级工具实操中，未涉及对称工具和现代几何体列表隔离蒙版。
4. **未教授 Designer 中的高级数学与参数暴露**：第 7–10 章为初阶节点连线指南，完全未涉及自定义数学函数图、Pixel Processor，在第 10 章实战中亦未教授参数暴露（Expose Parameters）。

---

## Source 2: Wes McDermott - The PBR Guide (2018, 3rd Edition)

* **书名**：*The PBR Guide: A Handbook for Physically Based Rendering*
* **作者**：Wes McDermott（时任 Allegorithmic / Substance 产品技术专家）
* **技术编辑**：Cyrille Damez, Nicolas Wirrmann
* **版本与版次**：Third Edition, February 2018（原第一版发布于 2016 年 6 月）
* **出版方**：Allegorithmic SAS（后并入 Adobe）
* **ISBN**：978-2-490071-00-5
* **总页数**：96 页（PDF 完整包含 Part 1 理论篇、Part 2 实战篇、Appendix 附录图表）

---

### Part 1: The Theory of Physically Based Rendering and Shading (pp. 18–40)

#### 原生章节目录与页码
* Light Rays (p. 18)
* Absorption and Scattering (pp. 19–21)
  * Transparency and Translucency (p. 21)
* Diffuse and Specular Reflection (pp. 22–27)
  * Microfacet Theory (pp. 24–27)
* Color (p. 28)
* BRDF (p. 29)
* Energy Conservation (p. 30)
* Fresnel Effect (pp. 30–32)
  * F0 (Fresnel Reflectance at 0 Degrees) (pp. 31–32)
* Conductors and Insulators (pp. 33–37)
  * Metals and Non-Metals (pp. 34–37)
* Linear Space Rendering (pp. 38–39)
* Key Characteristics of PBR (p. 40)

#### 核心物理与数学原理（EXPLICITLY TAUGHT）
1. **光的物理轨迹（Light Interaction）**：
   * 光线撞击材质表面分为反射（Reflection）与折射（Refraction）。
   * 吸收（Absorption）：光能转化为热能，导致光强衰减。
   * 散射（Scattering）：折射进入介质内部的光线多次碰撞后重新穿出表面，宏观呈现为**漫反射（Diffuse Reflection）**或**次表面散射（Subsurface Scattering）**。
2. **微表面理论（Microfacet Theory）**：
   * 任何平整的宏观表面在微观上都由微小的微表面（Microfacets）组成。
   * 每个微平面的法线方向不一致，微表面粗糙导致反射光束发散（粗糙高光，Roughness 高），微表面平整导致光束平行汇聚（镜面高光，Roughness 低）。
   * 微表面遮挡（Shadowing and Masking）：微凹凸之间相互遮挡造成的反射损失。
3. **双向反射分布函数（BRDF）与能量守恒（Energy Conservation）**：
   * 材质反射光总量**永远不能超过**入射光总量：$\text{Diffuse} + \text{Specular} \le \text{Incident Light}$。
   * 表面粗糙度变大时，高光亮点变暗且扩散，保持能量守恒。
4. **菲涅尔效应与 $F_0$（Fresnel Effect & F0）**：
   * 视线与表面法线夹角越平（Grazing Angle，接近 90°），表面反射率越强，所有真实物体在掠射角下的反射率均趋近于 100%（$F_{90} = 1.0$）。
   * **$F_0$ 定义**：视线垂直于表面（0 度法线入射）时的基础镜面反射率。
   * **非金属（Dielectric/绝缘体）$F_0$**：极低且固定，常见绝缘体 $F_0$ 介于 **2% 至 5%**（线性 0.02–0.05，对应 sRGB 40–75）。绝大多数非金属默认统一取 **4%（0.04，对应 sRGB 59）**。
   * **金属（Conductor/导体）$F_0$**：极高，通常介于 **70% 至 100%**（sRGB 180–255），且金属高光带有强烈的自身反射色彩（Tinted Specular）。
5. **导体与绝缘体划分规则（Conductors vs. Insulators）**：
   * 纯金属由于自由电子的存在，折射光在极短距离内被 100% 吸收，**金属没有漫反射（Diffuse = 0 / 纯黑）**，其视觉表现完全由带色彩的强镜面高光主导。
   * 铁锈、油污、漆面属于绝缘体（非金属），一旦金属表面氧化生锈，在物理光学着色中应按绝缘体特性处理。
6. **线性工作流（Linear Space Rendering）**：
   * 物理渲染引擎的光照加减乘除计算在线性色彩空间（Gamma 1.0）中进行。
   * 人眼对暗部变化更敏感，显示器采用 sRGB（约 Gamma 2.2）编码显示。
    * **通道色彩空间分配归纳（Color vs. Data Maps）[INTERPRETIVE SUMMARY]**：
      * **sRGB**：所有表征人眼可见颜色的贴图（Base Color, Diffuse, Specular Tint）。
      * **Linear**：所有表征数学数据或物理遮罩的贴图（Roughness, Metallic, Normal, Height, Ambient Occlusion）。

---

### Part 2: Practical Guidelines for Creating PBR Textures (pp. 45–88)

#### 原生章节目录与页码
* What is PBR? (pp. 45–46)
  * What Are The Benefits? (p. 45)
  * What Does It Mean for the Artist? (p. 46)
* Metal/Roughness Workflow (pp. 47–63)
  * Dielectric F0 (pp. 48–49)
  * Base Color (pp. 50–52)
  * Metallic (pp. 53–59)
  * Roughness (pp. 60–61)
  * Resolution and Texel Density (pp. 62–63)
  * Pros and Cons (p. 63)
* Specular/Glossiness Workflow (pp. 64–73)
  * Diffuse (pp. 65–67)
  * Specular (pp. 68–70)
  * Glossiness (pp. 71–72)
  * Resolution and Texel Density (p. 72)
  * Pros and Cons (p. 73)
* Maps Common to Both Workflows (pp. 74–79)
  * Ambient Occlusion (AO) (pp. 74–77)
  * Height/Normal (pp. 78–79)
* Substance PBR Utilities (pp. 80–88)
  * Substance Designer (pp. 81–83)
  * Substance Painter (pp. 84–86)
  * Substance Outputs and Rendering (pp. 87–88)

#### 核心实战规范与贴图准则（PRACTICALLY DEMONSTRATED & RULES）
1. **Metallic/Roughness 工作流贴图通道准则**：
   * **Base Color（sRGB）**：
     * 非金属：表征纯粹的漫反射反照率（Diffuse Albedo），**不应烘焙任何定向光照或投射阴影**。最暗非金属（木炭）通常不低于 30–50 sRGB，最亮非金属（雪）通常不高于 240 sRGB。
     * 金属：表征其在 0 度入射下的反射色彩（$F_0$），数值通常在 180–255 sRGB 之间。
   * **Metallic（Linear 灰度，pp. 53–59）**：
     * **基础取值倾向**：纯净、裸露的材质区域通常映射为接近 0（非金属/绝缘体）或接近 1（纯金属/导体）。
     * **过渡灰阶说明（Transitional Grayscale）**：教材明确指出金属贴图并不总是严格二值化的（may not always be binary）；表面灰尘、微观污渍、氧化层、极薄的半透明绝缘体覆盖层或抗锯齿过滤边缘均可产生合理的中间过渡灰阶。
     * **非绝对死板法则**：教材特别强调此处不存在硬性死板的铁律（"There are no hard-and-fast rules here"），明确不能将其简化为“过渡灰阶的唯一合法性”。
   * **Roughness（Linear 灰度）**：
     * 0.0（纯黑）代表绝对光滑镜面，1.0（纯白）代表极度粗糙漫散。
2. **Specular/Glossiness 工作流对比**：
   * **Diffuse**：仅存储非金属的漫反射颜色；在金属区域为纯黑（0 sRGB）。
   * **Specular**：存储所有材质的 $F_0$ 镜面反射率。非金属区域填充 4% 左右的灰度色阶（30–75 sRGB），金属区域填充带色彩的高光反射率（180–255 sRGB）。
   * **Glossiness**：Roughness 的反相显示（1.0 光滑，0.0 粗糙）。
   * **优缺点权衡**：Metallic 工作流贴图占用内存小且能防止艺术家误配 Specular 数值破坏能量守恒定律；Specular 工作流则允许自由打破物理限制自定义非标准 $F_0$。
3. **通用辅助贴图规范**：
   * **Ambient Occlusion（AO，Linear 灰度）**：
     * **物理约束**：AO 仅代表环境漫反射光线被几何褶皱遮蔽的比例，**仅影响漫反射环境光（Diffuse Contribution），不得遮挡镜面高光反射（Specular Contribution）**。
     * **贴图分离**：不应将 AO 直接乘入 Base Color 贴图，推荐作为独立通道提供给着色器。
   * **Tangent Space Normal（切线空间法线贴图）**：RGB 对应表面切线空间 XYZ 扰动向量，用于低模呈现高精度光影凹凸。
4. **Substance PBR 验证工具（PBR Validation Utilities）**：
   * 在 Designer/Painter 中挂载 `PBR Validate` 滤镜，根据金属度与反照率阈值实时标红/标黄违规像素（如过暗的非金属反照率、超出物理安全范围的数值），用于指导贴图规范检验。

---

### Appendix: PBR Charts & Comparisons (pp. 89–92)

* **决策树流程图（Flowchart: Is the surface metal?）**（pp. 89–90）：
  * 第一步确认材质表面状态：裸露金属 vs 漆面/涂层。
  * 若为漆面金属，着色器判断进入 Dielectric 分支；若为裸金属，进入 Conductor 分支，取用实测反射率。
* **物理材质反照率与反射率数值表（Reflectance Values Chart）**（p. 91）：
  * 金（Gold）：$F_0 = (1.00, 0.78, 0.34)$ / sRGB $(255, 226, 158)$
  * 银（Silver）：$F_0 = (0.97, 0.96, 0.91)$ / sRGB $(252, 250, 245)$
  * 铜（Copper）：$F_0 = (0.98, 0.82, 0.76)$ / sRGB $(250, 209, 194)$
  * 铁（Iron）：$F_0 = (0.77, 0.78, 0.78)$ / sRGB $(198, 198, 198)$
---

## Source 3: Eran Dinur (2026)

* **书名**：*The Complete Guide to Photorealism for Visual Effects, Visualization, and Games*
* **版本**：2nd Edition
* **作者**：Eran Dinur
* **出版年份与机构**：2026 (Routledge / Taylor & Francis)
* **Paperback ISBN**：`9781032966557`
* **Hardback ISBN**：`9781032966564`
* **eBook ISBN**：`9781040688663`
* **出版商官方产品元数据总页数 (Publisher product metadata)**：`246 pages`
* **一手 Notebook EPUB 源观测页码 (Notebook EPUB source)**：内嵌实体印刷页码标识观测至第 230 页（`Inline Print Page Markers observed through p. 230`，Index 索引项至 p. 230）
* **全书结构**：4 Parts, 19 chapters
* **提取范围说明**：`Material-relevant source-native extraction: 8 Chapters of 19`。
  * **纳入章节与理由**：
    * **Part 1 Core Concepts**: Ch 1 (Reality and Photorealism, pp. 9–21) 与 Ch 3 (Color, pp. 32–48)——直接提供照片级真实感的核心认知机制（为什么 CG 默认显得塑料/虚假）、细节困境、表面微瑕疵（Imperfections）的作用、倒角高光磁铁（Highlight Magnets），以及色彩与场景解构的六层模型（Six-Layer Approach）。
    * **Part 2 The Real World**: Ch 5 (Light Interaction, pp. 57–68) 与 Ch 9 (Basic Material Properties, pp. 92–96)——直接建立光线与物体表面微观交互物理机制（吸收、漫反射/镜面反射、次表面散射、透射折射、Albedo 与能量守恒）以及绝缘体（Dielectric）与金属导体（Metal）的光学本质与 Fresnel 效应。
    * **Part 3 The CG World**: Ch 11 (Rendering and Lighting, pp. 113–130)、Ch 12 (Shading, pp. 131–142) 与 Ch 13 (Texturing, pp. 143–156)——材质评估与打光支持（IBL、HDRI 标定、物理灯具衰减与色温）、现代 BRDF/PBR 着色模型（能量守恒、粗糙度驱动、清漆 Coat、透射与次表面）以及 PBR 贴图体系与实战工作流（图像纹理拍摄优化、程序化噪波、混合手绘）。
    * **Part 4 The 2D World**: Ch 19 (Photorealism with Generative AI, pp. 207–227)——第二版新增专章，作为生成式 AI 在真实感视觉工作流中的控制边界证据（扩散模型机制、Latent 空间、ControlNet 几何/法线引导、局部重绘与物理局限）。
  * **未纳入章节与排除理由**：
    * Ch 2 (Photorealism in Digital Media, pp. 22–31) 属行业宏观分类；
    * Ch 4 (Light Essentials, pp. 51–56)、Ch 6 (Daylight, pp. 69–79)、Ch 7 (Nighttime and Artificial Lighting, pp. 80–84)、Ch 8 (Shadows, pp. 85–91) 属一般性摄影与环境照明，其材质相关核心已包含在 Ch 5、9、11；
    * Ch 10 (Lens and Camera Characteristics, pp. 97–110) 与 Ch 18 (Lens and Camera Effects, pp. 195–206) 属于光学镜头与后期暗房缺陷，非材质表面生产；
    * Ch 14 (Modeling, pp. 157–164) 聚焦大尺度地形与植被程序化建模；
    * Ch 15 (Integrating 2D Elements, pp. 165–172)、Ch 16 (Integrating CG Elements, pp. 173–184)、Ch 17 (Lighting in 2D, pp. 185–194) 聚焦于后期合成（Compositing）、Deep Comp 与 2D 二次打光，脱离三维材质资产制作范畴。

---

### Ch 1: Reality and Photorealism (pp. 9–21)

#### 原生章节目录与页码
* Human Vision and Cameras (pp. 9–11)
  * Seeing with the Mind (pp. 10–11)
* The Uncanny Valley (pp. 11–13)
* The Detail Conundrum (pp. 13–15)
* The Role of Imperfections (pp. 15–18)
  * Case Study: Detail and Imperfections in Man-Made Objects (pp. 16–18)
* The Reality of The Unreal (pp. 18–19)
* Image Quality and Photorealism (pp. 19–20)
* 2D and 3D Workflows (pp. 20–21)

#### 知识分类解析
1. **EXPLICITLY TAUGHT（显式讲授与概念定义）**：
   * **CG 默认“塑料感/太干净”的数学根源**（pp. 15–16）：计算机图形学（CG）是一个脱胎于纯数学运算的虚拟媒介，在本质上具有“内在的完美性”（inherently perfect）。在 CG 中创建一个几何上绝对无瑕疵的球体或没有一丝划痕污垢的镜面是极其容易的，而这正是人眼直觉感到最虚假、最具有“塑料感”（synthetic / plastic look）的根源。
   * **自然界混沌与人造物解构**（p. 15）：大自然是混乱、破损、有机且不断风化衰变的；人造物体虽具有几何规则结构，但从出厂一刻起就不断受到自然界混沌的入侵——风化、重力沉降、灰尘附着、人为接触磨损与摩擦。照片级真实感要求艺术家在每个环节持续进行“对抗 CG 默认完美性的战役”。
   * **细节困境（The Detail Conundrum）与微细节累积效应**（pp. 13–15）：现实世界的物理细节是无限的，而计算机算力是有限的。CG 中艺术家常划定“基本必要线”（bare necessity line）或在游戏中依赖 LOD 系统；但真正的挑战在于“未被单独建模的微细节”（micro-details）。当相机远离物体时，肉眼虽无法解析单片瓦当或草叶，但无数微观细节在像素层面的“累积存在”（cumulative presence）构成了现实世界微妙的视觉丰富度与触觉质感，绝不能用平坦纯色替代。
   * **边缘倒角与高光磁铁（Beveled Edges as Highlight Magnets）**（pp. 16–18）：现实世界的人造物体几乎不存在绝对锋利垂直的 90 度几何直角。微小的倒角或圆角能够捕捉环境高光形成轮廓光（rim highlight），被称为“高光磁铁”；缺少倒角的高精度 CG 模型在渲染时边缘会显得生硬、扁平且虚假。
2. **PRACTICALLY DEMONSTRATED（手把手案例演练）**：
   * **人造物体细节与微瑕疵案例剖析（Case Study: Audio Console / Man-Made Objects, pp. 16–18）**：
     * 展示纯几何无瑕疵模型 vs 赋予真实感资产的巨大差异；
     * 演示边缘倒角对高光带的捕捉；
     * 分离材质贴图通道：不把所有细节塞入 Base Color，而是通过 Roughness 贴图表现手印、轻微油污与微弱划痕，利用 Normal 表现螺丝边缘凹凸。
3. **MENTIONED / USED ONLY（仅提及使用）**：
   * 电影长镜头与影视视效镜头运动分类（p. 10）；
   * 人眼视网膜与大脑视觉皮层感知心理学（pp. 10–11）；
   * 恐怖谷理论（The Uncanny Valley）在数字人类与角色动画中的表现（pp. 11–13）。
4. **INTERPRETIVE SUMMARY（归纳总结）**：
   * *真实感材质审视第一法则*：照片级材质制作的核心不是追求宏观纹理的堆砌，而是对表面几何边缘（倒角光泽）与微观粗糙度扰动（微瑕疵解构）的精细化物理还原。

---

### Ch 3: Color (pp. 32–48)

#### 原生章节目录与页码
* The Six-Layer Approach (pp. 32–36)
* Thinking Additive (pp. 36–39)
  * Subtractive Color (pp. 36–37)
  * Additive Color (pp. 37–39)
* Hue, Saturation, and Brightness in RGB (pp. 39–41)
* Color Operations (pp. 41–44)
  * Gain, Gamma, Lift, Offset, Saturation (pp. 42–44)
* Bit Depth and Dynamic Range (pp. 44–46)
* The Low End (pp. 46–47)
* The High End (pp. 47–48)

#### 知识分类解析
1. **EXPLICITLY TAUGHT**：
   * **客观视觉与主观认知打破**（pp. 32–33）：艺术家必须打破日常语言对色彩的笼统认知（例如把一辆车认定为“纯黑色”）。在真实相机成像中，黑色车身由于镜面高光和环境反射，实际包含了来自天空的蓝色、路面的黄色、环境物体的反光以及刺眼的白色高光点。
   * **场景与色彩解构六层模型（The Six-Layer Approach, pp. 33–36）**：
     1. **Layer 1 (Base Color)**：完全无外界环境光污染、在理想均匀白光漫射下物体的固有反照率；
     2. **Layer 2 (Surface Detail and Imperfections)**：附着在表面的物理细节与瑕疵（灰尘、划痕、锈渍、油印），独立于环境光改变基础色；
     3. **Layer 3 (Lighting & Environment Bounce)**：主光源定向照明、几何遮蔽阴影、环境漫反射光线弹射（Bounce Light）；
     4. **Layer 4 (Reflection Layer)**：由材质光滑度/粗糙度决定的高光反射与清晰环境镜像；
     5. **Layer 5 (Atmosphere Layer)**：视线距离产生的空气透视、薄雾、光能衰减与暗部抬升；
     6. **Layer 6 (Camera Layer)**：镜头光学成像、曝光、白平衡、色彩映射与传感器噪点。
   * **加色思维（Thinking Additive）与 RGB 像素操作**（pp. 37–39）：显示器与渲染器均采用 RGB 加色系统，艺术家需理解颜色通道之间的相对比例，而非仅凭直觉拖动明度滑块。
   * **暗部敏感性（The Low End, pp. 46–47）**：人类视觉对暗部明度微小变化的敏感度远高于亮部，黑电平（Black Level）的微弱漂移会彻底破坏场景材质的深度感与真实度。
2. **PRACTICALLY DEMONSTRATED**：
   * 对室外自然风光照片进行六层分层解构图解（从纯固有色逐步叠加瑕疵、直射光、环境反射、大气消散到最终相机输出，pp. 34–35）。
   * 对比 Gain（乘法/白场调节）、Lift（抬升/黑场调节）与 Gamma（中间调幂函数弯曲）对图像色彩层级的数学扰动（pp. 42–44）。
3. **MENTIONED / USED ONLY**：
   * 8-bit、10-bit、16-bit float 与 32-bit float 色彩位深在合成软件中的内存开销（pp. 44–46）；
   * 色彩管理 ACES 与 OpenColorIO 的工业管线术语（作为现代色彩空间背景提及，未展开转换公式）。

---

### Ch 5: Light Interaction (pp. 57–68)

#### 原生章节目录与页码
* Absorption (pp. 57–59)
* Reflection and Scattering (pp. 59–64)
  * Specular Reflection (pp. 60–61)
  * Diffuse Reflection (pp. 61–62)
  * Scattering (pp. 62–63)
  * Subsurface Scattering (pp. 63–64)
* Transmission and Refraction (pp. 64–66)
* Albedo (pp. 66–68)

#### 知识分类解析
1. **EXPLICITLY TAUGHT**：
   * **光能吸收（Absorption, pp. 57–59）**：光波与物质分子发生相互作用，特定波长的光能转化为分子热能；未被吸收的波长被反射或透射，决定了物体被人眼感知的色彩。
   * **镜面反射 vs 漫反射散射机制**（pp. 60–62）：
     * 镜面反射发生在微观绝对平整的光滑表面，入射角严格等于反射角；
     * 漫反射源自于次表面微观界面的多次微小散射或微观粗糙起伏，光线向四面八方均匀随机弹射，宏观上呈现出朗伯（Lambertian）漫反射。
   * **次表面散射（Subsurface Scattering / SSS, pp. 63–64）**：光线穿透半透明绝缘体表面进入物体内部，经历多次内部粒子碰撞散射后再从不同位置折射穿出。这是蜡、大理石、玉石、植物茎叶以及人体皮肤柔和通透感的核心物理成因。
   * **透射与折射（Transmission and Refraction, pp. 64–66）**：光在穿透致密透明介质时由于传播速率变慢发生方向偏折，遵循折射率（Index of Refraction, IOR）。
   * **Albedo 与能量守恒定律（Conservation of Energy, pp. 66–68）**：
     * 反照率（Albedo）定义为物体表面反射总辐射能与入射总能量的无量纲比值（0.0 至 1.0）；
     * 表面反射或透射的光能总和绝对不能超过入射的总能量（出射光能 $\le$ 入射光能）；
     * 纯金属和纯透明玻璃的漫反射反照率（Diffuse Albedo）严格为 0（纯黑），因为金属无光线穿透产生漫散射，而透明玻璃的光能被全部镜面反射与折射透射瓜分。
2. **PRACTICALLY DEMONSTRATED**：
   * 光束穿过棱镜发生折射偏角图解（p. 65）；
   * 石蜡与牛奶在强直射背光下的 SSS 穿透光晕展示（p. 64）；
   * 不同反照率小球在同等平行光照下的反射光照平衡测试（pp. 67–68）。
3. **MENTIONED / USED ONLY**：
   * 波动光学与光子量子态微观方程（作为物理背景简述，未提供偏振态与波动代数）；
   * 工业分光光度计实测光谱曲线（仅作为测量仪器概念提及）。

---

### Ch 9: Basic Material Properties (pp. 92–96)

#### 原生章节目录与页码
* Dielectric Materials (pp. 92–95)
  * Dielectric Diffuse/Specular Balance (pp. 93–94)
  * Fresnel Effect (pp. 94–95)
* Metals (pp. 95–96)

#### 知识分类解析
1. **EXPLICITLY TAUGHT**：
   * **绝缘体（Dielectric Materials / 非金属, pp. 92–95）**：
     * 涵盖自然界绝大多数材质（木材、石材、塑料、玻璃、水、皮革、皮肤）；
     * 光学表现为**漫反射（表现其固有色彩）与无色彩镜面反射的物理叠加**；
     * 绝缘体的镜面高光反射发生在最外层分子界面（或清漆/油脂层），因此高光绝对不会被材质本身染色，始终忠实反射入射光源的色温与颜色。
   * **菲涅尔效应（Fresnel Effect, pp. 94–95）**：
     * 表面镜面反射强度直接由“视线与表面法线的夹角（入射角）”决定；
     * **掠射角（Grazing Angles / 浅角度平视）**：镜面反射急剧增强，即使是粗糙木板或水面在接近 90 度切线平视时也呈现近乎 100% 的极强镜面反射；
     * **正视角（Facing Angles / 垂直俯视）**：镜面反射降至最低，主要由漫反射或透射占主导（例如垂直俯视水面能清晰看清池底，平视远方水面则只能看到天空倒影）；
     * 绝缘体的正视角反射率受其简单 IOR 严格控制（普通非金属 $F_0$ 约 2%–5%）。
   * **金属导体（Metals / Conductors, pp. 95–96）**：
     * 金属内部存在大量自由电子海，光子撞击表面瞬间即被弹回或直接吸收，无法穿透进入次表面；
     * 金属具有**严格为零的漫反射（Diffuse = 0 / 纯黑）**；
     * 金属的镜面反射率极高（通常在 70% 至 95% 以上），且其高光反射带有强烈的固有色彩（例如纯金反射黄色高光，紫铜反射粉橙色高光）；
     * 金属在正视角下依然保持极高的镜面反射率。
2. **PRACTICALLY DEMONSTRATED**：
   * 平视湖面（反射天空倒影）与垂直俯视水下卵石（看透折射水底）的菲涅尔实拍对比图解（pp. 94–95）；
   * 金币与铜器的高光染色与暗部反射行为图解（p. 96）。
3. **MENTIONED / USED ONLY**：
   * 金属复杂的复数折射率（Complex IOR: $n$ 与 $k$ 消光系数，书中仅指出金属折射行为与绝缘体不同，未展开复数公式计算）。
4. **INTERPRETIVE SUMMARY**：
   * *材质二元性法则*：自然界中裸露材质要么表现为绝缘体特性，要么表现为金属特性；半金属状态仅为微观混合或过渡污垢层，着色器参数应严格以物理二元性为准绳。

---

### Ch 11: Rendering and Lighting (pp. 113–130)

#### 原生章节目录与页码
* From Scanline to Path Tracing (pp. 113–116)
* Traditional Light Emitters (pp. 116–119)
* Contemporary Light Emitters (pp. 119–124)
* Essential Strategies for PBR Lighting (pp. 124–130)

#### 知识分类解析
1. **EXPLICITLY TAUGHT**：
   * **渲染算法演进与物理正确性**（pp. 113–116）：从传统光栅化/扫描线渲染（依靠人造环境光 Ambient Light 和经验公式补光）向基于物理的路径追踪（Path Tracing）演进。路径追踪遵循热力学与辐射度学定律，使材质表现完全取决于场景实际光线弹射。
   * **传统光源 vs 现代物理光源（Light Emitters）**（pp. 116–124）：
     * **Point / Spot Light（点光源/聚光灯）**：空间中无几何体积的点，产生不符合物理的锐利阴影，无法在镜面反射中呈现真实光源倒影；
     * **Area & Mesh Light（面光源与网格光源）**：具有真实三维几何尺寸的物理光源，能产生真实的半影模糊（Umbra & Penumbra），并在材质镜面高光中直接呈现真实的高光倒影反射；
     * **Photometric Light（光度学光源）**：加载真实灯具厂商 IES 文件，精准还原非均匀配光曲线与色温。
   * **基于图像的光照（Image-Based Lighting / IBL 与 HDRI）**（pp. 120–124）：
     * 利用 360 度多重包围曝光的高动态范围图像作为无限远照明天球，直接驱动材质的漫反射环境光、镜面反射高光与环境透射；
     * **天光平衡与标定（HDRI Calibration）**：实拍天空 HDRI 常存在蓝天像素过饱和问题，需适当微调饱和度；针对高亮度太阳，标准 PBR 工作流通常是在 HDRI 中修除太阳，另建平行直射光（Directional Light）精确匹配角度与强度，以保证阴影边缘与高光可控。
   * **光强平方反比衰减定律（Inverse-Square Law, pp. 124–125）**：
     * 点状/面状光源光强与距离平方成反比（$I \propto 1/d^2$）；
     * 产生近强远弱的剧烈照度阶梯，决定了靠近光源处材质高光强度的极端动态范围；
     * 太阳光作为平行直射光，在地表尺度上衰减可忽略不计。
   * **色温（Color Temperature in Kelvin, pp. 125–126）**：
     * 建立从烛光（1800K）、暖白钨丝灯（2800K）、日光（5500K）到阴天/蓝天（6500K–10000K）的绝对物理色温标准，在材质打光评估中必须结合 Lumen/Lux 照度单位使用。
   * **多光源环境下的材质表现评估策略（Strategies for Evaluating Materials under Lighting, pp. 126–130）**：
     * 强调材质外观无法脱离光照环境孤立存在；
     * 在渲染评估中，必须保证真实世界比例尺（Real-World Scale），否则物理衰减与 GI 计算将完全失真；
     * 结合主光（Key）、辅助光（Fill）、轮廓光（Rim）与环境天光构建多角度照明，以检验材质在不同入射角下的 Roughness 渐变、边缘倒角高光与金属反照。
2. **PRACTICALLY DEMONSTRATED**：
   * 音频调音台资产在单一环境光 vs 结合面光源、聚光灯与窗边冷光的多光源环境下的质感渲染对比（pp. 128–130）；
   * 点光源生硬阴影 vs 矩形面光源平滑柔和半影对比图解（pp. 118–120）。
3. **LIMITATION & BOUNDARIES（边界与局限性）**：
   * **IBL 的几何局限**：书里明确指出普通 2D/3D HDRI 仅为一个无限远天壳（eggshell），缺乏深度信息，无法替代室内或局部空间具有物理遮挡的真实灯具。
4. **INTERPRETIVE SUMMARY / Project Scope Boundary（项目教学边界裁定）**：
   * *Lighting ≠ Material Curriculum Automatically*：Dinur 在本章系统阐述了灯光与渲染机制，但其在材质课程中的定位应为“材质真实感评估与 LookDev 检验的技术支撑”，而非以此为据将完整的三维灯光与摄影视效课程全盘纳入数字材质制作课。

---

### Ch 12: Shading (pp. 131–142)

#### 原生章节目录与页码
* A Brief Overview of Shader Evolution (pp. 131–133)
* The Brdf Shading Model (pp. 133–140)
* Other Common Shaders (pp. 140–142)
  * Car Paint Shaders (p. 141)
  * Volumetric Shaders (pp. 141–142)
  * Hair/Fur Shaders (p. 142)

#### 知识分类解析
1. **EXPLICITLY TAUGHT**：
   * **着色器演进历程**（pp. 131–133）：
     * *Flat Shading*（面着色，逐面计算，棱角分明）；
     * *Gouraud Shading*（顶点着色插值，高光若落在面中心会丢失）；
     * *Phong & Blinn-Phong*（逐像素法线插值与经验高光，**核心缺陷：违背能量守恒定律，高光过曝，无微表面粗糙度物理散射**）。
   * **现代微表面 BRDF 着色模型**（pp. 133–140）：
     * 采用 GGX / Cook-Torrance 微表面理论（Microfacet Model），严格强制能量守恒；
     * **Metallic/Dielectric 二元切换机制**：非金属使用漫反射颜色与无色小比例高光；金属无漫反射，高光直接继承 Base Color。
   * **BRDF 核心参数体系详解**：
     * **Diffuse**：漫反射颜色与 Oren-Nayar 粗糙漫反射（表现粉末、织物与黏土的平缓漫反射衰减）；
     * **Specular & Roughness（高光与粗糙度控制）**：Dinur 明确指出，由于 BRDF 镜面反射遵循能量守恒定律，反射粗糙度越高、其反射光线越分散、高光自然越暗；仅通过调节粗糙度即可完整覆盖从极光滑到最暗哑表面的全范围，因此**高光强度/权重控制在通常情况下是多余的，应保持在 100%（"The specular intensity/weight control is therefore redundant and should normally be kept fixed at 100%"）**；包含各向异性（Anisotropy，拉丝金属与毛刷纹理的高光拉伸）；
     * **Coat（清漆/涂层）**：在材质表面附加独立的第二层光滑透明反射高光层（用于汽车漆表面罩光、打蜡木地板、塑料或雨水潮湿表面）；
     * **Transmission（透射）**：用于清澈/浑浊玻璃、透明树脂与液体，受透射粗糙度、基于厚度的吸收颜色深度（Depth-dependent color）与体积散射控制；
     * **Subsurface Scattering（次表面散射）**：通过散射半径（Scatter Radius）控制光在半透明介质内的渗透扩散范围；
     * **Emission（自发光）**：使材质表面成为光源，但警告严禁滥用 Emission 作为表面增亮伎俩（会破坏场景全局光照与能量守恒平衡）；
     * **高级光学特征**：Sheen（边缘光泽，织物微纤维）、Thin-Film Interference（薄膜干涉，肥皂泡与油膜七彩虹彩）、Dispersion（色散，通过 Abbe 阿贝数控制玻璃彩虹棱镜分色）。
   * **专用着色器类型**（pp. 140–142）：汽车漆着色器（含底层金属闪粉 Metallic Flakes 与表层清漆）、体积着色器（烟火流体）与毛发着色器（各向异性毛发纵向反射与黑色素 Melanin 吸收）。
2. **PRACTICALLY DEMONSTRATED**：
   * 犹他茶壶（Utah Teapot）在 Flat、Gouraud 与 Blinn 经典着色下的视觉缺陷对比（p. 132）；
   * 象头神石雕（Ganesha statue）在同一视角下测试不同 Diffuse Roughness、Dielectric vs Metallic 切换、Roughness 从 0.05 到 0.70 的逐级扩散、添加 Clear Coat 以及调节 SSS 半径的并列渲染实测（pp. 134–139）；
   * 玻璃花瓶在 Transmission 吸收深度与 Abbe 1 vs 30 色散效果下的对照实测（pp. 138–140）。
3. **LIMITATION & BOUNDARIES**：
   * **着色器参数边界约束**：中间态 Metallic 滑块值在物理世界不存在，仅用于材质边缘过渡混合；Abbe 阿贝数若低于 20 会产生夸张非真实的彩虹伪影；不可将自发光当作补光作弊工具。

---

### Ch 13: Texturing (pp. 143–156)

#### 原生章节目录与页码
* PBR Texturing (pp. 143–149)
  * The Linear Workflow (pp. 143–144)
  * Base Color Map (pp. 144–146)
    * Dielectric / Metallic Differences (p. 144)
    * PBR Safe Range (pp. 144–145)
    * Contrast and Saturation (pp. 145–146)
    * Avoiding Overly Busy Color (p. 146)
  * Roughness Map (pp. 146–147)
  * Metallic Map (p. 147)
  * Bump (Normal) Map (pp. 147–148)
  * Ambient Occlusion (AO) Map (p. 148)
  * Displacement (Height) Map (pp. 148–149)
  * Transparency Map Versus Opacity Map (p. 149)
* Texture Generation Workflows (pp. 149–150)
* Image Textures (pp. 150–153)
* Shooting and Prepping Photos for Texturing (pp. 153–154)
  * Resolution (p. 153)
  * Baked-in Lighting (pp. 153–154)
  * Exposure (p. 154)
  * Optimizing Photographs for Tiling (p. 154)
* Procedural Textures (pp. 154–155)
* Combining Workflows (pp. 155–156)

#### 知识分类解析
1. **EXPLICITLY TAUGHT**：
   * **PBR 核心贴图通道体系与线性管线**（pp. 143–149）：
     * **Linear Workflow**：色彩类贴图（Base Color）存储在 sRGB 空间，读取时必须线性化；数据类贴图（Roughness, Metallic, Normal, Displacement）必须在 Raw/Linear 模式下读取以保护数学精度；
     * **Base Color（反照率安全范围与渲染问题）**：非金属表达纯固有色，金属表达镜面高光颜色；Dinur 强调 Base Color 决定了反照率（Albedo），虽然没有绝对精准的色彩范围定义，但推荐漫反射安全范围通常在 30–240 sRGB 之间，金属色彩在 180–255 sRGB 之间。**若使用极端的纯黑（0 sRGB）或纯白（255 sRGB），表面会因吸收或反射过多光能而违背能量守恒定律，导致在光照变化下产生不自然的视觉反应，并严重干扰全局光照（GI）的弹射计算平衡**，因此确保数值处于安全范围可避免后续环节出现光照与渲染问题；
     * **Roughness Map**：黑（0.0 镜面）白（1.0 漫散）灰度图，是表现微观手印、水渍、油脂擦痕与尘土的核心载体；
     * **Metallic Map（金属贴图特征与制作建议）**：Dinur 明确指出金属贴图是灰度贴图，但在物理上表面要么是绝缘体要么是金属（不存在半金属）。作者明确建议：无论采用何种方法制作金属贴图，**都应大幅拉高对比度（crank the contrast and values）使其数值尽可能接近 0 或 1，避免过多的渐变灰阶；金属与绝缘体之间的过渡应当是相对清晰锐利的（"the transition should be fairly sharp"）**；中间过渡灰阶主要保留在两种材质状态的边缘分界线以处理抗锯齿和像素过渡；
     * **Normal vs Displacement**：Normal 贴图通过 RGB 向量扰动表面光影法线，不改动网格轮廓；Displacement 贴图在渲染时细分并真正顶起几何多边形；
     * **Transparency vs Opacity**：Transparency 产生真实的物理透射与折射（表面高光反射保留）；Opacity 则是几何镂空遮罩（彻底切除多边形）。
   * **三类纹理生成工作流的优缺点剖析**（pp. 149–156）：
     * **实拍照片纹理（Image Textures）**：真实感细节无可比拟，但致命缺陷是存在 UV 拉伸、平铺接缝、以及照片中不可消除的“烘焙光照”（Baked-in Lighting）；
     * **纹理摄影采集规范（Shooting & Prepping Photos）**：作者提出核心规则是“避免直射光（avoid direct light）”。**室外照片与三维扫描应始终在阴天散射光下或完全阴影中拍摄（"Outdoor photos and 3D scans should always be captured under overcast sky or in full shadow"）**；室内拍摄应尽量做到平坦漫射光照，避免明显的直射光源或强烈的投射阴影；必须进行正交透视矫正与去色调平铺处理；
     * **程序化纹理（Procedural Textures / Substance Designer）**：分辨率无关、无缝平铺、非破坏性且支持随机种子（Random Seed）批量迭代；但致命缺陷是容易产生冰冷机械的“程序化特征感”（generic procedural look）；
     * **综合混合工作流建议（Combining Workflows）**：推荐将照片真实感（作为 Base Color 底色）与程序化噪波（生成高度、法线与粗糙度）相结合，并通过手动绘制（Hand-painting）添加与具体几何拓扑强相关的定制微瑕疵（例如把手处的手印磨损、角落缝隙的灰尘沉降、曲面边缘的水流冲刷痕迹）。
2. **PRACTICALLY DEMONSTRATED**：
   * 复古电子合成器（Vintage Synthesizer）资产完整的 PBR 贴图流程拆解（从白模、底色、粗糙度、法线到最终微瑕疵的逐层演进，pp. 144–147）；
   * 潮湿地面材质的全套 PBR 贴图对应拆解（Base Color, Roughness, Normal, AO, Displacement，pp. 148–152）；
   * Substance Designer 节点图表与石头墙壁材质的 6 组随机种子（Seed）变换生成展示（p. 155）。
3. **LIMITATION & BOUNDARIES**：
   * **贴图使用陷阱**：法线贴图过度用力（Over-cranked）会在剪影边缘露馅且产生刺眼噪点；置换贴图滥用于微观织物会白白浪费显存与渲染时间；超出 PBR 安全范围的 Base Color 会破坏真实感并引发环境光照失衡。
4. **INTERPRETIVE SUMMARY / Project Synthesis（项目归纳）**：
   * *纹理制作整合方法论*：Dinur 提出“底色借照片、高度靠程序、瑕疵依拓扑手绘”的混合工作流思路，为数字材质制作中平衡生产效率与真实感细节提供了极佳的方法论指导。

---

### Ch 19: Photorealism with Generative AI (pp. 207–227)

#### 原生章节目录与页码
* Generative AI for Video Versus Stills (pp. 207–208)
* Oh, The Errors it Makes (pp. 208–210)
* A Note about Stable Diffusion (pp. 210–227)
  * Understanding the Diffusion Process (pp. 210–213)
    * Checkpoint Models (pp. 211–212)
    * LoRA Models (p. 212)
    * Other Types of Models (pp. 212–213)
    * Latent Space and VAE (p. 213)
    * Denoiser (p. 213)
    * Text Prompts (Clips) (p. 213)
  * Generative AI Concepts and Techniques (pp. 213–216)
    * Aspect Ratio (pp. 213–214)
    * Resolution (pp. 214–215)
    * CFG (Classifier-Free Guidance) (pp. 215–216)
    * Denoising Steps and Schedulers (p. 216)
  * The Art of Prompting (pp. 216–220)
    * Prompt Weights (pp. 217–218)
    * Negative Prompts (p. 218)
    * Prompting for Photorealism (pp. 218–219)
    * Prompting with AI (pp. 219–220)
    * Split Prompts (p. 220)
  * Inpainting (pp. 220–222)
    * Inpainting Prompts and Additional Guidance (pp. 221–222)
  * Using ControlNet Models (pp. 222–225)
    * Depth ControlNet (pp. 223–224)
    * Normal ControlNet (p. 224)
    * Canny (pp. 224–225)
    * OpenPose (p. 225)
    * IP Adapters (p. 225)
    * Segmentation (p. 225)
  * Case Study: Season Changes with ComfyUI and Nuke (pp. 225–227)

#### 知识分类解析
1. **EXPLICITLY TAUGHT**：
   * **扩散生成底层架构与运作机制**（pp. 210–213）：
     * **Diffusion Process**：基于高斯加噪与逐步去噪逆向重建图像；
     * **Latent Space & VAE**：在压缩隐空间内进行计算，VAE 负责像素空间与隐空间的编码/解码；
     * **Denoiser & Schedulers**：调度器（如 DPM2-Karras / DPM3-Karras）控制去噪采样的数学轨迹。
   * **提示词工程与引导参数控制**（pp. 213–220）：
     * 提示词结构（前景主体 -> 背景环境 -> 光照与时段）；
     * 提示词权重加减（如 `(subject: 1.3)`）；
     * **Negative Prompts**（负向提示词）：过滤非真实感风格（`CG, render, illustration`）与 AI 伪影（`extra fingers, wrong shadows`）；
     * **CFG（无分类器引导度）**：过高会导致图像严重过饱和、对比度发硬并产生伪影；适度调低能带来更柔和自然的真实感色彩。
   * **局部重绘（Inpainting）与去噪幅度**（pp. 220–222）：
     * 配合羽化遮罩实现局部画面重构；
     * Denoising Strength 决定对原图光照与几何的保留程度。
   * **ControlNet 结构条件引导套件**（pp. 222–225）：
     * **Depth ControlNet**：利用深度图（或 CG Z-depth 通道）引导画面的宏观空间布局、透视与物体比例；
     * **Normal ControlNet（法线条件控制）**：利用表面法线表征（surface-normal representation）指示几何表面朝向（direction of surfaces），作为光照方向与表面起伏细节的条件线索（surface-orientation / lighting-direction cue），与 Depth ControlNet 形成互补；
     * **Canny / OpenPose / IP Adapters / Segmentation**：分别提供硬轮廓、人体骨骼、视觉参考风格注入与语义区域隔离。
2. **PRACTICALLY DEMONSTRATED**：
   * **电影镜头季节变换实战案例（Case Study: Season Changes with ComfyUI and Nuke, pp. 225–227）**：
     * 艺术家 Kevin Samar 演示电影实拍长镜头秋季变冬季/春季的工作流；
     * 在 Nuke 中擦除演员并输出首尾关键帧干净背景板；
     * 将背景板与 CG 深度图送入 ComfyUI，借助 **Depth ControlNet** 与 SDXL 大模型，施加季节关键词重新生成雪景与春季植被；
     * 将生成结果带回 Nuke 投影到三维卡片模型上，重新合成摄像机运动、演员与粒子飘雪。
3. **LIMITATION & BOUNDARIES（明确的工具局限与证据边界）**：
   * **生成式 AI 的根本局限性（Why AI is Not Deterministic 3D）**：
     * **缺乏确定性物理控制**：传统 3D 渲染基于严密的几何与光学路径追踪，而 AI 生成本质上是基于概率关联重组像素。微调提示词或种子会导致全图不可控漂移，无法精准调整局部微观粗糙度或法线朝向；
     * **“知其形而不知其理”（Form without Physics）**：AI 只在统计学上知道“照片长什么样”，完全不理解三维空间、物理光学、光线追踪、能量守恒与透视法则；
     * **空间与解剖逻辑错误**：极易产生手指畸变、镜面反射错位（无法生成空间对应的镜中倒影）、标牌文字乱码等致命逻辑破绽；
     * **视频连续性崩溃**：视频生成在时间轴上算力开销暴增，且难以维持帧间连续性与物体几何恒常性。
   * **【特别证据纪律声明】Material Curriculum Deployment Boundary（材质课程部署证据边界）**：
     * Dinur 在 Ch 19 讲授的内容属于**通用视效/环境镜头生成（General Photoreal / Generative Scene Workflow）**的实战控制方案（如 ComfyUI + Nuke 视效镜头修图）；
     * **严禁将此处的生成式 AI 内容直接等同于“可直接部署于三维数字材质生产（Substance PBR Material Production）的一手证据”**。其在材质生产中的应用仅作为概念参考，不可替代标准 PBR 贴图的制作。

---

### Dinur (2026) 教学范围与未教授盲区总结

1. **DINUR (2026) 明确覆盖的核心知识贡献（Explicit Contributions）**：
   * **真实感观察与微瑕疵美学哲学**：系统论证了 CG 为何天生具有“完美塑料感”，奠定了通过边缘倒角（高光磁铁）、微观粗糙度扰动与自然侵蚀对抗纯数学完美的观察方法论；
   * **色彩与材质的六层解构模型**：提供了从 Base Color、微瑕疵、直射与弹射光、镜面反射、大气透视到相机光学的一整套自下而上逆向分析真实感的框架；
   * **物理光线交互与材质二元性**：深入阐释了绝缘体（固有色+无色高光+低正视角反射）与金属（无漫反射+彩色高光+高反射）的本质区别与能量守恒定律；
   * **多光源光照与物理渲染策略**：详述了面光源阴影半影、IBL 天光标定、平方反比衰减与多光源光照环境下的材质表现审视；
   * **PBR 着色器高级参数矩阵**：覆盖微表面粗糙度、各向异性、双层清漆（Coat）、透射折射、次表面散射、薄膜干涉与色散；
   * **PBR 贴图制作的三大流派**：透彻对比了实拍采样、程序化生成与手动绘制的优缺点，提出底色取实拍、高度取程序、瑕疵取手绘的综合思路；
   * **生成式 AI 的真实感控制边界**：在 ComfyUI / Stable Diffusion 环境下讲授了 Latent、VAE、CFG、局部重绘以及利用 Depth/Normal ControlNet 引入空间结构条件的实战工作流。
2. **DINUR (2026) 明确未教授的盲区与局限（Source Limitations & Does Not Cover）**：
   * **无特定软件手把手菜单操作**：本书属于跨软件的“原理与法则指南”（Principles Guide），不提供特定三维软件（如 Maya、Blender、Substance 3D Painter）的具体菜单点击操作步骤；
   * **无 Substance Designer 节点网络深度编写**：虽肯定了 Designer 的程序化价值并展示了成品节点图与石墙随机效果，但未讲授原子节点公式编写、空间数学映射或自定义函数；
   * **无实时渲染引擎底层着色代码**：未提供 HLSL/GLSL 编写、Deferred vs Forward 渲染管线深度分析或游戏引擎 DrawCall 优化细节；
   * **AI 仅作为视效镜头辅助而非 PBR 贴图生成器**：Ch 19 未讲解利用 AI 生成无缝 PBR 贴图通道（如将 AI 接入 Substance Sampler）的具体算法与实操。

---

## 4. Source Complementarity and Coverage Boundaries

本节基于当前已完成一手索引的三本权威教材（Shah 2022、The PBR Guide 2018 与 Dinur 2026）的正文事实，客观梳理其覆盖范围（Source Covers）、未覆盖盲区（Source Limitations）与内容互补关系（Source Complementarity）。严格遵循不包含任何周数安排（Week Scheduling）、软件课时配比或教学行动裁定的原则。

| 知识与能力维度 | Wes McDermott (*The PBR Guide* 2018) | Zeeshan Jawed Shah (*Realistic Asset Creation* 2022) | Eran Dinur (*Guide to Photorealism* 2026) | 三者互补性与边界事实说明 (Source Complementarity & Boundaries) |
| :--- | :--- | :--- | :--- | :--- |
| **物理光学基础与着色机制** | **Source Covers**：微表面理论、BRDF、能量守恒定律、Fresnel $F_0$ 绝缘体/金属微观反射推导。 | **Source Limitation**：仅套用默认 PBR 材质球模板，未解释微表面光学与能量守恒原理。 | **Source Covers**：系统阐释光能吸收、散射、透射折射、次表面散射（SSS）、能量守恒定律以及绝缘体 vs 金属的微观物理二元性。 | **Complementarity**：McDermott 与 Dinur 共同构筑坚实的物理光学理论基石；Dinur 进一步扩展了 SSS、透射折射与微表面漫反射的光学细节，弥补了 Shah 缺乏物理底层原理的短板。 |
| **真实感观察与质感审视 (LookDev Judgment)** | **Source Limitation**：偏向于贴图规范与数值表，较少探讨宏观审美认知与现实观察法则。 | **Source Limitation**：偏向于软件功能实现，缺乏“如何判断真实感是否达标”的审视训练。 | **Source Covers**：系统讲授现实观察方法论、“细节困境”微细节累积效应、解构场景色彩的“六层模型”、边缘倒角（高光磁铁）以及对抗 CG“塑料感/太完美”的核心法则。 | **Complementarity**：Dinur 专注于材质制作的审美认知与质感审视方法（LookDev Judgment），填补了 Shah 和 McDermott 偏向纯软件操作与规范定义时的观察方法论空白。 |
| **打光支持与材质评估环境** | **Source Limitation**：仅提及在不同光照环境下测试贴图，未展开物理打光实战。 | **Source Limitation**：主要在 Painter/Stager 预置 HDR 环境中预览，未讲授物理灯具衰减与色温。 | **Source Covers**：深入讲解物理面光源半影生成、光强平方反比衰减定律、真实世界尺寸比例尺、色温（Kelvin）标准以及多光源照明下的材质表现评估。 | **Complementarity**：Dinur 提供了评估材质真实感所需的光照物理机制分析，有助于学生在科学的照明环境下审视材质，弥补单纯依赖预置 HDR 预览的局限。 |
| **着色器参数体系 (Shading Controls)** | **Source Covers**：Metallic/Roughness 与 Specular/Glossiness 基础双管线参数映射。 | **Source Covers**：Painter 图层通道与 Designer 节点输出槽配置。 | **Source Covers**：全面覆盖现代 BRDF 着色器参数体系，包含 Diffuse Roughness、双层清漆（Coat）、透射吸收深度、次表面散射半径、各向异性（Anisotropy）、薄膜干涉与阿贝数色散。 | **Complementarity**：Dinur 建立了现代高级着色器的全功能参数认知图谱，极大拓宽了 McDermott 基础 PBR 参数的边界。 |
| **贴图规范与色彩空间安全** | **Source Covers**：线性空间渲染（Linear Space）、sRGB vs Linear 通道定义、Albedo 安全范围（30–240 sRGB）、PBR Validate 校验。 | **Source Limitation**：直接使用软件既有配置，未系统阐述 Gamma 矫正与色彩安全范围。 | **Source Covers**：系统强调线性管线、数据图读入 Raw/Linear 模式、Albedo 物理安全界限（避免过黑过亮干扰 GI 平衡与真实感）。 | **Complementarity**：McDermott 与 Dinur 交叉印证了贴图制作的数据安全标准，指导数字贴图规范化生产。 |
| **软件实操与资产烘焙管线** | **Source Limitation**：仅概述 Substance 软件定位，无具体操作步骤。 | **Source Covers**：手把手讲授 7 种核心网格贴图烘焙、Texel Density 计算、顶点色 ID 映射、图层堆栈与 6 大投影模式。 | **Source Limitation**：属于原理与法则指南，无具体软件菜单点击或手把手软件界面练习。 | **Complementarity**：Shah 提供了工业级软件手把手实操教学，将 McDermott 和 Dinur 的物理理论落实为生产力工具动作。 |
| **手绘贴图、智能材质与资产复用** | **Source Limitation**：无手绘与智能材质封装实操。 | **Source Covers**：详细示范 Black Mask、Planar Mask、Stencil、Clone/Smudge 工具、Smart Material 封装与 Anchor Point 联动。 | **Source Covers**（概念层面）：强调手工绘制与模型拓扑强相关的微瑕疵（把手油污、缝隙积灰、水渍），但无具体软件操作。 | **Complementarity**：Dinur 强调“在模型关键接触与风化部位手工绘制微瑕疵”的方法论，由 Shah 具体的 Painter 画笔、遮罩与锚点工具加以实现。 |
| **程序化纹理设计 (Procedural Texturing)** | **Source Limitation**：仅介绍节点化思想。 | **Source Covers**：原子节点 vs 复合节点、12 种混合模式、砖墙与电视架综合图表实战；但未覆盖参数暴露。 | **Source Covers**（方法论层面）：透彻对比程序化纹理的无缝随机优势与“冰冷机械感”陷阱，演示 Substance Designer 随机种子迭代。 | **Complementarity**：Shah 提供了 Designer 节点连接实操，Dinur 则提示了程序化纹理的审美陷阱并给出了破除机械感的方法论思路。 |
| **纹理摄影采集与处理** | **Source Limitation**：未涉及摄影采集。 | **Source Covers**：Sampler 中利用 Image-to-Material 快速解析单张照片为 PBR 贴图。 | **Source Covers**：系统讲授纹理摄影规范（阴天散射光或全阴影拍摄、避免直射光高光与投影、去色调透视调平与无缝平铺）。 | **Complementarity**：Dinur 补齐了前端纹理摄影采集的物理规范，与 Shah 的 Sampler 照片后处理形成完整闭环。 |
| **生成式 AI 在真实感工作流中的应用** | **Source Limitation**：出版时间较早，未覆盖生成式 AI。 | **Source Limitation**：2022 年出版，未涉及生成式 AI 辅助功能。 | **Source Covers**：详细讲授扩散模型逆向去噪机制、Latent 空间、CFG 引导、局部重绘（Inpainting）以及利用 Depth/Normal ControlNet 引入几何与表面法线条件线索的视效合成实战。 | **Complementarity**：Dinur 提供了生成式 AI 技术的权威一手教学依据，明确了以 Depth/Normal 空间图作为几何先验约束条件的控制方法，并清醒指出了 AI 的非确定性与物理逻辑缺陷。 |

---
*本文档为 Gate 2.5A 阶段成果，汇总了 Shah (2022)、The PBR Guide (2018) 与 Dinur (2026) 的一手源知识索引，作为后续 Gate 2.5B（Provenance Audit & Page Reference Update）与 Gate 3（Teaching Value Matrix 修正）的权威事实凭据。*
