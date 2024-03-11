from Objets.Noeud import Noeud
from Objets.Plateau import Plateau
from random import randrange
import copy

class Arbre:
    def __init__(self, etat_initial):
        self.racine = Noeud(Plateau.evaluation(etat_initial), etat_initial)

    def generer_arbre(self, noeud : Noeud, profondeur_max, joueur_max):
        if profondeur_max == 0 or noeud.plateau.jeu_est_termine() :
            return None
        for coup in noeud.plateau.get_possibilite():
            nouvel_etat = copy.deepcopy(noeud.plateau)
            nouvel_etat.ajouter_pion(coup,noeud.plateau.get_tour_joueur())
            nouvel_noeud = Noeud(nouvel_etat.evaluation(), nouvel_etat, noeud)
            if nouvel_noeud.valeur !=0 :
                print("valeur du noeud : " + str(nouvel_noeud.valeur))
            noeud.ajouter_enfant(nouvel_noeud)
            self.generer_arbre(nouvel_noeud, profondeur_max - 1, joueur_max)

    def minimax(self, noeud, profondeur, isTourDeIA):
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
        
        print("desente arbre")
        enfantsValide = []
        laValeur = self.minimax(self.racine,4,False)
        print("la valeur rechercher : " + str(laValeur))
        for enfant in self.racine.enfants:
            if enfant.valeur == laValeur :
                enfantsValide.append(enfant)
        nbAleatoir = randrange(len(enfantsValide))
        print(len(enfantsValide))
        print("nb de base : " + str(nbAleatoir))
        while self.racine.plateau.colonneOk(nbAleatoir) == False :
            print("nb possible : " + str(nbAleatoir))
            nbAleatoir = randrange(len(enfantsValide))
        print("nb choisie : " + str(nbAleatoir))
        return self.racine.plateau.ajouter_pion(nbAleatoir,self.racine.plateau.get_tour_joueur())
    
    def __str__(self) : 
        return "racine : "+str(self.racine)

    def __repr__(self):
        return self.__str__()



