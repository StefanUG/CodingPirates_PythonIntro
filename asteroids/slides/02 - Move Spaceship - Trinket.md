
# Let's move - Events

- For at flytte rumskibet skal vi lytte på nogle events.

```python
screen.listen()  # Fortæl turtle screen at den skal lytte på events.
screen.onkey(function, key)
```

### Men hvad er function og key ?

---

# Lad os starte med nogle konstanter

### Rotate speed og Player speed

```python
ROTATE_SPEED = 5
PLAYER_SPEED = 10
```

Det gør det nemmere at rette til senere, hvis man øsnker at justere hastigheden.

---

# Functions / funktioner

- Vi skal lave en funktion som bliver kaldt når noget sker...
 

```python
def press_left():
    player.left(ROTATE_SPEED)
    screen.update()

screen.listen()
screen.onkey(press_left, "Left")
```

Kan I selv lave
- `press_right`
- `press_forward`

---

# Prøv spillet nu

### Kan I flytte rumskibet?


