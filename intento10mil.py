lista = [9,[10,5,20,20,4,5,2,25,1]]
min=lista[1][0]
max=lista[1][0]
cont=0
cont2=0
for i in lista[1]:
    if i<min and i!=min:
        min=i
        cont=cont+1
    if i >max and i!=max:
        max=i
        cont2+=1
print(cont)
print(cont2)