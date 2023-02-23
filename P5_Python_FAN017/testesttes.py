import csv
import fonctions
with open('./Donnees_Projet_Python_DataC5.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    data = [i for i in csvreader]
    for dt in data:
        print(dt[4])