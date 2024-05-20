---
theme: gaia
marp: true
---
<style>
.container{
    display: flex;
}
.col{
    flex: 1;
}
</style>
<!-- need to enable HTML in the MARP extension -->

# Asteroids Game

## Ikke skyde de usynlige asteroider

Kan I se kuglen forsvinder når vi skyder der hvor der var en asteride vi har skudt?

Dem vi har skudt skal da ikke skydes igen?

---

# Hvordan kan vi undgå det?

* I `check_collision` løber vi hele listen af asteroider igennem
* Uanset om de er synlige eller ej
* Så vi skal lige tjekke om de er synlige inden vi tjekker afstanden: `if asteroid.isvisible()`
* Sammensat i samme `if` giver det:
  ```python
    if asteroid.isvisible() and abs(with_turtle.distance(asteroid)) < asteroid.radius:
            return asteroid
  ```

--- 

# NU !!! Gå ind på:

## stefanug.trinket.io

- og klik "Build an Asteroids Game in Python"
- find Lesson 4 og "**Shoot asteroids**"

Når I ser dette, så er der opgaver I skal løse, f.eks:

- ✅ Sæt koden ind i `CONSTANTS` sektionen

 