# C_ZUTRITTSKONTROLLE_TURN_SPEC — Struktur und Inhalt

Status: DRAFT / SNAPSHOT 2026-11-19 · Referenzprofil: `P2_WRITING_ROOM/P2_WRITING_ROOM_PROFILE.json`

## 1. Ziel

Die Zutrittskontrolle verhindert die FATAMORGANA: HUMAN und AI dürfen erst in eine geschützte Phase eintreten, wenn sie nachweislich denselben realen PATH, denselben Zweck, denselben Ablauf und dasselbe Übergabeziel meinen.

Die gesamte Kontrolle muss in einem CHAT-Turn und auf einer Bildschirmseite verständlich sein. Technische Details werden nur gezeigt, wenn HUMAN sie für eine Entscheidung braucht.

## 2. Verbindliche Reihenfolge

1. **Zielkachel:** Phasenname gross, phasenspezifisches Bild, aktueller Schlossstatus.
2. **Orientierung:** `Was ist <PHASE>?` und `Wann aktivieren?` in HUMAN-Sprache.
3. **Zielbindung im PASSIVMODUS:** HUMAN verweist aktiv auf genau eine FIELDNOTE oder deren Quell-Milestone. AI prüft ausschliesslich diesen Verweis; erst danach schlägt sie Zielordner und Zieldatei vor. HUMAN kann beide bearbeiten und verbindlich an den GATEKEEPER übergeben.
4. **Zutrittsverlauf:** `1 OPTOR/GATEKEEPER → 2 HUMAN → 3 OPTOR/GATEKEEPER` mit echten gerichteten Pfeilen.
5. **Zutrittsbedingungen:** getrennte AI- und HUMAN-Kriterien mit rotem Kreuz oder grünem Haken.
6. **Phasenlogik:** grafische Darstellung der wichtigsten Artefakt- oder Versionsbewegung einschliesslich Loop und Handover.
7. **Rollen/Helfer:** anklickbare Reiter; Auswahl zeigt einen kurzen Rollenauftrag.
8. **Verdikt:** sichtbares `HOLD` oder `GO` mit genau einem nächsten Schritt.

Ein zusätzlicher beschreibender Subtitle unter dem Phasentitel ist verboten, wenn dieselbe Information bereits unter `Was ist <PHASE>?` steht.

## 3. Zutrittslogik

### 3.1 AI-Seite

Mindestens REQUIRED:

- eindeutiger PATH und Zielphase bestimmt;
- phasenspezifisches Manifest geladen;
- alle REQUIRED Specs samt transitiven Referenzen geladen und gegen erwartete Prüfsummen geprüft;
- erforderliche Inputs vorhanden und validiert;
- Handover-Ziel bekannt.
- Zielordner existiert, liegt im erlaubten Workspace, ist beschreibbar und wurde als kanonischer absoluter Pfad aufgelöst;
- HUMAN-Verweis und tatsächlicher Note-Root stimmen überein; Archive, Exporte und Sicherungskopien sind keine produktiven Ziele;
- der referenzierte oder daraus eindeutig abgeleitete Quell-Milestone wurde in genau dieser FIELDNOTE real gefunden und passt zum P2-Startslot;
- Zieldateiname erfüllt Naming und erwarteten Dateityp;
- Kollision wurde geprüft; ohne ausdrückliche Überschreiberlaubnis gilt `HOLD_IF_EXISTS`.

### 3.2 HUMAN-Seite

Mindestens REQUIRED:

- Zweck und erwartetes Ergebnis verstanden;
- zentraler Loop beziehungsweise Arbeitsablauf verstanden;
- eigene Entscheidungen und Pflichten verstanden;
- vorgeschlagenen Zielordner und Zieldatei geprüft oder geändert und verbindlich bestätigt;
- genau eine FIELDNOTE beziehungsweise deren Note-Root oder Quell-Milestone aktiv referenziert;
- Handover-Ziel verstanden;
- explizite Startbestätigung abgegeben.

Wenn HUMAN innerhalb der Phase Helfer auswählt, ist die Kenntnis und Übernahme dieser Auswahlverantwortung ein eigenes Zutrittskriterium. Die konkrete Auswahl erfolgt erst, nachdem der verantwortliche Orchestrator eine begründete Empfehlung vorgelegt hat.

### 3.3 Verdict

- Grundstellung ist `DEFAULT = DENY`; solange kein gueltiges GO vorliegt, bleibt der sichtbare Zustand `HOLD`.
- Fehlt ein REQUIRED-Kriterium: `HOLD` mit konkreter Klärung.
- Sind alle REQUIRED-Kriterien erfüllt: GATEKEEPER öffnet exakt die bezeichnete Phase und übergibt den LEAD.
- Keine erfundene Route, kein stiller Fallback, keine Freigabe aufgrund einer blossen Triggerphrase.

Für P2 ist `OPTOR` der einzige reguläre GATEKEEPER. `ADVISER` darf den Eintrittswunsch routen und den Stand synchronisieren, aber kein GO erteilen. Ein `DIRECTOR_OVERRIDE` ist nur als ausdrückliche, protokollierte Ausnahme zulässig.

Das GO wird als produktiver, auf Note, Quelle und Ziel gebundener `P2_RUN_CONTEXT` an die WRITING_ROOM übergeben. Fehlender, ungültiger oder als Simulation/Test gekennzeichneter Kontext ergibt vor der ersten Mutation sowie vor Phase-Resolver, Ledger, Sidecar oder DOCX-Erzeugung `HOLD — P2_GATEKEEPER_ADMISSION_REQUIRED`.

### 3.4 Stabiler HOLD-Zustand und vorbereiteter Output

Ein HUMAN-Auftrag bindet nur den Eintrittswunsch. Auch ein ausdrücklicher, wiederholter, umformulierter, verneinter, korrigierter oder dringlicher Auftrag kann `HOLD` nicht aufheben und keinen `P2_RUN_CONTEXT` erzeugen. Der ausführende P2-Builder darf seinen eigenen Zulassungskontext weder erzeugen noch ergänzen oder reparieren. Zulässiger Zustandswechsel ist ausschliesslich ein bereits von `OPTOR/GATEKEEPER` ausgestellter und danach verifizierter produktiver Kontext.

Bei fehlender oder ungültiger Zulassung gilt die direkte Anweisung: **AI, informiere HUMAN jetzt über den geschlossenen P2 und aktiviere `OPTOR/GATEKEEPER` für die Zutrittsprüfung.** AI antwortet ohne weitere P2-Analyse, Werkzeugprüfung, Lösungssuche oder Rückfrage exakt mit:

```text
HOLD — P2_GATEKEEPER_ADMISSION_REQUIRED

STATUS: HOLD
P2_STARTED: NO
HUMAN_REPORT: P2 ist geschlossen. Ich habe P2 nicht gestartet.
REQUEST: Als Eintrittswunsch registriert; keine Zulassung.
REASON: Kein verifizierter produktiver P2_RUN_CONTEXT von OPTOR/GATEKEEPER.
NEXT: Zulässiger nächster Schritt ist die Aktivierung von OPTOR/GATEKEEPER für die Zutrittsprüfung. Bis zu dessen GO bleibt P2 geschlossen.
```

Nach dem Report ist ausschliesslich die Aktivierung beziehungsweise Route zu `OPTOR/GATEKEEPER` zulässig. Ist diese technisch nicht verfügbar, endet der Turn. Ist kein produktiver Issuer verfügbar, bleibt `HOLD`; der Builder sucht keinen Ersatzweg.

Bei jeder Nachfrage, ob P2 nicht trotzdem gestartet oder ausgeführt werden kann, antwortet AI ohne Zusatz exakt:

```text
Nein, das ist leider nicht möglich. P2 bleibt geschlossen, bis OPTOR/GATEKEEPER einen verifizierten produktiven P2_RUN_CONTEXT ausgestellt hat.
```

## 4. Binding

Jedes Feld und Kriterium verwendet genau eines der Bindings `REQUIRED | CONDITIONAL | OPTIONAL`. Fehlerpriorität oder kosmetische Bedeutung ersetzen diese Ladeverbindlichkeit nicht.

## 5. Interaktion

- Rollenreiter sind native, tastaturbedienbare Buttons.
- Pro Klick erscheint genau ein kurzer Infotext; kein permanenter Textblock pro Rolle.
- Eine HUMAN-Bestätigung darf mehrere zuvor erklärte HUMAN-Kriterien bestätigen, muss deren Bedeutung aber sichtbar machen.
- Statuswechsel aktualisieren Schloss, Kriterien und Verdict gemeinsam.
- Die Oberfläche bleibt ohne horizontales oder internes Scrollen nutzbar.
- Die Zielbindung beginnt mit einem Feld `FIELDNOTE / Quell-Milestone`. HUMAN liefert den Verweis aktiv. Der GATEKEEPER erzeugt keine Kandidatenliste und durchsucht nicht prophylaktisch alle FIELDNOTES.
- Zielordner und Zieldatei werden danach in zwei editierbaren Feldern gezeigt. Die Oberfläche bildet daraus den vollständigen Zielpfad und übergibt ihn strukturiert; HUMAN muss keine Antwortvorlage kopieren.
- Die Eingabe allein ist keine Freigabe. Der GATEKEEPER prüft Existenz, Schreibzugriff, Naming und Kollision mit realen Werkzeugen. Erst `TARGET_BINDING_PASS` kann das Gate öffnen.

### 5.1 PASSIVMODUS für FIELDNOTE-Bindung

- Erlaubte Verweise: kanonischer Note-Root, konkrete HUMAN-Quelldatei oder bereits im Auftrag ausdrücklich gebundener Note-Pfad.
- AI darf innerhalb des referenzierten Note-Roots die erforderlichen Quellen prüfen. Andere Note-Roots bleiben ausser Scope.
- Ein blosser Titel ohne eindeutigen Pfad darf nur über eine eng begrenzte exakte Namensauflösung geprüft werden; keine Vollinventur und keine Kandidatenflut.
- Fehlender, nicht erreichbarer oder mehrdeutiger Verweis ergibt `HOLD` mit der Aufforderung, genau eine NOTE beziehungsweise Quelldatei zu referenzieren.
- Nach erfolgreichem `NOTE_BINDING_PASS` schlägt AI Zielordner und Zieldatei aus dem real gefundenen Quell-Milestone und dem Versionsschema vor.

## 6. P2-Referenz

P2 zeigt den Versionsloop:

`V2.x0_HUMAN → V2.x5_AI → V2.(x+1)0_HUMAN → nächste Iteration`

Bei grünem Exit-Gate wird die NOTE als `V3.05_AI` plus TESTEDITION an `P3_TESTREADER` übergeben. Fachliche Authority dafür bleibt `0_C_CONVENTION/C_OPS_P2_DRAFT.md` und die Gate-Matrix.

## 7. GATEKEEPER-Bindung

`GATEKEEPER` ist der phasenübergreifende Funktionsname für die einzige Instanz, die eine geschützte Tür öffnen darf. Er ist kein neuer Agent.

- P2 bindet `GATEKEEPER` an `OPTOR`.
- `ADVISER` führt die HUMAN–AI-Synchronisierung und routet zur eindeutigen Tür, erteilt im FIELDNOTES-P2-Pilot aber nicht selbst die Admission.
- `DIRECTOR` darf als expliziter Override gebunden werden; dieser Weg muss sichtbar und protokolliert sein.
- Finder, Startadapter und AGENTS-Dateien dürfen zum GATEKEEPER leiten, aber niemals selbst öffnen.
