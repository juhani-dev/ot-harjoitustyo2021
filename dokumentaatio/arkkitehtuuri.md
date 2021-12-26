## Rakenne


### Ohjelman  pakkaus arkkitehtuuri

![kuva](https://github.com/juhani-dev/ot-harjoitustyo2021/blob/master/dokumentaatio/kuvat/arc3.png)

#### Ui pitää sisällään käyttölittymän.  Services sovelluslogiikasta vastaavat luokat.  Assets pitää sisällään kuvat mitä ohjelma käyttää.  Main on ohjelman aloittava luokka.


### Toiminnallisuuksia

 # Ohjelman toiminta loogiikkaa kuvattu sekvenssikaavioiden avulla.

Kun käytttäjä on painanut start painiketta Deal luokka luo pakan Create_deck luokan avulla.  Luo aloitus tilanteen jakamalla pelaajalle ja jakajalle kortit. Ui:n Draw luokka hakee kortteja vastaavat kuvat assets tiedostoista ja piirää ne näkyviin käyttäjälle pygame ikkunaan.
 
![kuva](https://github.com/juhani-dev/ot-harjoitustyo2021/blob/master/dokumentaatio/kuvat/arc.png)

käyttäjä painaessa *hit*  painiketta Checks luokka tarkistaa, että korttien summa on alle 22. Jos näin on Deal luokan player_hits metodi lisää pelaajalle yhden kortin lisää, get_hands metodi hakee kaikki pelaajan kortit. Tämän jälkeen Draw luokka hakee kortteja vastaavat kuvat ja piirtää ne pygame ikkunaan käyttäjän näkyville.

![kuva](https://github.com/juhani-dev/ot-harjoitustyo2021/blob/master/dokumentaatio/kuvat/arc2.png)



