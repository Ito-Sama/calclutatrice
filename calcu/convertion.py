



"""
--------------------------
    Definitions de toutes
    les fonctions pour                  Fait par Table Hautte#5362
    les conversions
    binaires
--------------------------

"""

def encode(n):
    
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
        


def decode(n):

    n.reverse()
    a = 0

    for i in range(len(n)):
        n[i] = n[i]*(2**i) #ok j'ai utiliser des opérandes de bases mais j'étais obliger aussi
        a = n[i] + a    
        

    return a

