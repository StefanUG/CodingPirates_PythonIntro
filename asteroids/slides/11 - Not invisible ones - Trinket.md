# Ikke skyde de usynlige asteroider

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


- ✅ Find `if` sætnigen i `check_collision` funktionen, og indsæt `asteroid.isvisible() and ` så det er det første i `if` sætningen

--- 

# Prøv spillet

- ✅ Start spillet og se om du kan skyde udenom de usynlige asteroider

