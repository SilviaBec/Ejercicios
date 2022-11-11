import itertools 
x = 1
y = 1
z = 2
n = 3

i=[]
j=[]
k=[] 
for num in range (x,-1,-1):
    i.append(num)
for num in range (y,-1,-1):
    j.append(num)
for num in range (z,-1,-1):
    k.append(num)

lista=[]
for num in k:
    lista.append(num)
    for num in i:
        lista.append(num)
        for num in j:
            lista.append(num)
perK= set(itertools.combinations(lista,3))

for val in perK:
    if val[0]+val[1]+val[2]!=n:
            print(val)

# lGrande=[]
# lista2=[perI,perJ,perK]
# for valor in i:
#     lGrande.append(valor)
# for valor in j:
#     lGrande.append(valor)
# for valor in k:
#         lGrande.append(valor)

# print(perJ)

# per=set(itertools.combinations(lGrande,3))




#CREO QUE YA , REVISAR COMPARANDO RESUTADOS

# for val in perI:
#     print(val)
