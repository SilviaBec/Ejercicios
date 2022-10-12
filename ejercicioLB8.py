#Diseñar un algoritmo que permita ingresar la hora, 
# minutos y segundos, y que calcule la hora en 
# el siguiente segundo ("0<= H <=23", "0<= M <=59" "0<= S<=59").

horas=int(input("Ingrese la hora en formato militar (0-24): "))
minutos=int(input("Ingrese los minutos: "))
segundos=int(input("Ingrese los segundos: "))

if segundos >=59:
    minutos=minutos+1
    segundos='00'
    print("La hora en el siguiente segundo es: ",horas,":",minutos,":",segundos)
    if minutos>=59:
        horas=horas+1
        minutos='00'
    else:
        minutos=minutos
        
else:
    segundos=segundos+1
    print("La hora en el siguiente segundo es: ",horas,":",minutos,":",segundos)

