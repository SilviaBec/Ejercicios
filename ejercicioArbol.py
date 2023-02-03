def countApplesAndOranges(s, t, a, b, apples, oranges):

    cont=0
    cont2=0
    for x in apples:
        manzana=x+a
        if manzana>=s and manzana<=t:
            cont=cont+1
    print(cont)
                    
    for i in oranges:
        naranja=i+b
        if naranja>=s and naranja<=t:
            cont2=cont2+1
    print(cont2)
