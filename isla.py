import random
from objetos import Fruta, Roca, Serpiente, Escorpion, Cocodrilo, Llave

class Isla:
    def __init__(self):
        self.mapa = [[None]*6 for _ in range(6)]
        self.explorado = [[False]*6 for _ in range(6)]
        self._llenar_mapa()

    def _llenar_mapa(self):
        objetos = [Llave(), Cocodrilo()] + [Fruta()]*3 + [Roca()]*3 + [Serpiente()]*2 + [Escorpion()]*2
        while len(objetos) < 36:
            objetos.append(random.choice([Fruta(), Roca(), Serpiente(), Escorpion()]))
        random.shuffle(objetos)

        k = 0
        for i in range(6):
            for j in range(6):
                self.mapa[i][j] = objetos[k]
                k += 1

    def mostrar_mapa(self):
        for i in range(6):
            for j in range(6):
                print(str(self.mapa[i][j]) if self.explorado[i][j] else "■", end=" ")
            print()

    def explorar(self, x, y, jugador):
        if not (0 <= x < 6 and 0 <= y < 6):
            print("Coordenadas inválidas.")
            return False
        if self.explorado[x][y]:
            print("Esa celda ya fue explorada.")
            return False
        self.explorado[x][y] = True
        self.mapa[x][y].interactuar(jugador)
        return True

    def mostrar_final(self):
        for fila in self.mapa:
            print(" ".join(str(obj) for obj in fila))