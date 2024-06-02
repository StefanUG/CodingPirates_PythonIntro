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

## Går livene for hurtigt?

Når hvert game tick tæller dine liv ned så går det ret hurtigt med at miste de liv.

Lad os indsætte en lille "henstandstid" aka "Grace Period"

---

# Hvor mange sekunder før vi kan blive ramt igen?

* Lad os sige 3 sekunder
* Burde være tid nok til at komme væk fra asteroiden
* ```python
  PLAYER_GRACE_PERIOD = 3 # seconds
  ```

---

# At holde styr på tiden

Nu skal vi til at holde styr på tiden, så vi kan tælle sekunder.

* Vi skal bruge et nyt bibliotek:
* ```python
  import time
  ```

---

# NU !!! Gå ind på:

## stefanug.trinket.io

- og klik "Build an Asteroids Game in Python"
- find Lesson 6 og "**17. Health Grace Period**"

Når I ser dette, så er der opgaver I skal løse, f.eks:

- ✅ Sæt koden ind i `CONSTANTS` sektionen

 