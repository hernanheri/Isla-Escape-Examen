from objetos.base import ObjetoIsla

class Roca(ObjetoIsla):
    def interactuar(self, jugador):
        print("Encontraste una roca. No pasa nada.")
    def __str__(self):
        return "⛰"