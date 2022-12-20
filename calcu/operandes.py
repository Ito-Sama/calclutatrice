from convertion import encode, decode
from portes_logiques import *

"""
==========================
    contient les opérandes
    de bases.
    N'acepte que les     Fait par Table Hautte#5362 
    nombres entiers 
    positifs
==========================

"""

def conv_int_to_list(n): #convertie un entier en une liste
    n=str(n)
    l=[]
    for i in n:
        l.append(int(i))
    return l

def con_list_to_str(l): #convertie une liste en une chaine de caractère
    st=''

    for i in range(len(l)):
        st = st + str(l[i]) 
        
    print(st)

def conv_list_to_int(l):
    st=''
    for i in range(len(l)):
        st = st + str(l[i])     

    st = int(st)
    return st


def add(n1,n2): #réalise un addition de deux nombres entiers positifs
   
    r=[]
    c = False
    d = None

    nv1=encode(n1)
    nv2=encode(n2)   #encode les deux entrées en binaires sous forme de listes

    len_nv1 = len(nv1)
    len_nv2 = len(nv2)   #récupère les longueurs des deux listes

    if len_nv1 > len_nv2:     #
        d = len_nv1 - len_nv2 #
        for i in range(d):    #
            nv2 = [0] + nv2   #
                              #verifie les longueurs des deux listes et rajoutes des 0 en débuts de la liste la plus courtes pour avoir la meme longueur
    elif len_nv2 > len_nv1:   #
        d = len_nv2 - len_nv1 #
        for i in range(d):    #
            nv1 = [0] + nv1   #


    for i in range(len(nv1)-1, -1, -1):                                                                           #                 
        a = nv1[i]                                                                                                #
        b = nv2[i]                                                                                                #sources : https://sites.google.com/site/sciencesdunumerique/algorithmique/Addition
        unite = (AND3(a,NOT(b),NOT(c))) or (AND3(NOT(a),b, NOT(c))) or (AND3(NOT(a),NOT(b),c)) or AND3(a,b,c)     #j'avoue j'ai pris cette boucle sur internet mais la variable "unite" et "c" on été
        r = [int(unite)] + r                                                                                      #refaite entierement par mes soins donc ça va ^^
        c = AND(a,b) or AND(b,c) or AND(a,c)                                                                      #
    r = [int(c)] + r                                                                                              #

    r = decode(r) #decode le résultat du binaire au décimal
    return r


def subb(n1,n2): #réalise une addition de deux nombres entiers
    n2 = -n2     
    n1=n1+n2
    return n1

def multiply(n1,n2): #realise une multiplication pour deuc nombres entiers positifs

    d = n1
    for i in range(n2-1):
        n1 = add(d,n1)

    return n1

def exposant(n1,n2): #calcule l'exposant n2 du nombre n1

    if n1 < 0: #si n1 est negatif, on le met en positif
        d = -n1
    else:
        d = n1

    for i in range(n2-1):
        n1 = multiply(d,n1)

    return n1


def div(n1,n2): #réalise une division euclidienne de deuc nombres entiers positif (pas fini car à terme, elle donneras le résultat exacte)
    if n2 == "0":
        return "on ne peut pas diviser par 0"
    q=0
    while n1 >= n2:
        n1 = subb(n1,n2)
        q=add(q,1)


    return "quotiens",q,"; reste", n1
