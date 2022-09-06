#Implementar clase"Operaciones" que reciba 2 decimales 
#en el metodo constructor (Init) y tenga 4 metodos suma, resta,* y /

class Operaciones:
    def __init__(self, x:float,y:float):
        self.x=x
        self.y=y
    def suma(self):
        print(f'La suma es: {self.x+self.y}')
    def resta(self):
        print(f'La resta es: {self.x-self.y}')
    def mul(self):
        print(f'La multiplicacion es: {self.x*self.y}')
    def div(self):
        try:
            print(f'La división es: {self.x/self.y}')
        except:
            print(f'División invalida')

x= Operaciones(55.40,35.9)
x.suma()
x.resta()
x.mul()
x.div()