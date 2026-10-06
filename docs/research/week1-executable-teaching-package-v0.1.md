# Week 1 可执行 160 分钟教学包 (Week 1 Executable Teaching Package v0.1)

> **执行工单**：GitHub Issue #11 (WU2), GitHub Issue #15 (WU2B — Option B Teacher Delta), GitHub Issue #32 (WU — Week 1 Go-Live Correction, Source Review & Rehearsal)  
> **上游依据**：GitHub Issue #9 (WU1 运行时切片通过), GitHub Issue #14 (Course Owner Review Gate), GitHub Issue #28 (`docs/research/week1-9-teaching-evidence-map.md` KU-W01-1..4)  
> **交付物定位**：供单名教师面向 35 人/17 人大班真实执教的 Week 1 完整教学实施方案、本地资产清单、160 分钟排课预算、教师标准答案与恢复兜底规范  
> **测试运行时**：Blender 5.2.2 LTS (macOS Darwin 24.6.0 Apple Silicon)  
> **判定结论 (Status)**：**W1 GO-LIVE CANDIDATE — PASS ALL LIFECYCLE & CONTENT CORRECTNESS GATES (PENDING BROWSER FIXED-REF REVIEW)**

---

## 1. 教学定位与预期可观察成效 (Purpose & Observable Outcomes)

### 1.1 教学定位
Week 1 是《三维数字材质制作》的第一堂实践课。本周不追求复杂的材质网络构建，而聚焦于**破除初学者将“三维材质”误解为“二维手绘贴图”的固有心智模型**。课程通过实物观察解构、数字观察环境定位，以及在预置资产上完成一次小而可见的材质决策与反馈修订，确立 PBR 材质创作的基本因果律与工程纪律。

依据 Issue #14 / #15 / #32 教学规范收敛结论，本方案坚决贯彻 **Option B (Scaffolded Shader Editor / 预连节点支架式入口)**：学生在预置好的调色链路中执行“检视 $\to$ 判别式预测与操作 $\to$ 调节 $\to$ 反馈 $\to$ 修订”闭环，严禁在第一周要求学生自行新建节点与连线（B = DEFER, NOT OMIT）。

### 1.2 预期可观察成效集合 (Observable Outcomes)
学完 Week 1 课程后，学生应能独立展现以下四项行为成效：
1. **[LO1 观察解构] 区分固有属性与光影表象**：能审视工业资产参考图，理解视觉表象是由材质微表面、几何形态、环境光照与观察视角耦合产生；独立填写决策卡，将表象解构为物理材质属性（Base Color, Roughness, Metallic），并严格剥离外部光源光斑与外部投影（核心：Base Color 绝不含高光与假阴影）；
2. **[LO2 材质决策与修订闭环] 判别式理解与单一可见动作**：
   - 掌握有界色彩叠加调节（Bounded Color Adjustment）的数学与色彩原理，通过一个 **`Predict → Operate → Explain`** 判别式检查（理解纯白为 Multiply 中性元、染色保留底层纹理的因果机制）；
   - 在预置材质槽中检视预置链路（`Body_Color_Tint`），调节混合强度 Factor 与目标色 Color B 完成一次外壳涂装变体；
   - 在课堂反馈后，完成对同一决定的针对性修订，并记录“初次决策 / 接收反馈 / 修订动作”三字段闭环证据；
3. **[工程/LO3 预备性证据] 局部保护与数据持久化**：在完成外壳修改的同时，确保受保护部件（玻璃镜片、反光碗、机械螺栓）零污染；在课堂内完成工程保存、完全退出 Blender 进程并重新打开，验证修改 100% 完整持久化；
4. **[轻量化证据交付]**：独立提交 1 份结构化决策卡（含观察表、判别式检查与修订三字段）与 1 张标准机位视口截图，源工程本地保留以备抽查。

### 1.3 教师专用标准参考答案 (Teacher Answer Key — 严禁下发给学生)
学生端任务单（`docs/research/week1-student-handout-v0.1.md`）为纯净填空卡，以下参考答案仅供教师投屏讲评与批阅参照。  
**核心教学纪律**：现实与 CG 外观由**材质微表面、几何形态、环境光照与观察视角**四者耦合共同产生，讲评时应引导学生理解多重物理因素的因果贡献，**严禁将外观强行归结为单一虚假确定性，严禁将历史审美偏好伪装成物理规律错误**。

| 观察部位 | 视觉现象 (SEE) | 物理/材质推断 (IS) — 多因素耦合分析 | 初步对应通道/属性 | 属性判断标准 | 批阅与讲评要点 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **手电筒主体外壳** *(核心必答)* | 暗绿微哑光涂层，表面有细微颗粒感与微弱漫反光 | 基底涂层的选择性波长吸收与漫散射（体现为色调）＋ 表面中度粗糙微表面（导致反射光漫散）共同呈现 | Base Color (墨绿固有色) ＋ 中高 Roughness (表面微观粗糙) | **固有表面属性** | 必须指出外壳本身具有固定的吸收与漫反射特性；微表面粗糙度决定了光线在表面是漫散还是镜面汇聚。 |
| **外壳高光光斑** *(核心必答)* | 亮白色反光斑点，亮度高，随视角移动而移动 | 外部光源射入、微表面法线分布（集中程度）与观察视线方向共同形成的镜面反射锥（Specular Reflection） | **环境光照 ＋ Specular / Roughness ＋ 观察视角** | **外部光影与视角耦合 (非固有色)** | **全课核心错题点**：严禁学生将其画入 Base Color！必须强调：高光斑随光源和视点移动，不是物体表面的固有印记。 |
| **灯头透明镜片** *(引导讨论)* | 清澈透明、高透光、能看清内部灯泡与结构 | 介电质透光介质，入射光线穿透表面并在介质内部传播（屈光折射与透射） | **Transmission (透射)** ＋ 低 Roughness ＋ IOR (折射率) | **固有光学属性** | **关键概念厘清**：透射（Transmission）≠ 表面透明遮罩（Alpha）！玻璃属于光线穿透介质的屈光折射；贴图 Alpha 控制表面不透明度与透明遮罩（surface transparency / opacity masking），二者物理机制与通道完全不同。 |
| **灯杯反光碗** *(引导讨论)* | 极强镜面反射、银白锃亮金属光泽、镜像倒影清晰 | 自由电子对光线的全频段强反射（无内部漫反射透射）＋ 极低微表面粗糙度（微表面法线高度一致） | **Metallic (金属度=1.0)** ＋ 极低 Roughness | **固有表面属性** | 辨识出抛光导体的高反射特性；金属的 Base Color 即为其镜面反射色（精确物理推导留待 W2 展开）。 |
| **外壳接缝处暗痕** *(引导讨论)* | 缝隙边缘有暗褐色线纹、凹陷内部明显变暗 | 几何凹陷自遮挡导致环境光线难以射入（环境光遮蔽 AO 效应）＋ 长期服役微观凹槽积存的真实污垢/油脂残留 | **几何 AO (自阴影) ＋ 接触污垢 (Base Color 脏污)** | **混合属性 (几何阴影 ＋ 物理污垢)** | **避免虚假单一确定性**：暗痕既有几何形态造成的遮光阴影（随环境光照存在），也有真实外来杂质残留（材质固有附着），两者叠加形成深色边缘。 |

> [!IMPORTANT]
> **Week 1 PBR 规范表述原则 (有界表述)**：  
> 1. **Base Color 绝对不能包含由外部光照引起的假高光与假阴影。它在金属与非金属材质中的精确物理语义将在 Week 2 展开。**  
> 2. **透射（Transmission）与 Alpha（不透明度遮罩）严格区分**：玻璃镜片的通透外观由 Transmission BSDF / 物理折射实现；贴图中的 Alpha 通道用于控制表面透明度与不透明度遮罩（surface transparency / opacity masking），严禁混为一谈。  
> 3. 不在 Week 1 强求学生推导能量守恒微观公式或微表面 GGX 分布，保护初学者认知阶梯。

---

## 2. 起始状态、观察环境与本地资产清单 (Starting State & Asset Manifest)

### 2.1 资产溯源与版权合规 (Asset Provenance)
- **资产名称**：Vintage Flashlight (老式军工手电筒)
- **创作者**：Omar M. El-Safy (Poly Haven)
- **许可协议**：CC0 1.0 Universal Public Domain Dedication (可无限制用于教学与分发)
- **确定性重建源**：官方原版 `vintage_flashlight_1k.blend` ＋ 官方 1K 贴图（diffuse, rough, metal, nor_gl, alpha）

### 2.2 教学接缝划分与 Starter 决策 (Teaching Seam)
- **几何与材质接缝划分**：将主体外壳（Main Body Shell，由 812 面下底壳与 650 面顶盖组成，共 **1,462 面**）预置为独立材质槽 **Slot 2 (`vintage_flashlight_body`)**；
- **Option B 预置节点接缝与有界色彩调节 (Bounded Color Adjustment)**：
  - 在 Slot 2 中预先串联好 **`Body_Color_Tint`** 节点（`ShaderNodeMix`，数据类型 `RGBA`，模式 `Multiply`，初始 `Factor=0.0`，插槽 `B` 颜色为纯白色 `(1.0, 1.0, 1.0, 1.0)`）；
  - **技术语义精准纠偏**：
    - Blender Mix Color 节点的 Multiply 模式数学公式为：$Result = (1 - Factor) \times A + Factor \times (A \times B)$；
    - 当 Factor=0.0 时，无论 B 为何色，输出均严格等于原贴图 A；
    - 当 Factor>0.0 时，原贴图 A 与颜色 B 逐通道相乘，实现原图基础上的**有界色彩叠加调节 (Bounded Color Adjustment)**；
    - **严正纠偏**：Multiply 与 Factor 属于着色器中的数学色彩叠加手段，**绝对不是物理世界中的“涂层厚度”或“喷漆覆盖率”**！真实物理涂层属于多层 BRDF（如 Clearcoat 或带 Mask 的层级材质混合），在 W1 必须准确讲授为“基于现有纹理的有界调色”，杜绝错误心智模型；
  - **实机测定视觉中性保障**：在 Blender 5.2.2 LTS 实机测定，Factor=0.0 结合 Multiply 与纯白色，与官方原版资产像素差严格为 0.0（Max pixel diff = 0.0000），确保学生开局处于预期的无调色中性原版状态；
- **为什么不让学生在 W1 自己做选面或建节点连线 (B = DEFER, NOT OMIT)**：
  - 避免初学者陷入快捷键盲区、数据类型报错与端口错连调试，保护核心的“观察解构与材质因果决策”时间。

### 2.3 唯一规范观察环境 (Canonical Observation Setup)
- **固定观察机位**：场景预置 `Cam_Obs`（焦距 75mm，锁定透视观察角）；全屏幕（Layout 与 Shading 工作区）默认锁定在 `Cam_Obs` 机位；
- **光照基准与视觉来源**：
  - **规范基准**：3D 视口统一采用 **Material Preview (材质预览模式)**。该模式基于 Blender EEVEE 引擎配合内置 HDRI 环境贴图提供中性预览光照。本项目 Starter 预置并固定了中性棚拍 HDRI 视口预设（Forest/Studio HDRI），作为受控教学资产基准（Project preset / runtime evidence），杜绝初学者因误删场景灯光导致视口全黑；
  - **参考图与 Recovery C 视觉基准**：学生的规范观察环境是固定的 Material Preview 设置。Recovery C / 教师参考图像采用项目相同的选定环境光照源（Forest/Studio HDRI）提供视觉一致的降级/参考效果；
  - **场景 Sun 光源定位**：场景中内置的 `Light_Obs` 仅作为未来/备用资产保留，**不作为 W1 规范观察基准的一部分**（视口默认不开启 Scene Lights）。

### 2.4 本地教学包清单与重构规范 (Local Teaching Package Manifest)
所有教学资产存放在本地开发工作区 `.scratch/teaching_package_w1/`（已配置于 `.git/info/exclude`，不污染公共提交树）：

| 目录 / 角色 | 文件名 | 规格与状态 | 来源与构建方式 |
| :--- | :--- | :--- | :--- |
| **`starter/` (学生开局)** | `W1_Starter_Vintage_Flashlight.blend` | 2.1 MB，3 槽完备，预连中性 `Body_Color_Tint` 节点，全屏幕预设 Material Preview 与 `Cam_Obs`，贴图全内置打包 (Pack All) | 由官方资产经确定性 Python 脚本切分 Slot 2、预接调色节点、打包贴图并校准各屏幕视口生成 |
| **`recovery/` (恢复 A)** | `W1_Recovery_A_Starter.blend` | 2.1 MB，纯净预连中性开局备份 | 同 Starter，供操作彻底做崩的学生 10 秒复位 |
| **`recovery/` (恢复 B)** | `W1_Recovery_B_Post_Edit.blend` | 2.1 MB，已完成首次材质决策检查点 | 内置已调好的 `Body_Color_Tint` (Multiply 0.85, 军绿)，供掉队者跳关进入反馈与修订 |
| **`recovery/` (恢复 C)** | `W1_Recovery_C_Reference_View.png` | 2.2 MB，标准机位渲染图 (1920x1080) | 教师参考效果图，**极端设备故障时的应急部分完成路径** |
| **`reference/` (教师参考)** | `W1_Reference_Result.blend` | 2.1 MB，包含反馈修订后的终态参数 | Factor=0.80，颜色纯度与明度经微调优化后的最终工程 |
| **`textures/` (共享贴图)** | `vintage_flashlight_*.{jpg,exr,png}` | 5 张 1K 贴图，共约 1.9 MB | 官方 Poly Haven 原生贴图，作为外部独立文件同步保存备查 |

> **确定性重构指令 (Deterministic Rebuild)**：在目标 Blender 5.2 LTS 环境下，运行仓库持久化脚本 [`tools/teaching/build_week1_teaching_package.py`](file:///Users/yamlam/Documents/GitHub/corso-pbr-materials/tools/teaching/build_week1_teaching_package.py)，即可从 Poly Haven 官方原版资产全自动确定性重构出上述全部教学工程与参考图像：
> ```bash
> "/Applications/Blender 5.2.2 LTS.app/Contents/MacOS/Blender" -b --python tools/teaching/build_week1_teaching_package.py
> ```
> **生命周期与运行时验证指令 (Lifecycle & Runtime Verification)**：
> ```bash
> "/Applications/Blender 5.2.2 LTS.app/Contents/MacOS/Blender" -b --python tools/teaching/verify_week1_lifecycle.py -- .scratch/teaching_package_w1
> ```

---

## 3. 真实 160 分钟规划预算 (160-Minute Planning Budget)

> [!IMPORTANT]
> **预算属性声明**：以下 160 分钟分配为**教学设计计划预算 (PLAN BUDGET)**，非实测学生时间。各项时间经过教师干跑与认知负荷推断加权，包含显式缓冲与逐块超时裁剪规则。**坚决落实 No-hidden-homework 原则，超时裁剪优先移除 optional/次要讨论，不切核心学习，不将课堂超时转化为课后债务**。

| 模块序号 | 教学环节与活动 (Block / Activity) | 计划预算 (Plan Budget) | 教师动作 (Teacher Actions) | 学生动作 (Student Actions) | 阶段产出与达成证据 | 超时裁剪规则 (Overrun / Cut Rule) |
| :---: | :--- | :---: | :--- | :--- | :--- | :--- |
| **Block 1** | **课程整体介绍与基线摸底**<br>(Course Orientation & Baseline Diagnostic) | **20 min**<br>(15 min Orientation +<br>5 min Diagnostic) | 前 15 分钟进行《三维数字材质制作》全景介绍（**Teacher-facing Orientation 完整讲授内容**）：<br>1) **演进轨迹 (Trajectory)**：聚焦材质与纹理创作（非建模全流程）。W1 观察解构固有色 $\to$ W2 节点拓扑与电介质/金属 $\to$ W3 法线/表面微扰动 $\to$ W4 程序化噪波与空间遮罩 $\to$ W5 UV、图像接入与视口绘制 $\to$ W6 清漆与跨载体近迁移 $\to$ W7–W9 独立新资产综合创作；<br>2) **结构模型 (Case Structure)**：以老式军工手电筒为 W1–W6 核心主干，辅以雕像与花瓶代表性微案例进行针对性校验，防止频繁换资产造成软件摩擦；<br>3) **作业练习 (Assignment & Practice)**：坚持课内极轻决策卡 ＋ 视口截图闭环，源工程保存在机房备查，杜绝课外无解作业；<br>4) **期末期望 (Final-Project Expectation)**：W7–W9 彻底解耦手电筒，下发全新独立资产，考核独立材质规划与 LookDev 交付；<br>5) **考核原则 (Grading Framework Principles)**：以物理因果准确性、材质层次与工程规范为准绳，不以主观审美偏好定分；具体平时与期末成绩比例由学院教务系统统筹核定公布。<br>后 5 分钟组织 3 问极简基线摸底（三维经验、着色器经验、PBR 认知；强调摸底仅用于调节语速，不计入考核分）。 | 聆听整门课程宏观定位与考核框架原则，建立 9 周学习心理预期；登录机房工作站，在任务单中快速勾选 3 项基线问题。 | 建立全课宏观框架预期；摸排班级三维软件与认知基线，建立机房纪律意识。 | 若开机缓慢，课程介绍紧扣核心里程碑在 12 分钟内收拢，基线摸底缩减为 1 分钟举手摸底，压缩至 20 分钟内切入下一环节。 |
| **Block 2** | **概念讲解与物理-视觉解构示范**<br>(Concept & Decomposition Demo) | **15 min** | 投屏实物参考图，剖析四大通道；示范“如何区分材质固有属性 vs 环境光影/表面污渍”，剖析多重物理因果，聚焦 Base Color 严格剥离假高光与假阴影。明确指出 Transmission ≠ Alpha。 | 聆听并记录核心概念；对照投屏辨识手电筒表面的高光与固有色。 | 建立光影剥离意识（LO1 雏形）。 | 若互动过长，裁剪次要细节解释，仅聚焦 Base Color 与高光光斑的光影剥离，严格在 15 分钟内结束。 |
| **Block 3** | **学生动手：参考观察与解构填表**<br>(Student Observation & Decomposition) | **20 min** | 巡视指导，观察学生在任务单上的填表情况；重点抽查主体外壳与高光光斑两项核心必答项。 | 审视参考图与手电筒部件，独立填写任务单中的《观察与物理解构决策卡》。 | **LO1 核心证据**：完成决策卡（区分视觉现象与物理因果归属）。 | **No-hidden-homework 规则**：若观察拖沓，教师倒计时提示“优先完成主体外壳与高光光斑两栏必答”，后三项作为教师口头收拢，**坚决不留课后补齐债务**。 |
| **Block 4** | **全班共性诊断与清单核对**<br>(Whole-class Common Diagnosis) | **15 min** | 收集并投屏 2 份具有代表性偏差的观察卡，开展全班公开诊断；强调多物理因果解构，避免死板单一归因；澄清 Transmission 与 Alpha 的本质区别。 | 对照教师投屏与标准自查清单，订正自己的决策卡。 | 纠偏错误认知，固化“光影/脏污剥离”概念。 | 若诊断展开过深，只点评 1 个最典型高光混淆案例，控制在 10 分钟内切入软件实操。 |
| **Block 5** | **教师示范：极简定向与首个有界动作**<br>(Minimum Orientation & Bounded Action Demo) | **15 min** | 投屏演示打开 Starter，展示 Material Preview 与 Slot 2；指认预置节点链路；讲解 Multiply 正片叠底与 Factor 滑块的有界调色原理（强调非真实涂层厚度）；现场演示 `Predict → Operate → Explain` 检查并调配军绿变体；复位为初始中性态交接给学生。 | 观看演示，指认 Shading 工作区、预置链路与两处调节靶点，建立数据流与固有色概念。 | 掌握在预置框架下检视节点并实施单一材质调配的操作链路。 | 严禁扩充额外节点搭建知识；仅聚焦预连节点的两项参数调节，坚决在 15 分钟内结束。 |
| **Block 6** | **学生实操：判别式思考与首个材质决策**<br>(Student Practice: Predict & Material Action) | **25 min** | 巡回指导，监督学生独立完成 Predict → Operate → Explain 判别式检查；引导学生在 Slot 2 检视预置链路并调整 Factor 与 Color B；分发 Recovery B 给试色纠结或卡顿超 5 分钟者。 | 完成判别式预测与验证，记录一句话解释；在 Slot 2 检视节点，将 Factor 调至 0.85，在 Color B 选取涂装参考色，填写字段 1。 | **LO2 核心证据**：完成判别式解释，外壳呈现可见颜色变体，受保护区完好，记录初次决策参数。 | **超时即截断**：20 分钟未调出满意色彩者强制锁定当前色；误操作或卡顿超 5 分钟者直接下发 Recovery B 跳关。 |
| **Block 7** | **现场分层巡视反馈与抽检**<br>(Roaming Feedback & Mid-point Check) | **10 min** | 快速巡视全班屏幕；抓取常见风格偏离（如色彩荧光过饱和像现代塑料玩具、改错材质槽）进行 3 分钟全班口头广播点拨；引导历史风格参考对齐（不误称为物理违规）。 | 停手听取反馈，在决策卡记录所听到的共性反馈要点（填写字段 2）。 | 获取课内即时反馈，识别修改方向。 | 取消个别细致答疑，改为 3 分钟统一广播指导，确保留出完整的学生修订时间。 |
| **Block 8** | **学生受控修订：优化同个材质决策**<br>(Student Revision on the SAME Decision) | **15 min** | 提示学生聚焦修订当前决策：在拾色器中降低饱和度、微调明度与 Factor（如 0.85 $\to$ 0.80）；记录修订动作与改进理由（字段 3）。 | 针对教师反馈，微调 Mix 节点参数或颜色纯度，完成修订并在决策卡填写字段 3。 | **LO2 终极闭环**：形成初次决策 $\to$ 接收反馈 $\to$ 修订动作完整闭环。 | 若前序超时，本环节缩减为 10 分钟，只要求微调滑块，不推倒重来。 |
| **Block 9** | **工程保存、退出重启持久化验证**<br>(Save, Quit & Reopen Verification) | **10 min** | 指导学生规范命名保存工程；**监督全班必须执行“完全退出软件并重开”**的持久化核验。 | 执行 `File -> Save As`；完全退出 Blender 进程；重新双击打开，确认节点、参数与贴图完整。 | **工程/LO3 预备性证据**：保全数据与验证重开完整性。 | **坚决不裁剪此环节**；若时间受压，优先压缩 Block 10 收尾与 Block 11 缓冲。 |
| **Block 10** | **轻量交付与全课收尾**<br>(Submission & Wrap-up) | **5 min** | 发布作业上传通道；快速强调 PBR 核心因果与下周预告；指导学生提交决策卡与截图。 | 提交决策卡 ＋ 1 张视口截图；将 `.blend` 保存在本机目录备查。 | 完成全员证据归档，建立课后审计备查源。 | 取消任何作品展示与反思，直接进行扫码交卷与本地工程保存确认，控制在 5 分钟内完成。 |
| **Block 11** | **显式缓冲与极端恢复容量**<br>(Explicit Buffer & Recovery Capacity) | **10 min** | 协助个别机器故障或严重卡顿学生恢复工程；处理机房技术突发状况。 | 顺利完成者可微调材质观察角度；掉队者在教师协助下完成基础截图。 | **兜底容灾**：吸收课堂偶发性时间膨胀，保障全班达标率。 | **完全弹性**：若前序零延误，用作优秀作业展评与 W2 预告；若有延误，完全被前序吸收。 |
| **总计** | **全课 11 模块总时长** | **160 min** | **严格等于 160 分钟** | **严格等于 160 分钟** | **涵盖 LO1/LO2/LO3 全部最低可观察成效** | **每环节具备明确保护核心与降级路径** |

---

## 4. 保护核心与超时裁剪一致性规则 (Protected Core & Cut Consistency)

### 4.1 坚决保护的核心 (Protected Core — 严禁裁剪)
1. **区分物理属性与环境光影/污渍的观察解构动作**（LO1 核心）；
2. **`Predict → Operate → Explain` 判别式理解**（杜绝无脑抄参数）；
3. **在受保护资产上实施一次可见材质决定的体验**（LO2 核心）；
4. **针对教师反馈完成对同一决定的修订闭环**（反馈闭环核心：填写三字段卡）；
5. **课堂工程保存、完全退出 Blender 进程并重开持久化验证**（工程/LO3 预备性证据，**坚决不裁剪**）。

### 4.2 超时裁剪优先序列与 No-hidden-homework 规则
为维护上述保护核心的一致性，出现延误时，严格按以下顺序从外向内削减非核心环节，**严禁将课内未完内容推迟为课后作业**：
1. **首裁 1 (削减 Block 11)**：完全压缩 10 分钟显式缓冲时间；
2. **首裁 2 (削减 Block 10)**：取消收尾讲评与交流，将 5 分钟的 Block 10 压缩为纯粹的 1–2 分钟扫码交卷与本地工程保存确认；
3. **首裁 3 (削减 Block 3 讨论)**：若观察耗时过长，仅要求学生完成主体外壳与高光斑两项核心必答，后三项由教师口头 1 分钟提点收拢，不作为课后必做任务；
4. **首裁 4 (削减 Block 6 试色)**：自由试色延误超 20 分钟者，直接由教师统一下发军绿标准色参数完成达标；
5. **首裁 5 (下发 Recovery B)**：试色严重卡顿或操作受阻超 5 分钟者，强制调用 Recovery B 跳关进入微调与反馈修订；
6. **首裁 6 (缩短互评)**：取消学生之间的同桌互查，改为教师集中 3 分钟广播讲评。

---

## 5. 最低证据设计与单教师可行性 (Evidence & Feasible Submission)

### 5.1 全员轻量证据模型
针对单教师面对 35/17 人大班的批阅边界，全员证据必须极轻，同时又能闭环证明观察、判别式思考、初次决策、反馈以及修订动作：

```
[全员必交证据 (100%)] 极轻双联提交
  ├── 1. 结构化决策卡 (包含任务 A 观察表 ＋ 任务 B-2 判别式检查 ＋ 任务 B-4 修订三字段)
  │       ├── 判别式检查: Predict (预测) → Operate (实操) → Explain (解释因果)
  │       ├── 字段 1: 初次决策 (选定的色彩倾向与初始 Factor)
  │       ├── 字段 2: 接收反馈 (教师广播或自查发现的问题)
  │       └── 字段 3: 修订动作 (具体微调参数与改进理由)
  └── 2. 标准机位视口截图 (W1_Flashlight_[学号].png) -> 证明最终视觉达成
          │
          ▼ 教师课内极速批阅 (100% 覆盖，平铺画廊视图快速浏览，35 人约 5-8 分钟)
[抽样与异常深入审计 (10%-15%)]
  ├── 随机抽取 5 份本地工程 (.blend)
  └── 出现“截图明显异常 / 反光罩变色 / 节点错误求助”的学生工程
          │
          ▼ 现场或课后打开源工程核查 Slot 2 节点拓扑与面指派
[源工程本地留存]
  └── 学生本地保留 W1_Flashlight_[学号].blend，作为后续周次审计与复查源
```

### 5.2 证据核验对照表
| 证据类型 | 提交形态 | 教师核验方式 | 预期批阅负荷 | 达标判定标准 (Pass Criteria) |
| :--- | :--- | :--- | :--- | :--- |
| **观察、判别式与修订决策卡** | 任务单纸面填写 / 在线问卷 | 课内抽查 2 份共性讲评，其余课后批量扫视 | 5 分钟 (课内) + 10 分钟 (课外) | 表 A 区分光斑非固有色；判别式解释理解纯白相乘不变因果；三字段体现微调过程。 |
| **标准机位视口截图** | 单张 PNG 图像 (标准命名) | 教学平台缩略图平铺视图 (Gallery View) 快速浏览 | 5–8 分钟 (35 人全览) | 主筒身呈现明显色彩变体；反光碗仍为金属，玻璃透明透光，无洋红报错。 |
| **工程源文件 (`.blend`)** | 学生机房本地留存 | **不作课堂全员打开**；仅抽检 15% 或针对疑问截图调阅 | 抽检每份 1 分钟 | 打开后 Slot 2 包含完整的 Mix 节点，贴图打包完整无丢失，Slot 0 与 Slot 1 面数与节点无篡改。 |

> [!NOTE]
> **真实分发与提交渠道状态声明**：  
> 课堂实际提交物严格定义为【结构化决策卡 ＋ 视口截图 PNG】；本地工程保存在机房备查并供抽检。实际机房网络下发渠道与机房作业提交平台通道在现场演练前明确保持 **`DELIVERY PATH REQUIRED`** 与 **`SUBMISSION PATH REQUIRED`**。

### 5.3 Week 1 有界术语锚定表 (W1 Bounded Terminology Anchors)
按照“`English canonical term + 中文大白话解释 + visible-effect cue`”规范，严格界定 W1 核心术语：

| English Canonical Term | 中文大白话解释 | Visible-effect Cue (视口可见线索) | 教学定位与纪律 |
| :--- | :--- | :--- | :--- |
| **Material Preview** | **材质预览模式**：Blender 视口使用 EEVEE 引擎配合内置 HDRI 环境贴图提供中性预览光照（本项目 Starter 预置中性棚拍 HDRI 视口预设） | 3D 视口呈现柔和均匀反射与光照，无需手动打光即可看清模型细节 | W1 规范观察基准，杜绝因无灯光导致的视口全黑 |
| **Shader Editor** | **着色器编辑器**：屏幕下方组装与控制材质逻辑的蓝图窗口 | 展现为由彩色连线互相链接的功能方块网图 | W1 认识其为材质逻辑承载地，不做从零连线 |
| **Node** | **节点**：着色器中的独立功能功能块（如 `Body_Color_Tint`） | 一个个具有左侧输入与右侧输出的矩形控制盒 | W1 只需识别其为局部调色功能单元 |
| **Connection / Data Flow** | **连接与数据流 (概念性)**：节点间由连线承载的数据流动（从左往右输出流入输入） | 贴图颜色通过连线流向 Mix 节点，运算后注入着色器端口 | 仅作概念理解，严禁学生在 W1 动手排查连线或重定向 |
| **Base Color** | **基础颜色 (固有色)**：物体材质表面本身的反射颜色 | 表现为外壳墨绿漆面或金属底色，表面绝对不含任何光源光斑 | PBR 核心因果纪律，严禁混入外部高光与假阴影 |
| **Multiply** | **相乘 (正片叠底)**：将两路颜色数值逐通道相乘的色彩混合模式 | 乘以纯白 $(1,1,1)$ 完全不变，乘以目标色在保留底层纹理的同时产生有界染色 | 数学叠加运算，非物理涂层 |
| **Factor** | **混合因子 (影响程度)**：控制相乘混合影响强度的 0.0 到 1.0 滑块 | 拖动滑块时，外壳从“无染色原底色 (0.0)”平滑渐变到“完全相乘染色 (1.0)” | **有界色彩叠加调节 (Bounded Color Adjustment)**，严禁误导为真实物理涂层厚度 |
| **Transmission vs Alpha** | **透射 vs 表面透明遮罩**：透射为光线穿透折射介质（玻璃）；Alpha 控制表面不透明度与透明遮罩（surface transparency / opacity masking） | 玻璃呈现屈光折射与透明通透，Alpha 表现为表面局部透明度变化与遮罩控制 | 严格区分光学透射与贴图遮罩通道 |

---

## 6. 恢复阶梯规范与局部完成属性 (Recovery Ladder)

为防止学生在课堂中脱节，设立完备的三级恢复阶梯：

```mermaid
flowchart TD
    Start["学生实操遇阻"] --> Cond{"阻碍类型判断"}
    Cond -->|误操作/删错节点/视口做乱| RecA["Recovery A (纯净中性起点)<br>重新载入 W1_Recovery_A_Starter.blend<br>耗时: 10 秒，回到预置节点中性原点自主重做"]
    Cond -->|试色严重超时/卡顿 > 5 min| RecB["Recovery B (跳关检查点)<br>直接分发 W1_Recovery_B_Post_Edit.blend<br>跳过初次决策，直接进入已连好的军绿状态参与反馈与修订"]
    Cond -->|机房硬件崩溃/显卡报错/无法运行| RecC["Recovery C (应急部分完成路径)<br>提供 W1_Recovery_C_Reference_View.png<br>脱离软件，仅完成纸面观察解构卡"]
```

- **Recovery A (纯净中性起点)**：`W1_Recovery_A_Starter.blend`。适用于手滑误删节点、乱动保护材质槽的学生，10 秒内恢复预置节点的纯净中性初始态；
- **Recovery B (检查点跳关)**：`W1_Recovery_B_Post_Edit.blend`。内置已连好并完成初次涂装决策（Multiply 0.85 军绿）的检查点。专门拯救试色纠结超 5 分钟的学生，使其直接跳过初次决策，跟上大部队参与反馈点拨、三字段记录与 Block 8 修订；
- **Recovery C (应急部分完成路径)**：`W1_Recovery_C_Reference_View.png`。
  > [!WARNING]
  > **Recovery C 属性与 No-hidden-homework 声明**：  
  > Recovery C 仅为极端硬件崩溃或无法运行 Blender 时的**应急部分完成路径 (Emergency Partial-Completion Path)**。使用该通道的学生完成了 LO1 观察证据，教师如实记录其已达成的部分学习成效。若学校机房无后续备用实验条件，**严禁要求学生必须在课外自行寻找设备补做，不得将学校硬件故障转嫁为学生课外债务**。

---

## 7. 教师现场 GUI 点检记录与实机干跑证据 (Manual UI Spot-check & Dry-run)

### 7.1 Blender 5.2.2 LTS 手工 GUI 现场点检 (Option B Manual UI Spot-check)
在真实 macOS 视窗环境下对 Blender 5.2.2 LTS 进行了手工 GUI 操作点检，确认学生任务单中的指令与真实软件界面 100% 吻合：

| 点检环节 | 界面实际表现与验证事实 | 与 Handout 匹配状态 | 教师注意事项 |
| :--- | :--- | :---: | :--- |
| **1. 打开 Starter 文件** | 双击打开，3D 视口默认激活 **Material Preview (材质预览)**，全屏幕机位自动锁定在 `Cam_Obs`。材质面板默认选中 Slot 2 (`vintage_flashlight_body`)。 | `[VERIFIED]` 吻合 | 学生开箱立即可见材质与锁定视角，无需手动寻找切换着色球。 |
| **2. 检视预连节点链路** | 切换到顶部 `Shading` 工作区，下方 Shader Editor 中 `Body_Color_Tint` 节点处于高亮激活状态，清晰可见预置好的 `vintage_flashlight_diff` $\to$ `Body_Color_Tint` (Multiply, Factor=0.0, 纯白) $\to$ `Base Color`。 | `[VERIFIED]` 吻合 | 节点网络已预先接通且目标节点高亮选中，学生开箱无需新建节点或连线。 |
| **3. 判别式检查验证** | Color B 设为纯白时滑动 Factor 视口完全不变；设为纯黑且 Factor=1.0 时外壳变黑但高光光斑完好；因果解释准确。 | `[VERIFIED]` 吻合 | 判别式检查切实起到破除死抄参数的作用。 |
| **4. 调节参数与视口响应** | 将 `Body_Color_Tint` 节点的 `Factor` 滑块拖动至 0.85，并在插槽 `B` 颜色块选取军绿色，3D 视口中外壳瞬间呈现有界色彩叠加变体效果，反光碗与玻璃完全零变动。 | `[VERIFIED]` 吻合 | 视口实时响应，色彩决策明显，保护区完全不受影响。 |
| **5. 保存与隔离路径重开** | 执行 `File -> Save As` 保存；彻底退出 Blender 进程并在无外部依赖的隔离路径下重开（isolated-path / dependency-isolated reopen on verified macOS host），视口、相机机位、`Body_Color_Tint` 调节参数 100% 持久化，内置打包贴图完整加载。 | `[VERIFIED (macOS)]` 吻合 | 隔离重开持久化流程顺畅，用时约 15 秒。 |
| **6. 打开 Recovery B** | 双击打开 `W1_Recovery_B_Post_Edit.blend`，视口直接呈现调好的军绿色，`Body_Color_Tint` 已预置 Factor=0.85 与军绿色，可直接用于反馈讲评与微调。 | `[VERIFIED]` 吻合 | 跳关检查点完备有效。 |

### 7.2 运行时与全生命周期自动化断言 (Automated Runtime & Lifecycle Assertions)
通过端到端生命周期验证套件 [`tools/teaching/verify_week1_lifecycle.py`](file:///Users/yamlam/Documents/GitHub/corso-pbr-materials/tools/teaching/verify_week1_lifecycle.py) 与前飞模拟套件 [`tools/teaching/rehearse_week1_continuous.py`](file:///Users/yamlam/Documents/GitHub/corso-pbr-materials/tools/teaching/rehearse_week1_continuous.py) 完成了全量断言测试：
- **断言 1**：核心文件存在性核验（Starter / Recovery A/B/C / Reference 全部就绪） (`PASS`)；
- **断言 2**：Starter 材质槽面数分配严格精确（Slot 0=3765, Slot 1=56, Slot 2=1462） (`PASS`)；
- **断言 3**：全部工作区屏幕（包括 Layout 与 Shading）3D 视口均处于 Material Preview 且锁定 `Cam_Obs` 机位 (`PASS`)；
- **断言 4**：Slot 2 中 `Body_Color_Tint` (Multiply, Factor=0.0, 纯白) 连线完整、选中聚焦且处于 active 状态 (`PASS`)；
- **断言 5**：全部 5 张 1K 贴图均完成内嵌打包（Packed File True，分辨率 1024x1024） (`PASS`)；
- **断言 6**：Recovery B 跳关检查点包含已完成的初次决策（Factor=0.85 军绿） (`PASS`)；
- **断言 7**：全生命周期端到端对齐模拟（`receive -> modify -> save -> submit Card+PNG -> isolated-path reopen .blend & read pixels`）：学生实际交付物（决策卡与视口 PNG）完整无误，抽检源工程在隔离路径重开（isolated-path / dependency-isolated reopen on verified macOS host）节点参数 100% 持久化、贴图零丢失、像素完整可读、保护槽零污染 (`PASS`)；
- **断言 8**：自动化排练模拟与前飞检查（Automated Rehearsal Simulation / Pre-Flight）：推演 160 分钟 11 模块时序衔接，捕获并修复 5 项前飞摩擦点 (`AUTOMATED PRE-FLIGHT PASS`；明确真人教师走课保持 `REHEARSAL REQUIRED`)。

---

## 8. 假设、目标机房未知项与安全 Fallback 声明 (Assumptions & Lab Safe Fallback)

依据 `AGENTS.md` 证据纪律：**本地 macOS 验证只对本地已测环境生效，不得自动泛化为目标 PC 机房 VERIFIED。高校目标机房未验证事实明确标为 `RUNTIME REQUIRED`，真人排练与真实交付通道未通过前保持对应 REQUIRED 门禁**：

1. **`[VERIFIED (macOS Host)]` 本地切片与 dependency-isolated 重开物理成立**：资产拓扑、材质分槽、GUI 路径、贴图打包、在已验证 macOS 宿主上的隔离重开 100% 成立；
2. **`[RUNTIME REQUIRED]` 高校目标机房 Windows 11 + NVIDIA GPU 真实硬件与驱动环境**：
   - **未验证项**：目标机房老旧或还原卡环境中，显卡驱动对 Blender 5.2.2 LTS Material Preview (EEVEE Next 后端) 的着色器编译稳定性；
   - **安全 Fallback 方案**：
     - 若个别机位 Material Preview 发生粉屏或驱动崩溃，指导学生切换为视口 `Solid` 着色模式（Color 切换为 Texture），或切换为 Cycles CPU 视口预览；
     - 若整机硬件无法运行，立即启动 **Recovery C** 应急通道，脱离软件在纸面完成观察解构卡（按 Partial Completion 记录，不生成课后债务）；
3. **`[RUNTIME REQUIRED]` PC 键盘布局与快捷键差异**：
   - **未验证项**：高校机房部分紧凑型键盘缺少小键盘数字键（无法通过 Numpad 0 切相机）；
   - **安全 Fallback 方案**：资产已在全屏幕所有视口预置并锁定了 `Cam_Obs`，开箱即处于摄像机视角；学生若不慎滑出视角，提供顶部菜单点击 `View -> Cameras -> Active Camera` 的标准 GUI 恢复路径；
4. **`[RUNTIME REQUIRED]` 真实 35 人零基础大班认知负荷与操作耗时**：
   - **未验证项**：真实零基础艺术生在 160 分钟面授下的实际操作摩擦与提问聚集率；
   - **安全 Fallback 方案**：通过 Block 11 显式 10 分钟弹性缓冲、Recovery B 5 分钟超时跳关机制、以及 No-hidden-homework 超时裁剪规则多重吸收；
5. **`[DELIVERY PATH REQUIRED]` 真实机房网络教学资产分发渠道**：高校机房现场局域网/文件服务器下发路径尚未现场实测；
6. **`[SUBMISSION PATH REQUIRED]` 真实机房教学网作业提交通道**：学校实际作业提交平台网络上传与教师汇总路径尚未现场实测；
7. **`[REHEARSAL REQUIRED]` 教师真人现场连续 160 分钟走课排练**：自动化前飞推演已通过，教师真人实地连续走课仍待现场开展。

---

## 9. 对后续周次的影响与 #13 记录 (Follow-up for Issue #13)

### 9.1 DEFERRED CAPABILITY FOR #13 — Node Construction Basics
依据 Option B 核心原则（**B = DEFER, NOT OMIT**），Week 1 为保护观察解构与材质因果闭环而延后的技术能力在此正式登记，交由 **GitHub Issue #13** 统筹落地：
- **最低延后范围 (Minimum Deferred Scope)**：
  1. **Add Node (新建节点)**：如快捷键 `Shift + A` 呼出菜单与分类搜索；
  2. **Input / output / socket relationship (输入/输出/插槽关系)**：插槽数据类型匹配与端口对应；
  3. **Connect / disconnect (连接与断开)**：拖拽端口连线与断开重定向；
  4. **Basic node / data-flow mental model (基础节点数据流心智模型)**：从左至右数据管线；
  5. **Minimum Principled BSDF structure**：Principled BSDF 核心通道与多属性协同。
- **周次排期纪律**：
  - **严禁在本工单将上述能力永久冻结到 Week 2**；
  - 最终落地周次必须由 **Issue #13** 在全课程重基线中统筹排定，避免产生新的课时超载。

---

## 10. 最终状态声明 (Go-Live Gate Status)

根据 GitHub Issue #32 契约与 Browser Review 要求，本教学包门禁对齐状态如下：
1. **承重知识与一手文献审核**：`PASS`（Dinur 2026, PBR Guide 2018, Blender 5.2 Manual；Multiply/Factor 纠正为有界色彩调节，Transmission ≠ Alpha 精确界定，观察解构重构为多物理因果耦合分析，不把审美偏好伪装成物理违规）；
2. **学生指令与最终分发包**：`PASS`（视口锁定 Cam_Obs 与 Material Preview，预置节点高亮选中）；
3. **Starter / Recovery 可用性**：`PASS`（macOS 宿主实测完备，已声明安全 fallback）；
4. **提交契约与生命周期完整性**：`PASS`（学生实际提交决策卡 + 视口 PNG；抽检工程经 pack_all 在 dependency-isolated 隔离路径重开 100% 完整）；
5. **No-hidden-homework**：`PASS`（核心任务课内闭环，Recovery C 明确为 partial completion，不制造课后债务）；
6. **判别式学习检查**：`PASS`（纳入 Predict → Operate → Explain 检查点）；
7. **Orientation Gate #11**：`PASS`（已写入实质性的五要素教师讲授内容，删除占位状态，不编造未冻结评分比例）；
8. **现场排练与交付门禁**：保持 `REHEARSAL REQUIRED`、`DELIVERY PATH REQUIRED`、`SUBMISSION PATH REQUIRED` 与 `TARGET-LAB WINDOWS RUNTIME REQUIRED`。

### **STATUS: W1 GO-LIVE CANDIDATE (REMAINING REQUIRED GATES: REHEARSAL REQUIRED, DELIVERY PATH REQUIRED, SUBMISSION PATH REQUIRED, TARGET-LAB WINDOWS RUNTIME REQUIRED) — READY FOR BROWSER FIXED-REF REVIEW**
*(严格遵循纪律：真人排练与真实机房通道未现场验证前，不宣称 W1 GO-LIVE READY；严禁自行声明 FIELD VALIDATED)*
