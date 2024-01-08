from identifizierbar import Identifizierbar
from repo import DataRepo

class Gericht(Identifizierbar):
    def __init__(self,name,portionsgrosse,preis,id):
        self.name=name
        self.portionsgrosse=portionsgrosse
        self.preis=preis
        Identifizierbar.__init__(self,id)

