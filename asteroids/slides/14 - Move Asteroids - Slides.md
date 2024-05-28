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

## Asteroider som flytter sig

De stillestående asteroider er ikke så sjovt. 

Lad os få dem til at flytte sig

---

# Asteroidernes hastighed

* Vi får dem til at flytt sig med forskellig hastighed
* Så vi skal definere en minimum og maksimum hastighed
* Her i antal pixels den skal rykke i hvert tick
* ```python
  ASTEROID_SPEED_MIN = 1
  ASTEROID_SPEED_MAX = 5
  ```

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

---

# Tilfældig hastighed

Asteroiden skal også have en tilfældig hastighed

* En `Turtle` har ikke selv en hastighed
* Lad os definere en selv og kalde det for `speed`
* Og så bruge `random` til at være en tilfældig hastighed mellem min og maks
* Sådan her:
  ```python
        self.speed = random.randint(ASTEROID_SPEED_MIN, ASTEROID_SPEED_MAX)
  ```

---

# Ny opførsel til at flytte asteroiderne

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

--- 

# Kald den nye behaviour

I vores game loop skal vi huske at kalde den funktion vi har lavet:

```python
    move_asteroids()
```
--- 

# Et par ekstra ting

Dem kan I se og finde ud af selv, når i gennemgår guiden.

---

# NU !!! Gå ind på:

## stefanug.trinket.io

- og klik "Build an Asteroids Game in Python"
- find Lesson 5 og "**14. Move asteroids**"

Når I ser dette, så er der opgaver I skal løse, f.eks:

- ✅ Sæt koden ind i `CONSTANTS` sektionen

 