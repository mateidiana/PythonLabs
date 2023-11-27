import turtle
from ui.console import user_input, user_input1


def menu():
     return """
        1 - Textnachricht zeichnen
        2 - Neues Zeichen hinzufugen
     """


def main():
    print(menu())
    opt = int(input('opt= '))
    if opt == 1:
        user_input()

    if opt == 2:
        user_input1()


main()



