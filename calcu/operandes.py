from convertion import encode, decode
from portes_logiques import *
import os


"""
-------------------------
    Full Adder
    N'acepte que les     Fait par Table Hautte#5362 
    nombres entiers 
    positifs
-------------------------

"""
n1 = int(input(">"))
n2 = int(input(">"))

def adder(n1,n2):
   
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


    for i in range(len(nv1)-1, -1, -1):                                                                                     #                 
        a = nv1[i]                                                                                                          #
        b = nv2[i]                                                                                                          #
        unite = (a and not(b) and not(c)) or (not(a) and b and not(c)) or (not(a) and not(b) and c) or (a and b and c)      #sources : https://sites.google.com/site/sciencesdunumerique/algorithmique/Addition
        r = [int(unite)] + r                                                                                                #j'avoue j'ai pris cette boucle sur internet mais la variable "unite" et "c" on été
        c = (a and b) or (b and c) or (a and c)                                                                             #refaite entierement par mes soins donc ça va ^^
    r = [int(c)] + r                                                                                                        #

    r = decode(r)
    return r




def multiply(n1,n2):

    d = n1
    for i in range(n2-1):
        n1 = d + n1

    return n1



os.system("pause")
