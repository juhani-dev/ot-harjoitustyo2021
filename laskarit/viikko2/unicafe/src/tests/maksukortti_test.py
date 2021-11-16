import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)
        
    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "Saldo: 0.1")

    def test_lataa_rahaa_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "Saldo: 0.2")

    def test_ota_rahaa_vahentaa_oikein(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "Saldo: 0.05")
    
    def test_ota_rahaa_ei_mene_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(11)
        self.assertEqual(str(self.maksukortti), "Saldo: 0.1")
    
    def test_ota_rahaa_palauttaa_true_jos_rahaa_riittaa(self):
        vertailu =self.maksukortti.ota_rahaa(1)
        self.assertEqual(vertailu, True)

    def test_ota_rahaa_palauttaa_False_jos_rahaa_ei_riittaa(self):
        vertailu =self.maksukortti.ota_rahaa(100)
        self.assertEqual(vertailu, False)
        