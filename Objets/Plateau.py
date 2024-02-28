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
        base = " └───┴───┴───┴───┴───┴───┴───┘\n   0   1   2   3   4   5   6"
        affiche = ""
        n = 0
        for i in self.plateau :
            for k in range(len(i)) :
                if (k == 0) : 
                    affiche += str(n) +"│ " + str(i[k]) + " │ "
                elif (k == len(i) - 1) : 
                    affiche +=  str(i[k]) + " │"
                else : 
                    affiche += str(i[k]) + " │ "
            affiche +=  "\n"
            n += 1
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
            colon = self.plateau[5-ligne]
            if (colon[colonne] == " ") :
                nouvPion = Pion(couleur,(5-ligne),colonne)
                colon[colonne] = nouvPion
                self.mise_a_jour_pion(nouvPion)
                break


    def mise_a_jour_pion(self, nouvPion) :
        ligne = nouvPion.getLigne()
        colonne = nouvPion.getColonne()
        # voisin droite
        if (colonne != 6 and self.plateau[ligne][colonne+1] != " ") :
            nouvPion.setVoisinDroite = self.plateau[ligne][colonne+1]
            self.plateau[ligne][colonne+1].setVoisinGauche = nouvPion
        # voisin gauche
        if (colonne != 0 and self.plateau[ligne][colonne-1] != " ") :
            nouvPion.setVoisinGauche = self.plateau[ligne][colonne-1]
            self.plateau[ligne][colonne-1].setVoisinGauche = nouvPion
        # voisin bas
        if (ligne != 5 and self.plateau[ligne+1][colonne] != " ") :
            nouvPion.setVoisinBas = self.plateau[ligne+1][colonne]
            self.plateau[ligne+1][colonne].setVoisinBas = nouvPion
        # voisin diagonaledroitehaute
        if (colonne != 6 and ligne != 0 and self.plateau[ligne-1][colonne+1] != " ") :
            nouvPion.setVoisinDiagonalDroiteHaut = self.plateau[ligne-1][colonne+1]
            self.plateau[ligne-1][colonne+1].setVoisinDiagonalGaucheBas = nouvPion
        # voisin diagonaledroitebas
        if (colonne != 6 and ligne != 5 and self.plateau[ligne+1][colonne+1] != " ") :
            nouvPion.setVoisinDiagonalDroiteBas = self.plateau[ligne+1][colonne+1]
            self.plateau[ligne+1][colonne+1].setVoisinDiagonalGaucheHaut = nouvPion
        # voisin diagonalegauchehaute
        if (colonne != 0 and ligne != 0 and self.plateau[ligne-1][colonne-1] != " ") :
            nouvPion.setVoisinDiagonalGaucheHaut = self.plateau[ligne-1][colonne-1]
            self.plateau[ligne-1][colonne-1].setVoisinDiagonalDroiteBas = nouvPion
        # voisin diagonalegauchehaute
        if (colonne != 0 and ligne != 5 and self.plateau[ligne+1][colonne-1] != " ") :
            nouvPion.setVoisinDiagonalGaucheBas = self.plateau[ligne+1][colonne-1]
            self.plateau[ligne+1][colonne-1].setVoisinDiagonalGaucheHaut = nouvPion

    #Renvoie les données d'une case
    def get_case(self,colonne,ligne) : 
        case = self.plateau[ligne][colonne]
        if (case == "") :
            return None
        else :
            return case

   # def puissance_4(self, pion):
   # Test puissance :

    def puissance_4(self, pion):
        couleur = str(pion)

        # Vérification horizontale
        if self.check_direction(pion, 0, 1) + self.check_direction(pion, 0, -1) >= 3:
            return True

        # Vérification verticale
        #print("vertical = " + str(self.check_direction(pion, 1, 0)))
        if self.check_direction(pion, 1, 0) >= 3:
            return True

        # Vérification diagonale droite bas et gauche haut
        if self.check_direction(pion, 1, 1) + self.check_direction(pion, -1, -1) >= 3:
            return True

        # Vérification diagonale gauche bas et droite haut
        if self.check_direction(pion, 1, -1) + self.check_direction(pion, -1, 1) >= 3:
            return True

        return False 

    def check_direction(self, pion, delta_ligne, delta_colonne):
        """
        Vérifie le nombre de pions alignés dans une direction donnée à partir du pion spécifié.
        """
        ligne = pion.getLigne() 
        colonne = pion.getColonne()
        #print ("ligne " + str(ligne) + " : " + str(delta_ligne) + " | colonne " + str(colonne) + " : " + str(delta_colonne))
        couleur = str(pion)
        verif = delta_colonne
        count = 0
        #for i in range (3) :
            #ligne = delta_ligne

        for i in range(3):
            ligne += delta_ligne
            colonne += delta_colonne
            # Vérifie si la case suivante a le même symbole
            if (0 <= ligne < 6 and 0 <= colonne < 7 and (str(self.plateau[ligne][colonne]) == couleur)):
                count += 1
                #print("delta colonne : " +str(delta_colonne) + " | colonne : " + str(colonne)  + " | ligne : " + str(ligne) + " : " + str(self.plateau[ligne][colonne]))
            else:
                #print("delta colonne : " +str(delta_colonne) + " | colonne : " + str(colonne)  + " | ligne : " + str(ligne))
                break

        return count

    def get_tour_joueur(self) :
        nb_pion_X = 0
        nb_pion_O = 0
        for ligne in range (6) :
            colon = self.plateau[ligne]
            for colonne in range (7) :
                if (str(colon[colonne]) == "X") :
                    nb_pion_X += 1
                elif (str(colon[colonne]) == "O") :
                    nb_pion_O += 1
        if (nb_pion_X <= nb_pion_O) :
            return "X"
        else :
            return "O"


    # Renvoie toutes les possibilités de jeu d'un pion. 
    # Retourne un tableau a 2 dimensions avec les coordonnées possibles
    def get_possibilite(self) :
        c = self.plateau[0]
        for colonne in range (7) :   
            if (self.plateau[0][colonne] != " ") :
                c[colonne] = True
        return c

        

