# To variabler

Lav [Opgave 12](https://studio.code.org/s/course4/lessons/6/levels/12) i Kunstner: Variabler.

> Let's set the sides variable to 5. The more sides we add to this algorithm, the bigger this whole pattern gets!
> 
> Notice that there is another variable called length. We can now use that variable wherever we have a move forward block.
> 
> Set the length variable to 75 for this shape.

## Kunstner: Variabler Opgave 12


```python
from turtle import *

# Dette gør så den starter længere nede
penup()
goto(-50,0)
pendown()


sides = ??
length = ???

for i in range( sides ):
  for j in range( sides ):
    forward( ? )
    left( 360 / sides )
  forward( ? )
  right( 360 / sides )

done()
```

