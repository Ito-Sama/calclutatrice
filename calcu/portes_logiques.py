



"""
--------------------------
    Definitions de toutes
    les portes logiques     Fait par Table Hautte#5362 
    utiles pour les 
    opérations de bases
--------------------------

"""

#vaiables de Debug !
l1 = [0,1]
l2 = [1,0]
n1,n2 = 0,1
l3=[]



def AND(a,b):
    if a == 1 and b == 1:
        return 1
    else:
        return 0


def NAND(a,b):
    if a == 1 and b == 1:
        return 0
    else:
        return 1


def OR(a,b):
    if a == 1 or b == 1:
        return 1
    else:
        return 0


def XOR(a,b):
    if a != b:
        return 1
    else:
        return 0


def NOT(a):
    return not a


def NOR(a, b):
    if(a == 0) and (b == 0):
        return 1
    elif(a == 0) and (b == 1):
        return 0
    elif(a == 1) and (b == 0):
        return 0
    elif(a == 1) and (b == 1):
        return 0


def XNOR(a,b):
    if(a == b):
        return 1
    else:
        return 0


