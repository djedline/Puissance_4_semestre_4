def get_gauche(self,plateau, ligne, colonne) :
    l = ligne
    c = colonne
    resultat = ["", 0]
    for i in range (3) :
        l -= 1
        if (l != 0) :
            resultat[0] = false
            break
