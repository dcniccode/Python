class Persona:
    """ Cuando no esta encapsulado, esta publico
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    """
    """Encapsulamiento se pone en privado"""
    def __init__(self, nombre):
        self.__nombre = nombre
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre = nombre
"""
Persona.nombre = "Daniela"
Persona.edad = 18
"""
persona = Persona("Daniel")
print(persona.getNombre())

persona.setNombre("Karla")
print(persona.getNombre())
"""
#Creacion de un objeto
persona = Persona("Tony",35)
print(persona.nombre)
print(persona.edad)
print(id(persona))

persona1 = Persona("Ziva",24)
print(persona1.nombre)
print(persona1.edad)
print(id(persona1))
"""