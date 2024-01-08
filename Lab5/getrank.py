from gericht import Gericht
from repo import DataRepo
import os
import pickle

class Getrank(Gericht):
    def __init__(self,name,portionsgrosse,preis,id,alkoholgehalt):
        self.alkoholgehalt=alkoholgehalt
        Gericht.__init__(self,name,portionsgrosse,preis,id)

    def __str__(self):
        return f'ID:{self.id},Name:{self.name},Portion size:{self.portionsgrosse},Price:{self.preis},Alcoholic content:{self.alkoholgehalt}'

class DrinkRepo(DataRepo):
    def __init__(self,filename):
        DataRepo.__init__(self)
        self.filename=filename

        if os.path.exists(self.filename):
            self.load()

    def add(self,drink):
        self.drinks.append(drink)
        self.save()

    def delete(self,name):
        for drink in self.drinks:
            if drink.name==name:
                self.drinks.remove(drink)
        self.save()

    def save(self):
        f=open(self.filename,'ab')
        pickle.dump(self.drinks,f)
        f.close()

    def load(self):
        f=open(self.filename,'rb')
        file_contents = str(f.read())
        list_of_records = file_contents.split('.')
        no_of_records = len(list_of_records) - 1
        f.seek(0)
        for i in range(no_of_records):
            self.drinks=pickle.load(f)
        f.close()