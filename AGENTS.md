# Agents Guide

## Agent skills

### Issue tracker

Issues and specs live in GitHub Issues (using the `gh` CLI). See `docs/agents/issue-tracker.md`.

### Triage labels

Five canonical triage roles (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`). See `docs/agents/triage-labels.md`.

### Domain docs

Single-context layout (`CONTEXT.md` and `docs/adr/` at repo root). See `docs/agents/domain.md`.

### Capabilities

External knowledge capabilities (NotebookLM knowledge bases). See `docs/agents/capabilities.md`.

## Artifact Boundary Guard

Repository-level file-growth and context-budget guidance across code, research Markdown, and Agent documents:
- ~600 physical lines is a soft structural-risk signal, not a hard limit or mandatory review/split gate.
- When real growth or maintenance friction suggests a boundary problem, consider natural responsibility, lifecycle, provenance/authority, review, and locality seams.
- Do not mechanically fragment cohesive artifacts solely to satisfy line counts.
- Refer to `docs/agents/artifact-governance.md` for current repository-specific placement guidance.

## Curriculum Evidence Discipline

任何会影响课程内容、周次排定、教学深度、能力要求、案例选择或考核设计的承重课程主张（load-bearing curriculum claim），必须明确标注其依据属性，严禁无 pointer 静默写成事实。

各维度标签**非互斥关系**，分别从以下三个正交维度进行定界：

1. **依据来源与溯源维度 (Grounding / Provenance)**：
   - **`SOURCE-BACKED`**：有明确的权威一手文献、教材章节或已验证素材引用（Exact Evidence Pointer：教材+章节/页码、官方规范/手册小节、CORE42 模块+课时 ID）；
   - **`PROJECT INFERENCE`**：明确标记为项目教学法推论或结构综合（如结合单师大班负荷对案例进行的剪裁与组合），不可混同为原始文献事实；
   - **`UNKNOWN / RESEARCH REQUIRED`**：当前在语料与仓库中缺乏足够依据，需显式暴露为待研究缺口（Research Gap），由后续专项调研补齐。
2. **运行时可行性维度 (Runtime Validity)**：
   - **`VERIFIED`**：已在受控环境（如真实机房 PC 或指定 Blender 版本）完成端到端探针验证；`VERIFIED` 只对实际测试的 host / software version / environment 生效；local macOS verification 不得自动泛化成 target-lab VERIFIED；
   - **`RUNTIME REQUIRED`**：理论与原理依据充分，但真实软件操作（如 Blender 交互路径）、资产拓扑/展开或机房环境可行性未经现场实测验证，必须由受控探针闭环。
3. **人类/项目决策权威维度 (Human / Project Disposition)**：
   - 从当前 Project Authority 读取（如 **`TEACHER ACCEPTED`**、`CONDITIONAL`、`HOLD` 等）；
   - 课程负责人采纳的项目决策属于 Project Authority，**严禁伪装为外部文献来源事实 (External Source Fact)**。

**智能体工作流守则 (Agent Discovery Rule)**：  
在进行任何课程规划、大纲编写、教学设计或代码审查前，智能体**必须首先查阅 `docs/research/week1-9-teaching-evidence-map.md` 中的对应条目**，严格贯彻“现有证据优先 (Existing Evidence First)”，严禁仅凭模型记忆或通用常识脑补课程内容。详细素材治理与消费链路见 `docs/methods/source-material-governance.md`。

**当代艺术引导教学决策指针 (Contemporary Art Guidance Decision Pointer)**：  
Course Owner 于 2026-10-21 权威采纳“艺术引导 → 技术支撑 → 创作表达 → 作品验证”四步闭环（`TEACHER ACCEPTED`）。后续课程设计智能体必须严格区分以下两个层次：
1. **全课程通用原则 (`TEACHER ACCEPTED`)**：PBR 与 Substance 3D Painter 技术学习仍是课程主体；当代艺术仅作为材质观察、创作判断与表达意图的引导资源，严禁独立增设艺术史或纯理论教学单元；严禁改变学院既有九讲顺序、严禁增加必修软件功能、严禁修改正式考核标准；
2. **第一讲专属待验证教学法 (`PROJECT INFERENCE / VALIDATION PENDING`)**：第一讲 MeetMat 采用单组材质身份对比与低负担前后观察对照法提升学生解释能力，属于局部待验证教学法，严格限定为第一讲有界试点，未经教师审查与真实课堂验证闭环，严禁向后续课次推广。完整决策边界与门禁依据见 [`docs/research/course-design-ledger.md` §5.9](docs/research/course-design-ledger.md)。

## Curriculum Terminology Discipline (课程术语规范纪律)

为落实 Course Owner 于 2026-10-31 权威确认的教学纪律（`TEACHER ACCEPTED — TERMINOLOGY POLICY`），全九周课堂课件、教师备课稿、操作卡、资产命名说明及智能体输出必须严格贯彻 **English-first** 术语原则：

1. **准确英文原名优先**：专业术语、界面元素、材质通道、纹理贴图与软件操作命令一律保留真实准确的英文原名（如 `Base Color`、`Roughness`、`Metallic`、`Specular Reflection`、`Diffuse Reflection`、`Specular Highlight`、`Fill Layer`、`Black Mask`、`Texture Set`、`Mesh Maps` 等）；
2. **中文仅作辅助释义**：中文用于通俗讲解生活现象或辅助认知，严禁单独使用模糊中文词（如笼统使用“反光”、“底色”、“贴图”、“通道”）替代不同英文原名导致指代混同；
3. **关键概念严禁混同**：
   - `Specular Reflection` (镜面反射光学现象) $\neq$ `Diffuse Reflection` (漫反射光学现象)；`Specular Highlight` (高光) 为视口观察到的动态镜面高光表现，非默认独立通道；
   - `Base Color` $\neq$ `Diffuse Map` $\neq$ `Albedo Map`（禁止作为无条件同义词，须按 Metallic/Roughness vs Specular/Glossiness 工作流及是否包含烘焙光照明确区分）；
   - `Material Channel` (材质通道) $\neq$ `Texture Map` (纹理贴图) $\neq$ `Layer` (图层) $\neq$ `Mask` (遮罩)；
   - `Microfacet Normal` (微平面法线) $\neq$ `Normal Map` (法线贴图)；`Roughness` 不等于真实几何置换；
4. **标准教学解释顺序**：遵循“先选英文原名 $\to$ 再用中文解释生活现象 $\to$ 最后回到软件 UI/参数/结果”的教学闭环；遇到不同软件版本 UI 差异与快捷键必须标为 `RUNTIME REQUIRED`，严禁凭空臆造。

## Cross-Platform & Multi-Agent Collaboration Protocol (跨平台与跨 Agent 协作规范)

为确保课程开发在 GitHub、Notion、Whimsical 跨平台及 Browser / IDE 智能体协作中保持严谨一致，避免重复建设与状态混乱，制定本规范：

### 1. 平台载体职责与权威层级 (Platform Roles & Authority Hierarchy)
- **GitHub (代码仓库)**：**唯一权威持久化基准 (Single Source of Truth / SSOT)**。所有正式采纳的课程架构、教学草案、实验代码及操作指南以 Git 仓库提交版本为准；
- **Notion (备课工作台)**：**教师备课与逐页内容审校工作台 (Teacher Review Scratchpad)**。用于教师交互式批注、逐页微调演讲脚本与视觉需求；Notion 为审校工作副本，**绝非与 GitHub 平级的第二 SSOT**；
- **Whimsical (知识白板)**：**课程知识全景与认知演化地图 (Course Knowledge Map)**。承载九讲能力递进与跨工具知识拓扑宏观概览，不承载微观执行代码与逐页讲稿；
- **权威层级与保护门禁准绳**：
  - `Course Owner 显式指令 > GitHub 已持久化权威基准 > Notion 审校工作稿 / Whimsical 视觉布局`；
  - **保护门禁定位**：GitHub 既有基线是**防止未经批准静默覆盖的保护门禁 (Protective Gate against unapproved silent overwrites)**，绝非用旧规则永久否决教师新决定的枷锁；
  - **结构变更流转**：若教师提出更改既有核心结构（如重排九讲、调整学时或考核框架），智能体应**暂缓执行、显式标记差异与潜在技术后果**，待教师明确授权后通过正常审查流转更新 GitHub 基线；严禁按时间新旧自动覆盖，严禁把未确认候选私自升格为批准决定。

### 2. Agent 职责分工与三步流转闭环 (The 3-Step Multi-Agent Loop)
跨 Agent 内容同步与任务交接必须严格贯彻以下三步闭环：
1. **Step 1 (Browser 传递与交接包完整性)**：
   - Browser Agent 负责在云端交互界面对接 Course Owner，整理教师已确认的内容变化（Confirmed Deltas），明确标注依据属性（如 `TEACHER ACCEPTED`）；
   - **交接包最低完整性字段 (Minimum Handoff Payload)**：因 IDE 端无权直接读取私有云端 Notion/Whimsical 内容，仅传外部链接视为无效交接。凡涉及归并的任务交接包必须具备：
     `source URL + content anchor/slide IDs + confirmed actual delta or accessible snapshot + teacher status + target GitHub path + base commit SHA`；
   - 图片与节点图等资产以**资源指针与审校状态**移交，不要求每次无谓复制整图数据；
2. **Step 2 (IDE 归并与凭证回传)**：
   - IDE Agent 严格基于交接包内的真实差量，在本地工作分支执行最小范围、有界且经过技术校验的文档/代码归并；
   - 创建规范 Git Commit 并推送至远端，向上游回传目标 Commit SHA、修改文件清单与验证说明；
3. **Step 3 (Browser 回读核验与状态闭环)**：
   - Browser Agent 基于 IDE 回传的目标 Commit SHA 回读 GitHub 仓库文件与 Diff，逐项核验是否严格符合教师原意、是否引入越界改动；
   - 审查通过后，在 Issue/PR 评论区发布闭环确认（Review Sign-off）并更新状态（`PENDING / VERIFIED / CONFLICT`）；**严禁仅凭 IDE“已推送”就单方面宣布内容双向同步完成**。

### 3. 同步触发条件与防碎片化纪律 (Sync Triggers & Anti-Fragmentation)
- **批量审校达成触发 (Batch Milestones)**：仅当教师在 Notion/交互端完成具有清晰边界的审校批次（如整组连续 Slide 审校完毕或关键教学决策确认）时，方可触发跨 Agent 同步工单；
- **严禁碎片化同步**：严禁逐字、逐条或单页频繁触发同步，坚决杜绝海量微型提交与状态抖动；
- **逆向技术事实回传**：IDE 本地环境探针结果（如软件版本限制、API 缺陷）通过 Issue/PR 评论持久化，由 Browser 回读并反馈至教师审校载体。

### 4. 冲突处理策略 (Conflict Resolution)
- **保护门禁拦截**：若 Notion 待审稿或 Whimsical 内容与 GitHub 既有核心架构冲突，**以 GitHub 既有基线为保护门禁拦截**；
- **禁止未审草稿覆盖**：未经教师最终确认的探索性草稿（`DRAFT / UNCONFIRMED`），**严禁直接覆盖 GitHub 既有文件**；
- **歧义降级裁决**：当存在冲突或表述不一致时，降级标记为 `CONFLICT DETECTED / PENDING TEACHER DISPOSITION`，由 Browser 提请教师裁决，获得明确确认后方可解锁同步。

### 5. 后续验证案例定界 (Week 1 Slide 12–14 Verification Case)
- **选定验证切片**：以 Notion 当前审校稿实际标题与内容（**Slide 12 `Microfacet & Roughness`**、**Slide 13 `Diffuse & Specular Reflection`**、**Slide 14 `Layer Mask Math` 候选**）作为后续跨 Agent 协作流程的候选验证切片；
- **执行门禁**：在教师于 Notion 完成这 3 页的逐页审校并由 Browser 明确传递确认 Delta 之前，**任何 Agent 严禁提前批量修改或直接覆盖 GitHub 中的 Slide Draft 对应段落，防止以旧草案错误覆盖**。




