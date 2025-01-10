import json

def enregistrer(fichier_donner, donner):
    """enregitrer les données au format json

    Args:
        fichier_donner (_type_): fichier ou chemin de fichier
        donner (_type_): tous type de donné compatible
    """
    with open(fichier_donner, 'w', encoding='utf-8') as f:
        json.dump(donner, f,ensure_ascii=False, indent=4)

def charger(fichier_donner):
    """(re)charger les données dans le programme

    Args:
        fichier_donner (_type_):fichier ou chemin de fichier
        donner (_type_): tous type de donné compatible
    """
    with open(fichier_donner, 'r', encoding='utf-8') as f:
        donner = json.load(f)
    return donner