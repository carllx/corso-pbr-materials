# Artifact Structure Guidance & Current Repository Placement Decisions

This document establishes repository-local guidance for artifact structure, file boundaries, and context guards across human-maintained code, research Markdown, and Agent-facing documents, alongside accepted placement decisions for current work units.

## Core Principle: Signals vs Architecture

**Size is a heuristic signal, not architecture.**

Physical line count serves as an informative signal rather than an architecture driver. Structural decisions are driven by contextual qualities rather than line-count targets:
- Agents must never perform mechanical splits or create shallow fragmentation solely to satisfy an arbitrary line count.
- When real growth or maintenance friction suggests a potential boundary problem, structural boundaries should follow natural modular seams.

## The ~600-Line Structural-Risk Signal

Across human-maintained code, research Markdown, and Agent-facing documents:
- **~600 physical lines** is a **soft, low-cost structural-risk signal**, not a hard limit or mandatory architecture/review gate.
- It may justify extra attention when the current task also encounters real friction (e.g., navigation overhead, review difficulty, or synchronization hazards).
- Line count alone does **not** require splitting, architecture review, or an extra refactoring work unit.

### Optional Diagnostic Lenses

When real task friction indicates that an artifact boundary might need rethinking, Agents may select from relevant diagnostic lenses suited to the live task (not a mandatory checklist):

- **Responsibility & Cohesion**: Does the artifact maintain a single cohesive purpose, or is it accumulating disjoint concepts?
- **Lifecycle & Change Propagation**: Do different sections change at different cadences and for different reasons?
- **Provenance & Authority / SSOT**: Does the artifact serve as a canonical source of truth where splitting would create synchronization hazards or ambiguity?
- **Interfaces & Natural Seams**: Are there clean boundaries and natural seams for partitioning, or would splitting produce tightly-coupled, shallow fragments?
- **Locality & Navigation**: Does a typical edit touch localized sections, or does it require holding sprawling unrelated context in working memory?
- **Review Boundary & Validation**: Can human reviewers and Agent tools effectively inspect, reason about, and verify diffs?

Decisions naturally align with common-sense patterns (such as continuing a cohesive file where unity is valuable, splitting along natural boundaries when seams are distinct, or deferring refactoring when out of scope), without requiring formal classification states.

## Legacy Over-Threshold Policy (Grandfathering)

Existing artifacts that already exceed ~600 lines are grandfathered:
- They do not require emergency splitting or preemptive re-architecting.
- Factual corrections, maintenance, and task-required localized edits proceed normally.
- Avoid default continued accumulation of substantial new, unrelated responsibilities onto existing large files.

## Code vs. Prose & Research Markdown

Boundary considerations differ fundamentally between executable code and explanatory prose:

- **Source Code**: Focus on cohesion, clear interfaces, low coupling, locality, testability, natural seams, and feedback loops. Deep modules with well-defined interfaces are preferred over sprawling files, without breaking apart naturally cohesive logic.
- **Prose & Research Markdown**: Focus on provenance, clear separation of source evidence vs. interpretation, lifecycle differences, navigation, reviewability, reuse, argument continuity, and clear boundaries between teaching/curriculum and research synthesis.
- **LOC is a weak signal for Markdown**: Syntheses, specification mappings, and reference indices frequently benefit from contiguous reading and unbroken internal links. Arbitrary segmentation based solely on line count harms context and readability.

## Recognized Exceptions

The 600-line heuristic signal does not mechanically apply to:
- Auto-generated artifacts, schemas, or compilation targets
- Vendor libraries and third-party imports
- Lockfiles (`package-lock.json`, etc.)
- Test fixtures, test matrices, and raw dataset files
- Self-contained narrative specifications or monolithic source transcripts where external slicing harms provenance

## Temporary Mitigation Discipline

When temporary mitigations are introduced (such as a temporary freeze, no-growth policy, or migration hold on an artifact):
- They should concisely state why they exist and what specific fact, event, or phase milestone triggers their reevaluation or retirement.
- They must not silently harden into permanent restrictions once their triggering condition has been resolved.
- Do not create a state machine or new tracker for temporary rules.

---

## Legacy Aggregate: `docs/research/source-native-knowledge-index.md` (~1,356 lines)

- **Status & Nature**: Legacy aggregate containing source-native evidence for Shah, The PBR Guide, Dinur, and RTR4 (Batches 1–4) with recognized structural risk due to size and multi-source accumulation.
- **Placement & Evolution Guidance**:
  - Factual corrections, maintenance, and task-required local changes are allowed normally.
  - Avoid default continued accumulation of new independent source batches into this file.
  - The previous temporary restriction ("until a dedicated artifact-placement decision was completed and Browser-reviewed") has been satisfied by the accepted Gate 2.5A placement decision at `2c141474167b3053abb5277680443a994ca491a5`. The strict temporary freeze is retired in favor of directing new source-native batches to independent leaf artifacts.
  - If future significant expansion or reorganization is actually needed, choose placement pragmatically based on the live task and current repository topology.
  - **No migration of Batches 1–4** is authorized by this Work Unit; historical content remains in place.

---

## Current Gate 2.5A Placement Decision / Default Layout

Starting with Batch 5, the accepted default layout places new source-native evidence into independent leaf artifacts under `docs/research/source-native/`.

### Default Mapping for Upcoming Source Batches

- **Batch 5 Painter**: `docs/research/source-native/adobe-painter-official.md`
- **Batch 6 Designer**: `docs/research/source-native/adobe-designer-official.md`
- **Batch 7 Sampler**: `docs/research/source-native/adobe-sampler-official.md`
- **Batch 8 Blender**: `docs/research/source-native/blender-official.md`
- **Batch 9 OpenPBR**: `docs/research/source-native/openpbr-specification.md`

*(Note: This specifies the default placement schema for upcoming batches; it does not authorize starting future batches early.)*

### Pragmatic Boundaries vs. Invariants

- This default layout does **not** establish a universal invariant that "one source batch = one file".
- A small or closely related source may share an artifact in future work, whereas a large or complex source may later warrant multiple artifacts if live evidence and reviewability support it.
- The current mapping remains the accepted default for present Gate 2.5A work, keeping review boundaries localized and preventing context bloat.
- **No historical migration**: Existing Shah, The PBR Guide, Dinur, and RTR4 evidence remains in `docs/research/source-native-knowledge-index.md`.
- **Minimal overhead**: No root manifest, YAML registry, or synthetic aggregate generation is required.
