class Persona:
    def __init__(self, nombre:str, apellido:str):
        self.nombre = nombre
        self.apellido=apellido
    def imprimir(self):
        print(self.nombre,self.apellido)

x = Persona('Juan','Pinto')
x.imprimir()

#Clase Hija
class Estudiante(Persona):
    def saludo(self):
        print(f'Bienvenida {self.nombre}')
y=Estudiante('Maria','Rincon')
y.imprimir()
y.saludo()