# Source-Native Knowledge Index: Shah (2022) & The PBR Guide (2018)

> **审计状态声明（Gate 2.5A Deliverable）**：
> 本文档是严格遵循 **Gate 2.5A** 要求自下而上建立的“教材一手知识索引”（Source-First Artifact）。
> 
> * **绝对遵循准则**：仅基于 Course Knowledge Notebook (`e29f9644-03b2-4e1b-bcb0-b954b5bf08be`) 内真实教材 PDF 源（Shah 2022 `6a26e0ee-71de-43cf-be7f-c39d2ad2da43` 与 The PBR Guide `7b3dde6d-a06c-42b1-9814-3bed5617c315`）的 Direct Retrieval 与提取文本。
> * **不采用任何二手证据**：绝不引用旧 transcript、旧 task log、`curriculum-coverage-matrix.md`、`textbook-source-map.md` 或现有 draft 作为事实证据。
> * **严禁凭空拟造页码**：所有章节名称、层级标题与页码均来自于教材正文目录（TOC）与正文检索。

---

## 目录

1. [Source 1: Zeeshan Jawed Shah (2022) 全章索引 (Ch 1–11)](#source-1-zeeshan-jawed-shah-2022)
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
3. [两本教材在 8 周本科课程中的知识结构对照与边界沉淀](#两本教材在-8-周本科课程中的知识结构对照与边界沉淀)

---

## Source 1: Zeeshan Jawed Shah (2022)

* **书名**：*Realistic Asset Creation with Adobe Substance 3D: Create materials, textures, filters, and 3D models using Substance 3D Painter, Designer, and Stager*
* **作者**：Zeeshan Jawed Shah
* **出版方**：Packt Publishing, 2022
* **ISBN**：978-1-80181-450-8
* **总页数**：478 页（正文含 Index）

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
   * **贴图导出色彩位深（Bit Depths）**：Normal/Height 必须导出为 16-bit 以防断层梯级，Base Color/Roughness 导出为 8-bit。
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
   * **灰度转彩色管道规范**：灰度图性能远高于彩色图；必须使用 `Gradient Map` 进行灰度转彩色；使用 `Grayscale Conversion` 进行彩色转灰度。
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
1. **EXPLICITLY TAUGHT（12 种混合模式算法与数学交换律）**：
   * 明确所有模式在 `[0, 1]` 归一化区间内执行逐像素运算，输出值钳位（Clamped）在 `[0, 1]`：
     1. **Copy**（p. 305）：前景直接覆盖背景，非交换律（Non-commutative）。
     2. **Add**（p. 307）：数值相加，$F + B$，溢出切至 1，满足交换律（Commutative）。
     3. **Subtract**（p. 307）：背景减前景，$B - F$，下溢切至 0，非交换律。
     4. **Min (Darken)**（p. 308）：取暗部最小值，$\min(F, B)$，满足交换律。
     5. **Max (Lighten)**（p. 308）：取亮部最大值，$\max(F, B)$，满足交换律。
     6. **Multiply**（p. 310）：相乘变暗，$F \times B$，满足交换律。
     7. **Divide**（p. 310）：相除变亮，$B / F$，非交换律。
     8. **Screen**（p. 312）：滤色防过曝，$1 - (1-F)(1-B)$，满足交换律。
     9. **Soft Light**（p. 312）：柔光对比，根据前景亮度决定提亮或压暗，非交换律。
     10. **Add Sub**（p. 314）：以 0.5 为阈值，$F > 0.5$ 则加，$F < 0.5$ 则减，非交换律。
     11. **Overlay**（p. 314）：结合正片叠底与滤色（按背景 0.5 分割），非交换律。
     12. **Switch**（p. 317）：纯基于不透明度与裁剪范围的通道切换，满足交换律。
2. **PRACTICALLY DEMONSTRATED**：
   * 使用 Transformation 2D 平移/缩放纹理。
   * 使用 Levels 控制灰度白平衡与黑阶截断。
   * 观察灰度高度相加与相减在 3D 视口细分网格上的实际隆起与凹陷物理表现。
3. **MENTIONED / USED ONLY**：
   * 颜色通道混合时的色彩空间加权（如感知亮度加权未作展开）。

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
   * **高度图驱动全通道（Height-Driven Pipeline）**：先完成精准的高度轮廓混合，再利用 Curvature、AO、Normal 从高度图中派生所有表面光影与材质细节。
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

### Shah (2022) 教学范围与未教授盲区总结

在将 Shah (2022) 纳入本科 8 周教学设计时，必须清醒确认以下**已被一手正文确证的事实盲区**：

1. **未教授 PBR 底层理论**：全书仅把 PBR 作为默认软件模板，完全未解释 Fresnel 反射率、GGX 积分分布、能量守恒定律及金属/绝缘体微观差异（必须由 *The PBR Guide* 承担）。
2. **未教授 UV 展平工艺**：全书直接提供预展平的 FBX 资产，完全不涉及拓扑与接缝切割。
3. **未教授 Painter 中的 Geometry Mask 与 Symmetry Tool**：第 5 章的高级工具实操中，漏掉了对称工具和现代几何体列表隔离蒙版。
4. **未教授 Designer 中的高级数学与参数暴露**：第 7–10 章为初阶节点连线指南，完全未涉及 `$time`、自定义数学函数图、Pixel Processor，在第 10 章实战中也**未教授参数暴露（Expose Parameters）**。

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
   * 铁锈、油污、漆面属于绝缘体（非金属），一旦金属生锈氧化，必须立即转为绝缘体处理。
6. **线性工作流（Linear Space Rendering）**：
   * 物理渲染引擎的加减乘除计算必须在线性色彩空间（Gamma 1.0）中进行。
   * 人眼对暗部变化更敏感，显示器采用 sRGB（约 Gamma 2.2）编码显示。
   * **通道色彩空间黄金法则**：
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
     * 非金属：表征纯粹的漫反射反照率（Diffuse Albedo），**绝对禁止烘焙任何定向光照或投射阴影**。最暗非金属（木炭）不低于 30–50 sRGB，最亮非金属（雪）不高于 240 sRGB。
     * 金属：表征其在 0 度入射下的反射色彩（$F_0$），数值必须在 180–255 sRGB 之间。
   * **Metallic（Linear 灰度）**：
     * **二值化原则（Binary Mask）**：真实材质在物理上要么是金属（1.0 / 255 白色），要么是非金属（0.0 / 0 黑色）。
     * **过渡灰阶的唯一合法性**：仅允许出现在微观过渡边缘（抗锯齿边缘）或半透明污染层（极薄的灰尘、未完全氧化的极薄锈膜）。
   * **Roughness（Linear 灰度）**：
     * 0.0（纯黑）代表绝对光滑镜面，1.0（纯白）代表极度粗糙漫散。
2. **Specular/Glossiness 工作流对比**：
   * **Diffuse**：仅存储非金属的漫反射颜色；在金属区域为纯黑（0 sRGB）。
   * **Specular**：存储所有材质的 $F_0$ 镜面反射率。非金属区域填充 4% 左右的灰度色阶（30–75 sRGB），金属区域填充带色彩的高光反射率（180–255 sRGB）。
   * **Glossiness**：Roughness 的反相显示（1.0 光滑，0.0 粗糙）。
   * **优缺点权衡**：Metallic 工作流贴图占用内存小且能彻底防止艺术家因误配 Specular 数值破坏能量守恒定律；Specular 工作流则允许自由打破物理限制自定义非标准 $F_0$。
3. **通用辅助贴图规范**：
   * **Ambient Occlusion（AO，Linear 灰度）**：
     * **物理约束**：AO 仅代表环境漫反射光线被几何褶皱遮蔽的比例，**仅能且只能影响漫反射环境光（Diffuse Contribution），绝对不能遮挡镜面高光反射（Specular Contribution）**。
     * **贴图分离**：严禁将 AO 直接乘入 Base Color 贴图，必须作为独立通道提供给着色器。
   * **Tangent Space Normal（切线空间法线贴图）**：RGB 对应表面切线空间 XYZ 扰动向量，用于低模呈现高精度光影凹凸。
4. **Substance PBR 验证工具（PBR Validation Utilities）**：
   * 在 Designer/Painter 中挂载 `PBR Validate` 滤镜，根据金属度与反照率阈值实时标红/标黄违规像素（如过暗的非金属反照率、金属度错误的中间灰阶），强制执行工业合规。

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
  * 常见非金属绝缘体默认 $F_0$：线性 0.04 / sRGB 59。

---

## 两本教材在 8 周本科课程中的知识结构对照与边界沉淀

通过对 Shah (2022) 与 McDermott (2018) 的自下而上一手对齐，课程大纲的理论与实操分工界限得以彻底明确：

| 教学知识维度 | Wes McDermott (The PBR Guide 2018) | Zeeshan Jawed Shah (2022) | 8周课程分工与集成裁定 |
| :--- | :--- | :--- | :--- |
| **物理光学基础** | **深度专精**（微表面、BRDF、能量守恒、Fresnel $F_0$） | ❌ **未讲授**（直接选取 PBR 模板） | **第 1 周理论奠基**：强制以 *The PBR Guide Part 1* 为唯一定量标准。 |
| **色彩空间与数值安全** | **深度专精**（线性空间、sRGB/Linear 规则、PBR Validate） | ❌ **未展开**（仅在导入导出中默认操作） | **第 1–2 周规范**：必须贯彻 *The PBR Guide* 的反照率安全范围与线性通道定义。 |
| **Painter 软件操作与烘焙** | 仅概述 Substance 工具管线定位 | **深度专精**（烘焙7张网格图、Texel Density、顶点色ID） | **第 2–3 周实操重心**：以 Shah Ch 1–3 建立工程资产标准与烘焙流。 |
| **高级手绘与图层遮罩** | 仅给出材质层级概念原则 | **深度专精**（Stencil、投影、Clone、Smudge、Planar Mask） | **第 4–5 周技法拔高**：以 Shah Ch 4–5 驱动高精度细节风化实操。 |
| **智能材质与多集落灰** | 阐明材质复用价值 | **深度专精**（`.spsm`、Position Map 全局落灰、Anchor Point） | **第 5–6 周核心实战**：以 Shah Ch 6 手把手打通工业级 LookDev。 |
| **Designer 节点化材质** | 介绍 Substance 节点逻辑 | **系统初阶教学**（原子节点、12种混合模式数学、红砖墙/电视架） | **第 7 周模块拓展**：以 Shah Ch 7–10 培养程序化节点思维（明确不超纲至数学函数）。 |
| **参数暴露与工业封装** | 提及发布 `.sbsar` 与暴露参数 | ❌ **未讲授参数暴露**（Ch 10 电视架实战完全未暴露参数） | **教学法裁定**：由于 Shah 未教参数暴露，8 周课中 Designer 模块仅作为“纹理生成与非破坏性逻辑训练”，不强求学生掌握复杂函数暴露。 |
| **材质采集 (Sampler)** | 提及扫描材质理念 | **系统概览**（Ch 11 Image-to-Material、无缝平铺、石板路实战） | **第 7–8 周辅助拓展**：作为 AI 辅助工作流快速概览。 |

---
*本文档为 Gate 2.5A 独立成果，作为后续 Gate 2.5B（Provenance Audit & Page Reference Update）与 Gate 3（Teaching Value Matrix 修正）的唯一直接事实依据。*
