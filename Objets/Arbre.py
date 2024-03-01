import Noeud
import Plateau
from random import randrange

class Arbre:
    def __init__(self, etat_initial):
        self.racine = Noeud(Plateau.evaluation(etat_initial), etat_initial)

    def generer_arbre(self, noeud : Noeud, profondeur_max, joueur_max):
        if profondeur_max == 0 or noeud.plateau.jeuFini :
            return None
        for coup in noeud.plateau.get_possibilite():
            nouvel_etat = noeud.plateau.ajouter_pion(coup,noeud.plateau.get_tour_joueur())
            nouvel_noeud = Noeud(Plateau.evaluation(nouvel_etat), nouvel_etat)
            noeud.ajouter_enfant(nouvel_noeud)
            self.generer_arbre(nouvel_noeud, profondeur_max - 1, joueur_max)

    def minimax(self, noeud, profondeur, isTourDeIA):
        if profondeur == 0 or Plateau.jeu_est_termine(noeud.etat):
            return noeud.valeur
        if isTourDeIA:
            valeur_max = float("-inf")
            for enfant in noeud.enfants:
                valeur = self.minimax(enfant, profondeur - 1, False)
                valeur_max = max(valeur_max, valeur)
            noeud.valeur = valeur_max
            return valeur_max
        else:
            valeur_min = float("inf")
            for enfant in noeud.enfants:
                valeur = self.minimax(enfant, profondeur - 1, True)
                valeur_min = min(valeur_min, valeur)
            noeud.valeur = valeur_min
            return valeur_min
        
    def descenteArbre(self):
        enfantsValide = []
        laValeur = Arbre.minimax(self.racine,4,True)
        for enfant in self.racine.enfants:
            if enfant.valeur == laValeur :
                enfantsValide.append(enfant)
        nonChoisie = True
        self.racine.plateau.jouer(enfantsValide[randrange(len(enfantsValide))].plateau)



