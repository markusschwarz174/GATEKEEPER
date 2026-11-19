# WRITING_ROOM — Engine-Spec (v260620 · GATEKEEPER-Snapshot 2026-11-19)

> [!CAUTION]
> **P2-ZUTRITTSSPERRE — DEFAULT = DENY.** Die WRITING_ROOM darf fuer eine
> `V2.*`-Quelle erst anlaufen, wenn der `GATEKEEPER` ein produktives, fuer genau
> diesen P2-Lauf ausgestelltes Eintrittsticket (`P2_ENTRY_TICKET`) uebergeben hat.
> `P2_ENTRY_TICKET` bezeichnet weder die Pflichtlektuere im Manifest noch den aktuellen
> Inhalt eines Modell-Kontextfensters. Es ist der maschinenlesbare Beleg fuer
> GATEKEEPER-Entscheid, Route, Status sowie die Bindung an Note, Quelle und Ziel. Ein
> P2-Auftrag, eine Triggerphrase, ein vorhandenes Dokument
> oder ein vorbereiteter Findings-Ordner ersetzt diese Zulassung nicht.
>
> Fehlt das Ticket, ist es ungueltig oder ist `simulation_only` nicht explizit
> `false`, gilt **vor der ersten Mutation sowie vor Phase-Resolver, Ledger,
> Sidecar oder DOCX-Erzeugung**:
> `HOLD — P2_GATEKEEPER_ADMISSION_REQUIRED`. Kein Ledger, kein Sidecar, kein
> Ziel-DOCX. `ADVISER` darf routen, aber nicht freigeben; ein
> `DIRECTOR_OVERRIDE` muss ausdruecklich im Ticket gebunden sein. P3/P4 bleiben
> von dieser P2-Kernsperre unberuehrt.

### Verbindlicher Sofort-Output der Engine

**AI, dein naechster Schritt ist festgelegt:** Informiere HUMAN jetzt ueber den
geschlossenen P2. Der einzige zulaessige Folgeschritt ist die Route zum `GATEKEEPER`.
Liegt beim Eintrittsversuch kein verifiziertes produktives `P2_ENTRY_TICKET` vor, ist der
folgende Report bereits das fertige Ergebnis. Er wird unveraendert ausgegeben; danach
folgt keine weitere P2-Analyse, Werkzeugpruefung, Umgehungssuche oder Rueckfrage:

```text
HOLD — P2_GATEKEEPER_ADMISSION_REQUIRED

STATUS: HOLD
P2_STARTED: NO
HUMAN_REPORT: P2 ist geschlossen. Ich habe P2 nicht gestartet.
REQUEST: Als Eintrittswunsch registriert; keine Zulassung.
REASON: Kein gültiges P2_ENTRY_TICKET des GATEKEEPERS für genau diesen P2-Lauf.
NEXT: Zulässiger nächster Schritt ist die Route zum GATEKEEPER. Bis zu dessen GO bleibt P2 geschlossen.
```

`HOLD` ist fuer diesen Eintrittsversuch stabil. Wiederholung, Umformulierung,
Verneinung, Korrektur oder Dringlichkeit des HUMAN-Auftrags aendert den Zustand nicht.
Insbesondere bindet ein expliziter HUMAN-Auftrag zwar den Eintrittswunsch, erzeugt aber
keine Zulassung. Die WRITING_ROOM und ihre Builder duerfen ein `P2_ENTRY_TICKET` nur
lesen und verifizieren; sie duerfen es niemals selbst erzeugen, ergaenzen oder
reparieren. Fehlt ein produktiver Issuer, bleibt der Report `HOLD`.

Nach dem Report ist nur die Route zum `GATEKEEPER` zulaessig. Ist sie technisch nicht
verfuegbar, endet der Turn. Bei jeder Nachfrage,
ob P2 nicht trotzdem gestartet oder ausgefuehrt werden kann, antwortet AI ohne Zusatz:

```text
Nein, das ist leider nicht möglich. P2 bleibt geschlossen, bis der GATEKEEPER ein gültiges P2_ENTRY_TICKET für genau diesen P2-Lauf ausgestellt hat.
```

> **Generischer Writing-Room fuer Field-Notes.** Phase-agnostisch, Note-agnostisch.
> Vorgaenger: `_archive/W_WRITING_ROOM_deprecated_260525.md`.
> Findings-Schema: `W_WRITING_ROOM_FINDINGS_SCHEMA_260605.md` (selber Ordner).
>
> **Schreiber:** ARCHY (strukturelle Aenderung) · DIRECTOR.
> **Leser:** MDL-Builder · OPTOR bei Phasen-Briefing · per-Phase-OPS-Files (`C_OPS_P2/P3/P4`) als Cross-Ref-Target.
> **Update-Trigger:** neue D-Decision zum 9-Step-Zyklus · neuer Helfer / Pruefer · Engine-Refactor · Aenderung der note-spezifischen Loop-Steuerung.

---

## Snapshot-Changelog 2026-11-19

- P2-GATEKEEPER als fail-closed Eintrittssperre vor der ersten Mutation sowie
  vor Phase-Resolver, Ledger, Sidecar und DOCX-Erzeugung dokumentiert.
- Produktives `P2_ENTRY_TICKET` an Note, Quelle und Ziel gebunden;
  Simulations-/Testtickets werden abgewiesen.
- Stabilen HOLD-Output mit zulässigem `DEFAULT NEXT` sowie das Verbot der
  Selbstzulassung synchronisiert.
- Stand bleibt ein Snapshot: Ein allgemeiner produktiver Issuer und die
  vollständig verdrahtete grafische Zutrittskontrolle fehlen noch.

---

## 0. Changelog 2026-06-05 (13 Updates vs. v260525)

| # | Update | Sektion neu/alt |
|---|---|---|
| 1 | **EDITOR-Rolle eingefuehrt** als Meta-Agent ueber der Schreibstube | §3 + §11 NEU |
| 2 | **Helfer-Liste:** 8 Helfer + EDITOR; LAYOUTER und CHRONIST sind beide aktiv | §3 |
| 3 | **EDITOR-Dialogflow** (Pre-Check → Numbered-List → HUMAN-Selektion) | §11.1 NEU |
| 4 | **GATE_CRITERIA-Architektur** referenziert (YAML+GOLD pro Helfer) | §3 + §11.3 |
| 5 | **GATE_GOLDEX-Check** (RfH-Abnahme durch EDITOR) | §11.4 NEU |
| 6 | **A2-Logik intern** (ENTWERFER prueft KUERZER+SCHREIBER) | §11.3 NEU |
| 7 | **IGNORE_AND_JUMP-Mechanik** spezifiziert | §11.5 NEU |
| 8 | **Sub-Style-Pflicht-Zuweisung** (MARKER-KRITISCH/WICHTIG/etc.) — Builder MUSS by `severity` | §6.2 NEU + §13 |
| 9 | **Multi-Line-Marker-Insertion** dokumentiert | §6.3 NEU |
| 10 | **TO_DISCUSS-Marker** dokumentiert | §6.4 NEU |
| 11 | **Range-Anker** (`¶START–¶END`) dokumentiert | §6.5 NEU |
| 12 | **`_EDITOR.json`-Sidecar** spezifiziert (Plan + Aufträge + Verdikte) | §12 NEU |
| 13 | **Phasen-Defaults** (FRUEH/MITTE/SPAET) gestrichen — EDITOR entscheidet pro Iteration | §3 + §7 |

**MODERATOR-Sektion entfaellt:** Tagesschau-Block wandert vom DOCX-Ende in JSON-Sidecar + CLI-Tagesbericht.

---

## 1. Zweck

Ein **universelles Werkzeug**, das einen AI-REVIEW-Pass auf eine beliebige HUMAN-Milestone-Version einer Note durchfuehrt — unabhaengig von Phase (P2/P3/P4) und unabhaengig von Note-Identitaet.

Es ersetzt phase- und note-spezifische Skripte (`W_P2.35_REVIEW_*`, lokale `_run_*.py`-Workarounds).

---

## 2. 9-Step-Zyklus (`D_260527_00_9STEP_ZYKLUS_VX4_VX9`)

Der Writing-Room hat einen 9-Step-Zyklus mit Pflicht-Slots V.x4 und V.x9 fuer HUMAN-Marker-Reader.

```
V<X>.<Y>0_DRAFT_HUMAN    ← HUMAN-Milestone (Quelle der Wahrheit)
                            kann >>MARKER_HUMAN:-Notizen enthalten
   ↓ W_WRITING_ROOM_HUMAN_MARKER_READER_build
V<X>.<Y>4_DRAFT_AI       ← HUMAN-Marker-Reader-Pass (KEIN Helfer-Lauf)
   ↓ W_WRITING_ROOM_REVIEW_build (NEUE Version, in Bau)
V<X>.<Y>5_DRAFT_AI       ← REVIEW-Pass mit Helfern (selektiv via EDITOR)
   ↓ W_WRITING_ROOM_HITL_build
V<X>.<Y>5_HITL.html      ← Browser-HITL
   ↓ HUMAN klickt durch → JSON-Decisions-Download
   ↓ W_WRITING_ROOM_DECISIONS_build
V<X>.<Y>6_DRAFT_AI       ← V.x5 + HUMAN-Decisions als Marker
   ↓ HUMAN sichtet V.x6, schreibt neue >>MARKER_HUMAN:
V<X>.<Y>8_DRAFT_HUMAN    ← HUMAN-Sichtung-Milestone
   ↓ W_WRITING_ROOM_HUMAN_MARKER_READER_build
V<X>.<Y>9_DRAFT_AI       ← Spiegelbild zu V.x4 auf V.x8
   ↓ HUMAN baut naechsten Milestone
V<X>.<Y+1>0_DRAFT_HUMAN  ← Zyklus startet erneut
```

**Reihenfolge V.x4 vor V.x5:**
1. HUMAN-Klaerungen IM Doc, bevor Helfer draufschauen → keine widerspruechlichen Findings.
2. HUMAN-Authority: Direkt-Anweisungen vor Helfer-Vorschlaegen.
3. Effizienz: V.x4 selektiv (3-5 Marker), V.x5 teuer (mehrere Helfer × Doc-Scan).

**Was NICHT erlaubt ist:**
- AI-Pass auf AI-Pass ohne HUMAN dazwischen → ERROR „AI-after-AI without HUMAN gate".

### 2.1 Versions-Schema-Detail

Verbindlich ab 2026-05-24 (`D_260524_00_P3_ARCHITEKTUR_RESET`). Erweitert 2026-05-27 (`D_260527_00`).

| Sub-Token | Rolle | Beispiel |
|---|---|---|
| `V<X>.x0_DRAFT_HUMAN` | **HUMAN-Meilenstein.** | `V3.30_DRAFT_HUMAN.docx` |
| `V<X>.x1–x3` | **Reserve.** | — |
| `V<X>.x4_DRAFT_AI` | **HUMAN-Marker-Reader-Pass.** Pflicht-Slot vor V.x5. | `V3.34_DRAFT_AI.docx` |
| `V<X>.x5_DRAFT_AI` | **REVIEW-Commit.** Helfer-Pass auf V.x4 (NICHT V.x0). | `V3.35_DRAFT_AI.docx` |
| `V<X>.x6_DRAFT_AI` | **HUMAN-Decisions als Marker.** | `V3.36_DRAFT_AI.docx` |
| `V<X>.x7` | **Reserve.** | — |
| `V<X>.x8_DRAFT_HUMAN` | **HUMAN-Sichtungs-Milestone.** | `V3.38_DRAFT_HUMAN.docx` |
| `V<X>.x9_DRAFT_AI` | **HUMAN-Marker-Reader-Pass auf V.x8.** | `V3.39_DRAFT_AI.docx` |
| `V<X>.(x+1)0_DRAFT_HUMAN` | **Naechster Meilenstein.** | `V3.40_DRAFT_HUMAN.docx` |

Plus Spezial-Suffix: `_V<N>` (z.B. `V3.25_DRAFT_AI_V1.docx`) — benannte Variante eines Slots (mehrere Versuche moeglich).

---

## 3. Helfer + EDITOR (NEUE Architektur, ab 2026-06-04)

> **Vorgaenger-Liste (8 Agenten):** archiviert. Siehe `_archive/W_WRITING_ROOM_deprecated_260525.md` und `_agents_WRITING_ROOM/_archive/W_WRITING_ROOM_AGENT_ARCHITEKT_deprecated_260605.md` etc.

### 3.1 Schreibstube — 8 Helfer + EDITOR (Meta)

| Familie | ID | Helfer | Domain | GATE | GOLD |
|---|---|---|---|---|---|
| a | a1 | 📐 **ENTWERFER** | Struktur + Erzaehlbogen | `W_WRITING_ROOM_ENTWERFER_GATE_260605.yaml` | `W_WRITING_ROOM_ENTWERFER_GOLD_260605.json` |
| b | b1 | 🖼️ **LAYOUTER** | Visuals + Layout (11 Sub-Modi) | `W_WRITING_ROOM_LAYOUTER_GATE_*.yaml` | `W_WRITING_ROOM_LAYOUTER_GOLD_*.json` |
| c | c1 | ✂️ **KUERZER** | Verdichten | `W_WRITING_ROOM_KUERZER_GATE_*.yaml` | `W_WRITING_ROOM_KUERZER_GOLD_*.json` |
| c | c2 | ✒️ **SCHREIBER** | Generieren (Multi-Option) | `W_WRITING_ROOM_SCHREIBER_GATE_*.yaml` | `W_WRITING_ROOM_SCHREIBER_GOLD_*.json` |
| c | c3 | 🔤 **KORREKTOR** | Pflicht: Vorschlags-Precheck; Body-Mechanik AUTO-Apply nach HUMAN-Autorisierung | `W_WRITING_ROOM_KORREKTOR_GATE_*.yaml` | `W_WRITING_ROOM_KORREKTOR_GOLD_*.json` |
| c | c4 | 📖 **LEKTOR** | Stil-Sparring | `W_WRITING_ROOM_LEKTOR_GATE_*.yaml` | `W_WRITING_ROOM_LEKTOR_GOLD_*.json` |
| d | d1 | 💎 **Perlensucher** | GOLD + PUSHBACK | `W_WRITING_ROOM_PERLENSUCHER_GATE_*.yaml` | `W_WRITING_ROOM_PERLENSUCHER_GOLD_*.json` |
| e | e1 | 📖 **CHRONIST** | Sonderhelfer Body → Dossier. P5A fuehrt **HIGHLIGHTER** als separate Sub-Phase-Chief-/Tooling-Rolle; LEKTOR (HL1) und PERLENSUCHER (HL2) bleiben fachliche Owner der Hervorhebungslogik. | Profil + Dossier-Schema | — |
| o | o1 | 🎼 **EDITOR** | **Chef-Agent von WRITING_ROOM** — Plan + Konflikt-Loesung + RfH-Abnahme (`D_260625_01 §K10`). Kein Helfer (Meta-Rolle). | — (Profil-only) | — |

**Phasen-Defaults gestrichen** (2026-06-05): EDITOR entscheidet pro Iteration via Pre-Check + HUMAN-Selektion (§11.1), welche Helfer laufen. Kein FRUEH/MITTE/SPAET-Default mehr.

**EDITOR-Chef-Agent-Klausel (`D_260625_01 §K10`):** EDITOR ist der Single-Use-of-Name fuer den WRITING_ROOM-Chef. Vorgaenger-Synonym `DIRIGENT` ist abgeloest und aus aktivem Spec-Body geloescht. Im Lesefluss erlaubte Bezeichnungen: „EDITOR", „Chef-Agent", „Meta-Agent", „Hub". NICHT mehr: „DIRIGENT".

### 3.2 Pruefstube (P4, extern — `C_OPS_P4A_TESTAGENTS.md`)

6 Pruefer fuer Cross-Note + Faktencheck + Recht — laufen einmalig in P4A_TESTAGENTS. Nicht Teil des MDL-Engine.

| ID | Pruefer | A1-Mapping |
|---|---|---|
| A1 | 🎬 NARRATIVA | a1 ENTWERFER cross-note |
| C1 | ✍ LINGUA | c4 LEKTOR final-pass |
| D1 | 🧭 POLARIS | d1 Perlensucher cross-note |
| E1 | 🔢 SIGMA | Fakten + Caption-Sub fuer LAYOUTER |
| F1 | ⚖ LEXA | Recht + Visual-Sub fuer LAYOUTER |
| G1 | 🎓 TECHNICA | EDUTECH + AITECH |

---

## 4. Builder-Suite (phase-agnostisch, alle produktiv)

| Tool | Rolle | Ziel-Slot |
|---|---|---|
| HUMAN-Marker-Reader (Builder geplant — SUBPROJEKT_01 FROZEN, Spec: `0_SUBPROJECTS/SUBPROJECT_MARKER_LOG_ARCHITECTURE/MLA_ARCHITECTURE.md §4.2`; alter Builder `W_WRITING_ROOM_HUMAN_MARKER_READER_build_260527.py` per 2026-06-06 in `_archive/`) | V.x0 → V.x4 + V.x8 → V.x9 | KEIN Helfer-Lauf |
| **`W_WRITING_ROOM_REVIEW_build_<YYMMDD>.py`** (NEU, in Bau) | REVIEW-Pass mit Helfern + Sub-Styles; ohne Marker-Cap | V.x5 (nach V.x4) |
| `W_HITL_RENDER_PRODUCER_260526.py` | HITL-HTML aus V.x5 | V.x5_HITL.html |
| `W_WRITING_ROOM_DECISIONS_build_260528.py` | HUMAN-Decisions aus HITL-JSON → V.x6 | V.x6 (nach HITL-Klicks) |

**Note:** Der alte `W_WRITING_ROOM_REVIEW_build_260525.py` ist deprecated — er kennt die neuen Helfer-IDs + Sub-Styles + Multi-Line nicht. Die kanonische produktive Fassung ist `W_REVIEW_FINDINGS_MATERIALIZE_PRODUCER_260605.py`.

---

## 5. CLI — Generischer Pattern (alle MDL-Builder)

```
py 0_W_WORKFLOW/W_WRITING_ROOM/W_REVIEW_FINDINGS_MATERIALIZE_PRODUCER_260605.py \
   --note <NOTE-FOLDER> \
   --note_prefix <PREFIX> \
   --from V<X>.<Y>0 \
   --findings <PATH-TO-FINDINGS.JSON or DIR> \
   --p2-entry-ticket <PATH-TO-PRODUCTIVE-P2_ENTRY_TICKET.JSON>
```

`--findings` kann sein:
- **eine JSON-Datei** (Sammel-File mit allen Helfer-Findings)
- **ein Verzeichnis** (Builder liest alle `findings_*.json` darin und aggregiert)

| Flag | Pflicht | Beschreibung |
|---|---|---|
| `--note` | ja | Note-Ordner |
| `--note_prefix` | ja | Datei-Prefix |
| `--from` | ja | Source-Version `V<X>.<Y>0` oder `V<X>.<Y>4`. Endziffer 0 oder 4. |
| `--findings` | ja | Pfad (Datei oder Ordner) |
| `--p2-entry-ticket` | bei `V2.*` ja | Produktives, vom GATEKEEPER ausgestelltes und exakt auf Note, Quelle und Ziel begrenztes Eintrittsticket. Simulation/Test wird abgewiesen. |
| `--variant` | nein | Variant-Suffix (z.B. `--variant V1` → Output `V<X>.<Y>5_DRAFT_AI_V1.docx`) |
| `--dry-run` | nein | Validiert + zeigt Plan, schreibt nichts |
| `--strict-anchors` | nein | Multi-Match-Anker werden SKIP statt WARN |

---

## 6. Output — V.x5_DRAFT_AI.docx

### 6.1 Aufbau

1. **Status-Block** am Doc-Anfang (max 15 Zeilen):
   - Versions-Info, Source-Hinweis
   - Helfer-Liste (welche liefen, wie viele Marker)
   - Marker-Bilanz (KRITISCH/WICHTIG/KOSMETIK/INFO/GOLD/PUSHBACK/TO_DISCUSS)
   - ENTWERFER-Final-Check-Resumee (siehe §11.3)
   - RfH-Status (PASS / HOLD + Diagnose, siehe §11.4)
   - Naechster Schritt
2. **Body** mit Inline-Markern (nach jedem Anker-Paragraphen).
3. **Keine MODERATOR-Sektion mehr** am Doc-Ende — Tagesschau lebt in `_EDITOR.json` + CLI-Bericht.

### 6.2 Marker-Sub-Style (Pflicht — fix V3.25-Bug)

Builder mapped `severity` auf Sub-Style automatisch (`C_FORMAT_DOCX §4.1` JSON-Block ist Single Source):

| `severity` | Sub-Style | Farbe |
|---|---|---|
| `KRITISCH` | `MARKER-KRITISCH` | `#C62828` rot |
| `WICHTIG` | `MARKER-WICHTIG` | `#EF6C00` orange |
| `KOSMETIK` | `MARKER-KOSMETIK` | `#1976D2` blau |
| `INFO` | `MARKER-KOSMETIK` | `#1976D2` blau |
| `GOLD` | `MARKER-GOLD` | `#2E7D32` dunkelgruen |
| `PUSHBACK` | `MARKER-KRITISCH` | `#C62828` rot (Sparring 2026-06-05) |
| `HINWEIS` | `MARKER-KOSMETIK` | `#1976D2` blau |
| `TO_DISCUSS` | `MARKER-WICHTIG` | `#EF6C00` orange |

**Pflicht:** Builder MUSS Sub-Style zuweisen — nie nur `MARKER`-Default-Style. Der V3.25-Lauf hatte alle 36 Marker als reines `MARKER` (dunkelgrau, Spec-Verstoss). Fix-Code in Builder erforderlich.

Diese Tabelle mappt eine bereits aufgeloeste `severity` auf Rendering-Farbe. Die fachliche Herkunft von KRITISCH/WICHTIG/KOSMETIK liegt ausschliesslich in `0_C_CONVENTION/REVIEW_TO_MARKER/RTM_ROUTING_MATRIX.yaml severity_definitions` — hier keine zweite Definition.

### 6.3 Marker-Format

**Stub** (ab 1F.a Renderer-Vertrag, `D_260622_01`): Single Source ist `0_C_CONVENTION/C_MARKER.md`.

- Header-Konvention: `C_MARKER §2` (`>>V<X.Y> #N [SLOT-TYP: NAME] [PRIO] AKTION`)
- Slot-Vertrag je Klasse: `C_MARKER §5.1` (KL1/KL2/KL3/KL4 + CONFIRM)
- KL3 Multi-Option-Rendering: `C_MARKER §5.1` + `make_marker_body` Varianten-Cap (`VARIANTS_HARD_MAX`)
- PUSHBACK 3-Teiler (Perlensucher): `C_MARKER §10` (KL4 Sub-Form)
- GOLD-Filter Match → KL1-AUTO: `C_MARKER §6`

Das alte `M07:`-Praefix-Format ist obsolet — Counter laeuft jetzt als `#N` global pro Note via `W_MARKER_INSERTER.advance_marker_counter(note_dir)`.

### 6.4 TO_DISCUSS-Marker

```
[TO DISCUSS] [<AKT>/¶<NR>] <Frage/Befund> — bitte gemeinsam klaeren
```

Style: `MARKER-WICHTIG` (orange). Wer setzt: jeder Helfer (oder HUMAN), wenn Apply-Vorschlag nicht eindeutig ist.

### 6.5 Anker-Format

- **Einzel-Anker:** `[<AKT>]/¶<NR>` — z.B. `[B1]/¶143`
- **Range:** `[<AKT>]/¶<START>–¶<END>` — z.B. `[B1]/¶148–¶151` (KUERZER-Pflicht bei >2 Paragraphen)
- **Akt-uebergreifend:** `[<AKT1>→<AKT2>]/¶<START>–¶<END>` — selten, mit Vorsicht

**¶-Nummerierung:** 1-basiert in der DOCX-Anzeige (HUMAN-Konvention, intuitiv in Word zaehlbar). Intern im JSON 0-basiert (Python). Builder rechnet beim Insert: `displayed_para = anchor_paragraph + 1`.

### 6.6 Marker-Counter-Vergabe (`#N` note-global)

Builder vergibt Counter `#N` fortlaufend **durchgaengig pro Note** via `W_MARKER_INSERTER.advance_marker_counter(note_dir)` (State persistiert in `<note>/_marker_log.json`). Reset NUR bei Note-Neuanlage. Im Marker erscheint der Counter im Header `#N` (`C_MARKER §2`).

Das alte `M07:`-Praefix-Format ist obsolet (Pre-1F.a, `D_260622_01`).

---

## 7. EDITOR / EDITOR (Meta-Agent, §11)

**EDITOR ist der Hub.** Vor jedem V.x5-Pass laeuft EDITOR als erster Schritt — Pre-Check + HUMAN-Selektion + Helfer-Orchestrierung + RfH-Abnahme.

EDITOR ist **kein** Body-Editor. EDITOR plant, andere setzen um. Profil: `_agents_WRITING_ROOM/W_WRITING_ROOM_EDITOR_AGENT_260606.md`.

**HERVORHEBUNGEN-Individual-Trigger (`D_260807_07`):** Wird EDITOR von OPTOR fuer einen HERVORHEBUNGEN-Einzel-Lauf angestossen (Trigger-Phrasen + Ausloese-Mechanik: `AGENT_OPTOR.md §2` + `C_HERVORHEBUNG.md §8.3.2`), orchestriert EDITOR ausschliesslich den PERLENSUCHER-Anteil (Fundstellen als HL2 setzen, `C_HERVORHEBUNG.md §8.3.3`) — kein Full-WRITING_ROOM-Run mit allen 8 Helfern. Scan- und Doku-Sub-Lauf bleiben bei OPTOR/dem Checkpoint-Mechanismus, nicht bei EDITOR.

---

## 8. Pre-Check (vor REVIEW, default aktiv)

Vor dem REVIEW-Pass laeuft ein billiger Pre-Check (`W_WRITING_ROOM_REVIEW_build --pre-check`):

**Check 1 — HUMAN-Delta vorhanden?**
- Wort-Vergleich V<X>.<Y>0 vs. V<X>.<Y-5>5.
- TRUE → REVIEW laeuft.
- FALSE → ABBRUCH oder `--force`.

**Check 2 — Vorgaenger-Marker noch unveraendert?**
- Anteil der `>>V<X>.<Y-5>5 [...]`-Marker, die in V<X>.<Y>0 noch verbatim vorkommen.
- > 80% → KRITISCH-Hinweis: HUMAN hat noch nicht verarbeitet.

**Skip-Bedingungen:** erster Loop einer Note · Vorgaenger fehlt · manueller Sprung.

---

## 9. DECISIONS-Builder (V.x5 → V.x6)

Schwester-Builder (`W_WRITING_ROOM_DECISIONS_build_*.py`), produktiv seit 2026-05-28. Setzt HUMAN-Entscheidungen aus HITL-JSON als Decision-Marker in DOCX.

Position im Zyklus: V.x5 → V.x6 (Step 5 von 9). Format-Details: siehe Builder-Code + Schema `C_FORMAT_DOCX §4.1` (MINIDEV_MODIFY).

---

## 10. Loop-Disziplin

> **`D_260530_00` (2+1-Rule + 15-Marker-Cap) ist STATUS GILT NICHT** seit 2026-06-20 (per `D_260620_12` + Sub-Audit B v2 Q4(c)). Memo-Begruendung: „lieber 30 mit Vollstaendigkeitsgarantie als 2×15 unsicher." Builder zeigen alle Marker sortiert nach Prio, ohne Cap. Loop-Anzahl ist Note-spezifisch — kein Default-Cap.

---

## 11. EDITOR-Orchestrierung (NEU)

### 11.1 Dialogflow (Pre-Check + HUMAN-Selektion)

EDITOR fuehrt KEINEN FULL-RUN als Default. Stattdessen:

```
HUMAN:  "V<X>.<Y>0 ist bereit" / "DevLoop fuer V<X>.<Y>0" / aequivalent
EDITOR: Pre-Check (§8) + Lage-Bild
EDITOR: nummerierte Helfer-Liste mit AI-Empfehlung

═══════════════════════════════════════════════════════════════
🎼 [EDITOR] V<X>.<Y>0 — Pre-Check fertig
═══════════════════════════════════════════════════════════════
LAGE:        <1-Satz Diagnose>
TOP-CONCERN: <1-Satz: welche Achse dominiert?>

HELFER-AUSWAHL (Empfehlung markiert):
  [1] 📐 ENTWERFER    → <empfohlen ✓ | optional | skip>  (<Begruendung>)
  [2] 💎 Perlensucher → <...>
  [3] ✒️ SCHREIBER    → <...>
  [4] ✂️ KUERZER      → <...>
  [P] 🔤 KORREKTOR    → PFLICHT: PROPOSAL_PRECHECK; BODY_AUTOAPPLY separat autorisieren
  [6] 📖 LEKTOR       → <...>
  [7] 🖼️ LAYOUTER     → <...>
  [8] 📖 CHRONIST     → <empfohlen wenn Dossier leer/stale; HIGHLIGHTER bleibt separate P5A-Rolle>

BODY-AUTOAPPLY: <EMPFOHLEN | NICHT NOETIG> — HUMAN-AUTORISIERUNG: <OFFEN | JA | NEIN>
Antwort z.B.: "alle" / "1,3,6" / "nur 1,4"; KORREKTOR-PRECHECK laeuft unabhaengig von der Auswahl.
═══════════════════════════════════════════════════════════════
```

### 11.2 Helfer-Lauf

Nach HUMAN-Selektion ruft EDITOR die gewaehlten Fachhelfer in Prio-Reihenfolge. KORREKTOR ist kein abwaehlbarer Fachhelfer, sondern Pflicht-Qualitaetsschritt:

1. 📐 ENTWERFER — Struktur-Check (auch fuer Cluster-Decision-Mapping aus Vor-Versionen)
2. 💎 Perlensucher — GOLD-Schutz **vor** allen Eingriffen
3. ✒️ SCHREIBER (mit ENTWERFER-Auftraegen)
4. ✂️ KUERZER (mit ENTWERFER-Auftraegen)
5. 📖 LEKTOR — Stil-Sparring
6. 🖼️ LAYOUTER — Visuals + Caption + Naming
7. 📖 CHRONIST — ereignisgesteuert Body → Dossier
8. 🔤 KORREKTOR — `PROPOSAL_PRECHECK` auf saemtliche erzeugten `apply_text`/`apply_options`; Body-Auto-Apply nur bei `HUMAN-AUTORISIERUNG: JA`

Pro Helfer ein `findings_<HELFER>.json` (Schema-konform — `W_WRITING_ROOM_FINDINGS_SCHEMA_260605.md`).

### 11.2a KORREKTOR-Pflicht und aktive HUMAN-Information

1. `PROPOSAL_PRECHECK` laeuft in jeder Iteration auf allen neu erzeugten Vorschlagstexten. Ein ungepruefter Vorschlag darf nicht gerendert werden.
2. EDITOR informiert HUMAN aktiv, ob ein Body-Auto-Apply empfohlen wird, und weist knapp auf Umfang und Schutzgrenzen hin.
3. Ohne ausdrueckliche HUMAN-Autorisierung bleibt `BODY_AUTOAPPLY` aus. Das ist kein Skip des KORREKTOR-Pflichtlaufs: Der Vorschlags-Precheck bleibt aktiv.
4. Bei Autorisierung arbeitet KORREKTOR nach RTM/AUTOFIX, setzt Audit-/Info-Marker und veraendert keine geschuetzten Zitate, Dialoge, Codes oder HUMAN-/HL-Stellen.
5. Jeder gepruefte Vorschlag traegt `proposal_precheck.status`, `proposal_precheck.checked_by` und `proposal_precheck.checked_stage: PRE_RENDER`. Der Precheck ist der letzte textveraendernde Checkpoint vor dem Rendern. Jede nachtraegliche Textaenderung routet den Vorschlag erneut durch `PROPOSAL_PRECHECK`; ein obligatorischer Text-Hash ist nicht Teil dieses Prozessvertrags.

### 11.2b Tandem-Revision-Mini-Loop (`260713_1339`)

**Trigger:** HUMAN sagt `TANDEM-REVISION`, `TANDEM`, `SPARRING-SCHREIBEN` oder `ALTERNATIV-VERSION` zu einer bestehenden Textstelle.

**Bedeutung:** isolierter WRITING_ROOM-Loop fuer eine ALT/NEU-Schreibschleife. Kein Full-Run der ganzen Schreibstube. EDITOR plant nur den benoetigten Mini-Loop und schreibt im Plan `TANDEM-CALL`.

**Rollenfolge:**

1. ✒️ **SCHREIBER** — verfasst die AI-Alternativ-Version (`apply_text` oder `apply_options`).
2. 🔤 **KORREKTOR** — prueft mechanische Fehler der AI-Version; auch AI kann Tipp-/Grammatikfehler machen.
3. 📖 **LEKTOR** — prueft Stimme, Ton und Lesefluss; kein stilles Umschreiben, nur Vorschlag.
4. ✍ **LINGUA** — Endabnahme auf AI-Sound und Stilprofil. Hinweis: C1 LINGUA ist architektonisch vorgesehen (`SPECARCHY_FOR_WRITING_ROOM`), aktives Profil muss fuer Builder-Umsetzung geklaert werden.

**Sichtbare Form:** Default ist KL2/KL3-Marker nach `C_MARKER §10`. Bei `tandem_table=true` rendert der Builder zusaetzlich eine 2-Spalten-Tabelle `Original | AI-Vorschlag` direkt nach dem Marker. Bauplan: `W_TANDEM_REVISION_BUILDPLAN_260713.md`.

### 11.3 A2-Logik intern — ENTWERFER prueft c1/c2

Nach jeder KUERZER- oder SCHREIBER-DONE-Meldung routet EDITOR den Output zu ENTWERFER fuer Final-Check.

Pro c1/c2-Marker ein Verdikt:

| Verdikt | Bedeutung | DOCX-Sichtbarkeit |
|---|---|---|
| **GREEN** | Auftrag erfuellt, GOLD erhalten, Stil OK | implizit — kein Zusatz-Marker |
| **CAVEAT** | Vorschlag OK, aber Detail-Hinweis | INFO-Marker drunter: `📐 [ENTWERFER] [CHECK] M<NN> {Hinweis}` |
| **REWORK** | Auftrag nicht erfuellt | EDITOR ruft Helfer 1x mit praezisiertem Auftrag |

REWORK-Limit = 1. Nach erneutem FAIL → IGNORE_AND_JUMP (§11.5).

### 11.3a Innere Validierung — aktive Authority

Die alte VALIDATOR-Gate-Logik aus `D_260608_04` bleibt gemaess `D_260620_12` ausser Kraft. Bis zu einer neuen ausdruecklichen Architekturentscheidung ist ausschliesslich der RfH-Check aus §11.4 die innere Freigabe des WRITING_ROOM. Ein technischer Validator darf einzelne RfH-Punkte mechanisch belegen, ist aber weder separate Freigabe-Authority noch Voraussetzung aufgrund der obsoleten NJET-Logik.

### 11.4 RfH-Check (GATE_GOLDEX, Abnahme durch EDITOR)

Ready-for-HUMAN-Liste — pro Punkt PASS oder FAIL:

| # | Check |
|---|---|
| 1 | Marker-Format alle in `C_FORMAT_DOCX §1`-Whitelist |
| 2 | `apply_text` (oder `apply_options`) bei allen Decision-Markern (ausser GOLD/INFO/PUSHBACK) |
| 3 | GOLD-Erhalt: alle GOLD-Marker aus Vorgaenger noch im V.x5 |
| 4 | ENTWERFER-Final-Check durchgelaufen, wenn c1/c2 aktiv |
| 5 | Vollstaendigkeit: alle erwarteten Finding-IDs sind genau einmal als gerendert, bewusst unterdrueckt oder HOLD bilanziert; kein Cap und kein stiller Rest |
| 6 | Status-Block vollstaendig + Sub-Style-Pflicht erfuellt (§6.2) |
| 7 | HUMAN-Marker aus V.x4 alle adressiert |
| 8 | M-IDs durchgaengig, kein Doppel-Index |
| 9 | core_properties gesetzt (kein 2013-Datum) |
| 10 | KORREKTOR-`PROPOSAL_PRECHECK` fuer jeden nichtleeren `apply_text`/jede `apply_option` PASS und `checked_stage: PRE_RENDER`; nach dem PASS keine Textaenderung ohne erneuten Precheck |
| 11 | Freigabe-Scope belegt: erwartete Helfer und Finding-IDs sind explizit erfasst. `0 Findings` ist als `result: CLEAN` gueltig, wenn konkreter Pruefscope, gepruefte Kriterien und `coverage_complete: true` vorliegen. Eine untypisierte leere Teilmenge ist nie PASS; Befunde werden nicht erzwungen. |

**PASS** → V.x5_AI geschrieben + CLI-Tagesbericht raus.
**FAIL** → HOLD im CLI + Diagnose. Kein V.x5-Release.

### 11.5 IGNORE_AND_JUMP-Mechanik

Bei FAIL nach 1× REWORK (oder unaufloesbarem Pattern-Match):

1. Defektes Item als SKIPPED loggen (`id` · `criterion_id` · `reason` · `recommended_fix`).
2. Naechstes Kriterium / naechsten Auftrag weiter — kein Stillstand.
3. Am Pass-Ende: SKIPPED-Sektion im CLI-Tagesbericht + `_EDITOR.json`.
4. Iteration schliesst trotzdem als RfH (mit SKIPPED-Hinweis im Status-Block + CHECK-Markern im Body fuer HUMAN-Sichtung).

**Begruendung:** kein Abbruch bei Einzel-FAIL — die anderen Kriterien sollen nicht blockiert sein.

---

## 12. JSON-Sidecar `_EDITOR.json` (NEU)

Neben jedem V.x5-DOCX schreibt der Builder ein JSON-Sidecar mit:

```json
{
  "version": "V3.25_AI_V1",
  "note": "04_LETS_YAML",
  "timestamp": "2026-06-06T10:00:00Z",
  "lage_bild": { "wortcount": 2951, "diff_to_prev": "...", "top_concern": "..." },
  "humans_selection": [1, 3, 5, 6, 7],
  "helfer_runs": [
    {
      "helfer": "ENTWERFER",
      "findings_count": 5,
      "auto_fixes_count": 2,
      "skipped_count": 0
    }
  ],
  "auftraege": [
    {
      "from": "ENTWERFER",
      "to": "SCHREIBER",
      "what": "Akt 4 fuellen, ~120W",
      "marker_id": "M07",
      "status": "GREEN"
    }
  ],
  "entwerfer_verdikte": {
    "M07": "GREEN",
    "M08": "CAVEAT — Uebergang zu ¶9 pruefen",
    "M09": "REWORK → GREEN nach Re-Try"
  },
  "rfh_status": "PASS",
  "skipped": [],
  "marker_log_state": "<note>/_marker_log.json (M01..M36 vergeben)"
}
```

**Zweck:**
- Maschinenlesbar fuer Audit/Replay/Crosscheck.
- HUMAN sieht nichts davon — Sidecar ist Builder-internal.
- Neuer V.x5-Pass liest letzte `_marker_log.json` fuer M-ID-Fortlauf.

---

## 13. Was das Tool NICHT tut

- **Keine Findings erfinden** — Findings kommen extern via JSON, Builder ist Bauer nicht Reviewer.
- **Keine Agent-Logik ausfuehren** — Helfer-Profile + GATE leben in `_agents_WRITING_ROOM/`, MDL-Engine ruft sie nicht direkt auf.
- **Keine Notes loeschen oder verschieben** — Source-DOCX bleibt unangetastet.
- **Keine Stimme aendern** — Stilprofil-Schutz liegt in Helfer-Profilen (`S_SPRACHREGELN`).
- **Keine Phase-Logik** — Tool ist phase-agnostisch.
- **Kein Body-Apply im V.x5** — V.x5 ist Marker-Pass, Apply ist Aufgabe der phasen-spezifischen DEVELOP/APPLY-Builder (V.(x+1)0).

---

## 14. Phasen-Eignung

| Phase | Mini-Loop nutzbar? | Bemerkung |
|---|---|---|
| P2 (DRAFT) | ✓ | Kernanwendung. V2.X0_HUMAN → V2.X5_AI iterativ. Detail: `C_OPS_P2_DRAFT.md`. |
| P3 (TESTREADING) | ✓ | Ab V3.20 (nach Pre-LOOP). Detail: `C_OPS_P3_TESTREADER.md`. |
| P4 (AGENTEN) | ✓ | Ab V4.20 (nach Pre-LOOP). Mit `P4_AGENT_LIST` (Pruefstube) statt Schreibstube-Helfer. Detail: `C_OPS_P4A_TESTAGENTS.md`. |
| P1 / P5+ | weniger relevant | Tool funktioniert technisch trotzdem. |

---

## 15. Naechste Schritte (Post-REVIEW)

1. **HUMAN sichtet** `V<X>.<Y>5_DRAFT_AI` (Status-Block oben → Inline-Marker im Body).
2. **HUMAN arbeitet Marker ab** (HITL-Klicks via `_HITL.html`).
3. **HUMAN speichert** `V<X>.<Y+1>0_DRAFT_HUMAN.docx` (Rename in Word, manuell).

Damit Iteration abgeschlossen. Naechste Iteration: erneut REVIEW.

---

## 16. Cross-Refs

- **`0_C_CONVENTION/REVIEW_TO_MARKER/RTM_ROUTING_MATRIX.yaml`** — fachliche Severity-/Routing-Authority; diese Engine mappt nur auf Stil (§6.2)
- **Per-Phase-OPS:** `C_OPS_P2_DRAFT.md` · `C_OPS_P3_TESTREADER.md` · `C_OPS_P4A_TESTAGENTS.md`
- **Gate + HO/TO:** `C_OPS_GATE.md`
- **Findings-Schema:** `W_WRITING_ROOM_FINDINGS_SCHEMA_260605.md` (selber Ordner)
- **MARKER_LOG Architektur (SUBPROJEKT_01 FROZEN):** `_archive/MARKER_DEPONIE_260621/02_WORKFLOW_LIBS/SUBPROJECT_MARKER_LOG_ARCHITECTURE/MLA_ARCHITECTURE.md` — konsolidierter Plan (`_marker_state/` JSON-Cluster) + Linie-A-Spec in Appendix A. Eingefroren seit `D_260608_09`.
- **Marker-Log (live):** `<note>/_marker_log.json` (M-ID-Counter + History pro Note; voller State-Cluster in Re-Architektur — siehe Konzept-Paper §3.1)
- **Helfer-Profile + GATE + GOLD:** `_agents_WRITING_ROOM/W_WRITING_ROOM_<NAME>_*_260605.{md,yaml,json}`
- **EDITOR-Profil:** `_agents_WRITING_ROOM/W_WRITING_ROOM_EDITOR_AGENT_260606.md`
- **A2-Logik:** `_agents_WRITING_ROOM/W_WRITING_ROOM_ENTWERFER_AGENT_260605.md §9`
- **Marker-Format:** `C_FORMAT_DOCX §1` (Whitelist) · `§3.1` (Styles) · `§4.1` (Sub-Style JSON) · `§9` (Format) · `§9.5` (Multi-Line) · `§9.6` (TO_DISCUSS)
- **Sprach-Authority:** `0_C_CONVENTION/C_SPRACHREGELN.md`
- **Naming-Schema:** `0_C_CONVENTION/C_NAMING.md`
- **Decision-Quellen:** `D_260524_01` (P2-Mini-Loop) · `D_260527_00` (9-Step) · `D_260620_12` (hebt `D_260530_00` mit 15-Marker-Cap + 2+1-Rule auf) · `D_260604_13` (Agent-Architektur) · `D_260605_*` (Updates oben in §0)
- **Vorgaenger:** `_archive/W_WRITING_ROOM_deprecated_260525.md`
