from Plateau import Plateau
from Pion import Pion

plateauJeu = Plateau()
print(plateauJeu.get_donnees())

#plateauJeu.ajouter_pion_symbole(6,"X")
plateauJeu.ajouter_pion(1,"X")
plateauJeu.ajouter_pion(2,"O")
plateauJeu.ajouter_pion(2,"X")
plateauJeu.ajouter_pion(3,"O")
plateauJeu.ajouter_pion(3,"O")
plateauJeu.ajouter_pion(3,"X")
plateauJeu.ajouter_pion(4,"O")
plateauJeu.ajouter_pion(4,"O")
plateauJeu.ajouter_pion(4,"O")
plateauJeu.ajouter_pion(4,"X")
plateauJeu.ajouter_pion(4,"X")
#plateauJeu.ajouter_pion(5,"X")
print(plateauJeu.get_donnees())
print("a qui le tour : " + plateauJeu.get_tour_joueur())
print(str(plateauJeu.get_case(5,5)))
print(str(plateauJeu.get_case(4,4).getLigne()))
print(str(plateauJeu.get_possibilite()))
pion_test = plateauJeu.get_case(4,2)
plateauJeu.puissance_4(pion_test)
if plateauJeu.puissance_4(pion_test):
    print("Puissance 4 trouvé!")
else:
    print("Pas de Puissance 4.")