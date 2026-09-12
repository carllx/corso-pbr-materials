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

Repository-level file-growth and context-budget policy across code, research Markdown, and Agent documents:
- ~600 physical lines is a mandatory structural-review trigger (not an absolute hard limit).
- Crossing ~600 lines or materially expanding over-threshold files requires evaluating responsibility, lifecycle, authority/SSOT role, review boundary, and change locality before expanding.
- Split only along natural, cohesive boundaries; never fragment mechanically just to satisfy line counts.
- Existing over-threshold artifacts are grandfathered (maintenance/corrections permitted; no new independent responsibilities without review).
- Generated, vendor, lockfile, and dataset fixtures are recognized exceptions.

See `docs/agents/artifact-governance.md` for full normative semantics and registered hotspots.
