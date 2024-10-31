import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto2 = Varasto(-1,-3)
        self.varasto3 = Varasto(10,12)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_konstruktori_luo_nolla_tilavuuden(self):
        self.assertAlmostEqual(self.varasto2.tilavuus, 0)

    def test_konstruktori_luo_nolla_saldon(self):
        self.assertAlmostEqual(self.varasto2.saldo, 0)

    def test_lisaa_varastoon_alle_nolla(self):
        self.varasto2.lisaa_varastoon(-3)
        self.assertAlmostEqual(self.varasto2.saldo,0)

    def test_lisaa_varastoon_yli_tilavuus(self):
        self.varasto.lisaa_varastoon(234)
        self.assertAlmostEqual(self.varasto.saldo,10)

    def test_ota_varastosta_alle_nolla(self):
        saatu = self.varasto.ota_varastosta(-3)
        self.assertAlmostEqual(saatu, 0)

    def test_ota_varastosta_yli_sallittu(self):
        self.varasto.lisaa_varastoon(12)
        saatu = self.varasto.ota_varastosta(11)
        self.assertAlmostEqual(saatu, 0)

    def test_konstruktori_luo_tilavuuden_pohjalta_saldon(self):
        self.assertAlmostEqual(self.varasto3.saldo, 10)

    def test_tulostus(self):
        representaatio = str(self.varasto)
        vaadittu = f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}"
        self.assertAlmostEqual(representaatio, vaadittu)
