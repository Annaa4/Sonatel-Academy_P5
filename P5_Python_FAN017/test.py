import csv
import fonctions
with open('donnees_projet_python.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    data = [row for row in csvreader]
    valide=[]
    invalide=[]
    list=[]
    for dt in data:
        numero=fonctions.numero(dt[1])
        #print(numero)
        nom=fonctions.nom(dt[2])
        prenom=fonctions.prenom(dt[3])
        date=fonctions.validdate(dt[4])
        classe=fonctions.definirFormatClasse(dt[5])
        if classe == False:
            continue
        cl=fonctions.classeValide(classe)
        note=fonctions.note(dt[6])
        list.append(dt[1])
        list.append(dt[2])
        list.append(dt[3])
        list.append(dt[4])
        list.append(classe)
        list.append(note)
        if (numero==True and nom==True and prenom==True and date==True and cl==True and note !=False):
            valide.append(list)
            list=[]
        else:
            invalide.append(list)
            list=[]
    for line in valide:
        print(line[5])
def affichage(a):
    print("-"*130)
    for i in a:
        for j in range (len(i)):
            print("|",i[j], end =(15-len(str(i[j])))*" ")
        print('\n')
    print("-"*130)
    print(len(a))
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
        affichage((valide))
    elif c=='b':
        affichage((invalide))
  elif choix == 2:
    c=(input("Entrer le numéro de l'étudiant : "))
    fonctions.affichage_d_une_information(c,valide)
    fonctions.affichage_d_une_information(c,invalide)
  elif choix == 3:
        fonctions.moyenne_generale(fonctions.note(valide[6]))
  elif choix == 4:
    fonctions.ajout_nouvelle_information(list)
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