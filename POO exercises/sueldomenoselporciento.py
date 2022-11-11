
class Persona:
   
    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.edad=int(input("Ingrese la edad: "))
 
 
    
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
 
class Empleado(Persona):
    
    def __init__(self):

        super().__init__()
        self.sueldo=float(input("Ingrese el sueldo: "))
 

    def mostrar(self):
        super().mostrar()
        print("Sueldo Normalmente: ",self.sueldo)

    
    def pagar_impuestos(self):
        if self.sueldo > 3600000:
            print("Su sueldo sera del 3.5% menos" )
           
           
        if self.sueldo * 0.035:
            print ("Su disminucion total sera de :",self.sueldo * 0.035)

        if self.sueldo:
            print ("Su sueldo total sera de:",self.sueldo - 0.035)

        else:
            print("Su Sueldo no se vera Afectado por no pagar impuestos  ")
 
# bloque principal
persona1=Persona()
persona1.mostrar()
empleado1=Empleado()
empleado1.mostrar()
empleado1.pagar_impuestos()
