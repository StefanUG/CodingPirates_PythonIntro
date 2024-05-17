# Asteroid spil forløb


| Uge | 1. time | 2. time |
|:-:|--|--|
| 0 | Workshop præsentation   | Install PyCharm, start på projekt, create screen and a player (1), simple events (2) |
| 1 | Intro til Game Loop, move better (3)  | Wrap player (4), function with parameters  |
| 2 | Intro til classes, create a bullet, make spaceship shoot (5) | Wrap the bullet (6), add more bullets (7)   |
| 3 | Refactor to Player class and shoot less rapidly (8)    | Add asteroids (9) and shoot them (10) but not the invisible ones (11)  |
| 4 | Game over when hitting asteroid (12) and keep a score (13)  | Make the asteroids move (14) and respawn (15)  |
| 5 | Let's have more than one life (16)   |  Let's add a grace period (17)  |
| 6 | Flash when hit (18)  |  Move with thrust like in space (19)  |
| 7 | Thrust animation (20)  |  Demo to the others  |

# Step by step

- 1 Create Screen and Player
- 2 Make the spaceship move  with events
- 3 Make it move better with keypress and keyrelease
- 4 Make the spaceship shoot with one bullet
- 5 Prevent player from exiting the screen (or appearing in the other side)
- 6 Add a lifetime to the bullets, and make them move across screens too
- 7 Add more bullets, but oops, they are too rapidly firing
- 8 Let's add a Player class and a cooldown/reload time
- 9 Add asteroids
- 10 shoot the asteroids
- 11 why are the bullets not passing on?
- 12 game over if hitting the asteroids
- 13 add score and display it
- 14 Make the asteroids move
- 15 Respawn asteroids
- 16 add health and a grace period after being hit
- 17 add a grace period after being hit
- 18 flash during grace period
- 19 move like in space
- 20 add thrust animation

More advanced
- break down asteroids when they are shot
- make the ship follow the mouse pointer and click to shoot
- make explosion animations
- make custom shapes for asteroids
- make random shapes for asteroids
- make the asteroids rotate as they move
- 

## Noter om materialet

Følg selv med materialet for lesson 2 var lidt for svært. Bør rettes til, så det bliver lidt letter.

## Acceleration

Track vs. Heading

![track vs heading](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fprod-cms.scouts.org.uk%2Fmedia%2F10408%2Ftrackcourseheading.png%3Fwidth%3D1800&f=1&nofb=1&ipt=961372850de22f7162679f4f5ba38d1e8d03468da51617a97e30d140af6b70be&ipo=images)

```python
def thrust():
    if s1.alive:
        s1.thrustlife = 0.5
        thrust_direction = s1.direction + math.pi/2
        s1.speedx, s1.speedy = s1.speedx + 5 * math.cos(thrust_direction), s1.speedy + 5 * math.sin(thrust_direction)
        speed = (s1.speedx ** 2 + s1.speedy ** 2) ** 0.5
        if speed > Spaceship.maxspeed:
            s1.speedx, s1.speedy = (s1.speedx * Spaceship.maxspeed) / speed, (s1.speedy * Spaceship.maxspeed)/speed
```

## Inspiration

The best implementation of the game so far:

[Asteroid_Turtles by BL-Lee](https://github.com/BL-Lee/Asteroid_Turtles/blob/master/Asteroids.py)

Though the resulting game is not great, there are some great ideas in it, like random asteroid shapes adn explosions.

https://github.com/HaimingXu679/Asteroids
