class Arbre:
    def __init__(self, etat_initial, joueur_initial):
        self.racine = Noeud(etat_initial, joueur_initial)

    def generer_arbre(self, noeud, profondeur_max, joueur_max):
        if profondeur_max == 0 or jeu_est_termine(noeud.etat):
            return
        for coup in generer_coups_possibles(noeud.etat):
            nouvel_etat = jouer_coup(noeud.etat, coup)
            nouvel_noeud = Noeud(nouvel_etat, joueur_suivant(noeud.joueur))
            noeud.ajouter_enfant(nouvel_noeud)
            self.generer_arbre(nouvel_noeud, profondeur_max - 1, joueur_max)

    def minimax(self, noeud, profondeur, joueur_max):
        if profondeur == 0 or jeu_est_termine(noeud.etat):
            return evaluation(noeud.etat)
        if joueur_max:
            valeur_max = float("-inf")
            for enfant in noeud.enfants:
                valeur = self.minimax(enfant, profondeur - 1, False)
                valeur_max = max(valeur_max, valeur)
            return valeur_max
        else:
            valeur_min = float("inf")
            for enfant in noeud.enfants:
                valeur = self.minimax(enfant, profondeur - 1, True)
                valeur_min = min(valeur_min, valeur)
            return valeur_min