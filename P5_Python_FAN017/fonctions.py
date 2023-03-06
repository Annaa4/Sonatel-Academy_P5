import datetime
#Verification du numero
def numero(a):
    if len(a)==7 and a.isalnum() and a.isupper() and any(cl.isdigit() for cl in a)==True:
     return True
    else:
     return False
# Verification du nom
def nom(a):

        if len(a) < 2 or not a.isalpha():
            return False
        else:
            return True

#Verification du prenom
def prenom(a):
        if len(a) < 2 or not a.isalpha():
         return False
        else:
         return True
#Verification de la date de naissance
def validdate(date):
    try:
        date=date.strip('#')
        date=date.replace(' ','/').replace('-','/').replace('_','/').replace(',','/').replace('|','/').replace(':','/').replace('.','/').replace('mars','03').replace('fev','02').replace('decembre','12')
        for i in date:
            cl=date.split('/')
        if cl[0].isdigit():
            dd=int(cl[0])

        if cl[1].isdigit():
            mois=int(cl[1])

        if cl[2].isdigit():
            an=int(cl[2])
        d=datetime.datetime(an,mois,dd).strftime('%d/%m/%y')
        return True
    except:
        return False

# Verification de la classe
def definirFormatClasse(classe):
    cl =""
    if classe == "" or classe == " ":
        return False
    else:
        cl = classe[0]+" "+"iem"+" "+classe[len(classe) - 1]
    return cl
#print(definirFormatClasse(" "))

def classeValide(cl):
    classValide=""
    if cl[0] in ["6","5","4","3"] and cl[len(cl) - 1] in ["A","B"]:
        classValide += cl
        return True
    else:
        return False
# Verification de la note
def note(a):
    # print(a)
    tab=[]
    for matiere in a.split('#') :
        matiere=matiere.replace('[',':').replace(';',':').replace(',','.').replace(']',':')
        matiere=matiere.split(":")
        del matiere[len(matiere)-1]
        s=0
        nbr=0
        moy=1
        so=0
        somme=0
        moyg=0
        if matiere==""  or matiere==" " or len(matiere)<= 1:
            return False
        # print("dddd",matiere)
        for i in range (1,len(matiere)):
            for c in matiere[i]:
                if c not in["0","1","2","3","4","5","6","7","8","9","."]:
                    return False
        for j in range(len(matiere)):
            if matiere[j]=="" or matiere[j]==" ":
                matiere[j]=matiere[j].replace("",'0.0').replace(" ",'0.0')
        for j in range (1,len(matiere)-1):
            s+=float(matiere[j])
            nbr+=1
        moy=round(((s/nbr)+2*float(matiere[-1]))/3,2)
        if (moy) > 0 and (moy) <=20:
            matiere.append(moy)
            tab.append(matiere)
    return tab

def moyenne_generale(donne):
    moyg=1
    somme = 0
    for line in donne:
        #print(line[len(line)-1])
        somme += float(line[len(line)-1])
    moyg = round((somme/len(donne)),2)
    return moyg
# n='Math[11;13:06] #Francais[08;17:12] #Anglais[13;13:12] #PC[09;18:07] #SVT[15;10:10] #HG[14;19:17]'
# m=note(n)
# #print(m)
# print(moyenne_generale(m))
    # a.append(moyg)
    # return a

#def affichage_cinq_premiers(a):
#     etu=sorted( a, key=lambda o:o[-1],reverse=True)
#     for i in range(5):


#Affichage d'une information selon le numero
def affichage_d_une_information(a,tab):
    bool=False
    for i in tab:
        if a in i:
            bool=True
            for j in range (len(i)):
                print("|",i[j], end =(15-len(str(i[j])))*" ")
    if bool==False:
        print("L'étudiant n'est pas sur la liste")

#Ajout d'une nouvelle information selon les critères de validité
def ajout_nouvelle_information(a):
    #Ajout du numero
    nume=str(input("Numero : "))
    nu=numero(nume)
    while nu == False:
        print('Veuillez entrer un bon numero')
        nume=input('Numero')
        nu=numero(nume)
    #Ajout du nom
    name=str(input("Nom : "))
    n=nom(name)
    while n == False:
        print('Veuillez entrer un bon nom')
        name=str(input("Nom : "))
        n=nom(name)
    #Ajout du prenom
    pren=str(input("Prenom : "))
    p=prenom(pren)
    while p == False:
        print('Veuillez entrer un bon prenom')
        pren=str(input("Prenom : "))
        p=prenom(pren)
    #Ajout de la date de naissance
    d=str(input("Date de naissance : "))
    da=validdate(d)
    while da == False:
        print('Veuillez entrer une bonne date de naissance')
        d=str(input("Date de naissance : "))
        da=validdate(d)
    #Ajout de la classe
    c=str(input("Entrer une classe : "))
    c1=definirFormatClasse(c)
    if c1 == False:
        pass
    c2 =classeValide(c1)
    while c2 == False:
        print("Veuiller entrer une bonne classe")
        c=str(input("Entrer une classe : "))
        n1=definirFormatClasse(c)
        if c1 == False:
            pass
        c2 =classeValide(n1)
    #Ajout des notes
    no=str(input("Entrer les notes: "))
    nt=note(no)
    while nt == False:
        print("Veuillez entrer de bonnes notes")
        no=str(input("Entrer les notes: "))
        nt=note(no)
    a.append(nume)
    a.append(name)
    a.append(pren)
    a.append(d)
    a.append(c)
    a.append(no)