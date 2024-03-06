from Objets.Noeud import Noeud
from Objets.Plateau import Plateau
from random import randrange
import copy

class Arbre:
    def __init__(self, etat_initial):
        self.racine = Noeud(Plateau.evaluation(etat_initial), etat_initial)

    def generer_arbre(self, noeud : Noeud, profondeur_max, joueur_max):
        print("generer arbre")
        if profondeur_max == 0 or noeud.plateau.jeu_est_termine() :
            return None
        for coup in noeud.plateau.get_possibilite():
            nouvel_etat = copy.deepcopy(noeud.plateau)
            nouvel_etat.ajouter_pion(coup,noeud.plateau.get_tour_joueur())
            nouvel_noeud = Noeud(nouvel_etat.evaluation(), nouvel_etat, noeud)
            noeud.ajouter_enfant(nouvel_noeud)
            self.generer_arbre(nouvel_noeud, profondeur_max - 1, joueur_max)

    def minimax(self, noeud, profondeur, isTourDeIA):
        print("minimax")
        if profondeur == 0 or noeud.plateau.jeu_est_termine():
            return noeud.valeur
        if isTourDeIA:
            valeur_max = -1000
            for enfant in noeud.enfants:
                valeur = self.minimax(enfant, profondeur - 1, False)
                valeur_max = max(valeur_max, valeur)
            noeud.valeur = valeur_max
            return valeur_max
        else:
            valeur_min = 1000
            for enfant in noeud.enfants:
                valeur = self.minimax(enfant, profondeur - 1, True)
                valeur_min = min(valeur_min, valeur)
            noeud.valeur = valeur_min
            return valeur_min
        
    def descenteArbre(self):
        enfantsValide = []
        laValeur = self.minimax(self.racine,4,True)
        for enfant in self.racine.enfants:
            if enfant.valeur == laValeur :
                enfantsValide.append(enfant)
        return self.racine.plateau.jouer(enfantsValide[randrange(len(enfantsValide))].plateau)



