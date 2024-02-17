from turtle import *

def hopfrem(trin):
    penup()
    forward(trin)
    pendown()

for i in range(10):
    circle(50)
    hopfrem(25)

done()
