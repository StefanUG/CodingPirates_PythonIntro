# Rektangel

![video](https://www.youtube.com/watch?v=BGeT8IyKd2M)

Lav [Opgave 6](https://studio.code.org/s/course4/lessons/6/levels/6) i Kunstner: Variabler.

> Now I want to make a rectangle that is twice as tall as it is wide. We've got a variable called width that needs to be set to 100. Can you use the math blocks to complete the code?

## Mere matematik

En rektangel er længere på den ene side end på den anden.

Vi kan gange med 2 for at få den ene side dobbelt så lang som den anden:

I programmering, og Python, bruger man en `*` som et gange tegn. F.eks.

    2 * length

## Kunstner: Variabler Opgave 6

```python
from turtle import *

# Dette gør så den starter længere nede
penup()
goto(0,-150)
pendown()


width = ???

for i in range(2):
  forward( width )
  left(90)
  forward( ? * ? )
  left(90)

done()
```
