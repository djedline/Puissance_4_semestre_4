from Plateau import Plateau

plateauJeu = Plateau()
print(plateauJeu.get_donnees())
print(plateauJeu.get_plein())
plateauJeu.ajouter_pion_symbole(2,"X")
print(plateauJeu.get_donnees())
plateauJeu.ajouter_pion_symbole(2,"X")
plateauJeu.ajouter_pion_symbole(2,"X")
plateauJeu.ajouter_pion_symbole(3,"X")
print(plateauJeu.get_donnees())
