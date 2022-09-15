#r, de read para leer archivos: abre un archivo para lectura
#r es el valor x defecto. Si el archivo no existe sale error

# w es write, escribir: Abre el archivo para escribir desde el inicio del archivo
# pero no guarda datos anteriores. Si el archivo no existe lo crea

#a, agregar: abre el archivo para agregar info. Si el archivo no existe lo crea

archivo=open('prueba.txt', 'r')
print(archivo.read())
archivo.close()

archivo2= open('prueba2.txt','w')
#.write metodo pora escribir sobre el archivo
archivo2.write('ke cringeeeeeeeeeeeeeeee')
archivo2.close()


lista=['Medellin','Popayan', 'Cali']
archivo2= open('prueba2.txt','w', encoding='utf-8')
for i in lista:
    archivo2.write(i)
    archivo2.write('\n')
archivo2.close()


lista2=['Bogota','Pereira', 'Tunja']
archivo2= open('prueba2.txt','a', encoding='utf-8')
for i in lista2:
    archivo2.write(i)
    archivo2.write('\n')
archivo2.close()