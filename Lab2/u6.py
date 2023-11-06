#Langste zusammenhangende Domino Teilfolge
def domino(a,b):
    if a%10==(b//10)%10:
        return True
    return False

def sequenz_domino(l):
    nl = []  # die Teilfolge ist anfangs eine leere Liste
    ct = 0
    i = 0
    maxinf = 0  # Anfangsindizes der langsten Teilfolge
    maxsup = 0  # Endindizes der langsten Teilfolge

    while ct < len(l) - 1:  # man geht alle Elemente des Vektors durch
        inf = ct  # das erste Element jeder Teilfolge

        while domino(l[i], l[i + 1]) == 1 and i < len(l) - 2:
            i = i + 1  # solange die Elemente domino sind wird zu der Lange addiert
            # das vorvorletzte und das vorletzte Element werden zuletzt verglichen

        if i == len(l) - 2 and domino(l[i], l[i + 1]) == 1:
            i = i + 1  # das vorletzte und das letzte Element werden verglichen

        sup = i  # Endindizes der kurrenten Teilfolge
        ct = i + 1  # Anfangsindizes der nachsten Teilfolge
        i = i + 1  # Anfangsindizes der nachsten Teilfolge

        if sup - inf > maxsup - maxinf:  # falls die kurrente Lange grosser ist als die vorige werden die Maximumwerte ersetzt
            maxsup = sup
            maxinf = inf

    nl = l[maxinf:maxsup + 1]  # die langste Teilfolge ubernimmt die Elemente auf den entsprechenden Positionen
    return nl

a=[89,95,54,32,11]
print(sequenz_domino(a))