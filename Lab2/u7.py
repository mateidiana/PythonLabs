#Kleinster gemeinsamer Vielfacher zw 2 Indizes
def gemein_vielf(l,ffrom,to):
    max_num=0
    for i in range(ffrom,to+1):        #man findet das hochste Element der Liste
        if (max_num<l[i]):
            max_num=l[i]
    res=1

    #Elemente werden auf der Form gebracht, so dass sie relativ prim zueinander sind
    x=2
    while (x<=max_num):
        indexes=[]
        for j in range(ffrom,to+1):
            if l[j]%x==0:
                indexes.append(j)

        if len(indexes)>=2:
            for j in range(len(indexes)):
                l[indexes[j]]=int(l[indexes[j]]/x)        #man teilt die Elemente der Liste durch
                                                          #gemeinsame Primfaktoren
            res=res*x  #das Ergebnis multipliziert die gemeinsamen Primfaktoren
        else:
            x+=1

    for i in range(ffrom,to+1):
        res=res*l[i]           #das Ergebnis multipliziert die Zahlen die relativ prim zueinander sind
    return res

a=[12,24,48,10,20,10,30,59]
print("Der kleinste gemeinsame Vielfacher in dieser Sequenz ist:")
print(gemein_vielf(a,0,2))


