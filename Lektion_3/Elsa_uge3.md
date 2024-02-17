# Recap fra Lektion 2

- anvendelse af lister til farver: `["blue", "red"]`
- random: `random.choice`
- definere funktioner med egne navne, f.eks. `hopfrem`
- løfte og sætte tussen (`penup()` og `pendown()`)
- tegne cirkler med `circle` 
- skifte hastighed med `speed()`


# Lektion 3

## Fortsæt Hour of Code with Elsa and Anna (Level 18)

https://studio.code.org/s/frozen/lessons/1/levels/18

Prøv at bruge blokken, "Lav en snefnug-gren", for at lave 3 grene, der nu begynder at ligne et snefnug.


## Opret snefnuggren funktion

```python
def opret_snefnuggren():
    hopfrem(90)
    left(45)
    for dybde in range(3):
        for grene in range(3):
            forward(30)
            back(30)
            right(45)
        left(90)
        back(30)
        left(45)
    right(45)
```

## Level 18 i Python

```python
from turtle import *

def hopfrem(trin):
    penup()
    forward(trin)
    pendown()

def opret_snefnuggren():
    hopfrem(90)
    left(45)
    for d in range(3):
        for g in range(3):
            forward(30)
            back(30)
            right(45)
        left(90)
        back(30)
        left(45)
    right(45)


# når programmet kører


done()
```




## Fortsæt Hour of Code with Elsa and Anna (Level 19)

https://studio.code.org/s/frozen/lessons/1/levels/19

Lad os nu gentage det 8 gange for at lave et smukt snefnug!


## Level 19 i Python

```python
from turtle import *

# hopfrem funktion
# opret snefnuggren funktion

# når programmet kører
for i in range(8):
    opret_snefnuggren()
    right(???)

done()
```

## Fortsæt Hour of Code with Elsa and Anna (Level 20)

https://studio.code.org/s/frozen/lessons/1/levels/20

Du er nu officielt en stor kunstner! Lav et vinterdrømmeland.

## Level 20 i Python

Lav lige hvad du har lyst til

### Udfordringer

Prøv at lave snefnug funktioner ud af de forskellige typer:
- firkanter (level 6)
- streger (level 9)
- parallelogram (level 12)
- spiral (level 15)
- blomst (level 17)
- fraktal (level 19)

f.eks. en snefnugfunktion af firkant typen:

```python

def snefnug_firkant():
    for i in range(10):
        for j in range(4):
            forward(100)
            right(90)
        right(36)



```
