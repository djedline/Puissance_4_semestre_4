#Classe Pion
class Pion :
    #Constructeur de la classe pion qui prend en paramètre une couleur pour savoir à quelle équipe appartient le pion  
    def __init__(self, couleur) : 
        self.couleur = couleur

    #Renvoie la couleur du pion
    def get_couleur() : 
        return self.couleur
         
    