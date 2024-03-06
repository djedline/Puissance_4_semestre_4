from Objets.Plateau import Plateau
import random
from Objets.Arbre import Arbre


MENUPRINCIPALE = """           *****************************************************
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

def initialisationJeu():
    print("initialisation du plateau")
    plateauJeu = Plateau()
    joueur = False
    gestionTour(plateauJeu,joueur)
    #print(plateauJeu.get_donnees())

#TODO terminé la méthode
def gestionTour(plateau,pionJ) :
    nbTour = 0
    joueur = ["J1","IA"]
    i = random.randrange(0,2)
    tourJ = joueur[i]
    while True :
        nbTour += 1
        if (nbTour != 1) :
            i = 1 if (i == 0) else 0
            tourJ = joueur[i]
        print ("C'est le tour de " + str(tourJ))
        if (tourJ[0] == "J") :
            pion = tourJoueur(plateau)
        else :
            pion = tourIA(plateau)
        if ((plateau.puissance_4(pion) == True) or (plateau.get_plein() == True)) :
            break
    print("Fin de partie. " + str(tourJ + " à gagné"))


def afficherRegles():
    print(REGLE_JEU)

def quitterLeJeu():
    raise SystemExit

def getMenu() :
    print(MENUPRINCIPALE)
    choix = input("Quel est votre choix ? ")
    match choix :
        case "L" :
            #lance le jeu
            initialisationJeu()
            getMenu()
        case "R":
            #Regle du jeu
            afficherRegles()
            getMenu()
        case "Q":
            print("Merci d'avoir joué !")
        case _:
            print(MESSAGE_ERREUR_SAISIE)
            getMenu()

def tourJoueur(plateau) :
    print(plateau.get_donnees())
    choix = input("Quel colonne ?")
    poser = True
    print(choix)
    match (choix) :
        case ("0") :
            poser = plateau.ajouter_pion(int(choix), "X")
        case ("1") :
            poser = plateau.ajouter_pion(int(choix), "X")
        case ("2") :
            poser = plateau.ajouter_pion(int(choix), "X")
        case ("3") :
            poser = plateau.ajouter_pion(int(choix), "X")
        case ("4") :
            poser = plateau.ajouter_pion(int(choix), "X")
        case ("5") :
            poser = plateau.ajouter_pion(int(choix), "X")
        case ("6") :
            poser = plateau.ajouter_pion(int(choix), "X")
        case _:
            print("cette colonne n'existe pas")
            tourJoueur(plateau)
    if (poser == False) :
        print("vous ne pouvez plus poser ici")
        tourJoueur(plateau)
    else :
        return poser

def tourIA(plateau) :
    print(plateau.get_donnees())
    lArbre = Arbre(plateau)
    lArbre.generer_arbre( lArbre.racine, 4, False)
    return lArbre.descenteArbre()

    """ i = random.randrange(0,7)
    poser = plateau.ajouter_pion(i,"O")
    if (poser == False) :
        tourIA(tourIA)
    else :
        return poser """
    
getMenu()