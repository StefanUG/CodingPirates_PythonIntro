# Add asteroids

Nu er det på tide at få nogle asteroider

---

# Lad os starte med 10 asteroider

Lad os definere hvor mange vi max kan have

```python
MAX_ASTEROIDS = 10
```

- ✅ Indsæt koden i `CONSTANTS` sektionen

---

# Lad os så lave en klasse til vores asteroide?

* Hvad skal det være for en slags? Hvad skal den kunne?
* Og hvad kan det?
* En `Turtle` selvfølgelig ! 
* `class Asteroid(turtle.Turtle):`
* Og lige nu skal den ikke kunne andet


```python
class Asteroid(turtle.Turtle):

    def __init__(self):
        super().__init__()    
```

- ✅ Indsæt koden i `# CLASSES` sektionen

---

# Tilfældighed

Vi vil gerne have asteroiderne til at være tilfældige steder på skærmen...

* Uden vi selv skal bestemme det.
* Så lad os importere `random`: `import random`
* På den måde kan vi bruge den senere.


```python
import random
```

- ✅ Indsæt koden øverst i filen, efter `import turtle`

--- 

# Hver ny asteroide (`__init__`)

* Sætte dens form: `self.shape("circle")`
* Sætte formens størrelse: `self.shapesize(3, 3)`
* Sætte dens farve: `self.color("white", BG_COLOR)`
* Løfte pennen: `self.penup()`
* Udregne en tilfældig `x` og `y` position (kommer senere)
* Sætte dens position: `self.goto(x, y)`


```python
        self.shape("circle")
        self.shapesize(3, 3)
        self.color("white", BG_COLOR)
        self.penup()
```

- ✅ Indsæt koden i `Asteroid.__init__` funktionen

--- 

# Udregne en tilfældig position

* `random.randint(a, b)` er en funktion, som giver et tilfældigt tal mellem tallet `a` og `b` 
* Så hvis `a = 0` og `b = 3` hvad kan den så returnere ?
* Hvad er vores `a` og `b`?
* For at finde x: `x = random.randint(-HALF_WIDTH, HALF_WIDTH)`
* For at finde y: `y = random.randint(-HALF_HEIGHT, HALF_HEIGHT)`

```python
        x = random.randint(-HALF_WIDTH, HALF_WIDTH)
        y = random.randint(-HALF_HEIGHT, HALF_HEIGHT)
        self.goto(x, y)
```

- ✅ Indsæt koden i `Asteroid.__init__` funktionen

--- 

# Når spillet starter: Lav asteroiderne

* I `# GAME SETUP`
* En liste til at have dem i: `asteroids = []`
* Lav så mange asteroider som vi har defineret:
    ```python
    for i in range(MAX_ASTEROIDS):
        asteroids.append(Asteroid())
    ```

Hele koden:

```python
# Create asteroids
asteroids = []
for i in range(MAX_ASTEROIDS):
    asteroids.append(Asteroid())
```

- ✅ Indsæt koden i `# GAME SETUP` sektionen

---

# Prøv spillet

- ✅ Start spillet og se om der kommer nogle asteroider frem
