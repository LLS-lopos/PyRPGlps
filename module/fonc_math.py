def arrondire(entier, facteur):
    calcul = entier * facteur
    resultat = int(str(calcul).split(".")[0])
    if str(calcul).split(".")[1].isdigit:
        if int(str(calcul).split(".")[1]) >= 5: resultat += 1
    return resultat

if __name__ == "__main__":
    print(arrondire(7, 0.2))
    print(arrondire(7, 0.4))