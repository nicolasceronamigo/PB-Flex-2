
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.personaje = None

    def seleccionar_personaje(self, personaje):
        self.personaje = personaje
        print(f"{self.nombre} seleccionó al personaje {self.personaje.nombre}")
    
    def mostrar_personaje(self):
        if self.personaje:
            print(f"El jugador {self.nombre} utiliza a {self.personaje.nombre}")
        else:
            print(f"El jugador {self.nombre} no tiene un personaje seleccionado")