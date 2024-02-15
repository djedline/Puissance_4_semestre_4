from Plateau import Plateau

plateauJeu = Plateau()
print(plateauJeu.get_donnees())

plateauJeu.ajouter_pion_symbole(6,"X")
print(plateauJeu.get_donnees())
print(plateauJeu.get_tour_joueur())

