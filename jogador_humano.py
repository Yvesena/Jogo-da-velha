# -*- coding: utf-8 -*-
import pygame

from jogador import Jogador
from tabuleiro import Tabuleiro


class JogadorHumano(Jogador):
    def __init__(self, tabuleiro: Tabuleiro, _buttons: list, tipo: int):
        super().__init__(tabuleiro, tipo)
        self.buttons = _buttons

    def getJogada(self) -> (int, int):
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    for l in range(0, 3):
                        for c in range(0, 3):
                            b = self.buttons[l][c]
                            if b.rect.collidepoint(pygame.mouse.get_pos()):
                                # verefica se o espaço esta vazio
                                if self.tabuleiro.matriz[l][c] != Tabuleiro.DESCONHECIDO:
                                    continue
                                return (l, c)
