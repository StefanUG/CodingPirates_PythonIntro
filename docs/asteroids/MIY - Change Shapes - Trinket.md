# Lav rumskib formen om

Den ser sådan ud nu:

![spaceship shape in grid](resources/spaceship_grid_shape.png)

Lav evt. jeres egen form her: https://www.geogebra.org/geometry


```python
# CONSTANTS

SPACESHIP_SHAPE = ( (7,-20), (0,5), (-7,-20) )
SPACESHIP_THRUST_SHAPE = turtle.Shape('compound')
SPACESHIP_THRUST_SHAPE.addcomponent(SPACESHIP_SHAPE, BG_COLOR, 'light grey')
SPACESHIP_THRUST_SHAPE.addcomponent(( (7,-20), (0,-30), (-7,-20) ), BG_COLOR, 'orange')
```

Eller brug en af de indbyggede forme:

- arrow
- turtle
- circle
- square
- triangle
- classic

Og sæt den i `Player.__init__` og `animate_spaceship`

```python
# Player.__init__

        self.shape("spaceship")


# animate_spaceship

    if keys_pressed["Up"]:
        player.shape("spaceship_thrust")
    else:
        player.shape("spaceship")

```

# Skyd med laser

Gør `Bullet` helt vildt lang!

```python
self.shapesize(0.1, 10)
```

# Asteroide agtig form

Brug denne `ASTEROID_SHAPE`, eller lav din egen her: https://www.geogebra.org/geometry

![asteroid shape in grid](resources/asteroid_grid_shape.png)


```python
#  CONSTANTS

ASTEROID_SHAPE = ( (-5,-1), (-4,0), (-3,0), (-2,1), (-2,2), (-1,3), (0,3.8), (1,3.2), (2.2,2.3), (2.4,1.5), (4.2,0.7), (4.1,-1), (3,-2.8), (1,-3), (-0.6,-3.8), (-2.5,-3.8), (-4,-2.5), (-5,-1) )

# GAME SETUP

screen.register_shape("asteroid", ASTEROID_SHAPE)


# Asteroid.__init__

        self.shape("asteroid")
        self.shapesize(5, 5)

```


# Drej asteroiden rundt når den flyver


```python

# def move_asteroids():

            asteroid.tilt(asteroid.speed)

```

---

# Skildpadde som skyder bier ?

Du kan også lave dit spil om til at din spiller er en skildpadde med `turtle` formen, og lave asteroiderne om til bier med denne `bee` form:

```python

# CONSTANTS
BEE_SHAPE = ((0, -22), (-4, -20), (-7, -13), (7, -13), (-7, -13), (-7.6, -5.6), (7.6, -5.6), (-7.6, -5.6), (-2.6, 7.4),
             (-13.1, -10.5), (-18, -13), (-23, -11), (-25, -6), (-23, -1), (-2.6, 7.5), (-7, 9), (-6, 15), (-4, 17),
             (-7, 20), (-11, 22), (-7, 20), (-4, 17), (0, 18), (4, 17), (7, 20), (11, 22), (7, 20), (4, 17), (6, 15),
             (7, 9), (2.6, 7.5), (23, -1), (25, -6), (23, -11), (18, -13), (13.1, -10.5), (2.6, 7.4), (7.6, -5.6),
             (7, -13), (4, -20))

# GAME SETUP

screen.register_shape("bee", BEE_SHAPE)

# Asteroid.__init__

        self.shape("bee")
        self.shapesize(1, 1)

