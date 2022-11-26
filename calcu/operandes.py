from convertion import encode, decode, encode2
from portes_logiques import *

"""
-------------------------
    contient les opérandes
    de bases.
    N'acepte que les     Fait par Table Hautte#5362 
    nombres entiers 
    positifs
-------------------------

"""

def conv_int_to_list(n):
    n=str(n)
    l=[]
    for i in n:
        l.append(int(i))
    return l


def add(n1,n2):
   
    r=[]
    c = False
    d = None

    nv1=encode(n1)
    nv2=encode(n2)

    len_nv1 = len(nv1)
    len_nv2 = len(nv2)

    if len_nv1 > len_nv2:
        d = len_nv1 - len_nv2
        for i in range(d):
            nv2 = [0] + nv2

    elif len_nv2 > len_nv1:
        d = len_nv2 - len_nv1
        for i in range(d):
            nv1 = [0] + nv1


    for i in range(len(nv1)-1, -1, -1):                                                                           #                 
        a = nv1[i]                                                                                                #
        b = nv2[i]                                                                                                #sources : https://sites.google.com/site/sciencesdunumerique/algorithmique/Addition
        unite = (AND3(a,not(b),not(c))) or (AND3(not(a),b, not(c))) or (AND3(not(a),not(b),c)) or AND3(a,b,c)     #j'avoue j'ai pris cette boucle sur internet mais la variable "unite" et "c" on été
        r = [int(unite)] + r                                                                                      #refaite entierement par mes soins donc ça va ^^
        c = AND(a,b) or AND(b,c) or AND(a,c)                                                                      #
    r = [int(c)] + r                                                                                              #

    r = decode(r)
    return r


def subb(n1,n2):
    r=[]
    c = False
    d = None

    nv1=encode2(n1)
    nv2=encode2(n2)

    len_nv1 = len(nv1)
    len_nv2 = len(nv2)

    if len_nv1 > len_nv2:
        d = len_nv1 - len_nv2
        for i in range(d):
            nv2 = [0] + nv2

    elif len_nv2 > len_nv1:
        d = len_nv2 - len_nv1
        for i in range(d):
            nv1 = [0] + nv1
    
        if nv2[0] == 0:
            nv2 = [1] + nv2
    
    
    nv2[0] = 1


def multiply(n1,n2):

    d = n1
    for i in range(n2-1):
        n1 = add(d,n1)

    return n1

def exposant(n1,n2):

    d = n1
    for i in range(n2-1):
        n1 = multiply(d,n1)

    return n1


def div(n1,n2):
    q=0
    while n1 > n2:
        n1 -= n2
        q=add(q,1)

    r=n1
    return "quotiens",q,"; reste", r

