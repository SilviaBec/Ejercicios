# Desarrollar un programa que solicite la carga 
# de 10 números e imprima la suma de los últimos 5 valores ingresados.

acumulador=0

for i in range(1,11):
    print("Ingrese el numero",i)
    num=float(input())
    if i>5 and i<11:
        print("Número ",i,": ",num)
        acumulador +=num
            
print("Los numeros ingresados suman ",acumulador)
        
