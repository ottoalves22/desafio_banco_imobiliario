from pecas_tabuleiro import tabuleiro_handler

def main():

    num_simulacoes = 300
    timeout = 1000 # rodadas
    '''
    Quantas partidas terminam portime out (1000 rodadas);
    Quantos turnos em média demora uma partida;
    Qual a porcentagem de vitórias por comportamento dos jogadores;
    Qual o comportamento que mais vence.
    '''
    resultados_jogos = []
    for n in range(num_simulacoes):
        tab = tabuleiro_handler.cria_tabuleiro()
        while tab.vencedor is None:
            for j in tab.jogadores:
                tab.rodadas += 1
                if j.derrota:
                    tab.retira_jogador(j)
                ganhador = tab.verifica_ganhador(j)
                if ganhador:
                    tab.vencedor = ganhador
                    break
                tab.jogada(j)
        resultados_jogos.append(tab.fim_de_jogo(timeout))

    # falta exibir estatisticas do jeito correto
    for i in resultados_jogos:
        print(i)


if __name__ == "__main__":
    main()
