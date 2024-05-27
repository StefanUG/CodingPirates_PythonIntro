# Move Spaceship

Et rumskib er ikke sjovt med mindre vi kan styre den.

# So let's move - Events

* Events er noget der sker, enten indenfor eller udenfor spillet
* De events kan vi "lytte" efter når noget sker
* f.eks. at et menneske trykker på en knap

Så for at flytte rumskibet skal vi lytte på nogle events. Det gør vi sådan her:

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

- ✅ Sæt koden ind i `CONSTANTS` sektionen, f.eks. efter de andre konstanter

---

# Ny sektion i koden til EVENTS

For at holde orden i vores kode, så lad os lave en ny sektion hvor vi holder alt vedrørende Events.

Denne sektion skal være efter GAME SETUP og før 

```python
#
#  EVENTS
#
```

- ✅ Sæt kommentaren i din fil før `# START THE SAME` sektionen


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

- ✅ Sæt koden ind i `CONSTANTS` sektionen

Kan I selv lave
- `press_right`
- `press_forward`

---

# Prøv spillet nu

### Kan I flytte rumskibet?


