# Forsvinder livene for hurtigt?

Når hvert game tick tæller dine liv ned så går det ret hurtigt med at miste de liv.

Lad os indsætte en lille "henstandstid" aka "Grace Period"

---

# Hvor mange sekunder før vi kan blive ramt igen?

* Lad os sige 3 sekunder
* Burde være tid nok til at komme væk fra asteroiden

```python
PLAYER_GRACE_PERIOD = 3 # seconds
```

- ✅ Sæt koden ind i `#  CONSTANTS` sektionen

---

# At holde styr på tiden

Nu skal vi til at holde styr på tiden, så vi kan tælle sekunder.

* Vi skal bruge et nyt bibliotek:
* ```python
  import time
  ```
* Med `time.time()` kan man få antal sekunder "tiden startede"
* Torsdag, 1. januar 1970, kl 00:00:00
* Også kalder `epoch`


- ✅ Indsæt `import time` øverst i filen, f.eks. på en linie lige efter `import random`


---

# Hvornår blev spilleren sidst ramt?

Vi skal have en ny variabel til at holde styr på hvornår spilleren sidst blev ramt

```python
self.last_hit = 0.0
```

- ✅ Sæt koden ind i `Player.hit` funktionen, f.eks. efter `self.health` bliver sat.


Hver gang spilleren rammes, sætter vi den til nuværende tid

```python
self.last_hit = time.time()
```

Det kan vi så bruge senere...

---

# Udødelig!

Vi skal også gøre spilleren uovervindelig

* Hvis tiden siden man sidst blev ramt er mindre en tre sekunder siden
* Hvordan kan vi udtrykke det i matematik ?
* Vi har `last_hit`, `3` og `time`, alt samme sekunder

---

# Hvis `epoch` var da vi startede spillet 

Lad os sige følgende:

- Vi bliver ramt efter 20 sekunder: `last_hit` er `20`
- `PLAYER_GRACE_PERIOD` er 3 sekunder
- Nu bliver vi ramt efter 2 sekunder, dvs. `time.time()` er `22`

Hvordan kan vi bruge de tre variabler til regne ud vi er udødelig lige nu?

* Hvis `last_hit + PLAYER_GRACE_PERIOD > time.time()`, så er man udødelig
* Hvis `20 + 3` er større end `22` ... er det det ?

---

# Ny funktion til udødeligheden

Det er meget at skrive hver gang, og ikke særlig beskrivende

* Lad os lave en funktion med et bedre navn til det
* Kald den `is_invincible`
* Lad den returnere om spilleren er udødlig lige nu eller ej

```python
    def is_invincible(self):
        return self.last_hit + PLAYER_GRACE_PERIOD > time.time()
```

- ✅ Sæt koden ind i `Player` klassen, f.eks. før `hit` funktionen

---

# Opdateret `hit` funktion i Player

Nu skal vi til at tjekke reglerne i `Player.hit` funktionen

* Hvis spilleren _ikke_ er udødelig lige nu,
  * trække liv fra: `health -= 1`
  * sætte: `last_hit` til tiden lige nu
  * skrive det nye antal liv på skærmen: `draw_health()`
* Til sidst, hvis ens liv er 0,
  * sæt `alive` til `False`

Samlet set, så skal `Player.hit` funktionen nu se sådan her ud:

```python
    def hit(self):
        if not self.is_invincible():
            self.health -= 1
            self.last_hit = time.time()
            draw_health()

        if self.health == 0:
            self.alive = False
```

- ✅ Erstat den nuværende `hit` funktion i `Player` klassen med koden herover

---

# Hvordan ved vi om vi er udødelige?

Til at starte med kan vi gøre så spilleren bliver rød så længe.

Ny funktion i `behaviours`, som kan kaldes i hvert game loop:

```python
def animate_spaceship():
    if player.is_invincible():
        player.color("red", BG_COLOR)
    else:
        player.color("light grey", BG_COLOR)
```

- ✅ Sæt koden ind i `# BEHAVIOURS` sektionen,  f.eks. før `move_spaceship` funktionen

---

# Kald `animate_spaceship` fra game loop

I `update` funktionen skal vi kalde den nye funktion, f.eks. efter `move_spaceship()`

```python
    animate_spaceship()
```

- ✅ Sæt koden ind i `update` funktionen fra `# GAME LOOP` sektionen, f.eks. lige efter kaldet til `move_spaceship()`


---

# Prøv spillet

- ✅ Start spillet og se om ikke rumskibet bliver rødt når det bliver ramt af asteroiderne