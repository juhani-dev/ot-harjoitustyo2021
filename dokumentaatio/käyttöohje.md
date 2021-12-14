# käyttöohje

## ohjelman käynnistäminen

1. Asenna riippuvuudet  **poetry install** komennolla
2. Aloita ohjelma **poetry run invoke start** komennolla

## aloitus

ohjelma käynnistyy aloitus näkymään ja punaista neliötä klikkaamaalla pääsee käyttäjä aloittamaan pelin

![kuva](https://github.com/juhani-dev/ot-harjoitustyo2021/blob/master/dokumentaatio/kuvat/start.png)

## Peli
peli näkymä

![kuva](https://github.com/juhani-dev/ot-harjoitustyo2021/blob/master/dokumentaatio/kuvat/game.png)

Kyseessä on Blackjack peli.  Pelin alkaessa jakajalla ja pelaajalla on yhdet kortit. 

 **Hit** painiketta painamalla pelaaja pyytää itselleen lisää kortteja

 **stop** painikkeella pelaaja päättää, että ei halua enempää kortteja ja vuoro siirtyy jakajalle.

 **restart** painikkeella pelaaja voi aloittaa uuden kierroksen

 *dealer hand* kertoo jakajan korttien summan *player hand* pelaajan korttien summan

 *player wins* ja *dealer wins* pitävät kirjaa kuinka monta kättä pelaaja ja jakaja ovat voittaneet

## pelin säännöt

"Pelaaja ilmoittaa, haluaako hän uuden kortin. Jakaja jakaa, kunnes pelaaja ei halua enää lisää kortteja tai korttien summa on yli kaksikymmentäyksi. Tämän jälkeen jakaja ottaa itselleen kortteja, kunnes hänen kätensä on kuusitoista tai enemmän. Jos käden arvo on seitsemäntoista tai enemmän, jakaja ei saa ottaa enempää kortteja. Pelin voittaa se, jolla korttien yhteislukema on suurempi menemättä yli kahtakymmentäyhtä tai tasan 21.  Jos pelaajalla ja jakajalla on yhteislukema sama, pelaaja häviää, paitsi jos kyseessä on tasapeli kahdessakymmenessäyhdessä.  Jos yhteislukema on suurempi kuin kaksikymmentäyksi, sen summan saanut häviää." https://fi.wikipedia.org/wiki/Blackjack