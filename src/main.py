from collections import Counter
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
    num_timeout = 0
    media_turnos = 0 # divide por 300 partidas
    exigente = 0
    cuidadoso = 0
    impulsivo = 0
    aleatorio = 0
    counter_winner = []
    for i in resultados_jogos:
        #print(i)
        if i['timeout']:
            num_timeout+=1
        media_turnos += i['rodadas']
        if i['estrategia'] == 'Exigente':
            exigente += 1
            counter_winner.append('Exigente')
        elif i['estrategia'] == 'Cuidadoso':
            cuidadoso += 1
            counter_winner.append('Cuidadoso')
        elif i['estrategia'] == 'Impulsivo':
            impulsivo += 1
            counter_winner.append('Impulsivo')
        elif i['estrategia'] == 'Aleatorio':
            aleatorio += 1
            counter_winner.append('Aleatorio')
        
    print(f'Terminadas por time out: {num_timeout}')
    print(f'Tempo médio de partida: {media_turnos/num_simulacoes} turnos por partida') # ta ruim aqui
    print(f'Procentagem de vitória: ')
    print(f'    Exigente: {(exigente*100)/num_simulacoes}%, Cuidadoso: {(cuidadoso*100)/num_simulacoes}%,')
    print(f'    Impulsivo: {(impulsivo*100)/num_simulacoes}%, Aleatorio: {(aleatorio*100)/num_simulacoes}%')
    
    c = Counter(counter_winner)
    print(f'O comportamento que mais vence: {c.most_common(1)[0][0]}')

if __name__ == "__main__":
    main()
