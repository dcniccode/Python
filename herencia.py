class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    #sobreescribimos el metodo str de la clase object
    def __str__(self):
        return "Nombre: " + self.nombre + ", edad: " + str(self.edad)
    
class Empleado(Persona):
    def __init__(self, nombre,edad, sueldo):
        super().__init__(nombre,edad)
        self.sueldo = sueldo
        
    def __str__(self):
        return super().__str__() + ", Sueldo: " + str(self.sueldo)
    
        
persona = Persona("Juan",28)
print(persona)

empleado = Empleado("Daniel",30,5000)
print(empleado)