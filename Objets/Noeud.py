import Plateau

class Noeud :

    def __init__(self, valeur, plateau, parent=None):
        self.valeur = valeur
        self.plateau = plateau
        self.parent = parent
        self.enfants = []

    def ajouter_enfant(self,enfant):
        if isinstance(enfant, Noeud):
            enfant.parent = self
            self.enfants.append(enfant)
        else:
            print("L'enfant doit être un Noeud")

    def supprimer_enfant(self,i):
        self.enfants.pop(i)

    def valeur_enfant(self,i):
        if i<len(self.enfants) :
            return self.enfants[i]
        else :
            return None

    def valeur_parent(self):
        if self.parent:
            return self.parent.valeur
        else:
            return None

    def __repr__(self):
        representation = "Noeud: " + repr(self.valeur) + "\n"
        if self.parent:
            representation += "Parent: " + repr(self.parent.valeur) + "\n"
        if self.gauche:
            representation += "Enfant gauche: " + repr(self.gauche.valeur) + "\n"
        if self.droit:
            representation += "Enfant droit: " + repr(self.droit.valeur) + "\n"
        return representation

# Exemple d'utilisation :
if __name__ == "__main__":
    racine = NoeudArbre("Racine")
    enfant_gauche = NoeudArbre("Enfant Gauche")
    enfant_droit = NoeudArbre("Enfant Droit")
    petit_enfant_gauche = NoeudArbre("Petit Enfant Gauche")

    racine.ajouter_enfant_gauche(enfant_gauche)
    racine.ajouter_enfant_droit(enfant_droit)
    enfant_gauche.ajouter_enfant_gauche(petit_enfant_gauche)

    print(racine)
    print("Parent de Enfant Gauche:", enfant_gauche.valeur_parent())
