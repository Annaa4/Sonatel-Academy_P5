#Verification du numero
def numero(a):
    if len(a) != 7:
        return False
    for c in a:
        if not (c[1].isdigit() or c[1].isupper()):
            return False
    return True
# b=numero('1ZZSERD')
# print(b)
       
# Verification du nom
def nom(a):
    if len(a) < 2 or not a[0].isalpha():
     return False
    else:
     return True
# b=nom('AZERTY')
# print(b)

# #Verification du prenom
def prenom(a):
    if len(a) < 2 or not a[0].isalpha():
     return False
    else:
     return True
def date_de_naissance_valide(a):
    from datetime import datetime 
    date=''
     #Changement du format de la date de naissance
    for p in a :
        if p not in ["0","1","2","3","4","5","6","7","8","9"]:
            date=date+"-"
        else:
            date+=p
    # Validité date de naissance 
    try:
        datetime.strptime(date, '%d-%m-%Y')
        return True
    except ValueError:
        return False
    
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
    s=a.split(" ")
    print(s)

