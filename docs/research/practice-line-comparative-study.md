# 三维数字材质制作实践主线候选有界对比研究 (Practice-Line Comparative Study)

> **研究阶段**：Stage 2 Gate 3B 路线重定向 (Route Re-baselining / Matt-aligned Shortest Route)  
> **审查基线与依据**：GitHub Issue #5 (Comment ID: `5706879947`)、独立纠偏审查报告 (`docs/research/curriculum-direction-red-team-2026-09-17.md`)、Gate 3A PASS 锚点 (`cdbeaa1aca0efcc81b0b6e4f26170722d81a32db`)。  
> **核心使命**：为 8 周本科《三维数字材质制作》寻找一条**最短、连贯、低备课负担、可维护的实践主线**，承载约 70–80% 的学生实践，其余能力通过最小课程补丁加入；通过单一代表性材质闭环干跑（Dry-run）验证路线，为进入 Week 1–8 Planning Draft 扫清障碍。

---

## 1. 定位与非目标边界 (Purpose & Boundaries)

依据 Issue #5 最新指导，本报告严格遵循以下工作纪律：
1. **不重新调查 47 Candidate Provenance**：Candidate Set v2 继续作为已冻结的 Research Inventory，不产生逐项教学覆盖义务；
2. **不搞伪精确数字打分与臆想阈值**：严禁使用未经实测的节点数、分钟数或百分比作为硬性及格线，以实际干跑观察记录为准；
3. **不展开全网教材重新海选**：严格限定在负责人指定的三条代表性候选实践主线；
4. **不提前编写 Week 1–8 排课大纲**：必须在代表性闭环验证完成且主线冻结后方可进入；
5. **不建设过度工程平台**：不开发自动化测试框架、MCP 备课流水线或复杂 Python Harness，坚持教师端轻量干跑。

---

## 2. 待确认 Owner 决策提议 (Proposed Owner Decisions / Pending Confirmation)

> *注：以下四项为基于教学可达性与维护成本提炼的**建议决策 (Proposed Decisions)**，尚待课程负责人/用户正式确认 (Pending Confirmation)，不预设已闭环。*

1. **提议决策 1：一条成熟实践主线承担约 70–80% 学生实践，其余能力通过最小课程补丁加入**
   * *建议结论*：**`ACCEPT (建议采纳)`**。
   * *依据*：避免拼凑 10–14 个孤立练习带来的资产频繁切换与教师维护负担；以单一贯穿资产建立核心心智模型，其余 LO4 程序化节点、LO5 外部素材质检与 LO6 交付作为模块化补丁注入。
2. **提议决策 2：`Blender-first` 仅为暂定候选 (Provisional Default)，而非课程原则；若受控局部修订在 Painter 中明显降低教学复杂度，则允许 Painter 成为该段主宿主**
   * *建议结论*：**`ACCEPT (建议采纳)`**。
   * *依据*：工具选型服务于学习收益与认知负荷。若 Blender 原生方案因缺乏非破坏图层栈而需要教师维护高度黑箱的自定义节点组，导致总体教学复杂度激增，则 Painter 应成为 LO3 的合规主宿主。
3. **提议决策 3：成熟第三方教学体系可作为实践参考 (Practice Reference)，但项目自有的 PBR Guide / Dinur / Shah / LO 架构继续保有知识与课程判断权威**
   * *建议结论*：**`ACCEPT (建议采纳)`**。
   * *依据*：第三方案例用于借用模型与操作步骤；课程评价标准、物理光学概念与质感审视权威归项目自身所有。
4. **提议决策 4：LO6 保留一次受限且真实的下游交付验证 (Export / Transfer / Open / Verify)，严禁用 EEVEE ↔ Cycles 内部切换冒充真实交付**
   * *建议结论*：**`ACCEPT (建议采纳，保持极窄)`**。
   * *依据*：内部渲染器切换无法暴露贴图通道错位、格式解析、坐标轴翻转等真实管线问题。必须保留一次极窄的真实跨环境流转检验。

---

## 3. 三条实践主线候选详细界定 (Three Practice-Line Candidates)

### 候选 A：Zeeshan Jawed Shah (2022) Chapters 3–6 (Retro TV 资产主线)
- **依托资产**：`Retro_Tv.FBX`（Packt 官方公开仓库提供全套资产、网格与贴图）。
- **实践范围**：Substance 3D Painter 资产纹理绘制（Ch 3 图层栈与投影 $\to$ Ch 4 复杂遮罩与平面裁剪 $\to$ Ch 5 笔刷预设与印花模板 $\to$ Ch 6 智能材质、锚点联动、全局落灰与贴图导出）。
- **事实边界**：Packt 官方提供配套下载代码与资产；**具体在高校班级分发与课堂复用的法律许可范围（Classroom redistribution rights）仍需在分发前核实确认**。

### 候选 B：Blender Fundamentals (4.5/5.2 LTS) Watering Can (水壶材质—渲染段)
- **依托资产**：`watering_can.blend`（Blender Studio 官方教程配套资产）。
- **实践范围**：提取教程中的 **Shading**（着色节点、程序化渐变、Noise 粗糙度、Voronoi 凹凸、Color Attributes 遮罩）与 **Lighting & Rendering**（环境光、三点布光与渲染）段落。
- **事实边界**：水壶案例与前序 Geometry Nodes 构造动画存在深层绑定，对材质创作主干而言是明显弱点；**但其官方着色与布光文件仍可作为高价值的局部教学参考**。

### 候选 C：CG Cookie CORE V2 (Blender 5.2 LTS) Materials & Texturing (双课组合段)
- **依托资产**：官方 Shading Ball 测试球 + 节点/贴图练习模型。
- **实践范围**：提取《Fundamentals of Materials and Shading》（着色器编辑器、Principled BSDF 参数、节点拓扑）与《Fundamentals of Texturing》（UV 基础、程序化纹理、贴图类型、绘制与烘焙）核心段。
- **事实边界**：CG Cookie CORE V2 明确支持教育采购与多坐席授权；**订阅费用与账号管理属于实际教学采购约束（Cost / access constraints），而非绝对的法律分发屏障**。其主要挑战在于案例分散，缺乏贯穿全流程的单一生产资产。

---

## 4. 逐项承重标准对比分析 (Detailed Comparative Analysis)

| 评价维度 | 候选 A：Shah (2022) Ch 3–6 (Retro TV) | 候选 B：Blender Fundamentals (Watering Can) | 候选 C：CG Cookie CORE V2 (Shading + Texturing) |
| :--- | :--- | :--- | :--- |
| **1. 实践连贯性 (Continuity)** | **高**。围绕单一资产 `Retro_Tv` 展开，前后图层与细节工艺递进演进，具有完整资产迭代体验。 | **较低**。Shading 段与 Geometry Nodes 构造动画耦合，材质节点混杂了几何节点属性输入。 | **模块化中等**。双课体系各自严谨，但在测试球、金属片与独立模型间切换，缺乏贯穿全周期的单一生产资产。 |
| **2. Material 是否真正居中 (Material Centrality)** | **高**。专注材质与纹理创作（PBR 通道、分层、磨损、几何贴图驱动），完全避开建模与展 UV 干扰。 | **低 (偏向综合功能集成)**。教程穿插拓扑修复（Dissolve/Knife）、UV 旋转以及几何节点数据输入。 | **中–高**。专注着色器与纹理技术，但包含较多传统 UV 展开与综合着色概念。 |
| **3. 已提供资产与许可状态 (Assets & Licensing)** | Packt 提供下载代码与网格工程；**但课堂批量分发的最终版权细则仍待核实**。 | Blender Studio 提供官方工程；部分源文件需会员登录下载；开源工具本体无门槛。 | 配套工程完备；支持多坐席与机构采购；**但存在订阅预算与账号准入约束**。 |
| **4. 教师补建与备课负担 (Teacher Prep Burden)** | **较低**。需对齐 2026 Painter 界面（F8 独立烘焙、OpenPBR），补建修改单与外部交付目标。 | **高**。需剥离几何节点动画依赖，为缺乏多通道贴图绘制的工作流补充大量自制教程。 | **中等**。需统一实战模型（教程末尾让学生自备模型），并为 Blender 贴图绘制补充辅助模板。 |
| **5. 第二次受控修订支持度 (Revision Support)** | **天然架构优势**。图层栈、黑白蒙版与锚点机制便于局部修改，非目标区域与无关通道隔离直观。 | **支持度较弱**。依赖 Color Attributes 与节点混合，面对多通道同步修改与二次追加时，节点网络易迅速复杂化。 | **程序部分支持，绘制部分繁琐**。程序节点调参容易；原生贴图绘制因缺少图层栈管理，局部版本迭代摩擦较大。 |
| **6. 程序化内容足够且可解释 (Procedural Content)** | 几何遮罩与程序噪波丰富，但缺乏显式 DAG 节点图连接（需由 Blender 节点补丁补充）。 | 涵盖 Separate XYZ、Noise、Voronoi 等经典节点，但与几何节点混合增加了理解干扰。 | **极佳且高度可解释**。从数学基础、颜色混合到复杂程序化生锈，步骤规范透彻，是节点教学典范。 |
| **7. AI / 外部素材判定插入点 (AI Seam)** | 外部位图可直接作为 Fill Layer、Stencil 或 Alpha 印花进入图层栈，接口直观。 | 主要依靠数学节点生成外观，较难自然容纳多通道外部生成贴图的质检与混合。 | 可在着色器中接入 Image Texture 节点替换程序纹理，直接对比外部素材与程序材质的响应。 |
| **8. 下游交付接口 (Downstream Delivery Seam)** | 原生支持工业级通道打包导出（如 ORM、16-bit Normal），对接外部引擎顺畅。 | 依赖内部属性与程序节点，导出为通用 FBX/glTF 需先进行烘焙，管线较脆弱。 | 详细讲授了 Blender 烘焙到贴图的流程，可输出标准贴图，但烘焙配置步骤较繁琐。 |
| **9. 许可、机房与维护成本 (License & Maintenance)** | 需机房配备 Painter 教育/实验室许可；版本更新平稳，维护成本较低。 | 软件全开源免费；机房部署摩擦极低；官方文件需确保教师端可稳定获取。 | 软件基于 Blender；但课程平台具商业属性，全班合规接入取决于机构采购预算。 |
| **10. 相对六大 LO 的缺口 (Deficits vs LO1–LO6)** | 缺深度微表面光学推导（需 McDermott 补丁）、缺独立着色节点连线（需 Blender 节点补丁）、缺外部 AI 质检。 | 缺失资产级多通道分层绘制与受控修订、缺失现实意图解构、缺乏标准外部打包流程。 | 缺失全流程单一生产资产贯穿、Blender 原生绘图层管理较弱、存在平台访问与采购前置。 |

---

## 5. 对比结论与暂定领先者建议 (Findings & Recommendation)

基于有界证据对比，正式提出当前路线建议：

> **当前暂定领先候选 (Current Provisional Front-runner)**：  
> **以 Shah Retro TV (Chapters 3–6) / Painter 为中心的资产纹理创作主线，尚待单一代表性闭环干跑验证。**

### 关键定性权衡：
1. **Watering Can 不作为主干，但保留为局部参考**：水壶案例与 Geometry Nodes 的深度耦合使其不适合作为 70–80% 的材质实践主干；但其官方制作的着色器设置与布光文件仍可作为 LO2/LO4 的辅助参考；
2. **CG Cookie CORE V2 重新定位为教学参考典范**：其在 Blender 5.2 下对着色器节点与程序化锈迹的剖析极具教学价值，适合作为教师设计 LO4 紧凑节点补丁的范式参考，而非全班直面教材；
3. **未决前置条件**：必须通过下述干跑检验，方能最终裁定 Painter 是否能正式担当 LO3 主宿主，不得提前宣布 Painter 胜出。

---

## 6. 单一代表性材质闭环验证定义 (Single Representative Material Loop Validation)

将原先分散的两个探针折叠为一个紧凑的**单一代表性材质闭环 (Single Representative Material Loop)**。教师端在真实软件环境中对同一测试资产进行干跑（Dry-run），只对比核心摩擦点。

```
       ┌────────────────────────────────────────────────────────────────────────┐
       │                单一代表性材质闭环验证 (Representative Material Loop)     │
       └───────────────────────────────────┬────────────────────────────────────┘
                                           │
  ┌────────────────────────────────────────┴────────────────────────────────────────┐
  ▼                                                                                 ▼
【阶段 1: 创作与受控修订对比 (Blender vs Painter)】             【阶段 2: 受限外部交付 (统一规范)】
  同一资产 (Retro TV 或机械部件)                                标准 PBR 导出 (BaseColor/ORM/Normal)
  → 可编辑基底材质搭建 (Base Material)                            → 导入单一外部目标 (glTF Viewer 或 UE5)
  → 艺术指导受控局部修改 #1 (Revision 1)                         → 旋转环境光与多视角观察
  → 二次追加受控局部修改 #2 (Revision 2)                         → 记录差异归因与排错要点
```

### 6.1 受控修订规范化定义 (Controlled Revision Scope)
严禁要求无关物理表现“100% 绝对不变”，采用结构化物理约束规范：
* **目标区域 (Target Region)**：指定的一个局部范围（如机壳顶盖右上边缘）；
* **预期改变的通道与关系 (Intended Changes)**：局部调整涂层剥落遮罩，显露底层红锈 Base Color，并增加对应位置的 Normal 微凹凸；二次修订微调剥落边缘羽化并加深红锈色相；
* **非目标区域 (Non-target Region)**：模型其余表面（如前面板、旋钮、未划伤漆面）；
* **预期保持不变的属性 (Properties Expected Unchanged)**：非目标区域的固有色、微表面粗糙度与金属度；
* **允许自然响应的物理耦合效果 (Physically Coupled Effects Allowed to Respond)**：脱漆交界处的金属度突变、局部微观法线凹凸引起的菲涅尔边缘高光重分布、以及受光角度变化带来的自然反射响应。

### 6.2 记录与观测指标清单 (Observation Checklist — 实测记录而非预设及格线)
在同一硬件与资产条件下干跑并记录以下真实事实：
1. **教师准备与工程搭建负担 (Teacher Prep & Setup)**：搭建起始工程所需的工时、外部资源依赖度；
2. **学生直面概念量 (Student-Visible Concepts)**：完成操作需调动的核心概念数（如：图层/遮罩/生成器 vs 节点类型/向量映射/属性传递）；
3. **预制黑箱结构量 (Prebuilt Black-box Structure)**：是否必须依赖教师封装好的复杂自定义节点组或专用插件；
4. **编辑局部性 (Edit Locality)**：执行修改时，操作范围是否被良好限制在局部，有无污染全局或误伤非目标通道；
5. **依赖关系的直观可查性 (Dependency Inspectability)**：各通道关联与遮罩驱动关系能否直观定位并排除故障；
6. **二次修改摩擦度 (Second-revision Friction)**：面对追加修改时，是顺畅滑动参数，还是需要重构连线/重绘像素；
7. **典型排错点与踩坑率 (Troubleshooting Points)**：干跑中记录的具体软件崩溃、贴图丢失或视觉异常点；
8. **导出与转换步数 (Export Steps)**：从创作环境生成合规 PBR 贴图的实际点击与配置步数；
9. **目标端重建负担 (Target-side Reconstruction)**：在外部查看器或测试引擎中还原材质时所需的连线与参数微调工作量。

---

## 7. 旧 Gate 3B 核心主张审计处理表 (Gate 3B Claims Disposition)

对基线 `minimal-teaching-stack.md` (commit `960090f...`) 作出审计处置：

| 原始主张项 | 原始宣称 | 处置裁定 | 处置理由 |
| :--- | :--- | :---: | :--- |
| **LO1–LO6 六大成效** | 课程核心能力框架。 | **RETAIN** | Gate 3A 已 PASS，具备跨工具持久性，继续作为共同设计语言。 |
| **人机责任分工原则** | 审美归人，计算归机。 | **RETAIN** | 确立核心能力护城河，经受住了审查检验。 |
| **支撑管线边界底线** | 建模展 UV 仅为支撑。 | **RETAIN** | 坚决防止课程反客为主蜕变为建模基础课。 |
| **开放标准认知深度** | 学生直面语义，不手写代码。 | **RETAIN** | 隔离底层管线工程超载，保护本科教学核心体验。 |
| **Blender-first 单宿主** | Blender 作为全课主宿主。 | **DOWNGRADE** | **降级为 Provisional Default**；最终地位取决于代表性闭环干跑结果。 |
| **14 TP / 10 Hands-on** | 宣称为“全局最小唯一组合”。 | **DOWNGRADE** | **降级为候选要素池**；缺乏实际时间账支持，不再享有必然性地位。 |
| **交付目标配置** | Primary: EEVEE; Secondary: Cycles。 | **DOWNGRADE** | **降级为内部比对工具**；真实交付必须包含一次狭窄的跨软件外部流转。 |
| **Designer 角色** | 教师演示与概念参考。 | **DOWNGRADE** | 保持为按需参考，不设学生端操作与安装要求。 |
| **“USER DECISION = NONE”** | 宣称所有决策已闭环。 | **WITHDRAW** | **彻底撤回**。掩盖了宿主复杂度与交付边界等核心待定决策。 |
| **“14/10 数量具必然性”** | 宣称数字是闭环真理。 | **WITHDRAW** | **彻底撤回**。教学单元数量应随实践主线与课堂容量自然生发。 |
| **内部比对冒充交付** | 用双渲染器切换替代真实交付。 | **WITHDRAW** | **彻底撤回**。违反 LO6 目标交付要求，撤回以内部比对代交付的主张。 |
| **伪精确课时节省数值** | 宣称精准节省 8–10 课时。 | **WITHDRAW** | **彻底撤回**。缺乏实际分钟级账目与备课成本核算。 |
| **预置模板零成本假定** | 假定提供模板无需维护成本。 | **WITHDRAW** | **彻底撤回**。模板存在黑箱理解与版本失效成本，撤回零成本假设。 |

---

## 8. 结论、未决事实与充分性停止声明 (Conclusion, Unknown Facts & Sufficiency Stop)

### 8.1 明确当前仍未决/未知的外部事实 (Unknown Facts)
以下客观事实当前仍处于 `UNKNOWN` 状态，不应在未经核实前做出确切结论：
1. `[UNKNOWN 01]`: **Packt 代码仓库中 `Retro_Tv` 资产面向高校教学全班二次分发（Classroom redistribution）的正式许可细则**；
2. `[UNKNOWN 02]`: **当前目标机房环境的实际 GPU 算力与 Adobe/Blender 真实授权部署状态**；
3. `[UNKNOWN 03]`: **开课专业学生的真实前置三维软件技能中位数**。

### 8.2 充分性停止声明 (Sufficiency Stop)
* **本 Work Unit 已正式完成**：已确立 4 项待确认决策提议、完成三条候选路线的客观有界证据对比、提出以 Shah Retro TV / Painter 为暂定领先候选，并将验证收敛为**单一代表性材质闭环 (Single Representative Material Loop)**。
* **门禁冻结说明**：**在上述单一代表性材质闭环干跑完成（证实路线顺畅或暴露重大阻碍）之前，严禁启动 Week 1–8 Planning Draft 编写**。
