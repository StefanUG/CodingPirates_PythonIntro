from turtle import *

def hopfrem(trin):
    penup()
    forward(trin)
    pendown()

def opret_snefnuggren():
    hopfrem(90)
    left(45)
    for d in range(3):
        for g in range(3):
            forward(30)
            back(30)
            right(45)
        left(90)
        back(30)
        left(45)
    right(45)


for i in range(8):
    opret_snefnuggren()
    right(45)

done()
