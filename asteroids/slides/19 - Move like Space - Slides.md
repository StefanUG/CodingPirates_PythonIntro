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

## Bevægelse som i rummet

Lige nu bevæger vores rumskib sig lidt for nemt - det stopper med det samme når man slipper pil-op tasten.

I rummet er der ingen luft, så der er ingen friktion! Lad os få rumskibet til at bevæge sig mere realistisk.

---

# Hvad skal vi ændre?

I stedet for at flytte rumskibet direkte, skal vi:

* Have en fart (hastighed) i X-retningen
* Have en fart (hastighed) i Y-retningen  
* Pil-op skal give rumskibet mere fart
* Rumskibet skal bevæge sig i den retning det har fart

---

# Et nyt bibliotek: `math`

For at regne vinkler og retninger ud, skal vi bruge matematik-funktioner.

* Importer `math` biblioteket øverst i filen:
* ```python
  import math
  ```
* Det giver os funktioner som `math.cos()` og `math.sin()`
* De hjælper os med at beregne bevægelse i forskellige retninger

---

# Nye konstanter

Vi skal ændre hvordan spillerens hastighed fungerer:

* I stedet for `PLAYER_SPEED = 10` skal vi have:
* ```python
  PLAYER_MAX_SPEED = 10  # Pixels to move player each tick
  PLAYER_THRUST = 0.1  # increase in speed per tick
  ```
* `PLAYER_THRUST` er hvor meget fart vi får når vi trykker pil-op
* `PLAYER_MAX_SPEED` er den maksimale fart vi kan opnå

---

# Opdater `BULLET_SPEED`

Da vi har omdøbt `PLAYER_SPEED` til `PLAYER_MAX_SPEED`, skal vi også opdatere den linje der bruger den:

* Find linjen med `BULLET_SPEED` og ret den til:
* ```python
  BULLET_SPEED = PLAYER_MAX_SPEED * 2  # Double of player speed
  ```

---

# Hastighed i X og Y retning

Spilleren skal holde styr på sin hastighed i både X og Y retning.

* I `Player.__init__` skal vi tilføje to nye variabler:
* ```python
          self.speedx = 0
          self.speedy = 0
  ```
* `speedx` = hastighed til højre (eller venstre hvis negativ)
* `speedy` = hastighed opad (eller nedad hvis negativ)

---

# `Player.thrust()` - Giv rumskibet mere fart!

Nu skal vi lave en ny funktion der giver rumskibet fart:

* Den skal finde ud af hvilken retning rumskibet peger
* Tilføje lidt fart i den retning
* Sørge for at den maksimale hastighed ikke overskrides

---

# `Player.thrust()` - koden

```python
    def thrust(self):
        track = math.radians(self.heading())
        self.speedx += PLAYER_THRUST * math.cos(track)
        self.speedy += PLAYER_THRUST * math.sin(track)
        speed = (self.speedx ** 2 + self.speedy ** 2) ** 0.5
        if speed > PLAYER_MAX_SPEED:
            self.speedx = (self.speedx * PLAYER_MAX_SPEED) / speed
            self.speedy = (self.speedy * PLAYER_MAX_SPEED) / speed
```

Sæt den ind i `Player` klassen, f.eks. efter `is_invincible()` funktionen.

---

# Hvad sker der i `thrust()`?

Lad os kigge på hvad funktionen gør:

1. `track = math.radians(self.heading())` - finder rumskibets retning i radianer
2. `self.speedx += ...` - tilføjer fart i X-retningen baseret på vinklen
3. `self.speedy += ...` - tilføjer fart i Y-retningen baseret på vinklen
4. `speed = ...` - beregner den totale hastighed
5. `if speed > PLAYER_MAX_SPEED:` - hvis vi er for hurtige, sæt hastigheden ned

---

# `Player.move()` - Flyt rumskibet!

Nu skal rumskibet flytte sig baseret på sin hastighed:

```python
    def move(self):
        x, y = self.pos()
        x += self.speedx
        y += self.speedy
        self.goto(x, y)
```

* Hent den nuværende position
* Tilføj hastigheden til positionen
* Flyt rumskibet til den nye position

Sæt den ind i `Player` klassen, f.eks. efter `thrust()` funktionen.

---

# Opdater `move_spaceship()` funktionen

Nu skal vi ændre måden rumskibet bevæger sig på:

* Find `move_spaceship()` funktionen under `# BEHAVIOURS`
* Vi skal ændre hvad der sker når man trykker pil-op
* I stedet for `player.forward(PLAYER_SPEED)` skal vi kalde `player.thrust()`
* Og efter alle tastetryk skal vi kalde `player.move()`

---

# Den nye `move_spaceship()` funktion

```python
def move_spaceship():
    if keys_pressed["Left"]:
        player.left(ROTATE_SPEED)
    if keys_pressed["Right"]:
        player.right(ROTATE_SPEED)
    if keys_pressed["Up"]:
        player.thrust()

    player.move()
    move_if_out_of_bounds(player)
    if check_collision(player):
        player.hit()
```

Læg mærke til: `player.thrust()` i stedet for `player.forward()`, og `player.move()` efter tastetjek!

---

# Prøv det!

Nu skulle rumskibet bevæge sig som i rummet!

* Tryk pil-op for at give gas
* Rumskibet fortsætter med at bevæge sig selvom du slipper tasten
* Du kan dreje mens du bevæger dig
* Det er meget sværere at kontrollere - præcis som i rigtig rumfart! 🚀

---

# Hvad lærte vi?

* Hvordan man simulerer bevægelse i rum uden friktion
* Hvordan man bruger `math.cos()` og `math.sin()` til at beregne bevægelse i forskellige retninger
* Hvordan man holder styr på hastighed i X og Y retning
* Hvordan man begrænser maksimal hastighed
* At rumfart er svært! 🌌

---

# NU !!! Gå ind på:

## stefanug.trinket.io

- og klik "Build an Asteroids Game in Python"
- find Lesson 6 og "**19. Move like Space**"

Når I ser dette, så er der opgaver I skal løse, f.eks:

- ✅ Importer `math` biblioteket
- ✅ Tilføj de nye konstanter
- ✅ Tilføj `speedx` og `speedy` til Player
