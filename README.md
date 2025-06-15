# Mallisalkku


* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
* Käyttäjä pystyy lisäämään sovellukseen omia sijoitussalkkuja. Lisäksi käyttäjä pystyy muokkaamaan ja poistamaan lisäämiään sijoitussalkkuja.
* Käyttäjä näkee sovellukseen lisätyt sijoitussalkut. Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät sijoitussalkut.
* Käyttäjä pystyy etsimään sijoitussalkkuja hakusanalla. Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä sijoitussalkkuja.
* Sovelluksessa on käyttäjäsivut, jotka näyttävät jokaisen käyttäjän lisäämät sijoitussalkut.
* Käyttäjä pystyy valitsemaan sijoitussalkulle useamman luokittelun sekä lisäämään, poistamaan sekä muokkaamaan kuvia omissa postauksissa.
* Käyttäjä pystyy kommentoimaan omia sekä muiden käyttäjien julkaisuja.
* Sovelluksessa on pääasiallisen tietokohteen (sijoitussalkun) lisäksi toissijainen tietokohde (kommentointi), joka täydentää pääasiallista tietokohdetta.

Tulossa:

* Ulkoasua tullaan yhtenäistämään
* Yleisesti pieniä virheitä korjaamaan
* Käyettävyyttä sekä otsikoiden ja kuvausten loogisuutta tullaan parantamaan

Tässä on suomenkielinen versio käynnistysohjeista, jotka voit lisätä README-tiedostoosi GitHubissa. Tämä malli noudattaa samaa rakennetta kuin esimerkkikuvassa:

Tässä päivitetyt ohjeet ympäristömuuttujilla ja käyttöohjeilla:

---

## Asennusohjeet

### Luo tietokanta:

```bash
$ sqlite3 database.db < schema.sql
```

### Alusta tietokanta:

```bash
$ sqlite3 database.db < init.sql
```

### Luo virtuaaliympäristö:

```bash
$ python3 -m venv venv
```

### Käynnistä virtuaaliympäristö:

```bash
$ source venv/bin/activate
```

### Asenna tarvittavat kirjastot (esim. Flask):

```bash
$ pip install flask
```

> Vaihtoehtoisesti, jos käytössä on `requirements.txt`:
>
> ```bash
> $ pip install -r requirements.txt
> ```

### Aseta ympäristömuuttujat:

```bash
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
```

### Käynnistä sovellus:

```bash
$ flask run
```

### Sovelluksen käyttö:

Kun palvelin on käynnissä, voit avata sovelluksen selaimessa osoitteessa:

```
http://localhost:5000
```

---

Voit liittää nämä suoraan README-tiedostoosi. Kerro jos haluat lisätä vielä Docker-version tai Windows-käyttöön sovitetun version!
