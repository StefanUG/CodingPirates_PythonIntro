# Kasser

Lav [Opgave 11](https://studio.code.org/s/course4/lessons/6/levels/11) i Kunstner: Variabler.

> Here’s some more complicated code using the same concepts from the last puzzle - what should you set the `sides` variable to in order to draw this picture made of squares?

## Kunstner: Variabler Opgave 11


```python
from turtle import *

# Dette gør så den starter længere nede
penup()
goto(-50,0)
pendown()


sides = 3

for i in range( sides ):
  for j in range( sides ):
    forward( 100 )
    left( 360 / sides )
  forward( 100 )
  right( 360 / sides )

done()
```

