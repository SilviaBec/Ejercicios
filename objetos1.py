class Persona:
    def crear(self, nombre:str,apellido:str):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar(self):
        print(self.nombre,self.apellido)

x= Persona()
x.crear('Camilo','Arce')
x.mostrar()


class Estudiante:
    def __init__(self,nombre:str,apellido:str):
        self.nombre=nombre
        self.apellido=apellido
        self.nota = float(input('Digite la nota del estudiante:\n'))

    def imprimir(self):
        print(self.nombre, self.apellido,self.nota)
    
    def aprobar(self):
        print('Aprobo') if self.nota >= 3.0 else print('no aprobo')

y= Estudiante('Juan','Pinto')
y.nombre = 'Pablo'
y.imprimir()
y.aprobar()