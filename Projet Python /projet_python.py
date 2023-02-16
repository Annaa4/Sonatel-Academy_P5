import csv
import fonctions
with open('/home/anna/Téléchargements/Donnees_Projet_Python_DataC5.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    data = [i for i in csvreader]
for i in range(len(data)-1):
    print (fonctions.numero(data[1]))



#     print(i['CODE'], i['Numero'], i['Nom'], i['Prénom'], i['Date de naissance'], i['Classe'], i['Note'])

#voulez-vous afficher ?\n a: Notes valides\n b:Notes invalides\n
# choix=int(input("                       MENU\n 1.Afficher les informations\n 2. Afficher une information\n 3.Afficher les cinq premiers étudiants\n 4.Ajouter une nouvelle information\n 5.Modifier une information\n 6.Quitter\n "))
# while choix in [1,2,3,4,5]:
#   if choix ==1:


#     choix=int(input("                       MENU\n 1.Afficher les informations\n 2. Afficher une information\n 3.Afficher les cinq premiers étudiants\n 4.Ajouter une nouvelle information\n 5.Modifier une information\n 6.Quitter\n "))
# numero(data)
# print(data)
