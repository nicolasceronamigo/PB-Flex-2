from jugador import Jugador
from mago import Mago
from guerrero import Guerrero
from objeto import Objeto

#Método principal
def main():
    #crear jugador
    jugador_1 = Jugador("jugador_1")
    jugador_2 = Jugador("jugador_2")

    #crear personajes
    mago_1 = Mago("mago_1", 10, 100, 10)
    guerrero_1 = Guerrero("guerrero_1", 20, 200, 20)

    #asociar el jugador con el personaje
    jugador_1.seleccionar_personaje(mago_1)
    jugador_1.mostrar_personaje()
    jugador_2.seleccionar_personaje(guerrero_1)
    jugador_2.mostrar_personaje()

    #ataque del mago
    mago_1.atacar()
    guerrero_1.atacar()

    #habilidad del mago
    mago_1.usar_habilidad()
    guerrero_1.usar_habilidad()
    
    #crear objeto
    pocion_1 = Objeto("pocion_1", "consumible")
    staff = Objeto("staff_1", "arma")
    pocion_2 = Objeto("pocion_2", "consumible")
    espada = Objeto("espada_1", "arma")
    
    #agregar objetos
    mago_1.inventario.agregar_objeto(pocion_1)
    mago_1.inventario.agregar_objeto(staff)
    guerrero_1.inventario.agregar_objeto(pocion_2)
    guerrero_1.inventario.agregar_objeto(espada)
    
    #mostrar inventario
    mago_1.inventario.mostrar_inventario()
    guerrero_1.inventario.mostrar_inventario()
    
    #recibir daño
    mago_1.recibir_danio(10)
    guerrero_1.recibir_danio(20)
    
    #mostrar información
    mago_1.mostrar_informacion()
    guerrero_1.mostrar_informacion()
    
#si el archiva que se ejecuta se llama main, ejecuta la función main()
if __name__ == "__main__":
    main()