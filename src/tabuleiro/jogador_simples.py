from sqlalchemy import false


class JogadorSimples:
    def __init__(self, estrategia) -> None:
        self.saldo = 300
        self.posicao = 0
        self.estrategia = estrategia
        self.derrota = False

    def paga(self, preco):
        self.saldo -= preco
        if self.saldo == 0:
            self.derrota = True