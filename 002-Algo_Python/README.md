                                                              TD ALGO-PYTHON
Exercice 1
Écrire un programme qui propose à l’utilisateur le menu de choix suivant :
1. Mois en Français
2. Mois en Anglais
3. Quitter
Règles de Gestion
● Par défaut le programme affiche les mois en Français
● Les mois doivent être affichés comme ci-dessous
● Les mois sont stockés dans un tableau
JanvierAvrilJuilletOctobre
FévrierMaiAoûtNovembre
MarsJuinSeptembreDécembre
Exercice 2
Écrire un programme qui permet de saisir une phrase. Le programme enlève tous les espaces
inutiles de la phrase.
Exercice 3
Écrire un programme qui permet de saisir une chaîne de N phrases. Le programme enlève
tous les espaces inutiles de chaque phrase puis réaffiche les phrases corrigées.
Règles de Gestion
● La chaîne de saisie est Obligatoire
● Les phrases ne doivent pas contenir des caractères spéciaux
● Une phrase commence par une lettre majuscule et se termine par un point (. ou ?ou !)
● Chaque phrase contiendra au moins 25 caractères
Exercice 4
Écrire un programme qui permet de remplir N numéros à partir d’une chaîne. Le programme
réaffiche les numéros valides à gauche et les numéros invalides à droite de l’écran. Le
programme affichera aussi le nombre de numéros de chaque opérateur.
Règles de Gestion
● La chaîne de saisie des numéros est obligatoire
● Les numéros doivent être valides.
● Un numéro est valide :
○ S’il commence par 77,78,76,70 ou 75
○ S’il contient que 9 chiffres
○ Un numéro peut contenir des espacesExercice 5
Proposer un programme qui permet la saisie :
● De l’ordre d’une matrice carrée
● Un Menu de choix avec comme options Bleu et Rouge
● Un Menu de choix pour la position de la couleur Bleu avec comme valeur HAUT ou
BAS.
Lorsque l’utilisateur valide, le programme devra dessiner la matrice en la coloriant suivant les
couleurs et les positions choisies par l’utilisateur.
Règles de Gestion
● Haut correspond aux éléments se situant au-dessus de la diagonale principale
● Bas correspond aux éléments se situant en dessous de la diagonale principale
● Tous les choix sont obligatoires
● L’ordre de la matrice est un entier et est supérieur à 5
Exercice 6
Proposer un programme qui permet la saisie :
● De l’ordre d’une matrice carrée
● Un Menu de choix pour la position de la couleur
○ ADDP, au-dessus de la diagonale principale.
○ EDDP, en dessous de la diagonale principale
○ SDP, sur la diagonale principale
○ ADDS, au-dessus de la diagonale secondaire.
○ EDDS, en dessous de la diagonale secondaire
○ SDS, sur la diagonale secondaire
● Un Menu de choix ayant comme options des couleurs
Lorsque l’utilisateur valide, le programme devra dessiner la matrice en la coloriant suivant les
couleurs et les positions choisies par l’utilisateur.
Initialiser un tableau de couleurs. Ce tableau sera utilisé pour générer le Menu choix des
couleurs.
Initialiser un tableau de positions formé des valeurs :
○ ADDP, au-dessus de la diagonale principale.
○ EDDP, en dessous de la diagonale principale
○ SDP, sur la diagonale principale
○ ADDS, au-dessus de la diagonale secondaire.
○ EDDS, en dessous de la diagonale secondaire
○ SDS, sur la diagonale secondaire
Ce tableau sera utilisé pour générer les options du menu de position.
Règles de Gestion
● A chaque choix d’une position on devra l’associer a une couleur.
● Toutes les valeurs sont Obligatoires
● Le champ de saisi de l’ordre de la matrice est un entier et est supérieur à 4
● Une couleur est choisie une et une seule foisExercice 7 :
Écrire un programme qui, à partir d’une phrase, affiche son équivalent codé.
Règles de codage de la phrase :
On considère le clavier avec les anciens téléphones avec touches.
- Pour Écrire la lettre A : il faut appuyer une fois sur la touche 2
- Pour Écrire la lettre B : il faut appuyer deux fois sur la touche 2
- Pour écrire la lettre S : il faut appuyer trois fois sur la touche 7.
Dans le programme on a les règles suivantes :
- Pour écrire des chiffres, on écrit des lettres et les lettres deviennent des chiffres :
- Pour écrire le chiffre ZÉRO (0), on écrit : A,
- Le chiffre UN (1) devient la lettre B, ainsi de suite jusqu’au chiffre NEUF (9) qui
devient la lettre J.
- Le caractère ESPACE est représenté par DEUX ZÉROS (00).
- Les autres caractères ne sont pas changés.
- Si des lettres partageant le même chiffre se succèdent, alors il faut les séparer par le
chiffre ZÉRO (0)
- Exemples :
- Bonjour aly ⇔ 22666066566688777002555999
- J’ai 17,5 en algo ⇔ 5’244400bh,f0033660025554666Exercice 8
Demander des informations concernant l’étudiant tant que l’utilisateur désire continuer.
Vous devez demander le téléphone, nom, prénom, classe, note de devoir, note de projet et
note d’examen pour ensuite calculer la moyenne et afficher le résultat sous forme du tableau
ci- dessous lorsque l’utilisateur terminera sa saisie.
Le numéro de téléphone doit être unique et doit répondre aux critères définis dans l’exo 4
Les notes et la moyenne sont des décimales à 2 chiffres comprises entre 0 et 20.
Ci-dessous un tableau vous montrant l’affichage comme il se doit.
Contraintes techniques
● Vous utiliserez une page ou vous mettrez toutes vos fonctions et vous les appelez dans
les autres pages.
● Dès l’exécution de votre fichier vous devez avoir un menu comme suit:
○ Afficher tout
○ Trier et afficher (par ordre décroissant de la moyenne)
○ Rechercher selon un critère (téléphone, nom, prénom ou classe)
○ Modification de notes pour un étudiant choisit par l’utilisateur en donnant le
numéro de téléphone.
○ Sortir (permet de terminer l’application)
● A chaque fois que vous terminez avec une étape (1à 5) vous devez réafficher le menu
● Tous les affichages doivent se faire sous forme de tableau
● Tous les contrôles de saisie doivent être faits par vos propres fonctions.
