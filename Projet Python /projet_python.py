import csv
a = open ("/home/anna/Téléchargements/Donnees_Projet_Python_DataC5.csv")
myReader = csv.reader(a)
for row in myReader :
    print(row)