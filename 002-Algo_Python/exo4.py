numero = 'ncghcgxbnjoikbvxfb77182610578654327kjbftcvghb8897542467hgjhxyfc776487690fhufdt34586563798'

# def espaces(a):
#     t=''
#     for i in range(len(a)):
#         if not (a[i] ==" "):
#             t=t+a[i]
#     return t 
# num1= espaces(numero)
# print(num1)
def recuperation(a):
    s = []
    p=0
    for i in range (len(a)):
        if a[i] in numero:
            x = a[p:i+1]
            if ((len(x) == 9)):
                s.append(x)
                p = i+1
    return s
num2 = recuperation(numero)
print (num2)

def num_valide(a):
    nv = []
    ni = []
    for i in range (len(a)):
        if (a[i] >= '0' and a[i]<= '9'):
            nv.append(a[i])
        elif a[i] :
            ni.append(a[i])
    return nv,ni
num3 = num_valide(num2)
print(num3)
    

