from inventario import Inventario

# clase Personaje

class Personaje:
    
    def __init__(self, nombre, nivel, vida):
        self.nombre = nombre
        self.nivel = nivel
        self.vida = vida
        self.inventario = Inventario()

    def atacar(self):
        print(f"{self.nombre} realiza un ataque.")
    
    def recibir_danio(self, danio: int):
        # if self.vida - danio <= 0:
        #     self.vida = 0
        #     print(f"Personaje {self.nombre} ya no tiene vida.")
        # else:
        #     self.vida -= danio
        #     print(f"Personaje {self.nombre} recibió {danio} puntos de daño")
        #     print(f"Vida actual es: {self.vida}")
        self.vida -= danio
        if self.vida < 0:
            self.vida = 0
        print(f"Personaje {self.nombre} recibió {danio} puntos de daño")
        print(f"Vida actual es: {self.vida}")
        
    
    def usar_habilidad(self):
        print(f"self.nombre utiliza una habilidad")        
        
    def mostrar_informacion(self):
        print(f"\n Información del Personaje")
        print(f"Nombre: {self.nombre}")
        print(f"Nivel: {self.nivel}")
        print(f"Vida: {self.vida}")
