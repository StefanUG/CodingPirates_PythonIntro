# Reload time

Den skyder lidt for hurtigt, lad os indsætte noget reload time på spilleren.

---

# Mere "state", mere at holde styr på

Hvordan holder vi styr på hvornår vi sidst har skudt?

* Kan vi bruge en tæller ?
* Hvor skal den være ?
* Lad os sætte den på en `Player` klasse.

---

# Skal `Player` også være en `Turtle` ?

* **JA DA !**
* `class Player(turtle.Turtle):`
* Og så skal den kunne:
* Lave en ny af sig selv: `__init__(self)`
* Skyde en kugle: `shoot(self, inactive_bullet)`
* Køle ned efter den har skudt: `cooldown(self)`

---

# En ny af sig selv

Fra `# GAME SETUP` til `# CLASSES`


### Før

```python
# GAME SETUP
player = turtle.Turtle()
player.shape("triangle")
player.color("light grey", BG_COLOR)
player.shapesize(0.75, 1.5)
player.penup()
```

- ✅ Find og fjern de linier fra `# GAME SETUP` sektionen (kun dem med `player` og **ikke** dem med `screen`)


### Efter

```python
# CLASSES
class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.color("light grey", BG_COLOR)
        self.shapesize(0.75, 1.5)
        self.penup()

# GAME SETUP
player = Player()
```



- ✅ Indsæt `Player` klassen i `# CLASSES` sektionen, f.eks. før `Bullet` klassen
- ✅ Indsæt `player = Player()` i `# GAME SETUP` sektionen, hvor du før fjernede det andet fra


--- 

# Hver ny spiller (`__init__`)

Foruden det, skal vi

* Sætte cooldown til 0 

```python
self.fire_cooldown = 0
```

- ✅ Indsæt linien som den sidste i `Player.__init__` funktionen


--- 

# Når spilleren skyder (`shoot`)

```python
    def shoot(self, inactive_bullet):
```

Vi går ud fra der allerede er fundet en inaktiv kugle (`inactive_bullet`)

Når spilleren skyder, skal vi

* Tjekke om man er klar (`if self.fire_cooldown == 0:`)
    * Skyde kuglen: `inactive_bullet.fire(self)`
    * Sætte cooldown: `self.fire_cooldown = RELOAD_TIME`


Det samlede kode:

```python
    def shoot(self, inactive_bullet):
        if self.fire_cooldown == 0:
            inactive_bullet.fire(self)
            self.fire_cooldown = RELOAD_TIME
```

- ✅ Indsæt den samlede `shoot` funktion i `Player` klassen efter `__init__` funktionen

--- 

# Cooldown...

I hvert game loop skal spilleren "køle ned" `def cooldown(self)`

* Men kun hvis spillerens cooldown ikke allerede er 0
* `if self.fire_cooldown > 0:`
    * træk en fra cooldown `self.fire_cooldown -= 1`


Det samlede kode:

```python
    def cooldown(self):
        if self.fire_cooldown > 0:
            self.fire_cooldown -= 1
```

- ✅ Indsæt den samlede `cooldown` funktion i `Player` klassen efter `shoot` funktionen


--- 

# Reload time

Lagde i mærke til `RELOAD_TIME` før ?

* Den skal defineres. Hvor skal den være ?
* I `# CONSTANTS` sektionen

```python
RELOAD_TIME = 5  # ticks between reload
```

- ✅ Indsæt koden i `# CONSTANTS` sektionen

--- 

# Færre max bullets

Lad os sætte sværhedsgraden en smule op, og sænke antallet af max antal bullets

```python
MAX_BULLETS = 10
```

- ✅ Ændr `MAX_BULLETS` fra `20` til `10`

--- 

# Rette game loop til

Nu er vi klar til at rette game loop til.

* I `move_bullets` skal vi køle spilleren ned: `player.cooldown()`
* Og så skal spilleren skyde kuglen: `player.shoot(inactive_bullet)`
* I stedet for `inactive_bullet.fire(player)`


```python
    player.cooldown()
```

- ✅ Indsæt koden som første linie i `move_bullets` funktionen
- ✅ I `move_bullets` funktionen, erstat ~~`inactive_bullet.fire(player)`~~ med `player.shoot(inactive_bullet)`


---

# Prøv spillet

- ✅ Start spillet og se hvad der sker når du holder space nede
