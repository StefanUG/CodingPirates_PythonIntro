from turtle import *
import random

#color_names = ["sky blue", "light blue", "turquoise", "cyan", "slate blue", "purple", "magenta", "aquamarine"]
color_names = ["blue", "cyan", "red", "orange", "green"]

speed(0)

for i in range(90):
    color(random.choice(color_names))
    forward(100)
    back(100)
    right(4)

done()
