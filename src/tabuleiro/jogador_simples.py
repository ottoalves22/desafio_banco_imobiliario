from javaproperties import Properties
from sqlalchemy import false
from propriedade import Propriedade


class JogadorSimples:
    def __init__(self, estrategia) -> None:
        self.saldo = 300
        self.posicao = 0
        self.estrategia = estrategia
        self.derrota = False

    def paga(self, propriedade: Propriedade, compra=False):
        if compra == False:
            valor_transacao = self.saldo - propriedade.aluguel
            self.saldo -= propriedade.aluguel
            if self.saldo <= 0:
                self.derrota = True
            propriedade.proprietario.saldo += valor_transacao # caso o pagador perca o dinheiro restante vem para o proprietario de toda forma
        else:
            self.saldo -= propriedade.venda
            if self.saldo <= 0:
                self.derrota = True # aqui o usuario perde o dinheiro
            else:
                propriedade.proprietario = self


    def compra_aluguel(self, propriedade: Propriedade, compra=False):
        if propriedade.proprietario:
            if propriedade.proprietario == self: #propriedade já deste jogador
                pass
            elif propriedade.proprietario != None and propriedade.proprietario != self:
                self.paga(propriedade, compra)
        elif compra and propriedade.proprietario == None:
            self.paga(propriedade, compra)

