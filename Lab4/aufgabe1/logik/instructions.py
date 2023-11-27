import turtle

def w():

    turtle.forward(10)
    file=open('input.txt','a')
    file.write('w')

def s():
    turtle.backward(10)
    file = open('input.txt', 'a')
    file.write('s')

def d():
    turtle.right(45)
    file = open('input.txt', 'a')
    file.write('d')

def a():
    turtle.left(45)
    file = open('input.txt', 'a')
    file.write('a')

def f():
    turtle.up()
    file = open('input.txt', 'a')
    file.write('f')

def g():
    turtle.down()
    file = open('input.txt', 'a')
    file.write('g')