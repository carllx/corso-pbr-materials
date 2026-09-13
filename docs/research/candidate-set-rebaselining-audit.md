# Candidate Set Re-baselining Audit: From Historical Baseline v1 to Proposed Candidate Set v2

> **Gate**: Gate 2.5A.5 — Candidate Set Re-baselining Audit  
> **Repository**: `carllx/corso-pbr-materials`  
> **Anchor Commit**: `275dc4db88b417a688ef20d628efd49fbbcb1f84` (Gate 2.5A Source Research Consolidated PASS)  
> **Governance Context**: Governed by Issue #3 (Stage 2 Strategy Clarification) and Issue #4 (Gate 2.5 Execution Tracker).  
> **Primary Purpose**: Re-evaluate the historical 57-candidate capability baseline formed in Phase 1 / early Phase 2 against first-party source-native research (OpenPBR, MaterialX/UsdShade, Painter, Designer, Sampler, Blender, Unreal/Substrate) and AI impact evidence, testing whether the capability map describes the durable competencies students truly need in an era of AI Agents, structured material representations, controlled revision, visual validation, and target delivery.

---

## Part 1 — Audit Principles & Methodology

### 1.1 The Baseline vs. The Target
- **Candidate Set v1 (Historical Baseline)**: 57 units (44 traditional units across 6 modules + 13 AI-native candidate units) cataloged in `curriculum-coverage-matrix.md` and `teaching-source-provenance.md`.
- **v1 Was Formed Under Specific Historical Biases**:
  1. *Software/GUI Inertia*: Several units reflected specific software panels, default button workflows, or manual authoring steps rather than durable, transferable competencies.
  2. *Operation vs. Capability Confusion*: Conflating repetitive manual GUI manipulations with higher-order causal reasoning and physical judgment.
  3. *Missing Representation Seams*: v1 had limited awareness of structured material representation formats (MaterialX, OpenUSD/UsdShade), representation selection, and the critical distinction between `Valid Representation ≠ Visual Equivalence ≠ Production Deliverable`.
  4. *Missing Controlled Revision Seams*: v1 assumed material authoring was predominantly greenfield "creation" (blank canvas $\to$ final asset), lacking formal treatment of edit locality, parameterization, and localized non-destructive modification under AI/generative iterations.
- **Proposed Candidate Set v2**: The target capability set resulting from this audit. **The candidate count is not constrained to 57**. 57 is neither a ceiling nor a floor; preservation of 57 by inertia is explicitly forbidden.

### 1.2 Allowed Disposition Taxonomy
For every candidate in v1, exactly one disposition is assigned:
1. `KEEP_AS_IS`: The capability definition remains conceptually sound, correctly framed at the transferable competency level, and supported by source evidence.
2. `CANDIDATE_REFRAME` (formerly `REFRAME`): The underlying capability remains vital, but historical wording was overly software-centric, GUI-centered, manual-operation-centered, or vendor-specific. It is rewritten as a transferable, durable capability. *(Note: This is an audit definition reframe, distinct from Gate 3 teaching-action reframing)*.
3. `MERGE`: Multiple historical units collapse into a single higher-order capability because keeping them separate artificially inflates manual micro-operations.
4. `SPLIT`: A historical unit conflated two or more fundamentally distinct competencies in modern/AI pipelines (e.g., authoring vs. validation; generative inference vs. de-lighting correction; interchange representation vs. target runtime adaptation).
5. `RETIRE_OR_DEFER`: The unit no longer justifies an independent candidate slot for Gate 3 consideration (e.g., automated by basic tools/agents, merged away, or merely an implementation detail).
6. `ADD`: Authoritative evidence reveals a durable capability completely unexpressed in the historical 57.

### 1.3 Mandatory Future-Facing Audit Dimensions
Every audit decision is tested against 10 core dimensions:
- **A. Material / Appearance Causality**: Physics, geometry, scale, lighting, camera, and display jointly producing appearance.
- **B. Representation Choice**: Textures vs. shader parameters vs. procedural graph vs. MaterialX vs. OpenPBR vs. engine-native assets.
- **C. Representation Loss Awareness**: What is lost during conversion ($A \to B$)? (`Valid Representation ≠ Visual Equivalence ≠ Production Deliverable`).
- **D. Controlled Revision / Edit Locality**: Modifying a specific requirement without destabilizing the whole asset (channel isolation, mask locality, parameter tweak).
- **E. Maintainability / Reuse / Parameterization**: Parameter exposure, modular subgraphs, deterministic reproducibility, versionability.
- **F. Agent Operability**: Structured graphs, machine-readable representations, clear APIs, deterministic execution enabling AI Agent interaction.
- **G. Generative vs. Retrieval vs. Parametric Reuse**: Knowing when to generate, retrieve, proceduralize, or manually paint.
- **H. Validation / Diagnosis / Visual QA**: Multi-environment lighting stress test, cross-channel consistency, scale check, de-lighting audit, failure detection.
- **I. Target Delivery / Lifecycle**: VFX/Animation (binding, lookdev consistency) vs. Realtime/Game (packing, instances, performance budgets).
- **J. Human Art Direction & Judgment**: Aesthetic intent, physical plausibility, reference comparison, and acceptance criteria that remain human responsibilities even when execution is automated.

### 1.4 Evidence Threshold & Lineage Rule
- Every change (`CANDIDATE_REFRAME`, `MERGE`, `SPLIT`, `RETIRE_OR_DEFER`, `ADD`) cites evidence classes ($A, B, C, D$) and authoritative documents.
- If an idea is only supported by $E$ (Project Inference Only), it is isolated as an `UNRESOLVED STRUCTURAL HYPOTHESIS` and cannot reshape Candidate Set v2.
- Full lineage from v1 ID to v2 ID is maintained with zero orphaned items.

---

## Part 2 — Full v1 $\to$ v2 Mapping & Audit Table

### Module 1: Material Literacy (Physical Optics & Theoretical Foundations) — Historical 10 Units

| v1 ID | Historical Capability (v1) | Disposition | Proposed v2 Capability / Target | Owning Evidence & Class | Rationale & Gate 3 Impact |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **M01-U01** | 现实材质观察与参考分析 *(Material Observation & Reference Analysis)* | `KEEP_AS_IS` | **V02-C01: 现实材质物理属性观察与多维参考解构** *(Physical Material Observation & Multi-attribute Reference Decomposition)* | Dinur (2026) Ch 1, 3 (`B`); RTR4 Ch 9.1 (`D`) | 核心人类审美与因果分析基石。AI 自动生成无法替代人眼对真实物理世界多尺度瑕疵与色彩层次的解构能力。直接决定 Gate 3 核心素养地位。 |
| **M01-U02** | PBR 物理可信性与能量守恒 *(PBR Plausibility & Energy Conservation)* | `KEEP_AS_IS` | **V02-C02: PBR 物理可信性与辐射度能量守恒** *(PBR Physical Plausibility & Radiometric Energy Conservation)* | McDermott (2018) pp. 29–30 (`B`); RTR4 Ch 9.2–9.3 (`D`); OpenPBR Spec §1.1 (`C`) | 跨光照环境不失真的不可动摇物理铁律。生成模型生成的贴图频繁违背能量守恒，必须由学生进行因果诊断与能量校验。 |
| **M01-U03** | Base Color 反射率与安全色阶 *(Base Color Reflectance & Safe Values)* | `CANDIDATE_REFRAME` | **V02-C03: 漫反射/镜面反射率安全区间与去光照纯度判定** *(Reflectance Safe Ranges & Albedo Delighting Purity)* | McDermott (2018) pp. 48–52 (`B`); OpenPBR Spec §3.1 (`C`); Dinur (2026) Ch 3 (`B`) | 历史表述侧重 sRGB 绝对数值死记硬背。重构为“电介质反射率安全阈值判定与 Base Color 中阴影/高光污染的物理诊断”，直接指导 AI 生成贴图的质量验收。 |
| **M01-U04** | Roughness 微表面粗糙度模型 *(Roughness & Microfacet Theory)* | `KEEP_AS_IS` | **V02-C04: 微表面粗糙度理论与微观几何法线分布** *(Microfacet Theory & Roughness NDF)* | McDermott (2018) pp. 22–27 (`B`); RTR4 Ch 9.2 (`D`); OpenPBR Spec §3.2 (`C`) | GGX 微表面法线分布（NDF）与高光衰减的核心理论。决定高光斑锐利度、模糊过渡与光照反应，为材质真实感的决定性维度。 |
| **M01-U05** | Metallic 金属度二值准则 *(Metallic Classification & Boundary Rules)* | `KEEP_AS_IS` | **V02-C05: 金属导体与电介质光学分类与金属度边界准则** *(Conductor vs. Dielectric Optical Classification & Metallic Boundary Rules)* | McDermott (2018) pp. 33–37, 53–55 (`B`); RTR4 Ch 9.4 (`D`); OpenPBR Spec §3.1 (`C`) | 纯物质非金即绝缘的光学本质。控制 F0 反射率来源；中间过渡灰阶的物理合法性（氧化锈蚀、极薄灰尘、抗锯齿像素）诊断是防止 AI 生成产生伪金属噪点的核心。 |
| **M01-U06** | Normal 切线空间法线原理 *(Tangent Space Normal Principles)* | `KEEP_AS_IS` | **V02-C06: 切线空间法线几何扰动原理与跨坐标系对齐** *(Tangent Space Normal Principles & Coordinate Alignment)* | Shah (2022) pp. 45–48 (`A`); McDermott (2018) pp. 76–79 (`B`); Blender Manual (`C`) | 宏观几何与微观着色扰动的桥梁。DirectX (Y-) 与 OpenGL (Y+) 绿通道及切线空间基底对齐是跨工具/引擎交付中最频繁的失效点。 |
| **M01-U07** | Height / Displacement 几何置换 *(Height & Displacement Mapping)* | `KEEP_AS_IS` | **V02-C07: 视差映射与几何置换原理** *(Parallax Occlusion & Geometric Displacement Mapping)* | Shah (2022) Ch 9–10 (`A`); McDermott (2018) p. 75 (`B`); Sampler Docs (`C`) | 从微观着色法线跨越到真实网格形变（POM/Displacement）的关键。驱动程序化雕刻、物理破损与轮廓级几何变化。 |
| **M01-U08** | Ambient Occlusion 环境遮挡作用 *(Ambient Occlusion Role & Limits)* | `KEEP_AS_IS` | **V02-C08: 环境光遮蔽物理意义与漫反射解耦** *(Ambient Occlusion Role & Diffuse Decoupling)* | McDermott (2018) p. 74 (`B`); Painter Baking Docs (`C`) | 模拟微观缝隙接触阴影，严格与直接光照和 Base Color 固有色解耦，杜绝传统把 AO 烘死在固有色里的非物理错误。 |
| **M01-U09** | 表面细节尺度与频率认知 *(Detail Scales: Macro, Medium, Micro)* | `KEEP_AS_IS` | **V02-C09: 表面细节多级频率与空间尺度解构** *(Multi-frequency Surface Detail Decomposition: Macro/Medium/Micro)* | Dinur (2026) Ch 1, 3 (`B`); Shah (2022) Ch 3–6 (`A`) | 跨软件图层堆栈、节点网络与风化破损组织的结构性思维基石。宏观结构、中频磨损与微观噪波必须分层控制。 |
| **M01-U010** | sRGB 与 Linear 色彩空间规范 *(Color Space: sRGB vs. Linear/Non-Color)* | `KEEP_AS_IS` | **V02-C10: 色彩管理与线性管线规范** *(Color Management & Linear Workflow Specification: sRGB vs. Linear/Data)* | McDermott (2018) pp. 38–39 (`B`); OpenPBR Spec §1.2 (`C`); RTR4 Ch 5.6 (`D`) | 数据贴图（Linear/Non-Color）与色彩贴图（sRGB/ACEScg）的数学处理差异。材质资产跨 DCC/引擎导入导出时最基础但最易破坏物理正确性的防线。 |

---

### Module 2: Texture-based Authoring (Asset-level Multi-channel Craft) — Historical 8 Units

| v1 ID | Historical Capability (v1) | Disposition | Proposed v2 Capability / Target | Owning Evidence & Class | Rationale & Gate 3 Impact |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **M02-U01** | Painter 工程设置与色彩管理 *(Painter Project Setup & OCIO/ACES)* | `CANDIDATE_REFRAME` | **V02-C11: 贴图工程架构、通道配置与色彩管理绑定** *(Texture Project Architecture, Channel Setup & Color Management Binding)* | Shah (2022) Ch 1 (`A`); Painter Official Docs (`C`) | 历史表述将能力绑定于 Painter 单一软件的初次向导点击。重构为跨工具通用的资产贴图工程初始化、材质集（Texture Sets）多网格管理及 OCIO/ACES 色彩管理管线绑定。 |
| **M02-U02** | 图层结构与多通道同步管理 *(Layer Stack & Multi-channel Sync)* | `KEEP_AS_IS` | **V02-C12: 非破坏性图层系统与多物理通道同步求值** *(Non-destructive Layer Stacking & Synchronized Multi-channel Evaluation)* | Shah (2022) Ch 3 (`A`); Painter Layer Docs (`C`) | 资产级材质创作的组织核心。Fill Layer / Paint Layer 的多通道独立混合模式（Color, Rough, Metal, Normal, Height 同步运算）是实现非破坏性编辑的前提。 |
| **M02-U03** | 遮罩体系与手绘特征细节 *(Mask Hierarchy & Feature Hand-painting)* | `CANDIDATE_REFRAME` | **V02-C13: 空间局部遮罩体系、投影绘制与特征细节修饰** *(Spatial Mask Hierarchy, Viewport Projection Painting & Feature Detailing)* | Shah (2022) Ch 4–5 (`A`); Painter Official Docs (`C`) | 历史表述偏向“纯手工画画”。重构为“三维视口投影、几何多边形填充、黑白通道遮罩与局部特征修补”。即使底层被 AI 生成，局部接缝与特定划痕依然需要空间遮罩精确控制。 |
| **M02-U04** | 智能材质 (Smart Materials) 组织 *(Smart Materials System & Encapsulation)* | `MERGE` | **合并入 V02-C14** | Shah (2022) Ch 6 (`A`); Painter Docs (`C`) | 智能材质与智能生成器在底层皆属于“基于几何烘焙贴图驱动的自适应图层模板与封装系统”。合并为一个高层模块，避免人为拆分成琐碎的 GUI 面板操作。 |
| **M02-U05** | 智能生成器 (Generators) 驱动逻辑 *(Generators Driven by Mesh Maps)* | `MERGE` | **合并入 V02-C14** | Shah (2022) Ch 4, 6 (`A`); Painter Docs (`C`) | 见 M02-U04。共同合并为 **V02-C14: 几何特征驱动的自适应材质分层封装与模板复用**。 |
| **M02-U06** | 材质分层逻辑 (Base $\rightarrow$ Detail) *(Material Stratification: Substrate to Wear)* | `KEEP_AS_IS` | **V02-C15: 材质物理工艺分层与底材-涂层-风化因果演变** *(Material Stratification & Substrate-to-Wear Physical Chronology)* | Shah (2022) Ch 4–6 (`A`); Dinur (2026) Ch 5, 13 (`B`) | 工业工艺学在数字材质中的映射：底材（裸金属/塑料）$\to$ 涂层底漆 $\to$ 表面面漆 $\to$ 机械划伤剥落 $\to$ 环境侵蚀氧化 $\to$ 表层积灰。决定材质真实感与叙事厚度。 |
| **M02-U07** | 风化与磨损物理逻辑 (Weathering) *(Weathering, Aging & Contact Logic)* | `CANDIDATE_REFRAME` | **V02-C16: 环境风化、接触磨损与空间位置因果模拟** *(Environmental Weathering, Contact Abrasion & Spatial Position Causality)* | Shah (2022) Ch 6 (`A`); Dinur (2026) Ch 5 (`B`) | 历史表述偏软件做旧滤镜。重构为“依据力学接触点（外露凸起边角磨损）、重力沉积（Position Y 积尘积水）、流体冲刷与环境交互等因果逻辑进行材质老化推演”。 |
| **M02-U08** | 贴图导出模板与通道配置 *(Export Presets & Channel Packing)* | `CANDIDATE_REFRAME` | **V02-C17: 目标引擎贴图格式转译与通道映射配置** *(Target Engine Texture Export Translation & Channel Mapping Configuration)* | Shah (2022) Ch 6 (`A`); Painter Docs (`C`) | 历史表述局限于 Painter 点击 Export 预设。重构为“根据下游渲染器/游戏引擎（Arnold/Unreal/glTF）的物理接口规范，执行通道重组、位深度匹配与色彩空间元数据标记”。 |

---

### Module 3: Supporting Pipeline Knowledge (Prerequisites & Baking) — Historical 5 Units

| v1 ID | Historical Capability (v1) | Disposition | Proposed v2 Capability / Target | Owning Evidence & Class | Rationale & Gate 3 Impact |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **M03-U01** | UV 参数化展开与接缝切分 *(UV Parameterization & Seam Layout)* | `CANDIDATE_REFRAME` | **V02-C18: UV 参数化质量评估、接缝布局与拉伸诊断** *(UV Parameterization Quality Assessment, Seam Layout & Distortion Diagnosis)* | Shah (2022) Ch 1 (`A`); Painter Docs Auto Unwrap (`C`); McDermott (2018) pp. 60–63 (`B`) | 本课程非建模拓扑课。重构为“UV 参数化质量评估、视口接缝（Seam）合理性检查与纹理形变拉伸诊断”，重点在于评估与指导自动/外部展开质量，而非从零手撕 UV。 |
| **M03-U02** | 接缝与硬边对应原则 *(UV Seams vs. Hard Edges Matching)* | `KEEP_AS_IS` | **V02-C19: 模型光滑组硬边与 UV 接缝拓扑协同准则** *(Hard Edges vs. UV Seams Topological Alignment & Artifact Prevention)* | McDermott (2018) pp. 60–63 (`B`); RTR4 Ch 6 (`D`) | 刚性几何拓扑与烘焙数学法则。硬边处必须切开 UV 接缝以防止顶点法线插值计算出黑边/渐变穿帮。极高排错与排险价值。 |
| **M03-U03** | 像素密度规划 (Texel Density) *(Texel Density Planning & Scaling)* | `KEEP_AS_IS` | **V02-C20: 纹素密度规划、一致性分配与跨资产对齐** *(Texel Density Planning, Consistency Budgeting & Asset Alignment)* | Shah (2022) Ch 1 (`A`); McDermott (2018) pp. 58–60 (`B`) | 资产级乃至场景级视觉品质均一的决定性指标。防止同一个道具上出现局部模糊、局部极度锐利的纹素失配。 |
| **M03-U04** | 高低模映射关系与拓扑准备 *(High-to-Low Poly Mapping & Topology)* | `MERGE` | **合并入 V02-C21** | Shah (2022) Ch 1 (`A`); Painter Baking Docs (`C`) | 高低模拓扑准备本身是贴图烘焙的前提环节，将其与贴图烘焙及失配排错合并为一个完整的“几何细节投射与烘焙”能力单元。 |
| **M03-U05** | 关键贴图烘焙 *(Mesh Maps Baking: Normal/AO/Curvature)* | `MERGE` | **合并入 V02-C21** | Shah (2022) Ch 1 (`A`); Painter Baking Docs (`C`) | 与 M03-U04 合并为 **V02-C21: 几何细节投影烘焙、网格贴图派生与烘焙伪影诊断** *(Geometric Detail Baking, Mesh Map Derivation & Artifact Diagnosis)*。包含高低模包裹笼（Cage）、射线投射、Paint Skew 斜切修复与法线反转排错。 |

---

### Module 4: Procedural / Parametric Materials (Procedural Nodes & Systems) — Historical 10 Units

| v1 ID | Historical Capability (v1) | Disposition | Proposed v2 Capability / Target | Owning Evidence & Class | Rationale & Gate 3 Impact |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **M04-U01** | 节点着色器架构 (Shader Nodes) *(Node-based Shader Graph Architecture)* | `CANDIDATE_REFRAME` | **V02-C22: 结构化节点图架构与数据流拓扑原理** *(Structured Shader Graph Architecture & Directed Dataflow Topology)* | Shah (2022) Ch 7 (`A`); Blender Manual Shader Nodes (`C`); Designer Docs (`C`); MaterialX Spec (`C`) | 历史表述偏向具体软件界面的连线基础。重构为通用的“有向无环图（DAG）数据流、强类型系统（标量、向量、色彩、表面接口）与复合子图拓扑”，直接为程序化合成、MaterialX 及 Agent 机器读写奠定心智模型。 |
| **M04-U02** | 纹理坐标系 *(Texture Coordinates: Generated, Object, UV)* | `KEEP_AS_IS` | **V02-C23: 多维空间纹理坐标系转换与映射逻辑** *(Texture Coordinate Systems & Spatial Mapping: UV, Object, World, Triplanar)* | Blender Manual (`C`); Shah (2022) Ch 7–8 (`A`); Designer Docs (`C`) | 区分 UV 平面、包围盒 Generated、三维 Object 空间与三平面投影（Triplanar）。摆脱模型 UV 依赖、实现无拉伸自然程序化铺底的核心。 |
| **M04-U03** | 算法纹理与噪声 *(Procedural Noise & Patterns: Perlin/Voronoi)* | `KEEP_AS_IS` | **V02-C24: 程序化算法噪波与自然图案合成** *(Procedural Noise Generators & Mathematical Pattern Synthesis)* | Shah (2022) Ch 8 (`A`); Blender Manual (`C`); Designer Docs (`C`) | 利用 Perlin/Simplex/Voronoi 等数学函数生成连续有机质感、开裂裂纹与高频细节。是参数化材质自洽无限分辨率的源泉。 |
| **M04-U04** | 数学运算与混合遮罩 *(Math Operations & Mix Masks)* | `MERGE` | **合并入 V02-C25** | Shah (2022) Ch 9 (`A`); Blender Manual Math/Mix Nodes (`C`) | 算术运算（Add, Multiply, Min/Max）与色彩/区间重映射在节点网络中是紧密一体的数据调理过程。分开导致微观连线碎片化。 |
| **M04-U05** | 色彩映射与区间重映射 *(ColorRamp & Range Remapping)* | `MERGE` | **合并入 V02-C25** | Shah (2022) Ch 9 (`A`); Blender Manual ColorRamp/MapRange (`C`) | 与 M04-U04 合并为 **V02-C25: 节点数学运算、通道混合与数值区间重映射** *(Node Mathematics, Channel Blending & Range Remapping)*。 |
| **M04-U06** | 映射缩放与平铺控制 *(Mapping, Scale & Tiling Control)* | `KEEP_AS_IS` | **V02-C26: 纹理空间变换、真实物理尺度对齐与平铺控制** *(Texture Spatial Transformation, Metric Scale Calibration & Tiling Control)* | Shah (2022) Ch 8 (`A`); Sampler Docs Physical Size (`C`); Blender Manual (`C`) | 将虚拟贴图坐标映射与现实世界公制物理尺寸（Real-world Metric Scale）对齐，消除平铺接缝与比例失真的关键能力。 |
| **M04-U07** | 随机化与多变异质感 *(Randomization & Multi-variation)* | `KEEP_AS_IS` | **V02-C27: 对象随机变体、种子控制与重复感消除** *(Object-level Variation, Seed Randomization & Tiling Pattern Breaking)* | Blender Manual Object Info (`C`); Designer Tile Sampler Docs (`C`) | 大规模资产复用时打破“瓷砖感/贴图重复痕迹”的不可或缺技能。通过随机种子（Seed）与位置扰动实现一套材质生成多样外观。 |
| **M04-U08** | 节点组封装与参数暴露 *(Node Group Encapsulation & Interface)* | `CANDIDATE_REFRAME` | **V02-C28: 模块化子图封装与有意义的参数接口暴露** *(Modular Subgraph Encapsulation & Meaningful Parameter Interface Design)* | Shah (2022) Ch 7 (`A`); Designer Values Docs (`C`); Blender Node Groups (`C`) | 历史表述局限于“右键打包节点组”。重构为“黑盒模块化抽象、参数暴露、定义合法数值区间与标签，为下游艺术家或自动化脚本构建易读的母材质控制面板”。 |
| **M04-U09** | 独立程序化纹理与 `.sbsar` 母版生成 *(Standalone Procedural Texture & `.sbsar`)* | `CANDIDATE_REFRAME` | **V02-C29: 可复用参数化材质资产打包与动态运行时集成** *(Reusable Parametric Material Packaging & Dynamic Runtime Integration)* | Designer User Guide (`C`); Shah (2022) Ch 10 (`A`) | 历史表述绑定于 Designer 专属 `.sbsar`。重构为“参数化材质包的编译、跨软件分发机制以及在宿主引擎运行时通过插件/API 动态调参的系统原理”。 |
| **M04-U10** | 程序化结果烘焙为 PBR 贴图包 *(Baking Procedural to PBR Texture Set)* | `CANDIDATE_REFRAME` | **V02-C30: 程序化节点网络向标准位图集的静态烘焙与精度控制** *(Procedural Graph Baking to Static Bitmap Sets & Bit-depth Precision Control)* | Shah (2022) Ch 10 (`A`); Blender Render Baking Docs (`C`); SAT Docs (`C`) | 解决程序化着色网络进入实时引擎或轻量管线时的算力开销问题。包含烘焙位深度（Normal/Height 16-bit 防阶梯断层）与性能权衡。 |

---

### Module 5: Material Acquisition & Conversion (Image-to-Material & Scanning) — Historical 5 Units

| v1 ID | Historical Capability (v1) | Disposition | Proposed v2 Capability / Target | Owning Evidence & Class | Rationale & Gate 3 Impact |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **M05-U01** | 照片/扫描参考转 PBR 材质原理 *(Photometric / Scan Reference to PBR)* | `KEEP_AS_IS` | **V02-C31: 真实世界材质采集光学原理与数字化反向推导** *(Photometric Capture Principles & Reverse Material Estimation)* | Dinur (2026) Ch 13 (`B`); Sampler Docs (`C`); IntrinsiX (2025) (`D`) | 理解真实世界光影与材质本征属性的解耦机制（偏振去反光、漫射光环境拍照、法线坡度推导），是连接现实与虚拟材质的认知桥梁。 |
| **M05-U02** | Substance 3D Sampler 工具链工作流 *(Substance 3D Sampler Workflow)* | `RETIRE_OR_DEFER` | *(退役/合并为实现载体)* | Sampler Official Docs (`C`); Shah (2022) Ch 11 (`A`) | **RETIRE_OR_DEFER**：这是纯软件 GUI 工作流外壳。其底层技术能力已被“图像反算通道”、“无缝平铺”与“物理尺寸标定”完全分解吸收。作为独立 Candidate 纯属历史软件中心主义惯性。 |
| **M05-U03** | Image-to-Material 智能通道提取 *(Image-to-Material AI/B2M Extraction)* | `SPLIT` | **拆分为 V02-C32 与 V02-C33** | Sampler Docs (`C`); IntrinsiX (2025) (`D`); LumiTex (2026) (`D`) | **SPLIT 核心原因**：原单元混淆了“图像到通道的估算生成”与“自动化去光照缺陷的物理诊断与二次修正”。在现代工作流中，生成是算法前向推断，而诊断修正是艺术家必修的品控防线。 |
| **M05-U04** | 图像无缝平铺处理 (Seamless Tiling) *(Seamless Tiling & AI Outpainting)* | `KEEP_AS_IS` | **V02-C34: 纹理图像无缝平铺处理与宏观大色块重复消除** *(Seamless Texture Tiling & Macro Clumping Elimination)* | Shah (2022) Ch 11 (`A`); Sampler Docs Tiling (`C`) | 平铺滤镜边缘混合、接缝消除与大面积重复纹样的人工打散。贴图复用不可或缺的通用技能。 |
| **M05-U05** | 真实物理尺寸校准 (Scale Calibration) *(Real-world Physical Scale Calibration)* | `MERGE` | **合并入 V02-C26** | Sampler Docs Physical Size (`C`); Shah (2022) Ch 11 (`A`) | 真实物理尺寸标定在物理原理与工作流上直接服务于纹理空间映射、缩放与平铺控制，与 M04-U06 存在高度逻辑重叠。合并入 **V02-C26**。 |

---

### Module 6: LookDev & Multi-environment Validation (Validation & Delivery) — Historical 6 Units

| v1 ID | Historical Capability (v1) | Disposition | Proposed v2 Capability / Target | Owning Evidence & Class | Rationale & Gate 3 Impact |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **M06-U01** | Blender 材质视口与基础着色验证 *(Blender Viewport & Basic Shading Validation)* | `CANDIDATE_REFRAME` | **V02-C35: 交互式视口物理着色检验与快速环境响应验证** *(Interactive Viewport Shading Inspection & Rapid Environmental Response Validation)* | Blender Manual Viewport Shading (`C`); Painter Viewport Docs (`C`) | 历史表述限定在 Blender 视口面板。重构为通用的“在实时光栅化/混合渲染视口中对 Principled/OpenPBR 材质进行光照响应、金属度/粗糙度快速目视检查”。 |
| **M06-U02** | Unreal Engine 实时材质实例组装 *(Unreal Engine Master & Material Instances)* | `CANDIDATE_REFRAME` | **V02-C36: 实时引擎材质母版架构与参数化材质实例体系** *(Realtime Engine Master Material Architecture & Parameterized Material Instancing)* | UE 5.8 Material Instances Docs (`C`); Karis (2013) (`D`) | 历史表述偏向特定软件操作。重构为实时引擎通用的“母材质（Master Material）静态着色拓扑设计、动态标量/向量/贴图参数暴露、以及实例化（Material Instances）层级管理与性能优化”。 |
| **M06-U03** | 游戏运行时材质性能与约束 (ORM/BC7) *(Runtime Performance, BC7 & Texture Packing)* | `KEEP_AS_IS` | **V02-C37: 实时游戏运行时材质性能开销、通道打包与硬件压缩** *(Realtime Runtime Material Performance, Channel Packing & Hardware Compression)* | McDermott (2018) pp. 60–63 (`B`); UE 5.8 Texture Compression Docs (`C`); Karis (2013) (`D`) | 游戏交付端的刚性技术约束。ORM 多通道合并、BC7/BC5/BC1 硬件纹理压缩、显存占用计算与材质复杂度开销控制。 |
| **M06-U04** | 影视/动画高保真着色差异 (SSS/Coat) *(Cinematic High-fidelity Shading: SSS, Coat)* | `CANDIDATE_REFRAME` | **V02-C38: 高保真多层着色模型物理特性与因果表达 (次表面/清漆/薄膜)** *(High-fidelity Multilayer Shading Physics: Subsurface, Clear Coat & Thin Film)* | OpenPBR Spec §3.3, §3.4 (`C`); Dinur (2026) Ch 11–12 (`B`); RTR4 Ch 9.6 (`D`) | 历史表述将 SSS/Coat 仅视为影视特定差异。重构为“基于 OpenPBR 多层介质模型对高阶物理外观（皮肤/玉石次表面散射、车漆清漆双层高光、氧化薄膜干涉）的参数理解与因果调控”。 |
| **M06-U05** | 跨渲染器着色表现差异对比 *(Cross-renderer Shading Discrepancies)* | `CANDIDATE_REFRAME` | **V02-C39: 跨渲染引擎着色差异分析与视觉一致性调校** *(Cross-renderer Shading Discrepancy Diagnosis & Visual Consistency Alignment)* | McDermott (2018) pp. 80–88 (`B`); RTR4 Ch 9.10 (`D`); OpenPBR Spec §1.1 (`C`) | 历史表述偏向被动比较。重构为“理解不同渲染器在微表面遮蔽（Smith/Kelemen）、环境光积分与色调映射（Tone Mapping）上的算法差异，主动排查并对齐视觉外观”。 |
| **M06-U06** | 多环境 IBL 与极端光照压力测试 *(Multi-environment IBL & Lighting Stress Testing)* | `KEEP_AS_IS` | **V02-C40: 多环境 IBL 旋转压力测试与严苛物理一致性验证** *(Multi-environment IBL Rotation Stress Testing & Rigorous Physical Consistency QA)* | Dinur (2026) Ch 12 (`B`); McDermott (2018) pp. 38–40 (`B`); OpenPBR White Furnace Test (`C`) | LookDev 质量验收的核心金标准。通过室内暖光、室外高动态烈日、阴天冷光多套 HDR 环境旋转照射，检验材质是否在任何极端光照下均保持物理可信、绝不自发光或突兀死黑。 |

---

### Module 7: AI-Native Candidate Pool — Historical 13 Units

| v1 ID | Historical Candidate (v1) | Disposition | Proposed v2 Capability / Target | Owning Evidence & Class | Rationale & Gate 3 Impact |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **AI-U01** | 材质语义提示词工程 *(Material Semantic Prompting)* | `RETIRE_OR_DEFER` | *(退役/不作为独立 Candidate)* | AI Impact Report §6.1 (`D`); Sampler Generative Docs (`C`) | **RETIRE_OR_DEFER**：泛化的“提示词工程”属于易逝的操作技巧，不具备长期学科教学厚度。理解材料的物理工艺术语本身已经被 **V02-C01** 与 **V02-C15** 涵盖；纯文本自然语言交互不能作为独立的 3D 材质底层能力。 |
| **AI-U02** | 参考图像条件约束与风格锚定 *(Reference Conditioning & ControlNet)* | `CANDIDATE_REFRAME` | **V02-C41: 几何条件引导与多模态参考约束的材质生成控制** *(Geometry-conditioned & Multimodal Reference-guided Material Generation)* | Dinur (2026) Ch 19 (`B`); IntrinsiX (2025) (`D`); ControlNet/IP-Adapter literature (`D`) | 历史表述偏向具体的 ComfyUI 插件操作。重构为通用的“利用几何线索（深度/法线/位置）与图像特征嵌入（Feature Embedding）对生成式纹理进行定向空间引导与保形约束”。 |
| **AI-U03** | 跨通道 PBR 物理诊断 *(Cross-channel PBR Physical Diagnosis)* | `KEEP_AS_IS` | **V02-C42: 跨通道 PBR 物理自洽性诊断与多贴图逻辑矛盾排查** *(Cross-channel PBR Consistency Diagnosis & Inter-map Logical Conflict Auditing)* | McDermott (2018) Appendix (`B`); 80 Level Tripo Interview (`D`); AI Impact Report §6.1 (`D`) | 专门针对 AI 生成与多源贴图的体检诊断技能。排查例如“法线贴图有锐利深凹槽，但粗糙度贴图完全平滑无污垢响应”或“金属度为 1 但固有色极度暗黑”等跨通道逻辑撕裂。 |
| **AI-U04** | 人机协同分层迭代与局部微调 *(Human-in-the-Loop Layer Structuring)* | `CANDIDATE_REFRAME` | **V02-C43: 扁平生成纹理的非破坏性分层重构与局部受控修订** *(Non-destructive Layer Reconstruction & Localized Controlled Revision from Flat Textures)* | Shah (2022) Ch 3–4 (`A`); Meshy Docs (`C`); AI Impact Report §6.1 (`D`) | 历史表述笼统。重构为现代核心能力：“将生成工具输出的扁平单层贴图，通过空间遮罩提取与通道解耦，逆向重构为可非破坏性微调的图层栈”，实现“只修改磨损而不破坏底色”的局部受控修订（Edit Locality）。 |
| **AI-U05** | 光照残留剥离与去光照修正 *(De-lighting Inspection & Correction)* | `KEEP_AS_IS` | **V02-C33: 漫反射光照残留诊断与反照率手工/算法去光照精修** *(De-lighting Inspection, Albedo Purity QA & Manual/Algorithmic Correction)* | IntrinsiX (2025) (`D`); LumiTex (2026) (`D`); Sampler Docs (`C`) | 独立成项。当前 AI 与单目采集生成的 Albedo 频繁残留阴影暗斑，导致重打光时穿帮。学生必须掌握检测残留光照、利用反向曲线与修复工具剥离阴影的实操硬核技能。 |
| **AI-U06** | AI 材质变体策展与筛选 *(AI Material Variation Curation)* | `RETIRE_OR_DEFER` | *(退役/合并为艺术指导通用素养)* | AI Impact Report §6.2 (`D`); Sampler Docs (`C`) | **RETIRE_OR_DEFER**：在大量生成草稿中“挑出好看的”是泛化的人类审美筛选，其核心依据（物理合规、世界观契合、细节尺度）已被 **V02-C01**、**V02-C02** 与 **V02-C09** 覆盖，不值得独立占用 Gate 3 候选坑位。 |
| **AI-U07** | 版本控制与随机种子管理 *(Seed & Workflow Version Reproducibility)* | `RETIRE_OR_DEFER` | *(退役/合并入参数化管线通用要求)* | Sampler Docs Seed (`C`); AI Impact Report §6.2 (`D`) | **RETIRE_OR_DEFER**：记录 Seed 和版本参数属于任何数字管线的通用工程纪律，已在 **V02-C27**（种子变体）与通用资产管理中体现，不构成独立的材质核心能力。 |
| **AI-U08** | AI 纹理接缝与伪影修复 *(AI Artifact & Seam Inpainting)* | `MERGE` | **合并入 V02-C13** | 80 Level Tripo Interview (`D`); Painter Docs (`C`) | AI 在 UV 接缝与凹陷处生成的拉伸伪影，其实质修复手段完全依赖三维视口投影绘制、克隆画笔与空间修补遮罩，本质属于 **V02-C13** 的典型实战用例。 |
| **AI-U09** | 材质母版提示词驱动调参 *(Prompt-to-Parameter Control)* | `RETIRE_OR_DEFER` | *(退役/仅保留为概念推导)* | Node To Talk Docs (`C`/`D`); AI Impact Report §6.3 (`D`) | **RETIRE_OR_DEFER**：属于实验性原型插件（Node To Talk）的临时功能。核心在于母材质参数暴露（**V02-C28**）与 Agent 接口（**V02-C45**），自然语言调参只是外壳包装。 |
| **AI-U10** | 资产血统与商用合规判断 *(Asset Provenance & Licensing Judgment)* | `RETIRE_OR_DEFER` | *(退役/移出材质技术能力核心)* | Firefly Licensing Docs (`C`); AI Impact Report §6.3 (`D`) | **RETIRE_OR_DEFER**：版权法务通识对于数字媒体专业重要，但属于通识伦理范畴，不属于三维材质创作技术与理论的核心能力地图。 |
| **AI-U11** | 智能体节点图编排 *(Agentic Graph Orchestration)* | `CANDIDATE_REFRAME` | **V02-C45: 机器可读材质图表拓扑、序列化协议与智能体可操作性** *(Machine-readable Material Graph Topology, Serialization Protocols & Agent Operability)* | DD3M (2024/2025) (`D`); Node To Talk Docs (`C`/`D`); Blender Python API (`C`); Designer Python API (`C`) | 历史表述偏向高深的多智能体编排。重构为底层的“理解结构化材质图表的拓扑表示、掌握 JSON/XML/代码序列化规范，使材质系统具备可被外部脚本与 AI Agent 安全解析、修改与验证的结构化特征”。 |
| **AI-U12** | 跨平台物理材质标准化映射 *(Standardized MaterialX/OpenPBR Translation)* | `SPLIT` | **拆分为 V02-C44 与 V02-C46** | OpenPBR Spec (`C`); MaterialX Spec (`C`); UE 5.8 Interchange Docs (`C`) | **SPLIT 核心原因**：原单元混合了“标准材质语义表达与跨平台交换（MaterialX/OpenPBR）”与“从标准格式到目标游戏引擎的转换损失认知与管线适配交付”。这两者在工程实践中分属表达层与交付层。 |
| **AI-U13** | 视觉特征约束规范制定 *(Visual Constraint Specification)* | `MERGE` | **合并入 V02-C40 与 V02-C42** | Dinur (2026) Ch 19 (`B`); AI Impact Report §6.3 (`D`) | 设定反射率范围、粗糙度极值等约束指标，实质就是执行物理一致性验证与质检清单。与 **V02-C40** 及 **V02-C42** 重复。 |

---

## Part 3 — New Candidate Proposals (ADD Proposals)

经过 Gate 2.5A 官方一手规范与目标交付样本提取，历史 57 项存在以下 **3 项具有 A/B/C/D 权威证据支撑且未被表达的本质能力缺口**：

### ADD-01: V02-C44 — 开放标准跨平台结构化材质表示 (Open Standards Structured Material Representation: MaterialX & OpenPBR)
- **Proposed Capability**: 掌握基于开源工业标准（MaterialX 节点图定义、NodeDef、类型系统与 OpenPBR 规范化物理参数体系）描述三维物体外观的结构化方法，理解外观表达与特定宿主 DCC/引擎专有文件格式的解耦原理。
- **Owning Sources & Classes**:
  - `ASWF MaterialX Specification v1.39.5` (`C — Technical Specification`)
  - `ASWF OpenPBR Surface Specification v1.1.1` (`C — Technical Specification`)
  - `Substance 3D Painter 12.1 Release Notes (Default OpenPBR)` (`C — Living Official Source`)
  - `Blender 5.2 Manual (Principled BSDF based on OpenPBR)` (`C — Living Official Source`)
- **Evidence Pointer**:
  - `materialx-usdshade.md` §2.1–§2.3; `openpbr-specification.md` §2.1–§2.4; `blender-official.md` §2.1.
- **Why It Materially Affects Gate 3**:
  - 历史 57 项默认材质只能以“离散位图贴图（Bitmap Maps）”或“特定软件节点图（Blender Shader Nodes / Substance SBS）”存在。
  - 2026 年工业界已确立 MaterialX 与 OpenPBR 为跨平台材质交换的标准中枢（Painter, Blender, Unreal, USD 均已原生对齐）。若学生缺乏对“开放结构化材质表示”的认知，将永远被锁死在单一厂商的黑盒软件孤岛中，无法理解现代管线资产流转。

### ADD-02: V02-C46 — 跨格式表示转换损失认知与目标交付适配 (Representation Conversion Loss Awareness & Target Delivery Adaptation)
- **Proposed Capability**: 深刻理解材质从一种表达形式转换至另一种形式时的技术损失边界，建立核心三层认知模型：
  $$\text{Valid Representation} \quad \neq \quad \text{Visual Equivalence} \quad \neq \quad \text{Production Deliverable}$$
  能够排查并处理 MaterialX/OpenPBR 导入特定目标引擎（如 Unreal Engine 5.8 / Substrate）时的节点透传退化、着色器变体编译开销与运行时交付约束。
- **Owning Sources & Classes**:
  - `Epic Games Unreal Engine 5.8 MaterialX Support Matrix & Substrate Docs` (`C — Platform Documentation`)
  - `MaterialX Developer Guide ShaderGeneration.md` (`C — Developer Documentation`)
  - `OpenPBR Specification §Flexibility of Implementation` (`C — Technical Specification`)
- **Evidence Pointer**:
  - `unreal-substrate-target-sample.md` §2.1, §2.2; `materialx-usdshade.md` §4.1.
- **Why It Materially Affects Gate 3**:
  - 这是传统教学与真实生产之间最严重的脱节断层。传统学生误以为“在 DCC 里连好材质导出，引擎里导入就能自动一模一样”。
  - UE 5.8 官方文档证实 MaterialX PBR BSDF 节点在导入时均作为透传节点处理（inputs not connected），Substrate 仍处 Beta，且静态参数开关会触发着色器变体（Permutations）。学生必须掌握“格式转换必有损失”的批判性工程认知，才能完成最终交付。

### ADD-03: V02-C47 — 材质获取范式权衡决策：生成、检索、参数化复用与实拍转换 (Material Acquisition Paradigm Selection: Generation vs. Retrieval vs. Procedural Reuse vs. Capture)
- **Proposed Capability**: 面对具体资产与项目需求时，能够基于物理真实度、可控性、编辑自由度、版权风险与时间预算，科学决策并选择最优的材质获取范式（AI 文本/图像生成 vs. 现有标准资产库检索 vs. 参数化母材质派生 vs. 照片扫描采集推导 vs. 全手工绘制）。
- **Owning Sources & Classes**:
  - `Dinur (2026) Ch 1, 13, 19` (`B — Supporting Text`)
  - `80 Level Tripo Interview on Production Bottlenecks` (`D — Industry Evidence`)
  - `AI Impact on Material Workflows §3.1, §5` (`D — Research Synthesis`)
- **Evidence Pointer**:
  - `ai-impact-on-material-workflows.md` §5; `source-native-knowledge-index.md` Dinur Ch 19; `adobe-sampler-official.md` §3.1.
- **Why It Materially Affects Gate 3**:
  - 历史 57 项受工具中心主义影响，预设“每次遇到材质任务都必须从零手工制作或单张图片生成”。
  - 在工业实践中，乱用 AI 生成可能导致拓扑混乱、无法局部修订，反而成倍增加修复成本；而盲目从零手工制作又效率低下。掌握“何时生成、何时复用参数化母板、何时直接检索高质量资产库”的权衡决策能力，是现代材质创作者的核心战略判断力。

---

## Part 4 — Lineage Map (Merge, Split, Retire & Add Tracing)

### 4.1 Merges (合并谱系)
1. **Merge 1: 几何特征驱动的自适应材质分层封装 (V02-C14)**
   - *Constituents*: `M02-U04` (智能材质系统) + `M02-U05` (智能生成器驱动逻辑)
   - *Lineage*: `M02-U04, M02-U05 -> V02-C14`
   - *Rationale*: 两者本质同为“烘焙几何网格图驱动的图层栈动态参数化封装”，分开会人为放大软件 UI 菜单层级。
2. **Merge 2: 几何细节投影烘焙、网格贴图派生与烘焙伪影诊断 (V02-C21)**
   - *Constituents*: `M03-U04` (高低模映射拓扑) + `M03-U05` (关键贴图烘焙)
   - *Lineage*: `M03-U04, M03-U05 -> V02-C21`
   - *Rationale*: 高低模准备是烘焙的前提，合并为一个具备完整准备、烘焙计算与偏斜/黑边排错的高效工程单元。
3. **Merge 3: 节点数学运算、通道混合与数值区间重映射 (V02-C25)**
   - *Constituents*: `M04-U04` (数学运算与混合遮罩) + `M04-U05` (色彩映射与区间重映射)
   - *Lineage*: `M04-U04, M04-U05 -> V02-C25`
   - *Rationale*: 算术节点与渐变映射同属标量/向量数据调理，在着色器网络中紧密相连。
4. **Merge 4: 纹理空间变换、真实物理尺度对齐与平铺控制 (V02-C26)**
   - *Constituents*: `M04-U06` (映射缩放平铺) + `M05-U05` (真实物理尺寸校准)
   - *Lineage*: `M04-U06, M05-U05 -> V02-C26`
   - *Rationale*: 物理尺寸校准的本质是将纹理空间 UV 缩放与现实米制单位对齐，合并消除概念割裂。
5. **Merge 5: 空间局部遮罩体系、投影绘制与特征细节修饰 (V02-C13)**
   - *Constituents*: `M02-U03` (遮罩体系手绘) + `AI-U08` (AI 纹理接缝与伪影修复)
   - *Lineage*: `M02-U03, AI-U08 -> V02-C13`
   - *Rationale*: 接缝瑕疵与伪影修补完全依托三维投影与空间遮罩绘制技术，合入 V02-C13。
6. **Merge 6: 多环境 IBL 旋转压力测试与跨通道物理自洽性诊断 (V02-C40, V02-C42)**
   - *Constituents*: `AI-U13` (视觉特征约束规范制定) 吸收入 `V02-C40` 与 `V02-C42`
   - *Lineage*: `AI-U13 -> V02-C40, V02-C42`
   - *Rationale*: 设定约束规范实质就是进行质检诊断，无独立存在必要。

### 4.2 Splits (拆分谱系)
1. **Split 1: 图像转材质通道估算 vs. 去光照物理精修**
   - *Original*: `M05-U03` (Image-to-Material 智能通道提取)
   - *Lineage*:
     - `M05-U03 (Part A) -> V02-C32` (**单张图像/照片多通道 PBR 属性算法推导与置信度评估**)
     - `M05-U03 (Part B) + AI-U05 -> V02-C33` (**漫反射光照残留诊断与反照率手工/算法去光照精修**)
   - *Rationale*: 单张图预测通道与 Albedo 中的阴影死黑剥离属于完全不同的算法逻辑与实操排错技能。
2. **Split 2: 开放标准材质表达 vs. 目标引擎交付损失**
   - *Original*: `AI-U12` (跨平台物理材质标准化映射)
   - *Lineage*:
     - `AI-U12 (Part A) -> V02-C44` (**开放标准跨平台结构化材质表示: MaterialX & OpenPBR**)
     - `AI-U12 (Part B) -> V02-C46` (**跨格式表示转换损失认知与目标交付适配**)
   - *Rationale*: 标准描述（数据层）与引擎落地（执行/优化层）存在巨大的技术鸿沟，混在一起会产生“标准等于落地”的严重认知偏差。

### 4.3 Retirements / Defers (退役与延后谱系)
1. **`M05-U02: Substance 3D Sampler 工具链工作流`**
   - *Lineage*: `M05-U02 -> RETIRED`
   - *Rationale*: 纯软件操作外壳，能力已被 V02-C31, V02-C32, V02-C34 吸收。
2. **`AI-U01: 材质语义提示词工程`**
   - *Lineage*: `AI-U01 -> RETIRED`
   - *Rationale*: 泛化文字技巧，工艺术语理解已在 V02-C01 与 V02-C15 扎根。
3. **`AI-U06: AI 材质变体策展与筛选`**
   - *Lineage*: `AI-U06 -> RETIRED`
   - *Rationale*: 人类审美筛选已被 V02-C01 与 V02-C09 覆盖，不具独立材质技术结构。
4. **`AI-U07: 版本控制与随机种子管理`**
   - *Lineage*: `AI-U07 -> RETIRED`
   - *Rationale*: 通用管线工程习惯，融入 V02-C27。
5. **`AI-U09: 材质母版提示词驱动调参`**
   - *Lineage*: `AI-U09 -> RETIRED`
   - *Rationale*: 实验性插件外壳，底层为参数暴露（V02-C28）与 Agent 接口（V02-C45）。
6. **`AI-U10: 资产血统与商用合规判断`**
   - *Lineage*: `AI-U10 -> RETIRED`
   - *Rationale*: 属于专业法律伦理通识，移出材质核心技能候选。

---

## Part 5 — Proposed Candidate Set v2 (Structured Full Inventory)

Proposed Candidate Set v2 包含 **47 项高聚合、去软件中心化、面向未来的可迁移材质能力单元**，划分为 7 大模块：

### Module 1: Material Literacy & Physical Optics (物理光学与因果素养 — 10 Units)
- **`V02-C01`**: 现实材质物理属性观察与多维参考解构 *(Physical Material Observation & Multi-attribute Reference Decomposition)*
- **`V02-C02`**: PBR 物理可信性与辐射度能量守恒 *(PBR Physical Plausibility & Radiometric Energy Conservation)*
- **`V02-C03`**: 漫反射/镜面反射率安全区间与去光照纯度判定 *(Reflectance Safe Ranges & Albedo Delighting Purity)*
- **`V02-C04`**: 微表面粗糙度理论与微观几何法线分布 *(Microfacet Theory & Roughness NDF)*
- **`V02-C05`**: 金属导体与电介质光学分类与金属度边界准则 *(Conductor vs. Dielectric Optical Classification & Metallic Boundary Rules)*
- **`V02-C06`**: 切线空间法线几何扰动原理与跨坐标系对齐 *(Tangent Space Normal Principles & Coordinate Alignment)*
- **`V02-C07`**: 视差映射与几何置换原理 *(Parallax Occlusion & Geometric Displacement Mapping)*
- **`V02-C08`**: 环境光遮蔽物理意义与漫反射解耦 *(Ambient Occlusion Role & Diffuse Decoupling)*
- **`V02-C09`**: 表面细节多级频率与空间尺度解构 *(Multi-frequency Surface Detail Decomposition: Macro/Medium/Micro)*
- **`V02-C10`**: 色彩管理与线性管线规范 *(Color Management & Linear Workflow Specification: sRGB vs. Linear/Data)*

### Module 2: Spatial Multi-channel Authoring & Controlled Revision (三维多通道创作与受控修订 — 7 Units)
- **`V02-C11`**: 贴图工程架构、通道配置与色彩管理绑定 *(Texture Project Architecture, Channel Setup & Color Management Binding)*
- **`V02-C12`**: 非破坏性图层系统与多物理通道同步求值 *(Non-destructive Layer Stacking & Synchronized Multi-channel Evaluation)*
- **`V02-C13`**: 空间局部遮罩体系、投影绘制与特征细节修饰 *(Spatial Mask Hierarchy, Viewport Projection Painting & Feature Detailing)*
- **`V02-C14`**: 几何特征驱动的自适应材质分层封装与模板复用 *(Geometry-driven Adaptive Material Encapsulation & Template Reuse)*
- **`V02-C15`**: 材质物理工艺分层与底材-涂层-风化因果演变 *(Material Stratification & Substrate-to-Wear Physical Chronology)*
- **`V02-C16`**: 环境风化、接触磨损与空间位置因果模拟 *(Environmental Weathering, Contact Abrasion & Spatial Position Causality)*
- **`V02-C17`**: 目标引擎贴图格式转译与通道映射配置 *(Target Engine Texture Export Translation & Channel Mapping Configuration)*

### Module 3: Geometric Foundations & Baking Pipeline (几何支撑与细节烘焙管线 — 4 Units)
- **`V02-C18`**: UV 参数化质量评估、接缝布局与拉伸诊断 *(UV Parameterization Quality Assessment, Seam Layout & Distortion Diagnosis)*
- **`V02-C19`**: 模型光滑组硬边与 UV 接缝拓扑协同准则 *(Hard Edges vs. UV Seams Topological Alignment & Artifact Prevention)*
- **`V02-C20`**: 纹素密度规划、一致性分配与跨资产对齐 *(Texel Density Planning, Consistency Budgeting & Asset Alignment)*
- **`V02-C21`**: 几何细节投影烘焙、网格贴图派生与烘焙伪影诊断 *(Geometric Detail Baking, Mesh Map Derivation & Artifact Diagnosis)*

### Module 4: Procedural Systems & Parametric Graphs (程序化系统与参数化节点 — 8 Units)
- **`V02-C22`**: 结构化节点图架构与数据流拓扑原理 *(Structured Shader Graph Architecture & Directed Dataflow Topology)*
- **`V02-C23`**: 多维空间纹理坐标系转换与映射逻辑 *(Texture Coordinate Systems & Spatial Mapping: UV, Object, World, Triplanar)*
- **`V02-C24`**: 程序化算法噪波与自然图案合成 *(Procedural Noise Generators & Mathematical Pattern Synthesis)*
- **`V02-C25`**: 节点数学运算、通道混合与数值区间重映射 *(Node Mathematics, Channel Blending & Range Remapping)*
- **`V02-C26`**: 纹理空间变换、真实物理尺度对齐与平铺控制 *(Texture Spatial Transformation, Metric Scale Calibration & Tiling Control)*
- **`V02-C27`**: 对象随机变体、种子控制与重复感消除 *(Object-level Variation, Seed Randomization & Tiling Pattern Breaking)*
- **`V02-C28`**: 模块化子图封装与有意义的参数接口暴露 *(Modular Subgraph Encapsulation & Meaningful Parameter Interface Design)*
- **`V02-C29`**: 可复用参数化材质资产打包与动态运行时集成 *(Reusable Parametric Material Packaging & Dynamic Runtime Integration)*

### Module 5: Material Acquisition, Conversion & Paradigm Choice (材质采集转换与范式选择 — 6 Units)
- **`V02-C30`**: 程序化节点网络向标准位图集的静态烘焙与精度控制 *(Procedural Graph Baking to Static Bitmap Sets & Bit-depth Precision Control)*
- **`V02-C31`**: 真实世界材质采集光学原理与数字化反向推导 *(Photometric Capture Principles & Reverse Material Estimation)*
- **`V02-C32`**: 单张图像/照片多通道 PBR 属性算法推导与置信度评估 *(Single-image Multi-channel PBR Estimation & Confidence Evaluation)*
- **`V02-C33`**: 漫反射光照残留诊断与反照率手工/算法去光照精修 *(De-lighting Inspection, Albedo Purity QA & Manual/Algorithmic Correction)*
- **`V02-C34`**: 纹理图像无缝平铺处理与宏观大色块重复消除 *(Seamless Texture Tiling & Macro Clumping Elimination)*
- **`V02-C47`**: 材质获取范式权衡决策：生成、检索、参数化复用与实拍转换 *(Material Acquisition Paradigm Selection: Generation vs. Retrieval vs. Procedural Reuse vs. Capture)*

### Module 6: High-fidelity Shading, LookDev & Rigorous Validation (高保真着色、LookDev 与严苛验证 — 6 Units)
- **`V02-C35`**: 交互式视口物理着色检验与快速环境响应验证 *(Interactive Viewport Shading Inspection & Rapid Environmental Response Validation)*
- **`V02-C36`**: 实时引擎材质母版架构与参数化材质实例体系 *(Realtime Engine Master Material Architecture & Parameterized Material Instancing)*
- **`V02-C37`**: 实时游戏运行时材质性能开销、通道打包与硬件压缩 *(Realtime Runtime Material Performance, Channel Packing & Hardware Compression)*
- **`V02-C38`**: 高保真多层着色模型物理特性与因果表达 (次表面/清漆/薄膜) *(High-fidelity Multilayer Shading Physics: Subsurface, Clear Coat & Thin Film)*
- **`V02-C39`**: 跨渲染引擎着色差异分析与视觉一致性调校 *(Cross-renderer Shading Discrepancy Diagnosis & Visual Consistency Alignment)*
- **`V02-C40`**: 多环境 IBL 旋转压力测试与严苛物理一致性验证 *(Multi-environment IBL Rotation Stress Testing & Rigorous Physical Consistency QA)*

### Module 7: Structured Representation, Generative Control & Agent Operability (结构化表达、生成受控与智能体交互 — 6 Units)
- **`V02-C41`**: 几何条件引导与多模态参考约束的材质生成控制 *(Geometry-conditioned & Multimodal Reference-guided Material Generation)*
- **`V02-C42`**: 跨通道 PBR 物理自洽性诊断与多贴图逻辑矛盾排查 *(Cross-channel PBR Consistency Diagnosis & Inter-map Logical Conflict Auditing)*
- **`V02-C43`**: 扁平生成纹理的非破坏性分层重构与局部受控修订 *(Non-destructive Layer Reconstruction & Localized Controlled Revision from Flat Textures)*
- **`V02-C44`**: 开放标准跨平台结构化材质表示 (MaterialX & OpenPBR) *(Open Standards Structured Material Representation: MaterialX & OpenPBR)*
- **`V02-C45`**: 机器可读材质图表拓扑、序列化协议与智能体可操作性 *(Machine-readable Material Graph Topology, Serialization Protocols & Agent Operability)*
- **`V02-C46`**: 跨格式表示转换损失认知与目标交付适配 *(Representation Conversion Loss Awareness & Target Delivery Adaptation)*

---

## Part 6 — Count & Change Summary

### 6.1 Statistical Breakdown
- **Historical Candidate Set v1 Total**: **57**
  - Traditional units: 44
  - AI-native candidate pool: 13
- **Audit Dispositions Applied to v1**:
  - `KEEP_AS_IS`: **18**
  - `CANDIDATE_REFRAME`: **17**
  - `MERGE`: **14** (collapsing into 6 consolidated capabilities)
  - `SPLIT`: **2** (expanding into 4 capabilities)
  - `RETIRE_OR_DEFER`: **6** (retired from independent candidate consideration)
- **New Capabilities Added (`ADD`)**: **3** (`V02-C44`, `V02-C46`, `V02-C47`)
- **Proposed Candidate Set v2 Total**: **47**

### 6.2 Structural Health Indicators
1. **Total Count Rationality**: Count evolved from 57 to **47**. The reduction is driven by eliminating redundant GUI micro-operations (`M02-U04/05`, `M03-U04/05`, `M04-U04/05`, `M04-U06/M05-U05`), retiring software shells (`M05-U02`) and ephemeral prompt/curation skills (`AI-U01, AI-U06, AI-U07, AI-U09, AI-U10`).
2. **Substantive Additions**: Added 3 vital industry-demanded capabilities: structured standard representations (MaterialX/OpenPBR), representation conversion loss awareness (`Valid Representation ≠ Visual Equivalence ≠ Production Deliverable`), and multi-paradigm acquisition choice.
3. **No Software Lock-in**: All candidate descriptions are framed as durable, transferable competencies rather than specific tool buttons or menus.
4. **Zero Orphaned Items**: Every single v1 item has a traceable trajectory in Part 2 and Part 4.

---

## Part 7 — Unresolved Structural Hypotheses (Isolated E-Class Items)

The following structural hypotheses emerged during the audit but are strictly isolated because they currently rely only on project extrapolation ($E$) and lack direct $A/B/C/D$ authoritative evidence:

### HYPO-01: AI Video Temporal Material Grounding & Consistency
- *Hypothesis*: In workflows integrating 3D materials with AI video generative models, students may need a specific competency in "3D-grounded material consistency under dynamic relighting".
- *Evidence Status*: While Dinur Ch 19 and general industry discourse touch on video generation, no standard textbook or platform specification defines a stable, taught curriculum unit for 3D-to-video material grounding.
- *Disposition*: `UNRESOLVED STRUCTURAL HYPOTHESIS`. Does not enter Candidate Set v2.

### HYPO-02: Universal Automated Multi-engine LookDev Pipeline
- *Hypothesis*: Students could be required to build a fully automated, headless multi-engine test runner (executing Cycles, EEVEE, and Unreal rendering simultaneously via Python CLI) for every assignment.
- *Evidence Status*: Blender headless execution is verified in Lane F (`C`), but mandating multi-engine automated testing in an 8-week undergraduate course exceeds verified curricular precedent ($E$).
- *Disposition*: `UNRESOLVED STRUCTURAL HYPOTHESIS`. Kept as a teacher-demonstration hypothesis for Gate 3, not a student candidate.

### HYPO-03: Real-time Neural BSDF / NeRF-to-PBR Material Inversion
- *Hypothesis*: Real-time neural representation shaders (Neural BSDFs) replacing standard PBR parameters in game engines.
- *Evidence Status*: Active academic research (CVPR/SIGGRAPH), but Epic Games UE 5.8 documentation and official standards show traditional GGX/Substrate PBR remains the production delivery baseline.
- *Disposition*: `UNRESOLVED STRUCTURAL HYPOTHESIS`. Excluded from Candidate Set v2.

---

## Part 8 — Critical Anti-Inertia Review

### The 2030 Counterfactual Test
> *"If the historical 57 units did not exist today, and we designed a curriculum for a 2030 student working alongside powerful AI Agents, would we actively create these candidates?"*

1. **Did we eliminate manual software inertia?**
   - **Yes**. We retired `Substance 3D Sampler 工具链工作流` (M05-U02) because it was merely a software shell. We merged `M02-U04` and `M02-U05` because separating smart materials from generators was an artifact of Substance GUI layout. We merged `M03-U04` into `M03-U05` because low-poly preparation is inseparable from baking calculation.
2. **Did we eliminate prompt-engineering illusions?**
   - **Yes**. We retired `材质语义提示词工程` (AI-U01), `AI 材质变体策展与筛选` (AI-U06), and `材质母版提示词驱动调参` (AI-U09) because prompt tricks evaporate as models evolve, whereas understanding physical causality (**V02-C01/C15**) and parameter exposure (**V02-C28**) are durable.
3. **What survived and why?**
   - **Physical Causality & Optical Laws**: Optics, energy conservation, reflectance ranges, and microfacet theory remain mandatory because AI frequently hallucinates non-physical values.
   - **Structured Representations & Agent Operability**: MaterialX, OpenPBR, and DAG topology survived and were strengthened because they provide the deterministic, machine-readable substrate that both humans and AI Agents need to collaborate safely.
   - **Controlled Revision & Edit Locality**: The ability to modify a single channel or localized mask without destroying the rest of the asset survived as a primary differentiator between amateur generation and professional production.
   - **Loss Awareness & Production Deliverability**: Knowing that a "valid file" does not mean "visual equivalence" or "production deliverable" survived because target runtime constraints (memory, draw calls, shader permutations) cannot be bypassed by automated generation.

---

*Artifact created at `docs/research/candidate-set-rebaselining-audit.md` for Gate 2.5A.5 review.*
