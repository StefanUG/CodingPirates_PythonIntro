from turtle import *

def hopfrem(trin):
    penup()
    forward(trin)
    pendown()

def opret_snefnuggren():
    dybde = 3
    grene = 3
    hopfrem(30*dybde)
    left(45)
    for d in range(dybde):
        for g in range(grene):
            forward(30)
            back(30)
            right(135/grene)
        left(90)
        back(30)
        left(45)
    right(45)


#speed(0)

for i in range(3):
    opret_snefnuggren()
    right(45)

done()
