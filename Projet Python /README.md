# Projet Python
__Récupérer le fichier contenant les données ()__
Faites un traitement de ce fichier ensuite mettez les données dans une structure de votre choix
(liste, tuple, dictionnaire ou une combinaison de ses derniers)  
 Vous devez séparer les données valides et celles non valide (Une ligne est invalide si une
des informations qu’il contient n’est pas valide) ; pour les ligne invalides vous devez
garder les informations qui l’on rendu invalide  
 Les différentes données sont :  
 Numéro  
Composé de lettre majuscule et de chiffre  
Sa taille est 7  
Exemple : H5G32YR ou 54YTG5T  
 Prénom  
Commence par une lettre  
Contient au moins 3 lettre  
 Nom  
Commence par une lettre  
Contient au moins 2 lettre  
 Date de naissance  
Doit être une date valide  
Vous devez choisir un format de date et transformer toutes les dates sous ce format
 Classe  
6em à 3em plus les lettres A & B  
Vous devez choisir un format de classe et transformer toutes les classes sous ce format  
 Note  
Voici ce que contient la chaine note  
- Les différentes matières sont séparer par dièse #  
- Les notes des matières sont dans des crochets []  
- Les notes de devoir sont séparées par la note d'examen par deux point :  
- Les notes de devoir sont séparées entre eux par une barre verticale |    

__Exemple__ 

Math[12|11:13]#Francais[4|11|8:13]#Anglais[13,5|11:15]#PC[11:9]#SVT[12|9|16|11:12]#HG[10:13]  
Francais[4|11:13]#Anglais[13,5:15]#PC[11:9]#SVT[12|9|16|11:12]#HG[10:13]#Math[12|14,5|11:13]  
Vous devez garder pour chaque matière  
o Les notes de devoir  
o La note d’examen  
o La moyenne [moyenne = (moyenne(note)+2*note_examen)/3]  

__Créer un menu permettant__  
 D’afficher les informations (Valide ou invalide ; au choix)  
 D’afficher une information (par son numéro)  
 D’afficher les cinq premiers  
 D’ajouter une information en vérifiant la validité des informations données.  
 De modifier une information invalide ensuite le transférer dans la structure où se
trouve les informations valides  

__Dans cette partie l’affichage se fera par pagination.__  
 Dans le premier cas vous paginez par 5 lignes  
 Dans le second cas vous demandez à l’utilisateur de choisir par combien de ligne il
veut paginer  