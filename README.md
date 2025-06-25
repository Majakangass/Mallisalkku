# Mallisalkku

## Sovelluksen toiminnot

* Käyttäjä pystyy luomaan käyttäjän ja kirjautumaan sisään sovellukseen.
* Käyttäjä pystyy lisäämään sovellukseen uusia sijoitussalkkuja.
  * Käyttäjä pystyy muokkaamaan ja poistamaan lisäämiään sijoitussalkkuja.
* Käyttäjä näkee sovellukseen lisätyt sijoitussalkut.
  * Käyttäjä näkee omat ja muiden käyttäjien lisäämät sijoitussalkut.
* Käyttäjä pystyy etsimään sijoitussalkkuja hakusanalla.
  * Käyttäjä pystyy hakemaan omia ja muiden käyttäjien lisäämiä sijoitussalkkuja.
* Sovelluksessa on käyttäjäsivut, jotka näyttävät käyttäjien lisäämät sijoitussalkut.
* Käyttäjä pystyy valitsemaan sijoitussalkulle useamman luokittelun.
* Käyttäjä pystyy lisäämään kuvia omiin postauksiinsa.
  * Käyttäjä pystyy myös poistamaan kuvia omista postauksistaan.
* Käyttäjä pystyy kommentoimaan omia sekä muiden käyttäjien julkaisuja.
* Sovelluksessa on pääasiallisen tietokohteen (sijoitussalkun) lisäksi toissijainen tietokohde (kommentointi), joka täydentää pääasiallista tietokohdetta.

---

## Sovelluksen asennusohjeet
### Asenna flask -kirjasto:
```
$ pip install flask
```

### Luo sekä alusta tietokanta:
```
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql
```

### Käynnistä sovellus:
```
$ flask run
```
---
