from mesfonctionsexo9 import *
tab = []
choix =int(input("          MENU\n 1. Saisir opérateurs et client\n 2. Affichage des clients\n 3. Afficher les clients d'un opérateur\n 4. Afficher les numéros d'un client\n 5. Modifier ou ajouter un numéro\n 6. Quitter"))
while choix in [1,2,3,4,5]:
    if choix == 1:
        saisie(tab)
    elif choix == 2:
        affichage(tab)
    elif choix == 3:
        c = input("Choisissez un opérateur")
        affichage_client(c,tab)
    elif choix == 4:
        nom = input("Donner le nom du client")
        prenom = input ("Donner le prenom du client")
        affiche_numero(nom,prenom,tab)
    elif choix == 5:
        nom = input("Donner le nom du client")
        prenom = input ("Donner le prenom du client")
        modification(nom,prenom,tab)
    choix =int(input("          MENU\n 1. Saisir opérateurs et client\n 2. Affichage des clients\n 3. Afficher les clients d'un opérateur\n 4. Afficher les numéros d'un client\n 5. Modifier ou ajouter un numéro\n 6. Quitter"))
if choix == 6:
    exit
                