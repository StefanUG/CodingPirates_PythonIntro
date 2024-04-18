# Sekskanter / Hexagon

Lav [Opgave 4](https://studio.code.org/s/course4/lessons/6/levels/4) i Kunstner: Variabler.

> Let's try it again!
> Can you set the length variable to 60 to make this cool design with hexagons?

## Matematik

Computere er rigtig god til matematik.

Der er 360 grader i en cirkel. Så hvis man vil tegne en trekant, skal man lave tre kanter og dreje 120 grader hver gang. 

> Det er fordi 120 gange 3 er 360

For at regne den anden vej, hvis du vil lave tre kanter, skal du dele 360 grader med 3:

    360 ÷ 3 = 120
  

På en computer bruger vi `/` (skråstreg) til at dividere med. Så vi skal skrive

    360 / 3

for at få 120.

Hvis man vil lave en sekskant skal man dividere med 6. Og det kan vi bare få computeren til at regne ud for os.

## Kunstner: Variabler Opgave 4

Tegn et sejt design med sekskander

```python
from turtle import *
import random

color_names = ["green", "sky blue", "light blue", "turquoise", "cyan", "slate blue", "medium orchid", "magenta", "aquamarine"]

def random_color(): return random.choice(color_names)

length = ???

for j in range(6):
  color(random_color())
  for i in range(6):
    forward(length)
    left(360 / 6)
  left(60)

done()
```
