class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura

base = int(input("Indica la base del rectangulo: "))
altura = int(input("Indica la altura del rectangulo: "))

rectangulo = Rectangulo(base,altura)
print("\nEl area del rectangulo es: ", rectangulo.area())