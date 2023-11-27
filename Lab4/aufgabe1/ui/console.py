import turtle
from aufgabe1.logik.letters import draw_a,draw_b,draw_c,draw_d,draw_e,draw_f,draw_g,draw_h,draw_i,draw_j,draw_k
from aufgabe1.logik.letters import draw_l,draw_m,draw_n,draw_o,draw_p,draw_q,draw_r,draw_s,draw_t,draw_u,draw_v
from aufgabe1.logik.letters import draw_w,draw_x,draw_y,draw_z,draw_dot,draw_exclam,draw_question

from aufgabe1.logik.instructions import w,s,d,a,f,g

dict={"w": w, "s": s, "d":d, "a":a, "f":f, "g":g}

dict1 =  {"a": draw_a, "b": draw_b, "c": draw_c, "d": draw_d, "e": draw_e, "f": draw_f, "g": draw_g,
         "h": draw_h, "i": draw_i, "j": draw_j, "k": draw_k, "l": draw_l, "m": draw_m, "n": draw_n,
         "o": draw_o, "p": draw_p, "q": draw_q, "r": draw_r, "s": draw_s, "t": draw_t, "u": draw_u,
         "v": draw_v, "w": draw_w, "x": draw_x, "y": draw_y, "z": draw_z, ".": draw_dot, "!": draw_exclam,
         "?":draw_question}
def user_input():

    f=open('input.txt','r')
    instr=f.read().strip()
    l1=list(instr)

    text=input('Your input is:')
    l=list(text)
    shift=0

    wn = turtle.Screen()
    for i in range(len(l)):
        if l[i]==' ':
            shift+=50
        if l[i] not in dict1:
            turtle.up()
            turtle.backward(350-shift)
            turtle.down()
            for j in range(len(l1)):

                dict[l1[j]]()
            shift+=40
        else:
            dict1[l[i]](shift)
            shift+=40


    wn.exitonclick()


def user_input1():

    text = input('Your input is:')

    wn=turtle.Screen()

    turtle.onkey(a,'a')
    turtle.onkey(w,'w')
    turtle.onkey(s,'s')
    turtle.onkey(d,'d')
    turtle.onkey(f, 'f')
    turtle.onkey(g, 'g')

    turtle.listen()
    wn.exitonclick()



