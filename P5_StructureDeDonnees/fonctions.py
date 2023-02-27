import datetime
#Verification du numero
def numero(a):
    if len(a)==7:
        if a.isalnum()==True:
            if a.isupper()==True:
                if any(cl.isdigit() for cl in a) == True:
                        return True
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
        date=date.strip()
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
# def validation_date(a):


#         a=a.strip()
#         for i in a: 
#             if not i.isalnum():
#                 a=a.replace(i,'/')          
#         b=a.split('/')
#         print("rrrrr",b)
#         #CORRESPONDANCE DES MOIS EN CHIFFRE
#         month={"jan":'1',"fev":'2',"mars":'3',"avr":'4',"mai":'5',"juin":'6',"juillet":'7',"Dec":'12'}
#         for mois in month.keys():
#             if b[1].lower().startswith(mois):
#                 b[1]=month[mois]
#                 break

#         for i in b[0] :
#             if not i.isnumeric():
#                 return False
#         for i in b[1] :
#             if not i.isnumeric():
#                 return False
#         for i in b[2] :
#             if not i.isnumeric() :
#                 return False
#         j=b[0]
#         m=b[1]
#         an=b[2]
        
        
#         j=int(j)
#         m=int(m)
#         an=int(an)
#         if 00<=an<=23:
#             an=an+2000
#         elif 25<=an<=99:
#             an =an +1900

        
#         try:
#             d=datetime.datetime(an,m,j)
            
#             # e=d.strftime("%d/%m/%y")
#             # print(e)            
#             return True
#         except:
#             return False

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
n='Math[11;13:06] #Francais[08;17:12] #Anglais[13;13:12] #PC[09;18:07] #SVT[15;10:10] #HG[14;19:17]'
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

