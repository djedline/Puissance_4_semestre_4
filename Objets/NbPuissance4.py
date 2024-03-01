from Plateau import *

def checkAll(ligne, colonne, joueur, plateau):
    nb_puissance_4_colonne = [3, 4, 5, 7, 5, 4, 3]
    nb_puissance_4_ligne = [0, 1, 2, 2, 1, 0]
    nb_puissance_4_case = nb_puissance_4_ligne[ligne] + nb_puissance_4_colonne[colonne]
    print (nb_puissance_4_case)
    nb_puissance_4_case = checkDroite(nb_puissance_4_case, ligne,colonne,joueur, plateau)
    print (nb_puissance_4_case)
    nb_puissance_4_case = checkGauche(nb_puissance_4_case, ligne,colonne,joueur, plateau)
    print (nb_puissance_4_case)
    nb_puissance_4_case = checkBas(nb_puissance_4_case, ligne,colonne,joueur, plateau)
    print (nb_puissance_4_case)
    nb_puissance_4_case = checkDiagBasGauche(nb_puissance_4_case, ligne,colonne,joueur, plateau)
    print (nb_puissance_4_case)
    nb_puissance_4_case = checkDiagBasDroite(nb_puissance_4_case, ligne,colonne,joueur, plateau)
    print (nb_puissance_4_case)
    nb_puissance_4_case = checkDiagHautGauche(nb_puissance_4_case, ligne,colonne,joueur, plateau)
    print (nb_puissance_4_case)
    nb_puissance_4_case = checkDiagHautDroite(nb_puissance_4_case, ligne,colonne,joueur, plateau)
    print (nb_puissance_4_case)
    return nb_puissance_4_case
    
def checkDroite(nb_puissance_4_case, ligne, colonne, joueur, plateau):
    #S'il s'agit du joueur jouant avec les croix
    if joueur == "croix":
        #Répéter 3 fois pour chercher les blocages (3 car 1 + 3 = 4) 
        for i in range(0, 3):
            #Vérifie qu'on ne sorte pas de la grille
            if (colonne + i < 7):
                #Vérifie si la case est occupée
                print(Plateau.get_case(plateau, ligne, colonne + i))
                if Plateau.get_case(plateau, ligne, colonne + i) == "O":
                    #Nombre de possibilité -1 car case bloquée
                    nb_puissance_4_case -= 1
                    return nb_puissance_4_case
        return nb_puissance_4_case
    #Sinon il s'agit du joueur jouant avec les ronds
    else:
        #Répéter 3 fois pour chercher les blocages (3 car 1 + 3 = 4) 
        for i in range(0, 3):
            #Vérifie qu'on ne sorte pas de la grille
            if (colonne + i < 7):
                #Vérifie si la case est occupée
                if Plateau.get_case(plateau, ligne, colonne + i) == "X":
                    #Nombre de possibilité -1 car case bloquée
                    nb_puissance_4_case -= 1
                    return nb_puissance_4_case
        return nb_puissance_4_case
def checkGauche(nb_puissance_4_case, ligne, colonne, joueur, plateau):
    #S'il s'agit du joueur jouant avec les croix
    if joueur == "croix": 
        #Répéter 3 fois pour chercher les blocages (3 car 1 + 3 = 4) 
        for i in range(0, 3):
            #Vérifie qu'on ne sorte pas de la grille
            if (colonne - i > -1):
                #Vérifie si la case est occupée
                if Plateau.get_case(plateau, ligne, colonne - i) == "O":
                    #Nombre de possibilité -1 car case bloquée
                    nb_puissance_4_case -= 1
                    return nb_puissance_4_case
        return nb_puissance_4_case
    #Sinon il s'agit du joueur jouant avec les ronds
    else:
        #Répéter 3 fois pour chercher les blocages (3 car 1 + 3 = 4) 
        for i in range(0, 3):
            #Vérifie qu'on ne sorte pas de la grille
            if (colonne - i > -1):
                #Vérifie si la case est occupée
                if Plateau.get_case(plateau, ligne, colonne - i) == "X":
                    #Nombre de possibilité -1 car case bloquée
                    nb_puissance_4_case -= 1
                    return nb_puissance_4_case
        return nb_puissance_4_case
def checkBas(nb_puissance_4_case, ligne, colonne, joueur, plateau):
    #S'il s'agit du joueur jouant avec les croix
    if joueur == "croix": 
        #Répéter 3 fois pour chercher les blocages (3 car 1 + 3 = 4) 
        for i in range(0, 3):
            #Vérifie qu'on ne sorte pas de la grille
            if (ligne - i > -1):
                #Vérifie si la case est occupée
                if Plateau.get_case(plateau, ligne - i, colonne) == "O":
                    #Nombre de possibilité -1 car case bloquée
                    nb_puissance_4_case -= 1
                    return nb_puissance_4_case
        return nb_puissance_4_case
    #Sinon il s'agit du joueur jouant avec les ronds
    else:
        #Répéter 3 fois pour chercher les blocages (3 car 1 + 3 = 4) 
        for i in range(0, 3):
            #Vérifie qu'on ne sorte pas de la grille
            if (ligne - i > -1):
                #Vérifie si la case est occupée
                if Plateau.get_case(plateau, ligne - i, colonne) == "X":
                    #Nombre de possibilité -1 car case bloquée
                    nb_puissance_4_case -= 1
                    return nb_puissance_4_case
        return nb_puissance_4_case
def checkDiagBasGauche(nb_puissance_4_case, ligne, colonne, joueur, plateau):
    #S'il s'agit du joueur jouant avec les croix
    if joueur == "croix": 
        #Répéter 3 fois pour chercher les blocages (3 car 1 + 3 = 4) 
        for i in range(0, 3):
            #Vérifie qu'on ne sorte pas de la grille
            if (ligne - i > -1 and colonne - i > -1):
                #Vérifie si la case est occupée
                if Plateau.get_case(plateau, ligne - i, colonne - i) == "O":
                    #Nombre de possibilité -1 car case bloquée
                    nb_puissance_4_case -= 1
                    return nb_puissance_4_case
        return nb_puissance_4_case
    #Sinon il s'agit du joueur jouant avec les ronds
    else:
        #Répéter 3 fois pour chercher les blocages (3 car 1 + 3 = 4) 
        for i in range(0, 3):
            #Vérifie qu'on ne sorte pas de la grille
            if (ligne - i > -1 and colonne - i > -1):
                #Vérifie si la case est occupée
                if Plateau.get_case(plateau, ligne - i, colonne - i) == "X":
                    #Nombre de possibilité -1 car case bloquée
                    nb_puissance_4_case -= 1
                    return nb_puissance_4_case
        return nb_puissance_4_case

def checkDiagBasDroite(nb_puissance_4_case, ligne, colonne, joueur, plateau):
    #S'il s'agit du joueur jouant avec les croix
    if joueur == "croix": 
        #Répéter 3 fois pour chercher les blocages (3 car 1 + 3 = 4) 
        for i in range(0, 3):
            #Vérifie qu'on ne sorte pas de la grille
            if (ligne - i > -1 and colonne + i < 7):
                #Vérifie si la case est occupée
                if Plateau.get_case(plateau, ligne - i, colonne + i) == "O":
                    #Nombre de possibilité -1 car case bloquée
                    nb_puissance_4_case -= 1
                    return nb_puissance_4_case
        return nb_puissance_4_case
    #Sinon il s'agit du joueur jouant avec les ronds
    else:
        #Répéter 3 fois pour chercher les blocages (3 car 1 + 3 = 4) 
        for i in range(0, 3):
            #Vérifie qu'on ne sorte pas de la grille
            if (ligne - i > -1 and colonne + i < 7):
                #Vérifie si la case est occupée
                if Plateau.get_case(plateau, ligne - i, colonne + i) == "X":
                    #Nombre de possibilité -1 car case bloquée
                    nb_puissance_4_case -= 1
                    return nb_puissance_4_case
        return nb_puissance_4_case

def checkDiagHautGauche(nb_puissance_4_case, ligne, colonne, joueur, plateau):
    #S'il s'agit du joueur jouant avec les croix
    if joueur == "croix":
        #Répéter 3 fois pour chercher les blocages (3 car 1 + 3 = 4)  
        for i in range(0, 3):
            #Vérifie qu'on ne sorte pas de la grille
            if (ligne + i < 6 and colonne - i > -1):
                #Vérifie si la case est occupée
                if Plateau.get_case(plateau, ligne + i, colonne - i) == "O":
                    #Nombre de possibilité -1 car case bloquée
                    nb_puissance_4_case -= 1
                    return nb_puissance_4_case
        return nb_puissance_4_case
    #Sinon il s'agit du joueur jouant avec les ronds
    else:
        #Répéter 3 fois pour chercher les blocages (3 car 1 + 3 = 4) 
        for i in range(0, 3):
            #Vérifie qu'on ne sorte pas de la grille
            if (ligne + i < 6 and colonne - i > -1):
                #Vérifie si la case est occupée
                if Plateau.get_case(plateau, ligne + i, colonne - i) == "X":
                    #Nombre de possibilité -1 car case bloquée
                    nb_puissance_4_case -= 1
                    return nb_puissance_4_case
        return nb_puissance_4_case

def checkDiagHautDroite(nb_puissance_4_case, ligne, colonne, joueur, plateau):
    #S'il s'agit du joueur jouant avec les croix
    if joueur == "croix": 
        #Répéter 3 fois pour chercher les blocages (3 car 1 + 3 = 4) 
        for i in range(0, 3):
            #Vérifie qu'on ne sorte pas de la grille
            if (ligne + i < 6 and colonne - i < 7):
                #Vérifie si la case est occupée
                if Plateau.get_case(plateau, ligne + i, colonne + i) == "O":
                    #Nombre de possibilité -1 car case bloquée
                    nb_puissance_4_case -= 1
                    return nb_puissance_4_case
        return nb_puissance_4_case
    #Sinon il s'agit du joueur jouant avec les ronds
    else:
        #Répéter 3 fois pour chercher les blocages (3 car 1 + 3 = 4) 
        for i in range(0, 3):
            #Vérifie qu'on ne sorte pas de la grille
            if (ligne + i < 6 and colonne - i < 7):
                #Vérifie si la case est occupée
                if Plateau.get_case(plateau, ligne + i, colonne + i) == "X":
                    #Nombre de possibilité -1 car case bloquée
                    nb_puissance_4_case -= 1
                    return nb_puissance_4_case
        return nb_puissance_4_case
<<<<<<< HEAD
=======
    
plateauTest = Plateau()
print(plateauTest.get_donnees())
print(plateauTest.get_plein())
plateauTest.ajouter_pion_symbole(4,"X")
print(plateauTest.get_donnees())
plateauTest.ajouter_pion_symbole(3,"O")
plateauTest.ajouter_pion_symbole(3,"X")
plateauTest.ajouter_pion_symbole(4,"O")
print(plateauTest.get_donnees())
print("Le nombre de possibilite pour le coup en 0,2 est ", checkAll(0,2,"croix",plateauTest))
>>>>>>> dbf72fd4d8978378d93fff5f4893d05aa92b85c2
