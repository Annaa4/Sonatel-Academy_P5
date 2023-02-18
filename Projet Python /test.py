t = 'Math[10;11:15] #Francais[7;12;8:13] #Anglais[13,5;9:15] #PC[11:9]  #SVT[12;9;16;11:12]  #HG[10:13]'
# Verification de la note
def note(a):
    a = a.split('#')
    # print(a)
    for matiere in a :
        matiere=matiere.replace('[',':').replace(';',':').replace(',','.').replace(']',':')
        matiere=matiere.split(":")
        del matiere[len(matiere)-1]
        s=0
        nbr=0
        moy=1
        for j in range (1,len(matiere)-1):
            s+=float(matiere[j])
            nbr+=1
        moy=((s/nbr)+2*float(matiere[-1]))/3
        print (matiere)
        print(moy)
note(t)



# for i in a:
#     i=i.split("[")
#     if len(i)==2:
#         mat=i[0]
#         note =i[1][:-1]
#     print(mat)
    # print(note)
# for i in range (0,len(a)):
#     note=a[i].split('[')
#     if len(note)==2:
#         matiere = note[0]
#         notes = note[1][:-1]
#     print(notes)