# Game over når rumskibet flyver ind i en asteroide

Kan rumskibet flyve igennem asteroiderne?

Det er da ikke meningen! Lad os lave så der er "Game Over" hvis det sker.

---

# Kan I huske Check Collision ?

* `check_collision` funktionen tager en `Turtle` som parameter
* Og tjekker om den `Turtle` kolliderer med en af asteroiderne
* Kan vi bruge det til at se om spilleren kolliderer?
* Er vores `Player` en `Turtle` ?
* JA DA!

---

# Hvor skal vi mon tjekke det ?

* Hvor giver det mening at se om rumskibet kolliderer med en asteroide ?
* Måske efter hver gang vi har flyttet rumskibet ?
* Så der kan vi lave en ny `if` sætning:
  ```python
    if check_collision(player):
  ```
* Men hvad skal der ske ?

--- 

# `Player.alive`


* Vi skal holde styr på mere tilstand, mere "state" om spilleren.
* Ud over `fire_cooldown` som vi tilføjede, skal vi nu have en ting mere, nemlig `alive`
* Det kan vi sætte ind i `Player.__init__` funktionen
  ```python
  self.alive = True
  ```
* Og efter vores `if`-sætning fra før, kan vi nu kalde
  ```python
          if check_collision(player):
              player.alive = False
  ```

- ✅ Indsæt `self.alive = True` i `Player.__init__` funktionen, f.eks. efter `self.fire_cooldown = 0`
- ✅ Indsæt `if` blokken i `move_spaceship` funktionen under `# BEHAVIOURS` sektionen, så det bliver kaldt lige efter `move_if_out_of_bounds(player)`

--- 

# Når spilleren ikke er `alive` mere

Hvad skal der så ske?

* Hvor skal vi tjekke om spilleren er i live ?
* Giver det mening at tjekke det i hvert game loop ?
* Måske inden vi kalder et nyt game loop ?
* Så kan vi bruge `if`/`else`
  ```python
        if player.alive:
            screen.ontimer(update, GAME_TICK)
        else:
          # GAME OVER
  ```

--- 

# Men hvordan skriver vi "Game Over"

En `Turtle` kan skrive 🐢✍️

* Lad os lave en ny `Turtle` til at skrive med
* Lad os kalde den `pen`
* Og give den en hvid farve

```python
# A pen to write stuff to the screen
pen = turtle.Turtle(visible=False)
pen.color("white")
```

- ✅ Indsæt koden i `# GAME SETUP` sektionen, f.eks. efter `player = Player()`

--- 

# Skrifttype 

Vi gider ikke hele tiden at skrive hvilken skrifttype vi vil skrive med, så lad os definere en konstant til det. Vi vil bruge skrifttypen "Courier New". Det er en "fixed width" type, som passer til vores spil.

```python
FONT_FAMILY = "Courier New"
```

- ✅ Indsæt koden i `# CONSTANTS` sektionen


Og så kan `Turtle` skrive noget sådan her:

```python
pen.write("GAME OVER", align="center", font=(FONT_FAMILY, 68, "normal"))
```

--- 

# Færdiggøre `update` game loop

Nu kan vi færdiggøre `if`/`else` i vores game loop

```python
      if player.alive:
          screen.ontimer(update, GAME_TICK)
      else:
        pen.write("GAME OVER", align="center", font=(FONT_FAMILY, 68, "normal"))
```

- ✅ Indsæt koden i `update` funktionen under `# GAME LOOP` sektionen, så den erstatter den nuværende linie med `screen.ontimer`


--- 

# Prøv spillet

- ✅ Start spillet og se om der bliver GAME OVER ved at flyve ind i en asteroide


--- 

# Udfordringer

Hvis du er hurtig kan du prøve om du kan:

- Bruge en skrifttype kaldet `fixedsys`, som er en gammel skrifttype der ser ret sej ud. Den skal downloades, da computeren ikke kommer med skrifttypen selv.
