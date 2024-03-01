class Person:
    def __init__(self, nombre, ape_paterno, ape_materno):
        self.nombre = nombre
        self._apellido_paterno = ape_paterno
        self.__apellido_materno = ape_materno
        
    def metodoPublico(self):
        self.__metodoPrivado()
        
    """Metodo privado"""
    def __metodoPrivado(self):
        print(self.nombre)
        print(self._apellido_paterno)
        print(self.__apellido_materno)
    
    def get_ape_materno(self):
        return self.__apellido_materno
    
p1 = Person("Juan" , "Flores" , "Ramos")
#p1.__metodoPrivado() no se puede acceder debido a que es privado
p1.metodoPublico()
print("")
print(p1.nombre)
print(p1._apellido_paterno) #parcialmente privado, no necesita get
print(p1.get_ape_materno())

    