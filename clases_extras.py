class Persona:
    def __init__(this, name, age, *t, **d):
        this.name = name
        this.age = age
        this.tuple = t
        this.dictionary = d

    def print_name(this):
        print(this.name, "tiene", this.age, "años")
        print("Valores(Tupla): ", this.tuple)
        print("Diccionario: ",this.dictionary)
    
persona = Persona("Nicole",35, 2,4,5, m="manzana", p="platano", n="naranja")
persona.print_name()