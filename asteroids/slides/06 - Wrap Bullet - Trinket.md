# Wrap the Bullet

Nu skal vi have kuglen til at flytte sig til den anden side af skærmen når den ryger ud. Den skal "wrappes"

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

- ✅ Indsæt koden i `CONSTANTS` sektionen

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

- ✅ Indsæt `self.ttl` linien i både `__init__` og `fire` funktionen

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

- ✅ Indsæt logikken som det sidste i `move` funktionen

---

# Og så skal vi "wrappe" kuglen

```python
    def move(self):
        self.forward(BULLET_SPEED)
        move_if_out_of_bounds(self)
        # .. SNIP ..
```

* Hvad sker der når vi sender `self` med som parameter ?

- ✅ Indsæt et kald til `move_if_out_of_bounds` i `move` funktionen, efter vi har flyttet kuglen fremad.

---

# Prøv spillet

- ✅ Start spillet og se hvad der sker når du skyder en kugle
