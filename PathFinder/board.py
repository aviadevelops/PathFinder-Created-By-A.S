# Copyright - all rights reserved to A.S.

import pygame


def draw_borders(window):
    pygame.draw.line(window, (255, 0, 0), (0, 0), (0, 600))
    pygame.draw.line(window, (255, 0, 0), (799, 0), (799, 600))
    pygame.draw.line(window, (255, 0, 0), (0, 2), (799, 2))
    pygame.draw.line(window, (255, 0, 0), (0, 599), (800, 599))


def draw_square(board, size, location, window):
    i = location[1]
    j = location[0]
    font = pygame.font.SysFont(None, 35)
    pygame.draw.line(window, (255, 0, 0), (i * 800 // size, 0), (i * 800 // size, 600))
    pygame.draw.line(window, (255, 0, 0), (0, j * 600 // size), (800, j * 600 // size))
    img = font.render(str(board[j][i]) + "", True, (100, 200, 100))
    window.blit(img, (i * 800 // size, j * 600 // size))


def draw_board(board, size, window):
    font = pygame.font.SysFont(None, 35)

    for i in range(size):
        for j in range(size):
            pygame.draw.line(window, (255, 0, 0), (i * 800 // size, 0), (i * 800 // size, 600))
            pygame.draw.line(window, (255, 0, 0), (0, j * 600 // size), (800, j * 600 // size))
            img = font.render(str(board[j][i]) + "", True, (200, 200, 200))
            window.blit(img, (i * 800 // size, j * 600 // size))
