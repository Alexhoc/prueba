class Fisico:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def hacer_sonido(self):
        return "Hace un sonido genérico"  # Un sonido genérico por defecto

class Tzihue(Fisico):
    def hacer_sonido(self):
        return "esta escatologico"

class Andres(Fisico):
    def hacer_sonido(self):
        return "es increible de veras"

class Alexis(Fisico):
    def hacer_sonido(self):
        return "¡cha chau!"

class Alejandra(Fisico):
    def hacer_sonido(self):
        return "Hola"

# Crear instancias de las clases
tzihue1 = Tzihue("tzihue", "moreliano", 3)
naranjas1 = Andres("andres", "zacatecano", 2)
pp1 = Alexis("pp", "calerense", 1)
alejandra1 = Alejandra("alejandra", "fresniraki", 1)

# Acceder a los atributos y métodos de los objetos
print(f"{tzihue1.nombre} es un {tzihue1.especie} que dice: {tzihue1.hacer_sonido()}")
print(f"{naranjas1.nombre} es un {naranjas1.especie} que dice: {naranjas1.hacer_sonido()}")
print(f"{pp1.nombre} es un {pp1.especie} que dice: {pp1.hacer_sonido()}")
print(f"{alejandra1.nombre} es una {alejandra1.especie} y dice: {alejandra1.hacer_sonido()}")
