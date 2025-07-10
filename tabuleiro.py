# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 6

    def __init__(self):
        self.matriz = [[Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO,
                            Tabuleiro.DESCONHECIDO],
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]]

    def tem_campeao(self):
     for i in range(3):
        resultado_linhas = 0
        resultado_colunas = 0
        for j in range(3):
            resultado_linhas += self.matriz[i][j]
            resultado_colunas += self.matriz[j][i]
        if resultado_linhas == 3 or resultado_colunas == 3:
            return Tabuleiro.JOGADOR_0
        if resultado_linhas == 18 or resultado_colunas == 18:
            return Tabuleiro.JOGADOR_X

    # Verificando diagonais
     resultado_diagonal_principal = self.matriz[0][0] + self.matriz[1][1] + self.matriz[2][2]
     resultado_diagonal_secundaria = self.matriz[0][2] + self.matriz[1][1] + self.matriz[2][0]

     if resultado_diagonal_principal == 3 or resultado_diagonal_secundaria == 3:
         return Tabuleiro.JOGADOR_0
     if resultado_diagonal_principal == 18 or resultado_diagonal_secundaria == 18:
         return Tabuleiro.JOGADOR_X

     return Tabuleiro.DESCONHECIDO