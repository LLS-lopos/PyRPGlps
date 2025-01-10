from random import randint
import json
import pathlib
import os
import sys

# Ajouter le dossier parent au sys.path
dossier_parent = pathlib.Path(__file__).resolve().parent.parent
sys.path.append(str(dossier_parent))

from module.fonc_math import arrondire
from module.fonc_sauve_charger import charger, enregistrer

registre = pathlib.Path(dossier_parent/"donner/")
json_player = os.path.join(registre, 'player.json')


class Personnage:
    def __init__(self, NOM, PV, ATT, DEF, VIT):
        self.stats = {
            "nom": NOM,
            "pv": PV,
            "att": ATT,
            "def": DEF,
            "vit": VIT,
            "exp": 0,
            "exp_max": 100,
            "att_critique": 0.2,
        }

    def attaquer(self, cible):
        att_init = self.stats["att"]
        self.att_critique()
        old = cible.stats["pv"]
        attaque = self.stats["att"] - cible.stats["def"]
        if attaque > 0:
            cible.stats["pv"] -= attaque
            print(f"{self.stats["nom"]} attaque {cible.stats["nom"]} et lui inflige {old - cible.stats["pv"]} points de dégâts")
            if self.stats["att"] != att_init: print(f"{self.stats["nom"]} porter un coup critique à {cible.stats["nom"]}")
        else: print("l'attaque est sans effet")
        if cible.stats["pv"] <= 0: cible.mort()
        else: print(f"{cible.stats["nom"]} a {cible.stats["pv"]} points de vie")
        self.stats["att"] = att_init
    
    def niveau_sup(self):
        for cle in self.stats:
            if cle == "nom":
                print(f"{self.stats.get(cle)}")
            else:
                old = self.stats.get(cle)
                self.stats[cle] += randint(0, 5)
                print(f"{cle.capitalize()}: {old} -> {self.stats[cle]} (+{self.stats[cle] - old})")

    def mort(self):
        if self.stats["pv"] <= 0:
            self.stats["pv"] = 0
            print(self.stats["nom"] + " n'a plus de points de vie et est mort au combat")
    
    def __str__(self):
        for cle in self.stats:
            print(f"{cle}: {self.stats[cle]}")

    def att_critique(self):
        a, b, c, d = randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1)
        if a == b == c == d:
            self.stats["att"] = self.stats["att"] + arrondire(self.stats["att"], self.stats["att_critique"])
            return self.stats["att"]

    def sauvegarder_donner(self):
        enregistrer(json_player, self.stats)
    def chager_donner(self):
        self.stats = charger(json_player)

class Guerrier(Personnage):
    def __init__(self, NOM="", PV=20, ATT=7, DEF=8, VIT=3):
        Personnage.__init__(self, NOM, PV, ATT, DEF, VIT)
        self.stats = {
            "nom": NOM,
            "pv": PV,
            "att": ATT,
            "def": DEF,
            "vit": VIT,
            "exp": 0,
            "exp_max": 100,
            "att_critique": 1.2,
        }
    
    def niveau_sup(self):
        for cle in self.stats:
            if cle == "nom":
                print(f"{self.stats.get(cle)}")
            elif cle == "pv":
                old = self.stats.get(cle)
                self.stats[cle] += randint(0, 5)
                print(f"{cle.capitalize()}: {old} -> {self.stats[cle]} (+{self.stats[cle] - old})")
            else:
                old = self.stats.get(cle)
                self.stats[cle] += randint(2, 3)
                print(f"{cle.capitalize()}: {old} -> {self.stats[cle]} (+{self.stats[cle] - old})")
            

if __name__ == "__main__":
    Joueur = Personnage("Player", 20, 3, 2, 4)
    Joueur.__str__()
    Joueur.sauvegarder_donner()