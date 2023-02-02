phrase = str(input("Entrer vos phrases:\n")) 
while phrase == "":
    input ("Entrer vos phrases:\n")
    
def recuperation_des_phrases():
    for p in phrase :
        p = p + phrase
        if((p >='A' or p <='Z') and (p in [".","!","?"])):
           pass
        else:
            
         print (p)

def caracteres_speciaux() :
    p1=""
    for i in range (0, len(phrase)):
        if phrase[i] == " " and phrase[i+1] == " ":
            pass 
        else :
            p1 = p1+phrase[i]
    print (phrase)
    print(p1) 