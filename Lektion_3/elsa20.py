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


def snefnug_firkant():
    for i in range(10):
        for j in range(4):
            forward(100)
            right(90)
        right(36)

def snefnug_parallelogram():
    for j in range(10):
        for i in range(2):
            forward(100)
            right(60)
            forward(100)
            right(120)
        right(36)

# Tilføj de resterende

snefnug_parallelogram() 

done()
