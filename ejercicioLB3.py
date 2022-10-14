#Escribir el algoritmo que permite calcular la nota 
# correspondiente al primer parcial de “análisis” 
# para un estudiante cualquiera. 
# Se debe considerar que hay dos talleres y un quiz, 
# que en conjunto valen un 30% de la nota y el resto 
# (70%) corresponde a la nota del examen parcial.

nota=0
Parcial=float(input("Ingrese la nota del parcial de Análisis: "))
taller1=float(input("Ingrese la nota del 1er Taller: "))
taller2=float(input("Ingrese la nota del 2ndo Taller: "))
quiz=float(input("Ingrese la nota del Quiz: "))
nota=(((taller1+taller2+quiz)/3)*0.3)+(0.7*Parcial)
print(nota)