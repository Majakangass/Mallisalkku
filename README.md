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

## Sovelluksen toiminta suurilla tietomäärillä
* Sovellus testattu käyttäen täältä löytyvää seed.py koodia.
 * Testeistä saadut tulostukset ovat seuraavat:
```
elapsed time: 0.04 s
127.0.0.1 - - [29/Jun/2025 21:12:32] "GET /1 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [29/Jun/2025 21:12:32] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.02 s
127.0.0.1 - - [29/Jun/2025 21:12:34] "GET /2 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [29/Jun/2025 21:12:34] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.01 s
127.0.0.1 - - [29/Jun/2025 21:12:36] "GET /3 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [29/Jun/2025 21:12:36] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.02 s
127.0.0.1 - - [29/Jun/2025 21:12:37] "GET /4 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [29/Jun/2025 21:12:37] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.01 s
127.0.0.1 - - [29/Jun/2025 21:12:37] "GET /5 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [29/Jun/2025 21:12:37] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.01 s
127.0.0.1 - - [29/Jun/2025 21:12:38] "GET /6 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [29/Jun/2025 21:12:38] "GET /static/main.css HTTP/1.1" 304 -
```
