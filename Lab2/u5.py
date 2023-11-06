#Filtern durch eine Fromel

def beziehung_ziffern(l,s):
    nl=[]

    for i in range(len(l)):
        x=l[i]//10
        y=l[i]%10
        if eval(s)==True:
            nl.append(l[i])

    return nl

l=[26,33,62,93]
s="x/y==3"
print(beziehung_ziffern(l,s))