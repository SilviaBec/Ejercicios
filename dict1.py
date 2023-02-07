#Ordenar por clave:
d1={
    'ravi': 10,
    'rajnish': 9,
    'sanjeev': 15, 
    'yash': 2, 
    'suraj': 
    32
    }
#Solucion:
llaves=list(d1.keys())
llaves.sort()
resultado= {i:d1[i] for i in llaves}
print(resultado)

# o tambien:
resultado2={}
for x in llaves:
    resultado2[x]=d1[x]
print(resultado2)
