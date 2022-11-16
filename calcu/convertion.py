



"""
--------------------------
    Definitions de toutes
    les fonctions pour                  Fait par Table Hautte#5362
    les conversions
    binaires
--------------------------

"""


def conv_int_to_list(n):
    n=str(n)
    l=[]
    for i in n:
        l.append(int(i))
    return l


def encode(n):

    l=[]

    if n != 0:
    
        while n > 0:
            m=n%2
            n=n//2
            l = l + [m]
            # out_e=''
            # j=0

            # for i in range(len(l)):
                
            #     out_e = str(l[0+i]) + out_e
            #     i=i+1
            #     j=j+1
                    

        return l #out_e

    else :
        #out_e='0'
        l = [0]
        return l #out_e
        



def decode(n):

    n=conv_int_to_list(n)
    n.reverse()
    a = 0

    for i in range(len(n)):
        n[i] = n[i]*(2**i)
        a = n[i] + a    
        

    return a

