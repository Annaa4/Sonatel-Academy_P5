phrase = (input("Entrer votre phrase"))
m = {'a':'2','b':'22','c':'222','d':'3','e':'33','f':'333','g':'4',
     'h':'44','i':'444','j':'5','k':'55','l':'555','m':'6','n':'66',
     'o':'666','p':'7','q':'77','r':'777','s':'7777','t':'8','u':'88',
     'v':'888','w':'9','x':'99','y':'999','z':'9999', ' ':'00',
     'A':'2','B':'22','C':'222','D':'3','E':'33','F':'333','G':'4',
     'H':'44','I':'444','J':'5','K':'55','L':'555','M':'6','N':'66',
     'O':'666','P':'7','Q':'77','R':'777','S':'7777','T':'8','U':'88',
     'V':'888','W':'9','X':'99','Y':'999','Z':'9999',',':',',"'":"'",
     '1':'B','2':'C','3':'D','4':'E','5':'F','6':'G','7':'H','8':'I','9':'J'}
r=[]
t=[]
for p in phrase:
    for i in m :
        if p == i :
            r.append(m[i])

t.append(r[0])
for i in range(1,len(r)): 
    a=r[i-1]
    b=r[i]
    if a[len(a)-1]==b[0]:
        t.append('0')
    t.append(r[i])


for i in t:
    print(i,end="")