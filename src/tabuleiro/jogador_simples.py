from sqlalchemy import false
from propriedade import Propriedade


class JogadorSimples:
    def __init__(self, estrategia) -> None:
        self.saldo = 300
        self.posicao = 0
        self.estrategia = estrategia
        self.derrota = False

    def recebe_vende(self, propriedade: Propriedade):
        pass