# autonom-gh-contribute

Ein Regelwerk für Agenten, die in einem **fremden** Repository einen Pull Request landen sollen —
mit Beleg statt Behauptung.

> **EN:** A procedure for AI agents contributing to third-party repositories. Fork, patch, test in the
> repo's own convention, prove the change through the real entry point, publish measurements in the PR
> text, then read the result back through the API. Ships with the policy duties that apply when the PR
> is opened under a human account.

## Warum es das gibt

Am 03.11.2026 wurden vier Wege parallel recherchiert: Produkte, die selbst PRs öffnen; veröffentlichte
Skill- und Workflow-Pakete; empirische Studien zu agentischen PRs; und GitHubs eigene Regeln.
**Kein Projekt deckt alle acht Punkte unten ab.** Zwei fehlen durchgehend, auch bei den großen Anbietern:

1. **Vorher/Nachher-Messwerte im PR-Text.** Alle schreiben eine Zusammenfassung, keiner schreibt
   „14 Tests vorher, 18 nachher, beide Läufe zitiert".
2. **Rücklesen des erzeugten PR über die API.** Niemand prüft, ob der PR tatsächlich enthält, was der
   Agent behauptet hat.

Beides ist genau der Teil, der Reviewern Zeit spart — und der einzige, den ein Agent ohne Vertrauensvorschuss
liefern kann. Details und Quellen: [`docs/evidence.md`](docs/evidence.md).

## Die acht Punkte

| # | Punkt | Woran man merkt, dass er fehlt |
|---|---|---|
| 1 | Fork und Branch automatisch | Der Agent committet in `main` |
| 2 | Patch erzeugt | — (das können alle) |
| 3 | Tests **in der Konvention des Zielrepos** | Neues Testframework, oder „Tests laufen" ohne Ausgabe |
| 4 | PR-Text mit Messwerten | „Summary" statt Zahlen |
| 5 | Verifikation durch Rücklesen (`GET /pulls/{n}`) | „PR erstellt" ohne Prüfung |
| 6 | Ehrlicher CI-Status | „CI grün", obwohl der Lauf auf `action_required` steht |
| 7 | Secret-Hygiene | Token in `.git/config`, `.env` im Commit |
| 8 | Etikette / kein Spam | Zwei PRs für eine Sache, Nachfragen im Minutentakt |

## Vier Gates, bevor eine Zeile entsteht

1. **Quelle der Wahrheit gelesen.** README behauptet, Code entscheidet. Wenn der Adapter den Agenten
   längst kennt und ihn nur nicht aufruft, ist der PR zehn Zeilen groß — nicht tausend.
2. **Lizenz und Beitragsregeln.** CLA? DCO/`Signed-off-by`? Testpflicht? Belegpflicht für Agent-Layer?
3. **Kleinster echter Eingriff.** Drei Varianten durchrechnen (10 / 200 / 900 Zeilen) und die kleinste
   wählen, die den Fall löst. Große Ports erst nach Issue und Zusage des Maintainers.
4. **Menschliches Go.** Ein PR unter fremdem Namen ist eine externe Wirkung.

## Der Ablauf

1. Fork per API, Klon flach und sparse (`--depth 1 --filter=blob:none --sparse`).
2. Auf aktuellen `main` branchen, `HEAD..origin/main` prüfen.
3. Änderung plus Test in der Repo-Konvention.
4. **E2E durch die exportierte Funktion, nicht durch die CLI.** Ein manueller CLI-Aufruf beweist die
   CLI. Erst der Aufruf des echten Einstiegspunkts zeigt, ob der Adapter trägt.
5. Baseline messen: `stash` → Tests → `stash pop` → Tests.
6. Commit-Hygiene: imperativer Titel mit Scope, CRLF-frei, kein Secret.
7. Push, PR per REST, **zurücklesen**: state, head, Dateien, Checks.
8. CI-Status benennen — gelaufen, `action_required`, oder nicht vorhanden.

## Pflichten gegenüber GitHub

Automatisierung unter einem Menschenkonto ist erlaubt — die Verantwortung bleibt beim Menschen.

- **Zurechnung:** „You are responsible for all content posted and activity that occurs under your
  Account." Jede Agenten-PR ist rechtlich die PR des Kontoinhabers.
- **Identität:** Für echte Dauer-Automatisierung ein Machine Account oder eine GitHub App, nicht das
  persönliche Konto. Accounts, die automatisiert *registriert* werden, sind verboten.
- **Volumen:** ≤ 80 content-generating requests pro Minute, ≤ 500 pro Stunde. Sperren drohen auch
  „for undisclosed reasons" — Backoff statt Retry.
- **Kein Bulk:** wiederholte unpassende PRs gelten als „coordinated inauthentic activity".
- **Erstbeiträger:** Workflow-Läufe warten auf Freigabe und **verfallen nach 30 Tagen**. Ein PR ohne
  CI ist kein grüner PR.

## Was es nicht ist

Kein Produkt, kein Bot, keine CI-Automation. Kein Werkzeug, um viele PRs zu öffnen — das ist der Fall,
den GitHubs Regeln ausdrücklich verbieten. Es ist die Prozedur für **einen** PR, den ein Mensch
verantworten kann.

## Nutzung

`SKILL.md` in den Skill-Ordner des Agenten legen (Hermes: `~/.hermes/skills/`, Claude Code:
`~/.claude/skills/`), oder als Abschnitt in `AGENTS.md` übernehmen. `CHECKLIST.md` ist die Fassung
zum Abhaken vor dem Öffnen.

## Lizenz

MIT — siehe [`LICENSE`](LICENSE).
