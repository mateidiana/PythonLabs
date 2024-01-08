from gericht import Gericht
from repo import DataRepo
import os
import pickle

class Gekochtergericht(Gericht):
    def __init__(self,name,portionsgrosse,preis,id,zubereitungszeit):
        self.zubereitungszeit=zubereitungszeit
        Gericht.__init__(self,name,portionsgrosse,preis,id)

    def __str__(self):
        return f'ID:{self.id},Name:{self.name},Portion size:{self.portionsgrosse},Price:{self.preis},Preparation time:{self.zubereitungszeit}'

class CookedDishRepo(DataRepo):
    def __init__(self,filename):
        DataRepo.__init__(self)
        self.filename=filename

        if os.path.exists(self.filename):
            self.load()

    def add(self,cooked_dish):
        self.cooked_dishes.append(cooked_dish)
        self.save()

    def delete(self,name):
        for cooked_dish in self.cooked_dishes:
            if cooked_dish.name==name:
                self.cooked_dishes.remove(cooked_dish)
        self.save()

    def save(self):
        f=open(self.filename,'ab')
        pickle.dump(self.cooked_dishes,f)
        f.close()

    def load(self):
        f=open(self.filename,'rb')
        file_contents=str(f.read())
        list_of_records=file_contents.split('.')
        no_of_records=len(list_of_records)-1
        f.seek(0)
        for i in range(no_of_records):
            self.cooked_dishes=pickle.load(f)
        f.close()