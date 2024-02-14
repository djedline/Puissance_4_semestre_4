from Plateau import plateau

class nombrePossibilites():

    nb_puissance_4_colonne = [3, 4, 5, 7, 5, 4, 3]
    nb_puissance_4_ligne = [0, 1, 2, 2, 1, 0]

    def __init__(self, ligne, colonne) :
        self.nb_puissance_4_case = nb_puissance_4_ligne[ligne] + nb_puissance_4_colonne[colonne]


def checkDroite(ligne, colonne, joueur):
    nb_puissance_4_case = nb_puissance_4_ligne[ligne] + nb_puissance_4_colonne[colonne]
    if joueur == "croix": 
        for i in range(0, 3):
            if (colonne + i != 7):
                if get_case(ligne, colonne) != "O":
                    nb_puissance_4_case -= 1
                    return nb_puissance_4_case
        return nb_puissance_4_case
    else:
        for i in range(0, 3):
            if (colonne + i != 7):
                if get_case(ligne, colonne) != "X":
                    nb_puissance_4_case -= 1
                    return nb_puissance_4_case
        return nb_puissance_4_case

def checkGauche(ligne, colonne, joueur):
    nb_puissance_4_case = nb_puissance_4_ligne[ligne] + nb_puissance_4_colonne[colonne]
    if joueur == "croix": 
        for i in range(0, 3):
            if (colonne - i != -1):
                if get_case(ligne, colonne) != "O":
                    nb_puissance_4_case -= 1
                    return nb_puissance_4_case
        return nb_puissance_4_case
    else:
        for i in range(0, 3):
            if (colonne - i != -1):
                if get_case(ligne, colonne) != "X":
                    nb_puissance_4_case -= 1
                    return nb_puissance_4_case
        return nb_puissance_4_case
    
def checkBas(ligne, colonne, joueur):
    nb_puissance_4_case = nb_puissance_4_ligne[ligne] + nb_puissance_4_colonne[colonne]
    if joueur == "croix": 
        for i in range(0, 3):
            if (ligne - i != -1):
                if get_case(ligne, colonne) != "O":
                    nb_puissance_4_case -= 1
                    return nb_puissance_4_case
        return nb_puissance_4_case
    else:
        for i in range(0, 3):
            if (colonne - i != -1):
                if get_case(ligne, colonne) != "X":
                    nb_puissance_4_case -= 1
                    return nb_puissance_4_case
        return nb_puissance_4_case
    
def checkDiagBasGauche(ligne, colonne, joueur):
    nb_puissance_4_case = nb_puissance_4_ligne[ligne] + nb_puissance_4_colonne[colonne]
    if joueur == "croix": 
        for i in range(0, 3):
            if (ligne - i != -1):
                if get_case(ligne, colonne) != "O":
                    nb_puissance_4_case -= 1
                    return nb_puissance_4_case
        return nb_puissance_4_case
    else:
        for i in range(0, 3):
            if (colonne - i != -1):
                if get_case(ligne, colonne) != "X":
                    nb_puissance_4_case -= 1
                    return nb_puissance_4_case
        return nb_puissance_4_case