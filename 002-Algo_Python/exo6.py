ordre = str (input("Donner l'ordre de votre matrice : "))
while ordre not in ['5','6','7','8','9'] or (int(ordre)) <4:
    ordre = str(input("L'ordre de la matrice doit être supérieure à 4; Veuillez réessayer : "))
couleur = int (input("choisissez une couleur :\n 1.Rouge\n 2. Bleu\n 3. Vert ")) 
position = int (input("Choisissez une position :\n 1. ADDP\n 2. EDDP\n 3. SDP\n 4. ADDS\n 5. EDDS\n 6. SDS \n"))
matrice = []

for i in range (int(ordre)):
    ligne = []
    for j in range (int(ordre)):
        if i < j and position == 1:
            if couleur == 1:
                ligne.append('r')
            elif couleur == 2 :
                ligne.append('b')
            elif couleur == 3 :
                ligne.append('v')
        elif i > j and position == 2:
            if couleur == 1:
                ligne.append('r')
            elif couleur == 2 :
                ligne.append('b')
            elif couleur == 3 :
                ligne.append('v')
        elif  i+j>(int(ordre)) and position == 5:
            if couleur == 1:
                ligne.append('r')
            elif couleur == 2 :
                ligne.append('b')
            elif couleur == 3 :
                ligne.append('v')
        elif i+j <=((int(ordre)) - 2)and position == 4:
            if couleur == 1:
                ligne.append('r')
            elif couleur == 2 :
                ligne.append('b')
            elif couleur == 3 :
                ligne.append('v')
        elif i == j and position == 3:
             if couleur == 1:
                ligne.append('r')
             elif couleur == 2 :
                ligne.append('b')
             elif couleur == 3 :
                ligne.append('v')
        elif i+j == ((int(ordre)) - 1) and position == 6:
             if couleur == 1:
                ligne.append('r')
             elif couleur == 2 :
                ligne.append('b')
             elif couleur == 3 :
                ligne.append('v')
        else:
            ligne.append('*')
        
    matrice.append(ligne)

for ligne in matrice :
    for i in range (int(ordre)):
        print (ligne[i], end='\t')
    print('\n')
