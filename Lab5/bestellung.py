from identifizierbar import Identifizierbar
from repo import DataRepo
import os
import pickle

class Bestellung(Identifizierbar):
    def __init__(self,kundenid,gerichtliste,getrankliste,gesamtkosten,gesamtzeit,rechnung,id):
        self.kundenid=kundenid
        self.gerichtliste=gerichtliste
        self.getrankliste=getrankliste
        self.gesamtkosten=gesamtkosten
        self.gesamtzeit=gesamtzeit
        self.rechnung=rechnung
        Identifizierbar.__init__(self,id)

    def __str__(self):
        return f'Customer ID:{self.kundenid},ID:{self.id},Dishes:{self.gerichtliste},Drinks:{self.getrankliste},Price:{self.gesamtkosten},Preparation time:{self.gesamtzeit},Calculation:{self.rechnung}'


class OrderRepo(DataRepo):
    def __init__(self,filename):
        DataRepo.__init__(self)
        self.filename=filename

        if os.path.exists(self.filename):
            self.load()

    def add(self,order):
        self.orders.append(order)
        self.save()

    def save(self):
        f=open(self.filename,'ab')
        pickle.dump(self.orders,f)
        f.close()

    def load(self):
        f=open(self.filename,'rb')
        file_contents = str(f.read())
        list_of_records = file_contents.split('.')
        no_of_records = len(list_of_records) - 1
        f.seek(0)
        for i in range(no_of_records):
            self.orders=pickle.load(f)
        f.close()

