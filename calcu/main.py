from operandes import *
from convertion import *

print("""
        Calculatrice   (version Beta encore)

            possibilité : -additionner 
                          -soustraire 
                          -multiplier 
                          -calculer un exposant 
                          -calculer une division euclidienne 

            bonus : -encoder un nombre entier positif en binaire (encode)
                    -decoder un nombre binaire vers la base 10 (decode)

            pour stopper l'appli, tapper "stop"
""")


while True:
    n1 = input(">")

    if n1 == "encode":
        c = encode(int(input(">")))
        print(con_list_to_str(c),end='\n\n')
        n1 = int(input(">"))

    elif n1 == "decode":
        print(decode(conv_int_to_list(int(input(">")))),end='\n\n')
        n1 = int(input(">"))

    elif n1 == "stop":
        break

    n1 = int(n1)
    choix = input(">")
    n2 = int(input(">"))
    

    if choix == "+":  
        print(add(n1,n2),end='\n\n')

    elif choix == "-":
        print(subb(n1,n2),end='\n\n')

    elif choix == "*":
        print(multiply(n1,n2),end='\n\n')

    elif choix == "/":
        print(div(n1,n2),end='\n\n')

    elif choix == "^":
        print(exposant(n1,n2),end='\n\n')


    else:
        print("""
        Calculatrice   (version Beta encore)

            possibilité : -additionner 
                          -soustraire 
                          -multiplier 
                          -calculer un exposant 
                          -calculer une division euclidienne 

            bonus : -encoder un nombre entier positif en binaire (encode)
                    -decoder un nombre binaire vers la base 10 (decode)

            pour stopper l'appli, tapper "stop"
        """)
        
