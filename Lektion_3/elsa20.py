from turtle import *
import random

color_names = ["white", "sky blue", "light blue", "turquoise", "cyan", "slate blue", "purple1", "magenta", "aquamarine"]

def nyfarve(): return random.choice(color_names)

# Prøv at ændre baggrundsfarven
screen = Screen()
screen.bgcolor("RoyalBlue")

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

def snefnug_fraktal():
    for i in range(8):
        opret_snefnuggren()
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

def snefnug_streger():
    for i in range(90):
        color(nyfarve())
        forward(100)
        back(100)
        right(4)


# Tilføj de resterende

# Ny funktion til at flytte turtle positionen
def teleport(x, y):
    penup()
    goto(x, y)
    pendown()

speed(0)

screensize(600, 600)

teleport(-200,-200)
color(nyfarve())
snefnug_parallelogram()

teleport(200,-200)
color(nyfarve())
snefnug_fraktal()

teleport(-200,200)
color(nyfarve())
snefnug_firkant()

teleport(200,200)
snefnug_streger()


done()
