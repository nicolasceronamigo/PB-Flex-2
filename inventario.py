class Inventario:
    def __init__(self):
        self.objetos = []
        
    def agregar_objeto(self, objeto):
        self.objetos.append(objeto)
        print(f"{objeto.nombre} ha sido agregado al inventario.")
    
    def mostrar_inventario(self):
        print("\n Inventario: ")
        #validar si lista está vacía
        if len(self.objetos) == 0:
            print("Inventario vacío")
        else:
            for obj in self.objetos:
                print(f"- {obj.nombre} ({obj.tipo})")