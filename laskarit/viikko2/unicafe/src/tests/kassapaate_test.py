import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(100000)
        self.tyhjaKortti = Maksukortti(1)
    def test_konstruktori_asettaa_kassan_oikein(self):
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100000')

    def test_konstruktori_asettaa_edulliset_oikein(self):
        self.assertEqual(str(self.kassapaate.edulliset), '0')
        
    def test_konstruktori_asettaa_maukkaat_oikein(self):
        self.assertEqual(str(self.kassapaate.maukkaat), '0')

    def test_syo_edullisesti_kateisella_myytyjen_maara_kasvaa_palautus_oikein(self):
        maksuVert = self.kassapaate.syo_edullisesti_kateisella(240)
        
        self.assertEqual(maksuVert, 0 )
        self.assertEqual(str(self.kassapaate.edulliset), '1')

    def test_syo_maukkaasti_kateisella_myytyjen_maara_kasvaa_palautus_oikein(self):
        maksuVert =self.kassapaate.syo_maukkaasti_kateisella(410)

        self.assertEqual(maksuVert, 10)
        self.assertEqual(str(self.kassapaate.maukkaat), '1')

    
    def test_syo_kassa_kateisella_kasvaa_oikealla_summalla(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100640')
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100640')    

    def test_maksu_ei_riittava_edullisesti_saldo_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100000')

    def test_maksu_ei_riittava_maukkaasti_saldo_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100000')
    
    def test_maksu_ei_riittava_edullisesti_palautus_oikein(self):
        maksuVert =self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(maksuVert, 200)

    def test_maksu_ei_riittava_maukkaasti_palautus_oikein(self):
        maksuVert =self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(maksuVert, 200)
    
    def test_maksu_ei_riittava_maukkaasti_myydyt_maara_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        
        self.assertEqual(str(self.kassapaate.maukkaat), '0')

    def test_maksu_ei_riittava_edullisesti_myydyt_maara_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        
        self.assertEqual(str(self.kassapaate.edulliset), '0')
    
    def test_lataa_rahaa_kortille(self):
        
        self.kortti.lataa_rahaa(100)
        self.assertEqual(str(self.kortti), 'Saldo: 1001.0')

    def test_lataa_rahaa_siirtyy_kassaan(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti,100)
        
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100100')

    def test_kassa_ei_kasva_kortti_ostolla(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100000')
    
    def test_korttiosto_toimii_jos_rahaa_tarpeeksi_edullisesti(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), 'Saldo: 997.6')

    def test_korttiosto_toimii_jos_rahaa_tarpeeksi_maukkaasti(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), 'Saldo: 996.0')

    def test_korttiosto_palauttaa_true_jos_rahaa_tarpeeksi_edullisesti(self):
        vertailu = self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(vertailu, True)

    def test_korttiosto_palauttaa_true_jos_rahaa_tarpeeksi_maukkaasti(self):
        vertailu = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(vertailu, True)

    def test_jos_kortilla_tarpeeksi_rahaa_myydyt_kasvavat_maukkaasti(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_jos_kortilla_tarpeeksi_rahaa_myydyt_kasvavat_edullisesti(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_korttiosto_saldo_ei_muutu_jos_rahaa_EI_tarpeeksi_edullisesti(self):
        self.kassapaate.syo_edullisesti_kortilla(self.tyhjaKortti)
        self.assertEqual(str(self.tyhjaKortti), 'Saldo: 0.01')

    def test_korttiosto_saldo_ei_muutu_jos_rahaa_EI_tarpeeksi_maukkaasti(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.tyhjaKortti)
        self.assertEqual(str(self.tyhjaKortti), 'Saldo: 0.01')

    def test_jos_kortilla_ei_tarpeeksi_rahaa_myydyt_ei_kasvava_maukkaasti(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.tyhjaKortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_jos_kortilla_ei_tarpeeksi_rahaa_myydyt_ei_kasvava_edullisesti(self):
        self.kassapaate.syo_edullisesti_kortilla(self.tyhjaKortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_korttiosto_palauttaa_false_jos_rahaa_ei_tarpeeksi_edullisesti(self):
        vertailu = self.kassapaate.syo_edullisesti_kortilla(self.tyhjaKortti)
        self.assertEqual(vertailu, False)

    def test_korttiosto_palauttaa_false_jos_rahaa_ei_tarpeeksi_maukkaasti(self):
        vertailu = self.kassapaate.syo_maukkaasti_kortilla(self.tyhjaKortti)
        self.assertEqual(vertailu, False)