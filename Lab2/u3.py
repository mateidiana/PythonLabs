#Generieren der hochsten moglichen Zahl die durch Konkatenation entsteht
def konkat(l):
    z=''
    #sort desc
    for i in range(len(l)):
        for j in range(len(l)-1):
            if l[i]>l[j]:
                aux=l[i]                         #fallend sortiert
                l[i]=l[j]
                l[j]=aux

    for i in range(len(l)):
        z=z+str(l[i])                            #konkatenation- vorne die hochsten Zahlen

    return z


a=[17,25,11,78,45]
print(konkat(a))

