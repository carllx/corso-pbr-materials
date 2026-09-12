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
