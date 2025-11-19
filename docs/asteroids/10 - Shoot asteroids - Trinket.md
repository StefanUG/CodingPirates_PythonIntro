# Skyde asteroider

Asteroiderne skal da kunne skydes

---

# Hvordan kan vi tjekke om en kugle har ramt en asteroide?

* Har de noget til fælles ?
* De er begge `Turtle`'s
* Så de har begge en position på skærmen
* Så vi kan finde afstanden mellem dem
* Hvis afstanden er mindre end asteroiden er stor, så har vi ramt den


---

# Den indbyggede `Turtle.distance` funktion

* Man kan spørge én `Turtle` hvor langt den er fra en anden `Turtle`
* f.eks. `asteroid.distance(bullet)`
* Det kan vi bruge i en funktion som vi kalder `check_collision`

---

# Asteroidens radius

Vi skal gemme på asteroiden hvor stor den er

* Altså dens radius: `self.radius = 30`
* Det skal vi sætte hvor ?
* I dens `__init__` funktion er et godt sted

```python
        self.radius = 30
```

- ✅ Indsæt koden i `Asteroid.__init__` funktionen

--- 

# Check Collision

Lad os lave en funktion til at tjekke om noget har ramt en asteroide.

* Vi skal lave en ny funktion: `def check_collision(with_turtle):`
    * Her er `with_turtle`, det som vi vil se har ramt en asteroide
* Så skal vi løbe listen af asteroider igennem: `for asteroid in asteroids:`
* For hver asteroide, tjekke om afstanden er mindre end radius: `if abs(with_turtle.distance(asteroid)) < asteroid.radius:`
    * Hvis ja, så returner asteroiden
* Ellers til sidst returnerer vi `None`



```python
def check_collision(with_turtle):
    # Check for collisions between a turtle and the asteroids
    for asteroid in asteroids:
        if abs(with_turtle.distance(asteroid)) < asteroid.radius:
            return asteroid
    return None
```

- ✅ Indsæt koden i `# BEHAVIOURS` sektionen


--- 

# Når vi flytter en kugle

Nu skal vi tjekke om vi har ramt, hver gang vi flytter en kugle (efter `bullet.move()` i `move_bullets` funktionen):

* Check om en asteroide er ramt: `hit_asteroid = check_collision(bullet)`
* Hvis vi ramte en: `if hit_asteroid:`
    * Skjul asteroiden: `hit_asteroid.hideturtle()`
    * Skjul kuglen: `bullet.hideturtle()`
    * Gør kuglen inaktiv: `bullet.active = False`



```python
            hit_asteroid = check_collision(bullet)
            if hit_asteroid:
                hit_asteroid.hideturtle()
                bullet.hideturtle()
                bullet.active = False
```

- ✅ Indsæt koden lige efter `bullet.move()` i `move_bullets` funktionen.

Hele din `move_bullets` funktion skal nu gerne se sådan ud:

```python
def move_bullets():
    player.cooldown()
    inactive_bullet = None
    for bullet in bullets:
        if bullet.active:
            bullet.move()
            hit_asteroid = check_collision(bullet)
            if hit_asteroid:
                hit_asteroid.hideturtle()
                bullet.hideturtle()
                bullet.active = False
        else:
            inactive_bullet = bullet

    if keys_pressed["space"] and inactive_bullet:
        player.shoot(inactive_bullet)
```

--- 

# Prøv spillet

- ✅ Start spillet og se om du kan skyde nogle asteroider

