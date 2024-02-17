# Recap fra Lektion 1

- Hvad lærte vi om Turtle?
- Frem, tilbage, drej
- Loops / løkker, `range`
- Indentering / Indrykning
- Brug af TAB og Shift-TAB
- Gem ofte

Evt. gennemgå koden fra Hour of Code - Elsa Level 8

# Lektion 2

## Fortsæt Hour of Code with Elsa and Anna (Level 9)

https://studio.code.org/s/frozen/lessons/1/levels/9

Tilfældige farver
Lav en stjerne, 90 gentagelser.
Hvor mange grader, når der er 360 grader i en hel cirkel.
Meget lille tal.

## Level 9 i Python

## Introduktion til color

```python
color('blue')
```

## Introduktion til Lister

```python
color_names = ["blue", "cyan", "red", "orange", "green"]
```

## Introduktion til random

Imports skal altid stå i toppen

```python
import random
```

Find en tilfældig farve

```python
color(random.choice(color_names))
```


Sæt det hele sammen


```python
from turtle import *
import random

color_names = ["blue", "cyan", "red", "orange", "green"]

# gentag 90 gange
color(random.choice(color_names))
forward(100)
back(100)
right(???)


done()
```

Andre fine farver:

```python
color_names = ["sky blue", "light blue", "turquoise", "cyan", "slate blue", "purple", "magenta", "aquamarine"]
```

Få det til at gå hurtigere

```python
speed(0)
```




## Fortsæt Hour of Code with Elsa and Anna (Level 10)

https://studio.code.org/s/frozen/lessons/1/levels/10

Brug en gentagelse omkring disse blokke til at oprette et parallelogram. Det er ligesom et rektangel, men har forskellige vinkler. Denne ene har 60 grader og 120 graders vinkler i stedet for alle 90 graders vinkler.

## Level 10 i Python

Husk en løkke til at gentage 2 gange

```python
from turtle import *

forward(100)
right(??)
forward(100)
right(??)

done()

```




## Fortsæt Hour of Code with Elsa and Anna (Level 11)

https://studio.code.org/s/frozen/lessons/1/levels/11

Vidste du at alle snefnug har forskellig form? Lad os skabe et nyt snefnug ved hjælp af "Gentag" blokken, for at gentage et parallelogram 4 gange, og dreje 90 grader mellem hvert parallelogram.


## Level 11 i Python

```python
from turtle import *

for i in range(2):
    forward(100)
    right(60)
    forward(100)
    right(120)
right(???)

done()

```




## Fortsæt Hour of Code with Elsa and Anna (Level 12)

https://studio.code.org/s/frozen/lessons/1/levels/12

Lad os nu lave et nyt snefnug ved at bruge gentag blokken til at gentage et parallelogram 10 gange og dreje 36 grader til højre mellem hver.


## Level 12 i Python

```python
from turtle import *

# Gentag 10 gange
for i in range(2):
    forward(100)
    right(60)
    forward(100)
    right(120)
right(???)


done()
```




## Fortsæt Hour of Code with Elsa and Anna (Level 13)

https://studio.code.org/s/frozen/lessons/1/levels/13

En cirkel er en speciel form. Kan du regne ud hvilket tal der skal stå i stedet for spørgsmåls tegnene for at tegne en cirkel?


## Level 13 i Python

```python
from turtle import *

speed(0)

for i in range(???):
    forward(1)
    right(1)

done()
```


Selv med hurtig hastighed går det ret langsomt.

Der er en smartere måde: `circle(radius)`


```python
from turtle import *

circle(50)

done()
```


## Fortsæt Hour of Code with Elsa and Anna (Level 14)

https://studio.code.org/s/frozen/lessons/1/levels/14

Se videon

Lad os lave en hop funktion da vi allerede har en til cirkel

## Pen up og pen down

Indtil nu har vi brugt turtle til at tegne med
Vi har holdt tussen nede hele tiden.
For at hoppe, så skal vi løfte den, og sætte den ned igen.
Det gør man med `penup()` og `pendown()`

## Hop funktion

```python

def hopfrem(trin):
    penup()
    forward(trin)
    pendown()

```

## Level 14 i Python

```python
from turtle import *

def hopfrem(trin):
    penup()
    forward(trin)
    pendown()

# gentag 10 gange
circle(50)
hopfrem(???)

done()

```




## Fortsæt Hour of Code with Elsa and Anna (Level 15)

https://studio.code.org/s/frozen/lessons/1/levels/15

Lad os nu lave 20 overlappende cirkler mens vi drejer 18 grader mellem hver cirkel.

## Level 15 i Python

```python
from turtle import *

def hopfrem(trin):
    penup()
    forward(trin)
    pendown()

# gentag 10 gange
circle(50)
hopfrem(???)
right(???)

done()

```

### Ekstra opgave

Flyt turtle opad, før vi starter

```
penup()
sety(200)
pendown()
```




## Fortsæt Hour of Code with Elsa and Anna (Level 16)

https://studio.code.org/s/frozen/lessons/1/levels/16

Her er en "Lav cirkel" blok, der laver cirkler af forskellig størrelse. Kan du bruge den til at lave en lille cirkel med størrelse 5 og en stor cirkel med størrelse 10?


## Level 16 i Python

```python
    circle(???)
    circle(???)
```

Kan I se noget anderledes ved resultatet fra Turtle ?

Gør det nogen forskel ? - Lad os finde ud af det.



## Fortsæt Hour of Code with Elsa and Anna (Level 17)

https://studio.code.org/s/frozen/lessons/1/levels/16

Indviklede mønstre kan være laves af meget enkle former. Kan du lave et mønster ved at gentagne 5 cirkler af størrelsen 5 og 5 cirkler af størrelsen 10?


## Level 17 i Python

```python

# Gentag 5 gange    
circle(???)
circle(???)
right(???)

```


