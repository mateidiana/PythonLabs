from kunde import CustomerRepo
from gekochtergericht import CookedDishRepo
from getrank import DrinkRepo
from bestellung import OrderRepo
class ControllerCustomer:
    def __init__(self,repo:CustomerRepo):
        self.repo=repo

    def find_customer(self,name):
        return [customer for customer in self.repo.customers if name in customer.name or name in customer.adresse]

    def delete_customer(self,name):
        for customer in self.repo.customers:
            if customer.name==name:
                self.repo.customers.remove(customer)

    def show_order_customer(self,id):
        return [customer for customer in self.repo.customers if customer.id == id]

    def convert_list_string(self,l):
        mystring=''.join(map(str,l))
        return mystring

    def show_customers(self):
        return [customer for customer in self.repo.customers]


class ControllerCookedDish:
    def __init__(self,repo:CookedDishRepo):
        self.repo=repo

    def show_dishes(self):
        return [cooked_dish for cooked_dish in self.repo.cooked_dishes]


class ControllerDrink:
    def __init__(self, repo:DrinkRepo):
        self.repo = repo

    def delete_drink(self,name):
        for drink in self.repo.drinks:
            if drink.name==name:
                self.repo.drinks.remove(drink)

    def show_drinks(self):
        return [drink for drink in self.repo.drinks]


class ControllerOrder:
    def __init__(self,repo:OrderRepo):
        self.repo=repo

    def show_orders(self):
        return [order for order in self.repo.orders]

