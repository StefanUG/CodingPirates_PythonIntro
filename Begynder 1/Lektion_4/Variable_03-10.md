# Fri tegning

Lav [Opgave 10](https://studio.code.org/s/course4/lessons/6/levels/10) i Kunstner: Variabler.

> Free Play: Experiment with the number of sides this shape has. Can you change the algorithm so that the overall size of the shape stays the same, no matter how many sides it has?

## Kunstner: Variabler Opgave 10


```python
from turtle import *

# Dette gør så den starter længere nede
penup()
goto(-100,-150)
pendown()


sides = 4

for i in range( sides ):
  forward( 150 )
  left( 360 / sides )

done()
```

