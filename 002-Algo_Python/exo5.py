ordre = int (input("Donner l'ordre de votre matrice : "))
couleur = str (input("choisissez une couleur entre Rouge et Bleu : ")) 
position = str (input("Choisissez une position : Haut ou bas"))

matrice = []

for i in range (ordre):
    ligne = []
    for j in range (ordre):
        if i < j and position == 'Haut':
            if couleur == 'Rouge':
                ligne.append('r')
            else :
                ligne.append('b')
        elif i > j and position == 'Bas':
            if couleur == 'Rouge':
                ligne.append(r)
            else :
                ligne.append(b)
        else:
            ligne.append('*')
    matrice.append(ligne)

for ligne in matrice :
    for i in range (ordre):
        print (ligne[i], end='  ')
    print('\n')
