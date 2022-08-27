#DEBO: Introducir un registro de ventas desde una lista de tuplas como parametro de autopartes
#y convertirlo luego en un diccionario con lista de tuplas

#Autopartes debe generar un dict que le llega a consultar registro como 'ventas' 
#el ventas de autopartes no es el mismo de consultar registro
def autoPartes(ventas:list)->dict:
    diccionario= {}
    for i in ventas:
        if diccionario.get(i[0]) ==None:
        # i seria cada linea larga de codigo en ventas
            diccionario[i[0]] = []
        diccionario[i[0]].append(([i[1],i[2],i[3]],i[4],i[5],i[6],i[7]))

    return diccionario

def consultaRegistro(ventas, idProducto)->str:
    if idProducto in ventas:

        for i in ventas[idProducto]:
        #Si id esta en ventas , armar la cadena de salida
            print(f'Producto consultado: {idProducto} Descripción {i[0]}')
    else: 
        print('No hay registro de venta')

ventas = [
    (2001,'rosca', 'PPT', 2,56, 'Laura Morero', 3456, '12/06/2020'),
    (2010,'bujia', 'KPT', 8,86, 'Linux Mendel', 1243, '12/06/2020'),
    (2010,'bujia', 'WPT', 3,56, 'Otto Openheimer', 1243, '12/06/2020'),
]
#print(autoPartes(ventas))
print(consultaRegistro(autoPartes(ventas),2010))
