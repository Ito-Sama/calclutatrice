



"""
==========================
    Definitions de toutes
    les fonctions pour                  Fait par Table Hautte#5362
    les conversions
    binaires
==========================

"""

def encode(n):  #encode un nombre entier positif n en nombre binaire sous forme de liste
    
    l=[]

    if n == 0:
        l = [0]            
        return l 

    else :
        while n > 0:
            m=n%2
            n=n//2
            l = [m] + l 
       
        return l 



# def encode2(n):

#         l=[]

#         if n == 0:
#             l = [0]            
#             return l 
#         else :
#             while n > 0:
#                 m=n%2
#                 n=n//2
#                 if m==1:
#                     m=0
#                 else:
#                     m=1

#                 l = [m] + l 
        
#             return l 


def decode(n): #decode un nombre binaire sous forme de liste en entier positif

    n.reverse()
    a = 0

    for i in range(len(n)):
        n[i] = n[i]*(2**i) 
        a = n[i] + a    
        

    return a
