# Thrust animation - giv gas med flammer! 🔥

Når vi trykker pil-op for at give gas, ville det være sejt hvis man kunne se ild komme ud bagved rumskibet!

Lad os tilføje en animation der viser når rumskibet giver gas.

---

# Lav en bedre rumskib-form

I stedet for at bruge den standard "triangle" form, lad os lave vores egen!

```python
SPACESHIP_SHAPE = ( (7,-20), (0,5), (-7,-20) )
```

- ✅ Sæt koden ind i `# CONSTANTS` sektionen, f.eks. lige efter `HALF_HEIGHT`

Det er tre punkter der tegner en trekant: højre hjørne, top, venstre hjørne.

---

# Lav en form med ild!

Nu skal vi lave en sammensatt form med både rumskib OG ild:

```python
SPACESHIP_THRUST_SHAPE = turtle.Shape('compound')
SPACESHIP_THRUST_SHAPE.addcomponent(SPACESHIP_SHAPE, BG_COLOR, 'light grey')
SPACESHIP_THRUST_SHAPE.addcomponent(( (7,-20), (0,-30), (-7,-20) ), BG_COLOR, 'orange')
```

- ✅ Sæt koden ind lige efter `SPACESHIP_SHAPE`

Dette laver en form der består af to dele:
* Første del: rumskibet (lys grå)
* Anden del: ilden (orange trekant bagved)

Ildens form `( (7,-20), (0,-30), (-7,-20) )` er en trekant der peger bagud, hvor `(0,-30)` gør at ilden rækker længere ned.

---

# Registrer formerne i turtle systemet

Efter vi har lavet `screen`, skal vi registrere vores nye former:

```python
screen.register_shape("spaceship", SPACESHIP_SHAPE)
screen.register_shape("spaceship_thrust", SPACESHIP_THRUST_SHAPE)
```

- ✅ Sæt koden ind i `# GAME SETUP` sektionen, lige efter `screen.tracer(0)`

Nu kan vi bruge `"spaceship"` og `"spaceship_thrust"` som former i vores spil.

---

# Opdater `Player.__init__`

Spilleren skal nu bruge den nye form i stedet for "triangle".

Før:
```python
self.shape("triangle")
self.color("light grey", BG_COLOR)
self.shapesize(stretch_wid=0.75, stretch_len=1.5)
self.penup()
```

Efter:
```python
self.shape("spaceship")
self.color("light grey", BG_COLOR)
self.penup()
```

- ✅ Find disse linier i `Player.__init__` funktionen
- ✅ Ændr `self.shape("triangle")` til `self.shape("spaceship")`
- ✅ **Slet** linjen med `self.shapesize` (vi behøver den ikke mere, da vores form allerede har den rigtige størrelse)

---

# Opdater `animate_spaceship()` funktionen

Nu skal vi skifte form når man trykker pil-op!

Tilføj denne kode i slutningen af `animate_spaceship()` funktionen:

```python
    if keys_pressed["Up"]:
        player.shape("spaceship_thrust")
    else:
        player.shape("spaceship")
```

- ✅ Find `animate_spaceship` funktionen i `# BEHAVIOURS` sektionen
- ✅ Sæt koden ind i slutningen af funktionen (efter `else: player.showturtle()`)

ℹ️ Pas på indrykningen! De nye linier skal være på samme niveau som `if player.is_invincible():` linjen.

---

# Den komplette `animate_spaceship()` funktion

Funktionen skulle nu se sådan ud:

```python
def animate_spaceship():
    if player.is_invincible():
        scaled = int(time.time() * 10)
        is_invisible = scaled % 2
        if is_invisible:
            player.hideturtle()
        else:
            player.showturtle()
    else:
        player.showturtle()

    if keys_pressed["Up"]:
        player.shape("spaceship_thrust")
    else:
        player.shape("spaceship")
```

Når du trykker pil-op viser den rumskibet med ild, når du slipper viser den rumskibet uden ild.

---

# Prøv det!

- ✅ Start spillet og tryk pil-op

Nu skulle rumskibet have orange ild når du giver gas! 🔥

* Tryk pil-op og se ilden komme ud bagved
* Slip tasten og ilden forsvinder
* Rumskibet fortsætter med at bevæge sig

---

# Bonus: Prøv at ændre farven!

I stedet for orange ild, prøv andre farver i `SPACESHIP_THRUST_SHAPE`:

* `'red'` - rød ild
* `'yellow'` - gul ild  
* `'cyan'` - blå ild (som i sci-fi rumskibe!)
* `'white'` - hvid ild

Find `'orange'` i linjen med `SPACESHIP_THRUST_SHAPE.addcomponent` og ret den til en anden farve!

---

# Bonus: Prøv at ændre formen!

Du kan også lave ilden større eller mindre ved at ændre tallene i `( (7,-20), (0,-30), (-7,-20) )`:

* `(0,-30)` styrer hvor langt ilden rækker
* Prøv `(0,-40)` for længere ild
* Eller `(0,-25)` for kortere ild

Eksperimenter og se hvad der ser bedst ud!
