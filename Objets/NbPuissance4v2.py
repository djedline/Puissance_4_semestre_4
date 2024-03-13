from Plateau import Plateau
from Arbre import Arbre
from Noeud import Noeud
import copy

def comptagePuissance4(joueur, plateau):
    tableauPoint = [[3,4,5,7,5,4,3],[4,6,7,10,7,6,4],[5,8,9,13,9,8,5],[5,8,9,13,9,8,5],[4,6,7,10,7,6,4],[3,4,5,7,5,4,3]]
    possibilite = plateau.get_possibilite()
    c0 = comptagePointCase(0,plateau, joueur) if (possibilite[0] == True) else None
    c1 = comptagePointCase(1,plateau, joueur) if (possibilite[1] == True) else None
    c2 = comptagePointCase(2,plateau, joueur) if (possibilite[2] == True) else None
    c3 = comptagePointCase(3,plateau, joueur) if (possibilite[3] == True) else None
    c4 = comptagePointCase(4,plateau, joueur) if (possibilite[4] == True) else None
    c5 = comptagePointCase(5,plateau, joueur) if (possibilite[5] == True) else None
    c6 = comptagePointCase(6,plateau, joueur) if (possibilite[6] == True) else None
    return [c0,c1,c2,c3,c4,c5,c6]
    
def comptagePointCase(colonne, plateau, joueur) :
    plateauUtil = copy.deepcopy(plateau)
    pion = plateauUtil.ajouter_pion(colonne,joueur)
    if (plateauUtil.puissance_4(pion) == False) : 
        h = plateauUtil.check_direction_voisin(pion, 0, 1) + plateauUtil.check_direction_voisin(pion, 0, -1)
        b = plateauUtil.check_direction_voisin(pion, 1, 0)
        vh = plateauUtil.check_direction_voisin(pion, 1, 1)  + plateauUtil.check_direction_voisin(pion, 1, -1)
        vb = plateauUtil.check_direction_voisin(pion, -1, 1) + plateauUtil.check_direction_voisin(pion, -1, -1)
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

def initialiser_arbre(profondeur, maxProfondeur, nbEnfants, c, plateauO, joueur):
    if profondeur > maxProfondeur :
        return None
    valeur = comptagePuissance4(joueur[profondeur%2], plateauO)
    if ( c != None ) :
        plateauO.ajouter_pion(c, joueur[profondeur%2])
    else :
        plateau = copy.deepcopy(plateauO)
    noeud = Noeud(valeur, plateauO)
    
    for c in range (nbEnfants) :
        enfant = initialiser_arbre(profondeur + 1 ,3, 7, c, noeud.get_plateau(), ["O","X"])
        if enfant :
            noeud.ajouter_enfant(enfant)
    return noeud

def minimax(noeud, profondeur, isTourDeIA):
    if profondeur == 0 or noeud.get_AllChildren() == []:
        return noeud,None

    if isTourDeIA:
        return max(minimax(noeud, profondeur-1, False))
    else:
        return min(minimax(noeud, profondeur-1, True))

plateauTest = Plateau()
racine = initialiser_arbre(1, 3, 7, None, plateauTest, ["O","X"])
print (racine.get_valeur())
arbre = Arbre(racine)
print(racine)
print(minimax(racine, 3, True))
#arbre = new Arbre(arbreConstruit)