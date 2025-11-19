# More Bullets

Det er da for kedeligt kun med en kugle!

**Er det ikke ?**

---

# En turtle forsvinder aldrig

* Når man først har lavet en `Turtle`, så forsvinder den aldrig HELT.
* Man kan skjule den, men ikke slette den.
* Derfor vil vi genbruge kuglerne
* Vi definerer et makimum
* og laver en liste til at gemme alle kuglerne i

---

# Maksimum antal kugler

* Vi skal definere et maksimum antal kugler
* Vi sætter det til 20 kugler

```python
MAX_BULLETS = 20
```

- ✅ Indsæt koden i `CONSTANTS` sektionen

---

# En liste til all kugler

Vi skal nu have en liste til alle kuglerne.

Husk hvad `for i in range(???)` gør ?

```python
# Create bullets
bullets = []
for i in range(???):
    bullets.append(Bullet())
```

- ✅ Indsæt koden i `GAME SETUP` sektionen
- ✅ Ret `???` til så den kun opretter det maksimale antal kugler. 

HINT: Du har lige defineret det som en konstant

---

# Ny `move_bullets` behaviour

I hvert game loop skal vi:

* løbe listen igennem
* flytte alle de aktive kugler
* gemme en inaktiv kugle... hvis der er en
* Hvis man trykker "space", affyr en inaktiv kugle

---

# Flytte alle de aktive kugler

Løb listen igennem og flyt de aktive kugler

```python
    for bullet in bullets:
        if bullet.active:
            bullet.move()
```

- ✅ Indsæt koden som det første i `move_bullets` funktionen

---

# Gem en inaktiv kugle

Men... vi skal jo huske at gemme en inaktiv kugle, mens vi løber listen igennem.

Inde i `move_bullets` funktionen skal vi som det første have en variable til at gemme en inaktiv bullet:

```python
    inactive_bullet = None
```

- ✅ Indsæt koden som det første i `move_bullets` funktionen

Inde i for-løkken, skal vi nu gemme en kugle i variablen, hvis den ikke er aktiv:

```python
        else:
            inactive_bullet = bullet
```

- ✅ Indsæt koden som else-betingelse til den eksisterende `if`

Så skulle din funktion gerne se nogenlunde sådan her ud:

```python
def move_bullets():
    inactive_bullet = None
    for bullet in bullets:
        if bullet.active:
            bullet.move()
        else:
            inactive_bullet = bullet
```

---

# Affyr inaktiv kugle, HVIS

1. Space er trykket ned, OG
2. Vi fandt en inaktiv kugle - alle kugler kunne jo være aktive.

```python
    if keys_pressed["space"] and inactive_bullet:
        inactive_bullet.fire(player)
```

* Grunden til vi bare kan skrive `and inactive_bullet` er at `None` svarer til `False`, og en anden værdi som `True`
* Det svarer til at skrive `and inactive_bullet is not None`



- ✅ Indsæt koden som det sidste i `move_bullets` funktionen


---

# Prøv spillet

- ✅ Start spillet og se hvad der sker når du trykker space, en enkelt gang eller holder den inde
