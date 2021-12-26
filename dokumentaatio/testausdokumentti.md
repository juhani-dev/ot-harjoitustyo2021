# Testausdokumentti

Ohjelman sovelluslogiikkaa on testattu unittestilla ja käyttöliittymän toimintaa on testattu manuaalisesti.

## Services luokat

Ohjelman sovelluslogiikasta vastaa **services** kansion tiedostoissa olevat luokat. Näitä luokkia testataan   [blackjack_test tiedoston luokissa](https://github.com/juhani-dev/ot-harjoitustyo2021/blob/master/blackjack_game/src/tests/blackjack_test.py)   

1. *TestCards52* luokka testaa, että *Deck* luokan luoma kortti pakka on oikean kokoinen, sisältää oikean määrän eri maita ja että jokainen uusi luotu pakka on eri järjestysessä

2. *TestCheck* testaa, että *Checks* luokka laskee pelaajan ja jakajan korttien arvot oikein

3. *TestCheckWinner* testaa, että *CheckWinner* luokka palauttaa oikean voittajan

4. *TestWinCount* testaa , että *Score* luokka palauttaa oikean määrän voittoja

5. *TestDealCards* testaa, että *Deal* luokka jakaa oikean määrän kortteja pelaajalle tai jakajalle


## Testauskattavuus

![kuva](https://github.com/juhani-dev/ot-harjoitustyo2021/blob/master/dokumentaatio/kuvat/tes.png)

Ohjelman sovelluslogiikan testauskattavuus 95 %

## Käyttöliittymän ja  ohjelman toiminnan manuaalinen testaus

Ohjelman asentamisen toiminta annettujen ohjeiden mukaan on testattu virtuaali ympäristössä manuaalisesti.  Testaus on tehty linux-ympäristössä.  
Peliä on testattu manuaalisesti painamalla nappuloita epäloogisessa järjestyksessä.  Koettaen näin saada esimerkiksi voittolaskuria näyttämään väärän tuloksen tai saada peliä jakamaan kortteja väärässä kohdassa. 

## Sovelluksen ongelmat

Ohjelmaan ei ole tehty erillistä lopetus mahdollisuutta.