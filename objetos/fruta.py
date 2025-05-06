from objetos.base import ObjetoIsla

class Fruta(ObjetoIsla):
    def interactuar(self, jugador):
        jugador.vidas += 1
        print("Encontraste una fruta. Ganas una vida.")
    def __str__(self):
        return "🍍"