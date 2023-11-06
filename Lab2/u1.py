#Entfernen die Zahlen die sich wiederholen
def wiederholen(l):
    nl=[]
    for i in range(len(l)-1):
        for j in range (i+1,len(l)):
            if l[i]==l[j]:           #Elemente die wenigstens doppelt gefunden werden ersetzt man mit 0
                l[j]=0
    for i in range(len(l)):
        if l[i]!=0:                  #Elemente die nicht 0 sind werden in der neuen Liste eingefugt
            nl+=[l[i]]
    return nl

a=[11,10,11,25,71,50,71,10,10,15,15]
print('Die Liste ohne Zahlen die sich wiederholen:')
print(wiederholen(a))

