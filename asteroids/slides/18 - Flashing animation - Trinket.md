# Blink når man bliver uovervindelig

⚠️ Dette er en avanceret lektion, hvis man skal forstå det.

I det rigtige Asteroids spil bliver spilleren ikke rød... Det var nemlig lavet til en sort-hvid skærm.

Så vi skal have rumskibet til at blinke i stedet for at blive rød

---

# Skiftevis synlig og usynlig

For at blinke skal vi skiftevis gøre spilleren usynlig og synlig igen

* F.eks. hver gang der er gået en tiendedel af et sekund
* Vi kan bruge en `modulus` operator: `%`
* Den giver os det der er til overs efter at have divideret de to tal.
* f.eks. `7 % 3` = `1` fordi man kun kan dele `7` mønter med `3` to gange
* Bagefter har du `1` mønt tilbage
* `10 % 2` giver hvad ? `10` mønter delt med `2`, er der nogen til overs?

---

# Det er smart til at tælle hver anden

* `time.time()` ser ca. sådan ud: `1717964314.8923671`
* Den kan vi gange med 10, for at flytte kommaet til højre
* Så får vi dette tal i stedet for `17179643148.923671` 
* Det repræsenterer nu det antal tiendedel-sekunder siden 1970
* Men ved at bruge modulus med `2`, så kan vi tælle hver anden
* F.eks. `17179643148 % 2` (uden decimaler) ... giver hvad ?

---

# Brudt ned i bidder, skal vi:

* gemme antal tiendedel-sekunder i en variabel: `scaled`
* og lave den om til et heltal (uden decimaler): `int()`
* gemme resultatet af modulus 2 i en anden variabel: `is_invisible`
* ```python
        scaled = int(time.time() * 10)
        is_invisible = scaled % 2
  ```
* Nu er `is_invisible` **altid** enten `0` eller `1`
* Så kan vi udnøtte et hack i Python:
  * `0` er det samme som `False` og `1` er `True`

---

# Hvis vi skal være usynlige...

Så nu kan vi lave en `if/else` konstruktion hvor vi enten skjuler `player`'en, eller viser den.

```python
        if is_invisible:
            player.hideturtle()
        else:
            player.showturtle()
```

---

# Opdater `animate_spaceship`

Lad os samle det hele i `animate_spaceship` funktionen, i stedet for at skifte farve.

```python
def animate_spaceship():
    if player.is_invincible():
        scaled = int(time.time() * 10)
        is_invisible = scaled % 2
        if is_invisible:
            player.hideturtle()
        else:
            player.showturtle()
    else:
        player.showturtle()
```

- ✅ Erstat den nuværende `animate_spaceship` funktion med koden herover

---

# Prøv spillet

- ✅ Start spillet og se om ikke rumskibet blinker når det bliver ramt af asteroiderne

 