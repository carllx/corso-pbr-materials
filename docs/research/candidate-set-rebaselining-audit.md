# Candidate Set Re-baselining Audit: From Historical Baseline v1 to Proposed Candidate Set v2

> **Gate**: Gate 2.5A.5 — Candidate Set Re-baselining Audit  
> **Repository**: `carllx/corso-pbr-materials`  
> **Anchor Commit**: `275dc4db88b417a688ef20d628efd49fbbcb1f84` (Gate 2.5A Source Research Consolidated PASS)  
> **Governance Context**: Governed by Issue #3 (Stage 2 Strategy Clarification) and Issue #4 (Gate 2.5 Execution Tracker, Browser Review Comment `5652034537`).  
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
- Supporting texts including Real-Time Rendering 4th Edition (RTR4) are categorized as Class `B` per Issue #3 governance authority.
- Project research reports (`ai-impact-on-material-workflows.md`) are cited as project synthesis pointers (`Synthesis Pointer`), with evidence classes assigned to their underlying academic/industry source documents.
- If an idea is only supported by $E$ (Project Inference Only), it is isolated as an `UNRESOLVED STRUCTURAL HYPOTHESIS` and cannot reshape Candidate Set v2.
- Full lineage from v1 ID to v2 ID is maintained with zero orphaned items.

---

## Part 2 — Full v1 $\to$ v2 Mapping & Audit Table

### Module 1: Material Literacy (Physical Optics & Theoretical Foundations) — Historical 10 Units

| v1 ID | Historical Capability (v1) | Disposition | Proposed v2 Capability / Target | Owning Evidence & Class | Rationale & Gate 3 Relevance Hypothesis |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **M01-U01** | 现实材质观察与参考分析 *(Material Observation & Reference Analysis)* | `KEEP_AS_IS` | **V02-C01: 现实材质物理属性观察与多维参考解构** *(Physical Material Observation & Multi-attribute Reference Decomposition)* | Dinur (2026) Ch 1, 3 (`B`); RTR4 Ch 9.1 (`B`) | 人类审美与因果分析基石。为 Gate 3 提供不可被纯前向算法黑盒替代的观察基准，具备高教学审议相关性。 |
| **M01-U02** | PBR 物理可信性与能量守恒 *(PBR Plausibility & Energy Conservation)* | `KEEP_AS_IS` | **V02-C02: PBR 物理可信性与辐射度能量守恒** *(PBR Physical Plausibility & Radiometric Energy Conservation)* | McDermott (2018) pp. 29–30 (`B`); RTR4 Ch 9.2–9.3 (`B`); OpenPBR Spec §1.1 (`C`) | 跨光照环境不失真的物理规律。提供检验生成式贴图能量过曝与漫反射反弹异常的评估依据。 |
| **M01-U03** | Base Color 反射率与安全色阶 *(Base Color Reflectance & Safe Values)* | `CANDIDATE_REFRAME` | **V02-C03: 漫反射/镜面反射率安全区间与去光照纯度判定** *(Reflectance Safe Ranges & Albedo Delighting Purity)* | McDermott (2018) pp. 48–52 (`B`); OpenPBR Spec §3.1 (`C`); Dinur (2026) Ch 3 (`B`) | 历史表述侧重 sRGB 绝对数值死记硬背。重构为“电介质反射率安全阈值判定与 Base Color 中阴影/高光污染的物理诊断”，直接指导贴图质量验收。 |
| **M01-U04** | Roughness 微表面粗糙度模型 *(Roughness & Microfacet Theory)* | `KEEP_AS_IS` | **V02-C04: 微表面粗糙度理论与微观几何法线分布** *(Microfacet Theory & Roughness NDF)* | McDermott (2018) pp. 22–27 (`B`); RTR4 Ch 9.2 (`B`); OpenPBR Spec §3.2 (`C`) | GGX 微表面法线分布（NDF）与高光衰减理论。调控高光斑锐利度、模糊过渡与光照反应的核心维度。 |
| **M01-U05** | Metallic 金属度二值准则 *(Metallic Classification & Boundary Rules)* | `KEEP_AS_IS` | **V02-C05: 金属导体与电介质光学分类与金属度边界准则** *(Conductor vs. Dielectric Optical Classification & Metallic Boundary Rules)* | McDermott (2018) pp. 33–37, 53–55 (`B`); RTR4 Ch 9.4 (`B`); OpenPBR Spec §3.1 (`C`) | 纯物质非金即绝缘的光学本质。控制 F0 反射率来源；中间过渡灰阶的物理合法性（氧化锈蚀、极薄灰尘、抗锯齿像素）诊断是排查伪金属噪点的核心。 |
| **M01-U06** | Normal 切线空间法线原理 *(Tangent Space Normal Principles)* | `KEEP_AS_IS` | **V02-C06: 切线空间法线几何扰动原理与跨坐标系对齐** *(Tangent Space Normal Principles & Coordinate Alignment)* | Shah (2022) pp. 45–48 (`A`); McDermott (2018) pp. 76–79 (`B`); Blender Manual (`C`) | 宏观几何与微观着色扰动的桥梁。DirectX (Y-) 与 OpenGL (Y+) 绿通道及切线空间基底对齐是跨工具/引擎交付中最频繁的失效点。 |
| **M01-U07** | Height / Displacement 几何置换 *(Height & Displacement Mapping)* | `KEEP_AS_IS` | **V02-C07: 视差映射与几何置换原理** *(Parallax Occlusion & Geometric Displacement Mapping)* | Shah (2022) Ch 9–10 (`A`); McDermott (2018) p. 75 (`B`); Sampler Docs (`C`) | 从微观着色法线跨越到真实网格形变（POM/Displacement）的关键。驱动程序化雕刻、物理破损与轮廓级几何变化。 |
| **M01-U08** | Ambient Occlusion 环境遮挡作用 *(Ambient Occlusion Role & Limits)* | `KEEP_AS_IS` | **V02-C08: 环境光遮蔽物理意义与漫反射解耦** *(Ambient Occlusion Role & Diffuse Decoupling)* | McDermott (2018) p. 74 (`B`); Painter Baking Docs (`C`) | 模拟微观缝隙接触阴影，严格与直接光照和 Base Color 固有色解耦，提供排查“AO 烘死在固有色里”的依据。 |
| **M01-U09** | 表面细节尺度与频率认知 *(Detail Scales: Macro, Medium, Micro)* | `KEEP_AS_IS` | **V02-C09: 表面细节多级频率与空间尺度解构** *(Multi-frequency Surface Detail Decomposition: Macro/Medium/Micro)* | Dinur (2026) Ch 1, 3 (`B`); Shah (2022) Ch 3–6 (`A`) | 跨软件图层堆栈、节点网络与风化破损组织的结构性思维基石。宏观结构、中频磨损与微观噪波分层控制的必要理论支撑。 |
| **M01-U10** | sRGB 与 Linear 色彩空间规范 *(Color Space: sRGB vs. Linear/Non-Color)* | `KEEP_AS_IS` | **V02-C10: 色彩管理与线性管线规范** *(Color Management & Linear Workflow Specification: sRGB vs. Linear/Data)* | McDermott (2018) pp. 38–39 (`B`); OpenPBR Spec §1.2 (`C`); RTR4 Ch 5.6 (`B`) | 数据贴图（Linear/Non-Color）与色彩贴图（sRGB/ACEScg）的数学处理差异。材质资产跨 DCC/引擎导入导出时防止物理错误的基础规范。 |

---

### Module 2: Texture-based Authoring (Asset-level Multi-channel Craft) — Historical 8 Units

| v1 ID | Historical Capability (v1) | Disposition | Proposed v2 Capability / Target | Owning Evidence & Class | Rationale & Gate 3 Relevance Hypothesis |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **M02-U01** | Painter 工程设置与色彩管理 *(Painter Project Setup & OCIO/ACES)* | `CANDIDATE_REFRAME` | **V02-C11: 贴图工程架构、通道配置与色彩管理绑定** *(Texture Project Architecture, Channel Setup & Color Management Binding)* | Shah (2022) Ch 1 (`A`); Painter Official Docs (`C`) | 历史表述将能力绑定于 Painter 单一软件的初次向导点击。重构为跨工具通用的资产贴图工程初始化、材质集（Texture Sets）多网格管理及 OCIO/ACES 色彩管理管线绑定。 |
| **M02-U02** | 图层结构与多通道同步管理 *(Layer Stack & Multi-channel Sync)* | `KEEP_AS_IS` | **V02-C12: 非破坏性图层系统与多物理通道同步求值** *(Non-destructive Layer Stacking & Synchronized Multi-channel Evaluation)* | Shah (2022) Ch 3 (`A`); Painter Layer Docs (`C`) | 资产级材质创作的组织支柱。Fill Layer / Paint Layer 的多通道独立混合模式（Color, Rough, Metal, Normal, Height 同步运算）是非破坏性局部微调的基础。 |
| **M02-U03** | 遮罩体系与手绘特征细节 *(Mask Hierarchy & Feature Hand-painting)* | `CANDIDATE_REFRAME` | **V02-C13: 空间局部遮罩体系、投影绘制与特征细节修饰** *(Spatial Mask Hierarchy, Viewport Projection Painting & Feature Detailing)* | Shah (2022) Ch 4–5 (`A`); Painter Official Docs (`C`) | 历史表述偏向“纯手工画画”。重构为“三维视口投影、几何多边形填充、黑白通道遮罩与局部特征修补”。提供空间精确定位与局部可控修订手段。 |
| **M02-U04** | 智能材质 (Smart Materials) 组织 *(Smart Materials System & Encapsulation)* | `MERGE` | **合并入 V02-C14** | Shah (2022) Ch 6 (`A`); Painter Docs (`C`) | 智能材质与智能生成器在底层皆属于“基于几何烘焙贴图驱动的自适应图层模板与封装系统”。合并为一个高层模块，避免人为拆分成琐碎的 GUI 面板操作。 |
| **M02-U05** | 智能生成器 (Generators) 驱动逻辑 *(Generators Driven by Mesh Maps)* | `MERGE` | **合并入 V02-C14** | Shah (2022) Ch 4, 6 (`A`); Painter Docs (`C`) | 见 M02-U04。共同合并为 **V02-C14: 几何特征驱动的自适应材质分层封装与模板复用**。 |
| **M02-U06** | 材质分层逻辑 (Base $\rightarrow$ Detail) *(Material Stratification: Substrate to Wear)* | `KEEP_AS_IS` | **V02-C15: 材质物理工艺分层与底材-涂层-风化因果演变** *(Material Stratification & Substrate-to-Wear Physical Chronology)* | Shah (2022) Ch 4–6 (`A`); Dinur (2026) Ch 5, 13 (`B`) | 工业工艺学在数字材质中的映射：底材（裸金属/塑料）$\to$ 涂层底漆 $\to$ 表面面漆 $\to$ 机械划伤剥落 $\to$ 环境侵蚀氧化 $\to$ 表层积灰。为 Gate 3 提供物理因果分层假说。 |
| **M02-U07** | 风化与磨损物理逻辑 (Weathering) *(Weathering, Aging & Contact Logic)* | `CANDIDATE_REFRAME` | **V02-C16: 环境风化、接触磨损与空间位置因果模拟** *(Environmental Weathering, Contact Abrasion & Spatial Position Causality)* | Shah (2022) Ch 6 (`A`); Dinur (2026) Ch 5 (`B`) | 历史表述偏软件做旧滤镜。重构为“依据力学接触点（外露凸起边角磨损）、重力沉积（Position Y 积尘积水）、流体冲刷与环境交互等因果逻辑进行材质老化推演”。 |
| **M02-U08** | 贴图导出模板与通道配置 *(Export Presets & Channel Packing)* | `CANDIDATE_REFRAME` | **V02-C17: 目标引擎贴图格式转译与通道映射配置** *(Target Engine Texture Export Translation & Channel Mapping Configuration)* | Shah (2022) Ch 6 (`A`); Painter Docs (`C`) | 历史表述局限于 Painter 点击 Export 预设。重构为“根据下游渲染器/游戏引擎（Arnold/Unreal/glTF）的物理接口规范，执行通道重组、位深度匹配与色彩空间元数据标记”。 |

---

### Module 3: Supporting Pipeline Knowledge (Prerequisites & Baking) — Historical 5 Units

| v1 ID | Historical Capability (v1) | Disposition | Proposed v2 Capability / Target | Owning Evidence & Class | Rationale & Gate 3 Relevance Hypothesis |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **M03-U01** | UV 参数化展开与接缝切分 *(UV Parameterization & Seam Layout)* | `CANDIDATE_REFRAME` | **V02-C18: UV 参数化质量评估、接缝布局与拉伸诊断** *(UV Parameterization Quality Assessment, Seam Layout & Distortion Diagnosis)* | Shah (2022) Ch 1 (`A`); Painter Docs Auto Unwrap (`C`); McDermott (2018) pp. 60–63 (`B`) | 本课程非建模拓扑课。重构为“UV 参数化质量评估、视口接缝（Seam）合理性检查与纹理形变拉伸诊断”，重点在于评估与指导自动/外部展开质量，而非从零手撕 UV。 |
| **M03-U02** | 接缝与硬边对应原则 *(UV Seams vs. Hard Edges Matching)* | `KEEP_AS_IS` | **V02-C19: 模型光滑组硬边与 UV 接缝拓扑协同准则** *(Hard Edges vs. UV Seams Topological Alignment & Artifact Prevention)* | McDermott (2018) pp. 60–63 (`B`); RTR4 Ch 6 (`B`) | 几何拓扑与烘焙数学法则。硬边处切开 UV 接缝以防止顶点法线插值计算出黑边/渐变穿帮，具有明确的工程排错价值。 |
| **M03-U03** | 像素密度规划 (Texel Density) *(Texel Density Planning & Scaling)* | `KEEP_AS_IS` | **V02-C20: 纹素密度规划、一致性分配与跨资产对齐** *(Texel Density Planning, Consistency Budgeting & Asset Alignment)* | Shah (2022) Ch 1 (`A`); McDermott (2018) pp. 58–60 (`B`) | 资产级乃至场景级视觉品质均一的决定性指标。防止同一个道具上出现局部模糊、局部极度锐利的纹素失配。 |
| **M03-U04** | 高低模映射关系与拓扑准备 *(High-to-Low Poly Mapping & Topology)* | `MERGE` | **合并入 V02-C21** | Shah (2022) Ch 1 (`A`); Painter Baking Docs (`C`) | 高低模拓扑准备本身是贴图烘焙的前提环节，将其与贴图烘焙及失配排错合并为一个完整的“几何细节投射与烘焙”能力单元。 |
| **M03-U05** | 关键贴图烘焙 *(Mesh Maps Baking: Normal/AO/Curvature)* | `MERGE` | **合并入 V02-C21** | Shah (2022) Ch 1 (`A`); Painter Baking Docs (`C`) | 与 M03-U04 合并为 **V02-C21: 几何细节投影烘焙、网格贴图派生与烘焙伪影诊断** *(Geometric Detail Baking, Mesh Map Derivation & Artifact Diagnosis)*。包含高低模包裹笼（Cage）、射线投射、Paint Skew 斜切修复与法线反转排错。 |

---

### Module 4: Procedural / Parametric Materials (Procedural Nodes & Systems) — Historical 10 Units

| v1 ID | Historical Capability (v1) | Disposition | Proposed v2 Capability / Target | Owning Evidence & Class | Rationale & Gate 3 Relevance Hypothesis |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **M04-U01** | 节点着色器架构 (Shader Nodes) *(Node-based Shader Graph Architecture)* | `CANDIDATE_REFRAME` | **V02-C22: 结构化节点图架构与数据流拓扑原理** *(Structured Shader Graph Architecture & Directed Dataflow Topology)* | Shah (2022) Ch 7 (`A`); Blender Manual Shader Nodes (`C`); Designer Docs (`C`); MaterialX Spec (`C`) | 历史表述偏向具体软件界面的连线基础。重构为通用的“有向无环图（DAG）数据流、强类型系统（标量、向量、色彩、表面接口）与复合子图拓扑”，为程序化合成、MaterialX 及 Agent 机器读写奠定心智模型。 |
| **M04-U02** | 纹理坐标系 *(Texture Coordinates: Generated, Object, UV)* | `KEEP_AS_IS` | **V02-C23: 多维空间纹理坐标系转换与映射逻辑** *(Texture Coordinate Systems & Spatial Mapping: UV, Object, World, Triplanar)* | Blender Manual (`C`); Shah (2022) Ch 7–8 (`A`); Designer Docs (`C`) | 区分 UV 平面、包围盒 Generated、三维 Object 空间与三平面投影（Triplanar）。摆脱模型 UV 依赖、实现无拉伸自然程序化铺底的重要手段。 |
| **M04-U03** | 算法纹理与噪声 *(Procedural Noise & Patterns: Perlin/Voronoi)* | `KEEP_AS_IS` | **V02-C24: 程序化算法噪波与自然图案合成** *(Procedural Noise Generators & Mathematical Pattern Synthesis)* | Shah (2022) Ch 8 (`A`); Blender Manual (`C`); Designer Docs (`C`) | 利用 Perlin/Simplex/Voronoi 等数学函数生成连续有机质感、开裂裂纹与高频细节。参数化材质无限分辨率特性的基础。 |
| **M04-U04** | 数学运算与混合遮罩 *(Math Operations & Mix Masks)* | `MERGE` | **合并入 V02-C25** | Shah (2022) Ch 9 (`A`); Blender Manual Math/Mix Nodes (`C`) | 算术运算（Add, Multiply, Min/Max）与色彩/区间重映射在节点网络中是紧密一体的数据调理过程。分开导致微观连线碎片化。 |
| **M04-U05** | 色彩映射与区间重映射 *(ColorRamp & Range Remapping)* | `MERGE` | **合并入 V02-C25** | Shah (2022) Ch 9 (`A`); Blender Manual ColorRamp/MapRange (`C`) | 与 M04-U04 合并为 **V02-C25: 节点数学运算、通道混合与数值区间重映射** *(Node Mathematics, Channel Blending & Range Remapping)*。 |
| **M04-U06** | 映射缩放与平铺控制 *(Mapping, Scale & Tiling Control)* | `KEEP_AS_IS` | **V02-C26: 纹理空间变换、真实物理尺度对齐与平铺控制** *(Texture Spatial Transformation, Metric Scale Calibration & Tiling Control)* | Shah (2022) Ch 8 (`A`); Sampler Docs Physical Size (`C`); Blender Manual (`C`) | 将虚拟贴图坐标映射与现实世界公制物理尺寸（Real-world Metric Scale）对齐，消除平铺接缝与比例失真的关键能力。 |
| **M04-U07** | 随机化与多变异质感 *(Randomization & Multi-variation)* | `KEEP_AS_IS` | **V02-C27: 对象随机变体、种子控制与重复感消除** *(Object-level Variation, Seed Randomization & Tiling Pattern Breaking)* | Blender Manual Object Info (`C`); Designer Tile Sampler Docs (`C`) | 大规模资产复用时打破“瓷砖感/贴图重复痕迹”的有效技能。通过随机种子（Seed）与位置扰动实现一套材质生成多样外观。 |
| **M04-U08** | 节点组封装与参数暴露 *(Node Group Encapsulation & Interface)* | `CANDIDATE_REFRAME` | **V02-C28: 模块化子图封装与有意义的参数接口暴露** *(Modular Subgraph Encapsulation & Meaningful Parameter Interface Design)* | Shah (2022) Ch 7 (`A`); Designer Values Docs (`C`); Blender Node Groups (`C`) | 历史表述局限于“右键打包节点组”。重构为“黑盒模块化抽象、参数暴露、定义合法数值区间与标签，为下游艺术家或自动化脚本构建易读的母材质控制面板”。 |
| **M04-U09** | 独立程序化纹理与 `.sbsar` 母版生成 *(Standalone Procedural Texture & `.sbsar`)* | `CANDIDATE_REFRAME` | **V02-C29: 可复用参数化材质资产打包与动态运行时集成** *(Reusable Parametric Material Packaging & Dynamic Runtime Integration)* | Designer User Guide (`C`); Shah (2022) Ch 10 (`A`) | 历史表述绑定于 Designer 专属 `.sbsar`。重构为“参数化材质包的编译、跨软件分发机制以及在宿主引擎运行时通过插件/API 动态调参的系统原理”。 |
| **M04-U10** | 程序化结果烘焙为 PBR 贴图包 *(Baking Procedural to PBR Texture Set)* | `CANDIDATE_REFRAME` | **V02-C30: 程序化节点网络向标准位图集的静态烘焙与精度控制** *(Procedural Graph Baking to Static Bitmap Sets & Bit-depth Precision Control)* | Shah (2022) Ch 10 (`A`); Blender Render Baking Docs (`C`); SAT Docs (`C`) | 解决程序化着色网络进入实时引擎或轻量管线时的算力开销问题。包含烘焙位深度（Normal/Height 16-bit 防阶梯断层）与性能权衡。 |

---

### Module 5: Material Acquisition & Conversion (Image-to-Material & Scanning) — Historical 5 Units

| v1 ID | Historical Capability (v1) | Disposition | Proposed v2 Capability / Target | Owning Evidence & Class | Rationale & Gate 3 Relevance Hypothesis |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **M05-U01** | 照片/扫描参考转 PBR 材质原理 *(Photometric / Scan Reference to PBR)* | `KEEP_AS_IS` | **V02-C31: 真实世界材质采集光学原理与数字化反向推导** *(Photometric Capture Principles & Reverse Material Estimation)* | Dinur (2026) Ch 13 (`B`); Sampler Docs (`C`); IntrinsiX (2025) (`D`) | 理解真实世界光影与材质本征属性的解耦机制（偏振去反光、漫射光环境拍照、法线坡度推导），是连接现实与虚拟材质的认知桥梁。 |
| **M05-U02** | Substance 3D Sampler 工具链工作流 *(Substance 3D Sampler Workflow)* | `RETIRE_OR_DEFER` | *(退役/合并为实现载体)* | Sampler Official Docs (`C`); Shah (2022) Ch 11 (`A`) | **RETIRE_OR_DEFER**：纯软件 GUI 工作流外壳。其底层技术能力已被“图像反算通道”、“无缝平铺”与“物理尺寸标定”完全分解吸收。作为独立 Candidate 属于历史软件中心主义惯性。 |
| **M05-U03** | Image-to-Material 智能通道提取 *(Image-to-Material AI/B2M Extraction)* | `SPLIT` | **拆分为 V02-C32 与 V02-C33** | Sampler Docs (`C`); IntrinsiX (2025) (`D`); LumiTex (2026) (`D`) | **SPLIT 核心原因**：原单元混淆了“图像到通道的估算生成”与“自动化去光照缺陷的物理诊断与二次修正”。生成是算法前向推断，而诊断修正是艺术家品控防线。 |
| **M05-U04** | 图像无缝平铺处理 (Seamless Tiling) *(Seamless Tiling & AI Outpainting)* | `KEEP_AS_IS` | **V02-C34: 纹理图像无缝平铺处理与宏观大色块重复消除** *(Seamless Texture Tiling & Macro Clumping Elimination)* | Shah (2022) Ch 11 (`A`); Sampler Docs Tiling (`C`) | 平铺滤镜边缘混合、接缝消除与大面积重复纹样的人工打散。贴图复用不可或缺的通用技能。 |
| **M05-U05** | 真实物理尺寸校准 (Scale Calibration) *(Real-world Physical Scale Calibration)* | `MERGE` | **合并入 V02-C26** | Sampler Docs Physical Size (`C`); Shah (2022) Ch 11 (`A`) | 真实物理尺寸标定在物理原理与工作流上直接服务于纹理空间映射、缩放与平铺控制，与 M04-U06 存在高度逻辑重叠。合并入 **V02-C26**。 |

---

### Module 6: LookDev & Multi-environment Validation (Validation & Delivery) — Historical 6 Units

| v1 ID | Historical Capability (v1) | Disposition | Proposed v2 Capability / Target | Owning Evidence & Class | Rationale & Gate 3 Relevance Hypothesis |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **M06-U01** | Blender 材质视口与基础着色验证 *(Blender Viewport & Basic Shading Validation)* | `CANDIDATE_REFRAME` | **V02-C35: 交互式视口物理着色检验与快速环境响应验证** *(Interactive Viewport Shading Inspection & Rapid Environmental Response Validation)* | Blender Manual Viewport Shading (`C`); Painter Viewport Docs (`C`) | 历史表述限定在 Blender 视口面板。重构为通用的“在实时光栅化/混合渲染视口中对 Principled/OpenPBR 材质进行光照响应、金属度/粗糙度快速目视检查”。 |
| **M06-U02** | Unreal Engine 实时材质实例组装 *(Unreal Engine Master & Material Instances)* | `CANDIDATE_REFRAME` | **V02-C36: 实时引擎材质母版架构与参数化材质实例体系** *(Realtime Engine Master Material Architecture & Parameterized Material Instancing)* | UE 5.8 Material Instances Docs (`C`); Karis (2013) (`D`) | 历史表述偏向特定软件操作。重构为实时引擎通用的“母材质（Master Material）静态着色拓扑设计、动态标量/向量/贴图参数暴露、以及实例化（Material Instances）层级管理与性能优化”。 |
| **M06-U03** | 游戏运行时材质性能与约束 (ORM/BC7) *(Runtime Performance, BC7 & Texture Packing)* | `KEEP_AS_IS` | **V02-C37: 实时游戏运行时材质性能开销、通道打包与硬件压缩** *(Realtime Runtime Material Performance, Channel Packing & Hardware Compression)* | McDermott (2018) pp. 60–63 (`B`); UE 5.8 Texture Compression Docs (`C`); Karis (2013) (`D`) | 游戏交付端的工程技术约束。ORM 多通道合并、BC7/BC5/BC1 硬件纹理压缩、显存占用计算与材质复杂度开销控制。 |
| **M06-U04** | 影视/动画高保真着色差异 (SSS/Coat) *(Cinematic High-fidelity Shading: SSS, Coat)* | `CANDIDATE_REFRAME` | **V02-C38: 高保真多层着色模型物理特性与因果表达 (次表面/清漆/薄膜)** *(High-fidelity Multilayer Shading Physics: Subsurface, Clear Coat & Thin Film)* | OpenPBR Spec §3.3, §3.4 (`C`); Dinur (2026) Ch 11–12 (`B`); RTR4 Ch 9.6 (`B`) | 历史表述将 SSS/Coat 仅视为影视特定差异。重构为“基于 OpenPBR 多层介质模型对高阶物理外观（皮肤/玉石次表面散射、车漆清漆双层高光、氧化薄膜干涉）的参数理解与因果调控”。 |
| **M06-U05** | 跨渲染器着色表现差异对比 *(Cross-renderer Shading Discrepancies)* | `CANDIDATE_REFRAME` | **V02-C39: 跨渲染引擎着色差异分析与视觉一致性调校** *(Cross-renderer Shading Discrepancy Diagnosis & Visual Consistency Alignment)* | McDermott (2018) pp. 80–88 (`B`); RTR4 Ch 9.10 (`B`); OpenPBR Spec §1.1 (`C`) | 历史表述偏向被动比较。重构为“理解不同渲染器在微表面遮蔽（Smith/Kelemen）、环境光积分与色调映射（Tone Mapping）上的算法差异，主动排查并对齐视觉外观”。 |
| **M06-U06** | 多环境 IBL 与极端光照压力测试 *(Multi-environment IBL & Lighting Stress Testing)* | `KEEP_AS_IS` | **V02-C40: 多环境 IBL 旋转压力测试与严苛物理一致性验证** *(Multi-environment IBL Rotation Stress Testing & Rigorous Physical Consistency QA)* | Dinur (2026) Ch 12 (`B`); McDermott (2018) pp. 38–40 (`B`); OpenPBR White Furnace Test (`C`) | LookDev 质量验收的关键评判手段。通过室内暖光、室外高动态烈日、阴天冷光多套 HDR 环境旋转照射，检验材质是否在任何极端光照下均保持物理可信，不出现自发光或非自然死黑。 |

---

### Module 7: AI-Native Candidate Pool — Historical 13 Units

| v1 ID | Historical Candidate (v1) | Disposition | Proposed v2 Capability / Target | Owning Evidence & Class | Rationale & Gate 3 Relevance Hypothesis |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **AI-U01** | 材质语义提示词工程 *(Material Semantic Prompting)* | `RETIRE_OR_DEFER` | *(退役/不作为独立 Candidate)* | Sampler Generative Docs (`C`); 见 AI Impact Report §6.1 (`Synthesis Pointer`) | **RETIRE_OR_DEFER**：泛化的“提示词工程”属于易逝的操作技巧，不具备长期学科教学厚度。理解材料的物理工艺术语本身已经被 **V02-C01** 与 **V02-C15** 涵盖；纯文本自然语言交互不作为独立的 3D 材质底层能力。 |
| **AI-U02** | 参考图像条件约束与风格锚定 *(Reference Conditioning & ControlNet)* | `CANDIDATE_REFRAME` | **V02-C41: 几何条件引导与多模态参考约束的材质生成控制** *(Geometry-conditioned & Multimodal Reference-guided Material Generation)* | Dinur (2026) Ch 19 (`B`); IntrinsiX (2025) (`D`); ControlNet/IP-Adapter 文献 (`D`) | 历史表述偏向具体的 ComfyUI 插件操作。重构为通用的“利用几何线索（深度/法线/位置）与图像特征嵌入（Feature Embedding）对生成式纹理进行定向空间引导与保形约束”。 |
| **AI-U03** | 跨通道 PBR 物理诊断 *(Cross-channel PBR Physical Diagnosis)* | `KEEP_AS_IS` | **V02-C42: 跨通道 PBR 物理自洽性诊断与多贴图逻辑矛盾排查** *(Cross-channel PBR Consistency Diagnosis & Inter-map Logical Conflict Auditing)* | McDermott (2018) Appendix (`B`); 80 Level Tripo Interview (`D`); 见 AI Impact Report §6.1 (`Synthesis Pointer`) | 专门针对 AI 生成与多源贴图的体检诊断技能。排查例如“法线贴图有锐利深凹槽，但粗糙度贴图完全平滑无污垢响应”或“金属度为 1 但固有色极度暗黑”等跨通道逻辑撕裂。 |
| **AI-U04** | 人机协同分层迭代与局部微调 *(Human-in-the-Loop Layer Structuring)* | `CANDIDATE_REFRAME` | **V02-C43: 扁平生成纹理的非破坏性分层重构与局部受控修订** *(Non-destructive Layer Reconstruction & Localized Controlled Revision from Flat Textures)* | Shah (2022) Ch 3–4 (`A`); Meshy Docs (`C`); 见 AI Impact Report §6.1 (`Synthesis Pointer`) | 历史表述笼统。重构为现代核心能力：“将生成工具输出的扁平单层贴图，通过空间遮罩提取与通道解耦，逆向重构为可非破坏性微调的图层栈”，提供“只修改磨损而不破坏底色”的局部受控修订（Edit Locality）方案。 |
| **AI-U05** | 光照残留剥离与去光照修正 *(De-lighting Inspection & Correction)* | `KEEP_AS_IS` | **V02-C33: 漫反射光照残留诊断与反照率手工/算法去光照精修** *(De-lighting Inspection, Albedo Purity QA & Manual/Algorithmic Correction)* | IntrinsiX (2025) (`D`); LumiTex (2026) (`D`); Sampler Docs (`C`) | 独立成项。当前 AI 与单目采集生成的 Albedo 频繁残留阴影暗斑，导致重打光时穿帮。学生掌握检测残留光照、利用反向曲线与修复工具剥离阴影的实操精修技能。 |
| **AI-U06** | AI 材质变体策展与筛选 *(AI Material Variation Curation)* | `RETIRE_OR_DEFER` | *(退役/合并为艺术指导通用素养)* | Sampler Docs (`C`); 见 AI Impact Report §6.2 (`Synthesis Pointer`) | **RETIRE_OR_DEFER**：在大量生成草稿中进行人类审美筛选，其核心依据（物理合规、世界观契合、细节尺度）已被 **V02-C01**、**V02-C02** 与 **V02-C09** 覆盖，不占用独立 Gate 3 候选坑位。 |
| **AI-U07** | 版本控制与随机种子管理 *(Seed & Workflow Version Reproducibility)* | `RETIRE_OR_DEFER` | *(退役/合并入参数化管线通用要求)* | Sampler Docs Seed (`C`); 见 AI Impact Report §6.2 (`Synthesis Pointer`) | **RETIRE_OR_DEFER**：记录 Seed 和版本参数属于任何数字管线的通用工程纪律，已在 **V02-C27**（种子变体）与通用资产管理中体现，不构成独立的材质核心能力。 |
| **AI-U08** | AI 纹理接缝与伪影修复 *(AI Artifact & Seam Inpainting)* | `MERGE` | **合并入 V02-C13** | 80 Level Tripo Interview (`D`); Painter Docs (`C`) | AI 在 UV 接缝与凹陷处生成的拉伸伪影，其实质修复手段依托三维视口投影绘制、克隆画笔与空间修补遮罩，属于 **V02-C13** 的实战用例。 |
| **AI-U09** | 材质母版提示词驱动调参 *(Prompt-to-Parameter Control)* | `RETIRE_OR_DEFER` | *(退役/仅保留为概念推导)* | Node To Talk Docs (`C`/`D`); 见 AI Impact Report §6.3 (`Synthesis Pointer`) | **RETIRE_OR_DEFER**：属于实验性原型插件（Node To Talk）的临时功能。核心在于母材质参数暴露（**V02-C28**）与 Agent 接口（**V02-C45**），自然语言调参只是外壳包装。 |
| **AI-U10** | 资产血统与商用合规判断 *(Asset Provenance & Licensing Judgment)* | `RETIRE_OR_DEFER` | *(独立候选退役；其中与材质获取直接相关的商用合规决策吸收进 V02-C47)* | Adobe Firefly Licensing Docs (`C`); 见 AI Impact Report §6.3 (`Synthesis Pointer`) | **RETIRE_OR_DEFER（吸收与分流）**：作为独立技术候选退役。超出材质专业边界的广泛法务与伦理通识予以延后退役；其中涉及材质资产获取选型（如生成资产商用许可、模型合规风险）的具体决策条件，作为输入准则有机并入 **V02-C47**，消除无源孤岛冲突。 |
| **AI-U11** | 智能体节点图编排 *(Agentic Graph Orchestration)* | `CANDIDATE_REFRAME` | **V02-C45: 机器可读材质图表拓扑、序列化协议与智能体可操作性** *(Machine-readable Material Graph Topology, Serialization Protocols & Agent Operability)* | MaterialX Spec (`C`); Blender Python API (`C`); Designer Python API (`C`); DD3M (2024/2025) (`D`); Node To Talk Docs (`C`/`D`) | 历史表述偏向高深的多智能体编排。重构为底层的“理解结构化材质图表的拓扑表示、掌握 JSON/XML/代码序列化规范，使材质系统具备可被外部脚本与 AI Agent 安全解析、修改与验证的结构化特征”。 |
| **AI-U12** | 跨平台物理材质标准化映射 *(Standardized MaterialX/OpenPBR Translation)* | `SPLIT` | **拆分为 V02-C44 与 V02-C46** | OpenPBR Spec (`C`); MaterialX Spec (`C`); OpenUSD UsdShade Spec (`C`); UE 5.8 Docs (`C`) | **SPLIT 核心原因**：原单元混合了“开放标准材质语义与中立结构化表达（MaterialX/OpenPBR）”与“面向影视动画（USD/渲染上下文绑定）和实时游戏（引擎原生转换/性能约束）的双出口目标交付与损失适配”。表达层与交付层在工程实践中分属不同层级。 |
| **AI-U13** | 视觉特征约束规范制定 *(Visual Constraint Specification)* | `MERGE` | **合并入 V02-C40 与 V02-C42** | Dinur (2026) Ch 19 (`B`); 见 AI Impact Report §6.3 (`Synthesis Pointer`) | 设定反射率范围、粗糙度极值等约束指标，实质就是执行物理一致性验证与质检清单。与 **V02-C40** 及 **V02-C42** 重复。 |

---

## Part 3 — Lineage Accounting: Net-New Additions vs. Reframing / Splits

为了消除概念双重计算，明确建立唯一的 Lineage 谱系模型：

### 3.1 明确唯一身份归属
- **`V02-C44` 与 `V02-C46` 的身份定位**：
  - 两者均源自 **`AI-U12 (跨平台物理材质标准化映射)` 的结构化拆分（`SPLIT`）**。
  - `V02-C44` 继承并特化了 AI-U12 的“标准材质语义与结构化数据表达”职能；
  - `V02-C46` 继承并特化了 AI-U12 的“向目标引擎交付时的转换损失与管线适配”职能。
  - **结论：`V02-C44` 与 `V02-C46` 属于 `SPLIT` 产物，不再作为无源的 net-new ADD 重复计算**。

### 3.2 唯一真正净新增项 (Net-New ADD: 1 项)
在全量 47 项 v2 候选单元中，仅有以下 **1 项为历史 57 项完全未表达、纯由 Gate 2.5A 综合实证推导而出的净新增能力（Net-New ADD）**：

#### ADD-01: V02-C47 — 材质获取范式权衡决策：生成、检索、参数化复用与实拍转换 (Material Acquisition Paradigm Selection: Generation vs. Retrieval vs. Procedural Reuse vs. Capture)
- **Proposed Capability**: 面对具体资产与项目需求时，能够基于物理真实度、可控性、编辑自由度、资产血统与合规风险（吸收 AI-U10 相关切片）以及制作周期，科学决策并选择最优的材质获取范式（AI 文本/图像生成 vs. 现有标准资产库检索 vs. 参数化母材质派生 vs. 照片扫描采集推导 vs. 全手工绘制）。
- **Owning Sources & Classes**:
  - `Dinur (2026) Ch 1, 13, 19` (`B — Supporting Text`)
  - `80 Level Tripo Interview on Production Bottlenecks` (`D — Industry Evidence`)
  - `Adobe Firefly Licensing & Generative Policy Docs` (`C — Living Official Source`)
- **Evidence Pointer**:
  - `source-native-knowledge-index.md` Dinur Ch 19; `adobe-sampler-official.md` §2.4, §3.1; `ai-impact-on-material-workflows.md` §5.
- **Why It Materially Affects Gate 3**:
  - 历史 57 项受工具中心主义影响，预设“每次遇到材质任务均从零手工制作或单张图片生成”。
  - 在现代多工具/多模态生产环境中，盲目使用 AI 生成可能导致拓扑混乱、无法局部修订，反而成倍增加修复成本；而盲目从零手工制作又效率低下。掌握“何时生成、何时复用参数化母板、何时直接检索高质量资产库”的战略权衡能力，是面向 Gate 3 教学结构评估不可或缺的决策层候选能力。

---

## Part 4 — Lineage Map (Merge, Split, Retire & Add Tracing)

### 4.1 Merges (合并谱系 — 9 项 v1 单元合并归入相应 v2 目标)
1. **Merge 1: 几何特征驱动的自适应材质分层封装与模板复用 (V02-C14)**
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
6. **Merge 6: 材质获取范式权衡决策 (V02-C47)**
   - *Constituents*: `AI-U10` 中与资产获取、商用合规及血统判断直接相关的生产决策切片 $\to$ 合并入 **`V02-C47`**；超出材质专业边界的广泛法务伦理通识予以延后。
   - *Lineage*: `AI-U10 (Production Slice) -> V02-C47`
   - *Rationale*: 统一 lineage，解决一边退役一边引用的矛盾。
7. **Merge 7: 多环境 IBL 旋转压力测试与跨通道物理自洽性诊断 (V02-C40, V02-C42)**
   - *Constituents*: `AI-U13` (视觉特征约束规范制定) 吸收入 `V02-C40` 与 `V02-C42`
   - *Lineage*: `AI-U13 -> V02-C40, V02-C42`
   - *Rationale*: 设定约束规范实质就是执行物理一致性验证与质检清单，无独立存在必要。

### 4.2 Splits (拆分谱系 — 2 项 v1 单元拆分为 4 项)
1. **Split 1: 图像转材质通道估算 vs. 去光照物理精修**
   - *Original*: `M05-U03` (Image-to-Material 智能通道提取)
   - *Lineage*:
     - `M05-U03 (Part A) -> V02-C32` (**单张图像/照片多通道 PBR 属性算法推导与置信度评估**)
     - `M05-U03 (Part B) + AI-U05 -> V02-C33` (**漫反射光照残留诊断与反照率手工/算法去光照精修**)
   - *Rationale*: 单张图预测通道与 Albedo 中的阴影死黑剥离属于完全不同的算法逻辑与实操排错技能。
2. **Split 2: 开放标准材质表达 vs. 双出口目标交付与转换损失适配**
   - *Original*: `AI-U12` (跨平台物理材质标准化映射)
   - *Lineage*:
     - `AI-U12 (Part A) -> V02-C44` (**开放标准材质语义与结构化表示: OpenPBR 材质语义 + MaterialX 图元模式**)
     - `AI-U12 (Part B) -> V02-C46` (**双出口表示转换损失认知与目标交付适配: 影视 USD/渲染上下文绑定 + 实时引擎原生约束**)
   - *Rationale*: 标准语义描述（数据中立层）与下游具体生产交付（影视 UsdShade 材质绑定/多渲染器终端 vs. 游戏实时引擎原生转换/通道打包/Shader Permutations 优化层）存在显著的技术断层，拆分以明确表达层与双出口交付层的独立职责。

### 4.3 Retirements / Defers (退役与延后谱系 — 6 项)
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
   - *Lineage*: `AI-U10 -> RETIRED_OR_DEFERRED (Production slice absorbed into V02-C47)`
   - *Rationale*: 作为独立技术候选单元予以退役。超出材质专业边界的广泛法务与伦理通识移出材质候选池；其中直接关系材质资产选型决策的商用授权与模型合规边界条件，作为输入准则有机吸收进 V02-C47，消除无源孤岛冲突。

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
- **`V02-C44`**: 开放标准材质语义与结构化表示: OpenPBR 材质语义 + MaterialX 图元模式 *(Open Material Semantics & Structured Representation: OpenPBR Semantics + MaterialX Graph/Schema)*
  - *精确概念界定*：明确区分两层职责——**OpenPBR** 定义标准表面着色物理语义（Surface Shading Model / Parameter Semantics）；**MaterialX** 提供中立的强类型节点图数据结构、XML 内容模式与跨平台交换规范（Graph/Content Schema）。两者协同构成现代开放材质表达。
- **`V02-C45`**: 机器可读材质图表拓扑、序列化协议与智能体可操作性 *(Machine-readable Material Graph Topology, Serialization Protocols & Agent Operability)*
- **`V02-C46`**: 双出口表示转换损失认知与目标交付适配 (影视动画 USD/渲染上下文绑定 + 实时游戏原生转换约束) *(Dual-target Representation Conversion Loss Awareness & Delivery Adaptation: Animation/VFX USD Binding + Realtime Engine Constraints)*
  - *能力范围完整覆盖*：
    - **影视动画 / VFX 出口**：掌握基于 OpenUSD / `UsdShade` 的材质资产绑定架构（`UsdShadeMaterialBindingAPI`、直接绑定、集合与面子集 `GeomSubsets` 绑定），理解多渲染上下文终端机制（`outputs:surface`、`outputs:arnold:surface`、`outputs:mtlx:surface`）与跨 DCC/渲染器着色外观对齐。
    - **实时游戏 / Realtime 出口**：深刻理解外部标准表达（MaterialX/OpenPBR）导入游戏引擎（如 UE 5.8）时的转换损失边界，识别 BSDF 节点透传（Pass-through/inputs not connected）与退化，排查静态参数开关引发的着色器变体（Permutations）编译开销，满足目标管线的 ORM 打包、材质实例化（Material Instances）与显存/Draw Call 预算约束。
  - *核心认知模型*：$$	ext{Valid Representation} \quad 
eq \quad 	ext{Visual Equivalence} \quad 
eq \quad 	ext{Production Deliverable}$$

---

## Part 6 — Count & Change Summary

### 6.1 Statistical Breakdown
- **Historical Candidate Set v1 Total**: **57**
  - Traditional units: 44
  - AI-native candidate pool: 13
- **Audit Dispositions Applied to v1 (Accurate Table Count)**:
  - `KEEP_AS_IS`: **23** (概念健全，定义直接继承)
  - `CANDIDATE_REFRAME`: **17** (剔除软件中心化描述，提升为可迁移能力)
  - `MERGE`: **9** (合并入其他能力单元)
  - `SPLIT`: **2** (`M05-U03` 与 `AI-U12` 各自拆分为 2 项，共派生出 4 项能力)
  - `RETIRE_OR_DEFER`: **6** (`M05-U02`, `AI-U01`, `AI-U06`, `AI-U07`, `AI-U09`, `AI-U10` 广泛部分)
- **Mathematical Accounting Verification**:
  $$\text{Total Dispositions} = 23 + 17 + 9 + 2 + 6 = 57$$
- **Net-New Additions (`Net-New ADD`)**: **1** (`V02-C47`；注：`V02-C44` 与 `V02-C46` 已归入 `AI-U12` 的 `SPLIT` 谱系，不作重复计算)
- **Proposed Candidate Set v2 Total**: **47**
  - 直接保留与改写 (`23 + 17`): 40 项
  - 拆分生成 (`M05-U03` 派生 `C32, C33`；`AI-U12` 派生 `C44, C46`): 4 项（其中 C33 与原 AI-U05 融合）
  - 几何与管线合并精炼项 (`C14, C21, C25, C26`): 覆盖原合并项
  - 唯一净新增项 (`V02-C47`): 1 项
  - 经 Part 5 逐项核验，全量 proposed v2 列表包含稳定、唯一的 **47 个 Candidate ID** (`V02-C01` 至 `V02-C47`)。

### 6.2 Structural Health Indicators
1. **Total Count Rationality**: 总数由 57 收敛为 **47**。减少来源于消除 GUI 微操作碎片、退役纯软件操作外壳与易逝的文本提示词工程。
2. **Lineage Completeness**: 原 57 项历史候选单元每一项均拥有明确的去向记录，零孤岛、零隐式遗失。
3. **Concept Decoupling**: 明确拆分了生成估算与去光照精修，以及标准材质语义（OpenPBR）与结构化图模式（MaterialX）。

---

## Part 7 — Mandatory 10-Dimension Coverage Crosswalk (A–J)

为了确保 Candidate Set v2 完整覆盖工业界与未来技术需求，逐项核验 Part 1 声明的 10 个审计维度：

| 维度代号 | 核心维度名称 (Audit Dimension) | 对应覆盖的 v2 候选能力 (Covered v2 Candidates) | 覆盖状态 (Status) | 权威证据指针 (Evidence Pointer) | 覆盖分析与结论 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Dim A** | **Material / Appearance Causality**<br>*(物理与外观因果分析)* | `V02-C01`, `V02-C02`, `V02-C04`, `V02-C05`, `V02-C15`, `V02-C16` | **FULLY COVERED** | Dinur (2026) Ch 1, 3, 5 (`B`); RTR4 Ch 9 (`B`); OpenPBR Spec §1.1 (`C`) | 全面覆盖光照、几何、尺度与表面微观交互的因果物理模型，防止黑盒生成幻觉。 |
| **Dim B** | **Representation Choice**<br>*(材质表示范式选择)* | `V02-C22`, `V02-C28`, `V02-C29`, `V02-C44`, `V02-C47` | **CROSS-CUTTING COVERAGE / PROJECT SYNTHESIS** | MaterialX Spec §2 (`C`); OpenPBR Spec §Metadata (`C`); Designer Docs (`C`); Dinur Ch 19 (`B`) | **横切综合判定**：官方标准未提供单一现成的范式选择决策树，而是由节点图架构（C22）、参数暴露（C28）、SBSAR 运行时包（C29）、MaterialX 结构化表示（C44）以及获取范式权衡（C47）联合支撑“在位图贴图、程序化图表、开放标准描述与引擎原生材质间权衡选择”的项目综合心智模型。 |
| **Dim C** | **Representation Loss Awareness**<br>*(表示转换损失认知)* | `V02-C30`, `V02-C39`, `V02-C46` | **FULLY COVERED** | UE 5.8 MaterialX Matrix (`C`); MaterialX ShaderGen Guide (`C`); OpenPBR Spec §Flexibility (`C`) | 深入贯彻三层模型（$\text{Valid Representation} \neq \text{Visual Equivalence} \neq \text{Production Deliverable}$），覆盖烘焙位深损失、节点透传及跨渲染器差异。 |
| **Dim D** | **Controlled Revision / Edit Locality**<br>*(局部受控修订与编辑局部性)* | `V02-C12`, `V02-C13`, `V02-C28`, `V02-C43` | **FULLY COVERED** | Shah (2022) Ch 3–5 (`A`); Painter Layer/Mask Docs (`C`); Meshy Docs (`C`) | 确立“只修改磨损而不破坏底材”、“只调局部遮罩而不重跑全局生成”的局部非破坏性受控修订体系。 |
| **Dim E** | **Maintainability / Parameterization**<br>*(可维护性、复用与参数暴露)* | `V02-C14`, `V02-C27`, `V02-C28`, `V02-C29`, `V02-C36` | **FULLY COVERED** | Designer Values Docs (`C`); UE 5.8 Material Instances Docs (`C`); Shah Ch 6, 7 (`A`) | 覆盖参数暴露设计、黑盒模块化封装、动态材质实例以及随机种子重现性。 |
| **Dim F** | **Agent Operability**<br>*(智能体可读性与自动化操作)* | `V02-C22`, `V02-C44`, `V02-C45` | **FULLY COVERED** | MaterialX Spec (`C`); Blender Python API (`C`); Designer Python API (`C`); DD3M (`D`) | 覆盖结构化 DAG 拓扑、机器可读 XML/JSON 序列化与公开 API，使 Agent 能够安全读取、构建与验证材质。 |
| **Dim G** | **Generative vs. Retrieval vs. Reuse**<br>*(生成、检索与复用权衡)* | `V02-C14`, `V02-C29`, `V02-C41`, `V02-C47` | **FULLY COVERED** | Dinur (2026) Ch 19 (`B`); 80 Level Tripo Interview (`D`); Sampler Generative Docs (`C`) | 建立在面对具体制作需求时，科学权衡 AI 生成、资产库检索、参数化派生与实拍采集的战略决策能力。 |
| **Dim H** | **Validation / Diagnosis / Visual QA**<br>*(严苛验证、因果排错与质检)* | `V02-C03`, `V02-C21`, `V02-C33`, `V02-C35`, `V02-C40`, `V02-C42` | **FULLY COVERED** | McDermott (2018) pp. 80–92 (`B`); OpenPBR White Furnace (`C`); IntrinsiX (`D`); LumiTex (`D`) | 覆盖反射率安全直方图、去光照暗斑排查、烘焙法线黑边排错、跨通道自洽性诊断及多环境 IBL 旋转压力测试。 |
| **Dim I** | **Target Delivery / Lifecycle**<br>*(目标交付与下游运行时生命周期)* | `V02-C17`, `V02-C36`, `V02-C37`, `V02-C46` | **FULLY COVERED (DUAL-TARGET)** | **Animation/VFX**: `materialx-usdshade.md` §3.1–§3.2 (`C`) (UsdShadeMaterialBindingAPI, GeomSubsets, Render Contexts `outputs:arnold` / `outputs:mtlx`);<br>**Game/Realtime**: `unreal-substrate-target-sample.md` §2.1–§2.4 (`C`) (Pass-through BSDF, Shader Permutations, ORM BC7 Packing, Instances); Karis (2013) (`D`); McDermott (`B`) | **双出口真实覆盖**：<br>1. **Animation/VFX 出口**：通过 `V02-C46` 结合 `V02-C17`，覆盖 UsdShade 材质绑定、多渲染上下文（Render Context）多后端终端管理与离线渲染着色一致性；<br>2. **Game/Realtime 出口**：通过 `V02-C36`（母材质与实例体系）、`V02-C37`（ORM/BC7 通道打包压缩）与 `V02-C46`（引擎原生转换退化与变体开销），覆盖实时游戏交付刚性技术约束。 |
| **Dim J** | **Human Art Direction & Judgment**<br>*(人类艺术指导、审美意图与验收准则)* | `V02-C01`, `V02-C09`, `V02-C15`, `V02-C16`, `V02-C40`, `V02-C47` | **FULLY COVERED (CROSS-CUTTING)** | Dinur (2026) Ch 1, 3, 5 (`B`); Shah (2022) Ch 4–6 (`A`) | **横切整合处理**：未机械增设孤立的“审美课”，而是将艺术意图（叙事风化、多级频率解构、现实质感对照、最终质量验收）紧密锚定在观察、分层因果与验证全流程中。 |

---

## Part 8 — Unresolved Structural Hypotheses (Isolated E-Class Items)

以下前沿假说在审计中被讨论，但因当前仅依赖项目外推推理（Class $E$），缺乏权威的 $A/B/C/D$ 证据支持，严格隔离于 Candidate Set v2 之外：

### HYPO-01: AI Video Temporal Material Grounding & Consistency
- *Hypothesis*: 在 3D 材质与 AI 视频生成模型融合的工作流中，学生需要掌握“在动态重打光与连续帧下保持 3D 材质时序一致性”的专门能力。
- *Evidence Status*: 尽管 Dinur Ch 19 提及视频模型，但目前主流教材与行业规范均未将 3D-to-video 材质绑定形式化为稳定教学单元。
- *Disposition*: `UNRESOLVED STRUCTURAL HYPOTHESIS`。不进入 Candidate Set v2。

### HYPO-02: Universal Automated Multi-engine LookDev Pipeline
- *Hypothesis*: 要求本科学生手写完整的跨引擎（Cycles, EEVEE, Unreal）无头自动化测试流水线脚本执行作业批处理。
- *Evidence Status*: Blender 命令行无头运行虽在 Lane F 证实，但强制本科综合课程编写多引擎自动化测试管线超出合理教学范畴 ($E$)。
- *Disposition*: `UNRESOLVED STRUCTURAL HYPOTHESIS`。保留为 Gate 3 教师演示假说，不作为学生必修候选能力。

### HYPO-03: Real-time Neural BSDF / NeRF-to-PBR Material Inversion
- *Hypothesis*: 实时神经着色模型（Neural BSDFs）全面替代游戏引擎中的传统参数化 PBR 材质。
- *Evidence Status*: 属于前沿学术原型（SIGGRAPH/CVPR），但 Epic Games UE 5.8 官方文档表明基于 GGX/Substrate 的传统 PBR 仍是绝对的工业交付基线。
- *Disposition*: `UNRESOLVED STRUCTURAL HYPOTHESIS`。不进入 Candidate Set v2。

---

## Part 9 — Critical Anti-Inertia Review & Gate 3 Hypotheses

### The 2030 Counterfactual Test (Structural Audit Perspective)
> *"如果历史 57 项今天完全不存在，我们面对一个与强能力 AI Agent 协同的 2030 学生，在能力地图中还会设立这些候选单元吗？"*

1. **针对软件与 GUI 惯性的结构性清理假说**：
   - 审计确认已无任何候选单元单纯定义为特定软件的工作流外壳（如纯软件操作向导 `M05-U02` 已退役）；
   - 避免将软件菜单项直接映射为独立能力（如智能材质与生成器合并为 `V02-C14` 自适应封装，高低模准备合并入 `V02-C21` 烘焙细节映射）；
   - 17 项带有工具操作倾向的历史单元已被重写为跨平台通用的能力表述，为 Gate 3 教学评估提供了去厂商绑定的中立候选底座。
2. **针对泛化自然语言提示技巧的边界划分假说**：
   - 退役了 `材质语义提示词工程` (AI-U01)、`AI 材质变体策展与筛选` (AI-U06) 与 `材质母版提示词驱动调参` (AI-U09) 等易随模型更新而波动的操作技巧；
   - 将对材料物理工艺的理解 (**V02-C01/C15**) 与参数接口设计 (**V02-C28**) 作为结构性能力保留在候选池中，作为待在 Gate 3 验证持久性的教学假说。
3. **保留与重构候选单元在 Gate 3 审议中的差异化价值假说**：
   - **物理光学与因果法则**：能量守恒、反射率安全区间与微表面理论（C01–C05）在 v2 中保持结构性表达，为 Gate 3 提供检验算法生成贴图物理自洽性的诊断依据。
   - **结构化表示与 Agent 可操作性**：MaterialX 节点图、OpenPBR 语义与 DAG 拓扑（C22, C44, C45）在候选池中获得明确表达，作为人机协同与外部脚本安全操作的潜在数据接口。
   - **受控修订与编辑局部性**：扁平贴图反向分层重构与局部通道遮罩（C12, C13, C43）作为区别于一次性黑盒生成的候选能力，提交 Gate 3 评估其实操训练深度。
   - **交付损失认知与双出口生产就绪度**：坚持“文件语法合法 $
eq$ 外观一致 $
eq$ 生产可交付”（C46），为影视 USD 绑定与游戏实时性能约束提供双出口交付的教学审议对象。

---

*Artifact updated and hardened at `docs/research/candidate-set-rebaselining-audit.md` for Gate 2.5A.5 review.*
