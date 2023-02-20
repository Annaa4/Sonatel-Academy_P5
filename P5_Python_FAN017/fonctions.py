#Verification du numero
def numero(a):
        if len(a[1]) != 7 or not (a[1].isdigit() or a[1].isupper()):
            return False
        return True

# Verification du nom
def nom(a):
        if len(a[2]) < 2 or not a[2].isalpha():
            return False
        else:
            return True

#Verification du prenom
def prenom(a):
    for i in a :
        if len(a[3]) < 2 or not a[3].isalpha():
         return False
        else:
         return True
#Verification de la date de naissance
def date_de_naissance_valide(a):
    from datetime import datetime 
    date=a[4]
     #Changement du format de la date de naissance
    for p in date :
        if not p.isalnum():
            s=date.replace(p,"/")
        return date
     #Validité date de naissance 
    
# Verification de la classe
def classe(a):
    t=[]
    if a[0] in ["3","4","5","6"] and a[-1] in ["A","B"]:
            t.append(a[0]+"e"+a[-1])
            for i in t:
                print(i)
    else :
            print("La classe n'est pas valide")
    return t

# Verification de la note 
def note(a):
    # print(a)
    tab=[]
    for matiere in a[6].split('#') :
        matiere=matiere.replace('[',':').replace(';',':').replace(',','.').replace(']',':')
        matiere=matiere.split(":")
        del matiere[len(matiere)-1]
        s=0
        nbr=0
        moy=1
        try:
            for j in range (1,len(matiere)-1):
                if matiere[j].isdigit():
                    s+=float(matiere[j])
                    nbr+=1
                moy=round(((s/nbr)+2*float(matiere[-1]))/3,2)
                matiere.append(moy)
            print(matiere)
        except:
            return False
    

