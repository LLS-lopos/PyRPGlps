from icecream import ic

class Equipe:
    def __init__(self, NOM, MEMBRE):
        self.nom = NOM
        self.membre = MEMBRE

    def composition(self):
        for membre in self.membre:
            ic(membre)

if __name__ == "__main__":
    hero = Equipe("alliance grg", ["toto", "polo", "pierre", "jacque"])
    hero.composition()