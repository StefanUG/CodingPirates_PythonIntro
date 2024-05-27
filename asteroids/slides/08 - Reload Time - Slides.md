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

## Reload time

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
* Skyde en kugle: `shootshoot(self, inactive_bullet)`
* Køle ned efter den har skudt: `cooldown(self)`

---

# En ny af sig selv

Fra `# GAME SETUP` til `# CLASSES`


<div class="container">
<div class="col">

### Før

```python
# GAME SETUP
player = turtle.Turtle()
player.shape("triangle")
player.color("light grey", BG_COLOR)
player.shapesize(0.75, 1.5)
player.penup()
```

</div>
<div class="col">

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

</div>
</div>

--- 

# Hver ny spiller (`__init__`)

Foruden det, skal vi

* Sætte cooldown til 0 `self.fire_cooldown = 0`

--- 

# Når spilleren skyder (`shoot`)

```python
    def shoot(self, inactive_bullet):
```

Vi går ud fra der allerede er fundet en inaktiv kugle (`inactive_bullet`)

Når spilleren skyder, skal vi

* Tjekke om man er klar (`if self.fire_cooldown == 0:`)
    * Skyde kuglen: `inactive_bullet.fire(player)`
    * Sætte cooldown: `self.fire_cooldown = RELOAD_TIME`

--- 

# Cooldown...

I hvert game loop skal spilleren "køle ned" `def cooldown(self)`

* Men kun hvis spillerens cooldown ikke allerede er 0
* `if self.fire_cooldown > 0:`
    * træk en fra cooldown `self.fire_cooldown -= 1`


--- 

# Reload time

Lagde i mærke til `RELOAD_TIME` før ?

* Den skal defineres. Hvor skal den være ?
* I `# CONSTANTS` sektionen
* `RELOAD_TIME = 5  # ticks between reload`


--- 

# Rette game loop til

Nu er vi klar til at rette game loop til.

* I `move_bullets` skal vi køle spilleren ned: `player.cooldown()`
* Og så skal spilleren skyde kuglen: `player.shoot(inactive_bullet)`
* I stedet for `inactive_bullet.fire(player)`

--- 

# NU !!! Gå ind på:

## stefanug.trinket.io

- og klik "Build an Asteroids Game in Python"
- find Lesson 4 og "**8. Reload Time**"

Når I ser dette, så er der opgaver I skal løse, f.eks:

- ✅ Sæt koden ind i `CONSTANTS` sektionen

 