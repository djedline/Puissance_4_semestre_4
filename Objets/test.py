tableau_chaine_vide = ["","","","","","",""]
tableau_annule = [None,None,None,None,None,None,None]
print(len(tableau_chaine_vide))
print(len(tableau_annule))
possible = True
for case in tableau_chaine_vide :
    if (case == None) :
        possible = False
        break
print(possible)
