# 选定权威文献材质行为调研与初学者代表性材质集 (Bounded Material-Behavior Survey & Beginner Teaching Set)

> **文档定位**：本研究报告响应 GitHub Issue #20 契约及最新 Browser Review（技术 locator 与来源准确性审查）要求。报告首先呈现选定一手权威文献（OpenPBR Surface Specification, Adobe PBR Guide 3rd ed, Eran Dinur 2026 2nd ed）所界定的**有界材质物理行为调研（Bounded Material-Behavior Survey）**；在此基础上，根据 9 周本科初学者教学容量、认知阶梯与先修门槛，由本项目综合推演提出 M1–M8 初学者代表性材质教学原型集（Project Pedagogical Synthesis / Teaching Hypothesis），为下游案例审计（#19）与期末项目设计（#22）提供具有严格追溯性的物理依据。  
> **前置依赖**：`CONTEXT.md`（Blender 5.2.2 LTS Principled BSDF v2 环境锁定）。  
> **门禁状态**：`RESEARCH CANDIDATE ARTIFACT — PENDING BROWSER REVIEW`（不代替 #19 冻结拓扑，不替 #22 预设期末考核规则）。

---

## 1. 核心理论底座与一手文献来源 (Primary Technical Sources & Locators)

本研究严格区分“来源显式事实（Source Explicit Physics）”、“项目教学综合（Project Pedagogical Synthesis）”与“项目推论（Project Inference）”。所依赖的核心权威来源与精确章节点索引如下：

| 权威规范标识 | 出处与版本 | 精确章节点定位 (Traceable Locators) | 规范定位与提取要点 (Source-Backed Evidence) |
| :--- | :--- | :--- | :--- |
| **OpenPBR Surface** | Academy Software Foundation (ASWF, 2024–2026), *OpenPBR Surface Specification* | • Named Layer: `Base` (Diffuse & Base Metal)<br>• Named Layer: `Specular` (Roughness / Dielectric & Conductor)<br>• Named Layer: `Transmission` (Specular Transmission & Absorption)<br>• Named Layer: `Subsurface` (Subsurface Scattering)<br>• Named Layer: `Coat` (Clearcoat Layer)<br>• Named Layer: `Fuzz` (Microfiber Sheen)<br>• Named Layer: `Emission` (Luminescence)<br>• Named Layer: `Thin Film` (Wave Interference)<br>• Named Layer: `Geometry` (Bump & Normal Mapping) | 现代影视与工业开放材质标准。严格定义了物理分层因果（Base $\to$ Specular $\to$ Coat $\to$ Fuzz），并为每种高级光学行为提供了独立的能量平衡与参数接口规范。 |
| **Adobe PBR Guide** | Wes McDermott (2018), *The PBR Guide: A Handbook for Physically Based Rendering*, 3rd ed., Allegorithmic / Adobe | • Pt 1, pp. 18–27 (Light Rays, Absorption, Scattering, Microfacet Theory)<br>• Pt 1, pp. 30–37 (Energy Conservation, Fresnel Effect, F0, Conductors & Insulators)<br>• Pt 2, pp. 47–63 (Metal/Roughness Workflow: Base Color, Metallic, Roughness)<br>• Pt 2, pp. 74–79 (Common Maps: Ambient Occlusion, Height/Normal) | 实时与游戏行业事实标准。明确了金属度工作流语义（金属无漫反射，F0 编码于 Base Color；绝缘体 F0 约 4%）、微表面粗糙度高光散射，以及反照率安全区与线性工作流规范。 |
| **Dinur (2026)** | Eran Dinur (2026), *The Complete Guide to Photorealism for Visual Effects, Visualization, and Games*, 2nd ed., Routledge | • Ch 1 (Reality and Photorealism, pp. 9–21: 细节困境、微瑕疵与倒角高光磁铁)<br>• Ch 3 (Color, pp. 32–48: 六层解构模型、固有色与环境剥离)<br>• Ch 5 (Light Interaction, pp. 57–68: 吸收、漫散射、镜面反射、透射折射、Albedo)<br>• Ch 9 (Basic Material Properties, pp. 92–96: 绝缘体与金属导体光学本质、菲涅尔效应)<br>• Ch 11 (Rendering and Lighting, pp. 113–130: IBL 与环境光照质检)<br>• Ch 12 (Shading, pp. 131–142: 现代 BRDF 着色与能量守恒)<br>• Ch 13 (Texturing, pp. 143–156: 贴图因果与程序化控制)<br>• Ch 19 (Photorealism with Generative AI, pp. 207–227: AI 质检与控制边界) | 质感观察与外观开发（LookDev）权威方法论。章节点严格对齐仓库一手知识索引（`docs/research/source-native-knowledge-index.md`），强调材质因果律（Material Causality）与微表面粗糙度变异。 |
| **Khronos glTF 2.0** | Khronos Group, *glTF 2.0 Specification* | • §3.9.2 (Metallic-Roughness Material)<br>• §3.9.3 (Additional Textures: Normal, Occlusion, Emissive)<br>• §3.8.4 & §3.8.4.5 (Sampler & NPOT Texture Handling)<br>• §5.19.5 (`normalTexture`), §5.21 (`occlusionTexture`), §5.22.5 (`metallicRoughnessTexture`) | 工业实时交换标准。定义 `metallicFactor` 在 $[0, 1]$ 连续区间的 BRDF 线性插值混合行为，明确 OpenGL (+Y) 切线空间法线约定。 |

---

## 2. 选定规范有界材质行为调研与教学分类 (Bounded Behavior Survey & Pedagogical Synthesis)

依据教师访谈要求，检视选定权威规范所涵盖的材质物理与视觉行为维度。下表逐行明确区分**来源显式物理机制（Source Explicit Physics）**与**本项目教学综合判定（Project Pedagogical Synthesis）**：

| 物理行为维度 | 来源显式物理机制 (Source Explicit Physics) | 规范出处索引 (Exact Locators) | 项目教学综合判定 (Project Pedagogical Synthesis) | 教学准入依据与认知门槛分析 | 候选教学安排窗口 (Candidate Placement Window) |
| :--- | :--- | :--- | :---: | :--- | :---: |
| **基础介电质反射<br>(Dielectric Reflectance)** | 光线折射入内部经散射出射为漫反射；表面具弱高光（$F_0 \approx 0.04$），受菲涅尔效应支配。 | OpenPBR Layer `Base`<br>Adobe Pt 1 pp. 30–37<br>Dinur Ch 5 & 9 | **CORE**<br>(核心教学主干) | 建立“反照率（Albedo）剥离光影”的基石认知，破除初学者颜色常识误区。 | 候选窗口：W1–W2 阶段导入，贯穿全课 |
| **导电金属反射<br>(Conductor Reflectance)** | 自由电子吸收透射光（无漫反射），高光反射率高（70%–100%）且具波长选择性（有色高光）。 | OpenPBR Layer `Base`<br>Adobe Pt 1 pp. 34–37<br>Dinur Ch 9 | **CORE**<br>(核心教学主干) | 掌握金属度工作流核心法则，理解金属 Base Color 即为高光颜色的物理本质。 | 候选窗口：W2–W3 阶段攻坚 |
| **微表面粗糙度变异<br>(Roughness Variation)** | 微观几何法线扰动导致镜面反射光线弥散，决定高光斑的锐利/模糊程度。 | OpenPBR Layer `Specular`<br>Adobe Pt 1 pp. 24–27<br>Dinur Ch 1, 12, 13 | **CORE**<br>(核心教学主干) | 观察并表达岁月抚摸、摩擦抛光与灰尘粗糙，质感逼真度第一控制轴。 | 候选窗口：W2 起作为主线控制轴贯穿 |
| **法线与微起伏<br>(Normal / Bump Relief)** | 利用切线空间法线贴图扰动像素着色法线，在平整几何面上产生凹凸光影流动。 | glTF §3.9.3 & §5.19.5<br>OpenPBR Layer `Geometry`<br>Adobe Pt 2 pp. 78–79 | **CORE**<br>(核心教学主干) | 区分“表面轮廓剪影”与“微表面着色欺骗”，理解工业贴图烘焙与纹理表征。 | 候选窗口：W3 微实验或专项实操导入 |
| **物理分层与复合遮罩<br>(Layering & Masks)** | 基底与涂层物理叠加（如金属底材 + 绝缘色漆），遮罩受边缘磨损或凹陷脏迹因果驱动。 | OpenPBR Layer `Base` & `Coat`<br>Dinur Ch 3, 12, 13 | **CORE**<br>(核心教学主干) | 破除单一着色器思维，建立工业人造物“制造工艺 $\to$ 服役损坏”因果逻辑。 | 候选窗口：W3–W5 分层与细节进阶 |
| **清漆涂层<br>(Clearcoat Layer)** | 在粗糙介电质或金属基底上叠加一层薄透明反射涂层（带独立 IOR 与粗糙度）。 | OpenPBR Layer `Coat`<br>Dinur Ch 12 | **BOUNDED EXPOSURE**<br>(有界接触/启发) | 适用于陶瓷釉面或汽车烤漆，Principled BSDF v2 已内置 Coat 滑块，适于近迁移启发。 | 候选窗口：W6 近迁移或高阶示范 |
| **透射与透明折射<br>(Transmission / IOR)** | 入射光穿透物体产生屈光折射（Snell 定律），涉及表面粗糙度与内部透明吸收。 | OpenPBR Layer `Transmission`<br>Adobe Pt 1 p. 21<br>Dinur Ch 5 | **BOUNDED EXPOSURE**<br>(有界接触/预置) | 视觉吸引力高，但透射要求网格封闭且折射易受环境扭曲，初学者难以自主调试。 | 候选窗口：手电透镜提供预置参数，不作深调 |
| **表面自发光<br>(Emission)** | 表面主动向外辐射光能，不依赖外部反射。 | OpenPBR Layer `Emission`<br>glTF §3.9.3 | **BOUNDED EXPOSURE**<br>(有界接触/微量) | 技术原理简单直观，但易导致学生滥用破坏场景光影平衡。 | 候选窗口：手电灯珠或状态指示微量接触 |
| **微纤维光泽与绒毛<br>(Fuzz / Sheen)** | 微纤维（Microfibers）在物体边缘产生逆反射与前向天鹅绒般的高光漫晕（Velvet sheen）。 | OpenPBR Layer `Fuzz`<br>ASWF Spec (2024) | **DEFER**<br>(明确延后) | 属于织物与特定软质生物表面专项，不属于 9 周基础硬表面与工业质感主线。 | 明确排除于本 9 周教学范围 |
| **次表面散射<br>(Subsurface / SSS)** | 光线穿入半透明介质在内部多次散射后出射，产生柔和通透感（玉石、皮肤、蜡烛）。 | OpenPBR Layer `Subsurface`<br>Adobe Pt 1 pp. 20–25<br>Dinur Ch 5 | **DEFER**<br>(明确延后) | 计算昂贵，依赖模型真实物理尺度与闭合体积，极易混淆漫反射基础理解。 | 明确排除于本 9 周教学范围 |
| **各向异性<br>(Anisotropy)** | 微表面存在定向平行细纹（如拉丝金属、唱片），高光沿特定切线方向拉长。 | OpenPBR Layer `Specular`<br>ASWF Spec (2024) | **DEFER**<br>(明确延后) | 依赖复杂的网格切线（Tangents）与极坐标贴图，实时端兼容性差。 | 明确排除于本 9 周教学范围 |
| **薄膜干涉<br>(Thin-Film Interference)** | 光波在纳微米级薄膜（如油污膜、肥皂泡、高温回火层）上下界面反射产生波干涉彩虹纹。 | OpenPBR Layer `Thin Film`<br>ASWF Spec (2024) | **DEFER**<br>(明确延后) | 涉及高阶波动光学与复数折射率，超出本科基础教学认知负荷。 | 明确排除于本 9 周教学范围 |
| **参与介质与体积着色<br>(Volume / Absorption)** | 烟雾、浑浊水体内部的吸收与前向/后向散射系数计算。 | OpenPBR Layer `Transmission`<br>ASWF Spec (2024) | **DEFER**<br>(明确延后) | 属于环境与特效范畴，脱离表面着色（Surface Shading）本体。 | 明确排除于本 9 周教学范围 |

---

## 3. 初学者代表性材质原型教学集 (Beginner Teaching Set: M1–M8)

基于上述剪裁边界，本项目综合提炼出一套**结构化教学原型集（M1–M8 Teaching Archetypes）**。此套原型属于**项目教学综合假设（Project Pedagogical Synthesis / Hypothesis）**，旨在以渐进阶梯降低认知负荷，而非绝对的物理教条：

### 教学原型架构与创作建议
> **说明**：下述参数取值均为面向初学者的**建议参考范围（Illustrative starting reference / Teaching hypothesis）**，用于课堂指导与自查启发，绝非判断作品合格的绝对物理门槛。

1. **M1 纯净哑光介电质 (Matte Dielectric — 粉笔 / 石膏 / 干土)**：
   - **核心物理行为**：纯漫反射为主，高微表面粗糙度（参考建议：Roughness ~0.75–0.95），无强烈聚焦高光。
   - **参数创作惯例**：纯介电质遵循 `Metallic = 0.0` 约定；Base Color 代表漫反射反照率（参考范围：中间色阶，避免纯黑纯白极端值）。
   - **教学意图与误区**：破除“把素描阴影画进贴图”与“纯白即 255”的经验误区，建立光影剥离意识。
2. **M2 光滑施釉介电质 (Glossy Glazed Dielectric — 陶瓷釉面 / 光滑塑料)**：
   - **核心物理行为**：低微表面粗糙度（参考建议：Roughness ~0.05–0.20），具有清晰锐利的镜面菲涅尔反射。
   - **参数创作惯例**：`Metallic = 0.0`；高光颜色完全由入射光源决定；Base Color 提供底层吸收色。
   - **教学意图与误区**：破除“反光强就是金属”的错误直觉；纠正为了减弱高光而调高金属度的操作。
3. **M3 抛光纯净金属 (Polished Pure Metal — 镀铬 / 亮钢 / 镜面黄铜)**：
   - **核心物理行为**：几乎无漫反射，垂直入射反射率极高且具色彩倾向，低粗糙度（参考建议：Roughness ~0.05–0.15）。
   - **参数创作惯例**：纯金属遵循 `Metallic = 1.0` 创作约定；Base Color 直接作为镜面高光颜色。
   - **教学意图与误区**：理解金属度工作流语义（Base Color 变为高光色），纠正在无环境反射的黑背景下调试金属的盲目行为。
4. **M4 粗糙/工业金属 (Rough / Cast Metal — 铸铁 / 喷砂铝 / 机械拉丝件)**：
   - **核心物理行为**：导电体微表面起伏较大（参考建议：Roughness ~0.35–0.60），高光被大幅打散成宽厚光晕。
   - **参数创作惯例**：`Metallic = 1.0`；依靠 Base Color 与中高 Roughness 共同表达金属质感。
   - **教学意图与误区**：破除“金属必须像镜子一样反光”的刻板印象，理解粗糙度对导电体的物理散射作用。
5. **M5 复合带磨损漆面金属 (Coated Metal with Edge Wear — 机械外壳 / 涂漆器具)**：
   - **核心物理行为**：基底（金属 M4/M3）与面层（绝缘色漆 M1/M2）物理分层，受机械刮擦磨损露出底材。
   - **参数创作惯例**：双层通过黑白遮罩（Mask）隔离；漆面处 Metallic 约 0，露底处 Metallic 约 1；过渡边缘受抗锯齿控制。
   - **教学意图与误区**：掌握双层解耦因果结构；纠正在一个着色网络中用单滑块调出半金属半油漆的“幽灵材质”。
6. **M6 化学风化与锈蚀 (Oxidized Weathered Metal — 铁锈 / 铜绿 / 钝化金属)**：
   - **核心物理行为**：金属氧化生成介电质矿物层（多孔疏松、高粗糙度、红褐/青绿吸光），伴随表面微起伏。
   - **参数创作惯例**：锈斑区域物理性质跃迁（Metallic 衰减至 0，Roughness 升高至 ~0.80+，产生微法线凹凸）。
   - **教学意图与误区**：理解化学风化造成的“物理性质根本跃迁”，纠正“只改铁锈颜色而不改金属度与粗糙度”的错误。
7. **M7 空间沉积脏迹灰尘 (Spatial Contamination / Crevice Dust — 内凹积灰 / 缝隙油垢)**：
   - **核心物理行为**：空气粉尘或人体油脂覆盖于表面，大幅提升微表面粗糙度并抑制高光，分布受空间几何因果驱动。
   - **参数创作惯例**：沉积物作为介电微粒（Metallic = 0，Roughness 偏高）；空间分布主要由环境光遮蔽（AO）与内凹槽驱动。
   - **教学意图与误区**：建立物体与服役环境交互的因果意识，纠正全表面均匀抹灰或在频繁抚摸的凸起手柄上绘制厚灰的盲目操作。
8. **M8 纹理微浮雕结构 (Textured Micro-Relief — 防滑滚花 / 冲压细纹 / 细致凹凸)**：
   - **核心物理行为**：宏观网格面数平整，通过切线空间法线贴图（Normal Map）扰动着色计算，实现凹凸光影流动。
   - **参数创作惯例**：法线贴图采用标准切线空间（OpenGL +Y）；色彩空间严格标定为 `Non-Color`。
   - **教学意图与误区**：建立“着色欺骗并非宏观几何形变”的心智模型，理解切线法线对光照倾斜角的敏感响应。

---

## 4. 候选教学案例覆盖度评估矩阵 (Candidate Asset Coverage Matrix)

本节基于仓库已验证的资产事实（Provenance-Verified Baseline），对照 M1–M8 原型集进行映射分析。对未获实测证据支撑的细节，严格标定为**项目推论（Project Inference）**：

### 4.1 候选资产已有仓库事实基准 (Asset Provenance Baseline)
- **Poly Haven `Vintage Flashlight`**（CC0 1.0 Universal，作者：Omar M. El-Safy）：
  - `[PROVENANCE VERIFIED]`: 约 11K 三角面（~11K tris），UV 已展开；
  - `[PROVENANCE VERIFIED]`: 官方材质构成：红色绝缘漆外壳（Red dielectric paint）、裸金属（Bare metal）、黑色橡胶/塑料把手（Black rubber/plastic）、镀铬反光碗（Chrome reflector）与玻璃透镜（Glass lens）；
  - `[PROJECT INFERENCE / REQUIRES ASSET INSPECTION]`: 电池仓内部氧化锈蚀（M6）、细微缝隙积灰分布（M7）、握柄处防滑滚花法线贴图适配度（M8），属于推论性教学设想，需在实测中进一步核验。
- **Poly Haven `Antique Ceramic Vase 01`**（CC0 1.0 Universal，作者：James Ray Cock）：
  - `[PROVENANCE VERIFIED]`: 约 9K 三角面（~9K tris），包含完整展开 UV；
  - `[PROVENANCE VERIFIED]`: 官方材质构成：高反光玻璃质光滑釉面、开片微裂纹法线、青花釉下彩，以及底部露胎素烧粗陶底圈。
- **古典石膏胸像套件 (`Classical Bust Bundle`)**：
  - `[PROVENANCE VERIFIED]`: 纯哑光石膏材质。

### 4.2 案例原型覆盖度映射表

| 代表性材质原型 | 手电筒主资产<br>(Vintage Flashlight) | 陶瓷花瓶迁移载体<br>(Antique Ceramic Vase 01) | 古典石膏胸像微实验<br>(Classical Bust) | 历史参考案例<br>(Legacy Reference Projects) | 原型覆盖度分析与替代性评估 (Pedagogical Assessment) |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **M1: 哑光介电质** | ⚪ 局部弱<br>(把手橡胶衬垫) | ⚪ 局部弱<br>(底部未上釉泥胎圈) | **🟢 极强<br>(全器物纯哑光石膏)** | 🟡 部分具备<br>(旧课件墙体/泥土) | 手电筒缺乏大面积均质哑光面；石膏胸像或类似漫反射模型是快速建立 M1 概念的高效微载体。 |
| **M2: 光滑施釉介电质** | ⚪ 缺乏<br>(无大面积高光釉面) | **🟢 极强<br>(全器身玻璃态釉面)** | ❌ 无<br>(石膏无釉) | ⚪ 偶有涉及 | 手电筒缺乏大面积非金属镜面高光；陶瓷花瓶能承载 M2，亦可评估木器清漆或其他光滑塑料器具作为备选。 |
| **M3: 抛光纯净金属** | **🟢 极强<br>(镀铬反光碗/金属件)** | ❌ 无 | ❌ 无 | 🟡 部分具备 | 手电筒反光碗提供镜面金属高光对照样本。 |
| **M4: 粗糙工业金属** | **🟢 极强<br>(磨损裸金属底材)** | ❌ 无 | ❌ 无 | 🟡 部分具备 | 手电外壳磕碰露出的金属底材能展现工业金属粗糙度散射。 |
| **M5: 复合带磨损漆面** | **🟢 极强<br>(外壳红漆与边缘剥落)** | ❌ 无 | ❌ 无 | 🟢 传统强项 | 手电筒为 M5 提供了典型的“底材-面漆-外缘剥落”物理因果支撑。 |
| **M6: 化学风化锈蚀** | 🟡 待核实<br>*(Project Inference)* | ❌ 无 | ❌ 无 | 🟡 部分具备 | 手电筒是否具备自然锈蚀承载点尚待实测；大面积锈蚀需补充局部案例或替代资产。 |
| **M7: 空间沉积积灰** | 🟡 待核实<br>*(Project Inference)* | 🟡 局部中<br>(瓶口沿/瓶底积灰) | 🟡 局部中<br>(石膏雕像凹陷褶皱) | 🟡 部分具备 | 手电筒接缝结构被推论适合环境遮蔽（AO）积灰，需在模型网格上最终确认。 |
| **M8: 纹理微浮雕法线** | 🟡 待核实<br>*(Project Inference)* | ⚪ 局部弱<br>(釉面微开片纹) | **🟢 极强<br>(高模烘焙微细节)** | 🟡 部分具备 | 手电筒滚花贴图与石膏雕刻均能承载切线法线教学，视最终资源配套而定。 |

---

## 5. 初学者材质物理诊断参考指标 (Candidate Diagnostic Reference Checks)

本节提炼出 5 项基于微表面物理行为的诊断观察指标，属于**参考诊断启发（Candidate Diagnostic Checks）**，非正式考核评分细则（具体评分规则留待 Issue #22 配合教务大纲确定）：

1. **导电/绝缘二元性启发 (Metallic Authoring Heuristic)**：
   - 纯净宏观均质材质建议遵守“非 0 即 1”创作惯例（绝缘体取 0，纯金属取 1）；若发现大面积 0.3~0.7 中间浮点数，教师应提示核查是误用半金属还是抗锯齿过渡。
2. **反照率明度安全范围 (Albedo Value Range Heuristic)**：
   - 自然界非金属漫反射反照率 sRGB 明度通常分布于中间色阶（经验参考区间约 30–240）；若出现纯黑或纯白，提示核查是否混入环境阴影或过曝高光。
3. **微表面粗糙度变异性 (Roughness Variation)**：
   - 检查全模型是否使用常量 Roughness（导致缺乏真实细节）；手常抚摸处粗糙度是否适度降低，积灰处是否适度升高。
4. **法线贴图切线空间与色彩空间 (Normal Map Color Space & Orientation)**：
   - 切线法线记录向量数据，必须标定为 `Non-Color`；若视口出现异常黑斑，优先自查贴图节点色彩空间；旋转光源观察凹凸朝向是否正常。
5. **分层因果逻辑自洽性 (Layering Causality)**：
   - 磨损通常发生于易碰撞的外凸棱角；脏迹通常滞留于避风避光的内凹缝隙；避免无规则数学噪波全模型均匀覆盖。

---

## 6. 与上下游研究工单的接口关系 (Interfaces & Open Questions)

1. **对 Issue #19 (教学案例与拓扑审计) 的接口**：
   - 本调研呈现了 M1–M8 材质行为维度与选定规范全景。#19 应基于此行为空间，审计候选案例的教学覆盖度与拓扑结构，评估“单一资产贯穿”、“分阶段替换案例”或“主案例+有界微案例”的可行性与时间成本；
   - 证明了单一手电筒资产在 M1（漫反射哑光）与 M2（高光玻璃态釉面）上存在天然局限，但花瓶仅为 M2 候选之一，保留其他非金属替代案例的评估可能性。
2. **对 Issue #22 (综合期末大作业设计) 的接口**：
   - 本文提出的“5 项诊断参考指标”可作为期末作品质检的技术参考维度，但不提前冻结具体评分占比或硬性通过/挂科标准。
3. **未决决策边界 (Unresolved Decisions for Course Owner & #19 Join)**：
   - M6（氧化锈蚀）与 M7（缝隙积灰）在手电筒上的实际承载性需通过模型实测验证；
   - 最终的案例拓扑选择（如选项 4 解耦模型 vs 选项 3 混合模型）需在 #19 Join Gate 正式裁定。
