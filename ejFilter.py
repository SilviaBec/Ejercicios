#PARES DEL 0 AL 50
#Program imperativa
lista=[]
for x in range(51):
    if x%2==0:
        lista.append(x)
print(lista)

#Con comprension de listas
lista2= [i for i in range(51) if i%2==0]
print(lista2)
#Con filter
lista3=list(filter(lambda x: x%2==0,range(51)))
print(lista3)