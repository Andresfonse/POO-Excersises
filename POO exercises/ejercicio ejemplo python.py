
class Alumno:
    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.nota=int(input("Nota del Alumno "))
 
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Nota: ",self.nota)
 
    def boletin(self):
        if self.nota > 3:
            print("Aprobo")
        else:
            print("No Aprobo")
 
consola1=Alumno()
consola1.mostrar()
consola1.boletin()
