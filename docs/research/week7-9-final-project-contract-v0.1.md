# W7–W9 期末大作业契约与里程碑拓扑草案 (Final Project Contract & Milestone Topology Draft v0.1)

> **工单与状态声明 (Issue #22 Phase B Deliverable)**：  
> 本报告为 **Issue #22（期末大作业设计）阶段 B 的核心设计工件**。  
> 
> * **证据纪律约束 (Curriculum Evidence Discipline)**：严格遵循 `AGENTS.md` 课程证据纪律，所有承重主张在三个正交维度上明确标定（依据溯源：`[SOURCE-BACKED]`、`[PROJECT INFERENCE]`、`[UNKNOWN / RESEARCH REQUIRED]`；运行时有效性：`[VERIFIED]`、`[RUNTIME REQUIRED]`；人类与项目权威：`[TEACHER ACCEPTED]`、`[PROPOSED / NOT YET TEACHER ACCEPTED]`、`[CONDITIONAL]`），严禁无凭据写成事实；  
> * **宏观边界锁定 (Macro Boundary)**：**W1–W6 为能力构建阶段（有限主案例 Flashlight + 微案例），W7–W9 为全新独立综合期末大作业（严禁复用 Flashlight 练习模型）**；  
> * **载体无关与非目标恪守**：本设计基于**载体无关 (Carrier-independent)** 原则，通用框架完全解耦于具体资产。秦陵兵马俑仅作为当前**首选候选载体 (PREFERRED CARRIER CANDIDATE - NOT FROZEN)**，受 `[GATE-ASSET-03]` 约束；  
> * **决策权限边界 (Standing Gate)**：**本文件不冻结兵马俑为法定模型、不冻结最终成绩评分权重、不拟定学生任务书、不生成教学周历 v0.4、不合并分支**。成果止步于 Course Owner / Browser 评审门禁。

---

## 1. 已接受的期末大作业架构基准 (Accepted Architecture) `[TEACHER ACCEPTED]` `[PROJECT INFERENCE]`

基于 Issue #22 阶段 A（事实核验与前序审计）的审定结论，本课程期末大作业（Weeks 7–9）确立并锁定以下五大核心架构原则：

1. **统一预制主体资产与几何基准 (Common Prepared Hero Asset & Geometry Baseline) `[TEACHER ACCEPTED]`**：
   - 彻底剥离三维建模与复杂拓扑任务。全班统一下发同一套由教师预制、经过严格规范检验的中多边形白模；
   - 消解因学生建模技术参差导致的评分污染，使评估标尺聚焦于材质创作与着色表现本体；
   - *具体工程参数*（标准流形、UV 展开无拉伸无重叠、Material ID 贴图、预烘焙 AO/Curvature 图集等）定位于候选验收目标 `[PROPOSED] [RUNTIME REQUIRED]`，待资产实测闭环，不作为预设已批准的既成事实。
2. **个体独立材质重释 (Individual Material Reinterpretation) `[TEACHER ACCEPTED]`**：
   - 在统一几何形体约束下，要求学生自主选择不同的物质文明、工业时代或艺术假说主题（如风化青铜、仿生陶瓷机甲、残损玉石琉璃、工业特种涂装等），对载体进行微观物理材质的深度重构与叙事性重释，破除视觉同质化。
3. **统一最低材质物理行为契约框架 (Common Minimum Material-Behavior Floor Architecture) `[TEACHER ACCEPTED]`**：
   - 不以主观审美或单一贴图数量论成败，而是建立全班统一的“物理行为及格底线架构”（包含微观粗糙度层次、表面细节法线、环境自适应性等），防范“仅换底色”的应付式作品；具体条款保持为 `[PROPOSED / NOT YET TEACHER ACCEPTED]`。
4. **个体独立考核绝对为主，班级装置汇聚为次且条件性 (Individual Grading Primary, Cohort Secondary/Conditional) `[TEACHER ACCEPTED]`**：
   - 学生的学分与期末成绩评定完全基于个人独立完成的工件（工程、渲染静帧、说明报告）；
   - 班级群像军阵（Cohort Installation / Web 3D 展厅）定位于教学成果展示与文化冲击力呈现，其技术实现与学生个人成绩在架构上彻底解耦，汇聚成败绝不波及个人评分。
5. **兵马俑载体定位与平替兜底原则 (Preferred Candidate with Seamless Fallback) `[TEACHER ACCEPTED]`**：
   - 秦陵兵马俑白模为当前首选候选载体（PREFERRED CARRIER CANDIDATE），但受制于资产合规与制作门禁 `[GATE-ASSET-03]`；
   - 若兵马俑通过门禁，则载入该模型；若门禁失败，完整保留本文确立的 W7–W9 教学结构与契约，仅平替为另一套合规的通用预制载体（如复古精密工业道具）。

---

## 2. 期末项目学生任务目标与考察能力 (Student Project Purpose) `[PROJECT INFERENCE]` `[SOURCE-BACKED]`

### 2.1 任务核心使命
在 3 周（总计 12 课节 / 480 分钟面授学时）内，面向一套全新的标准化预制白模，学生综合调动 W1–W6 积累的光学物理知识、着色器节点网络搭建、微观粗糙度刻画、法线微起伏雕琢与局部受控遮罩技术，完成该物体的全套 PBR 材质外观开发（LookDev），并自证其在多重光照环境下的物理一致性与鲁棒性。

### 2.2 核心检验能力 (Assessed Capabilities) `[SOURCE-BACKED]`
对齐行业权威规范与艺术质感经典方法论：
1. **物理因果解构能力 (Material Causality)**：能够识别物体在真实世界中的材质分层逻辑（基底 Substrate $\to$ 表面涂层 Coating $\to$ 岁月磨损 Edgewear $\to$ 环境沉积 Grime/Dust），避免无依据的纯数学噪波堆砌（依据：Dinur 2026 Ch 3 pp. 32–48 & Ch 13 pp. 143–156；OpenPBR Surface Spec v1.1.1 `Base Substrate` & `Coat`）；
2. **微表面光学控制能力 (Microfacet Shading Control)**：精确驾驭微观粗糙度（Roughness）的空间演变与反射高光聚焦度，严格区分导体（金属有色高光）与介电质（菲涅尔约 4% 高光）的底层差异（依据：Adobe PBR Guide 2018 Pt 1 pp. 24–37 & Pt 2 pp. 47–63）；
3. **着色欺骗与法线表现力 (Normal / Relief Articulation)**：掌握切线空间法线贴图与微观凹凸逻辑，实现“平整网格上的宏观立体光影流动”（依据：Khronos glTF 2.0 §3.9.3；Adobe Pt 2 pp. 78–79）；
4. **外观开发多环境自证能力 (LookDev Neutral Validation)**：能够在至少 2 套对比环境（中性演播室光 vs 复杂漫射光）下调试材质，保证材质能量守恒、不漏光、不高光崩塌（依据：Dinur 2026 Ch 11 pp. 113–130）。

### 2.3 明确剥离的非目标 (Explicit Non-Goals)
- ❌ **不考察网格建模与雕刻**（严禁现场要求学生建中高模）；
- ❌ **不考察拓扑布线与减面技巧**；
- ❌ **不考察 UV 缝合线剪切与打包算法**（UV 由教师标准预置）；
- ❌ **不要求全套骨骼绑定或复杂角色蒙皮动画**。

---

## 3. 载体无关型学生任务定义 (Carrier-Independent Task Definition) `[PROJECT INFERENCE]`

为确保教学设计的稳健性与通用性，无论期末载体最终采用秦陵兵马俑、复古机械道具还是文化雕塑，学生端任务书的核心框架严格保持一致：

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        Carrier-Independent Capstone Brief Structure                    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. 统一几何白模包 (.blend) ── 包含规范网格、无重叠 UV、材质槽位与预置烘焙 ID 贴图       │
│ 2. 材质重构主题自选 ────── 在材料系统分类（金属机械/矿物陶瓷/风化有机/科幻异质）中自选 │
│ 3. 物理分层着色开发 ────── 依据 Material-Behavior Floor 搭建节点与受控纹理             │
│ 4. LookDev 标定质检 ─────── 导入官方统一演播室场景，验证中性与对比光照反射一致性       │
│ 5. 三件套规范化交付 ─────── 提交源工程 (.blend)、规定三视角静帧渲染图、材质标定报告    │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. 候选最低材质行为契约 (Proposed Material-Behavior Contract) `[PROPOSED / NOT YET TEACHER ACCEPTED]` `[PROJECT INFERENCE]`

> **决策状态说明 (Review Standing)**：  
> 本契约属于 **项目教学法候选提案 (PROPOSED / NOT YET TEACHER ACCEPTED)**。旨在替代过去“必须做 3 个材质球”或“必须有金属和铁锈”的机械考核，建立面向物理本质的科学标尺。

为解决历史教学中容易出现的“只改底色不调质感”、“全局使用单一粗糙度”以及“全介电质题材（如纯陶瓷/白玉）被强制做旧/生锈的不公平现象”，本契约采用 **CORE（核心及格底线）/ CONDITIONAL（题材条件项）/ STRETCH（进阶拔高项）** 三层架构：

### 4.1 核心及格底线 (CORE Floor — 候选全员及格底线，缺一不可)
凡期末作品，不论任何题材，建议必须同时满足以下 5 项核心物理行为契约：
1. **$\ge 2$ 个物理分异明显的行为区域 (Behavior Zones)**：全表面必须清晰划分出至少两个物理光学属性具有本质区别的材质区域（例如：抛光面 vs 磨砂面、施釉层 vs 泥胎裸露、硬质外壳 vs 软质衬垫等）；
2. **有意义的粗糙度微对比 (Meaningful Roughness Differentiation)**：粗糙度通道必须具有明确的空间微观变化与对比层次，**绝对禁止全模型使用全局单一恒定 Roughness 数值**，高光反射必须展现微瑕疵或受控漫散；
3. **表面微结构/起伏证据 (Surface Detail / Normal / Height Evidence where appropriate)**：在合理表面必须呈现切线空间法线（Normal）或微凹凸（Bump）细节（如铸造砂眼、织物编织纹、划痕凹痕或釉面开片），法线贴图切线空间与色彩空间（Non-Color）必须标定正确；
4. **$\ge 1$ 处受控局部微观变化 (Localized / Non-uniform Controlled Variation)**：表面必须具有至少一处**与题材概念相符 (Concept-appropriate)** 的受控非均匀变化（如涂层光泽差异、釉面渐变、抚摸抛光过渡、局部受控遮罩；风化磨损仅在题材合理时采用），杜绝无脑均匀噪波平铺；
5. **多环境 LookDev 标定自证与基底合规 (LookDev Validation & Albedo Compliance)**：
   - 材质在标准中性演播室光与对比环境光下均展现守恒物理反射，无自发光式过曝、无环境反射穿透漏光；
   - Base Color 严禁手绘素描阴影、全局环境闭塞或烘焙环境光；反照率明度必须在自然界物理合理区间内（排除纯黑 0 与过曝 255）。

### 4.2 题材条件性要求 (CONDITIONAL Rules — 依据题材自适应)
根据学生自选题材，自动匹配对应物理法则，杜绝机械化套用：
* **若涉及金属/导电体题材 (Conductor Rules)**：
  - 严格遵守金属度二元语义（Metallic 理论上非 0 即 1，仅允许抗锯齿边缘与微米级氧化过渡带存在中间过渡）；
  - 金属 Base Color 必须承载其镜面高光颜色（有色反射率）；
  - 若表现磨损露底，必须呈现“面漆绝缘体（Metallic 0）$\to$ 底材导电体（Metallic 1）”的物理跃迁，并伴随粗糙度跳变。
* **若选择全介电质题材 (Dielectric / Non-metal Rules — 如全陶、玉石、布塑、洁净工业品)**：
  - **享有免除金属度与风化锈蚀考核的完全公平性**；
  - 重点考核其介电质表面状态的分异（例如：釉层玻璃质感 $F_0 \approx 0.04$ 与开片纹理、石材质感孔隙法线、织物微纤维散射或清漆涂层 Coat 的分层叠加）。

### 4.3 进阶拔高探索项 (STRETCH Features — 优秀档引导，非全员强制)
面向学有余力的学生提供探索通道，不设及格硬性门槛，不增加基础考核焦虑：
* **高阶物理光学扩展**：清漆涂层 (Clearcoat)、次表面散射 (SSS 局部)、各向异性 (Anisotropy)、薄膜干涉 (Thin-Film)；
* **复杂服役叙事 (Multi-stage Aging)**：呈现 3 层以上物理因果嵌套（底材 $\to$ 氧化锈斑 $\to$ 底漆 $\to$ 面漆剥落 $\to$ 浮土覆盖）。

---

## 5. Week 7 里程碑：启动、材质解构与初版搭建 (W7 Milestone) `[PROJECT INFERENCE]` `[PROPOSED / NOT YET TEACHER ACCEPTED]`

- **课内接触预算**：第 7 周单次课 160 分钟（以里程碑达成度为准，不设机械分钟切片）。
- **Entry State (入场状态)**：
  - 教师下发期末候选工程包（白模 `.blend`、展开 UV、Material ID 贴图、Curvature/AO 预置烘焙图，规格保持 `[PROPOSED] [RUNTIME REQUIRED]`）；
  - 学生已掌握 W1–W6 材质基础理论与节点网络搭建基础。
- **Student Goal (学生目标)**：
  - 确立个人材质重释方向，收集并整理真实材质参考板（Moodboard）；
  - 完成材质行为解构草案（明确划分至少 2 个计划制作的物理区域）；
  - 在 Blender 中成功加载白模，建立材质槽，完成初版粗胚搭建（First-Pass Blocking：赋予各区域基础 Base Color、Metallic 与粗糙度大关系）。
- **Required Evidence (本周物证)**：
  1. **材质规划与参考板 (Material Plan & Moodboard)**：至少包含 3 张高清物理材质参考图，用文字明确标注至少 2 个计划制作的物理行为区域及其材质类型；
  2. **第一阶段工程切片 (.blend 或视口无遮挡截图)**：证明模型已正确就绪，材质槽已分配，模型已摆脱默认灰色，完成基础分区分色。
- **Checkpoint W7 (检查点 1)**：
  - 准出标准：是否有明确参考？工程是否跑通？是否已进入 Blocking 状态？
- **Teacher Feedback (教师反馈方式)**：
  - 课前集中讲评：剖析优秀与违规参考图案例，强调光影剥离；
  - 课中流动巡检：快速走访，排查模型加载与材质槽分配问题；
  - 课末投屏纠偏：展示典型 Blocking 进展，及早纠偏纯手绘阴影苗头。
- **Recovery Path (脱轨挽救)**：
  - 详见第 9 节挽救阶梯 Level 1（选题卡壳者分发标准预设参考卡，跳过犹豫期）。
- **Exit State (出场状态)**：
  - 目标状态为全体学生锁定材质方向，工程具备有效着色器底座，降低历史前期拖延风险。

---

## 6. Week 8 里程碑：材质深化、迭代与形成性讲评 (W8 Milestone) `[PROJECT INFERENCE]` `[PROPOSED / NOT YET TEACHER ACCEPTED]`

- **课内接触预算**：第 8 周单次课 160 分钟。
- **Entry State (入场状态)**：
  - 模型已有基础材质分区；学生手握明确材质参考。
- **Student Goal (学生目标)**：
  - 刻画微观粗糙度空间变异（引入微孔隙、光洁度差异或合理划痕）；
  - 接入表面微起伏与切线法线细节；
  - 引入至少一处**与题材概念相符 (Concept-appropriate)** 的受控非均匀变化（如釉层变化、涂层过渡、抚摸高光、或题材合理的边缘剥落/积灰，不强制全员做旧）；
  - 修正所有违反物理规律的“幽灵材质”与贴图通道错误。
- **Required Evidence (本周物证)**：
  1. **W8 中期工程文件 (.blend 存盘)**；
  2. **双环境视口对比截图 (Mid-Project LookDev Staging)**：在标准光与侧光下的无修图视口截图；
  3. **已签字的红线双人互查表 (Peer & Self Redline Form)**。
- **Checkpoint W8 (MID-PROJECT GATE 中期门禁)**：
  - 准出红线：**“非单色、具微观、有法线、无手绘光影”**；
  - 凡此时仍处于“全局单一粗糙度”、“仅有一张扁平 Base Color”或工程崩溃无法渲染者，标记为 `MID-PROJECT DEFECT`，触发重点关注与辅导。
- **Teacher Feedback (教师反馈方式)**：
  - 激活第 8 节详述的四级反馈漏斗（广播 $\to$ 互查 $\to$ 巡回 $\to$ 聚焦）。
- **Recovery Path (脱轨挽救)**：
  - 详见第 9 节挽救阶梯 Level 2（着色网络崩溃者提供防呆节点组，收缩至保底线）。
- **Exit State (出场状态)**：
  - 核心物理行为在模型上清晰具象化，材质达到及格线要求，留待最终演播室渲染与文档整理。

---

## 7. Week 9 里程碑：打磨、演播室标定与终期交付 (W9 Milestone) `[PROJECT INFERENCE]` `[PROPOSED / NOT YET TEACHER ACCEPTED]`

- **课内接触预算**：第 9 周单次课 160 分钟。
- **Entry State (入场状态)**：
  - 材质主要行为已基本成型，通过 W8 中期门禁。
- **Student Goal (学生目标)**：
  - 解决材质接缝拉伸与微观噪波瑕疵；
  - 将模型置入官方统一 LookDev 演播室场景，在 3 点光与 2 套对比 HDRI 下完成光影标定；
  - 渲染规定三视角的离线静帧效果图；
  - 撰写 1–2 页《材质行为与 LookDev 标定报告》；
  - 规范命名并打包归档工程。
- **Required Evidence (本周物证)**：
  - 提交期末三件套候选工件（源工程、三视角渲染图、材质标定报告，详见第 10 节）。
- **Checkpoint W9 (FINAL EXIT GATE 终验门禁)**：
  - 终验验收，核验交付物完备性与契约达成度。
- **Teacher Feedback (教师反馈方式)**：
  - 课内流动答疑，排查打包丢贴图、渲染器报错与文档格式问题。
- **Recovery Path (脱轨挽救)**：
  - 详见第 9 节挽救阶梯 Level 3（针对极端脱轨学生开启 Minimum Assessable Submission 通道）。
- **Exit State (出场状态)**：
  - 个人终验交付物提交至教务作业平台；
  - （条件性可选）导出标准轻量资产，移交班级汇聚池。

---

## 8. 单师大班反馈漏斗机制 (Large-Class Feedback Funnel) `[PROJECT INFERENCE]` `[PROPOSED / NOT YET TEACHER ACCEPTED]`

> **依据溯源说明 `[SOURCE-BACKED]` 与缺口定位 `[GAP-W08-FEED]`**：  
> - 广州软件学院真实教学容量为单师面对 35 人班（GR2102-1）及 17 人班（GR2102-3），单班课内仅 160 分钟（依据：`course-offering-impact-analysis-2026-2027-1.md` §3；历史教研档案考查分析报告记录两班合计 101 人，单师指导负荷极重）；  
> - Evidence Map 中 **`[GAP-W08-FEED]` 仍属于 OPEN 状态的教学法与评估缺口**。本漏斗机制属于**项目教学法候选设计方案 `[PROJECT INFERENCE] [PROPOSED]`**，不伪装为已验证事实，删除未经验证的吞吐率量化承诺（如“过滤 70%”、“覆盖 100%”等）。

若采用“学生排队、教师逐个 1:1 面对面修改”模式，每人平均不足 4.5 分钟，容易引发大面积等待与进度失控。本方案提出旨在缓解单师排队压力的**四级反馈漏斗 (Four-Tier Feedback Funnel)**：

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              Four-Tier Feedback Funnel                                 │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Level 1: 全班共性缺陷投屏讲评 (Cohort Defect Broadcast) ──────── 面向全班统一广播       │
│          课前集中排查共性高频报错：贴图未保存、法线色彩空间错误、纯黑粗糙度            │
│                                                                                        │
│ Level 2: 结构化红线双人互查 (Peer Redline Cross-Check) ──────── 同伴对照排查           │
│          同桌依据一纸化 Checklist 逐项核验并签名，及早发现基础通道配置疏漏             │
│                                                                                        │
│ Level 3: 教师巡回靶向干预 (Teacher Roaming Targeted Spot-Check) ───────────────────────│
│          跳过互查无异常学生，重点针对互查暴露的“疑难排障点”进行窄干预                  │
│                                                                                        │
│ Level 4: 典型范式投屏点睛 (Exemplar Spotlight) ──────────────── 提炼优秀，指引拔高方向 │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

> **特别声明**：本反馈漏斗属于**形成性过程辅导支架 (Formative Scaffolding)**，互查结果不设正式百分比评分权重，不记入学生正式成绩，仅作为推进课堂教学排障工具。

---

## 9. 历史失败规避阶梯与最低可评价提交 (Historical Failure Recovery Ladder) `[PROJECT INFERENCE]` `[SOURCE-BACKED]`

### 9.1 历史事实教训核实 `[SOURCE-BACKED]` 与因果定界 `[PROJECT INFERENCE]`
广州软件学院（GZUS）《三维数字材质制作》（GR2102，101 人）官方考核分析报告（物证哈希：`38d5b29fb50c32a69bc8df14c836c9c82fa2a6498d102d73b3019b9d9d7db309`）确凿证明：  
* 课程不及格 11 人（低分率占 20.4%–31.6%），原文断定：**“不及格者皆因未提交大作业，成绩归零，并非能力不及”**；
* **历史多重因果事实 `[SOURCE-BACKED]`**：历史考核分析报告复盘指出，作业弃交是多重复合因素导致的系统性问题，包括学生自选模型与准备消耗、Substance 软件操作与贴图复杂度、烘焙渲染耗时、终结式考核缺乏阶段过程预警、部分学生误以为平时成绩可兜底、以及时间规划失当引发的后期畏难弃交；
* **设计推论定界 `[PROJECT INFERENCE]`**：采用“统一预制白模”剥离建模负担，可能有助于减少模型准备失控与前期拖延风险，属于合理的项目教学推论，但不可将历史弃交归因于单一变量。

### 9.2 四级脱轨挽救阶梯 (The Recovery Ladder)
针对历史拖延与畏难弃交风险，建立具有明确防线的过程挽救阶梯：

* **Level 0 (正常推进通道)**：按 W7 Blocking $\to$ W8 Deepening $\to$ W9 Polish 稳步推进。
* **Level 1 (W7 启动卡壳挽救)**：
  - *触发条件*：W7 结束时未能确定材质参考或模型槽位混乱；
  - *挽救动作*：教师分发“3 套标准参考配方（青铜器、施釉彩陶、特种铸铁）”，学生一键认领起步，跳过选型犹豫期。
* **Level 2 (W8 制作畏难挽救)**：
  - *触发条件*：W8 中期门禁未通过、着色网络崩溃或停留于单色平涂；
  - *挽救动作*：触发过程学业预警，教师提供“防呆着色节点子网络组 (Failsafe PBR Node Groups)”，将任务收缩至保底线，协助搭通 2 个区域的物理反射。
* **Level 3 (W9 濒临弃交挽救 - Minimum Assessable Submission, MAS)**：
  - *触发条件*：临近截止仍无法输出复杂贴图或面临弃考风险；
  - *挽救动作*：开启最低可评价提交通道，见下文详述。

### 9.3 最低可评价提交通道 (Minimum Assessable Submission - MAS / Recovery Submission) `[PROJECT INFERENCE]` `[PROPOSED / NOT YET TEACHER ACCEPTED]`
针对 W9 出现严重制作障碍或重度心理畏难的学生，设立 **MAS 极简保底交付通道**：
* **MAS 核心定位与目的**：
  - **核心目的**：避免因完不成复杂效果而直接放弃提交（Non-submission / Zero-by-abandonment），使严重落后学生仍有一份包含核心学习证据的工件可供教师正式评定；
  - **成绩定界规范**：**MAS 绝不自动保证及格（Does NOT guarantee a passing grade）**！期末最终成绩严格依据后续冻结的正式评分量表（Adopted Rubric）、学校官方考核政策（`[GATE-ADMIN-02]`）以及学生实际展现的有效学习证据独立裁定。删除任何“自动及格”或“直接达到 passing baseline”的承诺。
* **MAS 候选交付物规格**：
  1. 源工程 `.blend`：在预制白模上至少实现 2 个不同区域的基础 Principled BSDF 分区（具有清晰 Base Color 与 Roughness 差异）；
  2. 1 张正面 Blender 视口 LookDev 渲染截图（无黑斑、无穿透）；
  3. 1 份不少于 100 字的简要说明，正确陈述这两个区域为什么分别属于导体或绝缘体、其粗糙度设定的物理依据。

---

## 10. 候选交付物架构分层 (Proposed Deliverables Architecture) `[PROJECT INFERENCE]` `[PROPOSED / NOT YET TEACHER ACCEPTED]`

明确区分“证明课程核心学习成果（LO）的法定证据”与“次级展示性附加物”，消除学生无效负担：

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                             Deliverables Architecture                                  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ PROPOSED CORE (候选法定必交，建议作为个人独立成绩评定基准，待裁决)                     │
│  ├── 1. 打包源工程 (.blend) ─── 包含独立命名着色器、贴图 Pack 完整、无粉色丢失        │
│  ├── 2. 规定三视角静帧渲染 ── 正面、四分之三侧面、局部微距特写 (统一 LookDev 演播室) │
│  └── 3. 材质行为与标定报告 ── 1–2 页 PDF，含参考对比、物理参数表与两环境自检截图      │
│                                                                                        │
│ CONDITIONAL (条件性交付，受技术门禁或自选管线约束)                                    │
│  ├── 4. 独立导出的 PBR 贴图包 ─ 仅在选择外部贴图管线时提交 (BC, R, M, N, AO)           │
│  └── 5. 实时查看器 glTF/GLB ── 严格受 [GATE-RT-01] 约束，未通过门禁绝不设为必交        │
│                                                                                        │
│ STRETCH (可选拓展与卓越证据 Optional Extension / Excellence Evidence，非全员要求)     │
│  ├── 6. 360 度转台旋转短视频 ── 5–10 秒 Cycles/EEVEE 动画                              │
│  └── 7. 班级军阵汇聚资产 ───── 按规范导出的标准化轻量资产，完全不影响个人独立成绩     │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

> **绝对隔离纪律 (Decoupling Invariant) `[TEACHER ACCEPTED]`**：  
> **班级军阵汇聚绝不作为个人独立评分的前置条件**。哪怕自动化组装脚本崩溃、哪怕某位学生未提交汇聚资产，只要其个人候选 CORE 工件完备，个人期末成绩评定照常进行，彻底隔离系统性风险。  
> **评分权重声明**：STRETCH 交付物不作预设“加分项”承诺，评分规则与权重严格受制于 `[GATE-ADMIN-02]`。

---

## 11. 兵马俑特定叠加层与候选资产就绪要求 (Terracotta Specific Overlay) `[PROJECT INFERENCE]` `[CONDITIONAL]`

本节阐述若秦陵兵马俑最终通过 `[GATE-ASSET-03]` 成为法定载体时的具体工程与教学规范：

### 11.1 白模工程规范候选验收指标 (Candidate Asset Targets) `[PROPOSED]` `[RUNTIME REQUIRED]`
1. **几何面数与拓扑**：候选控制在 **1.5 万–3.5 万三角面** 之间（兼顾 35 人机房老旧显卡的实时着色视口流畅度，且保留甲片与头部的结构轮廓，须通过机房带载验证）；
2. **切线法线底模 (Pre-baked Base Normal)**：由高精度雕刻扫描件烘焙出基础微观起伏（发髻线条、甲片重叠光影），作为基础 Normal 预置在工程中；
3. **UV 象限规范**：展开于单张 0–1 象限，UV 缝合线隐藏于内侧袍服，展开率候选目标 $\ge 75\%$，无拉伸变色；
4. **预置辅助贴图集 (Pre-baked Maps)**：教师端发布工程建议内置全套 2K 贴图：
   - `Curvature Map`（曲率图，用于边缘快速识别）；
   - `Ambient Occlusion Map`（环境光遮蔽图，用于内凹缝隙积灰）；
   - `Material ID Mask`（顶点色或分色贴图，清晰界定战甲片、甲带钉扣、面部肌肉、发髻、袍服布料、靴履六大部位）。
5. **运行时隔离原则**：
   - **学生个人资产运行时要求**：必须在机房 PC 单机实现流畅着色编辑与渲染；
   - **班级 35/52 人阵列汇聚运行时要求**：属于展示性扩展，其性能压力由汇聚脚本与展示主机承担，**绝不反向成为学生个人 carrier gate 的必要门禁**。

### 11.2 教学承载天然优势与重释方向
* **高度契合 M1–M8 材质矩阵**：陶俑天然具备“泥胎陶土（哑光介电质 M1）”、“残存矿物颜料彩绘（涂层剥落 M5）”、“氧化出土（风化 M6）”与“地宫淤积（积灰 M7）”的真实历史属性；
* **宽广的重释空间**：
  - 传统重释：战国青铜古兵、唐三彩琉璃俑、风化残损汉白玉俑；
  - 现代与先锋重释：仿生镀铬赛博机甲俑、现代波普搪胶艺术俑、特种防腐涂料工业俑。

### 11.3 教学负荷防呆规避
* **避免学生手动抠图描边甲片**：兵马俑甲片繁密，若无高质量 Material ID，学生课内时间易被机械选区耗尽，因此建议预置 ID；
* **防范退化为“脸谱涂鸦贴纸”**：建议通过行为契约，引导面部花纹具备物理涂层厚度（Normal/Bump 微起伏）与粗糙度差异。

### 11.4 门禁阻断与平替触发 (`[GATE-ASSET-03]`)
* 兵马俑方案的推进严格受制于：
  - 版权合规审查（确认开源许可或公有领域无排他性商用/学术限制）；
  - 教师制作成本实测（低模拓扑与贴图烘焙必须可控）；
  - 机房运行时带载实测（单机编辑视口流畅不崩溃）。
* 若上述任何一项不满足，**平替为其他已验证的 CC0 复杂中型工业道具**（如 Vintage Cash Register 或类似复古机械），本文件除第 11 节外，其余通用章节保持适用。

---

## 12. 待课程负责人裁决事项 (Open Course Owner Decisions) `[UNRESOLVED DECISIONS FOR COURSE OWNER]`

请 Course Owner 审阅本设计，并针对以下 4 项核心决策进行裁决：

1. **里程碑拓扑架构裁决**：
   - 是否批准采纳 **W7 (Kickoff & Blocking) $\to$ W8 (Deepening & Mid-Gate) $\to$ W9 (LookDev & Delivery)** 的三周里程碑拓扑？
2. **最低材质物理行为契约裁决**：
   - 是否批准将 **CORE（2 区域、粗糙度微对比、表面法线、概念自洽的局部非均匀变化、多环境自证）** 作为期末考核及格底线框架，并批准全介电质题材享有免除金属度与风化锈蚀考核的完全公平性？
3. **交付物分层与解耦裁决**：
   - 是否批准将 **CORE 三件套候选工件（工程、三静帧、标定报告）** 作为个人独立考核基准，并永久将“班级军阵汇聚”定位于次级条件性呈现、彻底与个人评分脱钩？
4. **历史失败挽救机制裁决**：
   - 是否批准在大班中推行**四级反馈漏斗**，并设立 **Minimum Assessable Submission (MAS) 最低可评价提交通道**（不承诺自动及格，仅确保有作业可供正式评价以规避弃考归零）？

---

## 13. 运行时与资产门禁对照表 (Runtime & Asset Gates)

| 门禁标识 | 门禁描述 | 当前状态 | 阻断范围与影响 |
| :--- | :--- | :---: | :--- |
| **`[GATE-ASSET-03]`** | 秦陵兵马俑白模资产就绪性、拓扑规范、辅助贴图烘焙与版权合规核验 | `OPEN / CONDITIONAL` | 仅阻断兵马俑作为法定 carrier 的最终冻结；不阻断本契约与里程碑拓扑；FAIL 则自动平替载体。 |
| **`[GATE-RT-01]`** | 离线机房 WebGL/glTF 实时查看器端到端兼容性与显卡性能 | `OPEN / CONDITIONAL` | 阻断将 glTF/Web 实时交互设为 mandatory 交付物；未通过前以 Blender 原生视口/渲染为唯一基准。 |
| **`[GATE-ADMIN-02]`** | 广州软件学院考查课总评与期末各项官方评分比例红头文件 | `PENDING INSTITUTIONAL INPUT` | 阻断期末作业在总评中的具体百分比权重冻结；不阻断里程碑过程物证与及格底线设计。 |
