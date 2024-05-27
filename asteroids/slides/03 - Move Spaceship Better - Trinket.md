# Move spaceship better

---

# I dag skal vi lære om

* Events - mere om events
* Game loop

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

# Tilstand (State) - Hvilke knapper

Til at holde styr på tilstanden (state) af hvilke knapper man holder nede, skal vi bruge et så kaldt "Dictionary".

I kan tilføje dette under `# EVENTS` sektionen

```python
keys_pressed = {
    "Left": False,
    "Right": False,
    "Up": False,
    "???": False
}
```

Kan I selv sætte en værdi ind for "space" ?

- ✅ Sæt koden ind i `# EVENTS` sektionen
- ✅ Indsæt værdien "space" i stedet for "???"

--- 

# Funktioner til at håndtere events

For hver af de 4 knapper skal vi have 2 funktioner.
Hver funktion ændrer tilstanden i vores Dictionary, f.eks.

```python
def press_left():
    keys_pressed["Left"] = True

def release_left():
    keys_pressed["Left"] = False
```

- ✅ Find de gamle `press_left`, `press_right` og `press_forward` funktioner i din kode og **slet dem**
- ✅ Sæt koden ind i `# EVENTS` sektionen efter dit dictionary
- ✅ Lav nu de resterende 6 `press_` og `release_` funktioner til `Up`, `Down` og `space`


- ℹ️ Hvis du har problemer, kan du finde hjælp i bunden ⬇

--- 

# Lytte på events

Vi skal **fjerne** vores `onkey` events. Dem skal vi ikke bruge!

Dvs. denne kode skal slettes fra jeres fil:

```python
screen.onkey(press_left, "Left")
screen.onkey(press_right, "Right")
screen.onkey(press_forward, "Up")
```

- ✅ Find og fjern denne kode fra din fil.

I stedet skal vi for hver af de 4 knapper lytte på 2 events (tast ned og tast op), f.eks.:

```python
screen.onkeypress(press_left, "Left")
screen.onkeyrelease(release_left, "Left")
```

- ✅ Indsæt koden efter `screen.listen()`
- ✅ Lav selv de 6 andre linier med `onkeypress` og `onkeyrelease` for `Up`, `Down` og `space` events.

- ℹ️ Hvis du har problemer, kan du finde hjælp i bunden ⬇

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

Et game loop er et loop som kører igen og igen

Hver gang skal vi grundlæggende:

1. Opdatere spillet baseret på input - opdatere state
2. Tegne spillet igen
3. Holde en mikroskopisk pause

---

# Det er lidt ligesom sådan en

![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimg.buzzfeed.com%2Fbuzzfeed-static%2Fstatic%2F2018-12%2F19%2F13%2Fasset%2Fbuzzfeed-prod-web-01%2Fanigif_sub-buzz-28885-1545245156-2.gif&f=1&nofb=1&ipt=bc0bc13d01d651689bf356a64bf320daa2be394a9dc0e2b4ec72420cf5e85d2b&ipo=images)

Hver side er en gennemgang i vores loop

--- 

# Ny sektion: Behaviors - Adfærd

Adfærden er det som der sker i vores event loop.

Lad os lave en ny section til det, efter vores `# EVENTS` section og alle vores events, og før vi `# START THE GAME` sektionen:

```python
#
# BEHAVIOURS
#
```

- ✅ Sæt kommentaren ind i din fil efter alle vores events, lige før `# START THE GAME` sektionen.
 
--- 

# Move spaceship adfærd

```python
def move_spaceship():
    if keys_pressed["Left"]:
        player.left(ROTATE_SPEED)
    if keys_pressed["Right"]:
        player.right(???)
    if keys_pressed["Up"]:
        player.forward(PLAYER_SPEED)
```

- ✅ Indsæt koden i den nye `# BEHAVIOURS` sektion
- ✅ Erstat `???` med den rigtige værdi

--- 

# Game Loop

## Game Tick

Husk vi skal holde en mikroskopisk pause mellem hvert game loop. Det kalder vi et "tick"

Ny konstant, med det antal millisekunder mikro-pausen skal være - alstå tiden mellem hvert `update` kald.

```python
GAME_TICK = 20 # milliseconds, lower means faster game
```

- ✅ Indsæt koden i den nye `# CONSTANTS` sektion

## Ny Game Loop Sektion

Vi skal lave en ny sektion til vores Game Loop

```python
#
#  GAME LOOP
#
```

- ✅ Indsæt kommentaren efter vores behaviour lige før `# START THE GAME` sektionen.

## Lav vores `update` funktion

`update` bliver den funktion som kaldes i hvert game loop - for hvert "tick". Den skal se sådan her ud:

```python
def update():
    move_spaceship()

    screen.update()
    screen.ontimer(update, GAME_TICK) # this calls the game loop again for the next tick
```

- ✅ Indsæt funktionen i den nye `# GAME LOOP` sektion


## Erstat den forrige `update`

Nu skal vi fjerne koden som kalder `screen.update()` fra `# START THE GAME` sektionen. Det skal erstattes med et kald til vores egen nye `update` funktion


Så i stedet for:

```python
screen.update()
```

skal der blot stå 

```python
update()
```

- ✅ Fra `# START THE GAME` sektionen, find `screen.update()` og slet `screen.`, så der bare står `update()`
 
# Prøv spillet

- ✅ Kør spillet og se om rumskibet flytter sig bedre end før


---
---

# Hjælp

## Alle press og release funktionerne

Koden her skal være i `# EVENTS` sektionen under `keys_pressed` dictionary og alle dets værdier. 

```python
def press_left():
    keys_pressed["Left"] = True

def release_left():
    keys_pressed["Left"] = False

def press_right():
    keys_pressed["Right"] = True

def release_right():
    keys_pressed["Right"] = False

def press_forward():
    keys_pressed["Up"] = True

def release_forward():
    keys_pressed["Up"] = False

def press_fire():
    keys_pressed["space"] = True

def release_fire():
    keys_pressed["space"] = False
```

## Registrering af alle onkeypress og onkeyrelease funktionerne

Denne kode skal være i `# EVENTS` sektionen lige efter `screen.listen()`

```python
screen.onkeypress(press_left, "Left")
screen.onkeypress(press_right, "Right")
screen.onkeypress(press_forward, "Up")
screen.onkeypress(press_fire, "space")
screen.onkeyrelease(release_left, "Left")
screen.onkeyrelease(release_right, "Right")
screen.onkeyrelease(release_forward, "Up")
screen.onkeyrelease(release_fire, "space")
```
