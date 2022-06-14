from random import randint
from .jogador_simples import JogadorSimples
from .propriedade import Propriedade

class JogadorExigente(JogadorSimples):
    tipo = 'Exigente' 
    def compra_aluguel(self, propriedade: Propriedade, compra=False):
        if propriedade.proprietario:
            if propriedade.proprietario == self: #propriedade já deste jogador
                pass
            elif propriedade.proprietario != None and propriedade.proprietario != self:
                self.paga(propriedade, compra)
        elif propriedade.proprietario == None:
            if propriedade.aluguel > 49: # checa se sobra o aluguel presta
                self.paga(propriedade, True)