# Femkanter (Pentagons)

Lav [Opgave 5](https://studio.code.org/s/course4/lessons/6/levels/5) i Kunstner: Variabler.

> Draw this pattern of pentagons with 100 pixel sides by setting the right value for length and dropping the length variable into all of the the correct places.
> 
> See how you only have to set the value for length once, and the code uses the right value everywhere?

## Kunstner: Variabler Opgave 5

```python
from turtle import *
import random

# Dette gør så den starter længere nede
penup()
goto(0,-150)
pendown()

color_names = ["green", "blue", "orange", "red", "purple"]

def random_color(): return random.choice(color_names)

length = ???

for j in range(5):
  color(random_color())
  for i in range(6):
    forward(  )
    left(360 / 5)
  forward(  )

done()
```
