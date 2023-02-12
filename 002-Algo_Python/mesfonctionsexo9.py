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
def affichage_client(o,a):
        print(o)
        if o == "orange":
            for j in a :
                for k in j:
                   if k[0] == '7' and (k[1]== '7' or k[1]== '8' ) and len(k) == 9:
                    print(j)
        elif o == "tigo":       
            for j in a :
                for k in j:
                   if k[0] == '7' and k[1]== '6' and len(k) == 9:
                    print(j)
        elif o == "expresso":
            for j in a :
                for k in j:
                   if k[0] == '7' and k[1]== '0' and len(k) == 9:
                    print(j) 
def affiche_numero(n,p,a): 
    print("Les numeros de ", p," " ,n)
    for i in a:
        if p in i  and n in i:
            print(i[2])
def modification(n,p,a):
    modif = input("Modifier le client\n Ajouter un client\n")
    if modif == 'ajouter':
        nom = n
        prenom = p
        telephone =(input("Donner le numéro du client : "))
        a.append ([nom,prenom,telephone])
    elif modif == 'modifier':
        h = 0
        for i in a :
            if p in i and n in i and h <1 :
                telephone =(input("Donner le nouveau numéro du client : "))
                i[2] = telephone
                h+=1
            elif p in i and n in i and h >=1:
                choix=(input("Voulez-vous modifier ce numéro ? : oui/non"))
                if choix == 'oui':
                    telephone =(input("Donner le nouveau numéro du client : "))
                    i[2] = telephone
                    h+=1
                else:
                    break


