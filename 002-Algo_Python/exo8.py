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
    choix = (input('Voulez-vous continuez ? : oui/non'))
    r=[]
    while choix=='oui': 
        saisie(r)
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
tab = [['Prenom','Nom','Téléphone','Classe','Dev','Proj','Exam','Moyenne']]
saisie(tab)
print(tab)