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

## Flytte rumskibet

---

# I dag skal vi lære om

* Events
* altså at "lytte" på når noget sker udenfor spillet
* f.eks. at et menneske trykker på en knap

---

# At "lytte" efter Events

- For at flytte rumskibet skal vi lytte på nogle events.

```python
screen.listen()  # Fortæl turtle screen at den skal lytte på events.
screen.onkey(function, key)
```

### Men hvad er function og key ?

* `funktion` skal være navnet på en funktion som kaldes
* når `key`-knappen den trykkes på

---

# Lad os starte med nogle konstanter

### Rotate speed og Player speed

Vi skal bestemme den hastighed rumskibet drejer rundt og flytter sig med.

```python
ROTATE_SPEED = 5
PLAYER_SPEED = 10
```

At have disse ting i konstanter gør det nemmere at rette til senere, hvis man ønsker at justere hastigheden.

---

# Functions / funktioner

- Vi skal lave en funktion som bliver kaldt når noget sker...
 
f.eks. når vi trykker på "Left", alstå den venstre piletast

```python
def press_left():
    player.left(ROTATE_SPEED)
    screen.update()

screen.listen()
screen.onkey(press_left, "Left")
```

---

# NU !!! Gå ind på:

## stefanug.trinket.io

- og klik "Build an Asteroids Game in Python"
- find Lesson 1 og "**2. Move spaceship**"

Når I ser dette, så er der opgaver I skal løse, f.eks:

- ✅ Sæt koden ind i `CONSTANTS` sektionen

