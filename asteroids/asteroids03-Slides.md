---
theme: gaia
marp: true
---

# Asteroids Game

## Flytte rumskibet (bedre)

---

# I dag skal vi lære om

* Events - mere om events
* Game loop

---

# Anderledes i dag

1. Først skal I lytte
2. Så får I link til instruktioner
3. Og så skal I kode

---

# Hvordan opfører rumskibet sig ?

Fik I spillet til at virke med `onkey` events ?

Hvordan virker det?

* Rigtig godt?
* Eller lidt underligt ?
* Kan man dreje og rykke fremad på samme tid?

---

# Lad os se hvorfor

* `turtle.onkey` lytter på en tast bliver trykket.
* Den afhænger af computerens gentagelse
* ligesom når man holder en knap nede, og den skriver det samme bogstav mange gange

---

# Kan vi gøre det anderledes?

* Hvad kan vi ellers lytte på ?
* Hvad sker der faktisk når jeg trykker på en knap ?
* Og hvad sker der når jeg slipper ?

---

# `press` og `release` til undsætning

* Man kan lytte på "tast ned" og "tast slip" events
* `onkeypress` og `onkeyrelease` hedder funktionerne
* ... men hvad kan vi bruge det til i hver sin funktion ?

---

# Tilstand (state)

* Vi skal holde styr på spillets tilstand
* Tilstanden kan ændre sig ved at trykke på knapper
* *Eller senere ved at ramme ind i asteroider*

Vi kan bruge et dictionary til at holde styr på state.

```python
keys_pressed = {
    "Left": False,
    "Right": False,
    "Up": False,
    "space": False
}
```

---

# Ændring af state med events

```python
def press_left():
    keys_pressed["Left"] = True

def release_left():
    keys_pressed["Left"] = False

screen.onkeypress(press_left, "Left")
screen.onkeyrelease(release_left, "Left")
```

---

# Adfærd / Behaviour

Hvad tror I dette gør?

```python
def move_spaceship():
    if keys_pressed["Up"]:
        player.forward(???)
```

Hvad skal vi skrive i stedet for `???` ?

---

# Hvad er et Game loop ?

* Et game loop er et loop som kører igen og igen
* Hver gang skal vi grundlæggende:
* 1 - Opdatere spillet baseret på input - opdatere state
* 2 - Tegne spillet igen
* 3 - Holde en mikroskopisk pause

---

# Det er lidt ligesom sådan en

![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimg.buzzfeed.com%2Fbuzzfeed-static%2Fstatic%2F2018-12%2F19%2F13%2Fasset%2Fbuzzfeed-prod-web-01%2Fanigif_sub-buzz-28885-1545245156-2.gif&f=1&nofb=1&ipt=bc0bc13d01d651689bf356a64bf320daa2be394a9dc0e2b4ec72420cf5e85d2b&ipo=images)

Hver side er en gennemgang i vores loop

---

# Et simpelt game loop

```python
def update():
    move_spaceship()
    screen.update()
    screen.ontimer(update, GAME_TICK)
```

Nogen der kan gætte hvad `ontimer` funktionen gør ?
`GAME_TICK` er en ny konstant med et antal millisekunder mellem hvert `update` kald.

---

# Næsten klar til at kode

## Reminder om variabler og værdier

```python
Stefan = "frivillig"
name = Stefan
print(name)
```

Hvad tror I bliver skrevet ud ?

A. Stefan
B. frivillig

---

## Husk : Copy+Paste

Hvis I ser noget kode som I gerne vil bruge:

1. Marker det med musen eller brug `SHIFT + piletaster` til at markere det med
2. Tryk `CTRL + C` eller `CMD + C` for at kopiere
3. Gå derhen I koden hvor I vil have det ind.
4. Tryk `CTRL + V` eller `CMD + V` for at sætte ind

---

# NU !!! Gå ind på:

## stefanug.trinket.io

- og klik "Build an Asteroids Game in Python"
- find Lesson 2 og "**Move the spaceship better**"

Når I ser dette, så er der opgaver I skal løse, f.eks:

- ✅ Lav et dictionary i jeres kode

