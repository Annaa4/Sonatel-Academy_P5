def saisie(a):
    prenom = str(input('Prenom: '))
    nom = str(input('Nom: '))
    telephone = str (input('Telephone : '))
    booleen = verification_number(telephone)
    while booleen == False :
        print ("Vous n'avez pas saisi un bon numero")
        telephone = str(input('Telephone : '))
        booleen = verification_number(telephone)
    classe = str(input('Classe: '))
    dev = float(input('Devoir : '))
    while dev > 20 or dev <0:
        dev = float(input('Devoir : '))
    proj= float(input('Projet : '))
    while proj > 20 or proj <0:
        proj = float(input('Projet : '))
    exam = float(input('Examen : '))
    while exam > 20 or exam <0:
        exam = float(input('Devoir : '))
    moyenne = calcul_moyenne(dev,proj,exam)
    a.append([prenom,nom,telephone,classe,dev,proj,exam,moyenne]) 
    choix = str(input('Voulez-vous continuez ? : oui/non\n'))
    while choix =="oui": 
        return saisie(a)  

def verification_number(a):
    c = ['0','1','2','3','4','5','6','7','8','9']
    second_indice=['0','7','8','6','5']
    t = []
    s=''
    for i in range (len (a)) :
        if a[i] in c :
            s = s + a[i]
    t.append (s)
    for num in t:
        if len(num)> 9 or len(num) < 9 or num[0] !='7' or num[1] not in second_indice:
            return False
        else:
            return True
            
def calcul_moyenne(a,b,c):
    m=(a+b+c)/3
    return m
# saisie(tab)
# print("-"*110)
    # h=['Prenom','Nom','Téléphone','Classe','Dev','Proj','Exam','Moyenne']
    #     for a in h:
    #        for k in a:
    #     print("|",k," "*10, end ="")
def affichage(a):
    print("-"*130)
    for i in a:
        for j in range (len(i)):
            print("|",i[j], end =(15-len(str(i[j])))*" ")
        print('\n')
    print("-"*130)

def recherche(a,tab):
    for i in tab:
        if a in i: 
            for j in range (len(i)):
                print("|",i[j], end =(15-len(str(i[j])))*" ")

def modification(a,tab):
     for i in tab: 
        if i[2] == a:
            dev = float(input('Devoir : '))
            while dev > 20 or dev <0:
                dev = float(input('Devoir : '))
            proj= float(input('Projet : '))
            while proj > 20 or proj <0:
                    proj = float(input('Projet : '))
            exam = float(input('Examen : '))
            while exam > 20 or exam <0:
                    exam = float(input('Devoir : '))
            moyenne = calcul_moyenne(dev,proj,exam)
            i[4]=dev
            i[5]=proj
            i[6]=exam
            i[7]=moyenne
            for j in range (len(i)):
                print("|",i[j], end =(15-len(str(i[j])))*" ")

def tri(a):
        for i in range(2,len(a)) :
            k = a[i]
            u=i-1
            b=a[u]
            t = b[7]
            l=k[7]
            c = []
            while  u >= 1 and l>t:
                a[u + 1] = a[u]
                u = u - 1
            a[u+1]= k
        affichage(a)