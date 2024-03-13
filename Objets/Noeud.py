import Plateau

class Noeud :

    def __init__(self, valeur, plateau):
        self.valeur = valeur
        self.plateau = plateau
        self.enfants = []

    def get_plateau(self) :
        return self.plateau

    def get_valeur(self) :
        return self.valeur

    def ajouter_enfant(self,enfant):
        self.enfants.append(enfant)
        
    def supprimer_enfant(self,i):
        self.enfants.pop(i)

    def get_AllChildren(self):
        return self.enfants

    def get_child(self,i):
        if i<len(self.enfants) :
            return self.enfants[i]
        else :
            return None

    def __repr__(self):
        return repr(self.valeur)

# Exemple d'utilisation :
if __name__ == "__main__":
    racine = NoeudArbre("Racine")
    enfant_gauche = NoeudArbre("Enfant Gauche")
    enfant_droit = NoeudArbre("Enfant Droit")
    petit_enfant_gauche = NoeudArbre("Petit Enfant Gauche")

    racine.ajouter_enfant_gauche(enfant_gauche)
    racine.ajouter_enfant_droit(enfant_droit)
    enfant_gauche.ajouter_enfant_gauche(petit_enfant_gauche)

