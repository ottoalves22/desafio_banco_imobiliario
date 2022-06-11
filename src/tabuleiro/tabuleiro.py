from random import randint
from propriedade import Propriedade
from jogador_simples import JogadorSimples


class Tabuleiro:
    def __init__(self) -> None:
        self.jogadores = []
        self.rodadas = 0
        self.vencedor = None
        self.propriedades = [Propriedade(i) for i in range(int(20))]

    def dado(self):
        # dado de 6 lados
        return randint(1, 6)

    def caminha(self, jogador: JogadorSimples):
        pos = jogador.posicao + self.dado()
        # checar se deu uma volta
        if 20 <= pos: # 20 sendo numero de propriedades
            jogador.saldo += 100 # recebe 100 de saldo
            pos -= 20 # reseta a posicao
        jogador.posicao = pos
        return pos

    def verifica_ganhador(self, jogador: JogadorSimples):
        if len(self.jogadores) == 1:
            return jogador # so restou um jogador
        if self.rodadas >= 1000: #timeout de 1000 rodadas
            vencedor = None
            dinheiro = 0
            for p in self.jogadores: # itera nos jogadores e ve qual é o com mais saldo
                if dinheiro < p.saldo:
                    dinheiro = p.dinheiro
                    vencedor = p
            return vencedor

    def jogada(self, jogador: JogadorSimples, tab):
        if jogador.saldo > 0: # checa o saldo do candango
            propriedade_atual = self.propriedades[self.caminha(jogador)]
            jogador.recebe_vende(propriedade_atual, tab)
        else:
            jogador.derrota = True
            return