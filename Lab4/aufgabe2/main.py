def ersetzen_worter(filename,word1,word2):
    f=open(filename,'r')

    result=[]
    cnt_ersetzen=0

    for line in f:
        words=line.split(' ')
        for word in words:
            word=word.strip()
            if word==word1:
                result.append(word2)
                cnt_ersetzen+=1
            else:
                result.append(word)

    f.close()

    f=open(filename,'w')
    for i in range(len(result)):
        f.write(result[i])
        if i!=len(result)-1:
            f.write(' ')

    f.close()
    if cnt_ersetzen==0:
        print('nichts war ersetzt')
    return cnt_ersetzen

assert ersetzen_worter('text.txt','Katze','Hund')==0




