class Aritmetica:
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2
    def sumar(self):
        """Se realiza la operacion con los atributos de la clase"""
        return self.operando1 + self.operando2
    
#creamos un objeto
aritmetica = Aritmetica(4,5)
print("Resultado de la suma: ", aritmetica.sumar())