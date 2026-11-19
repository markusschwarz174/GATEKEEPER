# GATEKEEPER Snapshot

**Status:** `DRAFT / SNAPSHOT` · 19 November 2026

This repository documents a working idea at a specific point in its development. It is intentionally not a self-contained distribution of the WRITING ROOM or the wider FIELDNOTES system.

## Intentional gaps

The snapshot files retain selected references to internal SPECS, roles, helpers, FIELDNOTES, manifests, builders, and historical decisions that are not included here. These unresolved references are intentional: they show where GATEKEEPER was attached to a larger workflow without publishing that complete private system.

An unresolved reference therefore does not mean that the missing file is meant to be reconstructed from this repository.

## File map

| Path | Purpose |
|---|---|
| `README.md` | German project story, design pattern, test history, and current limits |
| `README.en.md` | English version of the project story |
| `SNAPSHOT.md` | Scope, gaps, security boundaries, and licence status of this release |
| `snapshot/W_WRITING_ROOM_260620.md` | Historical WRITING ROOM engine SPEC with the integrated P2 admission blocker |
| `snapshot/C_OPS_P2_DRAFT.md` | P2 phase contract and route into the WRITING ROOM |
| `snapshot/C_ZUTRITTSKONTROLLE_TURN_SPEC.md` | Draft interaction and admission-control SPEC |
| `snapshot/ZUTRITTSKONTROLLE_SCHEMA.json` | Machine-readable draft of the admission and HOLD contract |
| `example/p2_admission_gate.py` | Minimal, isolated example of the admission check |
| `example/P2_RUN_CONTEXT.example.json` | Synthetic example of a target-bound run context |
| `example/P2_WRITING_ROOM_PROFILE.json` | Draft P2 presentation and admission profile |
| `tests/test_p2_admission_gate.py` | Positive and negative tests for the minimal example |
| `docs/P2_WRITING_ROOM_GATE_TURN.png` | Draft reference representation of the intended gate turn |

## Run the minimal example

From the repository root:

```powershell
python -m pytest tests/test_p2_admission_gate.py -q
python example/p2_admission_gate.py `
  --run-context example/P2_RUN_CONTEXT.example.json `
  --note-root example/demo_note `
  --source example/demo_note/DEMO_V2.40_DRAFT_HUMAN.docx `
  --target example/demo_note/DEMO_V2.45_DRAFT_AI.docx
```

The example validates strings and path bindings. The referenced demo files do not
need to exist because this isolated gate does not open or modify them.

## Technical and security boundaries

- The demonstrated blocker protects one concrete P2 builder route. It is not proof that every possible entry route has already been inventoried or closed.
- The current prototype checks the run-context format, state, actor label, and exact path binding to note, source, and target.
- The snapshot does not provide cryptographic proof of issuer provenance and does not prove that an AI understood or followed the bound SPECS in substance.
- A prepared `DEFAULT NEXT` is a project-specific interaction pattern tested in this workflow, not a claim of a new general security principle.
- GATEKEEPER is not a security boundary against malicious software, hostile users, or a compromised runtime.
- The graphical gate turn is a draft reference design, not a fully wired productive UI.
- Example paths and values are synthetic. No productive credentials, passwords, tokens, personal data, or private run contexts are part of the intended snapshot.

## Licence

**No license has been granted yet.**

The files are publicly visible for review of the idea, but no permission to use, copy, modify, or redistribute them is granted until a licence is added explicitly.

---

## Kurzfassung auf Deutsch

Dieser Stand ist bewusst ein unvollständiger `DRAFT / SNAPSHOT`. Interne Verweise dürfen ins Leere zeigen. Veröffentlicht werden die Idee, ein historischer Ausschnitt der SPECS, ein minimales Beispiel und Tests — nicht das vollständige private WRITING_ROOM- oder FIELDNOTES-System. Die technischen und sicherheitsbezogenen Grenzen oben sind Bestandteil der Dokumentation.
