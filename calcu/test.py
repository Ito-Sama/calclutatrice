def div(n1,n2): #réalise une division euclidienne de deuc nombres entiers positif (pas fini car à terme, elle donneras le résultat exacte)
    if n2 == 0:
        return "on ne peut pas diviser par 0"
    q=0
    while n1 >= n2:
        n1 = n1 - n2
        q+=1


    return "quotiens",q,"; reste", n1


print(div(7,3))
