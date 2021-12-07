# ohjelmistotekniikka Blackjack sovellus

Sovelluksella voi pelata pygame:illa tehtyä blackjack peliä.  Tässä vaiheessa vielä hyvin yksinkertaistettua versiota.  Blackjackissa jaetaa ensin jakajalle ja pelaajalle yksi kortti. Pelaaja voi pyytää lisää kortteja tai antaa vuoron halutessaan jakajalle.  Jakaja jakaa itselleen kortteja kunnes summa on 16 tai enemmän, jos summa on 17 tai enemmän ei jakaja jaa enemäpä kortteja.

Voittajan summa on 21 tai se kumpi on lähempänä 21:tä.

## Ohjeet 
Pelissä **hit** napilla voi pyytää lisää kortteja

**stop** napilla pelaaja tytyy sen hetkiseen käteensä ja jakaja aloittaa oman vuoronsa

**restart** napilla voi aloittaa uuden kierroksen


## Asennus

 Riipuvuudet asennetaan komennolla **poetry install**

## Ohjelman käynnistys

 Ohjelma aloitetaan komennolla **poetry run invoke start**

## Testit

 Testit suoritetaan komennolla **poetry run invoke test**

## Testikattavuus

 Testikattavuus saadaan komennolla **poetry run invoke coverage-report**

## Pylint

 koodin pylint tarkistukset suoritetetaan komennolla **poetry run invoke lint**

## Dokumentit
[linkki sekvennsikaavioon](https://github.com/juhani-dev/ot-harjoitustyo2021/blob/master/dokumentaatio/sekvenssikaavio.png)
[linkki arkkitehtuuriin](https://github.com/juhani-dev/ot-harjoitustyo2021/blob/master/dokumentaatio/arkkitehtuuri.md)
[linkki työaikakirjanpitoon](https://github.com/juhani-dev/ot-harjoitustyo2021/blob/master/dokumentaatio/työaikakirjanpito.md)