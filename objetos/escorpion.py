from objetos.base import ObjetoIsla

class Escorpion(ObjetoIsla):
    def interactuar(self, jugador):
        jugador.vidas -= 1
        print("¡Un escorpión! Pierdes una vida.")
    def __str__(self):
        return "🦂"