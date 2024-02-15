#Classe Pion
class Pion :

    #Constructeur de la classe pion qui prend en paramètre une couleur pour savoir à quelle équipe appartient le pion  
    def __init__(self, couleur,ligne,colonne) : 
        self.couleur = couleur
        self.ligne = ligne
        self.colonne = colonne

        self.voisinBas = " "
        self.voisinDroite = " "
        self.voisinGauche = " "
        self.voisinDiagonalDroiteHaut = " "
        self.voisinDiagonalGaucheHaut = " "
        self.voisinDiagonalDroiteBas = " "
        self.voisinDiagonalGaucheBas = " "
        initialisation_voisin()

    #Renvoie la couleur du pion
    def __str__(self) : 
        return self.couleur

    #Renvoie le voisin de la Diagonale Gauche Bas
    def getVoisinDiagonalGaucheBas(self) :
        return self.voisinDiagonalGaucheBas
       
    #Renvoie le voisin de la Diagonale Droite Bas
    def getVoisinDiagonalDroiteBas(self) :
        return self.voisinDiagonalDroiteBas
        
    #Renvoie le voisin de la Diagonale Gauche Haut
    def getVoisinDiagonalGaucheHaut(self) :
        return self.voisinDiagonalGaucheHaut

    #Renvoie le voisin de la Diagonale Droite Haut
    def getVoisinDiagonalDroiteHaut(self) :
        return self.voisinDiagonalDroiteHaut
        
    #Renvoie le voisin de la Gauche
    def getVoisinGauche(self) :
        return self.voisinGauche
        
    #Renvoie le voisin de la Droite
    def getVoisinDroite(self) :
        return self.voisinDroite
        
    #Renvoie le voisin de la Bas
    def getVoisinBas(self) :
        return self.voisinBas

    #Renvoie le voisin de la Diagonale Gauche Bas
    def setVoisinDiagonalGaucheBas(self, nouveauVoisin) :
        self.voisinDiagonalGaucheBas = nouveauVoisin
       
    #Mise à jour du voisin de la Diagonale Droite Bas
    def setVoisinDiagonalDroiteBas(self, nouveauVoisin) :
        return self.voisinDiagonalDroiteBas = nouveauVoisin
        
    #Mise à jour du voisin de la Diagonale Gauche Haut
    def setVoisinDiagonalGaucheHaut(self, nouveauVoisin) :
        return self.voisinDiagonalGaucheHaut = nouveauVoisin
        
    #Mise à jour du voisin de la Diagonale Droite Haut
    def setVoisinDiagonalDroiteHaut(self, nouveauVoisin) :
        return self.voisinDiagonalDroiteHaut = nouveauVoisin
        
    #Mise à jour du voisin de la Gauche
    def setVoisinGauche(self, nouveauVoisin) :
        return self.voisinGauche = nouveauVoisin

    #Mise à jour du voisin de la Droite
    def setVoisinDroite(self, nouveauVoisin) :
        return self.voisinDroite = nouveauVoisin

    #Mise à jour du voisin de la Bas
    def setVoisinBas(self, nouveauVoisin) :
        return self.voisinBas = nouveauVoisin

    #Initialisation des voisins du pions
    def initialisation_voisin (self) :
        if (ligne == 0) :
            self.voisinBas = False
            self.voisinDiagonalDroiteBas = False
            self.voisinDiagonalGaucheBas = False
        if (colonne == 0) :
            self.voisinGauche = False
            self.voisinDiagonalGaucheBas = False
            self.voisinDiagonalGaucheHaut = False
        if (colonne == 6) :
            self.voisinDroite = False
            self.voisinDiagonalDroiteHaut = False
            self.voisinDiagonalDroiteBas = False
        if (ligne == 5) :
            self.voisinDiagonalGaucheHaut = False
            self.voisinDiagonalDroiteHaut = False

    