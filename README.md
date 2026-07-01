# Fruit Loop

Ett terminalspel där du samlar frukter och försöker ta dig ut genom utgången.

## Starta projektet

Skriv komando i terminalen medan du står i projektets rotmapp:

```
python -m src.game
```

## Hur man spelar

Använd tangenterna för att styra spelaren `@` runt på kartan:

| Tangent | Rörelse |
|---------|---------|
| `w` | Upp |
| `s` | Ner |
| `a` | Vänster |
| `d` | Höger |
| `i` | Visa inventory |
| `j` + riktning (t.ex. `jw`) | Hoppa två steg |
| `q` | Avsluta spelet |

## Symboler på kartan

| Symbol | Betydelse |
|--------|-----------|
| `@` | Spelaren |
| `#` | Vägg |
| `?` | Frukt (+20 poäng) |
| `^` | Fälla (-10 poäng) |
| `K` | Nyckel |
| `C` | Kista (+100 poäng, kräver nyckel) |
| `S` | Spade (gräver bort en vägg) |
| `E` | Utgång |

## Mål

Samla allt på kartan och gå sedan till utgången `E` för att vinna.
Obs: varje steg du tar kostar 1 poäng, så rör dig smart!

## Vad jag har gjort

| Version 1 | Status |
|-----------|--------|
| A - Spelaren börjar nära mitten | ✅ |
| B - Rörelse i 4 riktningar (WASD) | ✅ |
| C - Kan inte gå igenom väggar | ✅ |
| D - Frukter ger 20 poäng | ✅ |
| E - Inventory sparas i en lista | ✅ |
| F - Kommandot "i" visar inventory | ✅ |
| G - Varje steg kostar 1 poäng | ✅ |
| H - Väggar byggda med loopar | ✅ |

| Version 2 | Status |
|-----------|--------|
| I - Fällor (-10 poäng, ligger kvar) | ✅ |
| J - Spade gräver bort en vägg | ✅ |
| K - Nycklar och kistor (+100 poäng) | ✅ |
| L - Ny frukt varje 25:e drag | ✅ |
| M - Utgång när allt är samlat | ✅ |
| N - Hoppa med j + riktning | ✅ |