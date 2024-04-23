import turtle
import random
import time

"""
Let's make the spaceship flash instead of turning red, when it is invincible
"""

#
#  CONSTANTS
#

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
BG_COLOR = "black"

GAME_TICK = 20 # miliseconds, lower means faster game
ROTATE_SPEED = 5 # turn 5 degrees each tick
PLAYER_SPEED = 10 # Pixels to move player each tick
PLAYER_START_HEALTH = 3
PLAYER_GRACE_PERIOD = 3 # seconds
BULLET_SPEED = PLAYER_SPEED * 2 # Double of player speed
BULLET_LIFETIME = 75  # live for 200 game ticks
MAX_BULLETS = 10
RELOAD_TIME = 5  # ticks between reload
MAX_ASTEROIDS = 10
ASTEROID_SPEED_MIN = 1
ASTEROID_SPEED_MAX = 5
ASTEROID_RESPAWN_AFTER = 150  # respawn after number of game ticks

FONT_FAMILY = "Courier New"
SCORE_FONT = (FONT_FAMILY, 16, "normal")

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


class Player(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.color("light grey", BG_COLOR)
        self.shapesize(stretch_wid=0.75, stretch_len=1.5)  # Stretch the triangle to be pointy
        self.penup()  # to not draw lines

        self.fire_cooldown = 0
        self.alive = True
        self.score = 0
        self.health = PLAYER_START_HEALTH
        self.last_hit = 0.0

    def shoot(self, inactive_bullet):
        if self.fire_cooldown == 0:
            inactive_bullet.fire(player)
            self.fire_cooldown = RELOAD_TIME

    def cooldown(self):
        if self.fire_cooldown > 0:
            self.fire_cooldown -= 1

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


class Asteroid(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=3, stretch_len=3)
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

# Create bullets
bullets = []
for i in range(MAX_BULLETS):
    bullets.append(Bullet())

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


def check_collission(with_turtle):
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
        if check_collission(player):
            player.hit()


def move_bullets():
    player.cooldown()
    inactive_bullet = None
    for bullet in bullets:
        if not bullet.active:
            inactive_bullet = bullet
        elif bullet.active:
            bullet.move()
            hit_asteroid = check_collission(bullet)
            if hit_asteroid:
                hit_asteroid.hit()
                bullet.hideturtle()
                bullet.active = False
                player.score += 1
                draw_score()

    if keys_pressed["space"] and inactive_bullet:
        player.shoot(inactive_bullet)


def move_asteroids():
    for asteroid in asteroids:
        if asteroid.isvisible():
            asteroid.forward(asteroid.speed)
            move_if_out_of_bounds(asteroid) # let the kids figure this one out for a while
            # also this one:
            if abs(player.distance(asteroid)) < asteroid.radius:
                player.hit()
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
    move_bullets()
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
