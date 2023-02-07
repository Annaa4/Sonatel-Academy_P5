phrase = str(input("Entrez vos phrases"))
while phrase == "":
    input ("Entrer vos phrases:\n") 

def espaces_inutiles(x):
    o=""
    for i in range(len(x)):
        if not (x[i] ==" " and x[i+1]== " "):
            o=o+x[i]
    return o 

ph_1= espaces_inutiles(phrase)
print(ph_1)


def caracteres_speciaux(x):
    a = ''
    for i in range (len(x)):
        if ((x[i] >= 'A' and x[i] < 'Z') or(x[i] >= 'a' and x[i] < 'z') or(x[i] in [",","'",":"," ",";","|","()","/","-","é"])):
            a =a+x[i]
    return a 
n = caracteres_speciaux(ph_1)
print(n)
    
def recuperation_des_phrases(x):
    t=[]
    a=0
    for i in range (len(x)) : 
        if(x[i] in [".","!","?"]):
           g = x[a:i+1]
           if len(g)>=25:
               t.append(g) 
               a = i+1    
    return t

v=recuperation_des_phrases(n)
print(v)