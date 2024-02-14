#Classe Pion
class Pion :
    #Constructeur de la classe pion qui prend en paramètre une couleur pour savoir à quelle équipe appartient le pion  
    def __init__(self, couleur,ligne,colonne) : 
        self.couleur = couleur
        self.ligne = ligne
        self.colonne = colonne

        if (ligne != 0) :
            self.voisinBas = false
        self.voisinDroite = ""
        self.voisinGauche = ""
        self.voisinDiagonalDroiteHaut = ""
        self.voisinDiagonalGaucheHaut = ""
        self.voisinDiagonalDroiteBas = ""
        self.voisinDiagonalGaucheBas = ""

    #Renvoie la couleur du pion
    def get_couleur() : 
        return self.couleur
         
    def initialisation_voisin
    