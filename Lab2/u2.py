#Anzahl der symmetrischen Paaren xy yx
def symmetrisch(l):
    nr=0
    for i in range (len(l)-1):
        aux=l[i]

        num=0
        while aux!=0:
            num=num*10+aux%10
            aux=aux//10               #jedes Element wird umgekehrt

        for j in range(i+1,len(l)):   #man sucht Elemente, die symmetrisch sind
           if num==l[j]:
               nr=nr+1                #wenn man ein Paar findet dann wird die Anzahl plusiert und die Schleife wird
                                      #unterbrochen
               break

    return nr

a=[31,44,13,23,52,25,25]
print('Die Anzahl der Paare die symmetrisch sind ist:')
print(symmetrisch(a))