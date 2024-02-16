from .Pion import Pion

class Plateau: 

    #Constructeur de la classe plateau
    def __init__(self) : 
        #colonne_vide = ["","","","","","","",]
        self.plateau = [[" "," "," "," "," "," "," ",],[" "," "," "," "," "," "," ",],[" "," "," "," "," "," "," ",],[" "," "," "," "," "," "," ",],
        [" "," "," "," "," "," "," ",],[" "," "," "," "," "," "," ",]]
        #for i in range (6) :
        #    self.plateau[i] = colonne_vide
        #Créer un tableau a deux dimensions avec ligne et colonne


    #permet de renvoyer le tableau et ses données
    def get_donnees(self):
        base = "└───┴───┴───┴───┴───┴───┴───┘"
        affiche = ""
        for i in self.plateau :
            for k in range(len(i)) :
                if (k == 0) : 
                    affiche += "│ " + i[k] + " │ "
                elif (k == len(i) - 1) : 
                    affiche +=  i[k] + " │"
                else : 
                    affiche += i[k] + " │ "
            affiche +=  "\n"
        affiche += base
        return affiche
        

    #Permet de savoir si le tableau est plein
    def get_plein(self) : 
        plein = True
        for colonne in self.plateau[5] :
            if (colonne == " ") :
                plein = False
        return plein


    #Ajoute un pion dans le plateau à une certaine colonne
    def ajouter_pion_symbole(self, colonne, symbole) : 
        ligne = 0
        for ligne in range (6) :
            colon = self.plateau[5 - ligne]
            if (colon[colonne] == " ") :
                colon[colonne] = symbole
                break

    #Ajoute un pion dans le plateau à une certaine ligne et colonne
    def ajouter_pion(self,colonne, couleur) : 
        ligne = 0
        for ligne in range (6) :
            colon = self.plateau[5 - ligne]
            if (colon[colonne] == " ") :
                nouvPion = Pion(couleur,ligne,colonne)
                colon[colonne] = nouvPion
                break


 #Ajoute un pion dans le plateau à une certaine ligne et colonne
    def get_case(self,colonne) : 
        ligne = self.plateau[ligne]
        case = ligne[colonne]
        if (case == "") :
            return None
        else :
            return case

    def get_tour_joueur(self) :
        nb_pion_X = 0
        nb_pion_O = 0
        for ligne in range (6) :
            colon = self.plateau[ligne]
            for colonne in range (7) :
                if (colon[colonne] == "X") :
                    nb_pion_X += 1
                elif (colon[colonne] == "O") :
                    nb_pion_O += 1
        if (nb_pion_X <= nb_pion_O) :
            return "X"
        else :
            return "O"


    # Renvoie toutes les possibilités de jeu d'un pion. 
    # Retourne un tableau a 2 dimensions avec les coordonnées possibles
    def get_possibilite(self) :
        ligne = 0
        colonne_possible = ["","","","","","",""]
        for ligne in range (6) :
            colon = self.plateau[ligne]
            for c in range (6) :
                if (colon[c] == "") :
                    colonne_possible[c] = True

        print("TODO get possibilité")

        

