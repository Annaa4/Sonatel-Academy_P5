# phrase = (input("Entrer votre phrase"))
phrase = 'bonjour aly'
m = {'a':'2','b':'22','c':'222','d':'3','e':'33','f':'333','g':'4',
     'h':'44','i':'444','j':'5','k':'55','l':'555','m':'6','n':'66',
     'o':'666','p':'7','q':'77','r':'777','s':'7777','t':'8','u':'88',
     'v':'888','w':'9','x':'99','y':'999','z':'9999', ' ':'00'}
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


