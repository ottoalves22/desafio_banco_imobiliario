from jogador_simples import JogadorSimples
from tabuleiro.propriedade import Propriedade

class JogadorImpulsivo(JogadorSimples): 
    # O jogador cauteloso compra qualquer propriedade desde que ele tenha uma reserva de 80 saldo sobrando depois de realizada a compra.
    #override metodo de compra pra comprar sempre

    def compra_aluguel(self, propriedade: Propriedade, compra=False):
        if propriedade.proprietario:
            if propriedade.proprietario == self: #propriedade já deste jogador
                pass
            elif propriedade.proprietario != None and propriedade.proprietario != self:
                self.paga(propriedade, compra)
        elif propriedade.proprietario == None:
            if self.saldo - propriedade.venda >= 80: # checa se sobra um dinheirinho antes
                self.paga(propriedade, True)