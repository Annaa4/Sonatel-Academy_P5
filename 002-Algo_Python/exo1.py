mois =  [["Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin","Juillet", "Aout","Septembre","Octobre","Novembre","Decembre"],
["January", "February", "March", "April","May", "June", "July", "Aout", "SEptember", "Ocotber", "November", "Decembrer"]]
def mois_f (a):
    for k in range(3):
        for i in range (k, 12, 3):
            print ("|" , mois[a][i]+" "*(20 - len(mois[a][i])), end ="")
        print ("\n")
choix = int (input("Veuillez faire votre choix :\n 1. Mois en français\n 2. Mois en anglais\n 3. Quitter\n"))
if choix == 1: mois_f(0)
elif choix == 2: mois_f(1)          