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

## Collaborative Lesson Preparation Discipline

Teacher-facing lesson preparation is **decision-driven, not document-driven**.

- Keep the existing authority split: the Teaching Evidence Map routes evidence and research gaps; the executable Teaching Package owns weekly teaching contract and runtime/cut/recovery logic; the Student Handout owns the student task interface; the PPT with embedded Presenter Notes owns classroom presentation.
- **Do not create a fifth long-lived teaching SSOT** merely to make discussion easier. A teacher discussion view may be generated from existing authorities, but it must be rebuildable, source-versioned, disposable, and must not contain unique decisions.
- Use the loop **decision -> cheapest adequate validation -> propagate to affected consumers -> revalidate only the affected chain**. Propagation is part of completing the decision; do not defer synchronization to a later batch cleanup stage.
- Prototype by **risk/question**, not by ritual. A complete low-fidelity slide deck is not mandatory. Use the real Handout, Starter, critical observation image, or a few rough slides according to what must be tested. When an image/interface is itself the teaching input or evidence, use the real material early; defer decorative polish.
- Teacher/Course Owner owns pedagogical choices (what to teach, depth, ordering, task value, acceptable evidence). Agents own evidence lookup, dependency/impact analysis, mechanical propagation, pointer checks, and bounded revalidation. Agent suggestions remain proposals until accepted by Project Authority.
- Presenter Notes may add page-level speaking cues, transitions, misconceptions, demo prompts, and source pointers, but must not become a parallel policy document that independently redefines timing, recovery, terminology, or learning requirements.
- Separate **production readiness** from **go-live readiness**. Passing a slide/prototype production gate never closes target-lab runtime, delivery, submission, rehearsal, or field-validation gates.
- Stop when additional research, documentation, synchronization, or visual polish no longer changes a teacher decision, student action, acceptance criterion, recovery path, source pointer, or known validation risk.

Detailed artifact lifecycle and change-propagation guidance lives in `docs/agents/artifact-governance.md`.

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


