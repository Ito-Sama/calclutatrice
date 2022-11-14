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

def adder():

    a = int(input(">"))
    b = int(input("+ >"))

    a=encode(a)
    b=encode(b)
    Cin = 0


    xo1 = XOR(a,b)
    Out = XOR(xo1, Cin)
    ao1 = AND(a,b)
    ao2 = AND(Cin, xo1)
    Cout = OR(ao1, ao2)

    return Out, Cout

print(adder())

