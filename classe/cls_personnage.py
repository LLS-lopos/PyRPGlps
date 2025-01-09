from icecream import ic
from random import randint

class Personnage:
    def __init__(self, NOM, PV, ATT):
        self.stats = {
            "nom": NOM,
            "pv": PV,
            "att": ATT,
        }

    def attaquer(self, cible):
        cible.stats["pv"] -= self.stats["att"]
        ic(cible.stats["nom"], cible.stats["pv"])
        if cible.stats["pv"] <= 0:
            cible.mort()
    
    def niveau_sup(self):
        for cle in self.stats:
            ic(cle, self.stats[cle])
            old = self.stats.get(cle)
            self.stats[cle] += randint(0, 5)
            diff = self.stats[cle] - old
            ic(cle, self.stats[cle])
            ic(diff)

    def mort(self):
        if self.stats["pv"] <= 0:
            self.stats["pv"] = 0
            ic(self.stats["nom"] + " est mort au combat")
    
    def __str__(self):
        for cle in self.stats:
            print(f"{cle}: {self.stats[cle]}")

if __name__ == "__main__":
    Dai = Personnage("Daï", 12, 5)
    Croco = Personnage("Dino", 10, 2)
    Dai.__str__()
    Croco.__str__()
    Dai.attaquer(Croco)
    Croco.attaquer(Dai)
    Croco.attaquer(Dai)
    Croco.attaquer(Dai)
    Dai.attaquer(Croco)
    Dai.__str__()
    Croco.__str__()