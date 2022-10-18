# Confeccionar un programa que lea 3 pares de datos, cada par de datos corresponde a la medida de la base y la altura de un triángulo. El programa deberá informar:
#         a. De cada triángulo la medida de su base, su altura y su superficie.
#         b.La cantidad de triángulos cuya superficie es mayor a 12.

contador=0
for i in range (1,4):
        print("TRIÁNGULO ",i,"Ingrese el valor de la BASE del triángulo ",i,":")
        base=float(input())
        print("TRIÁNGULO ",i,"Ingrese el valor de la ALTURA del triángulo ",i,":")
        altura=float(input())
        print("RESUMEN TRIÁNGULO ",i,"\nBase: ",base,"\nAltura: ",altura,"\nSuperficie: ",((base*altura)/2))
        print('----------------------------------')
        if(((base*altura)/2)>12):
            contador=contador+1
print("Hay ",contador,' triángulos cuya superficie es mayor a 12')
