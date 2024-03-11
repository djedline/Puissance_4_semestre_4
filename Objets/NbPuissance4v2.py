from Plateau import *
from Noeud import *
from Arbre import *
import copy

def comptagePuissance4(joueur, plateau):
    tableauPoint = [[3,4,5,7,5,4,3],[4,6,7,10,7,6,4],[5,8,9,13,9,8,5],[5,8,9,13,9,8,5],[4,6,7,10,7,6,4],[3,4,5,7,5,4,3]]
    possibilite = plateau.get_possibilite()
    c0 = copy.deepcopy(plateau)
    c1 = copy.deepcopy(plateau)
    c2 = copy.deepcopy(plateau)
    c3 = copy.deepcopy(plateau)
    c4 = copy.deepcopy(plateau)
    c5 = copy.deepcopy(plateau)
    c6 = copy.deepcopy(plateau)
    plateauC0 = ["plateau si pion colonne 0","score case"]
    plateauC1 = ["plateau si pion colonne 1","score case"]
    plateauC2 = ["plateau si pion colonne 2","score case"]
    plateauC3 = ["plateau si pion colonne 3","score case"]
    plateauC4 = ["plateau si pion colonne 4","score case"]
    plateauC5 = ["plateau si pion colonne 5","score case"]
    plateauC6 = ["plateau si pion colonne 6","score case"]
    
    plateauC0 = [c0,comptagePointCase(0,c0, joueur)] if (possibilite[0] == True) else [None,0]
    plateauC1 = [c1,comptagePointCase(1,c1, joueur)] if (possibilite[1] == True) else [None,0]
    plateauC2 = [c2,comptagePointCase(2,c2, joueur)] if (possibilite[2] == True) else [None,0]
    plateauC3 = [c3,comptagePointCase(3,c3, joueur)] if (possibilite[3] == True) else [None,0]
    plateauC4 = [c4,comptagePointCase(4,c4, joueur)] if (possibilite[4] == True) else [None,0]
    plateauC5 = [c5,comptagePointCase(5,c5, joueur)] if (possibilite[5] == True) else [None,0]
    plateauC6 = [c6,comptagePointCase(6,c6, joueur)] if (possibilite[6] == True) else [None,0]

    #pion = plateau.ajouter_pion(0, joueur)
    return [plateauC0, plateauC1, plateauC2, plateauC3, plateauC4, plateauC5, plateauC6]
    
def comptagePointCase(colonne, plateau, joueur) :
    pion = plateau.ajouter_pion(colonne,joueur)
    if (plateau.puissance_4(pion) == False) : 
        h = plateau.check_direction_voisin(pion, 0, 1) + plateau.check_direction_voisin(pion, 0, -1)
        b = plateau.check_direction_voisin(pion, 1, 0)
        vh = plateau.check_direction_voisin(pion, 1, 1)  + plateau.check_direction_voisin(pion, 1, -1)
        vb = plateau.check_direction_voisin(pion, -1, 1) + plateau.check_direction_voisin(pion, -1, -1)
        nb4h = h - 2 if h > 2 else 0
        nb4b = 1 if (plateau.get_case(colonne, 4) != None and (str(plateau.get_case(colonne, 3)) == joueur or plateau.get_case(colonne, 3) == None)) else 0
        nb4vh = vh - 2 if vh > 2 else 0
        nb4vb = vb - 2 if vb > 2 else 0
        nbpuissance4 = nb4h + nb4b + nb4vh + nb4vb
        nbpionpuissance4 = max(nb4b, b, nb4vh, nb4vb)
        pointTotal = nbpionpuissance4 * nbpuissance4
    else :
        pointTotal = 100
    return pointTotal*-1 if joueur == "O" else pointTotal # calculer

def attributionNoeud(tableauResult) :
    noeud0 = Noeud(tableauResult[0][0], tableauResult[0][1])
    noeud1 = Noeud(tableauResult[1][0], tableauResult[1][1])
    noeud2 = Noeud(tableauResult[2][0], tableauResult[2][1])
    noeud3 = Noeud(tableauResult[3][0], tableauResult[3][1])
    noeud4 = Noeud(tableauResult[4][0], tableauResult[4][1])
    noeud5 = Noeud(tableauResult[5][0], tableauResult[5][1])
    noeud6 = Noeud(tableauResult[6][0], tableauResult[6][1])

def creerArbre(profondeur, plateau) :
    arbre = Arbre(plateau)
    for p in range (profondeur) :
        print ("coucou")
    print(arbre.getRacine())

plateauTest = Plateau()
creerArbre(3,plateauTest)

#Test noeud
#print(plateauTest.get_donnees())
#plateauTest.ajouter_pion(0,"O")
#plateauTest.ajouter_pion(0,"X")
#plateauTest.ajouter_pion(0,"X")
#plateauTest.ajouter_pion(0,"X")
#print(str(comptagePuissance4("X", plateauTest)))
#attributionNoeud(comptagePuissance4("O", plateauTest))