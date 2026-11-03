# Belege und Prüfstatus

Stand 03.11.2026. Vier Recherche-Wege liefen parallel, jeder read-only, jeder gegen dasselbe
Acht-Punkte-Raster. Danach wurden die tragenden Aussagen **einzeln nachgeprüft** — was hier mit
„geprüft" steht, wurde vom Autor selbst gegen die Quelle abgerufen, nicht aus einem Lauf übernommen.

## Ergebnis je Weg

| Weg | Frage | Antwort | Geprüfte Kernbelege |
|---|---|---|---|
| A Produkte | Kapselt ein Produkt den ganzen Ablauf? | **nein** | `gh-aw` Safe Outputs: Agent ohne Schreibrechte beantragt `create-pull-request` mit `max: 1`, erzwungenem `draft`, `expires`, `excluded-files` (github.github.com/gh-aw). SWE-agent `open_pr.py`: `draft=True`, springt bei zugewiesenem, gelocktem oder bereits von Commits referenziertem Issue ab („Be nice :)"). Kein Produkt schreibt Messwerte in den PR-Text oder liest den PR zurück. |
| B Skill-Pakete | Gibt es die Prozedur als veröffentlichtes Regelwerk? | **nein** | `n8n/.agents/skills/create-pr` (repo-lokal, `gh pr create --draft`, kein Fork/Test/Rücklesen). `agentsview.io/contributing`: „Never claim a check passed without its current output". `obra/superpowers-skills` ist **archiviert** (API: `archived: true`, letzter Push 14.10.2025). |
| C Forschung | Was belegen Zahlen? | **nein** (kein publizierter geschlossener Workflow) | Watanabe et al., arXiv 2509.14745: 83,8 % angenommen, 54,9 % ohne Nacharbeit gemergt. MSR 2602.00164: 8.106 Fix-PRs, 326 manuell analysiert, Testfehler und bereits gelöste Issues als häufigste Gründe. LF/OpenSSF-Umfrage: 25 % der PRs „AI Slop" (31 % in großen Projekten), 59 % mehr Contributions, 35 % mit KI-Policy. |
| D Policy | Welche Pflichten gelten? | **nein** (Regeln ja, Übersetzung in einen Agenten-Ablauf nein) | ToS: „You must be a human to create an Account … We do permit machine accounts"; „one free machine account". Rate Limits: 80 content-generating requests/Minute, 500/Stunde, Sperren auch „for undisclosed reasons". Erstbeiträger-Freigabe verfällt nach 30 Tagen. |

## Was wir daraus übernommen haben

1. **Rechte-Trennung statt Vertrauen** (`gh-aw`): Der Agent, der den Patch erzeugt, hat keine
   Schreibrechte; ein separater Schritt veröffentlicht. Übernommen als Gate im Ablauf, nicht als Code.
2. **Etikette ist kodifizierbar** (SWE-agent): Vor dem Öffnen prüfen, ob das Issue schon bearbeitet
   wird — „schon von einem anderen PR gelöst" ist der häufigste Ablehnungsgrund.
3. **Keine Erfolgsaussage ohne frischen Beweis** (agentsview, superpowers): der Satz, der aus einem
   Agentenbericht einen Beleg macht.
4. **Draft und ein PR pro Aufgabe** (n8n, gh-aw, Copilot Cloud Agent): die einzige Statusmeldung, die
   nicht lügt, solange die CI nicht gelaufen ist.

## Korrekturen an den Recherche-Läufen

- Ein Lauf berichtete „63 % Burnout ist die Top-Sorge der Maintainer" und „64 % längere
  Review-Zyklen". Beides steht **nicht** in der OpenSSF-Quelle: die 63 % beziehen sich auf Zeit für
  neue Features, „burnout" kommt im Text nicht vor. Beide Zahlen wurden entfernt. Die Aussage
  „Maintainer-Belastung steigt" bleibt belegt — über die 53 %, die GenAI als zusätzliche Reibung
  beschreiben.
- Die Prozentzahlen zu Ablehnungsgründen (22,1 % / 18,1 %) stammen aus dem Volltext von
  arXiv 2602.00164 und waren im Abstract nicht prüfbar. Die **Rangfolge** ist im Abstract bestätigt,
  die exakten Werte sind hier bewusst nicht zitiert.

## Grenzen dieser Belege

- Alle Zahlen sind eine Momentaufnahme vom 03.11.2026 und verschieben sich mit jedem Monat.
- Ein Teil der Studien zieht aus derselben Datenquelle (AIDev/AIDev-pop) und ist damit nicht
  unabhängig voneinander.
- Die Policy-Aussagen gelten für Pull Requests unter einem Menschenkonto. Für GitHub Apps und Machine
  Accounts gelten andere Regeln — dieser Text deckt sie nicht ab.
