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

## "Wrap bullet"


---

# Kan I huske?

* Vores `move_if_out_of_bounds` funktion?
* ... og at den tager en `Turtle` som parameter ?
* Hvordan tror I vi kan bruge det ?
* Kan I huske en `Bullet` er faktisk en `Turtle`?
* Hvad tror I der sker når vi "wrapper" vores kugle ?
* Stopper den nogensinde ?

---

# Bullet lifetime

* Vi skal definere en levetid for en kugle, så den forsvinder efter noget tid
* Vi sætter den til 75 game ticks
* og så skal vi tælle ned i hvert game loop

```python
BULLET_LIFETIME = 75  # game ticks
```

---

# Sæt levetiden når kuglen affyres

Vi bruger en forkortelse for "Time to Live" (`ttl`)

```python
    def __init__(self):
        # ... SNIP ...
        self.ttl = BULLET_LIFETIME

    def fire(self, start):
        self.ttl = BULLET_LIFETIME
```

* Det er god skik at sætte en variabel på en klasse i `__init__`
* Men ikke nødvendigt.
* det vigtigste er vi gør det i `fire`

---

# Nu skal vi tælle ned

* Hver gang en kugle flytter sig, trækker vi en fra `ttl`
* Og hvis `ttl` er mindre end 0, så er den ikke længere aktiv

```python
    def move(self):
        # .. SNIP ..
        self.ttl -= 1
        if self.ttl < 0:
            self.hideturtle()
            self.active = False
```

`ttl -= 1` er det samme som `ttl = ttl - 1`

---

# Og så skal vi "wrappe" kuglen

```python
    def move(self):
        self.forward(BULLET_SPEED)
        move_if_out_of_bounds(self)
        # .. SNIP ..
```

* Hvad sker der når vi sender `self` med som parameter ?

---

# NU !!! Gå ind på:

## stefanug.trinket.io

- og klik "Build an Asteroids Game in Python"
- find Lesson 3 og "**Wrap the bullet**"

Når I ser dette, så er der opgaver I skal løse, f.eks:

- ✅ Sæt koden ind i `CONSTANTS` sektionen

