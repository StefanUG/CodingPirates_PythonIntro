---
theme: gaia
marp: true
---

# Conditionals i Python

---

# If-sætninger

```
if card.is_red():
    points.yours = points.yours + 1
```
## If/Else

```
if card.is_red():
    points.yours = points.yours + 1
else:
    points.other = points.other + 1
```

---

## Else if: `elif` (som det hedder i Python)




> If I draw a 7, clap.
> Else if I draw something less than 7, you say "YAY".
> Else say "Awwwwe".


```
card = pile.draw()
if card.value == 7:
    print("*** CLAP, CLAP, CLAP ***")
elif card.value < 7:
    print("YAY")
else:
    print("Awwwwe")
```

**HUSK** Kolon `:` og indrykning (aka *indentation*)

---

## Install IDE

IDE betyder "Integrated Development Environment" og bruges til at programmere og lave apps og programmer i.

- Søg efter "PyCharm"
- Download "Community Edition"
- Installer

---

## Hent kode projektet

- Gå til github.com/StefanUG
- Under Repositories find "code-org-python"
- Download release "2024-04-02" *enten zip (Win) eller tar.gz (Mac)*
- Pak det ud
- Åbn PyCharm, og vælg Open
- Vælg den folder som blev pakket ud. Vigtigt! Den som indeholder `README.md` filen
- Sig ja til at den opretter et Python Environment


--- 

# Mød bien 🐝

I python kan man skrive:

```python
bee.forward()
bee.right()
bee.left()
bee.get_nectar()
bee.at_flower() # Ja (True), hvis bien er ved en blomst, ellers nej (False)
```

--- 

# Hvis 🌺, tag nektar

```python
if bee.at_flower():
    bee.get_nectar()
```

For loops virker stadig

```python
for i in range(3):
    bee.forward()
```

Men forward kan noget smart 😎

```python
bee.forward(3) # Ryk frem 3 gange
```
---

# Nu er det jeres tur

Nu skal I lave code.org: If/Else with Bee:

- studio.code.org/s/coursed
- find Lesson 14 og start

