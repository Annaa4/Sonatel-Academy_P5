p = str (input("Veuiller entrer votre phrase"))
p1=""
for i in range (0, len(p)):
    if p [i] == " " and p[i+1] == " ":
     pass 
    else :
        p1 = p1+p[i]
print (p)
print(p1) 