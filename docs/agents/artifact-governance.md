# Artifact Boundary & Growth Governance

This document establishes the repository-local policy for artifact growth, file boundaries, and context guards across human-maintained code, research Markdown, and Agent-facing documents.

## Core Principle: Guardrails vs Architecture

**Size is a guardrail, not architecture.**

Physical line count serves as an objective structural-review trigger. However, structural decisions are driven by architectural qualities, not line-count optimization:
- **Responsibility**: Does the artifact maintain a single, cohesive responsibility, or is it accumulating disjoint concepts?
- **Lifecycle**: Do different sections change at different times and for different reasons?
- **Authority / SSOT Role**: Does the artifact serve as a canonical source of truth where splitting would create ambiguity or synchronization hazards?
- **Review Boundary**: Can human reviewers and Agent tools effectively inspect, reason about, and verify diffs?
- **Change Locality**: Does a typical edit touch localized sections, or does it require holding the entire document in immediate working context?

Agents must never perform mechanical splits or create shallow fragmentation solely to satisfy an arbitrary line-count target.

## The ~600-Line Structural Review Trigger

For human-maintained code, research Markdown, and Agent-facing documents:
- **~600 physical lines** is a **mandatory structural-review trigger**, not an absolute hard limit.
- **Trigger Conditions**:
  1. A proposed change causes a previously under-threshold file to cross ~600 lines.
  2. A proposed change materially expands an existing file that is already over ~600 lines.

When the trigger is reached, the Agent must conduct a structural assessment before expanding the file.

### Permitted Structural Evaluation Outcomes

When evaluating an artifact at or above the ~600-line trigger, the Agent must explicitly determine one of three outcomes:

1. **`CONTINUE COHESIVE`**:
   The content remains tightly coupled to a single responsibility or authoritative lifecycle. Splitting would introduce artificial boundaries, harm readability, or disperse a single coherent reference. Expansion is permitted within that responsibility.
2. **`SPLIT REQUIRED`**:
   Natural, independent boundaries exist (distinct sub-domains, independent lifecycles, clear module seams). The artifact should be partitioned along these natural boundaries.
3. **`EXCEPTION OR DEFERRED REFACTOR`**:
   The artifact qualifies as a recognized exception (see below) or is an existing monolithic asset where refactoring is explicitly out of scope for the current work unit.

## Legacy Over-Threshold Policy (Grandfathering)

Existing artifacts that already exceed the ~600-line threshold prior to the adoption of this policy are grandfathered.
- Grandfathered artifacts do not require emergency splitting or preemptive re-architecting.
- **Factual corrections, maintenance, and narrow localized edits** within grandfathered artifacts do **not** automatically trigger a large refactor.
- However, Agents **must not** unilaterally append substantial new independent responsibilities or unrelated topics to grandfathered files without explicit structural review and deliberate planning.

## Code vs. Prose & Research Markdown

- **Source Code**: Adheres to strict modularity, high cohesion, loose coupling, and testability boundaries. Deep modules with narrow interfaces are preferred over sprawling files.
- **Prose & Research Markdown**: Research syntheses, native knowledge indices, and comprehensive curricula often benefit from contiguous reading and unified cross-referencing. Review triggers for Markdown must prioritize topical cohesion and indexing integrity over arbitrary segmenting.

## Recognized Exceptions

The 600-line trigger does not mechanically apply to:
- Auto-generated artifacts, schemas, or compilation targets
- Vendor libraries and third-party imports
- Lockfiles (`package-lock.json`, etc.)
- Test fixtures, test matrices, and raw dataset files
- Self-contained narrative specifications or monolithic source transcripts where external slicing harms provenance

---

## Known Repository Hotspots (Registered Architecture Reviews)

| Artifact Path | Current Lines | Status | Governance Directive |
| :--- | :--- | :--- | :--- |
| `docs/research/source-native-knowledge-index.md` | ~1,356 | **Existing Over-Threshold Artifact** / *Architecture Review Required* | Grandfathered monolith. Contains browser-verified synthesis (Shah, PBR Guide, Dinur, RTR4). **Do not split, migrate, or restructure** during localized research or narrow maintenance. Refactoring requires a dedicated, deliberate architectural work unit. |
