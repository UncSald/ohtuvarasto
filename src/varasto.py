"""Module contains the Varasto class
    """
class Varasto:
    """Class contains information about a container.
    Container balance can be added and taken out.
    """
    def __init__(self, tilavuus, alku_saldo = 0):
        """Class constructor for Varasto.
        Varasto contains information about maximum space,
        and currently occupied space.

        Args:
            tilavuus (int): Maximum capacity of the Varasto.
            alku_saldo (int, optional): Occupied space. Defaults to 0.
        """
        if tilavuus > 0.0:
            self.tilavuus = tilavuus
        else:
            # virheellinen, nollataan
            self.tilavuus = 0.0

        if alku_saldo < 0.0:
            # virheellinen, nollataan
            self.saldo = 0.0
        elif alku_saldo <= tilavuus:
            # mahtuu
            self.saldo = alku_saldo
        else:
            # täyteen ja ylimäärä hukkaan!
            self.saldo = tilavuus

    # huom: ominaisuus voidaan myös laskea.
    # Ei tarvita erillistä kenttää viela_tilaa tms.
    def paljonko_mahtuu(self):
        """Returns how much capacity there is left.

        Returns:
            int: Amount of unused capacity.
        """
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        """Adds given amount o balance. Balance
        will not exceed maximum capacity

        Args:
            maara (int): Amount added to balance.
        """
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        """Takes out given amount from the balance.
        Releases more capacity.

        Args:
            maara (int): Amount to be taken out.

        Returns:
            int: return the amount taken out.
            If amount wanted exeeds balance return the balance
            available.
        """
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        """String representation of the balance and the remaining space.

        Returns:
            str: string representation of the balance and remaining space.
        """
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
