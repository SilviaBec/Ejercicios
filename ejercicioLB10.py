# Realizar un algoritmo que muestre por pantalla 
# la tabla de multiplicar decreciente 
# de cualquier número, 
# ingresado entre el 1 y el 10
n=int(input("Ingrese un número del 1 al 10: "))
if n >=1 and n <=10:
    for i in range(10,0,-1):
        print(i,"x",n,"=",i*n)