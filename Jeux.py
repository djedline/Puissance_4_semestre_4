from Objets.Plateau import Plateau


MENU = """           *****************************************************
           |                         MENU                      |
           *****************************************************
           | L : lancer le jeu                                 |
           | R : Règles du jeu                                 |
           | Q : Quitter                                       |
           *****************************************************
                """     



REGLE_JEU = """
            **********************************************************   
            |                          REGLES !                      |
            **********************************************************
            |                                                         |
            ********************************************************** 
            """
MESSAGE_ERREUR_SAISIE = "Erreur de saisie !"

def jouerJeu():
    plateauJeu = Plateau()
    print(plateauJeu.get_donnees())
    coupTotaux = 0
    while True : 
        colonneJeu = input("Ou voulez-vous jouer ? (numéro de la colonne entre 1 et 6)")
        if (coupTotaux % 2 == 0) :
            choixContinuer = input("Voulez vous continuer le jeu ? (o/n")
            if (choixContinuer == "n") :
                break



        coupTotaux += 1

def afficherRegles():
    print(REGLE_JEU)
    input("Cliquez sur \"Entrée\" pour revenir au menu. ").lower()


def quitterLeJeu():

    raise SystemExit


def default():
    print(MESSAGE_ERREUR_SAISIE)

totalChoix = {
    "L": jouerJeu,
    "R": afficherRegles,
    "Q": quitterLeJeu
}


def switch(option):
    print('\n' * 50)
    func = totalChoix.get(option, default)
    func()



while True:
    print(MENU)
    choix = input("Quel est votre choix ? ")
    switch(choix)
    