# Hacer un programa que sume 5 precios de camisas (en dólares) 
# y que luego muestre el total de la venta en pesos

enPesos=0
acum=0
for n in range(1,6):
    print("Ingrese el precio de la camisa N°",n, ": ")
    precio=int(input())    
    acum+= precio
    enPesos=acum*4500
print("El precio total es de ", acum," doláres que corresponden a ",enPesos,"pesos colombianos")        

