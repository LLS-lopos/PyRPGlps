from icecream import ic
#ic.disable()

def boucle_de_jeu():
    ic("Bonjours le monde")
    while True:
        choix = input("touche ?:\n>>> ")
        if choix == "1":
            ic("encore")
        else: break

if __name__ == "__main__":
    boucle_de_jeu()
    
