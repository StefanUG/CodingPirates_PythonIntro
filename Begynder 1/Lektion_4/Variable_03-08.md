# Sekskant igen

Lav [Opgave 8](https://studio.code.org/s/course4/lessons/6/levels/8) i Kunstner: Variabler.

> Use what you learned in the last puzzle to create this hexagon using the sides variable.
> 
> See how you could change just one value to draw a triangle, square, pentagon, or octagon?

## Husk hvordan man dividerer

    360 / sides

## Kunstner: Variabler Opgave 8


```python
from turtle import *

# Dette gør så den starter længere nede
penup()
goto(-100,-150)
pendown()


sides = ???

for i in range( ? ):
  forward( 150 )
  left( 360 / ? )

done()
```
