import json
from data_structure import *


choix_fichier =str(input("Sur quel type de fichier voulez-vous travaillez ? : CSV,JSON,XML : "))
if choix_fichier=='json'or'JSON':
    choix=int(input("            MENU       \n"
                    "1.Afficher les informations\n"
                    "2.Afficher une information\n"
                    "3.Affficher les cinq premiers\n"
                    "4.Ajouter une information\n"
                    "5.Modifier une information invalide\n"
                    "6.Quitter"
                    "Veuillez faire votre choix: "))
    while choix in [1,2,3,4,5]:
        if choix ==1:
            c=str(input("a.Informations valides\n"
                        "b.Informations invalides\n"))
            if c =='a':
                data = open('project_data.json','r') 
                donnees = json.load(data)
                val,inval=choix_json(donnees)
                json_to_csv(val)
    if choix==6:
        exit

