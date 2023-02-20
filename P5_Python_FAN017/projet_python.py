import csv
import fonctions
with open('/home/anna/Téléchargements/Donnees_Projet_Python_DataC5.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    data = [i for i in csvreader]
    
    for dt in data:
        print(fonctions.note(dt))
        # # for u in dt:
        # print("===========================================================")
        # # print(dt)
        # print("===========================================================\n\n")
    exit()
    #Verification du numero:
    num = fonctions.numero(data)
    Tab1=[]
    for i in data[0][6]:
        for j in i:
            print (i[j])
        # for j in i :
            # if num == True:
            #     Tab1.append(num)
            #     print(Tab1)
            
        # fonctions.note(data[0][6])

#voulez-vous afficher ?\n a: Notes valides\n b:Notes invalides\n
# choix=int(input("                       MENU\n 1.Afficher les informations\n 2. Afficher une information\n 3.Afficher les cinq premiers étudiants\n 4.Ajouter une nouvelle information\n 5.Modifier une information\n 6.Quitter\n "))
# while choix in [1,2,3,4,5]:
#   if choix ==1:


#     choix=int(input("                       MENU\n 1.Afficher les informations\n 2. Afficher une information\n 3.Afficher les cinq premiers étudiants\n 4.Ajouter une nouvelle information\n 5.Modifier une information\n 6.Quitter\n "))
# numero(data)
# print(data) 
