import csv
import fonctions
with open('./Donnees_Projet_Python_DataC5.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    data = [i for i in csvreader]
    # print(data)
    valideglo=[]
    invalideglo=[]
    valide=[]
    invalide=[]
    for dt in data:
        numero=fonctions.numero(dt[1])
        #print(numero)
        nom=fonctions.nom(dt[2])
        prenom=fonctions.prenom(dt[3])
        date=fonctions.validdate(dt[4])
        classe=fonctions.definirFormatClasse(dt[5])
        if classe == False:
            continue
        cl = fonctions.classeValide(classe)
        note=fonctions.note(dt[6])
        if (numero==True and nom==True and prenom==True and date==True and cl==True and note !=False):
            valide.append(dt[1])
            valide.append(dt[2])
            valide.append(dt[3])
            valide.append(dt[4])
            valide.append(classe)
            valide.append(note)
            valideglo.append(valide)
            valide=[]
        else:
            invalide.append(dt[1])
            invalide.append(dt[2])
            invalide.append(dt[3])
            invalide.append(dt[4])
            invalide.append(classe)
            invalide.append(note)
            invalideglo.append(invalide)
            invalide=[]
def affichage(a):
    print("-"*130)
    for i in a:
        for j in range (len(i)):
            print("|",i[j], end =(15-len(str(i[j])))*" ")
        print('\n')
    print("-"*130)
# for dt in invalide:
#     print('==========================================================================================')
#     print(dt)
#     print('==========================================================================================')

choix=int(input('           MENU\n' 
                '1.Afficher les informations\n' 
                '2.Afficher une information\n' 
                '3.Afficher les cinq premiers étudiants\n' 
                '4.Ajouter une nouvelle information\n'
                '5.Modifier une information\n' 
                '6.Quitter\n '
                'Veuillez faire votre choix : '))
while choix in [1,2,3,4,5]:
  if choix ==1:
    c = (input('a.Afficher les informations valides\n'
             'b.Afficher les informations invalides\n'))
    if c =='a':
        affichage((valideglo))
    elif c=='b':
        affichage((invalideglo))

    choix=int(input('           MENU\n' 
                '1.Afficher les informations\n' 
                '2.Afficher une information\n' 
                '3.Afficher les cinq premiers étudiants\n' 
                '4.Ajouter une nouvelle information\n'
                '5.Modifier une information\n' 
                '6.Quitter\n '
                'Veuillez faire votre choix\n'))
    if choix==5:
        exit
# for i in invalideglo:
#  print('===============================================================================')   
#  print(i)
#  print('===============================================================================')   
# print(len(invalideglo))