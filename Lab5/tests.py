from kunde import Kunde,CustomerRepo
from gekochtergericht import Gekochtergericht,CookedDishRepo
from bestellung import Bestellung,OrderRepo
from logic import ControllerCustomer,ControllerCookedDish,ControllerOrder

repo=CustomerRepo('test.data')
controller=ControllerCustomer(repo)

#Finden Kunde anhand des Teilnamens
client=Kunde('Bob','Balea',1)
controller.repo.add(client)
clienti=controller.find_customer('Bo')
assert clienti[0].name=='Bob'
assert clienti[0].adresse=='Balea'
assert clienti[0].id==1

#Finden Kunde anhand der Teiladresse
clienti1=controller.find_customer('Bal')
assert clienti1[0].name=='Bob'
assert clienti1[0].adresse=='Balea'
assert clienti1[0].id==1

#Aktualisieren Kundenname
client1=Kunde('Zob','Titulescu',2)
controller.repo.add(client1)
controller.repo.aktualisieren('Zob','Oob')
for i in range(2):
    clienti2=controller.show_customers()
    kundenname=clienti2[0].name


#Hinzufugen von Gericht
repo1=CookedDishRepo('testgericht.data')
controller1=ControllerCookedDish(repo1)

dish=Gekochtergericht('Potatoes',250,15,1,10)
controller1.repo.add(dish)
dishes=controller1.show_dishes()
assert dishes[0].name=='Potatoes'
assert dishes[0].portionsgrosse==250

#Bestellungsinstanz
repo2=OrderRepo('testorder.data')
controller2=ControllerOrder(repo2)

order=Bestellung(1,['Schnitzel'],['Juice'],40,20,[25,'+',15],1)
controller2.repo.add(order)
orders=controller2.show_orders()
assert orders[0].kundenid==1
assert orders[0].gerichtliste==['Schnitzel']

#Konvert list to string
mystring=controller.convert_list_string(orders[0].rechnung)=='25+15'