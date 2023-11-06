#Verschlusseln der Liste mit +,*,XOR
def versch_plus(l):
    for i in range(1,len(l)):
        l[i]+=l[0]
    return l

def versch_mal(l):
    for i in range(1,len(l)):
        l[i]*=l[0]
    return l

def versch_bit(l):
    for i in range(1,len(l)):
        l[i]=l[i]^l[0]
    return l

a=[10,11,20]
#print(versch_plus(a))
#print(versch_mal(a))
print(versch_bit(a))