from identifizierbar import Identifizierbar
from repo import DataRepo
import os
import pickle

class Kunde(Identifizierbar):
    def __init__(self,name,adresse,id):
        self.name=name
        self.adresse=adresse
        Identifizierbar.__init__(self,id)

    def __str__(self):
        return f'ID:{self.id},Name:{self.name},Address:{self.adresse}'


class CustomerRepo(DataRepo):
    def __init__(self,filename):
        DataRepo.__init__(self)
        self.filename=filename
        # self.customers=[]

        if os.path.exists(self.filename):
            self.load()

    def add(self,customer):
        self.customers.append(customer)
        self.save()

    def delete(self,name):
        for customer in self.customers:
            if customer.name==name:
                self.customers.remove(customer)
        self.save()

    def aktualisieren(self,name,other_name):
        for customer in self.customers:
            if customer.name==name:
                customer.name=other_name
        self.save()

    def save(self):
        f=open(self.filename,'ab')
        pickle.dump(self.customers,f)
        f.close()

    def load(self):
        f=open(self.filename,'rb')
        file_contents = str(f.read())
        list_of_records = file_contents.split('.')
        no_of_records = len(list_of_records) - 1
        f.seek(0)

        for i in range(no_of_records):
            self.customers=pickle.load(f)
        f.close()