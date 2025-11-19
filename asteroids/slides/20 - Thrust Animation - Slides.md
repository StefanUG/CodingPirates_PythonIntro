---
theme: gaia
marp: true
---
<style>
.container{
    display: flex;
}
.col{
    flex: 1;
}
</style>
<!-- need to enable HTML in the MARP extension -->

# Asteroids Game

## Thrust animation - giv gas med flammer! 🔥

Når vi trykker pil-op for at give gas, ville det være sejt hvis man kunne se ild komme ud bagved rumskibet!

Lad os tilføje en animation der viser når rumskibet giver gas.

---

# Hvad skal vi ændre?

Vi skal:

* Lave en ny form for rumskibet - en med ild bag
* Skifte mellem de to former når man trykker/slipper pil-op
* Registrere begge former i turtle systemet

---

# Først: Lav en bedre rumskib-form

I stedet for at bruge den standard "triangle" form, lad os lave vores egen!

* Placer denne kode under `HALF_HEIGHT` konstanten:
* ```python
  SPACESHIP_SHAPE = ( (7,-20), (0,5), (-7,-20) )
  ```
* Det er tre punkter der tegner en trekant: højre, top, venstre

---

# Så: Lav en form med ild!

Nu skal vi lave en sammensatt form med både rumskib OG ild:

```python
SPACESHIP_THRUST_SHAPE = turtle.Shape('compound')
SPACESHIP_THRUST_SHAPE.addcomponent(SPACESHIP_SHAPE, BG_COLOR, 'light grey')
SPACESHIP_THRUST_SHAPE.addcomponent(( (7,-20), (0,-30), (-7,-20) ), BG_COLOR, 'orange')
```

* `'compound'` betyder at vi kan have flere dele
* Første del: rumskibet (lys grå)
* Anden del: ilden (orange trekant bagved)

---

# Hvad betyder alle de tal?

Ildens form: `( (7,-20), (0,-30), (-7,-20) )`

* `(7,-20)` - højre hjørne (samme som rumskibet)
* `(0,-30)` - midten, længere ned (ilden peger bagud)
* `(-7,-20)` - venstre hjørne (samme som rumskibet)

Så ilden er en trekant der peger den modsatte vej!

---

# Registrer formerne i turtle systemet

Efter vi har lavet `screen`, skal vi registrere vores nye former:

```python
screen.register_shape("spaceship", SPACESHIP_SHAPE)
screen.register_shape("spaceship_thrust", SPACESHIP_THRUST_SHAPE)
```

* Nu kan vi bruge `"spaceship"` og `"spaceship_thrust"` som former
* Placer denne kode lige efter `screen.tracer(0)`

---

# Opdater `Player.__init__`

Spilleren skal nu bruge den nye form i stedet for "triangle":

* Find linjen der siger `self.shape("triangle")`
* Ret den til:
* ```python
  self.shape("spaceship")
  ```
* Vi kan også fjerne linjen med `shapesize`, da vores form allerede har den rigtige størrelse

---

# Før og efter i `Player.__init__`

**Før:**
```python
self.shape("triangle")
self.color("light grey", BG_COLOR)
self.shapesize(stretch_wid=0.75, stretch_len=1.5)
self.penup()
```

**Efter:**
```python
self.shape("spaceship")
self.color("light grey", BG_COLOR)
self.penup()
```

---

# Opdater `animate_spaceship()` funktionen

Nu skal vi skifte form når man trykker pil-op!

* Find `animate_spaceship()` funktionen
* Tilføj denne kode i slutningen af funktionen:
* ```python
      if keys_pressed["Up"]:
          player.shape("spaceship_thrust")
      else:
          player.shape("spaceship")
  ```

---

# Den komplette `animate_spaceship()` funktion

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

---

# Hvad sker der nu?

* Når du trykker pil-op: `player.shape("spaceship_thrust")` viser rumskibet med ild
* Når du slipper pil-op: `player.shape("spaceship")` viser rumskibet uden ild
* Det skifter hver gang i game loop, så det opdaterer hele tiden

---

# Prøv det!

Nu skulle rumskibet have orange ild når du giver gas! 🔥

* Tryk pil-op og se ilden komme ud bagved
* Slip tasten og ilden forsvinder
* Rumskibet fortsætter med at bevæge sig (fra sidste lektion)

---

# Bonus: Prøv at ændre farven!

I stedet for orange ild, prøv andre farver:

* `'red'` - rød ild
* `'yellow'` - gul ild  
* `'cyan'` - blå ild (som i sci-fi rumskibe!)
* `'white'` - hvid ild

Ret bare `'orange'` til en anden farve i `SPACESHIP_THRUST_SHAPE`!

---

# Bonus: Prøv at ændre formen!

Du kan også lave ilden større eller mindre ved at ændre tallene:

* `(0,-30)` styrer hvor langt ilden rækker
* Prøv `(0,-40)` for længere ild
* Eller `(0,-25)` for kortere ild

Eksperimenter og se hvad der ser bedst ud!

---

# Hvad lærte vi?

* Hvordan man laver custom former i turtle
* Hvordan man laver sammensatte former med flere dele
* Hvordan man skifter mellem former baseret på input
* Hvordan man registrerer former i turtle systemet
* At små animationer kan gøre et spil meget federe! ✨

---

# NU !!! Gå ind på:

## stefanug.trinket.io

- og klik "Build an Asteroids Game in Python"
- find Lesson 6 og "**20. Thrust Animation**"

Når I ser dette, så er der opgaver I skal løse, f.eks:

- ✅ Tilføj `SPACESHIP_SHAPE` konstanten
- ✅ Tilføj `SPACESHIP_THRUST_SHAPE` konstanten
- ✅ Registrer formerne med `screen.register_shape()`
