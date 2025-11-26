# Bevægelse som i rummet

## Rumskibet stopper for hurtigt

Lige nu bevæger vores rumskib sig lidt for nemt - det stopper med det samme når man slipper pil-op tasten.

I rummet er der ingen luft, så der er ingen friktion! Lad os få rumskibet til at bevæge sig mere realistisk.

---

# Et nyt bibliotek: `math`

For at regne vinkler og retninger ud, skal vi bruge matematik-funktioner.

```python
import math
```

- ✅ Indsæt `import math` øverst i filen, f.eks. på en linje lige efter `import time`

---

# Nye konstanter

Vi skal ændre hvordan spillerens hastighed fungerer.

I stedet for `PLAYER_SPEED = 10` skal vi have:

```python
PLAYER_MAX_SPEED = 10  # Pixels to move player each tick
PLAYER_THRUST = 0.1  # increase in speed per tick
```

- ✅ Find `PLAYER_SPEED` i `# CONSTANTS` sektionen og **erstat** den med de to konstanter herover

`PLAYER_THRUST` er hvor meget fart vi får når vi trykker pil-op, og `PLAYER_MAX_SPEED` er den maksimale fart vi kan opnå.

---

# Opdater `BULLET_SPEED`

Da vi har omdøbt `PLAYER_SPEED` til `PLAYER_MAX_SPEED`, skal vi også opdatere linjen der bruger den.

```python
BULLET_SPEED = PLAYER_MAX_SPEED * 2  # Double of player speed
```

- ✅ Find `BULLET_SPEED` linjen i `# CONSTANTS` sektionen og opdater den så den bruger `PLAYER_MAX_SPEED` i stedet for `PLAYER_SPEED`

---

# Hastighed i X og Y retning

Spilleren skal holde styr på sin hastighed i både X og Y retning.

```python
        self.speedx = 0
        self.speedy = 0
```

- ✅ Sæt koden ind i `Player.__init__` funktionen, f.eks. efter `self.last_hit` bliver sat

`speedx` = hastighed til højre (eller venstre hvis negativ)
`speedy` = hastighed opad (eller nedad hvis negativ)

---

# `Player.thrust()` - Giv rumskibet mere fart!

Nu skal vi lave en ny funktion der giver rumskibet fart i den retning det peger:

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

- ✅ Sæt koden ind i `Player` klassen, f.eks. efter `hit` funktionen

Funktionen finder rumskibets retning, tilføjer fart i den retning, og sørger for at den maksimale hastighed ikke overskrides.

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

- ✅ Sæt koden ind i `Player` klassen, f.eks. efter `thrust` funktionen

Funktionen henter den nuværende position, tilføjer hastigheden, og flytter rumskibet til den nye position.

---

# Opdater `move_spaceship()` funktionen

Nu skal vi ændre måden rumskibet bevæger sig på.

Vi skal ændre hvad der sker når man trykker pil-op, og tilføje et kald til `player.move()`.

Den nye `move_spaceship()` funktion skal se sådan ud:

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

- ✅ Find `move_spaceship` funktionen i `# BEHAVIOURS` sektionen
- ✅ Ændr den så `if keys_pressed["Up"]:` blokken kalder `player.thrust()` i stedet for `player.forward(PLAYER_SPEED)`
- ✅ Sæt `player.move()` ind lige efter alle `if` blokkene, men før `move_if_out_of_bounds(player)`

---

# Prøv spillet

- ✅ Start spillet og prøv at flyve rundt

Nu skulle rumskibet bevæge sig som i rummet!

* Tryk pil-op for at give gas
* Rumskibet fortsætter med at bevæge sig selvom du slipper tasten
* Du kan dreje mens du bevæger dig
* Det er meget sværere at kontrollere - præcis som i rigtig rumfart! 🚀
