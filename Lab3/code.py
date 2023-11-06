# zwei Rechtecke 100*50 und 50*25, das Kleine im Inneren des Grossen

import turtle


def rechteck():
    t = turtle.Pen()

    t.speed(1)
    t.backward(200)

    t.right(90)
    t.forward(100)
    t.left(90)

    t.forward(200)
    t.left(90)
    t.forward(100)

    t.up()

    t.left(180)
    t.forward(37)
    t.right(90)
    t.forward(75)
    t.down()

    t.forward(50)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(25)

    turtle.done()

#Herz
def herz():
    t = turtle.Pen()
    t.left(40)
    t.forward(113)
    t.up()
    t.left(180)
    t.forward(113)
    t.down()
    t.right(90)
    t.forward(113)
    for i in range(190):
        t.right(1)
        t.forward(1)
    t.up()
    t.left(10)
    t.forward(101)
    t.left(90)
    t.down()
    for i in range(185):
        t.left(1)
        t.forward(1)

    turtle.done()

#Hauser
def hauser():
    t = turtle.Pen()
    q = turtle.Pen()

    t.backward(200)

    q.up()
    q.forward(210)
    q.down()

    q.backward(200)

    t.right(90)
    q.right(90)
    t.forward(100)
    q.forward(100)
    t.left(90)
    q.left(90)

    t.forward(200)
    q.forward(200)
    t.left(90)
    q.left(90)
    t.forward(100)
    q.forward(100)

    t.left(40)
    q.left(40)
    t.forward(150)
    q.forward(150)
    t.left(98)
    q.left(98)
    t.forward(153)
    q.forward(153)

    t.left(40)
    q.left(40)
    t.up()
    q.up()
    t.forward(100)
    q.forward(100)
    t.left(90)
    q.left(90)
    t.forward(90)
    q.forward(90)
    t.down()
    q.down()

    t.left(90)
    q.left(90)
    t.forward(50)
    q.forward(50)
    t.right(90)
    q.right(90)
    t.forward(25)
    q.forward(25)
    t.right(90)
    q.right(90)
    t.forward(50)
    q.forward(50)

    t.right(180)
    q.right(180)

    t.up()
    q.up()
    t.forward(60)
    q.forward(60)
    t.down()
    q.down()
    t.forward(20)
    q.forward(20)
    t.left(90)
    q.left(90)
    t.forward(25)
    q.forward(25)
    t.left(90)
    q.left(90)
    t.forward(25)
    q.forward(25)
    t.left(90)
    q.left(90)
    t.forward(25)
    q.forward(25)

    turtle.done()


def menu():
    return """
        1 - Rechteck
        2 - Herz
        3 - Hauser
        0 - Exit
    """


def main():
    while True:
        print(menu())
        opt = int(input('opt= '))
        if opt == 1:
            rechteck()

        if opt == 2:
            herz()

        if opt == 3:
            hauser()

        if opt == 0:
            break


main()

