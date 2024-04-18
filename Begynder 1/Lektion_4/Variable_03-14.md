# Tegn frit

Lav [Opgave 14](https://studio.code.org/s/course4/lessons/6/levels/14) i Kunstner: Variabler.

> Free Play: Check it out! Now your algorithm is nested within one more loop. Experiment with changing the values of your two variables to draw cool patterns.
> 
> For even more effect, try playing with color! Use random colors inside loops to see how it changes your design.

## Kunstner: Variabler Opgave 14


```python
from turtle import *
import random

speed(0)

color_names = ["green", "blue", "orange", "red", "purple"]

def random_color(): return random.choice(color_names)

# Dette gør så den starter længere nede
penup()
goto(-50,0)
pendown()


sides = 8
length = 200 / sides

for i in range(sides):
  for j in range(sides):
    for k in range(sides):
      forward(length)
      right(360/sides)
    forward(length)
    left(360/sides)
  forward(length)
  right(360/sides)


done()
```

### Hints

```python

# skift farve
color(random_color())

# Turtle :)
shape("turtle")

# Hastighed
speed(0)

```