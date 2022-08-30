lista=[]
for i in range(9):
    lista.append(i)
print(lista)
#Si tengo un solo elemento de instruccion y un elemento iterable
#lo puedo expresar asi
#a mi lista le voy a ir agregando un valor que es i
# lista.append(i) , la expresion es i entonces empiezo con eso
#luego lo meto en una lista []
print([i for i in range(9)])

lista=[i for i in 'Silvia']
print(lista)

bases=[2,4,6]
lista=[i**2 for i in bases]
print(lista)

lista=list(map(lambda x:x**2,bases))
print(lista)