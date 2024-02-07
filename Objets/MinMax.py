#Classe MinMax
class MinMax() : 

    #Méthode qui defini la valeur d'un plateau
    def valeur(plateau) : 
        return 10
    #Méthode qui détermine le minimum d'un tableau
    def min(p,d) :
        if p.isFeuille or d==0 :
            return MinMax.valeur(p)
        else :
            for lePlateau in p.enfant :
                return max(lePlateau, d-1)
    #Méthode qui détermine le maximum d'un tableau
    def max(p,d) :  
        if p.isFeuille or d==0 :
            return MinMax.valeur(p)
        else :
            for lePlateau in p.enfant :
                return min(lePlateau, d-1)
    #méthode qui donne me mini ou maxi du tableau
    def minimax(p,d) :
        for lePlateau in p.enfant :
                return max(lePlateau, d-1)