from turtle import *

def hopfrem(trin):
    penup()
    forward(trin)
    pendown()

speed(0)
penup()
sety(200)
pendown()

for i in range(20):
    circle(50)
    hopfrem(50)
    right(18)

done()
