# Mange-kant

Lav [Opgave 7](https://studio.code.org/s/course4/lessons/6/levels/7) i Kunstner: Variabler.

> Here’s some code that can draw any regular polygon.
> 
> There’s a new variable called sides that is set to 4.
> 
> Can you use the sides variable (along with the math block) to turn the right amount regardless of how many sides are in the polygon?

## Husk hvordan man dividerer

    360 / sides

## Kunstner: Variabler Opgave 7


```python
from turtle import *

# Dette gør så den starter længere nede
penup()
goto(-150,-150)
pendown()


sides = ???

for i in range( sides ):
  forward( 150 )
  left( 360 / ? )

done()
```
