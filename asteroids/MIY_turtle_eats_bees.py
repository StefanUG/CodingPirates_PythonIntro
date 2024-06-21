import turtle
import random
import time

"""
What about a turtle player that eats bees
WIP / some bees need to be angry
"""

#
#  CONSTANTS
#

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
BG_COLOR = "black"

GAME_TICK = 20  # milliseconds, lower means faster game
ROTATE_SPEED = 5  # turn 5 degrees each tick
PLAYER_SPEED = 5  # Pixels to move player each tick
PLAYER_START_HEALTH = 3
PLAYER_GRACE_PERIOD = 3 # seconds
RELOAD_TIME = 5  # ticks between reload
MAX_ASTEROIDS = 10
ASTEROID_SPEED_MIN = 3
ASTEROID_SPEED_MAX = 7
ASTEROID_RESPAWN_AFTER = 150  # respawn after number of game ticks

FONT_FAMILY = "Courier New"
SCORE_FONT = (FONT_FAMILY, 16, "normal")

HALF_WIDTH = int(SCREEN_WIDTH / 2)
HALF_HEIGHT = int(SCREEN_HEIGHT / 2)

BEE_SHAPE = ((0, -22), (-4, -20), (-7, -13), (7, -13), (-7, -13), (-7.6, -5.6), (7.6, -5.6), (-7.6, -5.6), (-2.6, 7.4),
             (-13.1, -10.5), (-18, -13), (-23, -11), (-25, -6), (-23, -1), (-2.6, 7.5), (-7, 9), (-6, 15), (-4, 17),
             (-7, 20), (-11, 22), (-7, 20), (-4, 17), (0, 18), (4, 17), (7, 20), (11, 22), (7, 20), (4, 17), (6, 15),
             (7, 9), (2.6, 7.5), (23, -1), (25, -6), (23, -11), (18, -13), (13.1, -10.5), (2.6, 7.4), (7.6, -5.6),
             (7, -13), (4, -20))


#
#  Classes
#


class Player(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white", BG_COLOR)
        self.shapesize(2, 2)
        self.penup()

        self.fire_cooldown = 0
        self.alive = True
        self.score = 0
        self.health = PLAYER_START_HEALTH
        self.last_hit = 0.0

    def is_invincible(self):
        # a chance to talk about return values
        return self.last_hit + PLAYER_GRACE_PERIOD > time.time()

    def hit(self):
        if not self.is_invincible():
            self.health -= 1
            self.last_hit = time.time()
            draw_health()

        if self.health == 0:
            self.alive = False

    def eat(self, asteroid):
        asteroid.hit()
        self.score += 1


class Asteroid(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("bee")
        self.color("white", BG_COLOR)
        self.penup()
        x = random.randint(-HALF_WIDTH, HALF_WIDTH)
        y = random.randint(-HALF_HEIGHT, HALF_HEIGHT)
        self.goto(x, y)

        self.radius = 30
        self.speed = 0
        self.respawn_in = 0
        self.reset()

    def reset(self):
        self.setheading(random.randint(0, 360))
        self.speed = random.randint(ASTEROID_SPEED_MIN, ASTEROID_SPEED_MAX)
        self.showturtle()

    def hit(self):
        self.hideturtle()
        self.respawn_in = ASTEROID_RESPAWN_AFTER




#
#  GAME SETUP
#

# Set up the screen
screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT) # width and height
screen.bgcolor(BG_COLOR) # background color
screen.tracer(0) # disable the built in movement animation of turtle

screen.register_shape("bee", BEE_SHAPE)


# Make a turtle for the player
player = Player()

# A pen to write stuff to the screen
pen = turtle.Turtle(visible=False)
pen.color("white")
pen.penup()
pen.goto(-HALF_WIDTH + 20, HALF_HEIGHT - 30)
pen.write("SCORE: ", font=SCORE_FONT)
pen.goto(-HALF_WIDTH + 20, HALF_HEIGHT - 60)
pen.write("HEALTH: ", font=SCORE_FONT)

score_pen = turtle.Turtle(visible=False)
score_pen.color("white")
score_pen.penup()
score_pen.goto(-HALF_WIDTH + 90, HALF_HEIGHT - 30)

health_pen = turtle.Turtle(visible=False)
health_pen.color("white")
health_pen.penup()
health_pen.goto(-HALF_WIDTH + 90, HALF_HEIGHT - 60)

# Create asteroids
asteroids = []
for i in range(MAX_ASTEROIDS):
    asteroids.append(Asteroid())


#
#  EVENTS
#

keys_pressed = {
    "Left": False,
    "Right": False,
    "Up": False
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


screen.listen()
screen.onkeypress(press_left, "Left")
screen.onkeypress(press_right, "Right")
screen.onkeypress(press_forward, "Up")
screen.onkeyrelease(release_left, "Left")
screen.onkeyrelease(release_right, "Right")
screen.onkeyrelease(release_forward, "Up")

#
#  BEHAVIOURS
#


def move_if_out_of_bounds(t: turtle.Turtle):
    # Border checking for turtle
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


def check_collision(with_turtle):
    # Check for collisions between the player and asteroids
    for asteroid in asteroids:
        if asteroid.isvisible() and abs(with_turtle.distance(asteroid)) < asteroid.radius:
            return asteroid
    return None


def animate_spaceship():
    if player.is_invincible():
        scaled = int(time.time() * 10)
        is_invisible = scaled % 2
        if is_invisible:
            player.hideturtle()
        else:
            player.showturtle()
    else:
        player.showturtle()


def move_spaceship():
    if keys_pressed["Left"]:
        player.left(ROTATE_SPEED)
    if keys_pressed["Right"]:
        player.right(ROTATE_SPEED)
    if keys_pressed["Up"]:
        player.forward(PLAYER_SPEED)
        move_if_out_of_bounds(player)
        hit_asteroid = check_collision(player)
        if hit_asteroid:
            # player.hit()
            player.eat(hit_asteroid)
            draw_score()


def move_asteroids():
    for asteroid in asteroids:
        if asteroid.isvisible():
            asteroid.forward(asteroid.speed)
            move_if_out_of_bounds(asteroid) # let the kids figure this one out for a while
            # also this one:
            if abs(player.distance(asteroid)) < asteroid.radius:
                # player.hit()
                player.eat(asteroid)
                draw_score()
        else:
            asteroid.respawn_in -= 1
            if asteroid.respawn_in == 0:
                asteroid.reset()


def draw_score():
    score_pen.clear()
    score_pen.write(player.score, font=SCORE_FONT)


def draw_health():
    health_pen.clear()
    health_pen.write(player.health, font=SCORE_FONT)


#
#  GAME LOOP
#

def update():
    move_spaceship()
    animate_spaceship()
    move_asteroids()

    screen.update()
    if player.alive:
        screen.ontimer(update, GAME_TICK) # this calls the game loop again for the next tick
    else:
        pen.goto(0, 0)
        pen.write("GAME OVER", align="center", font=(FONT_FAMILY, 68, "normal"))


#
#  START THE GAME
#

draw_score()
draw_health()
update() # call the game loop to start the game
screen.mainloop() # don't close the window
