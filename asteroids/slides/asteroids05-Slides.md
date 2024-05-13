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

## Skyde en kugle


---

# Nu skal vi lære om

* Classes

... og få rumskibet til at skyde

---

# Kender I Classes i programmering?

* Hvad tænker I når I hører det?
* Har I hørt om klassificeringer ?
* F.eks. i dyreriget?
* Hvirveldyr er en klassificering af dyr med rygrad.
* Varm-blodige dyr er en klassificering af dyr med rygrad.
* Pattedyr er en klassificering af varmblodige dyr

---

![bg fit](resources/classification-of-animals.jpg)

by <a href="https://www.freepik.com/free-vector/hand-drawn-classification-animals-infographic_26526557.htm">Freepik</a>

---

# Classes i programmering er lidt det samme

* Det definerer en entitet som deler nogle egenskaber
* F.eks. om det har en rygrad eller ej, elle om det er varmblodigt.

<div class="container">
<div class="col">

```python
class Animal:

    def eat(self):
        print("Animal is eating")

ant = Animal()
ant.eat()
```

</div>
<div class="col">

```python
class Bird(Animal):

    def fly(self):
        print("Bird is flying")

hawk = Bird()
hawk.eat()
```

</div>
</div>

---

# En Kugle er en Turtle !?!

En Turtle i Python kan flytte sig...
Men nu skal vi have en kugle til at kunne flere ting:

* affyres 
* ... og fra det sted rumskibet er
* ramme asteroider

Så vores `Bullet` skal være en `turtle.Turtle`, men kan flere ting.

---

# Det kan vi gøre således

```python
class Bullet(turtle.Turtle):

    def __init__(self):
        super().__init__()

    def fire(self, start):

    def move(self):
```

Læg mærke til `__init__` funktionen. Det er til hver gang vi laver en ny `Bullet`.

--- 

# A note to `self`

En funktion inde i en klasse skal altid have `self` som første parameter

<div class="container">
<div class="col">

### Inde i en klasse

```python
class Bullet(turtle.Turtle):

    def move(self):
        self.forward(BULLET_SPEED)
```

</div>
<div class="col">

### Udenfor en klasse

```python
bullet = Bullet()
bullet.forward(BULLET_SPEED)
# eller blot
bullet.move()
```

</div>
</div>

Inde i klassen ved man ikke på forhånd hvad variablen hedder udenfor.

--- 

# Hver ny kugle (`__init__`)

For hver ny kugle skal vi 

* Definere dens `shape` og `shapesize`
* Sætte dens farve
* Løfte penen
* Skjule den, så den ikke er synlig før den bliver affyret
* lave en ny variabel til at holde styr på om den er aktiv eller ej

--- 

# Når kuglen affyres (`fire`)

```python
    def fire(self, start):
```

Når kuglen affyres, skal vi

* Sætte den til aktiv (`self.active = False`)
* Flytte den til start positionen
* Sætte retningen den skal flyve i
* Vise den
* Læg mærke til `start` parameteren. Hvad tror I det er ?

--- 

# Når kuglen flytter sig (`move`)

Hver gang kuglen flytter sig. I hvert game loop skal vi:

* Flytte den lidt - men hvor langt ?
    * Hurtigere eller langsommere end rumskibet ?
    * Lad os sige dobbelt så hurtigt: `BULLET_SPEED = PLAYER_SPEED * 2`
* Hvis den er kommet ud over kanten
    * Skjule den
    * Sætte den til inaktiv (`self.active = False`)
* Vi kan lave den lidt smartere senere

--- 

# Så er vi klar til at bruge vores `Bullet`

Når din `Bullet` kan de 3 ting, så er du klar til at bruge den.

* Definere en `BULLET_SPEED` konstant til dens hastighed
* Vi skal have en ny `Bullet` i `# GAME SETUP` sektionen
* Og vi skal have en ny "Behaviour" / en ny funktion
    * Lad os kalde den `move_bullets()`
    * Hvis "space" er trykket ned, skal kuglen affyres
    * Hvis kuglen er aktiv, skal den flyttes frem
* Og så skal den nye funktion kaldes fra vores game loop

---

# NU !!! Gå ind på:

## stefanug.trinket.io

- og klik "Build an Asteroids Game in Python"
- find Lesson 3 og "**Fire one bullet**"

Når I ser dette, så er der opgaver I skal løse, f.eks:

- ✅ Sæt koden ind i `CONSTANTS` sektionen

