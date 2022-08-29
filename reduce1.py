from functools import reduce
lista=[1,2,3,4]
acumulador=0
#Programación Iterativa
for x in lista:
    acumulador +=x
print(acumulador)

#Programación Funcional
def acumular(acumulador, elemento):
    return acumulador + elemento
total=reduce(acumular,lista)
print(total)

#Programacion funcional con lambda + reduce
#a,e mis parametros acumulador y elemento
total2= reduce(lambda a,e:a+3,lista)
print(total2)