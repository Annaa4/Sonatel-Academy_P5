from mesfonctionsexo8 import *
tab = [['Prenom','Nom','Téléphone','Classe','Dev','Proj','Exam','Moyenne']]
choisir = int (input("        MENU\n 1. Ajouter un étudiant\n 2. Afficher tout\n 3. Trier et afficher \n 4. Rechercher\n 5. Modification de notes\n 6. Quitter\n Veuillez faire votre choix : "))
if choisir == 1 : 
    saisie(tab)
elif choisir == 2 :
    print('\n')
    print ('La liste des étudiants :\n' )
    affichage(tab)
elif choisir == 3 : 
    print('Voici le tri par ordre décroissant de la moyenne :\n')
    tri(tab)
elif choisir == 4 : 
    choix = input('Donner un critère de recherche d"un étudiant: ')
    print('\n')
    recherche(choix,tab)
elif choisir == 5 : 
    choix = input('Vous souhaitez modifier les informations de quel étudiant ? Veuiller donner son numero : ')
    modification(choix,tab)
elif choisir == 6 : exit
while choisir != 6:
    print('\n')
    choisir = int (input("        MENU\n 1. Ajouter un étudiant\n 2. Afficher tout\n 3. Trier et afficher \n 4. Rechercher\n 5. Modification de notes\n 6. Quitter\n Veuillez faire votre choix : "))
if choisir == 1 : 
    saisie(tab)
elif choisir == 2 :
    print('\n')
    print ('La liste des étudiants :\n' )
    affichage(tab)
elif choisir == 3 : 
    print('Voici le tri par ordre décroissant de la moyenne :\n')
    tri(tab)
elif choisir == 4 : 
    choix = input('Donner un critère de recherche d"un étudiant: ')
    print('\n')
    recherche(choix,tab)
elif choisir == 5 : 
    choix = input('Vous souhaitez modifier les informations de quel étudiant ? Veuiller donner son numero : ')
    modification(choix,tab)
if choisir == 6 : exit