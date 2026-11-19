"""Minimal P2 admission gate extracted from the WRITING_ROOM prototype.

This example demonstrates a contractual fail-closed gate:

* a P2 run starts only with an explicitly productive run context;
* the context must declare the permitted route and issuer role;
* it must be bound to the exact note root, source path, and target path;
* missing or invalid admission produces a prepared terminal HOLD report.

Prototype boundary
------------------
This is not a security boundary. The JSON fields are contract assertions. The
prototype has no signature or authenticated issuer provenance, no content-hash
binding for source files, and no replay protection. A process with write access
can forge a structurally valid context. Production use therefore requires an
external trusted issuer and stronger provenance controls.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


class P2AdmissionHold(Exception):
    """Raised when P2 admission is missing, invalid, or not productively bound."""


P2_RUN_CONTEXT_FORMAT = "P2_RUN_CONTEXT_V1"
P2_PRODUCTION_ROUTE_ID = "FIELDNOTES.P2.WRITING_ROOM"

P2_HOLD_REPORT = """HOLD — P2_GATEKEEPER_ADMISSION_REQUIRED

STATUS: HOLD
P2_STARTED: NO
HUMAN_REPORT: P2 ist geschlossen. Ich habe P2 nicht gestartet.
REQUEST: Als Eintrittswunsch registriert; keine Zulassung.
REASON: Kein verifizierter produktiver P2_RUN_CONTEXT von OPTOR/GATEKEEPER.
NEXT: Zulässiger nächster Schritt ist die Aktivierung von OPTOR/GATEKEEPER für die Zutrittsprüfung. Bis zu dessen GO bleibt P2 geschlossen."""

P2_HOLD_FOLLOW_UP_DENIAL = (
    "Nein, das ist leider nicht möglich. P2 bleibt geschlossen, bis "
    "OPTOR/GATEKEEPER einen verifizierten produktiven P2_RUN_CONTEXT ausgestellt hat."
)

PROTOTYPE_LIMITATIONS = (
    "no signature or authenticated issuer provenance",
    "no content-hash binding",
    "no replay protection",
)


def p2_hold_report() -> str:
    """Return the prepared terminal HUMAN report without further problem-solving."""

    return P2_HOLD_REPORT


def p2_hold_follow_up_denial() -> str:
    """Return the prepared response to attempts to override HOLD in natural language."""

    return P2_HOLD_FOLLOW_UP_DENIAL


def _resolve_declared_path(raw: str, *, context_dir: Path) -> Path:
    """Resolve a declared path; relative example paths are based on the JSON file."""

    declared = Path(raw)
    if not declared.is_absolute():
        declared = context_dir / declared
    return declared.resolve()


def validate_p2_run_context(
    run_context_path: Path | None,
    *,
    note_dir: Path,
    source_path: Path,
    target_path: Path,
) -> dict[str, Any]:
    """Validate a pre-existing contractual P2 admission without mutating files.

    The function only reads and validates the context. It never creates,
    completes, repairs, or upgrades admission. Relative paths inside the JSON
    are resolved from the directory containing that JSON document.
    """

    if run_context_path is None:
        raise P2AdmissionHold("P2_RUN_CONTEXT fehlt")

    context_path = Path(run_context_path)
    if not context_path.is_absolute():
        context_path = Path.cwd() / context_path
    context_path = context_path.resolve()
    if not context_path.is_file():
        raise P2AdmissionHold(f"P2_RUN_CONTEXT nicht gefunden: {context_path}")

    try:
        context = json.loads(context_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise P2AdmissionHold(f"P2_RUN_CONTEXT nicht lesbar/ungültig: {exc}") from exc

    if not isinstance(context, dict):
        raise P2AdmissionHold("P2_RUN_CONTEXT muss ein JSON-Objekt sein")
    if context.get("context_format") != P2_RUN_CONTEXT_FORMAT:
        raise P2AdmissionHold(f"context_format muss {P2_RUN_CONTEXT_FORMAT} sein")
    if context.get("simulation_only") is not False:
        raise P2AdmissionHold("Simulations-/Testkontext ist produktiv verboten")
    if context.get("control_result") != "PASS":
        raise P2AdmissionHold("control_result ist nicht PASS")
    if context.get("status") != "OPEN":
        raise P2AdmissionHold("Run-Context ist nicht OPEN")
    if context.get("workflow_state") != "P2_ACTIVE":
        raise P2AdmissionHold("workflow_state ist nicht P2_ACTIVE")
    if context.get("route_id") != P2_PRODUCTION_ROUTE_ID:
        raise P2AdmissionHold("route_id ist keine produktive P2-WRITING_ROOM-Route")
    if context.get("entry_actor") != "EDITOR" or context.get("lead_owner") != "EDITOR":
        raise P2AdmissionHold("P2-LEAD ist nicht eindeutig an EDITOR übergeben")

    gatekeeper_actor = context.get("gatekeeper_actor")
    if gatekeeper_actor not in {"OPTOR", "DIRECTOR_OVERRIDE"}:
        raise P2AdmissionHold("Zulassung deklariert weder OPTOR noch DIRECTOR_OVERRIDE")
    if gatekeeper_actor == "DIRECTOR_OVERRIDE" and context.get("override_explicit") is not True:
        raise P2AdmissionHold("DIRECTOR_OVERRIDE ist nicht ausdrücklich protokolliert")

    binding = context.get("target_binding")
    if not isinstance(binding, dict) or binding.get("pass_token") != "TARGET_BINDING_PASS":
        raise P2AdmissionHold("TARGET_BINDING_PASS fehlt")

    expected_paths = {
        "note_root": Path(note_dir).resolve(),
        "source_path": Path(source_path).resolve(),
        "target_path": Path(target_path).resolve(),
    }
    for field, expected in expected_paths.items():
        raw = binding.get(field)
        if not isinstance(raw, str) or not raw.strip():
            raise P2AdmissionHold(f"target_binding.{field} fehlt")
        actual = _resolve_declared_path(raw, context_dir=context_path.parent)
        if actual != expected:
            raise P2AdmissionHold(
                f"target_binding.{field} stimmt nicht mit diesem Lauf überein"
            )

    return context


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-context", type=Path, required=True)
    parser.add_argument("--note-root", type=Path, required=True)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--target", type=Path, required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        validate_p2_run_context(
            args.run_context,
            note_dir=args.note_root,
            source_path=args.source,
            target_path=args.target,
        )
    except P2AdmissionHold:
        print(p2_hold_report(), file=sys.stderr)
        return 2

    print("GO — P2_GATEKEEPER_ADMISSION_VERIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
