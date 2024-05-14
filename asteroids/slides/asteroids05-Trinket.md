# Fire one Bullet

Nu skal vi have rumskibet til at skyde en kugle. En `Bullet`

---

# Kuglens hastighed

Lad os sætte kuglens hastighed til at være dobbelt så hurtig som spillerens, og gemme det som en konstant.

```python
BULLET_SPEED = PLAYER_SPEED * ???
```

- ✅ Sæt koden ind i `CONSTANTS` sektionen
- ✅ Erstat `???` så `BULLET_SPEED` er dobbelt så meget som `PLAYER_SPEED`.

## Ny sektion til vores `Classes`

Lav en ny kommentar efter konstanterne og før `Events`

```python
#
#  CLASSES
#
```

- ✅ Indsæt kommentaren efter konstanterne og før `Events`

---

# Ny klasse til vores `Bullet`

Lad os starte simpelt med strukturen til vores `Bullet` klasse.

```python
class Bullet(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.active = False

    def fire(self, start):
        self.active = True

    def move(self):
        self.forward(BULLET_SPEED)
```

- ✅ Sæt koden ind i den nye `CLASSES` sektion

--- 

# Hver ny kugle (`__init__`)

For hver ny kugle skal vi 

1. Definere dens `shape` og `shapesize`
    ```python
            self.shape("square")
            self.shapesize(stretch_wid=0.2, stretch_len=0.2)
    ```
2. Sætte dens farve
    ```python
            self.color("light grey")
    ```
3. Løfte penen
    ```python
            self.penup()
    ```
4. Skjule den, så den ikke er synlig før den bliver affyret
    ```python
            self.hideturtle()
    ```
5. ~~lave en ny variabel til at holde styr på om den er aktiv eller ej~~ allerede gjort


- ✅ Sæt alle kodelinerne ind i `__init__` funktionen

--- 

# Når kuglen affyres (`fire`)

Når kuglen affyres, skal vi

1. ~~Sætte den til aktiv (`self.active = False`)~~ allerede gjort
2. Flytte den til start positionen
    ```python
            self.setposition(start.xcor(), start.ycor())
    ```
   Her tager vi x- og y-koordinaterne fra `start`, som er spilleren.
3. Sætte retningen den skal flyve i
    ```python
            self.setheading(start.heading())
    ```
   Her tager vi heading fra `start`, som er spilleren.
4. Vise den
    ```python
            self.showturtle()
    ```

- ✅ Sæt alle kodelinerne ind i `fire` funktionen

--- 

# Når kuglen flytter sig (`move`)

Hver gang kuglen flytter sig. I hvert game loop skal vi:

1. ~~Flytte den lidt~~ allerede gjort
2. Hvis den er kommet ud over kanten
    * Skjule den
    * Sætte den til inaktiv (`self.active = False`)
    ```python
            if abs(self.xcor()) > HALF_WIDTH or abs(self.ycor()) > HALF_HEIGHT:
                self.hideturtle()
                self.active = False
    ```

- ✅ Sæt alle kodelinerne ind i `move` funktionen

--- 

# Lav en ny kugle

Vi skal have en ny `Bullet` i `# GAME SETUP` sektionen

```python
bullet = Bullet()
```

- ✅ Sæt koden ind i `GAME SETUP` sektion. Før `EVENTS`.

---

# Ny behavior til at flytte kuglen

Vi skal have en ny "Behaviour" / en ny funktion.

1. Lad os kalde den `move_bullets()`
    ```python
    def move_bullets():
    ```
2. Hvis "space" er trykket ned - og kuglen IKKE allerede er affyret (er aktiv), skal kuglen affyres
    ```python
        if keys_pressed["???"] and not bullet.active:
            bullet.fire(player)
    ```
3. Hvis kuglen er aktiv, skal den flyttes frem
    ```python
        if bullet.???:
            bullet.move()
    ```

- ✅ Lav funktionen `move_bullets` i `BEHAVIOURS` sektionen.
- ✅ Indsæt koden fra punkt 2 og 3 i funktionen.
- ✅ Ret `???` til så koden fungerer efter hensigten

---

# Opdater game loop

Nu skal den nye funktion kaldes fra vores game loop

```python
    move_bullets()
```

- ✅ Indsæt koden i `update` game loop funktionen, efter `move_spaceship()`

---

# Prøv spillet

- ✅ Start spillet og se hvad der sker når du skyder en kugle
