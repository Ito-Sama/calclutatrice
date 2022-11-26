from operandes import *
from convertion import *
from gui import *
from tkinter import *

print("""
Calculatrice   (version Beta encore)

    possibilité : -additionner (add)
                -multiplier (mult)
                -calculer un exposant (exp)
                -calculer une division euclidienne (div)

    bonus : -encoder un nombre entier positif en binaire (encode)
            -decoder un nombre binaire vers la base 10 (decode)

    pour stopper l'appli, tapper "stop"
""")


while True:
    choix = input(">")

    if choix == "add":
        n1 = int(input(">"))
        n2 = int(input(">"))
        print(add(n1,n2))

    elif choix == "mult":
        n1 = int(input(">"))
        n2 = int(input(">"))
        print(multiply(n1,n2))

    elif choix == "exp":
        n1 = int(input(">"))
        n2 = int(input(">"))
        print(exposant(n1,n2))

    elif choix == "div":
        n1 = int(input(">"))
        n2 = int(input(">"))
        print(div(n1,n2))

    elif choix == "encode":
        print(encode(int(input(">"))))

    elif choix == "decode":
        print(decode(conv_int_to_list(int(input(">")))))

    elif choix =="stop":
        break

    else:
        print("""
        Calculatrice   (version Beta encore)

            possibilité : -additionner (add)
                        -multiplier (mult)
                        -calculer un exposant (exp)
                        -calculer une division euclidienne (div)

            bonus : -encoder un nombre entier positif en binaire (encode)
                    -decoder un nombre binaire vers la base 10 (decode)

            pour stopper l'appli, tapper "stop"
        """)
        
