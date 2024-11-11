"""Contains test for Varasto class
    """
import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    """Tester class for Varasto class

    Args:
        unittest : Inherits unittest.TestCase
    """
    def setUp(self):
        """Constructor for cases to be tested.
        """
        self.varasto = Varasto(10)
        self.varasto2 = Varasto(-1,-3)
        self.varasto3 = Varasto(10,12)

    def test_konstruktori_luo_tyhjan_varaston(self):
        """Tests if balance is empty.
        """
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        """Tests maximum capacity is 0.
        """
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        """Tests balance increase is added correctly.
        """
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        """Tests that capacity decreases as new content is added.
        """
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        """Taking out returns correct amount.
        """
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        """Tests taking out releases occupied space.
        """
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_konstruktori_luo_nolla_tilavuuden(self):
        """Tests constructor creates zero capacity,
        with negative capacity input.
        """
        self.assertAlmostEqual(self.varasto2.tilavuus, 0)

    def test_konstruktori_luo_nolla_saldon(self):
        """Tests balance is created as zero,
        with negative balance input in constructor.
        """
        self.assertAlmostEqual(self.varasto2.saldo, 0)

    def test_lisaa_varastoon_alle_nolla(self):
        """Tests negative value cannot be added to the balance.
        """
        self.varasto2.lisaa_varastoon(-3)
        self.assertAlmostEqual(self.varasto2.saldo,0)

    def test_lisaa_varastoon_yli_tilavuus(self):
        """Tests balance won't go above maximum capacity.
        """
        self.varasto.lisaa_varastoon(234)
        self.assertAlmostEqual(self.varasto.saldo,10)

    def test_ota_varastosta_alle_nolla(self):
        """Tests negative value cannot be taken out.
        """
        saatu = self.varasto.ota_varastosta(-3)
        self.assertAlmostEqual(saatu, 0)

    def test_ota_varastosta_yli_sallittu(self):
        """Tests cannot take more out than balance.
        """
        self.varasto.lisaa_varastoon(12)
        saatu = self.varasto.ota_varastosta(11)
        self.assertAlmostEqual(saatu, 10)

    def test_konstruktori_luo_tilavuuden_pohjalta_saldon(self):
        """Tests balance to be equal to max capacity,
        when constructor is given bigger value to balance than to
        capacity.
        """
        self.assertAlmostEqual(self.varasto3.saldo, 10)

    def test_tulostus(self):
        """Tests if string is printed out in the correct format.
        """
        representaatio = str(self.varasto)
        vaadittu = "saldo = 0, vielä tilaa 10"
        self.assertAlmostEqual(representaatio, vaadittu)
