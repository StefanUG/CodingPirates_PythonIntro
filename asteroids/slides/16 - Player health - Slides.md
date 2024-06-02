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

# Til at skrive `HEALTH` ændrer sig

Når man først har skrevet noget kan man ikke nemt fjerne det igen. Man kan enten

1. fjerne alt fra hele skærmen, 
2. fjerne alt en turtle har skrevet

- Men man kan ikke slette enkelte dele af noget som en enkelt turtle har lavet.

Så vi skal have nye Turtles til at skrive det som ændrer sig

--- 

# En `score_pen` til at skrive score

* Vi skal lave en ny `score_pen`
* Skrive med hvid farve
* Løfte pennen så der ikke kommer streger
* Flytte den til det efter "SCORE: "
* ```python
  score_pen = turtle.Turtle(visible=False)
  score_pen.color("white")
  score_pen.penup()
  score_pen.goto(-HALF_WIDTH + 90, HALF_HEIGHT - 30)
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

# Når asteroiden bliver ramt

En asteroide kan blive ramt.

* Så lad os på klassen definere hvad der sker når den rammes
* Ny funktion på `Asteroid`, kaldet `hit`
* Så skal den skjule sig
* Og sætte tælleren, så der kan tælles ned
* ```python
      def hit(self):
          self.hideturtle()
          self.respawn_in = ASTEROID_RESPAWN_AFTER
  ```

---

# Kald den nye `Asteroid.hit` funktion

Der hvor vi før blot skjulte asteroiden når den blev ramt, skal vi nu kalde `hit` funktionen i stedet for.

* Før:
  ```python
              if hit_asteroid:
                  hit_asteroid.hideturtle()
  ```
* Efter:
  ```python
              if hit_asteroid:
                  hit_asteroid.???()
  ```

---

# Tæl ned, hvis asteroiden ikke er synlig

* I `move_asteroids` funktionen kan vi tælle ned på hver asteroide, hvis den ikke er synlig.
* Vi har allerede en `if asteroid.isvisible():` block
* Så vi kan sætte en `else:` block bagefter
* Her tæller vi `respawn_in` ned
* Og nulstiller asteroiden hvis tælleren er 0

---

# Tæl ned, hvis asteroiden ikke er synlig

Det ser sådan udÆ

```python
        else:
            asteroid.respawn_in -= 1
            if asteroid.respawn_in == 0:
                asteroid.reset()
```


---

# Men hvad gør `reset()` ?

Vi har ikke lavet nogen reset funktion på Asteroid. Det skal vi nu!

* Men skal asteroiden have samme retning og hastighed som da den forsvandt?
* Det synes jeg ikke!
* Så lad reset funktion sætte tilfældig retning og hastighed
* Altså flytte koden fra `__init__` ned i den
* Og så vise asteroiden.

---

# Reset funktionen

Sådan kan `reset` funktionen se ud:

```python
  def reset(self):
      self.setheading(random.randint(0, 360))
      self.speed = random.randint(ASTEROID_SPEED_MIN, ASTEROID_SPEED_MAX)
      self.showturtle()
```

---

# Kald reset ved ny asteroide

Vi skal stadig have en ny asteroide til at sætte en retning og hastighed, men hvordan nu hvor vi har flyttet det fra `__init__`

* Det kan vi gøre ved at kalde `reset` fra `__init__` funkitonen:
* Vi skal også huske den gode skik, og sætte `speed` fra `__init__` funktionen
* ```python
        self.reset()
        self.speed = 0
  ```

---

# NU !!! Gå ind på:

## stefanug.trinket.io

- og klik "Build an Asteroids Game in Python"
- find Lesson 5 og "**15. Respawn asteroids**"

Når I ser dette, så er der opgaver I skal løse, f.eks:

- ✅ Sæt koden ind i `CONSTANTS` sektionen

 