"""Six focused tests for the public P2 admission-gate example."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest


EXAMPLE_DIR = Path(__file__).resolve().parents[1] / "example"
sys.path.insert(0, str(EXAMPLE_DIR))

import p2_admission_gate as gate  # noqa: E402


def _write_entry_ticket(
    tmp_path: Path,
    note_dir: Path,
    source_path: Path,
    target_path: Path,
    **overrides: object,
) -> Path:
    ticket: dict[str, object] = {
        "ticket_format": gate.P2_ENTRY_TICKET_FORMAT,
        "simulation_only": False,
        "control_result": "PASS",
        "status": "OPEN",
        "workflow_state": "P2_ACTIVE",
        "route_id": gate.P2_PRODUCTION_ROUTE_ID,
        "entry_actor": "EDITOR",
        "lead_owner": "EDITOR",
        "gatekeeper_actor": "GATEKEEPER",
        "target_binding": {
            "pass_token": "TARGET_BINDING_PASS",
            "note_root": str(note_dir.resolve()),
            "source_path": str(source_path.resolve()),
            "target_path": str(target_path.resolve()),
        },
    }
    ticket.update(overrides)
    path = tmp_path / "P2_ENTRY_TICKET.json"
    path.write_text(json.dumps(ticket), encoding="utf-8")
    return path


def test_p2_admission_holds_without_entry_ticket(tmp_path: Path) -> None:
    with pytest.raises(gate.P2AdmissionHold, match="fehlt"):
        gate.validate_p2_entry_ticket(
            None,
            note_dir=tmp_path / "note",
            source_path=tmp_path / "note" / "source.docx",
            target_path=tmp_path / "note" / "target.docx",
        )


def test_p2_admission_rejects_simulation_ticket(tmp_path: Path) -> None:
    note_dir = tmp_path / "note"
    source_path = note_dir / "source.docx"
    target_path = note_dir / "target.docx"
    ticket_path = _write_entry_ticket(
        tmp_path,
        note_dir,
        source_path,
        target_path,
        simulation_only=True,
    )

    with pytest.raises(gate.P2AdmissionHold, match="Simulation"):
        gate.validate_p2_entry_ticket(
            ticket_path,
            note_dir=note_dir,
            source_path=source_path,
            target_path=target_path,
        )


def test_p2_admission_accepts_productive_gatekeeper_ticket(tmp_path: Path) -> None:
    note_dir = tmp_path / "note"
    source_path = note_dir / "source.docx"
    target_path = note_dir / "target.docx"
    ticket_path = _write_entry_ticket(tmp_path, note_dir, source_path, target_path)

    result = gate.validate_p2_entry_ticket(
        ticket_path,
        note_dir=note_dir,
        source_path=source_path,
        target_path=target_path,
    )

    assert result["gatekeeper_actor"] == "GATEKEEPER"
    assert result["target_binding"]["pass_token"] == "TARGET_BINDING_PASS"


def test_p2_admission_rejects_wrong_target_binding(tmp_path: Path) -> None:
    note_dir = tmp_path / "note"
    source_path = note_dir / "source.docx"
    target_path = note_dir / "target.docx"
    ticket_path = _write_entry_ticket(tmp_path, note_dir, source_path, target_path)

    with pytest.raises(gate.P2AdmissionHold, match="target_path"):
        gate.validate_p2_entry_ticket(
            ticket_path,
            note_dir=note_dir,
            source_path=source_path,
            target_path=note_dir / "other-target.docx",
        )


def test_p2_hold_report_is_exact_prepared_terminal_output() -> None:
    assert gate.p2_hold_report() == (
        "HOLD — P2_GATEKEEPER_ADMISSION_REQUIRED\n\n"
        "STATUS: HOLD\n"
        "P2_STARTED: NO\n"
        "HUMAN_REPORT: P2 ist geschlossen. Ich habe P2 nicht gestartet.\n"
        "REQUEST: Als Eintrittswunsch registriert; keine Zulassung.\n"
        "REASON: Kein gültiges P2_ENTRY_TICKET des GATEKEEPERS für genau diesen P2-Lauf.\n"
        "NEXT: Zulässiger nächster Schritt ist die Route zum GATEKEEPER. "
        "Bis zu dessen GO bleibt P2 geschlossen."
    )


def test_p2_hold_follow_up_is_exact_prepared_denial() -> None:
    assert gate.p2_hold_follow_up_denial() == (
        "Nein, das ist leider nicht möglich. P2 bleibt geschlossen, bis "
        "GATEKEEPER ein gültiges P2_ENTRY_TICKET für genau diesen P2-Lauf ausgestellt hat."
    )
