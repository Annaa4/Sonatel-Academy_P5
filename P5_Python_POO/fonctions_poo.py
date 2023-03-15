import datetime
class Etudiant:
    def __init__(self,num,name,pren,date_de_naissance,classe_etudiant,note_etudiant):
        self.numero = num
        self.nom = name
        self.prenom = pren 
        self.date = date_de_naissance
        self.classe = classe_etudiant
        self.note = note_etudiant
    
    def verification_numero(self,numero):
        if len(self.numero) == 7 and self.numero.isalnum() and self.numero.isupper() and any(caractere.isdigit() for caractere in self.numero):
            return True
        else:
            return False
    #Syntaxe appel de la methode pour vérifier un numero 
# numero_etudiant=Etudiant('FD434DDF')
# numero_etudiant.verification_numero()
# print(numero_etudiant.verification_numero())

    def verification_nom(self,nom):
        if len(self.nom) < 2 or not self.nom.isalpha():
            return False
        else:
            return True
        
    def verification_prenom(self,prenom):
        if len(self.prenom)<2 or not self.prenom.isalpha():
            return False
        else:
            return True
        
    def date_valide(self,date):
        try:
            self.date=self.date.strip()
            self.date=self.date.replace(' ','/').replace('-','/').replace('_','/').replace(',','/').replace('|','/').replace(':','/').replace('.','/').replace('mars','03').replace('fev','02').replace('decembre','12')
            for i in self.date:
                cl=self.date.split('/')
            if cl[0].isdigit():
                dd=int(cl[0])

            if cl[1].isdigit():
                mois=int(cl[1])
            
            if cl[2].isdigit():
                an=int(cl[2])
            d=datetime.datetime(an,mois,dd).strftime('%d/%m/%y')
            return d
        except:
            return False
   
    def definirFormatClasse(self,classe):
        cl =""
        if self.classe == "" or self.classe == " ":
            return False
        else:
            cl = self.classe[0]+" "+"iem"+" "+self.classe[len(self.classe) - 1]
        return cl
    #print(definirFormatClasse(" "))

    def classeValide(self,cl):
        classValide=""
        if cl[0] in ["6","5","4","3"] and cl[len(cl) - 1] in ["A","B"]:
            classValide += cl
            return True
        else:
            return False
# class Matiere:
    def verification_note(self,note):
    # print(a)
        tab=[]
        for matiere in self.note.split('#') :
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
# d=Etudiant('Anna')
# print(nom_etudiant.verification_nom())




