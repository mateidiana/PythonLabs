from logic import ControllerCustomer,ControllerDrink,ControllerCookedDish,ControllerOrder
from kunde import Kunde
from gekochtergericht import Gekochtergericht
from getrank import Getrank
from bestellung import Bestellung
import pickle
from datetime import datetime

class ConsoleCustomer:
    def __init__(self,controller:ControllerCustomer):
        self.controller=controller

    def menu(self):
        return """
        1-Add customer
        2-Find by name or street
        3-Show all customers
        4-Delete customer
        5-Show customer's order
        6-Update name
        7-Exit
    """

    def run(self):
        while True:
            print(self.menu())
            opt=int(input('Input: '))
            if opt==1:
                name=input('name= ')
                adresse=input('address= ')
                id=input('id= ')

                self.controller.repo.add(Kunde(name,adresse,id))
            if opt==2:
                name=input('name=')
                customers=self.controller.find_customer(name)
                for customer in customers:
                    print(customer)
            if opt==3:
                customers=self.controller.show_customers()
                for customer in customers:
                    print(customer)
            if opt==4:
                name = input('name=')
                self.controller.repo.delete(name)
            if opt==5:
                now=datetime.now()
                st=now.hour
                min=now.minute

                id=input('Customer ID=')
                customers=self.controller.show_order_customer(id)

                f = open('orders.data', 'rb')
                file_contents = str(f.read())
                list_of_records = file_contents.split('.')
                no_of_records = len(list_of_records) - 1
                f.seek(0)

                for i in range(no_of_records):
                    orders = pickle.load(f)
                    for customer in customers:
                        for order in orders:
                            if customer.id == order.kundenid:
                                print(f'{customer.name} s order is:')
                                print(order)
                                mystring=self.controller.convert_list_string(order.rechnung)
                                print(f'{customer.name} s order price is:')
                                print(mystring+'='+str(order.gesamtkosten))
                                min+=int(order.gesamtzeit)
                                while min>59:
                                    st+=1
                                    min-=60
                                print(f'{customer.name} s order will be ready at:')
                                if min==0:
                                    print(f'{st}:{min}0')
                                else:
                                    if min<10:
                                        print(f'{st}:0{min}')
                                    else:
                                        print(f'{st}:{min}')
                                customers.remove(customer)

                f.close()

            if opt==6:
                name = input('Which customer to update=')
                other_name=input('The name is now=')
                self.controller.repo.aktualisieren(name,other_name)
            if opt==7:
                break


class ConsoleCookedDish:
    def __init__(self,controller:ControllerCookedDish):
        self.controller=controller

    def menu(self):
        return """
        1-Add cooked dish
        2-Show dishes
        3-Delete dish
        4-Exit
    """

    def run(self):
        while True:
            print(self.menu())
            opt=int(input('Input: '))
            if opt==1:
                name=input('name= ')
                portionsgrosse=input('portion size= ')
                preis=input('price= ')
                id=input('id= ')
                preparation_time=input('preparation time= ')
                self.controller.repo.add(Gekochtergericht(name,portionsgrosse,preis,id,preparation_time))

            if opt==2:
                cooked_dishes=self.controller.show_dishes()
                for dish in cooked_dishes:
                    print(dish)

            if opt==3:
                name=input('name=')
                self.controller.repo.delete(name)

            if opt==4:
                break


class ConsoleDrink:
    def __init__(self,controller:ControllerDrink):
        self.controller=controller

    def menu(self):
        return """
        1-Add drink
        2-Show drinks
        3-Delete drink
        4-Exit
    """

    def run(self):
        while True:
            print(self.menu())
            opt=int(input('Input: '))
            if opt==1:
                name=input('name= ')
                portionsgrosse=input('portion size= ')
                preis=input('price= ')
                id=input('id= ')
                alcohol=input('alcohol content= ')
                self.controller.repo.add(Getrank(name,portionsgrosse,preis,id,alcohol))

            if opt==2:
                drinks=self.controller.show_drinks()
                for drink in drinks:
                    print(drink)

            if opt==3:
                name=input('name=')
                self.controller.repo.delete(name)

            if opt==4:
                break


class ConsoleOrder:
    def __init__(self,controller:ControllerOrder):
        self.controller=controller

    def menu(self):
        return """
        1-Add order
        2-Show orders
        3-Exit
    """

    def run(self):
        while True:
            print(self.menu())
            opt=int(input('Input: '))
            if opt==1:
                kundenid=input('Customer ID= ')
                id=input('Order ID= ')

                dishes=[]
                dishes1=[]
                drinks=[]
                drinks1=[]
                gesamtkosten=0
                gesamtzeit=0
                rechnung=[]

                nr_dishes=int(input('How many dishes?'))
                for i in range(nr_dishes):
                    dish=input('Enter dish:')
                    dishes.append(dish)
                    dishes1.append(dish)

                nr_drinks = int(input('How many drinks?'))
                for i in range(nr_drinks):
                    drink = input('Enter drink:')
                    drinks.append(drink)
                    drinks1.append(drink)


                f=open('dishes.data','rb')
                file_contents = str(f.read())
                list_of_records = file_contents.split('.')
                no_of_records = len(list_of_records) - 1
                f.seek(0)

                for i in range(no_of_records):
                    cooked_dishes = pickle.load(f)
                    for dish in dishes:
                        for cooked_dish in cooked_dishes:
                            if dish==cooked_dish.name:
                                gesamtkosten+=int(cooked_dish.preis)
                                rechnung.append(int(cooked_dish.preis))
                                rechnung.append('+')
                                gesamtzeit+=int(cooked_dish.zubereitungszeit)
                                dishes.remove(dish)


                f.close()

                f = open('drinks.data', 'rb')
                file_contents = str(f.read())
                list_of_records = file_contents.split('.')
                no_of_records = len(list_of_records) - 1
                f.seek(0)

                for i in range(no_of_records):
                    repo_drinks = pickle.load(f)
                    for drink in drinks:
                        for repo_drink in repo_drinks:
                            if drink == repo_drink.name:
                                gesamtkosten += int(repo_drink.preis)
                                rechnung.append(int(repo_drink.preis))
                                rechnung.append('+')
                                drinks.remove(drink)

                f.close()

                rechnung.pop()

                self.controller.repo.add(Bestellung(kundenid,dishes1,drinks1,gesamtkosten,gesamtzeit,rechnung,id))

            if opt==2:
                orders=self.controller.show_orders()
                for order in orders:
                    print(order)

            if opt==3:
                break