# Tegn efter

![tegn efter dette mønster](https://images.code.org/b5e28b084cb331ee030ea3853ed921bd-image-1440060815818.51.21.png)

Lav [Opgave 15](https://studio.code.org/s/course4/lessons/6/levels/15) i Kunstner: Variabler.

> Free-Play Inspiration: You've now learned everything you need to know to make a pattern like this! If this picture inspires you, try to make something similar. Otherwise, create something all your own.

## Kunstner: Variabler Opgave 15


```python
from turtle import *
import random

speed(0)

color_names = ["green", "blue", "orange", "red", "purple"]

def random_color(): return random.choice(color_names)



done()
```

### Hints

```python

# loop
for i in range( ? ):

# skift farve
color(random_color())

# Turtle :)
shape("turtle")

# Hastighed
speed(0)

```