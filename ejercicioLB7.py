#Hacer un programa que registre el consumo realizado por los clientes de un restaurante, 
# si el consumo de cada cliente excede 50000 se hará un descuento del 20%. 
# Se debe mostrar el pago de cada cliente y el total de todos los pagos.
nClientes=int(input("Ingrese el numero de clientes: "))
acum=0

for x in range(1,nClientes+1):
    print("Ingrese el consumo del cliente ",x, ":")
    consumo=float(input())
    

    if consumo>50000:
        conDescuento = consumo-(consumo*0.2)
        print("*Aplica descuento del 20%. Valor consumo: ", conDescuento)
    else:
        conDescuento=consumo
        #print("El consumo total de los clientes es de ",acum)
    acum=acum+conDescuento
print("El consumo total es de: ",acum)