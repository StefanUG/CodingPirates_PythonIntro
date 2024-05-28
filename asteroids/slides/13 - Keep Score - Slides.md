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

## Lad os tælle point

Lad os tælle hvor mange point du får.

---

# `Player.score`

* Endnu mere tilstand, endnu mere "state" om spilleren.
* Nu skal vi også have `score` på
* Det kan vi sætte ind i `Player.__init__` funktionen
  ```python
  self.score = 0
  ```
* Og hver gang vi rammer en asteroide, kan vi lægge en til scoren
  ```python
                  player.score += 1
  ```

--- 

# Skrift til vores score

Det er fint vi holder styr på scoren, men vi skal vel også skrive det på skærmen?

* Selvfølgelig! 
* Vi kommer til at skrive mere end en ting med samme skrift, størrelse og justering.
* Lad os definere det i en konstant
  ```python
  SCORE_FONT = (FONT_FAMILY, 16, "normal")
  ```
---

# Til det tekst som *ikke* ændrer sig

* Vi har lavet en `pen`-Turtle, til at skrive på skærmen med
* Lad os sikre den ikke tegner streger når vi flytter den
* Så skal vi flytte pen'en til øverste venstre hjørne
* Og så kan vi skrive "SCORE"
* ```python
  pen.penup()
  pen.goto(-HALF_WIDTH + 20, HALF_HEIGHT - 30)
  pen.write("SCORE: ", font=SCORE_FONT)
  ```

---

# Til det som ændrer sig

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

# Ny funktion til at skrive `player.score`

Vi skal skrive scoren hver gang den ændrer sig, så lad os lave en ny funktion til det.

* Lad os kalde den `draw_score`
* Den skal rydde det den tidligere har skrevet
* skrive den nye score
* ```python
  def draw_score():
      score_pen.clear()
      score_pen.write(player.score, font=SCORE_FONT)
  ```

--- 

# Kald funktionen

Nu skal vi kalde funktionen så vi kan skrive scoren.

* Når spillet starter
* Hver gang scoren ændrer sig
* 
  ```python
  draw_score()
  ```

--- 

# Flytte `pen` tilbage

Nu skrev vi jo SCORE med den samme pen som vi vil skrive GAME OVER med. 

* Men vi har ikke flyttet den tilbage til midten af skærmen endnu.
* Lad os flytte den til midten, inden vi skriver GAME OVER:
* ```python
          pen.goto(0, 0)
  ```

---

# NU !!! Gå ind på:

## stefanug.trinket.io

- og klik "Build an Asteroids Game in Python"
- find Lesson 5 og "**13. Keep Score**"

Når I ser dette, så er der opgaver I skal løse, f.eks:

- ✅ Sæt koden ind i `CONSTANTS` sektionen

 