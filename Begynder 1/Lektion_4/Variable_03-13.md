# Juster størrelse

Lav [Opgave 13](https://studio.code.org/s/course4/lessons/6/levels/13) i Kunstner: Variabler.

> When a shape has lots of sides, each side needs to be shorter if you want the whole pattern to fit on the screen.
> 
> Let's recreate the algorithm for this amazing pattern, but instead of manually setting the length variable, let's use a math block with the sides variable inside to make sure that each shape fits correctly.
> 
> The perimeter of each polygon is 300 pixels.

## Kunstner: Variabler Opgave 13


```python
from turtle import *

# Dette gør så den starter længere nede
penup()
goto(-50,0)
pendown()


sides = ??
length = ???


done()
```

### Hints

```python


length = 300 / ?

# Loop
for i in ragnge( ? ):
  forward()
  left()


```