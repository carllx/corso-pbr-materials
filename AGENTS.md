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

任何会影响课程内容、周次排定、教学深度、能力要求、案例选择或考核设计的承重课程主张（load-bearing curriculum claim），必须属于以下至少一种明确状态，严禁无 pointer 静默写成事实：

1. **`SOURCE-BACKED`**：有明确的权威一手文献、教材章节或已验证素材引用（Exact Evidence Pointer：教材+章节/页码、官方规范/手册小节、CORE42 模块+课时 ID）。
2. **`PROJECT INFERENCE`**：明确标记为项目教学法推论或结构综合（如结合单师大班负荷对案例进行的剪裁与组合），不可混同为原始文献事实。
3. **`UNKNOWN / RESEARCH REQUIRED`**：当前在语料与仓库中缺乏足够依据，需显式暴露为待研究缺口（Research Gap），由后续专项调研补齐。
4. **`RUNTIME REQUIRED`**：理论与原理依据充分，但真实软件操作（如 Blender 交互路径）、资产拓扑/展开或机房环境可行性未经现场实测验证，必须由受控探针闭环。

详细路由地图与缺口台账见 `docs/research/week1-9-teaching-evidence-map.md`；素材治理与消费链路见 `docs/methods/source-material-governance.md`。

