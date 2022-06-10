from random import randint
from propriedade import Propriedade


class Tabuleiro:
    def __init__(self) -> None:
        self.jogadores = []
        self.rodadas = 0
        self.vencedor = None
        self.propriedades = [Propriedade(i) for i in range(int(20))]

    def dado(self):
        # dado de 6 lados
        return randint(1, 6)
