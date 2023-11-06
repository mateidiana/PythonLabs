#1a Generieren Sie alle Primzahlen, die kleiner als eine naturliche Zahl n sind
print("Ubung 1a")
def primz(n):
    l=[]                          #die Liste ist anfangs leer
    for i in range(1,n):          #man geht alle Elemente von 1 bis n-1 durch und pruft ob sie prim sind
        ok=1
        if i<=1:
            ok=0                  #die Zahlen kleiner als 2 sind nicht prim
        if i==2:
            ok=1                  #2 ist Primzahl
        for j in range(2,i//2+1):
            if i%j==0:
                ok=0              #wenn man einen Teiler der Zahl zwischen 2 und i/2 findet, ist diese nicht prim
                break
        if ok==1:
            l+=[i]                #Primzahlen werden in der Liste eingefugt
    return l

# print("Geben Sie eine naturliche Zahl n ein:")
# n=int(input("n="))
# print("Alle Primzahlen,die kleiner als ",n," sind:")
# print(primz(n))

#1b Gegeben sei ein Vektor von Zahlen, finden Sie die langste ansteigende zusammenhangende Teilfolge
print("Ubung 1b")
def stteilf(l):
    nl=[]                               #die Teilfolge ist anfangs eine leere Liste
    ct=0
    i=0
    maxinf=0                            #Anfangsindizes der langsten Teilfolge
    maxsup=0                            #Endindizes der langsten Teilfolge

    while ct<len(l)-1:                  #man geht alle Elemente des Vektors durch
        inf=ct                          #das erste Element jeder Teilfolge

        while l[i]<l[i+1] and i<len(l)-2:
            i=i+1                           #solange die Elemente steigend sind wird zu der Lange addiert
                                            #das vorvorletzte und das vorletzte Element werden zuletzt verglichen

        if i==len(l)-2 and l[i]<l[i+1]:     #das vorletzte und das letzte Element werden verglichen
            i=i+1

        sup=i  #Endindizes der kurrenten Teilfolge
        ct=i+1 #Anfangsindizes der nachsten Teilfolge
        i=i+1  #Anfangsindizes der nachsten Teilfolge

        if sup-inf>maxsup-maxinf: #falls die kurrente Lange grosser ist als die vorige werden die Maximumwerte ersetzt
            maxsup=sup
            maxinf=inf

    nl=l[maxinf:maxsup+1]  #die langste Teilfolge ubernimmt die Elemente auf den entsprechenden Positionen
    return nl

# print("Geben Sie die Anzahl der Elemente aus dem Vektor ein:")
# n1=int(input("n="))
# a=[]
# print("Geben Sie die Elemente ein:")
# for i in range(0,n1):
#     print("l[",i,"]= ")
#     m=int(input())
#     a+=[m]
# #a=[1,2,3,1,2,3,4,5,1]

# print("Die langste steigende Teilfolge ist:")
# print(stteilf(a))


#5a Schreiben Sie eine Funktion, welche den Exponenten einer Primzahl p aus der Zerlegung in
#Primfaktoren einer gegebenen naturlichen Zahl n auf dem Bildschirm ausgibt
print("Ubung 5a")
def primf(n,p):
    d=2 #der Teiler (Primzahl)
    p1=0 #der Exponent, zu dem die Primzahl erscheint
    while(n%d==0):    #die Zahl wird zuerst durch 2 geteilt
        n=n/d
        p1=p1+1
    if (p==d):
        return p1 #falls die gegebene Primzahl 2 ist, wird der Exponent angeschrieben
    else:
        p1=0
        d=3
        while(n!=0):
            while(n%d==0): #die Zahl wird durch die nachsten Primzahlen beginnend von 3 geteilt
                n=n/d
                p1=p1+1
            if p==d:
                return p1 #falls die gegebene Primzahl der kurrente Teiler ist, wird der Exponent angeschrieben
            d=d+2 #man geht zu dem nachsten ungeraden Teiler weiter
            p1=0  #fur jeden Teiler wird der Exponent mit 0 initialisiert

# print("Geben Sie eine naturliche Zahl n und eine Primzahl p ein:")
# n2=int(input("n="))
# p2=int(input("p="))
# print("Der Exponent der Zahl p aus der Zerlegung in Primfaktoren der Zahl n ist:")
# print (primf(n2,p2))

#5b Gegeben sei eine Reihe von Zahlen, finden Sie die langste zusammenhangende Teilfolge so, dass
#alle 2 beliebige aufeinanderfolgende Elemente relativ prim sind
print("Ubung 5b")

#Funktion fur das Berechnen des GGTs
def cmmdc(x,y):
    if (x==0 and y==0):
        return 2          # 0 und 0 sind nicht relativ prim
    else:
        if (x==0 and y!=0):   #GGT von 0 und n ist n
            return y
        else:
            if (y == 0 and x != 0):
                return x
            else:
                while x != y:       #Algorithmus von Euklid
                    if x > y:
                        x = x - y
                    else:
                        y = y - x
                return x


def relativprim(l):
    nl = []        #die Teilfolge ist anfangs eine leere Liste
    ct = 0
    i = 0
    maxinf = 0     #Anfangsindizes der langsten Teilfolge
    maxsup = 0     #Endindizes der langsten Teilfolge

    while ct < len(l) - 1:     #man geht alle Elemente des Vektors durch
        inf = ct                #das erste Element jeder Teilfolge

        while cmmdc(l[i],l[i + 1])==1 and i < len(l) - 2:
            i = i + 1     #solange die Elemente relativ prim sind wird zu der Lange addiert
                          # das vorvorletzte und das vorletzte Element werden zuletzt verglichen

        if i == len(l) - 2 and cmmdc(l[i],l[i + 1])==1:
            i = i + 1     #das vorletzte und das letzte Element werden verglichen

        sup = i     #Endindizes der kurrenten Teilfolge
        ct = i + 1  #Anfangsindizes der nachsten Teilfolge
        i = i + 1   #Anfangsindizes der nachsten Teilfolge

        if sup - inf > maxsup - maxinf:  #falls die kurrente Lange grosser ist als die vorige werden die Maximumwerte ersetzt
            maxsup = sup
            maxinf = inf

    nl = l[maxinf:maxsup + 1] #die langste Teilfolge ubernimmt die Elemente auf den entsprechenden Positionen
    return nl

print("Geben Sie die Anzahl der Elemente aus dem Vektor ein:")
n2=int(input("n="))
b=[]
print("Geben Sie die Elemente ein:")
for i in range(0,n2):
    print("l[",i,"]= ")
    m=int(input())
    b+=[m]


print("Die langste Teilfolge, so dass alle 2 aufeinanderfolgende Elemente relativ prim sind, ist:")
#b=[2,4,15,13,19]
print(relativprim(b))



