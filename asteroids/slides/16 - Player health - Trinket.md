# Player Health

## Skal vi ikke have mere end et liv?

Kun en enkelt chance inden man er game over?

Vi skal da have nogle flere liv: Player Health

---

# Mere tekst som *ikke* ændrer sig

* Vi har stadig en `pen`-Turtle, til at skrive på skærmen med
* Den skal vi flytte til under "SCORE"
* Og så kan vi skrive "HEALTH"

```python
pen.goto(-HALF_WIDTH + 20, HALF_HEIGHT - 60)
pen.write("HEALTH: ", font=SCORE_FONT)
```

- ✅ Sæt koden ind i `#  GAME SETUP` sektionen, f.eks. efter vi lige har skrevet "SCORE" ud på skærmen.


---

# En `health_pen` til at skrive antal liv

* Vi skal lave en ny `health_pen`
* Skrive med hvid farve
* Løfte pennen så der ikke kommer streger
* Flytte den til det efter "HEALTH: "

```python
health_pen = turtle.Turtle(visible=False)
health_pen.color("white")
health_pen.penup()
health_pen.goto(-HALF_WIDTH + 90, HALF_HEIGHT - 60)
```

- ✅ Sæt koden ind i `#  GAME SETUP` sektionen, f.eks. efter vi har sat `score_pen` op.


---

# Hvor mange liv skal vi have?

* Lad os definere en konstant 
* med måske `3` liv?

```python
PLAYER_START_HEALTH = 3
```

- ✅ Sæt koden ind i `#  CONSTANTS` sektionen


--- 

# `Player.health`

Nu skal spilleren have noget liv, så vi kan tælle det ned.

* Til det skal vi bruge en variabel på `Player` klassen
* Kald den `health`
* Sæt den til `PLAYER_START_HEALTH` i første omgang

```python
        self.health = PLAYER_START_HEALTH
```

- ✅ Sæt koden ind i `Player.__init__` funktionen, f.eks. efter vi har sat `self.score` til `0`.

--- 

# Ny funktion til at skrive `player.health`

Vi skal skrive antal liv hver gang den ændrer sig, så lad os lave en ny funktion til det.

* Lad os kalde den `draw_health`
* Den skal rydde det den tidligere har skrevet
* skrive det nye antal liv

```python
def draw_health():
    health_pen.clear()
    health_pen.write(player.health, font=SCORE_FONT)
```

- ✅ Sæt koden ind i `#  BEHAVIOURS` sektionen, f.eks. efter `draw_score` funktionen.

---

# Når rumskibet bliver ramt

Hvad skal der ske når rumskibet bliver ramt ?

* Ny `hit` opførsel på `Player` klassen
* Vi skal trække en fra `health`
* Opdatere antal liv tilbage på skærmen
* Hvis spilleren har 0 liv tilbage skal vi sætte `alive` til `False`


```python
      def hit(self):
          self.health -= 1
          draw_health()

          if self.health == 0:
              self.alive = False
```

- ✅ Sæt koden ind i `Player` klassen, f.eks. efter `cooldown` funktionen.

---

# Hvor (i koden) bliver man ramt ?

* Før havde vi logik i `move_asteroids` som siger spilleren ikke er i live mere, når den bliver ramt.

Før:

```python
                player.alive = False
```

Nu skal vi kalde den nye funktion i stedet for

Efter:

```python
                player.hit()
```

Vi havde en lignende logik i `move_spaceship` som siger spilleren ikke er i live mere, når man flyver ind i en asteroide


- ✅ I `move_asteroids` funktionen, find `player.alive = False` og erstat det med `player.hit()`.
- ✅ I `move_spaceship` funktionen, find `player.alive = False` og erstat det med `player.hit()`.

---

# Manger bare at skrive liv ved start

Nu mangler vi kun en ting:

* At skrive antal liv på skørmen
* ... når spillet starter

```python
draw_health()
```

- ✅ Indsæt koden i `#  START THE GAME` sektionen, f.eks. efter `draw_score()`

---

## Prøv spillet

- ✅ Prøv spillet og se om ikke dine liv tæller ned
