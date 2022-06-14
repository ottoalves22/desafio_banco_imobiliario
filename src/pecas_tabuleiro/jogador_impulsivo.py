from .jogador_simples import JogadorSimples
from .propriedade import Propriedade

class JogadorImpulsivo(JogadorSimples): 
    # O jogador impulsivo compra qualquer propriedade sobre a qual ele parar.
    #override metodo de compra pra comprar sempre

    def compra_aluguel(self, propriedade: Propriedade, compra=False):
        if propriedade.proprietario:
            if propriedade.proprietario == self: #propriedade já deste jogador
                pass
            elif propriedade.proprietario != None and propriedade.proprietario != self:
                self.paga(propriedade, compra)
        elif propriedade.proprietario == None:
            self.paga(propriedade, True) # True pra comprar sempre que der