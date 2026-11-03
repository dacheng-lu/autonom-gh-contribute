# Checkliste vor dem Öffnen

Kopierbar. Jede Zeile ist ein Beleg, keine Erinnerung — wenn du sie nicht mit einer Ausgabe belegen
kannst, ist sie nicht erfüllt.

## Vor der Arbeit

- [ ] Zielrepo gelesen: `CONTRIBUTING`, `LICENSE`, `.github/workflows/`, Testkonfiguration
- [ ] Der Code bestätigt die Lücke (nicht nur das README)
- [ ] Drei Varianten durchgerechnet, die kleinste gewählt, Umfang notiert: ____ Zeilen
- [ ] Freigabe des Kontoinhabers liegt vor

## Beim Bauen

- [ ] Branch von aktuellem `main`, `git log HEAD..origin/main` war leer
- [ ] Test in der Konvention des Repos (gleicher Runner, gleicher Stil)
- [ ] E2E-Aufruf über den echten Einstiegspunkt, nicht über die CLI
- [ ] Scratch-Test gelöscht, `git status` zeigt nur die gewollten Dateien

## Vor dem Commit

- [ ] Baseline gemessen: ___ Tests auf `main`, ___ Tests auf dem Branch
- [ ] `git show HEAD:<pfad> | grep -c $'\r'` ist 0 für jede geänderte Datei
- [ ] Kein Token / kein `.env` / keine Debug-Ausgabe im Diff
- [ ] `git remote -v` enthält keine Zugangsdaten

## PR-Text

- [ ] `## Problem` mit der echten Fehlermeldung
- [ ] `## Measurement` als Tabelle, beide Läufe zitiert
- [ ] `## Change` nummeriert, jede Änderung mit Grund
- [ ] `## Compatibility` (was sich für wen ändert)
- [ ] `## Not changed` (was bewusst ausgelassen wurde)
- [ ] `## Verification` mit Kommandos und exakten Ergebniszeilen

## Nach dem Öffnen

- [ ] `GET /pulls/{n}` gelesen: `state`, `mergeable`, `head`
- [ ] `GET /pulls/{n}/files` zeigt genau die beabsichtigten Dateien
- [ ] CI-Status geprüft und benannt: gelaufen / `action_required` / nicht vorhanden
- [ ] Falls `action_required`: im Text als „wartet auf Freigabe" benannt, nicht als Fehler

## Pflichten (GitHub)

- [ ] Volumen im Rahmen: ≤ 80/Minute, ≤ 500/Stunde content-generating
- [ ] Ein Zweck pro PR, echter Projektbezug
- [ ] Bei Dauer-Automatisierung: Machine Account oder GitHub App statt Personen-Konto
- [ ] `Signed-off-by` nur, wenn die DCO-Zertifizierung inhaltlich zutrifft
