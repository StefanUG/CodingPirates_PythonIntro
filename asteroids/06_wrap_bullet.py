import turtle

"""
Prevent bullets from exiting the screen
"""

#
#  CONSTANTS
#

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
BG_COLOR = "black"

GAME_TICK = 20  # milliseconds, lower means faster game
ROTATE_SPEED = 5  # turn 5 degrees each tick
PLAYER_SPEED = 10  # Pixels to move player each tick
BULLET_SPEED = PLAYER_SPEED * 2  # Double of player speed
BULLET_LIFETIME = 75  # game ticks

HALF_WIDTH = int(SCREEN_WIDTH / 2)
HALF_HEIGHT = int(SCREEN_HEIGHT / 2)

#
#  Classes
#


class Bullet(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("light grey")
        self.shapesize(stretch_wid=0.2, stretch_len=0.2)
        self.penup()
        self.hideturtle()
        self.active = False
        self.ttl = BULLET_LIFETIME

    def fire(self, start):
        self.active = True
        self.ttl = BULLET_LIFETIME
        self.setposition(start.xcor(), start.ycor())  # Move the bullet to the player
        self.setheading(start.heading())  # set the same heading as the player
        self.showturtle()  # show the bullet

    def move(self):
        self.forward(BULLET_SPEED)
        move_if_out_of_bounds(self)

        self.ttl -= 1
        if self.ttl < 0:
            self.hideturtle()
            self.active = False


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

# Create a turtle for the bullet
bullet = Bullet()

#
#  EVENTS
#

keys_pressed = {
    "Left": False,
    "Right": False,
    "Up": False,
    "space": False
}

# Make the spaceship move
def press_left():
    keys_pressed["Left"] = True

def release_left():
    keys_pressed["Left"] = False

def press_right():
    keys_pressed["Right"] = True

def release_right():
    keys_pressed["Right"] = False

def press_forward():
    keys_pressed["Up"] = True

def release_forward():
    keys_pressed["Up"] = False

def press_fire():
    keys_pressed["space"] = True

def release_fire():
    keys_pressed["space"] = False


screen.listen()
screen.onkeypress(press_left, "Left")
screen.onkeypress(press_right, "Right")
screen.onkeypress(press_forward, "Up")
screen.onkeypress(press_fire, "space")
screen.onkeyrelease(release_left, "Left")
screen.onkeyrelease(release_right, "Right")
screen.onkeyrelease(release_forward, "Up")
screen.onkeyrelease(release_fire, "space")

#
#  BEHAVIOURS
#


def move_if_out_of_bounds(t: turtle.Turtle):
    # Border checking for bullet
    x = t.xcor()
    y = t.ycor()
    # abs turns any number to a positive number
    if x > HALF_WIDTH:  # too far right
        t.goto(-HALF_WIDTH, y)
    elif x < -HALF_WIDTH:  # too far left
        t.goto(HALF_WIDTH, y)
    if y > HALF_HEIGHT:  # too far up
        t.goto(x, -HALF_HEIGHT)
    elif y < -HALF_HEIGHT:  # too far down
        t.goto(x, HALF_HEIGHT)


def move_spaceship():
    if keys_pressed["Left"]:
        player.left(ROTATE_SPEED)
    if keys_pressed["Right"]:
        player.right(ROTATE_SPEED)
    if keys_pressed["Up"]:
        player.forward(PLAYER_SPEED)
        move_if_out_of_bounds(player)

    
def move_bullets():
    if keys_pressed["space"] and not bullet.active:
        bullet.fire(player)

    if bullet.active:
        bullet.move()


#
#  GAME LOOP
#

def update():
    move_spaceship()
    move_bullets()

    screen.update()
    screen.ontimer(update, GAME_TICK) # this calls the game loop again for the next tick


#
#  START THE GAME
#

update() # call the game loop to start the game
screen.mainloop() # don't close the window
