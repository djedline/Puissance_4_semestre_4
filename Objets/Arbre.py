import Noeud
import Plateau
from random import randrange

class Arbre:
    def __init__(self, racine):
        #self.racine = Noeud(Plateau.evaluation(etat_initial), etat_initial)
        self.racine = racine

    def generer_arbre(self, noeud : Noeud, profondeur_max, joueur_max):
        if profondeur_max == 0 or noeud.plateau.jeuFini :
            return None
        for coup in noeud.plateau.get_possibilite():
            nouvel_etat = noeud.plateau.ajouter_pion(coup,noeud.plateau.get_tour_joueur())
            nouvel_noeud = Noeud(Plateau.evaluation(nouvel_etat), nouvel_etat)
            noeud.ajouter_enfant(nouvel_noeud)
            self.generer_arbre(nouvel_noeud, profondeur_max - 1, joueur_max)

    def minimaxv2(self, noeud, profondeur) :
        if profondeur == 0 or ... :
            return noeud
        else :
            if isTourDeIa :
                return max(minimaxV2())
            else :
                return min(minimaxV2())

        
    def descenteArbre(self):
        enfantsValide = []
        laValeur = Arbre.minimax(self.racine,4,True)
        for enfant in self.racine.enfants:
            if enfant.valeur == laValeur :
                enfantsValide.append(enfant)
        nonChoisie = True
        self.racine.plateau.jouer(enfantsValide[randrange(len(enfantsValide))].plateau)



