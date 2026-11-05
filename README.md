# autonom-gh-contribute

Ein Skill für nachvollziehbare Beiträge zu fremden GitHub-Projekten: von der Problemrecherche über reproduzierbare Tests bis zur überprüften Veröffentlichung und Review-Nachverfolgung.

**English:** A practical skill for evidence-based upstream contributions: investigate policies and duplicates, verify a focused change, publish only within the user's authorization, and read back the actual result. It also supports reports and documentation without a PR.

## Welche Beiträge?

- **Problembericht:** reproduzierbarer Fehler, Umgebung und erwartetes Verhalten.
- **Dokumentation oder Beispiel:** überprüfte Schritte und passende Änderungen.
- **Test oder Evaluierung:** relevantes Fixture oder Regressionstest mit aussagekräftigem Ergebnis.
- **Code:** kleiner begründeter Patch mit zum Projekt passender Verifikation.

## Ablauf

1. Ziel und Projektregeln prüfen: KI-Richtlinie, Lizenz, Vorlagen, CLA/DCO und bestehende Arbeiten.
2. Tatsächlichen Upstream-Zielbranch und dessen SHA bestimmen; Ansatz und Autorisierung klären.
3. In isolierter Umgebung arbeiten; passende Baseline und reale Einstiegspunkte prüfen.
4. Ergebnis und Grenzen mit echten Belegen dokumentieren; Projektvorlage verwenden.
5. Nur autorisierte öffentliche Aktionen ausführen und die veröffentlichte Änderung samt CI zur exakten Head-SHA zurücklesen.
6. Review im autorisierten Rahmen begleiten und nach Änderungen erneut prüfen.

Die Details stehen in [SKILL.md](SKILL.md); die [Checkliste](CHECKLIST.md) ergänzt die menschliche Prüfung. Eine geprüfte Rekonstruktion und ein offener PR sind wertvolle Ergebnisse, auch wenn nichts gemergt wird.

## Optional: lokalen Nachweis prüfen

Python 3 ist erforderlich; keine zusätzlichen Pakete oder Netzwerkzugriffe. Kopiere [examples/contribution-record.json](examples/contribution-record.json), passe es an und führe aus:

```sh
python3 scripts/validate_record.py path/to/record.json
python3 -m unittest discover -s tests -v
```

Der Validator kontrolliert Struktur und ausgewählte Zustandsregeln, etwa eine veraltete Prüf-SHA oder ein noch nicht aufgelöstes Duplikat. Er prüft **nicht**, ob eine Behauptung stimmt, eine URL existiert, Tests ausgeführt wurden oder eine Aktion genehmigt ist; er verhindert selbst keine Veröffentlichung. Siehe [record-format.md](docs/record-format.md).

## Installation

Den **gesamten Repository-Inhalt** als Skill-Ordner installieren, damit relative Verweise auf Skripte und Beispiele funktionieren. Plattformabhängige Pfade und Möglichkeiten unterscheiden sich; den Anweisungen des jeweiligen Agenten folgen. Der Skill führt selbst keine GitHub-Aktionen aus und enthält keinen Bot.

## Umfang und Quellen

Die frühere Recherche ist eine begrenzte Momentaufnahme, kein Beweis für Einzigartigkeit. Siehe [docs/evidence.md](docs/evidence.md). Projektrichtlinien ändern sich: vor jedem Beitrag neu prüfen. Keine feste PR-Menge als Ziel setzen; GitHub-Limits sind keine Erlaubnis, viele Anfragen zu versenden.

## Lizenz

[MIT](LICENSE)
