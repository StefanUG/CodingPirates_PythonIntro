# Farver i Python

Der er mange farver at vælge i mellem:

![colors in tkinter](https://patriciaemiguel.com/assets/tkinter_colores.png)

Find også farver her: https://trinket.io/docs/colors

Og ændr farven på enten baggrund, Player, Bullet, Asteroid, tekst, osv.

Find de forskellige farver i koden ved at søge efter `color` ved at trykket `Ctrl+F`

---

## Tilfældig farve

Du kan også finde en tilfældig farve, vha. `random` biblioteket, som vi også 
bruger til at finde tilfældige koordinater til vores asteroider.

```python
# liste mad farver at vælge imellem
asteroid_colors = ["blue", "cyan", "red", "orange", "green"]

# f.eks. i Asteroid, __init__ eller reset
self.color(random.choice(asteroid_colors))
```