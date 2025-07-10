# -*- coding: utf-8 -*-
from random import randint

from jogador import Jogador
from tabuleiro import Tabuleiro


class JogadorIA(Jogador):
    def getJogada(self) -> (int, int):
        posicoes_livres = [
            (l, c)
            for l in range(3)
            for c in range(3)
            if self.tabuleiro.matriz[l][c] == Tabuleiro.DESCONHECIDO
        ]

        adversario = Tabuleiro.JOGADOR_0 if self.tipo == Tabuleiro.JOGADOR_X else Tabuleiro.JOGADOR_X

        def pode_vencer(jogador, l, c):
            self.tabuleiro.matriz[l][c] = jogador
            venceu = self.tabuleiro.tem_campeao() == jogador
            self.tabuleiro.matriz[l][c] = Tabuleiro.DESCONHECIDO
            return venceu

        # R1: Vitória imediata ou bloqueio
        for l, c in posicoes_livres:
            if pode_vencer(self.tipo, l, c):
                return (l, c)
        for l, c in posicoes_livres:
            if pode_vencer(adversario, l, c):
                return (l, c)

        # R2: Criar uma "dupla ameaça" (fork)
        def conta_vitorias_possiveis(jogador, l, c):
            self.tabuleiro.matriz[l][c] = jogador
            count = 0
            for i, j in posicoes_livres:
                if (i, j) != (l, c) and pode_vencer(jogador, i, j):
                    count += 1
            self.tabuleiro.matriz[l][c] = Tabuleiro.DESCONHECIDO
            return count

        for l, c in posicoes_livres:
            if conta_vitorias_possiveis(self.tipo, l, c) >= 2:
                return (l, c)

        # R3: Centro livre
        if (1, 1) in posicoes_livres:
            return (1, 1)

        # R4: Oponente marcou canto, jogue no oposto
        cantos_opostos = { (0, 0): (2, 2), (2, 2): (0, 0), (0, 2): (2, 0), (2, 0): (0, 2) }
        for canto, oposto in cantos_opostos.items():
            l, c = canto
            if self.tabuleiro.matriz[l][c] == adversario and oposto in posicoes_livres:
                return oposto

        # R5: Marcar um canto livre
        cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
        for canto in cantos:
            if canto in posicoes_livres:
                return canto

        # R6: Qualquer jogada
        if posicoes_livres:
            return posicoes_livres[0]
        return None

