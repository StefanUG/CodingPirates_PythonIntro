# State - Hvilke knapper

Til at holde styr på tilstanden (state) af hvilke knapper man holder nede, skal 
vi bruge et så kaldt "Dictionary".

I kan tilføje dette under `# EVENTS` sektionen

```python
keys_pressed = {
    "Left": False,
    "Right": False
}
```

Kan I selv sætte værdierne "Up" og "space" ind ?

- ✅ Lav et dictionary i jeres kode
- ✅ Indsæt værdierne "Left", "Right", "Up" og "space" 

- Husk komma `,` imellem linierne!
- Vigtigt at skrive navnene med de rigtige store og små bogstaver

--- 

# Funktioner til at håndtere events

For hver af de 4 knapper skal vi have 2 funktioner, f.eks.

```python
def press_left():
    keys_pressed["Left"] = True

def release_left():
    keys_pressed["Left"] = False
```

- ✅ Lav alle 8 funktioner til alle 4 knapper

--- 

# Lytte på events

Vi skal **fjerne** vores `onkey` events. Dem skal vi ikke bruge!

I stedet skal vi for hver af de 4 knapper lytte på 2 events, f.eks.:

```python
screen.listen()
screen.onkeypress(press_left, "Left")
screen.onkeyrelease(release_left, "Left")
```

- ✅ Få dit spil til at lytte på alle 8 events


--- 

# Ny sektion: Behaviors - Adfærd

Adfærden er det som der sker i vores event loop.

Lad os lave en ny section til det, efter vores `# EVENTS` section og alle vores events, og før vi `# START THE GAME` sektionen:

```python
#
# BEHAVIOURS
#
```

- ✅ Lav kommentar til den nye sektion, som ovenover
 
--- 

# Move spaceship adfærd

```python
def move_spaceship():
    if keys_pressed["Left"]:
        player.left(???)

    if keys_pressed[???]:
        player.forward(???)
```

- ✅ Find selv ud af hvad der skal stå i stedet for `???`
- ✅ Gør selv koden færdig så vi kan dreje til højre, til venstre og rykke fremad

--- 

# Game Loop

Ny konstant, med det antal millisekunder mellem hvert `update` kald.

```python
GAME_TICK = 20 # milliseconds, lower means faster game
```

Og så skriv funktionen til vores game loop:

```python
#
#  GAME LOOP
#

def update():
    move_spaceship()

    screen.update()
    screen.ontimer(update, GAME_TICK) # this calls the game loop again for the next tick
```

- ✅ Indsæt konstanten det rigtige sted i koden
- ✅ Indsæt GAME LOOP sektionen mellem `# BEHAVIORS` og `# START THE GAME` sektionerne
 
# Start the game

Til sidst skal vi lige lave lidt om for at starte spillet.

I stedet for at kalde `screen.update()` en enkelt gang, skal vi kalde vores egen nye `update()` funktion.

- ✅ Erstat `screen.update()` med et kald til den nye game loop funktion.
- ✅ Kør spillet og se om det virker
