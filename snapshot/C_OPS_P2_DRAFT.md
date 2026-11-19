# C_OPS_P2_DRAFT — Phase 2: Iteratives Drafting via Writing-Room

> [!CAUTION]
> **P2 GATEKEEPER — DEFAULT = DENY.** Eine P2-Triggerphrase oder der Auftrag, eine
> `V2.x4`/`V2.x5`-Fassung zu erzeugen, ist nur ein **Eintrittswunsch** und niemals
> eine Aktivierung. Vor jeder P2-Mutation sowie vor Phase-Resolver, Ledger, Sidecar
> oder DOCX-Erzeugung muss ein produktives, fuer genau diesen P2-Lauf ausgestelltes
> **Eintrittsticket** (`P2_ENTRY_TICKET`) vorliegen. `P2_ENTRY_TICKET` bezeichnet
> weder die Pflichtlektuere im Manifest noch den aktuellen Inhalt eines Modell-
> Kontextfensters. Es ist der maschinenlesbare Beleg fuer GATEKEEPER-Entscheid,
> Route, Status sowie die Bindung an Note, Quelle und Ziel. Fuer P2 fuehrt jede
> Sammlung und Kanalisierung ausschliesslich zum `GATEKEEPER`. `ADVISER` darf nur
> dorthin routen und synchronisieren, aber keinen Zutritt erteilen. Ein
> `DIRECTOR_OVERRIDE` muss innerhalb des GATEKEEPERS ausdruecklich und
> nachvollziehbar gebunden sein. Fehlt die Zulassung, ist sie ungueltig oder stammt
> sie aus Simulation/Test, gilt sofort:
> `HOLD — P2_GATEKEEPER_ADMISSION_REQUIRED`. Danach endet die Ausfuehrung.
> Authority: `ZUTRITTSKONTROLLE/C_ZUTRITTSKONTROLLE_TURN_SPEC.md`.

### Verbindlicher Sofort-Output bei HOLD

**AI, dein naechster Schritt ist festgelegt:** Informiere HUMAN jetzt ueber den
geschlossenen P2. Der einzige zulaessige Folgeschritt ist die Route zum `GATEKEEPER`.
Liegt kein verifiziertes produktives `P2_ENTRY_TICKET` vor, gib **ohne weitere
P2-Analyse, Werkzeugpruefung, Loesungssuche oder Rueckfrage** exakt diesen bereits
fertigen Report an HUMAN aus:

```text
HOLD — P2_GATEKEEPER_ADMISSION_REQUIRED

STATUS: HOLD
P2_STARTED: NO
HUMAN_REPORT: P2 ist geschlossen. Ich habe P2 nicht gestartet.
REQUEST: Als Eintrittswunsch registriert; keine Zulassung.
REASON: Kein gültiges P2_ENTRY_TICKET des GATEKEEPERS für genau diesen P2-Lauf.
NEXT: Zulässiger nächster Schritt ist die Route zum GATEKEEPER. Bis zu dessen GO bleibt P2 geschlossen.
```

Nach dem Report ist ausschliesslich die Route zum `GATEKEEPER` erlaubt; keine
P2-Handlung. Ist diese Route technisch nicht verfuegbar, endet der Turn mit dem
Report. Ein weiterer HUMAN-Auftrag,
eine Wiederholung, Umformulierung, Verneinung, Korrektur oder Dringlichkeit bestaetigt
nur den Eintrittswunsch. Sie hebt `HOLD` nicht auf und darf nie in eine Zulassung
umgedeutet werden. Der P2-Builder darf sein `P2_ENTRY_TICKET` weder selbst erzeugen
noch ergaenzen, reparieren oder durch eine HUMAN-Formulierung ersetzen. Nur ein bereits
vom GATEKEEPER ausgestelltes und anschliessend verifiziertes Ticket kann den
naechsten Eintrittsversuch auf `GO` setzen. Ein `DIRECTOR_OVERRIDE` ist nur als
ausdruecklich protokollierte Ausnahme innerhalb des GATEKEEPERS zulaessig.

Bei jeder Nachfrage, ob P2 nicht trotzdem gestartet oder ausgefuehrt werden kann,
antwortet AI ohne Zusatz exakt:

```text
Nein, das ist leider nicht möglich. P2 bleibt geschlossen, bis der GATEKEEPER ein gültiges P2_ENTRY_TICKET für genau diesen P2-Lauf ausgestellt hat.
```

> **Spec.** Neu erstellt 2026-05-31 durch Extraktion aus `W_WRITING_ROOM_260620.md`. MDL-Block-Entfernung pendant S7-Session.
>
> **AUFGABE:** Fliesstext der Note iterativ aufbauen — HUMAN schreibt Milestones (V2.x0), AI laeuft 9-Step-Writing-Room drueber (V.x4 Reader → V.x5 REVIEW → HITL → V.x6 Decisions → V.x8 HUMAN-Sichtung → V.x9 Reader), bis Loop-Exit-Kriterium erfuellt.
> **ZIEL:** Note steht textlich „gut genug" zum Test-Lesen: Wortcount im Ziel, stringenter Aufbau, organischer Schluss/Cliffhanger-Kandidat geprueft, Stilprofil eingehalten, TAKEAWAY konkret. Ein Cliffhanger-Fund ist SOLL, die dokumentierte Suche ist Pflicht (`D_260718_01`).
> **TAKEOVER (per K13 · `D_260625_01 §K13.A`):**
> ```
> NAME: PX_WRITING_ROOM (phase-agnostisches Werkzeug, in P2 als Phase-Body)
> CONDITION(MIN): V1.x-Skelett + DOSSIER + QUELLEN da (P1 abgeschlossen)
> HUM>AI: EINTRITTSWUNSCH: „Starte EDITOR" · „Starte WRITING_ROOM" · „P2 starten" · „beginne Draft"
> AI:     ROUTE „GATEKEEPER"; ohne produktives P2_ENTRY_TICKET → verbindlichen HOLD-Report unveraendert ausgeben und STOPP
> AI:     NUR NACH GO: OPS „WRITING_ROOM" (9-Step-Zyklus)
> AI>HUM: REPORT/OUTPUT: „DRAFT_V2.x5_AI" + RECOMMENDATION NEXT STEP
> HUM>AI: ADDITIONAL: „STARTE HTML"
> AI>HUM: OPS GENERATING „HTML" + INTEGRATING JSON + OPS WRITING ROOM
> HUM>AI: UPLOAD JSON
> AI>HUM: REPORT/OUTPUT: „DRAFT_V2.x9_AI" + RECOMMENDATION NEXT STEP
> ```
> Pattern-Master: `0_C_CONVENTION/C_CONSTITUTION.md Anhang C` + `D_260625_01 §K13`. Input-Detail: V1.x-Skelett mit META-Section, `<note>_DOSSIER.md` (`take_away` darf in P1 leer sein — `D_260606_03`), `<note>_QUELLEN.md`, vorbereitete LAYOUTER-Ordnerstruktur, S_DREHBUCH/S_QUELLEN_GENEALOGIE-Eintraege. HUMAN baut V1.x → `V2.00_DRAFT_HUMAN` als Startpunkt.
> **HANDOVER:** Phase endet beim Gate → P3 (siehe §3). HUMAN ruft `W_P2_GATE_BUILD --check exit` auf einer beliebigen `V2.X0_HUMAN` oder `V2.X5_AI`. Bei gruenem Gate: HO/TO-Mechanik in `C_OPS_GATE.md` (Mutter `V3.05_AI` + TESTEDITION). Nachfolger-OPS: `C_OPS_P3_TESTREADER.md`.
>
> **Schreiber:** ARCHY (bei strukturellen Aenderungen).
> **Leser:** OPTOR bei P2-Anleitung · DIRECTOR bei P2→P3-Gate-Pruefung · alle Writing-Room-Builder bei Phasen-Kontext.
> **Update-Trigger:** Aenderung am 9-Step-Zyklus · neue Quality-Agent-Decision · Aenderung am P2→P3-Gate-Kriterium · Aenderung am Stilprofil-Check.
> **Severity-Authority:** Fehlerklassifikation (KRITISCH/WICHTIG/KOSMETIK) lebt ausschliesslich in `0_C_CONVENTION/REVIEW_TO_MARKER/RTM_ROUTING_MATRIX.yaml`; diese Phase-Spec definiert keine eigene Skala.

---

## 1. Workflow

**Wann:** V1.x liegt vor (P1 abgeschlossen), Inhalt wird iterativ aufgebaut.

### 1.1 Architektur

Writing-Room mit 9 Agenten (1 Meta + 8 Helfer, `D_260604_13_AGENT_ARCHITEKTUR` + `D_260606_22` + CHRONIST-Erweiterung):

- 🎼 **EDITOR** (o1) — Meta-Agent: plant Iteration, Helfer-Selektion, Konflikt-Resolution
- 📐 **ENTWERFER** (a1) — Struktur + Erzaehlbogen (Schwerpunkt Erzaehlbogen, H1/H2-Schema)
- 🖼️ **LAYOUTER** (b1) — Visuals + Captions + Layout
- ✂️ **KUERZER** (c1) — Verdichten, Wortcount-Reduktion
- ✒️ **SCHREIBER** (c2) — Generieren, Luecken fuellen
- 🔤 **KORREKTOR** (c3) — Pflichtlauf in jeder Iteration: `PROPOSAL_PRECHECK` immer; Body-Auto-Apply nur nach aktiver Information und ausdruecklicher HUMAN-Autorisierung
- 📖 **LEKTOR** (c4) — Stil-Sparring, qualitativ
- 💎 **Perlensucher** (d1) — GOLD-Schutz + Verlust-Pushback
- 📖 **CHRONIST** (e1) — Sonderhelfer Body → Dossier; kein Body-Editor. Die P5A-Unterphase fuehrt **HIGHLIGHTER** als Sub-Phase-Chief/Tooling; innerhalb der Hervorhebungslogik bleiben LEKTOR (HL1) und PERLENSUCHER (HL2) die fachlichen Owner.

Der Perlensucher sucht bereits in P2 gezielt nach HEUREKA, INNOVATION und CLIFFHANGER. Kandidaten und `NONE`-/`REJECTED_BY_HUMAN`-Abschluesse schreibt er mit `TEXT`, `STATUS` und optional `HL_CANDIDATE` ins DOSSIER. Ein fruehes „WOW" darf als `HL3_OR_HL4` markiert werden; persistenter Word-HL-Apply bleibt P4→P5.

Engine-Spec (Builder, CLI, Findings-Schema, Pre-Check, Loop-Disziplin): `W_WRITING_ROOM_260620.md`.
Agent-Profile: `0_W_WORKFLOW/W_WRITING_ROOM/_agents_WRITING_ROOM/W_WRITING_ROOM_<HELFER>_AGENT_*.md` (EDITOR + 8 Helferprofile).
Agent-Config (Phasen-Defaults frueh/mitte/spaet): ~~`W_P2_QUALITY_MODI.json`~~ (archiviert D_260606_23 — Phase-Defaults leben heute pro Agent-Profil §2).

### 1.2 Verb-Schema (`D_260524_01_P2_MINI_LOOP_PRODUKTIV` + `D_260527_00_9STEP_ZYKLUS_VX4_VX9`)

| Verb | Wo | Was |
|---|---|---|
| **HUMAN-MARKER-READER** | V.x4 (nach V.x0) + V.x9 (nach V.x8) | AI liest `>>MARKER_HUMAN:`-Notizen, beantwortet, setzt `[AI-RESPONSE]`. KEIN Agent-Lauf. |
| **REVIEW** | V.x5 (nach V.x4) | AI-Pass mit 9 Agenten (1 Meta + 8 Helfer). KORREKTOR-Pflichtpass plus selektive Fachhelfer. Inline-Marker + EDITOR-Plan-Block (keine Tabellen-Sektion mehr). Kein Marker-Cap. |
| **HITL** | V.x5_HITL.html | HUMAN-Browser-Klicks auf V.x5-Findings → JSON-Decisions. |
| **DECISIONS** | V.x6 (nach HITL) | HUMAN-Decisions als Marker in DOCX gespiegelt (kein Body-Apply). |
| **DEVELOP** | V.x7 / V.(x+1)0 | HUMAN-Commit; Apply auf Body (optional separater Sub-Step). |
| **TRIAGE** | — | In P2 nicht standardmaessig (Sonderfall bei Marker-Flut, sonst P3-Cluster-Prozess). |

### 1.3 Inline-Marker-Format

Detail → `C_FORMAT_DOCX.md §9`. Kurz:

```
>>V<X>.<Y>5 [M<NN> | <AGENT>] <Befund> — <Empfehlung>
<AKTION>: <Vorschlag>
```

`AGENT` = eine der 8 IDs aus `W_P2_QUALITY_MODI.json`. Prio-codierte MARKER-Farben: rot KRITISCH · orange WICHTIG · blau KOSMETIK · gruen GOLD (Perlensucher, Schutz bis P6a).

### 1.4 AI tut (zusaetzlich zu Agent-Findings)

- Stilprofil-Check live (Anti-Muster pruefen, `S_SPRACHREGELN.md §5`)
- Tippfehler-Autofix mit `[AI-AUTOFIX]`-Info-Marker (`C_FORMAT_DOCX.md §3.2`)
- Wortcount-Tracking + Diff zu Ziel 1500–2500 (`D_260406_03_GENRE_FIELDNOTES`)
- VISUAL-Marker-Konsistenz
- H1/H2-Schema gemaess `C_FORMAT_DOCX.md` (`D_260525_01_GENERIC_AGENT_LIST_7PLUS1`)

### 1.5 HUMAN tut

- Inhalt schreiben (Stimme heilig — `S_SPRACHREGELN.md`)
- Cliffhanger suchen und – nur wenn organisch – als Kandidat setzen; `NONE` ist zulaessig
- Sixth-Sense-Dosierung entscheiden
- Bilder zuordnen
- TAKEAWAY ausformulieren (Ausfuellungs-Pflicht ab P2-Exit, siehe §3)

### 1.6 Loop-Steuerung (`D_260620_12`)

Die fruehere 2+1-Regel und der 15-Marker-Cap aus `D_260530_00` gelten nicht mehr. Die Zahl der Iterationen ist note- und aufgabenspezifisch. REVIEW zeigt alle gueltigen Findings priorisiert und vollstaendig; eine kuenstliche Begrenzung darf keine Befunde unterdruecken. Der P2-Exit richtet sich nach den aktiven Gate-Kriterien, nicht nach einer Markerzahl.

---

## 2. Slot-Tabelle (P2-spezifisch)

P2 nutzt das generische Versions-Schema aus `C_OPS_WRITING_ROOM.md §4.Y`. P2-Iterations-Range typisch: `V2.10` → `V2.20` (+ ggf. `V2.30`).

| Sub-Token | Beispiel | Rolle in P2 |
|---|---|---|
| `V2.00_DRAFT_HUMAN` | `<note>_V2.00_DRAFT_HUMAN.docx` | **Pickup von P1.** HUMAN baut Skelett (V1.x) zum ersten Draft mit Fliesstext aus. |
| `V2.x0_DRAFT_HUMAN` | `V2.10_DRAFT_HUMAN.docx` | HUMAN-Meilenstein pro Iteration. Kann neue `>>MARKER_HUMAN:`-Notizen enthalten. |
| `V2.x4_DRAFT_AI` | `V2.14_DRAFT_AI.docx` | HUMAN-Marker-Reader-Pass. Pflicht-Slot vor V.x5. |
| `V2.x5_DRAFT_AI` | `V2.15_DRAFT_AI.docx` | REVIEW-Output. 1 Meta + 8 Helfer; KORREKTOR-Pflichtpass, uebrige Helfer selektiv. Status-Block mit EDITOR-Plan-Block. |
| `V2.x5_HITL.html` | `V2.15_HITL.html` | HITL-Browser fuer V.x5-Findings. |
| `V2.x6_DRAFT_AI` | `V2.16_DRAFT_AI.docx` | HUMAN-Decisions aus HITL als Marker (kein Body-Apply). |
| `V2.x8_DRAFT_HUMAN` | `V2.18_DRAFT_HUMAN.docx` | HUMAN-Sichtungs-Milestone. Schreibt neue HUMAN-Marker. |
| `V2.x9_DRAFT_AI` | `V2.19_DRAFT_AI.docx` | HUMAN-Marker-Reader-Pass auf V.x8. |
| `V2.(x+1)0_DRAFT_HUMAN` | `V2.20_DRAFT_HUMAN.docx` | Naechster Iterations-Meilenstein. |

**Pflicht-Reihenfolge:** V2.x0 → V2.x4 → V2.x5 → V2.x6 → V2.x8 → V2.x9 → V2.(x+1)0. Sub-Tokens V2.x1–x3 / V2.x7 = Reserve.
**Forbidden:** AI-after-AI ohne HUMAN-Gate dazwischen (z.B. V.x5 → V.x6 ohne HITL-Klicks).

---

## 3. Gate → P3

> **Per `D_260620_16`:** HO/TO-Mechanik-Master ist `C_OPS_GATE.md §3`. Gate-Kriterien-Authority (SSoT) ist `C_OPS_GATE_MATRIX.md §3 Gate P2→P3`. Diese Sektion zeigt nur die Phase-spezifische Sicht („Gut genug"-Kriterien). Builder: `W_HAND_OVER_GATE_P2_BUILDER_260614.py`.

**„Gut genug" P2-Ende** (`D_260406_03_GENRE_FIELDNOTES`):

- [ ] Wortcount im Bereich 1500–2500
- [ ] Stringenter Aufbau (Erzaehl-Bogen schluessig)
- [ ] Jeder Akt zu mind. 80% ausformuliert
- [ ] Stilprofil eingehalten (`S_SPRACHREGELN.md §5`-Anti-Muster geprueft)
- [ ] Anker-Nummerierung gesetzt
- [ ] **TAKEAWAY konkret** in `<note>_DOSSIER.md` YAML-Frontmatter `take_away` — nicht leerer String / `?` / `-` (`W_DOSSIER_SCAN_build_260616` F2-Validator `NO_TAKE_AWAY`, `D_260606_06`)
- [ ] Letzter REVIEW unter 15 neuen Markern (Loop-Exit)
- [ ] H1/H2-Schema durchgehend (`C_FORMAT_DOCX.md §14`)

**Bei gruenem Gate:** HO/TO-Mechanik (Source-Strategy, Mutter-Erzeugung, TESTEDITION-Strip) in `C_OPS_GATE.md`. Output: `<note>_V3.05_DRAFT_AI.docx` (Mutter) + `<note>_V3.05_DRAFT_AI_TESTEDITION.docx`. HANDOVER an `C_OPS_P3_TESTREADER.md`.

### 3.1 P2_PRE_TESTAGENTS — Pflicht vor Persona-Upload

Nach dem P2-Gate laeuft auf der erzeugten P3-Testedition der fachliche Risikoscan `P2_PRE_TESTAGENTS`: `SIGMA` plus `TECHNICA` mit beiden Kindachsen `[EDUTECH]` und `[AITECH]`. Der Lauf darf technisch zu Beginn von P3 nachgeholt werden, bleibt aber ein P2-Artefakt. Abschluss ist `COMPLETE`, wenn jeder Pflichtpruefer Findings oder `CLEAN` geliefert hat; fehlende Ergebnisse ergeben `HOLD`. Der Lauf bereitet P3 vor und ersetzt den P4-Voll-Run nicht.

---

## 4. Cross-Refs (read-only)

- `C_OPS_P1_SETUP.md` — Vorgaenger-Phase (TAKEOVER-Source)
- `W_WRITING_ROOM_260620.md` — Engine-Spec (Builder, CLI, 9-Step-Zyklus, Pre-Check, note-spezifische Loop-Steuerung, Versions-Schema)
- `C_OPS_GATE.md` — Gate-Check + HO/TO-Mechanik (P2→P3 Dual-Output: Mutter + TESTEDITION)
- `C_OPS_P3_TESTREADER.md` — Nachfolger-Phase (HANDOVER-Target)
- `0_C_CONVENTION/ZUTRITTSKONTROLLE/P2_WRITING_ROOM/P2_WRITING_ROOM_PROFILE.json` — zentrale HUMAN-lesbare Zutrittsdarstellung, GATEKEEPER-Bindung und Referenzbild; keine zweite fachliche P2-Authority
- `0_C_CONVENTION/C_MARKER.md §9` — MARKER_LOG Architektur-Konzept (CONCEPT 2026-06-06; alte Spec `W_MARKER_LOG_SPEC.md` per 2026-06-06 in `_archive/`). Aktuell live: Counter-Sidecar `<note>/_marker_log.json` (entsteht in P2 beim ersten REVIEW-Run V.x5)
- `0_W_WORKFLOW/W_WRITING_ROOM/_agents_WRITING_ROOM/W_WRITING_ROOM_<HELFER>_AGENT_260605.md` — 8 Agent-Profile
- ~~`W_P2_QUALITY_MODI.json`~~ (archiviert D_260606_23 — Phase-Defaults leben heute pro Agent-Profil §2) — Agent-Config (Phasen-Defaults)
- `C_FORMAT_DOCX.md §9` (Marker-Format) · `§3.2` (AI-AUTOFIX) · `§14` (H1/H2) · `§4a` (META)
- `S_SPRACHREGELN.md §5` — Stilprofil-Anti-Muster (Live-Check)
- `AGENT_OPTOR.md §9` — OPTOR's Phase-Detail-Spec-Verweise (zeigt hierhin)
- `W_P2_GATE_BUILD` / `W_GATE_CHECKS.check_takeaway_definiert` — Matrix #11 (TAKEAWAY-Check)
- Decision-Quellen: `D_260524_01_P2_MINI_LOOP_PRODUKTIV` (Mini-Loop produktiv) · `D_260527_00_9STEP_ZYKLUS_VX4_VX9` (9-Step + V.x4/V.x9) · `D_260620_12_SCHREIBSTUBE_OBSOLETE_SPEC_REMOVAL` (hebt 2+1-Rule + 15-Marker-Cap aus `D_260530_00` auf) · `D_260406_03_GENRE_FIELDNOTES` (Wortcount-Range)
