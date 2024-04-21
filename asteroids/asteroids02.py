import turtle

"""
Make the spaceship move
"""

#
#  CONSTANTS
#

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
BG_COLOR = "black"

ROTATE_SPEED = 5  # turn 5 degrees each tick
PLAYER_SPEED = 10  # Pixels to move player each tick

#
#  GAME SETUP
#

# Set up the screen
screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT) # width and height
screen.bgcolor(BG_COLOR) # background color
screen.tracer(0) # disable the built in movement animation of turtle


# Make a turtle for the player
player = turtle.Turtle()
player.shape("triangle")
player.color("light grey", BG_COLOR)
player.shapesize(stretch_wid=0.75, stretch_len=1.5) # Stretch the triangle to be pointy
player.penup() # to not draw lines


#
#  EVENTS
#

# Make the spaceship move
def press_left():
    player.left(ROTATE_SPEED)
    screen.update()

def press_right():
    player.right(ROTATE_SPEED)
    screen.update()

def press_forward():
    player.forward(PLAYER_SPEED)
    screen.update()


screen.listen()
screen.onkey(press_left, "Left")
screen.onkey(press_right, "Right")
screen.onkey(press_forward, "Up")


#
#  START THE GAME
#

screen.update() # Since we disabled the tracer, we manually have to update the screen
screen.mainloop() # don't close the window
