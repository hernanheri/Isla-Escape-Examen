from objetos.base import ObjetoIsla

class Cocodrilo(ObjetoIsla):
    def interactuar(self, jugador):
        jugador.vidas = 0
        jugador.pierde = True
        print("¡Te atacó un cocodrilo! Fin del juego.")
    def __str__(self):
        return "🐊"