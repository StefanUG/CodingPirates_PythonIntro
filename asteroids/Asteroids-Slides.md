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

# Python Game Development

## Asteroids

med Turtle Graphics

---

# Lad os installere et IDE

> Integrated Development Environment

## PyCharm Community Edition: 
- https://www.jetbrains.com/pycharm/download/

### Og gør jer klar til at kode

- Hav et projekt klar i dit IDE
- Lav en ny fil, f.eks. `asteroids.py`

---

# Turtle's 
# koordinat system

![bg contain](slide-resources/coordinate-system.svg)

---

# Lad os holde orden i tingene

<div class="container">

<div class="col">
Opdeling af koden

1. Imports øverst
2. Definere konstanter
3. (Classes) - kommer senere
4. Game setup
5. Events
6. Behaviours
7. (Game Loop)
8. Start the game
</div>

<div class="col">

```python
import turtle
# CONSTANTS, e.g.
SCREEN_WIDTH = 1200  # en konstant
# CLASSES, e.g.
class Asteroid(turtle.Turtle): 
# GAME SETUP, e.g.
player = turtle.Turtle()
# EVENTS, e.g.
screen.onkey(press_up, "Up")
# BEHAVIOURS, e.g.
def move_spaceship():
# GAME LOOP, e.g.
def update():
# START THE GAME, e.g.
screen.mainloop()
```

</div>

</div>


---

# Kommentarer

De er der for at hjælpe jer. I behøver ikke skrive dem.

```python
#
#  GAME SETUP
#

player.penup() # to not draw lines
```

Hvis I gør, så skriv **hvorfor** og ikke **hvad**.
Jeg skriver måske lidt **hvad**, men for at hjælpe jer til bedre at forstå koden til at starte med.

---

# Lad os komme i gang

## Start med at importere turtle

så vi kan bruge den i vores kode

```python
import turtle
```

---

# Lad os definere nogle konstanter

Det gør det nemmere at justere spillet senere hen

```python
#
#  CONSTANTS
#

SCREEN_WIDTH = 1200 # Bredden på skærmbilledet
SCREEN_HEIGHT = 800 # Højden
BG_COLOR = "black" # Baggrundsfarven
```

En konstant er en slags variabel, men som ikke ændrer sig mens programmet kører

---

# Bagefter sætter vi skærmen op

```python
#
#  GAME SETUP
#

# Set up the screen
screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT) # width and height
screen.bgcolor(BG_COLOR) # background color
screen.tracer(0) # disable the built in movement animation of turtle
```

Det laver vinduet, sætter størrelsen og baggrundsfarven på det, og slår den indbyggede bevægelses-animation fra.

---

# Lad os lave et rumskib

```python
# Make a turtle for the player
player = turtle.Turtle()
player.shape("triangle")
player.color("light grey", BG_COLOR)
player.penup() # to not draw lines
```

- Her bruger vi en `triangle` shape til vores turtle, sætter den til lysegrå med sort fyld.
- Til sidst løfter vi pen'en, så den ikke tegner streger efter sig.


---

# Lad os se vores spil

```python
#
#  START THE GAME
#

screen.update() # Since we disabled the tracer, we manually have to update the screen
screen.mainloop() # don't close the window
```

- Nu skal vi opdatere skærmen med det vi har sat på den: rumskibet.
- Det skal vi selv gøre fordi vi har slået `tracer` (aninationen) fra.
- Og den sidste linie i koden kalder vi `mainloop` funktionen, så programmet ikke stopper


---

# _     Ser det sådan ud?

![bg fit](slide-resources/asteroids-01-screenshot.png)

---

# Samlet set

<div class="container">

<div class="col">

```python
import turtle

#
#  CONSTANTS
#
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
BG_COLOR = "black"

#
#  GAME SETUP
#
screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor(BG_COLOR)
screen.tracer(0)  # disable animation

```

</div>

<div class="col">

```python
# Make a turtle for the player
player = turtle.Turtle()
player.shape("triangle")
player.color("light grey", BG_COLOR)
player.penup()  # to not draw lines


#
#  START THE GAME
#

screen.update()
screen.mainloop()



```

</div>

</div>

---

# Skal vi have rumbkibet til at se lidt bedre ud ?

```python
# Stretch the triangle to be pointy
player.shapesize(stretch_wid=0.75, stretch_len=1.5)
```

- Her strækker vi den i længden så den ligner mere et rumskib

Hvor skal vi sætte den kode ind?

---

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

screen.onkey(press_left, "Left")
```

Kan I selv lave
- `press_right`
- `press_forward`

---

# Prøv spillet nu

### Kan I flytte rumskibet?


