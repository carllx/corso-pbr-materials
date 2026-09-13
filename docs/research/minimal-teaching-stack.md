# 《三维数字材质制作》最小教学内容栈 (Minimal Teaching Stack)

> **研究阶段**：Stage 2 Gate 3B — Minimal Content Selection  
> **前置门禁基准**：Gate 3A Teaching Layer Architecture PASS (Review Anchor: `cdbeaa1aca0efcc81b0b6e4f26170722d81a32db`)  
> **治理规范**：依据 GitHub Issue #5 (Gate 3 契约) 与 Issue #3 (Stage 2 总体策略)。  
> **核心使命**：回答唯一核心问题——“为了让学生达到已接受的 LO1–LO6，最少需要哪些 student-facing knowledge / practice / representation / tools？”严格执行“做减法”，剔除工具功能堆砌与不必要的动手冗余，确立紧凑、高迁移性、人机分工明确的最小教学内容组合。

---

## 目录
1. [定位与门禁边界声明 (Purpose & Gate Boundary)](#1-定位与门禁边界声明-purpose--gate-boundary)
2. [接受的核心学习成效参考 (Accepted LO1–LO6 Reference)](#2-接受的核心学习成效参考-accepted-lo1lo6-reference)
3. [最小教学单元清单 (Minimal Teaching Primitives Table)](#3-最小教学单元清单-minimal-teaching-primitives-table)
4. [跨成效全局最小性去重与合并检验 (Global Minimality & Deduplication)](#4-跨成效全局最小性去重与合并检验-global-minimality--deduplication)
5. [必须保留的学生实操体验 (Required Hands-on Experiences)](#5-必须保留的学生实操体验-required-hands-on-experiences)
6. [人机责任与自动化分工界限 (Human vs AI / Automation Split)](#6-人机责任与自动化分工界限-human-vs-ai--automation-split)
7. [软件与宿主职责裁决 (Software / Host Responsibilities)](#7-软件与宿主职责裁决-software--host-responsibilities)
   - 7.1 程序化创作宿主裁决 (Procedural Host: Blender vs Designer)
   - 7.2 Painter 的最小且不可替代角色 (Painter Role)
   - 7.3 采集与 AI 工具栈最低必要深度 (Acquisition / AI Stack)
   - 7.4 目标环境交付裁决 (Target Delivery: Primary vs Secondary)
8. [开放材质标准认知深度 (Standards Depth: OpenPBR / MaterialX / UsdShade)](#8-开放材质标准认知深度-standards-depth-openpbr--materialx--usdshade)
9. [几何、UV 与烘焙支撑底线 (Geometry / UV / Baking Support Floor)](#9-几何uv-与烘焙支撑底线-geometry--uv--baking-support-floor)
10. [容量分级架构：基础栈、弹性扩展与首批裁减 (Capacity Handling)](#10-容量分级架构基础栈弹性扩展与首批裁减-capacity-handling)
11. [Gate 3B 核心裁决结论总表 (Gate 3B Decision Findings)](#11-gate-3b-核心裁决结论总表-gate-3b-decision-findings)
12. [后置 Gate 3C 任务可行性待决事项 (Unresolved Decisions for Gate 3C)](#12-后置-gate-3c-任务可行性待决事项-unresolved-decisions-for-gate-3c)

---

## 1. 定位与门禁边界声明 (Purpose & Gate Boundary)

### 1.1 核心使命
Gate 3B 从 Gate 3A 的“学生最终应能做到什么（LO1–LO6）”切换为“产生这些结果的最小教学内容组合是什么”。

教学设计的推导链条为：
$$\text{Learning Outcome} \longrightarrow \text{Irreplaceable Teaching Gain} \longrightarrow \text{Minimum Teaching Primitive} \longrightarrow \text{Required Depth} \longrightarrow \text{Host/Tool Choice} \longrightarrow \text{Candidate Traceability}$$

### 1.2 严格防线与非目标 (Non-goals)
- **47 项 Candidate 保持为溯源研究目录，不是教学清单**：严禁按 Candidate 找理由塞入课程；
- **绝对不排 Week 1–8 周课表**：具体周次与课时分配属于 Stage 4 架构；
- **不编写完整大作业任务书与打分量表 (Rubrics)**：属于 Gate 3C 及以后阶段；
- **不扩张 Candidate Set v3**，不重新开启一手教材/文献研究；
- **不回填 47 项 Candidate 的 Teaching Actions**：回填属于 Gate 3D。

---

## 2. 接受的核心学习成效参考 (Accepted LO1–LO6 Reference)

依据权威基线文档 `docs/research/teaching-layer-architecture.md` (Review Anchor: `cdbeaa1aca0efcc81b0b6e4f26170722d81a32db`)，本 Gate 服务于已接受的 6 个核心学习成效：
- **LO1 (观察与意图)**：材质物理观察、艺术意图与情绪板多维解构；
- **LO2 (光学因果)**：光学因果推理与微表面物理可信性认知；
- **LO3 (分层与受控修订)**：多通道分层创作与空间局部受控修订；
- **LO4 (程序化与变体)**：参数化/程序化系统思维与变体控制；
- **LO5 (获取与 AI 评估)**：多源材质获取、AI 转换质量评估与混合精修；
- **LO6 (目标交付与验证)**：目标交付约束对齐、着色一致性调校与 LookDev 验证。

---

## 3. 最小教学单元清单 (Minimal Teaching Primitives Table)

经最小充分性归纳与提炼，达成 LO1–LO6 仅需 **14 个最小教学单元 (Teaching Primitives, TP-01 ~ TP-14)**：

| 编号 | 教学单元名称与学生直面能力 (Student-facing Capability) | 支撑成效 (Supports) | 要求深度 (Required Depth) | 动手必要性 (Hands-on Necessity) | 人机责任分工 (Human vs AI Split) | 支撑候选溯源 (Candidate Traceability) | 不可替代教学收益 (Why Required) | 简化/自动化替代机会 (Simplification / Automation) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TP-01** | **多维解构实物参考并建立材质意图清单**<br>能将实物参考照片解构为固有色、光泽粗糙度、微观起伏与时间演变四维特征，撰写明确的艺术意图。 | LO1 | `INDEPENDENT PRACTICE` | `MUST EXPERIENCE HANDS-ON`<br>*不亲手拆解，学生将无法建立主观艺术决策与物理真实度之间的锚点，易沦为盲目调参。* | **人**：审美判断、故事设定、视觉主次；<br>**机**：辅助色彩提取、关键词补全。 | `V02-C01`, `V02-C09` | 若删除，资产制作失去审美与物理目标，导致“虽然通道正确但质感平庸或逻辑混乱”。 | 教师提供结构化解构模板（Moodboard Template），免去学生排版负担。 |
| **TP-02** | **动态光照旋转与通道隔离审查**<br>能在视口中旋转动态环境光，并切入单通道（Base Color, Roughness, Normal, Metallic）逐一排查物理矛盾。 | LO2, LO6 | `INDEPENDENT PRACTICE` | `MUST EXPERIENCE HANDS-ON`<br>*若无亲手旋转光照与切通道排查，学生无法形成“光影变化产生质感”的光学因果直觉。* | **人**：动态光影肉眼质检、因果归因；<br>**机**：一键切通道快捷键、通道直方图统计。 | `V02-C02`, `V02-C03`, `V02-C04`, `V02-C05`, `V02-C42` | 若删除，学生无法诊断材质跨光照失真原因，会将光照缺陷误判为材质贴图问题。 | 预置标准化单键切通道与三光源/环境光旋转测试场景。 |
| **TP-03** | **反照率范围合规与色彩空间设置**<br>能利用参考基准（如 30–240 sRGB 经验区间）诊断 Base Color 过曝或过暗，并纠正数据贴图（Raw/Linear）误标为 sRGB 的色彩空间错误。 | LO2 | `INDEPENDENT PRACTICE` | `MUST EXPERIENCE HANDS-ON`<br>*色彩空间配置若不亲手修正，学生对“数据贴图伽马校正导致粗糙度发白”的隐蔽故障毫无排查经验。* | **人**：判断材质物理属性类别、核查反照率区间；<br>**机**：色彩管理自动读取规则、越界像素高亮提示。 | `V02-C03`, `V02-C08`, `V02-C10` | 若删除，渲染时产生过曝光斑或粗糙度失真，破坏能量守恒可信性。 | 教师提供 PBR 反照率参考色板（Albedo Cheat Sheet）与色彩空间自检预设。 |
| **TP-04** | **AO 与阴影从固有色中解耦**<br>能识别出 Base Color 贴图中误烘死的高对比度直射阴影或强环境遮挡，并将其修正为中立反照率。 | LO2, LO5 | `INDEPENDENT PRACTICE` | `MUST EXPERIENCE HANDS-ON`<br>*不亲手剔除一次烘死阴影，学生无法理解漫反射光照与物体固有属性的根本解耦关系。* | **人**：识别直射光投射与局部自遮挡特征；<br>**机**：去光照（Delight）算法前向分离阴影。 | `V02-C04`, `V02-C32` | 若删除，资产在逆光或背光时将出现黑斑与假阴影，无法在动态光照下使用。 | 提供一键调用 Delighting 算法工具，学生只需判定残余阴影并做画笔曲线微调。 |
| **TP-05** | **非破坏性“底材-涂层-磨损-脏污”图层栈搭建**<br>能按照物理工艺演进逻辑搭建非破坏性多通道图层架构，实现逻辑自洽的材质历史表现。 | LO3 | `INDEPENDENT PRACTICE` | `MUST EXPERIENCE HANDS-ON`<br>*若不亲手搭建，学生无法理解多通道同步更新的非破坏性生产架构。* | **人**：规划材料层级关系、控制混合逻辑与细节尺度；<br>**机**：程序噪波填充、基础底色平铺。 | `V02-C11`, `V02-C12`, `V02-C15`, `V02-C16` | 若删除，学生创作过程退化为不可逆的手工涂抹，完全丧失版本修改能力。 | 提供多通道分层标准图层模板（Layer Stack Preset）。 |
| **TP-06** | **空间自适应遮罩调配与局部锚点联动**<br>能利用曲率/AO 等几何特征生成初始破损遮罩，结合锚点（Anchor）或图层引用实现上下层细节动态联动。 | LO3 | `INDEPENDENT PRACTICE` | `MUST EXPERIENCE HANDS-ON`<br>*不亲手配置遮罩生成器与微调参数，学生无法领会“几何驱动纹理”与细节协同变化的因果关系。* | **人**：调整破损平衡、判定磨损合理性；<br>**机**：几何曲率与遮挡位置计算、生成器初稿计算。 | `V02-C13`, `V02-C14`, `V02-C15` | 若删除，细节分布失去与三维形体的关联，沦为漂浮在表面的均匀平铺噪波。 | 预置标准 Generator 组合与遮罩微调预设。 |
| **TP-07** | **艺术指导下的受控局部版本修订**<br>面对明确的修改意见（如缩小局部掉漆面积并改变底漆色相），能精准定位并修改对应遮罩与通道，保持其余部分完全稳定。 | LO3 | `INDEPENDENT PRACTICE` | `MUST EXPERIENCE HANDS-ON`<br>*工业生产核心痛点即为受控版本迭代，不亲手体验修订就会发生“牵一发而动全身”的推倒重来。* | **人**：执行艺术指导意图、划定受控修订边界（Edit Locality）；<br>**机**：无破坏图层缓存重算。 | `V02-C12`, `V02-C14`, `V02-C43` | 若删除，学生无法应对生产中的反复修改诉求，丧失工业流水线协作基本能力。 | 教学提供“已完成资产+修改反馈单”，学生仅在局部图层上做定向修订练习。 |
| **TP-08** | **紧凑节点流搭建与数据类型对齐**<br>能在 DAG 节点图中正确连接标量、向量与颜色数据，运用乘加与范围重映射（Map Range）控制数值区间。 | LO4 | `SUPPORTED / TEMPLATE PRACTICE` | `MUST EXPERIENCE HANDS-ON`<br>*数据类型不匹配与数值范围溢出是节点图最大绊脚石，必须亲手连线纠错才能建立抽象数据流直觉。* | **人**：设计逻辑因果链条、判定数值映射端点；<br>**机**：节点图自动编译、即时视口着色。 | `V02-C22`, `V02-C24`, `V02-C25` | 若删除，学生对程序化着色完全黑盒化，无法理解现代着色器的基本工作逻辑。 | 限制节点总数在 15 个以内；提供半成品模板节点组，学生专注核心运算连接。 |
| **TP-09** | **平铺重复消除与参数化变体接口暴露**<br>能使用噪波混合打破贴图连续平铺重复感，封装 Node Group 并暴露 3–5 个有语义的外部调节参数（如粗糙度偏移、破损密度）。 | LO4 | `INDEPENDENT PRACTICE` | `MUST EXPERIENCE HANDS-ON`<br>*不亲手暴露参数并拉动验证，学生无法理解“母材质/参数化资产”的工业复用价值。* | **人**：定义参数语义与可用数值范围、把控多变体美感；<br>**机**：程序随机种子重新分形计算。 | `V02-C26`, `V02-C27`, `V02-C28` | 若删除，材质生产退化为只能生产单一死尺寸资产，失去工业化规模复用思维。 | 基础噪波组合使用预置资产，学生只需完成重映射与 Group Input 暴露。 |
| **TP-10** | **材质多范式获取权衡决策**<br>针对具体资产需求，能理性对比分析从资产库检索、实物拍摄采集、AI 生成与从零手绘的成本、版权与可控性优劣并作出选择。 | LO5 | `RECOGNIZE & EXPLAIN` | `DEMO SUFFICIENT`<br>*范式权衡是高阶决策思维，重在方法论与标准权衡，无需学生逐个工具从头配置一遍。* | **人**：评估制作工期、版权合规、艺术风格可控度；<br>**机**：资产库搜索引擎、AI 提示词联想。 | `V02-C30`, `V02-C31`, `V02-C41` | 若删除，学生在实际项目中易走向“盲目手绘一切”或“盲目 AI 抽卡”的极端效率陷阱。 | 提供典型资产需求场景选择题或案例分析表。 |
| **TP-11** | **图像转材质通道级评估与光照解耦精修**<br>能对单图/AI 生成材质输出的 Normal、Roughness、Base Color 等通道分别查验，运用算法去光照结合手动工具消除定向光照伪影与缝隙。 | LO5 | `SUPPORTED / TEMPLATE PRACTICE` | `MUST EXPERIENCE HANDS-ON`<br>*不亲手对生成结果进行通道级抓虫与去光照，学生会盲信 AI 贴图“一键可用”，留下严重渲染隐患。* | **人**：识别假光影、假凹凸与接缝；判定各通道可信度；<br>**机**：AI/算法估计各通道初稿、AI 辅助无缝拼接。 | `V02-C32`, `V02-C33`, `V02-C34`, `V02-C47` | 若删除，AI 材质无法成为合规生产力，生产管线将被劣质脏数据污染。 | 采用现成 Image-to-Material / Delighting 预设滤镜，专注精修与通道复核。 |
| **TP-12** | **目标约束下的贴图打包与材质实例配置**<br>能根据下游目标规范（如游戏引擎 ORM 打包、线性通道压缩），配置导出预设并将贴图赋予目标材质实例。 | LO6 | `INDEPENDENT PRACTICE` | `MUST EXPERIENCE HANDS-ON`<br>*贴图通道未正确打包或通道分配错位是跨平台交付最常见失误，必须亲手导出并组装一次。* | **人**：确认通道映射对应关系（R/G/B/A）；<br>**机**：批量贴图导出与多通道自动化合成打包。 | `V02-C17`, `V02-C35`, `V02-C37` | 若删除，资产停留在创作软件视口，无法进入任何下游实时或渲染生产环境。 | 教师提供标准导出 Preset 与预置母材质（Master Material）。 |
| **TP-13** | **跨环境外观一致性检验与残余差异归因**<br>能在目标视口中检验材质质感，调校参数达到可接受视觉一致性，并能专业解释为何无法做到 100% 绝对等同。 | LO6 | `INDEPENDENT PRACTICE` | `MUST EXPERIENCE HANDS-ON`<br>*不亲手在目标环境中对质感进行对比与调校，学生就无法打破“软件视口好看等于渲染好看”的幻觉。* | **人**：对比两端质感差异、调校实例参数；解释色调映射与微表面模型差异；<br>**机**：目标引擎实时渲染着色计算。 | `V02-C36`, `V02-C38`, `V02-C40` | 若删除，学生无法掌握“以最终交付环境为准”的 LookDev 基本职业准则。 | 提供标准一键同步场景或双视口对照工程。 |
| **TP-14** | **开放材质标准概念映射与结构化认知**<br>能理解 OpenPBR 表面物理语义与 MaterialX 结构化表示对跨软件资产流转的价值，解释为何参数化图比扁平位图更具自动化修改优势。 | LO2, LO4, LO6 | `RECOGNIZE & EXPLAIN` | `DEMO SUFFICIENT`<br>*理解标准语义与数据表示模型足以支撑认知跃升，不需要学生去手写底层代码或强行连线。* | **人**：理解跨平台统一语义与机器可维护性逻辑；<br>**机**：底层解析器转换与代码生成。 | `V02-C44`, `V02-C45`, `V02-C46` | 若删除，学生认知受限于特定软件封闭格式，无法理解现代工业标准演进。 | 教师通过直观图示与对比演示（如 OpenPBR 规范映射表）展示。 |

---

## 4. 跨成效全局最小性去重与合并检验 (Global Minimality & Deduplication)

为了确保 14 个 Teaching Primitives 达到“全局最小”，逐项执行 5 项全局最小性测试：

### 4.1 五项测试标准定义
- **Test A — 依赖与重叠测试 (Dependency & Overlap)**：是否存在其他单元能完全替代其学习收益？若有则合并。
- **Test B — 默会认知测试 (Tacit Learning)**：学生是否必须亲手操作？若看演示即可获得同等认知，则降级为 `RECOGNIZE & EXPLAIN` 或 `TEACHER DEMONSTRATION`。
- **Test C — 自动化替代测试 (Automation)**：机械操作是否可由工具/AI 代劳？只保留人类的因果模型、诊断与审美判断。
- **Test D — 跨工具迁移测试 (Transfer)**：是特定软件的死记菜单，还是可迁移至多工具的通用心智模型？
- **Test E — 8 周学时收益比 (8-week ROI)**：在有限容量下，该单元是否产生最高价值的教学转化？

### 4.2 去重与合并执行记录 (Deduplication Audit Log)
1. **合并烘焙与网格准备至底层支撑**：
   - *原考量*：将高低模烘焙（V02-C18 ~ C21）拆为独立实操单元；
   - *测试结论*：违反 Test E 与课程定位（非建模课）。将烘焙降为 LO3/TP-06 的**前置支撑底线（Support Floor）**，由教师提供已烘焙好的资产，仅保留最小自检，大幅削减手动实操。
2. **合并多通道绘制与局部修饰**：
   - *原考量*：将 Base Color 绘制、Roughness 涂抹、Normal 刻画拆为 3 个独立单元；
   - *测试结论*：违反 Test A。现代工作流是多通道同步关联的，合并为 **TP-05（图层栈搭建）** 与 **TP-06（遮罩联动）**。
3. **合并图像去光照、无缝拼接与 AI 估计**：
   - *原考量*：分别开设“图像无缝平铺教程”、“AI 材质生成实操”、“Delighting 滤镜教学”；
   - *测试结论*：违反 Test A 与 Test C。合并为 **TP-11（图像转材质通道级评估与光照解耦精修）**。工具一键完成运算，学生只负责通道独立验证与局部精修。
4. **移除手写 MaterialX / UsdShade 代码**：
   - *测试结论*：违反 Test B 与 Test E。手写 XML/Python 代码属于管线工程师范畴，对本科材质创作者的 8 周 ROI 极低。归入 **TP-14（概念映射与结构化认知，RECOGNIZE & EXPLAIN）**，动手深度降为 0。
5. **移除 Agent 编排实操**：
   - *测试结论*：违反 Test E。学生不需要在 8 周内“编写 Agent 系统”，只需理解结构化节点图利于自动化，归入 TP-09 与 TP-14 的概念认知。

---

## 5. 必须保留的学生实操体验 (Required Hands-on Experiences)

在 14 个 Primitives 中，经过严格默会知识检验，**仅保留 10 个学生必须亲自动手的核心实验 (Required Hands-on Experiences, HO-01 ~ HO-10)**：

```
                    ┌────────────────────────────────────────────────────────┐
                    │     10 个不可替代的学生亲身动手体验 (HO-01 ~ HO-10)     │
                    └───────────────────────────┬────────────────────────────┘
                                                │
         ┌──────────────────────────────┬───────┴──────────────┬──────────────────────────────┐
         ▼                              ▼                      ▼                              ▼
  【物理因果与诊断体验】         【资产图层与受控修订】         【节点抽象与参数暴露】         【获取精修与目标交付】
  HO-01: 情绪板多维特征解构     HO-04: 多通道工艺图层装配      HO-06: 紧凑节点连接与范围截断  HO-08: AI/图像通道排错与去光
  HO-02: 动态光照与单通道排错   HO-05: 定向局部版本受控修订    HO-07: 平铺打散与参数接口暴露  HO-09: 目标约束贴图打包配置
  HO-03: 反照率与色彩空间纠偏                                                                 HO-10: 目标视口质感调校对齐
```

### 10 项核心实操明细：
1. **HO-01 (对应 TP-01)**：面对一个具风化痕迹的工业或自然物品，亲手标注并解构其四维物理与工艺特征。
2. **HO-02 (对应 TP-02)**：在一个包含 3 个典型物理矛盾（如法线翻转、固有色含强阴影、金属度杂色）的视口场景中，旋转光照并切单通道逐一识别指出。
3. **HO-03 (对应 TP-03)**：动手纠正一张被错误应用 sRGB 伽马校正导致泛白的数据贴图，使其在线性色彩空间下恢复正确表现。
4. **HO-04 (对应 TP-05, TP-06)**：在资产模型上构建“底材-涂层-磨损-污垢”图层栈，并利用几何遮罩实现局部磨损边界自然过渡。
5. **HO-05 (对应 TP-07)**：接收一份模拟艺术指导修改单（如“局部掉漆缩小并露出红锈底漆”），在 20 分钟内完成局部受控修改，无关图层保持不动。
6. **HO-06 (对应 TP-08)**：在受限的 10–15 节点范围内，正确连接标量与颜色运算，使用 Map Range 消除高光溢出。
7. **HO-07 (对应 TP-09)**：为程序化材质接入平铺打散噪波，并将 3 个关键变量封装并暴露到材质面板，拖动滑块验证变体生成。
8. **HO-08 (对应 TP-11)**：将一张带日光强阴影的实拍/AI 贴图导入工具，执行去光照处理并手动修补残留接缝与阴影死黑，在视口中验证背光效果。
9. **HO-09 (对应 TP-12)**：按照引擎规范（如 R=AO, G=Roughness, B=Metallic），亲手在导出面板中完成一次通道合并打包导出。
10. **HO-10 (对应 TP-13)**：将导出的材质赋予目标环境的测试资产，对比源视口与目标视口的质感差异，微调实例参数使两者达到可接受的一致性。

---

## 6. 人机责任与自动化分工界限 (Human vs AI / Automation Split)

为防止将宝贵的学生注意力消耗在低级重复劳动中，确立全课程的人机责任分工红线：

| 领域 | 学生必须亲自负责的核心能力 (人类不可替代) | 工具、算法、脚本与 AI 代劳的机械操作 (应尽量自动化) | 自动化手段与教学支撑减负方案 |
| :--- | :--- | :--- | :--- |
| **观察与意图** | 确立艺术风格定位、生活经历故事假说、视觉中心与细节主次层级平衡。 | 参考图片像素提取、关键词检索、画幅裁剪。 | 预置情绪板排版模板，支持一键色卡吸取。 |
| **物理可信性** | 依据因果推理排查逻辑冲突；在动态光照下评判质感是否符合物理常理。 | 计算微表面 BRDF 微分方程；贴图直方图数值统计分布计算。 | 软件实时渲染计算与直方图诊断指示器。 |
| **分层绘制** | 规划图层堆栈架构；决定磨损与环境风化的空间分布逻辑；受控修订边界。 | 手工逐像素绘制基础底色；重复铺设基础噪波底纹；图层通道逐个手动分配。 | 智能材质预设、基础材质库、自适应几何遮罩生成器。 |
| **程序化系统** | 设计逻辑因果链路；确定暴露给外界的参数接口与合理数值上下限。 | 手工编写底层 HLSL/GLSL 数学代码；基础数学运算拓扑展开。 | 封装好的高阶节点组（Node Groups）、宏节点。 |
| **材质获取** | 审视生产约束并决策最佳获取范式；逐通道验收 AI 生成贴图的质量与可控性。 | 贴图无缝拼接算法求解；单张图像前向生成多通道贴图的初始估计。 | Substance 3D Sampler 算法滤镜、开源 AI 生图插件一键生成。 |
| **目标交付** | 双视口主观质感对比；调校实例参数；解释技术与色调映射差异原因。 | 贴图通道拼接计算（将三张单色图合成一张 RGB 图）；批量规范重命名；格式压缩转码。 | 预置一键导出预设（Export Presets）、材质自动绑定脚本。 |

---

## 7. 软件与宿主职责裁决 (Software / Host Responsibilities)

### 7.1 程序化创作宿主裁决 (Procedural Host Decision: Blender vs Designer)

针对 LO4 的程序化教学宿主，进行系统对比与最终裁决：

| 评价维度 | Blender Shader Nodes | Substance 3D Designer | 教学裁决权衡 (Decision Tradeoff) |
| :--- | :--- | :--- | :--- |
| **1. LO4 教学收益** | **极高**。直接在着色器上下文体验“数据流 $\to$ 表面质感”，即时可视反馈极快。 | **极高**。工业级离线贴图生成标准，参数化与图案合成极为严谨。 | 教学收益相当，均能完整建立 DAG 数据流与暴露参数思维。 |
| **2. 学习成本** | **低-中**。学生多半已有基础视口认知；节点系统轻量直观，易于理解。 | **高**。全新软件界面、抽象的数据流、复杂的原子节点与函数系统，认知摩擦大。 | **Blender 显著占优**。在 8 周限制下，Designer 会吞噬大量基础操作课时。 |
| **3. 跨 LO 环境共用** | **极高**。Blender 可同时承担 LO2 物理因果观察、LO4 节点实操、LO6 渲染验证与双目标比对。 | **低**。仅服务于程序化材质生成，后续资产绘制仍需跳出到 Painter。 | **Blender 显著占优**。大幅减少学生在不同大型软件间切换的认知负荷。 |
| **4. 认知切换成本** | **单一集成环境**。在同一视口内完成材质节点调节与光照/渲染观察。 | **高碎片化**。需在 Designer、Painter、引擎三个完全不同逻辑的 UI 间反复横跳。 | **Blender 显著占优**。8 周课程严防“多软件认知超载”。 |
| **5. 模板减负能力** | **强**。可通过 Node Group 模板封装复杂噪波，学生仅需连线核心重映射。 | **强**。同样可通过 SBS 模板减负，但整体软件概念包袱依然沉重。 | 平手。 |
| **6. 知识可迁移性** | **通用着色语言直通性**。其数学与节点拓扑直接迁移至 Unreal/Unity/MaterialX。 | **工业贴图管线专精**。高度适合大型环境资产与程序化贴图库生产。 | Blender 的节点概念对实时引擎材质编辑器迁移更为直接顺畅。 |
| **7. AI 时代持久价值** | **高**。Blender API 完善，开源生态与 LLM/Agent 代码交互极其成熟。 | **高**。SBS 格式是工业资产参数化标准。 | 平手。 |

#### 最终裁决：
- **Primary Recommended Host (主要实操宿主)**：**Blender Shader Nodes**。
  - *理由*：在 8 周有限学时内，Blender 以最低认知切换成本（Zero Cost / Single Environment）达成 LO4 核心目标；学生直面“输入 $\to$ 映射 $\to$ BSDF 输出”通用流程，避免被 Designer 庞大的独立工业体系拖垮。
- **Secondary / Demo Host (辅助/演示宿主)**：**Substance 3D Designer**。
  - *定位*：仅作为**教师演示与工业标准概念参考 (`TEACHER DEMONSTRATION` / `RECOGNIZE & EXPLAIN`)**。通过教师演示 1 个标准 SBS 资产及 SBSAR 参数发布，让学生理解工业贴图母图集的生产形态，**学生显式无需独立掌握 Designer 完整操作**。
- **学生显式无需学习的内容 (Explicitly NOT Needed)**：
  - 显式无需手写 Designer 像素处理器（Pixel Processor）或自定义函数图（Function Graphs）；
  - 显式无需掌握 Designer 复杂的贴图烘焙模型传递节点；
  - 显式无需背诵数十个微观原子节点菜单。

---

### 7.2 Painter 的最小且不可替代角色 (Painter Role)

Substance 3D Painter 在当前课程架构中重新定位，避免盲目承担全部教学负荷：

1. **Painter 不可替代的核心角色 (Indispensable Role)**：
   - **LO3（资产三维空间分层绘制与局部修订）的唯一核心承载宿主**：Painter 在三维模型表面的直接投射绘制、基于几何法线/曲率贴图的自适应遮罩生成（Smart Masks）、多通道同步混合以及非破坏性图层栈管理，具备行业不可替代的直观操作优势。
2. **Painter 中应大幅压缩的操作 (Compressible Operations)**：
   - **基础模型 UV 展开与编辑**：全面压缩为 0 手动实操，使用提供好的合规模型；
   - **从零手绘精细图案**：压缩手绘时间，引导学生使用几何投射、模板与程序遮罩替代纯手绘；
   - **常规贴图烘焙配置**：压缩手动调参，依托 Painter 预设模板或自动烘焙直接生成支撑贴图。
3. **Painter 中应自动化的操作 (Automatable Operations)**：
   - **贴图批量重命名与通道打包导出**：通过预配置好的 Export Presets 一键导出，学生不再手动拼图；
   - **基础材质打底**：通过调用内置 Smart Materials 快速铺设基础层级。
4. **Painter 中降为演示/仅参考的深度 (Demo/Reference Depth)**：
   - 自定义 QML 插件开发与 JavaScript 自动化批处理；
   - 手动配置复杂的 UDIM 多象限贴图分发管线；
   - 自定义 HLSL 着色器接入。

---

### 7.3 采集与 AI 工具栈最低必要深度 (Acquisition / AI Stack)

严禁将 LO5 办成“AI 工具大进展”，确立最低必要工具组合：

1. **最低实践组合裁决**：
   - **实拍采集 (Photo Capture)**：`SUPPORTED PRACTICE`。手机拍摄受控参考图，重点理解光照均匀度与色彩校正，不引入专业偏振十字摄影硬件。
   - **图像转材质 (Image-to-Material)**：`SUPPORTED / TEMPLATE PRACTICE`。选用 **Substance 3D Sampler** 或 **Blender AI 插件/轻量生成工具** 中的 Image-to-Material / Delighting 滤镜，学生亲身体验一次“单图生成四通道 + 去光照精修”。
   - **生成式 AI 生图 (Generative AI)**：`RECOGNIZE & EXPLAIN` / `TEACHER DEMONSTRATION`。通过演示理解文生贴图/图生贴图的边界与可控度，**不强制学生掌握复杂 Prompt 工程与私有模型部署**。
   - **资产库检索 (Retrieval)**：`INDEPENDENT PRACTICE`。鼓励在 Poly Haven 等开源平台检索标准 PBR 资产作为高质量对照基准。
2. **学生真正需要独立实践的本质**：
   - 是 **“通道级多维质量验证与去光照精修 (Validate, Diagnose & Refine)”**，而不是掌握五花八门的生成模型操作。

---

### 7.4 目标环境交付裁决 (Target Delivery: Primary vs Secondary)

根据 dual-target 现实，裁定最小交付教学策略：

1. **Primary Practice Target (主要实操交付目标)**：
   - **轻量实时视口环境 (Blender EEVEE Next 或 轻量 Unreal Engine 5 模板工程)**。
   - *理由*：提供即时、交互式的光照响应与视口反馈，能在最短时间内验证材质在不同光源旋转下的物理可信度，且环境搭建成本可控。
2. **Secondary Comparison Target (次要对比/演示目标)**：
   - **离线光线追踪环境 (Blender Cycles)**。
   - *定位*：仅作为**对照组 (`SUPPORTED / COMPARISON PRACTICE`)**。在相同资产上切换至 Cycles 渲染，直观对比多重漫反射反弹、精确微表面高光与次表面散射的细微差异，回答“为何实时与离线无法 100% 绝对一致”。
3. **明确规避**：
   - 严禁要求学生分别完整学习一套游戏开发管线和一套影视灯光渲染全流程；两者统一在“材质物理属性在不同着色器计算下的表现差异”这一单一材质视角下。

---

## 8. 开放材质标准认知深度 (Standards Depth: OpenPBR / MaterialX / UsdShade)

严格执行 Gate 3A 的语义切分，对三大开放标准划定学生直面深度：

| 标准名称 | 核心工业定位 | 学生直面深度 (Student-facing Depth) | 具体要求与操作边界 | 如果学生完全不亲手编码，是否影响 LO 达成？ |
| :--- | :--- | :--- | :--- | :--- |
| **OpenPBR** | 通用表面材质物理语义标准 | `RECOGNIZE & EXPLAIN` | 理解 Base, Specular, Transmission, Coat 等标准层级语义；理解 Painter 12.1 默认 OpenPBR 工作流参数。无需手写着色器。 | **NO**。完全不影响。学生在 Painter/Blender 中调节物理参数时已隐式运用其语义。 |
| **MaterialX** | 结构化材质图与内容表达规范 | `RECOGNIZE & EXPLAIN` / `TEACHER DEMONSTRATION` | 理解材质作为中立、强类型数据图的价值；理解节点图优于扁平位图的机器可维护性。**学生不直接编写 XML 代码，不直接配置 ShaderGen**。 | **NO**。完全不影响。Blender 节点逻辑与 MaterialX DAG 拓扑高度同构，在 Blender 中动手即可达成因果直觉。 |
| **UsdShade** | 场景材质绑定与渲染上下文 | `INFRASTRUCTURE / TEACHER REFERENCE` | 理解 USD 资产引用概念及“材质绑定至网格”的解耦逻辑。**学生不调用 Python/C++ API 进行编程**。 | **NO**。完全不影响。场景材质赋予在任何 DCC 视口拖拽均可体验其概念。 |

> **关键仲裁结论**：
> 学生**完全不需要**在课程中直接打开文本编辑器编写 MaterialX XML，也**完全不需要**手写 UsdShade 绑定脚本。他们只需在通用节点视口（Blender）中建立 DAG 数据流直觉，并通过教师演示理解其工业标准化价值，即可 100% 达成全部 6 个 Learning Outcomes。

---

## 9. 几何、UV 与烘焙支撑底线 (Geometry / UV / Baking Support Floor)

为了让 LO3 和 LO6 正常工作，同时严防课程退化为建模/展 UV 课，确立最低前置支撑底线（Support Floor）：

1. **UV 知识最低底线 (UV Floor)**：
   - **概念底线**：理解 UV 展开是将三维表面展平为二维坐标系的过程；理解“接缝（Seam）”与拉伸对贴图分辨率的影响；
   - **实操底线**：学生**显式不需要**从零手动剪切缝合复杂模型 UV；教学全过程采用教师预置展开完毕的资产模型；学生仅需能识别出“UV 严重拉伸或颠倒”的显示现象。
2. **硬边与接缝知识底线 (Hard-edge & Seam Floor)**：
   - **概念底线**：理解法线贴图烘焙中“平滑组/硬边必须对齐 UV 缝隙”的基本工程常识，防止烘焙黑线；
   - **实操底线**：教师演示 1 次常见黑边成因，提供的资产已预处理合规。
3. **烘焙知识最低底线 (Baking Floor)**：
   - **概念底线**：理解高模细节向低模传递的法线贴图（Normal Map）与几何掩膜（Curvature, AO, Position）原理；
   - **实操底线**：在 Painter 内体验**一键加载模型自动烘焙（Baking Mode / F8）**，学生无需手动调节复杂的笼子（Cage）膨胀距离或手动修复复杂偏斜（Skew），只需确保贴图计算正常生成。
4. **几何贴图支撑底线 (Geometry Maps Floor)**：
   - 仅需学生认识 Curvature（曲率驱动凸起磨损与凹陷脏污）、AO（自遮挡积灰）、Position（地表渐变）三张核心支持图对智能遮罩的作用。

---

## 10. 容量分级架构：基础栈、弹性扩展与首批裁减 (Capacity Handling)

为了应对实际教学学时可能出现的波动，建立弹性的三级容量配置模型：

```
     ┌─────────────────────────────────────────────────────────────┐
     │             弹性扩展栈 (Capacity-sensitive Extensions)        │
     │   (仅当总学时 > 72h 或学生 3D/代码基础极佳时激活: 见 10.2)      │
     ├─────────────────────────────────────────────────────────────┤
     │                                                             │
     │             基础教学栈 (Base Stack — 最小可行核心)            │
     │         (基准规划情境: 56–72h, 14 个 Primitives + 10 实操)      │
     │                                                             │
     ├─────────────────────────────────────────────────────────────┤
     │             首批裁减清单 (First Cuts — 应急压缩预案)           │
     │         (当总学时 < 56h 时，最先按顺序砍掉的内容: 见 10.3)     │
     └─────────────────────────────────────────────────────────────┘
```

### 10.1 基础教学栈 (Base Stack — 最小可行核心)
- **规划容量**：56–72 实际人时（4 课时面授 + 4–6 课时作业/周）；
- **核心构成**：
  - **14 个 Teaching Primitives (TP-01 ~ TP-14)**；
  - **10 个必须亲手动手的实操体验 (HO-01 ~ HO-10)**；
  - **核心软件宿主**：Substance 3D Painter (贴图与图层) + Blender (节点与双目标渲染验证) + Substance 3D Sampler (AI/图像精修)；
  - **开放标准定位**：OpenPBR 语义实操内嵌，MaterialX / UsdShade 为概念与演示。

### 10.2 弹性扩展栈 (Capacity-sensitive Extensions)
只有在实际面授课时更充裕（如校方安排 6–8 课时/周）或学生具备熟练 3D 软件前置基础时，才考虑选修扩展的内容：
1. **Extension 1: Substance 3D Designer 独立节点子图实操**：从纯演示升级为学生亲手连接一个小型程序化砖石/金属材质图；
2. **Extension 2: Unreal Engine 5 Substrate / 进阶母材质深度接入**：将实时目标从轻量视口升级为在 UE5 中亲手搭建包含多层材质混合与性能分析的 Shader Graph；
3. **Extension 3: 实物偏振十字正交摄影与多角度采集 (Photometric Stereo)**：引入实物测色卡与偏振光源进行物理级高精度真实采集。

### 10.3 首批裁减清单 (First Cuts — 应急压缩预案)
如果教务最终批复课时显著低于当前 56 小时规划情境（例如压缩至 32–40 小时），**最先被裁减的 3 项内容清单**：
- **First Cut 1：裁减 TP-11 中的“AI 图像转材质通道精修与去光照”实操**：
  - *裁减方案*：将 HO-08 动手实操降为教师演示（DEMO ONLY），完全由教师提供精修完毕的现成素材贴图，节省 8–10 课时。
- **First Cut 2：裁减 TP-09 中的“平铺打散与参数化变体接口暴露”独立实操**：
  - *裁减方案*：LO4 的 Blender 节点实操仅保留 TP-08（基础节点连接与数值映射），将 Node Group 封装与参数对外暴露改为教师提供模板直接拉动滑块，节省 6–8 课时。
- **First Cut 3：裁减 TP-13 中的“跨环境离线渲染 (Cycles) 对比调校”实操**：
  - *裁减方案*：放弃双环境对比实操，全课程交付与 LookDev 仅锁定在单一视口（如 EEVEE Next 实时视口），离线渲染差异仅作口头讲授，节省 4–6 课时。

---

## 11. Gate 3B 核心裁决结论总表 (Gate 3B Decision Findings)

针对 Gate 3B 的 13 项关键决策问题，提供明确的确定性答案：

1. **最小 Teaching Primitive 集合是什么？**  
   $\to$ 共有 **14 个 Teaching Primitives (TP-01 ~ TP-14)**，完整覆盖 LO1–LO6，无冗余工具菜单。
2. **哪些必须学生亲手做？**  
   $\to$ 共有 **10 个不可替代的亲手实操体验 (HO-01 ~ HO-10)**，涵盖情绪板解构、光照旋转审查、色彩空间排错、图层栈搭建、局部受控修订、紧凑节点连接、参数接口暴露、图像去光照精修、目标通道打包、以及跨环境质感调校。
3. **哪些只需识别解释？**  
   $\to$ 多范式权衡决策（TP-10）、开放材质标准语义与机器可维护性概念（TP-14）。
4. **哪些应该 teacher demo / infrastructure only？**  
   $\to$ Substance 3D Designer 宏图表生成演示、生成式 AI 文生贴图前沿演示、MaterialX XML 源码与 ShaderGen、UsdShade C++/Python API 绑定、复杂高低模拓扑与手动展开 UV、底层着色器性能汇编调优。
5. **Painter 的最小且不可替代角色是什么？**  
   $\to$ **LO3（资产级三维多通道分层创作与受控局部修订）的唯一核心承载宿主**；其余 UV 展开、手绘涂抹与贴图打包导出均被压缩或自动化。
6. **程序化主宿主推荐是什么？**  
   $\to$ **Blender Shader Nodes**。以最低认知切换成本达成 LO4，直通通用着色器逻辑。
7. **Designer 如果不是主宿主，还剩什么角色？**  
   $\to$ **教师演示与工业标准概念参考 (`TEACHER DEMONSTRATION` / `RECOGNIZE & EXPLAIN`)**。学生显式无需独立掌握其软件操作。
8. **Blender 的最小角色是什么？**  
   $\to$ 承担 **LO4 节点逻辑实操**、**LO2 物理因果与色彩空间纠偏**、以及 **LO6 实时与离线双渲染环境对比验证** 的多功能通用底座。
9. **Sampler / AI 工具最低实践深度是什么？**  
   $\to$ **“通道级多维质量验证与去光照精修”**。学生只需通过 Sampler 或轻量滤镜亲手完成一次单图转换、去光照与通道查验，不进行庞大 AI 工具链的横向学习。
10. **Primary target / Secondary comparison target 推荐是什么？**  
    $\to$ **Primary Target** 为**轻量实时交互视口 (Blender EEVEE Next 或 轻量 UE5 模板工程)**；**Secondary Target** 为**离线渲染环境 (Blender Cycles 对照组)**。
11. **OpenPBR / MaterialX / UsdShade 各自学生深度是什么？**  
    $\to$ OpenPBR 为 `RECOGNIZE & EXPLAIN`（理解物理参数语义）；MaterialX 为 `RECOGNIZE & EXPLAIN` / `TEACHER DEMONSTRATION`（理解结构化图拓扑）；UsdShade 为 `INFRASTRUCTURE / TEACHER REFERENCE`（理解场景绑定逻辑）。**学生全过程无需亲手编写代码**。
12. **如果实际课时不足，前三个 First Cuts 是什么？**  
    $\to$ ① 裁减图像转材质与去光照实操（改演示）；② 裁减程序化节点变体参数暴露实操（改套模板）；③ 裁减跨环境离线渲染对比调校实操（锁定单一视口）。
13. **有无真正需要 User 决策的方向问题？**  
    $\to$ **`NONE`**。全部技术选型与教学深度均已在严谨的教学成效与学时约束下形成收敛闭环。

---

## 12. 后置 Gate 3C 任务可行性待决事项 (Unresolved Decisions for Gate 3C)

以下微观任务细节属于 Gate 3C（代表性任务可行性验证）的事项，不在 Gate 3B 提前预设：
- `[TASK FEASIBILITY 01]`：Gate 3C 选用的具体代表性资产道具题材（如工业机械旧件、科幻道具或自然地表标本）及其预制低模的多边形面数与贴图分辨率；
- `[TASK FEASIBILITY 02]`：在代表性任务中用于检验“受控局部版本修订”的具体修改意见单（Art Direction Brief）设计；
- `[TASK FEASIBILITY 03]`：跨环境验证时所采用的标准 HDR 环境光（如 1 个强直射日光室外 HDR + 1 个室内均匀漫射光 HDR）的具体文件资产配置。

---
*本文档生成并归档于 `docs/research/minimal-teaching-stack.md`，作为 Gate 3B 规范交付基线。*
