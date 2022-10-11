#Elaborar un algoritmo que permita ingresar 20 números 
# y muestre todos los números menores e iguales a 25.
arr=[]
for i in range(1,21):
    print("Ingrese el numero ",i)
    n=int(input()) 
    if n<=25:
        arr.append(n)
print("Los números menores a 25 son: ",arr)