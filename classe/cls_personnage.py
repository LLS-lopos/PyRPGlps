from icecream import ic

class Personnage:
    def __init__(self, NOM, PV, ATT):
        self.nom = NOM
        self.pv = PV
        self.att = ATT

    def attaquer(self, cible):
        cible.pv -= self.att
        ic(cible.pv)

    def mort(self):
        if self.pv <= 0:
            self.pv = 0
            ic(self.nom + " est mort au combat")

if __name__ == "__main__":
    Dai = Personnage("Daï", 5, 12)
    Dai.mort()