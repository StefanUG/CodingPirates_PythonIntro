# Wrap Player

Nu skal vi have rumskibet til at flytte sig til den anden side når den flyver ud af syne / ud af skærmbilledet.

# Kan I huske koordinat systemet ?

![coordinate system](slide-resources/coordinate-system.svg)

---

# Kan I huske skærmens størrelse ?

```python
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
```

## Hvordan finder vi halvdelen ?

Python er rigtig god til matematik:

`+` (plus) og `-` (minus) og `*` (gange) og `/` (divider) 

```
SCREEN_WIDTH / ???
```

---

# Regn halvdelen af bredde og højde ud

```python
HALF_WIDTH = int(SCREEN_WIDTH / 2)
HALF_HEIGHT = ???
```

- ✅ Sæt koden ind i `CONSTANTS` sektionen
- ✅ Gør HALF_HEIGHT færdig, så den indeholder halvdelen af højden.

---

# Lav en ny funktion til at flytte turtle

```python
def move_if_out_of_bounds(t: turtle.Turtle):
```

`t` er navnet på en variabel
`turtle.Turtle` efter `:` er et type-hint, som man kan bruge til at fortælle editoren hvad vi kan forvente. 

Så kan den bedre hjælpe os med forslag

- ✅ Lav funktionen i `BEHAVIORS` sektionen, **før** `move_spaceship` (man kan ikke bruge en funktion før den er defineret)

---

# Lav logikken til at flytte turtle

Inde i den nye funktion, start med at gemme `x` og `y` i en variabel:

```python
    x = t.xcor()
    y = t.ycor()
```

Og så skal du tjekke om turtle er ude af syne.

I pseudo kode skal vi bruge noget ala dette:

```python
    if x is too far right:
        t should goto left side of screen
    elif x is too far left:
        t should goto right side of screen
```

Og det samme med op og ned.

F.eks.:

```python
    if x > HALF_WIDTH  # too far right
        t.goto(-HALF_WIDTH, y)
```

Inde i `move_if_out_of_bounds` funktionen skal du:

- ✅ Gem `x` og `y` i hver sin variabel som vist ovenover.
- ✅ Færdiggør algoritmen som er startet herover ved brug af `if` og `elif`. Du skal bruge to af hver.


---

# Til sidst skal funktionen kaldes

Det vil vi gøre lige efter vi har flyttet spilleren i hvert game loop. F.eks. som det sidste i `move_spaceship` funktionen.


```python
        move_if_out_of_bounds(player)
```

Her sender vi `player` med som parameter. 
Det er den vi gerne vil flytte hvis den er ude af syne.

- ✅ Indsæt kaldet til `move_if_out_of_bounds` i `move_spaceship` funktionen.

# Prøv spillet

- ✅ Start spillet og se hvad der sker når rumskibet flyver ud af skærmen
