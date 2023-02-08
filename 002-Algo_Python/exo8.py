# prenom = str(input("Donner votre prenom"))
# nom = str(input("Donner votre nom"))
telephone = str (input("Donner votre numero"))
# classe =str(input("Donner votre classe"))
# devoir= int(input("Donner la note de devoir"))
# projet =int(input("Donner la note de projet"))
# exam=int(input("Donner la note d'examen"))
def recuperation_telephone(a):
    for i in range (len(a)):
        s = []
        p=0
        if a[i] in telephone:
            x = a[p:i+1]
            if ((len(x) == 9)):
                s.append(x)
                p = i+1
    return print("Telephone\n",s)
tel= recuperation_telephone(telephone)
print(tel)