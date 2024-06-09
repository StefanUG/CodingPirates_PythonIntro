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

## Skal vi ikke have mere end et liv?

Kun en enkelt chance inden man er game over?

Vi skal da have nogle flere liv: Player Health

---

# Mere tekst som *ikke* ændrer sig

* Vi har stadig en `pen`-Turtle, til at skrive på skærmen med
* Den skal vi flytte til under "SCORE"
* Og så kan vi skrive "HEALTH"
* ```python
  pen.goto(-HALF_WIDTH + 20, HALF_HEIGHT - 60)
  pen.write("HEALTH: ", font=SCORE_FONT)
  ```

---

# En `health_pen` til at skrive antal liv

* Vi skal lave en ny `health_pen`
* Skrive med hvid farve
* Løfte pennen så der ikke kommer streger
* Flytte den til det efter "HEALTH: "
* ```python
  health_pen = turtle.Turtle(visible=False)
  health_pen.color("white")
  health_pen.penup()
  health_pen.goto(-HALF_WIDTH + 90, HALF_HEIGHT - 60)
  ```

---

# Hvor mange liv skal vi have?

* Lad os definere en konstant 
* med måske `3` liv?
* ```python
  PLAYER_START_HEALTH = 3
  ```

--- 

# `Player.health`

Nu skal spilleren have noget liv, så vi kan tælle det ned.

* Til det skal vi bruge en variabel på `Player` klassen
* Kald den `health`
* Sæt den til `PLAYER_START_HEALTH` i første omgang
* ```python
          self.health = PLAYER_START_HEALTH
  ```

--- 

# Funktion til at skrive `player.health`

Vi skal skrive antal liv på skærmen hver gang den ændrer sig, så lad os lave en ny funktion til det.

* Lad os kalde den `draw_health`
* Den skal rydde det den tidligere har skrevet
* skrive det nye antal liv
* ```python
  def draw_health():
      health_pen.clear()
      health_pen.write(player.health, font=SCORE_FONT)
  ```

---

# Når rumskibet bliver ramt

Hvad skal der ske når rumskibet bliver ramt ?

* Ny `hit` opførsel på `Player` klassen
* Vi skal trække en fra `health`
* Opdatere antal liv tilbage på skærmen
* Hvis spilleren har 0 liv tilbage skal vi sætte `alive` til `False`

---

# Ny `hit` funktion på `Player` klassen

Det kan skrives sådan her

```python
      def hit(self):
          self.health -= 1
          draw_health()

          if self.health == 0:
              self.alive = False
  ```

---

# Hvor (i koden) bliver man ramt ?

* Før havde vi logik i `move_asteroids` som siger spilleren ikke er i live mere, når den bliver ramt.
* Før:
  ```python
                  player.alive = False
  ```
* Nu skal vi kalde den nye funktion i stedet for
* Efter:
  ```python
                  player.hit()
  ```

---

# Også i `move_spaceship`

* Vi havde en lignende logik i `move_spaceship` som siger spilleren ikke er i live mere, når man flyver ind i en asteroide
* Før:
  ```python
                  player.alive = False
  ```
* Nu skal vi kalde den nye funktion i stedet for
* Efter:
  ```python
                  player.hit()
  ```

---

# Manger bare at skrive liv ved start

Nu mangler vi kun en ting:

* At skrive antal liv på skørmen
* ... når spillet starter
* ```python
  draw_health()
  ```

---

# NU !!! Gå ind på:

## stefanug.trinket.io

- og klik "Build an Asteroids Game in Python"
- find Lesson 6 og "**16. Player Health**"

Når I ser dette, så er der opgaver I skal løse, f.eks:

- ✅ Sæt koden ind i `CONSTANTS` sektionen

 