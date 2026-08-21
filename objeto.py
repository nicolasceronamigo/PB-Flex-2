class Objeto:
    def __init__(self, nombre: str, tipo: str):
        self.nombre: str= nombre
        self.tipo: str = tipo
    
    def mostrar_informacion(self):
        print(f"Objeto {self.nombre}")
        print(f"Tipo {self.tipo}")