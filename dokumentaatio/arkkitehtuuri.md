## Rakenne



#### Ohjelman tämän hetkinen pakkaus arkitehtuuri

![kuva](https://github.com/juhani-dev/ot-harjoitustyo2021/blob/master/dokumentaatio/kuvat/pakkaus.png)

#### käyttöliittymä eriytetään ui:hin , services taas vastaa sovelluslogiikasta ja assets pitää sisällään kuvat mitä services käyttää.


### Käyttöliittymä koostuu
	- näkymä mistä peli voidaan aloittaa start painikkeella
	- itse peli näkymästä
	Nämä ovat kahdessa eri luokassa (joista toinen vielä ui tiedoston ulkopuolella)


### Esimerkki sovelluslogiikasta

![kuva](https://github.com/juhani-dev/ot-harjoitustyo2021/blob/master/dokumentaatio/sekvenssikaavio.png)

