# Hallar los radios de numeros positivos, negativos y ceros en un array
# determinado usando 6 cifras decimales en el resultado.
def miFuncion(arr):
    n= len(arr)
    pos= 0
    neg=0
    cero=0
    if n>= -100 and n<=100:
        for x in arr:
            if x >0:
                pos=pos+1
            if x<0:
                neg=neg+1
            if x==0:
                cero=cero+1
    print(format(pos/n,'.6f'),format(neg/n,'.6f'),format(cero/n,".6f"),sep='\n')
    
miFuncion([-4,-9,3,0,1,4])

    
