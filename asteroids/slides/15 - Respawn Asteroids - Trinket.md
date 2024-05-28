# Nye asteroider over tid: Respawn

Når spillet går godt, så er det hurtigt overstået.

Lad os få flere asteroider, efter de er skudt.

---

# Hvor lang tid skal de være væk?

* Lad os definere det som et antal "game ticks"
* Og gemme det i en konstant
* Kald den `ASTEROID_RESPAWN_AFTER`

```python
ASTEROID_RESPAWN_AFTER = 150
```

- ✅ Sæt koden ind i `CONSTANTS` sektionen

--- 

# Tæller på asteroiden

Når en asteroide er ramt skal den selv tælle ned til den igen kan spawne.

* Til det skal vi bruge en tæller på `Asteroid` klassen
* Kald den `respawn_in`
* Sæt den til `0` i første omgang

```python
        self.respawn_in = 0
```

- ✅ Sæt koden ind i `Asteroid.__init__` funktionen, f.eks. efter `self.radius` linien

---

# Når asteroiden bliver ramt

En asteroide kan blive ramt.

* Så lad os på klassen definere hvad der sker når den rammes
* Ny funktion på `Asteroid`, kaldet `hit`
* Så skal den skjule sig
* Og sætte tælleren, så der kan tælles ned

```python
    def hit(self):
        self.hideturtle()
        self.respawn_in = ASTEROID_RESPAWN_AFTER
```

- ✅ Sæt koden ind i `Asteroid` klassen, efter `__init__` funktionen og al dens indhold


---

# Kald den nye `Asteroid.hit` funktion

Der hvor vi før blot skjulte asteroiden når den blev ramt, skal vi nu kalde `hit` funktionen i stedet for.

* Før:
  ```python
              if hit_asteroid:
                  hit_asteroid.hideturtle()
  ```
* Efter:
  ```python
              if hit_asteroid:
                  hit_asteroid.???()
  ```

- ✅ I `move_bullets` funktionen, ændr linien under `if hit_asteroid:`, så den kalder `hit` funktionen på den ramte asteroide

---

# Tæl ned, hvis asteroiden ikke er synlig

* I `move_asteroids` funktionen kan vi tælle ned på hver asteroide, hvis den ikke er synlig.
* Vi har allerede en `if asteroid.isvisible():` block
* Så vi kan sætte en `else:` block bagefter
* Her tæller vi `respawn_in` ned
* Og nulstiller asteroiden hvis tælleren er 0

```python
        else:
            asteroid.respawn_in -= 1
            if asteroid.respawn_in == 0:
                asteroid.reset()
```

- ✅ Indsæt koden i `move_asteroids` funktionen, så det bliver `else` delen til den eksisternde `if asteroid.isvisible():` block.


ℹ️ Husk `else` skal være på samme niveau / have samme indrykning, som dens tilhørende `if`.

Eksempel på en `if`-block uden else:

```python
if something:
    do_stuff()
```

Eksempel på en `if`-block med en tilhørende `else`-del

```python
if something:
    do_stuff()
else:
    do_something_else()
```

---

# Men hvad gør `reset()` ?

Vi har ikke lavet nogen reset funktion på Asteroid. Det skal vi nu!

* Men skal asteroiden have samme retning og hastighed som da den forsvandt?
* Det synes jeg ikke!
* Så lad reset funktion sætte tilfældig retning og hastighed
* Altså flytte koden fra `__init__` ned i den
* Og så vise asteroiden.

# Reset funktionen

Sådan kan `reset` funktionen se ud:

```python
  def reset(self):
      self.setheading(random.randint(0, 360))
      self.speed = random.randint(ASTEROID_SPEED_MIN, ASTEROID_SPEED_MAX)
      self.showturtle()
```

- ✅ Find de to linier i `Asteroid.__init__` funktionen, som sætter heading og speed, og **slet dem**.
- ✅ Indsæt koden i `Asteroid` klassen, f.eks. efter `hit` funktionen du satte ind før.

---

# Kald reset ved ny asteroide

Vi skal stadig have en ny asteroide til at sætte en retning og hastighed, men hvordan nu hvor vi har flyttet det fra `__init__`

* Det kan vi gøre ved at kalde `reset` fra `__init__` funkitonen:

```python
      self.reset()
```

- ✅ Indsæt koden i `Asteroid.__init__` funktionen, der hvor du før slettede to linier

* Vi skal også huske den gode skik, og sætte `speed` fra `__init__` funktionen

```python
      self.speed = 0
```

- ✅ Indsæt koden i `Asteroid.__init__` funktionen, f.eks. lige før kaldet til `reset`


---

# Prøv spillet

- ✅ Start spillet og se om asteroiderne kommer igen efter de er blevet skudt
