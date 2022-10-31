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

mix=i,j,k
print(mix)
perI= itertools.permutations(i)
perJ= itertools.permutations(j)
perK= itertools.permutations(k)
lGrande=[]
for valor in i:
    lGrande.append(valor)
for valor in j:
    lGrande.append(valor)
for valor in k:
        lGrande.append(valor)

per=set(itertools.permutations(lGrande,3))

for val in per:
    if val[0]+val[1]+val[2]!=n:
        print(val)


#CREO QUE YA , REVISAR COMPARANDO RESUTADOS

# for val in perI:
#     print(val)
