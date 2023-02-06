numero = int(input("Entrer vos numeros"))
def num_valide(a):
    for p in numero:
        if p[0] in [7] and p[1] in [0,7,8]:
            return p 
