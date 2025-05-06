from objetos.base import ObjetoIsla

class Serpiente(ObjetoIsla):
    def interactuar(self, jugador):
        jugador.vidas -= 1
        print("¡Una serpiente! Pierdes una vida.")
    def __str__(self):
        return "🐍"