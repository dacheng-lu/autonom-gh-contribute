---
name: autonom-gh-contribute
description: Use when landing a verified PR in a third-party repo.
version: 1.0.0
license: MIT
---

# Autonom beitragen (Fremdrepo, belegt, ohne PR-Müll)

Ein PR in einem fremden Repository ist eine externe Wirkung unter fremdem Namen. Dieser Skill regelt
die Entscheidungskette davor — ob überhaupt beigetragen wird, was der kleinste echte Eingriff ist und
wann der PR als fertig gilt — und die Belegpflicht danach.

## When to use
- Ein Fremdrepo könnte etwas, das wir brauchen, aber ein Adapter/Feature fehlt.
- Der Nutzer sagt „contributen", „PR aufmachen", „das gehört upstream".
- Nicht für: eigene Repos (normaler Workflow), Issues ohne Code, Drive-by-Formatierung.

## Gates (alle vier, bevor eine Zeile entsteht)
1. **Quelle der Wahrheit gelesen.** README behauptet, der Code entscheidet. Lies den Adapter-Code,
   nicht die Feature-Liste. Beispiel: Ein Projekt listete den gesuchten Agenten längst in seiner
   Adapter-Tabelle — nur als „nicht aufrufbar" markiert. Das macht aus „neuer Agent" einen
   10-Zeilen-PR statt eines 900-Zeilen-Ports.
2. **Lizenz und Beitragsregeln.** LICENSE, CONTRIBUTING: CLA? DCO/`Signed-off-by`? Testpflicht?
   Belegpflicht für Agent-Layer?
3. **Kleinster echter Eingriff.** Drei Varianten durchrechnen (10 / 200 / 900 Zeilen) und die
   kleinste wählen, die den Fall wirklich löst. Große Ports erst nach Issue und Zusage des
   Maintainers — ein 900-Zeilen-PR aus dem Nichts wird höflich abgelehnt.
4. **Nutzer-Go.** Ein PR unter fremdem Namen ist eine externe Wirkung: ausdrückliche Freigabe abwarten.

## Procedure
1. **Fork und Klon.** `POST /repos/{upstream}/forks`, pollen bis `GET /repos/{me}/{repo}` antwortet.
   Große Repos flach und sparse: `git clone --depth 1 --filter=blob:none --sparse`, dann
   `git sparse-checkout set --no-cone 'pfad/*'`. Push aus dem flachen Klon funktioniert.
2. **Auf aktuellen Stand branchen.** `git fetch`, `git log HEAD..origin/main` lesen, dann editieren.
3. **Änderung plus Test in der Repo-Konvention.** Testdatei neben die bestehenden legen, Importe und
   Describe-Stil kopieren, kein neues Testframework einführen.
4. **E2E durch die exportierte Funktion, nicht durch die CLI.** Ein manueller CLI-Aufruf beweist die
   CLI, nicht den Adapter. Scratch-Test (uncommitted) gegen den echten Einstiegspunkt; er findet
   Fehler, die der Handaufruf verdeckt. Danach löschen und `git status` prüfen.
5. **Baseline messen.** `git stash -u` → Tests → `git stash pop` → Tests. Nur so steht „14 → 18" im
   PR statt einer Behauptung.
6. **Commit-Hygiene.** Titel imperativ plus Scope. Blobs CRLF-frei. Kein Token in `.git/config`,
   kein `.env`, keine Debug-Datei.
7. **Push und PR per REST.** Nach dem Push `git remote -v` prüfen. PR mit
   `POST /repos/{upstream}/pulls`, `head: "{me}:{branch}"`, `base: "main"` plus vollständiger Body.
8. **Zurücklesen statt glauben.** `GET /pulls/{n}` und `/files`: state, head, Dateizahl. Ein 201 ist
   kein Beleg. Danach Check-Runs und Actions-Runs zur Head-SHA abfragen.

## PR-Body (sechs Abschnitte, in dieser Reihenfolge)
`## Problem` (echte Fehlermeldung) · `## Measurement` (Vorher/Nachher aus echten Läufen) ·
`## Change` (nummeriert, mit Begründung) · `## Compatibility` · `## Not changed` (bewusst ausgelassen) ·
`## Verification` (Kommandos, exakte Ergebniszeilen, Umgebung).
Der „Not changed"-Abschnitt spart Reviewern Zeit und nimmt die Nachfragen vorweg.

## Verification (Gate vor „fertig")
- [ ] Testzahl vorher/nachher belegt, beide Läufe zitiert
- [ ] E2E-Ereignisliste im PR (start → delta/html → done(0)) mit Dauer
- [ ] `GET /pulls/{n}` zeigt `mergeable` und genau die beabsichtigten Dateien
- [ ] CI-Status benannt: gelaufen / `action_required` (Erstbeiträger-Sperre) / nicht vorhanden
- [ ] Volle Suite **nicht** behauptet, wenn sie nicht lief — Grund genannt
- [ ] Kein Secret in Commit, Config oder PR-Text

## Pitfalls
- **`action_required` ist kein Fehlschlag, sondern eine Freigabe-Warteschlange.** GitHub startet
  Workflows von Erstbeiträgern erst nach einem Maintainer-Klick, und offene Freigaben **verfallen
  nach 30 Tagen**. „CI grün" wäre hier gelogen.
- **Windows `shell: true` frisst `<`, `>` und `&` aus Argumenten.** Jeder Prompt oder Patch mit HTML
  bricht mit `"<" kann syntaktisch an dieser Stelle nicht verarbeitet werden` und Exit 1. Nur
  `.cmd`/`.bat` brauchen die Shell, `.exe` wird direkt gespawnt.
- **Sauberer `git status` heißt nicht „nichts vergessen":** Scratch-Tests liegen als untracked Datei
  daneben und landen sonst im Commit.
- **Ein PR, eine Idee.** Ein Fix, ohne den die Änderung nicht funktioniert, gehört dazu; eine
  Umformatierung derselben Datei nicht.
- **Nach dem PR nicht nachfassen.** Kein Ping, kein Reviewer-Tagging, kein Kommentar aus dem Nichts.
  Auf Rückfragen antworten ja, drängeln nein.
- **Volumen ist eine Sperrfalle.** ≤ 80 content-generating requests/Minute, ≤ 500/Stunde; wiederholte
  unpassende PRs gelten als „coordinated inauthentic activity".

## Reporting
Drei Zeilen: PR-Link, was er ändert, was der Beleg war. Dann der eine offene Punkt (CI-Sperre,
fehlende Suite, Folge-PR). Keine Nacherzählung der Schritte.
