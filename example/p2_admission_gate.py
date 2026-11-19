"""Minimal P2 admission gate extracted from the WRITING_ROOM prototype.

This example demonstrates a contractual fail-closed gate:

* a P2 run starts only with an explicitly productive entry ticket;
* the ticket must declare the permitted route and issuer role;
* it must be bound to the exact note root, source path, and target path;
* missing or invalid admission produces a prepared terminal HOLD report.

Prototype boundary
------------------
This is not a security boundary. The JSON fields are contract assertions. The
prototype has no signature or authenticated issuer provenance, no content-hash
binding for source files, and no replay protection. A process with write access
can forge a structurally valid ticket. Production use therefore requires an
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


P2_ENTRY_TICKET_FORMAT = "P2_ENTRY_TICKET_V1"
P2_PRODUCTION_ROUTE_ID = "FIELDNOTES.P2.WRITING_ROOM"

P2_HOLD_REPORT = """HOLD — P2_GATEKEEPER_ADMISSION_REQUIRED

STATUS: HOLD
P2_STARTED: NO
HUMAN_REPORT: P2 ist geschlossen. Ich habe P2 nicht gestartet.
REQUEST: Als Eintrittswunsch registriert; keine Zulassung.
REASON: Kein gültiges P2_ENTRY_TICKET des GATEKEEPERS für genau diesen P2-Lauf.
NEXT: Zulässiger nächster Schritt ist die Route zum GATEKEEPER. Bis zu dessen GO bleibt P2 geschlossen."""

P2_HOLD_FOLLOW_UP_DENIAL = (
    "Nein, das ist leider nicht möglich. P2 bleibt geschlossen, bis "
    "GATEKEEPER ein gültiges P2_ENTRY_TICKET für genau diesen P2-Lauf ausgestellt hat."
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


def _resolve_declared_path(raw: str, *, ticket_dir: Path) -> Path:
    """Resolve a declared path; relative example paths are based on the JSON file."""

    declared = Path(raw)
    if not declared.is_absolute():
        declared = ticket_dir / declared
    return declared.resolve()


def validate_p2_entry_ticket(
    entry_ticket_path: Path | None,
    *,
    note_dir: Path,
    source_path: Path,
    target_path: Path,
) -> dict[str, Any]:
    """Validate a pre-existing contractual P2 admission without mutating files.

    The function only reads and validates the ticket. It never creates,
    completes, repairs, or upgrades admission. Relative paths inside the JSON
    are resolved from the directory containing that JSON document.
    """

    if entry_ticket_path is None:
        raise P2AdmissionHold("P2_ENTRY_TICKET fehlt")

    ticket_path = Path(entry_ticket_path)
    if not ticket_path.is_absolute():
        ticket_path = Path.cwd() / ticket_path
    ticket_path = ticket_path.resolve()
    if not ticket_path.is_file():
        raise P2AdmissionHold(f"P2_ENTRY_TICKET nicht gefunden: {ticket_path}")

    try:
        ticket = json.loads(ticket_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise P2AdmissionHold(f"P2_ENTRY_TICKET nicht lesbar/ungültig: {exc}") from exc

    if not isinstance(ticket, dict):
        raise P2AdmissionHold("P2_ENTRY_TICKET muss ein JSON-Objekt sein")
    if ticket.get("ticket_format") != P2_ENTRY_TICKET_FORMAT:
        raise P2AdmissionHold(f"ticket_format muss {P2_ENTRY_TICKET_FORMAT} sein")
    if ticket.get("simulation_only") is not False:
        raise P2AdmissionHold("Simulations-/Testticket ist produktiv verboten")
    if ticket.get("control_result") != "PASS":
        raise P2AdmissionHold("control_result ist nicht PASS")
    if ticket.get("status") != "OPEN":
        raise P2AdmissionHold("Entry-Ticket ist nicht OPEN")
    if ticket.get("workflow_state") != "P2_ACTIVE":
        raise P2AdmissionHold("workflow_state ist nicht P2_ACTIVE")
    if ticket.get("route_id") != P2_PRODUCTION_ROUTE_ID:
        raise P2AdmissionHold("route_id ist keine produktive P2-WRITING_ROOM-Route")
    if ticket.get("entry_actor") != "EDITOR" or ticket.get("lead_owner") != "EDITOR":
        raise P2AdmissionHold("P2-LEAD ist nicht eindeutig an EDITOR übergeben")

    gatekeeper_actor = ticket.get("gatekeeper_actor")
    if gatekeeper_actor not in {"GATEKEEPER", "DIRECTOR_OVERRIDE"}:
        raise P2AdmissionHold("Zulassung stammt weder vom GATEKEEPER noch aus DIRECTOR_OVERRIDE")
    if gatekeeper_actor == "DIRECTOR_OVERRIDE" and ticket.get("override_explicit") is not True:
        raise P2AdmissionHold("DIRECTOR_OVERRIDE ist nicht ausdrücklich protokolliert")

    binding = ticket.get("target_binding")
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
        actual = _resolve_declared_path(raw, ticket_dir=ticket_path.parent)
        if actual != expected:
            raise P2AdmissionHold(
                f"target_binding.{field} stimmt nicht mit diesem Lauf überein"
            )

    return ticket


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--entry-ticket", type=Path, required=True)
    parser.add_argument("--note-root", type=Path, required=True)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--target", type=Path, required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        validate_p2_entry_ticket(
            args.entry_ticket,
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
