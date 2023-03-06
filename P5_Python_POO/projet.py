#Programme écrit en utilisant les listes
import csv
from fonctions_poo import Etudiant
with open('donnees_projet_python.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    data = [i for i in csvreader]
    valide=[]
    invalide=[]
    list=[]
    for dt in data:
        etudiant=Etudiant(dt[1],dt[2],dt[3],dt[4],dt[5],dt[6])
        numero=etudiant.verification_numero(dt[1])
        nom = etudiant.verification_nom(dt[2])
        prenom = etudiant.verification_prenom(dt[3])
        date=etudiant.date_valide(dt[4])
        if date == False:
            continue
        classe=etudiant.definirFormatClasse(dt[5])
        if classe == False:
            continue
        cla=etudiant.classeValide(classe)
        no=etudiant.verification_note(dt[6])  
        list.append(dt[1])
        list.append(dt[2])
        list.append(dt[3])
        list.append(date)
        list.append(classe)
        list.append(no) 
        if (numero==True and nom==True and prenom==True and date!=False and cla==True and no!=False ):
            valide.append(list)
            list=[]
        else:
            invalide.append(list)
            list=[]
    print("fghjkl")
    for line in valide:
     print(len(valide))

# def affichage(a):
#     print("-"*130)
#     for i in a:
#         for j in range (len(i)):
#             print("|",i[j], end =(15-len(str(i[j])))*" ")
#         print('\n')
#     print("-"*130)