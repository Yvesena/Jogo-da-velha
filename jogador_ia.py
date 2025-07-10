# -*- coding: utf-8 -*-
from random import randint

from jogador import Jogador
from tabuleiro import Tabuleiro


class JogadorIA(Jogador):
    def __init__(self, tabuleiro: Tabuleiro, tipo: int):
        super().__init__(tabuleiro, tipo)

    def getJogada(self) -> (int, int):
        posicoes_livres = [
            (l, c)
            for l in range(3)
            for c in range(3)
            if self.tabuleiro.matriz[l][c] == Tabuleiro.DESCONHECIDO
        ]

        # Como a IA é sempre o jogador 0
        adversario = Tabuleiro.JOGADOR_X

        # Função auxiliar
        def pode_vencer(jogador, l, c):
            self.tabuleiro.matriz[l][c] = jogador
            venceu = self.tabuleiro.tem_campeao() == jogador
            self.tabuleiro.matriz[l][c] = Tabuleiro.DESCONHECIDO
            return venceu

        # 1. Verifica se a IA pode vencer
        for l, c in posicoes_livres:
            if pode_vencer(Tabuleiro.JOGADOR_0, l, c):
                return (l, c)

        # 2. Verifica se precisa bloquear o adversário
        for l, c in posicoes_livres:
            if pode_vencer(adversario, l, c):
                return (l, c)

        # 3. Ocupa o centro
        if (1, 1) in posicoes_livres:
            return (1, 1)

        # 4. Ocupa um dos cantos
        cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
        for canto in cantos:
            if canto in posicoes_livres:
                return canto

        # 5. Joga na primeira posição livre
        if posicoes_livres:
            return posicoes_livres[0]

        return None  # Sem jogadas possíveis
