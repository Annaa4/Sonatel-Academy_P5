ordre = int (input("Donner l'ordre de votre matrice : "))
couleur = str (input("choisissez une couleur entre Rouge et Bleu : ")) 
position = str (input("Choisissez une position : ADDP, EDDP, SDP,ADDS,EDDS,SDS : "))
matrice = []

for i in range (ordre):
    ligne = []
    for j in range (ordre):
        if i < j and position == 'ADDP':
            if couleur == 'Rouge':
                ligne.append('r')
            else :
                ligne.append('b')
        elif i > j and position == 'EDDP':
            if couleur == 'Rouge':
                ligne.append('r')
            else :
                ligne.append('b')
        elif  i+j>ordre and position == 'EDDS':
            if couleur == 'Rouge':
                ligne.append('r')
            else :
                ligne.append('b')
        elif i+j <=(ordre - 2)and position == 'ADDS':
            if couleur == 'Rouge':
                ligne.append('r')
            else :
                ligne.append('b')
        elif i == j and position == 'SDP':
             if couleur == 'Rouge':
                ligne.append('r')
             else :
                ligne.append('b')
        elif i+j == (ordre - 1) and position == 'SDS':
             if couleur == 'Rouge':
                ligne.append('r')
             else :
                ligne.append('b')
        else:
            ligne.append('*')
        
    matrice.append(ligne)

for ligne in matrice :
    for i in range (ordre):
        print (ligne[i], end='\t')
    print('\n')
