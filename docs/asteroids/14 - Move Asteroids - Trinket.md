## Move asteroids

De stillestående asteroider er ikke så sjovt. 

Lad os få dem til at flytte sig

---

# Asteroidernes hastighed

* Vi får dem til at flytt sig med forskellig hastighed
* Så vi skal definere en minimum og maksimum hastighed
* Her i antal pixels den skal rykke i hvert tick

```python
ASTEROID_SPEED_MIN = 1
ASTEROID_SPEED_MAX = 5
```

- ✅ Sæt koden ind i `# CONSTANTS` sektionen

--- 

# Tilfældig Retning

Hver gang en ny asteroide laves, skal vi give den en tilfældig hastighed og retning.

* Hvor i koden giver det mening at gøre det?
* I `Asteroid.__init__` funktionen.
* Så skal vi bruge `random.randint` igen. Kan I huske hvad den gør?
* "Heading" er den retning i grader (0-360), som asteroiden "peger"
* Sådan her:
  ```python
        self.setheading(random.randint(0, 360))
  ```

- ✅ Sæt koden ind i `Asteroid.__init__` funktionen


---

# Tilfældig hastighed

Asteroiden skal også have en tilfældig hastighed

* En `Turtle` har ikke selv en hastighed
* Lad os definere en selv og kalde det for `speed`
* Og så bruge `random` til at være en tilfældig hastighed mellem min og maks
* Sådan her:
* Sådan her:
  ```python
        self.speed = random.randint(ASTEROID_SPEED_MIN, ASTEROID_SPEED_MAX)
  ```

- ✅ Sæt koden ind i `Asteroid.__init__` funktionen

---

# Opførsel til at flytte asteroiderne

I hvert game loop skal vi flytte asteroiderne.

* Ny behaviour funktion til det
* Lad os kalde den `move_asteroids`
* Den skal løbe alle asteroiderne igennem, og for hver
* Hvis asteroiden er synlig
* flytte den fremad

* Er det nok ? Prøv det efter vi har lavet et kald til funktionen.

--- 

# Funktion til den nye opførsel

Det kan vi skrive sådan her:

```python
def move_asteroids():
    for asteroid in asteroids:
        if asteroid.isvisible():
            asteroid.forward(asteroid.speed)
```

- ✅ Sæt koden ind i `#  BEHAVIOURS` sektionen

--- 

# Kald den nye behaviour

I vores game loop skal vi huske at kalde den funktion vi har lavet:

```python
    move_asteroids()
```

- ✅ Sæt koden ind i `update` funktionen, f.eks. efter `move_bullets()`

--- 

# Prøv spillet

- ✅ Start spillet og se om der mangler noget i asteroidernes opførsel
- f.eks. når asteroiderne flytter sig ud af skærmne ?
- eller når rumskibet holder stille ?

--- 

# Wrap asteroid

Giver det mening at flytte asteroiden hvis den kommer ud af skærmen?

* Så i `move_asteroids` skal vi lave et kald til `move_if_out_of_bounds`

```python
            move_if_out_of_bounds(asteroid)
```

- ✅ Sæt koden ind i `move_asteroids` funktionen efter vi har rykket en asteroide fremad

--- 

## Prøv igen

- ✅ Start spillet og se om der mangler andet
- f.eks. når rumskibet holder stille ?

--- 

# Player collision

Det giver måske også mening at tjekke om vi har ramt spilleren, hver gang vi flytter en asteroide?

* Så hvis afstanden fra asteroiden til spilleren er mindre end asteroidens størrelse, så bliver spilleren ramt

```python
            if abs(player.distance(asteroid)) < asteroid.radius:
                player.alive = False
```

- ✅ Sæt koden ind i `move_asteroids` funktionen efter den anden linie du lige satte ind

---

## Prøv igen nu

- ✅ Start spillet og se om alt er som det skal være
