def arrondire(entier, facteur):
    calcul = entier * facteur
    text_calcul = str(calcul)
    text_entier = text_calcul.split(".")[0]
    text_reste = text_calcul.split(".")[1]
    resultat = int(text_entier)
    if text_reste.isdigit:
        if int(text_reste[0]) >= 5:
            resultat += 1
            
    return resultat

if __name__ == "__main__":
    arrondire(7, 0.2)
    arrondire(7, 0.4)