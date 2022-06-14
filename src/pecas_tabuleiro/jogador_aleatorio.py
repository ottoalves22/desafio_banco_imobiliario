from random import randint
from .jogador_simples import JogadorSimples
from .propriedade import Propriedade

class JogadorAleatorio(JogadorSimples): 
    tipo = 'Aleatorio'
    def compra_aluguel(self, propriedade: Propriedade, compra=False):
        if propriedade.proprietario:
            if propriedade.proprietario == self: #propriedade já deste jogador
                pass
            elif propriedade.proprietario != None and propriedade.proprietario != self:
                self.paga(propriedade, compra)
        elif propriedade.proprietario == None:
            if randint(0, 1) == 1: # 50%
                self.paga(propriedade, True)