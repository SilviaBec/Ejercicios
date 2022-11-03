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

perI= list(itertools.combinations(i,1))

perJ= list(itertools.combinations(j,1))

perK= set(itertools.combinations(k,1))

lGrande=[]
lista2=[perI,perJ,perK]
for valor in i:
    lGrande.append(valor)
for valor in j:
    lGrande.append(valor)
for valor in k:
        lGrande.append(valor)

print(perJ)

per=set(itertools.combinations(lGrande,3))

# for val in per:
#     if val[0]+val[1]+val[2]!=n:
#         print(val)


#CREO QUE YA , REVISAR COMPARANDO RESUTADOS

# for val in perI:
#     print(val)
