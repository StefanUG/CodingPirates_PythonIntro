# Skift knapper

F.eks. til A, W, D

Find det sted i koden som handler om events, efter `screen.listen()`

```python
screen.listen()
screen.onkeypress(press_left, "Left")
screen.onkeypress(press_right, "Right")
screen.onkeypress(press_forward, "Up")
screen.onkeypress(press_fire, "space")
screen.onkeyrelease(release_left, "Left")
screen.onkeyrelease(release_right, "Right")
screen.onkeyrelease(release_forward, "Up")
screen.onkeyrelease(release_fire, "space")
```

og skift det ud med de ønskede knapper

```python
screen.listen()
screen.onkeypress(press_left, "a")
screen.onkeypress(press_right, "d")
screen.onkeypress(press_forward, "w")
screen.onkeypress(press_fire, "space")
screen.onkeyrelease(release_left, "a")
screen.onkeyrelease(release_right, "d")
screen.onkeyrelease(release_forward, "w")
screen.onkeyrelease(release_fire, "space")
```

Men bemærk CAPS LOCK