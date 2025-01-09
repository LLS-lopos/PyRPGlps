from icecream import ic
from random import randint

class Personnage:
    def __init__(self, NOM, PV, ATT):
        self.nom = NOM
        self.pv = PV
        self.att = ATT
        self.statistique = {
            "pv": PV,
            "att": ATT,
        }

    def attaquer(self, cible):
        cible.pv -= self.att
        ic(cible.nom, cible.pv)
        if cible.pv <= 0:
            cible.mort()
    
    def niveau_sup(self):
        for cle in self.statistique:
            ic(cle, self.statistique[cle])
            old = self.statistique.get(cle)
            self.statistique[cle] += randint(0, 5)
            diff = self.statistique[cle] - old
            ic(cle, self.statistique[cle])
            ic(diff)

    def mort(self):
        if self.pv <= 0:
            self.pv = 0
            ic(self.nom + " est mort au combat")

if __name__ == "__main__":
    Dai = Personnage("Daï", 12, 5)
    Croco = Personnage("Dino", 10, 2)
    Dai.attaquer(Croco)
    Croco.attaquer(Dai)
    Croco.attaquer(Dai)
    Croco.attaquer(Dai)
    Dai.attaquer(Croco)