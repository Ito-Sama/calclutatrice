from convertion import encode, decode
from portes_logiques import *


"""
-------------------------
    Full Adder
    N'acepte que les 
    nombres entiers 
    positifs
-------------------------

"""
def add_2b(a,b,c):
    st=''

    a = int(a)
    b = int(b)
    c = int(c)

    for i in range(4-1): 
        xo1 = XOR(a,b)
        out = XOR(xo1, c)
        ao1 = AND(a,b)
        ao2 = AND(c, xo1)
        c = OR(ao1, ao2) 

        st = str(out) + st

        print(st)


def adder():
    n1 = int(input(">"))
    n2 = int(input("+ >"))
    Cin = 0

    nv1=encode(n1)
    nv2=encode(n2)
    Cin=encode(Cin)


    return add_2b(nv1, nv2, Cin)

print(adder())

