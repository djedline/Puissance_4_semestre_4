import Plateau

class Noeud :

    def __init__(self, valeur, plateau, parent=None):
        self.valeur = valeur
        self.plateau = plateau
        self.parent = parent
        self.gauche = None
        self.droit = None

    def ajouter_enfant_gauche(self, enfant_gauche):
        if isinstance(enfant_gauche, NoeudArbre):
            enfant_gauche.parent = self
            self.gauche = enfant_gauche
        else:
            print("L'enfant doit être un NoeudArbre")

    def ajouter_enfant_droit(self, enfant_droit):
        if isinstance(enfant_droit, NoeudArbre):
            enfant_droit.parent = self
            self.droit = enfant_droit
        else:
            print("L'enfant doit être un NoeudArbre")

    def supprimer_enfant_gauche(self):
        self.gauche = None

    def supprimer_enfant_droit(self):
        self.droit = None

    def valeur_enfant_gauche(self):
        if self.gauche:
            return self.gauche.valeur
        else:
            return None

    def valeur_enfant_droit(self):
        if self.droit:
            return self.droit.valeur
        else:
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
