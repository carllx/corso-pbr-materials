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

## Teacher Preparation Views, PPT Production, and Change Propagation

The course repository uses several artifacts because they serve different audiences and validation duties. Efficiency comes from controlling **authority and propagation**, not from forcing every artifact to be textually unique.

### Authority and presentation responsibilities

- **Teaching Evidence Map**: authority for evidence routing, coverage/gap status, and source/decision boundaries. It is not the teacher's day-to-day preparation dashboard.
- **Executable Teaching Package**: authority for the weekly teaching contract: outcomes, protected/cuttable core, activity order and plan budget, teacher/student actions, evidence requirements, answer boundaries, recovery, and runtime gates.
- **Student Handout**: authority for what students actually read, fill in, operate, and submit. Its task semantics must remain compatible with the Teaching Package.
- **PPT + embedded Presenter Notes**: the single classroom presentation artifact. Visible slides own page-level expression, visuals, reveal order, and activity prompts. Notes own page-level speaking cues, transitions, misconceptions, demo cues, and necessary pointers.
- **Teacher discussion view / prototype copy**: no authority. It is a rebuildable projection of current authorities for a specific discussion or validation question.

Literal duplication is sometimes necessary for usability. The invariant is that duplicated rules must have one clear owner and must not become independently maintained policy.

### No fifth teaching SSOT

Do not create a long-lived Teacher Preparation Spine, parallel Notes document, YAML/JSON curriculum database, or other registry solely to reduce teacher reading load unless live evidence demonstrates that the additional system reduces net maintenance cost.

A temporary teacher view is allowed only when it:
- can be regenerated from existing authority artifacts;
- identifies the source revision it reflects;
- contains no unique decision or policy;
- is overwritten or discarded when its validation purpose is complete.

If unique content accumulates in the temporary view, first move that content to the correct authority before continuing.

### Decision-driven preparation loop

Use this loop for lesson preparation and revisions:

1. **Locate the authority** for the proposed change.
2. **Make or obtain the teaching decision** at the correct authority boundary.
3. **Choose the cheapest adequate validation** for the uncertainty:
   - structure/order -> a compact block view or short walkthrough;
   - student task wording/evidence -> the real Handout;
   - software interaction -> the real Starter/Recovery asset;
   - visual discrimination -> the real reference image or verified screenshot;
   - page flow/explanation -> a few rough slides or a page sequence.
4. **Propagate the accepted decision immediately** to affected consumers.
5. **Revalidate only the affected chain** unless the change alters the full lesson architecture.

Do not require two complete review meetings, a complete rough deck, or a fixed number of prototype rounds when a narrower test can answer the live question.

### Prototype fidelity follows the risk

Low cost does not mean fake content.

- Keep decoration, typography polish, animation, and nonessential image hunting low fidelity until the teaching structure is stable enough for production.
- Use **real** or already verified material early whenever the material itself is part of the learning task, evidence, or operation: software controls, important reference images, observation contrasts, task prompts, file/recovery behavior.
- A prototype may be disposable or may evolve into the final deck, but there must be only **one active editable slide lineage**. Do not maintain separate prototype and final decks in parallel.

### Markdown Slide Draft as the low-cost visual prototype

When a slide prototype is useful, the preferred default is a lightweight Markdown draft that remains part of the **single active PPT production lineage**, not a fifth curriculum authority.

Use the minimum semantic structure:

```md
# <slide title>

## Visible
What students should actually see/read.

## Visual
status: READY | TODO | LIVE
type: observation-reference | runtime-screenshot | conceptual-diagram | navigation | live-demo

<embedded image, concrete visual requirement, or live-demo instruction>

## Notes
Page-level teacher speaking/transition/demo cues only.

## Trace
P: <Teaching Package block/section>
H: <Handout task/step if applicable>
E: <Evidence Map KU if applicable>
```

Rules:
- **READY**: the real/verified image exists and should be embedded directly in Markdown with a repository-relative or otherwise controlled path.
- **TODO**: the image does not yet exist; specify what must be visible, the intended source, and any truthfulness constraint. Do not use vague "image here" placeholders for load-bearing visuals.
- **LIVE**: the correct teaching move is to switch to the real software/demo rather than fabricate a static slide image. The slide may simply hold the student attention state or action instruction.
- Use real or verified visuals early for software controls, observation judgments, material comparisons, recovery behavior, and other visuals that are themselves part of the learning input or evidence. AI-generated or decorative imagery must not impersonate runtime/UI/evidence.
- Annotated PNG/SVG derived from a real screenshot/reference is acceptable when labels, arrows, crops, or callouts are needed. The annotation should clarify the verified source rather than recreate it from imagination.
- The draft may contain multiple page types: **Concept**, **Observation**, **Activity**, and **Live Demo / Hold**. Do not force every block into a title-plus-bullets lecture layout, and do not require every Teaching Package block to have a dedicated slide.
- Markdown is the cheapest review surface, not a commitment to Marp, Slidev, Quarto, or any final renderer. Tool choice for the production deck should be delayed until the visual/layout needs justify it.
- Once the Production Gate is passed, either evolve this draft into the single final slide-editing lineage or deliberately hand it off to the chosen production source. Do not maintain a parallel Markdown truth and independently edited final deck without a clear one-way ownership transition.

### Production gate vs. go-live gate

A lesson may enter final PPT/Notes production when:
- protected learning requirements and student tasks are understood well enough that no known dispute would change the page/task architecture;
- the representative high-risk task path has been walked using the actual student/asset materials relevant to that path;
- the teacher can account for the major see/listen/do/fill/submit transitions and identify remaining timing assumptions as plan estimates;
- the relevant Teaching Package, Handout, critical visuals/assets, and known pointers belong to the same revision.

This gate authorizes production effort only. It does **not** establish classroom readiness. Existing runtime, delivery, submission, rehearsal, accessibility, and field-validation gates remain independent.

### Minimal change-propagation model

Agents should classify a change by meaning, then update only semantically dependent artifacts:

| Change type | Owning location | Typical dependent consumers | Minimum revalidation |
| --- | --- | --- | --- |
| Teaching decision: add/remove/deepen a concept, task, outcome, evidence requirement | Project Authority and/or Teaching Package | Handout; related PPT/Notes; Evidence Map only if evidence/decision boundary changes; code/assets only when their behavior/assertions depend on the decision | Student can still produce intended evidence; timing/recovery still coherent |
| Timing/order/cut/recovery | Teaching Package | Notes pacing; Handout step/recovery wording; PPT reveal/transition order; Evidence Map pointers when block anchors change | Affected block plus its entry/exit transitions |
| Implementation: control name, parameter, path, asset/version | Asset/code + Teaching Package interface text | Handout operation; related screenshots/PPT/Notes; source/version pointers when applicable | Real operation, save/reopen/recovery path affected by the change |
| Presentation-only: layout, crop, equivalent phrasing, typography | Active PPT/Notes editing source | Usually none | Projected readability and unchanged meaning/reveal order |
| Evidence/source correction | Evidence Map / verified source pointer | Only consumers that use the corrected claim; related assertions | Claim-pointer consistency plus affected teaching fragment |
| Validation-state change | Existing gate/evidence location in Teaching Package or tracker | Operational hints/fallbacks in Handout/Notes when affected | Corrected runtime/delivery path; unrelated validation remains valid |

For each accepted substantive change, the Agent should leave a short review trace in the active Issue/PR or commit message containing:
**decision/status | semantic change | affected artifacts | deliberately unchanged artifacts + why | evidence requiring revalidation**.

### Cross-agent repository reconciliation

Browser-side and IDE-side repository mutations are allowed, but each mutation creates a potential dependency event for other active work.

- A Browser repository change should use an explicit branch/PR or otherwise expose a concrete ref; do not rely on chat memory as the synchronization mechanism.
- Every active IDE/Browser mission should retain its starting/base SHA. Before final delivery, compare that base and its authority inputs against newer relevant refs.
- If another active Work Unit changed overlapping authority or dependent artifacts, fetch/compare and reconcile before declaring the mission complete, even when Git reports no textual conflict.
- **No textual conflict != no semantic drift.** A stale branch can remain mechanically mergeable while implementing superseded teaching rules.
- Ordinary non-fast-forward protection prevents some direct overwrites, but it does not protect against stale branches, generated-file replacement, semantic regressions, or unqualified force pushes.
- Avoid `git push --force` for shared work. If history repair is genuinely required, use an explicit lease/expected-head discipline and first inspect the remote head.
- The human should authorize meaning and direction, not manually transport commits between agents. Agents should communicate concrete refs and perform the reconciliation themselves.

### Supersession and retirement discipline

When a newer teacher decision replaces an older project choice:
- mark the older choice as superseded in the current Issue/PR or edit the owning authority so only one active rule remains;
- remove obsolete downstream wording and stale pointers rather than preserving competing variants;
- do not rewrite historical audit reports merely to hide that a prior decision once existed;
- keep unresolved proposals explicitly non-authoritative until accepted.

Current teacher-preparation decisions should live in the active project authority plus these durable Agent rules; they should not be copied into an additional teaching manual.

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
