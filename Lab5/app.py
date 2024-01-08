from logic import ControllerCustomer,ControllerDrink,ControllerCookedDish,ControllerOrder
from kunde import CustomerRepo
from gekochtergericht import CookedDishRepo
from getrank import DrinkRepo
from bestellung import OrderRepo
from console import ConsoleCustomer,ConsoleDrink,ConsoleCookedDish,ConsoleOrder

def main():
    print('Which repo?')
    print('1-Customer')
    print('2-Cooked dish')
    print('3-Drink')
    print('4-Order')

    wahl=int(input())

    if wahl==1:
        repo=CustomerRepo('customers.data')
        c=ConsoleCustomer(ControllerCustomer(repo))
        c.run()
    if wahl==2:
        repo=CookedDishRepo('dishes.data')
        c=ConsoleCookedDish(ControllerCookedDish(repo))
        c.run()

    if wahl==3:
        repo=DrinkRepo('drinks.data')
        c=ConsoleDrink(ControllerDrink(repo))
        c.run()

    if wahl==4:
        repo=OrderRepo('orders.data')
        c=ConsoleOrder(ControllerOrder(repo))
        c.run()

main()


