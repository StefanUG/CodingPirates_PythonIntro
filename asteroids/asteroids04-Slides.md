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

## Wrap Player

## Har I prøvet at flyve lidt ?

## Er der noget galt ?

---

# Kan I huske 
# koordinat systemet ?

![bg contain](slide-resources/coordinate-system.svg)

---

# Kan I huske skærmens størrelse ?

```python
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
```

## Hvordan finder vi halvdelen ?

Python er rigtig god til matematik:

`+` (plus) og `-` (minus) og `*` (gange) og `/` (divider) 

```
SCREEN_WIDTH / ???
```

---

# Lad os gemme det i en konstant

```python
HALF_WIDTH = int(SCREEN_WIDTH / 2)
HALF_HEIGHT = ???
```

`int` funktionen laver et decimaltal `600.0` til et heltal `600`

Det er desværre nødvendigt for at bruge det i Turtle senere.

---

# Lad os lave en funktion til at flytte en turtle

Vi skal nemlig ikke kun flytte rumskibet.

Vi skal også flytte asteroider.

Funktioner gør så vi kan genbruge algoritmen.

---

# Kan I huske funktioner?

Det er lidt ligesom

* Omkvædet i en sang
* Opskrifter til madlavning

Men vidste I en funktion kan tage parametre?

---

# Eksempler på parametre i funktioner

I har allerede brugt funktioner som tager parametre

```python
player.shape("triangle")
turtle.forward(100)
turtle.right(90)
```

Hvordan laver vi *selv* sådan en funktion ?

---

# Eksempler på definitioner

```python
# En funktion uden parametre
def chorus():
   print("doo doo, doo doo doo doo")

# En funktion med en parameter
def verse(person):
   for i in range(4):
       print(person + " Shark")
       chorus()

for p in ("Baby", "Mommy"):
    verse(p) # For hver person-type, skriv et vers
```

---

# Vores funktion til at flytt en turtle

```python
def move_if_out_of_bounds(t: turtle.Turtle):
```

`t` er navnet på en variabel
`turtle.Turtle` efter `:` er et type-hint, som man kan bruge til at fortælle editoren hvad vi kan forvente. 

Så kan den bedre hjælpe os med forslag

---

# Hvad skal vi så have indeni ?

Vi skal bruge x og y koordinaterne fra vores turtle, så vi kan se om den er kommet udenfor vores koordinatsystem.

```python
    x = t.xcor()
    y = t.ycor()
```

---

# Tjekke om turtle er ude af syne

I pseudo kode skal vi bruge noget ala dette:

```python
    if x is too far right:
        t should goto left side of screen
    elif x is too far left:
        t should goto right side of screen
```

Og det samme med op og ned.

---

# Hvordan ved vi om x er for langt til højre eller til venstre ?

* Vi har `x` og vi har `HALF_WIDTH`
* Hvordan sammenligner vi dem ?
* `x` er større end `HALF_WIDTH`
* `x` er mindre end `-HALF_WIDTH`

Python er også god til logik:

`>` (større end) og `<` (mindre end)  

---

# Til sidst skal funktionen kaldes

Det vil vi gøre lige efter vi har flyttet spilleren i hvert game loop. F.eks. som det sidste i `move_spaceship` funktionen.


```python
        move_if_out_of_bounds(player)
```

Her sender vi `player` med som parameter. 
Det er den vi gerne vil flytte hvis den er ude af syne.

---

# NU !!! Gå ind på:

## stefanug.trinket.io

- og klik "Build an Asteroids Game in Python"
- find Lesson 2 og "**Wrap Player**"

Når I ser dette, så er der opgaver I skal løse, f.eks:

- ✅ Sæt koden ind i `CONSTANTS` sektionen

