from objetos.base import ObjetoIsla

class Llave(ObjetoIsla):
    def interactuar(self, jugador):
        jugador.gana = True
        print("¡Encontraste la llave! ¡Ganaste!")
    def __str__(self):
        return "🗝"