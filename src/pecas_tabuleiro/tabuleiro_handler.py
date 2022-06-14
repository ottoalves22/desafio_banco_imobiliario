import random
from .tabuleiro import Tabuleiro
from .jogador_aleatorio import JogadorAleatorio
from .jogador_cuidadoso import JogadorCuidadoso
from .jogador_exigente import JogadorExigente
from .jogador_impulsivo import JogadorImpulsivo


def cria_tabuleiro():
    tabuleiro = Tabuleiro()
    cria_jogadores(tabuleiro)
    return tabuleiro

def cria_jogadores(tabuleiro: Tabuleiro):
    estrategias = [JogadorAleatorio(), JogadorCuidadoso(), JogadorExigente(), JogadorImpulsivo()]
    random.shuffle(estrategias)
    tabuleiro.jogadores = estrategias


