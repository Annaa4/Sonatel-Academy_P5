def saisie(a):
    nombre = int (input("Donner le nombre d'opérateurs"))
    for i in range (nombre):
        operateur =(input("Choississez votre opérateur : "))
        a.append (operateur)
    client = int (input("Donner le nombre de clients : "))
    for i in range (client):
        nom = str(input("Donner le nom du client"))
        prenom = str (input("Donner le prenom du client : "))
        telephone = str (input("Donner le numéro du client : "))
        a.append([nom,prenom,telephone])
def affichage(a):
    for i in a : 
        if i == "orange":
            print(i)
            for j in a :
                for k in j:
                   if k[0] == '7' and (k[1]== '7' or k[1]== '8' ) and len(k) == 9:
                    print(j)
        elif i == "tigo":
            print(i)
            for j in a :
                for k in j:
                   if k[0] == '7' and k[1]== '6' and len(k) == 9:
                    print(j)
        elif i == "expresso":
            print(i)
            for j in a :
                for k in j:
                   if k[0] == '7' and k[1]== '0' and len(k) == 9:
                    print(j)
tab = []
saisie(tab)
affichage(tab)
