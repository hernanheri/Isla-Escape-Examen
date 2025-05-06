from jugador import Jugador
from isla import Isla

class JuegoIsla:
    def __init__(self):
        self.jugador = Jugador()
        self.isla = Isla()

    def jugar(self):
        while not self.jugador.gana and self.jugador.vidas > 0 and not self.jugador.pierde:
            self.isla.mostrar_mapa()
            print(f"Vidas: {self.jugador.vidas}")
            try:
                x = int(input("Fila (0-5): "))
                y = int(input("Columna (0-5): "))
                self.isla.explorar(x, y, self.jugador)
            except ValueError:
                print("Entrada inválida.")

        self.finalizar()

    def finalizar(self):
        print("\n--- Fin del juego ---")
        if self.jugador.gana:
            print("¡Ganaste!")
        else:
            print("Has perdido.")
        print(f"Vidas restantes: {self.jugador.vidas}")
        print("Mapa final:")
        self.isla.mostrar_final()