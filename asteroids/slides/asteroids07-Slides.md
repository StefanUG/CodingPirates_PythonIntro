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

## Flere kugler

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

---

# En liste til all kugler

En liste er en slags variabel hvor man kan have mere end en værdi!


<div class="container">
<div class="col">

### Eksempel

```python
# En tom liste
my_list = []
# Tilføj noget til listen
my_list.append("bird")
# Print det første element fra listen
print(my_list[0])

another_list = ["monkey"]
# Print det første element fra listen
print(another_list[0])
```

</div>
<div class="col">

### List of Bullets

```python
# Create bullets
bullets = []
for i in range(MAX_BULLETS):
    bullets.append(Bullet())
```

* Kan I huske `range` ?

</div>
</div>

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
def move_bullets():
    for bullet in bullets:
        if bullet.active:
            bullet.move()
```

---

# Gem en inaktiv kugle

Men... vi skal jo huske at gemme en inaktiv kugle, mens vi løber listen igennem.

```python
def move_bullets():
    inactive_bullet = None # En variabel uden nogen værdi (None)
    for bullet in bullets:
        if not bullet.active: # Hvis kuglen ikke er aktiv
            inactive_bullet = bullet # gem kuglen i variablen til senere
        elif bullet.active: # ellers hvis kuglen er aktiv
            bullet.move() # flyt den
```

* Kan det gøres bedre?

---

# Affyr inaktiv kugle, HVIS

1. Space er trykket ned, OG
2. Vi fandt en inaktiv kugle - alle kugler kunne jo være aktive.

```python
def move_bullets():
    # SNIP
    if keys_pressed["space"] and inactive_bullet:
        inactive_bullet.fire(player)
```

* Grunden til vi bare kan skrive `and inactive_bullet` er at `None` svarer til `False`, og en anden værdi som `True`
* Det svarer til at skrive `and inactive_bullet is not None`

---

# NU !!! Gå ind på:

## stefanug.trinket.io

- og klik "Build an Asteroids Game in Python"
- find Lesson 3 og "**More Bullets**"

Når I ser dette, så er der opgaver I skal løse, f.eks:

- ✅ Sæt koden ind i `CONSTANTS` sektionen

 