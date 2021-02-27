# Copyright - all rights reserved to A.S.

from heuristic import Heuristic
import pygame
from player import Player


def draw_borders():
    pygame.draw.line(window, (255, 0, 0), (0, 0), (0, 600))
    pygame.draw.line(window, (255, 0, 0), (799, 0), (799, 600))
    pygame.draw.line(window, (255, 0, 0), (0, 2), (799, 2))
    pygame.draw.line(window, (255, 0, 0), (0, 599), (800, 599))


def draw_square(board, size, location):
    i = location[1]
    j = location[0]
    font = pygame.font.SysFont(None, 35)
    pygame.draw.line(window, (255, 0, 0), (i * 800 // size, 0), (i * 800 // size, 600))
    pygame.draw.line(window, (255, 0, 0), (0, j * 600 // size), (800, j * 600 // size))
    img = font.render(str(board[j][i]) + "", True, (100, 200, 100))
    window.blit(img, (i * 800 // size, j * 600 // size))


def draw_board(board, size):
    font = pygame.font.SysFont(None, 35)

    for i in range(size):
        for j in range(size):
            pygame.draw.line(window, (255, 0, 0), (i * 800 // size, 0), (i * 800 // size, 600))
            pygame.draw.line(window, (255, 0, 0), (0, j * 600 // size), (800, j * 600 // size))
            img = font.render(str(board[j][i]) + "", True, (200, 200, 200))
            window.blit(img, (i * 800 // size, j * 600 // size))


pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Max Profit Path Finder")
player = Player()
h = Heuristic(5)
h.calculate_max_profit_path()
path_stack = h.recover_path()
run = True
show = False
player_turn = True
printWinner = False
while run:
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and player_turn:
            current_location = player.current_square(pos, h.board_size)
            if player.is_legal(current_location):
                player.move(current_location, h.board)

    window.fill((0, 0, 0))
    draw_borders()
    draw_board(h.board, h.board_size)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and player.current_position == (h.board_size - 1, h.board_size - 1):
        player_turn = False
        show = True

    if player_turn:
        draw_square(h.board, h.board_size, player.current_position)

    if show:
        pygame.time.delay(1500)
        if len(path_stack) > 0:
            if len(path_stack):
                current_location = path_stack.pop()
        draw_square(h.board, h.board_size, current_location)
        if not printWinner:
            print(f"Player Profit = {player.profit}, AI Profit: {h.profit}")
            print("Player wins!" if player.profit == h.profit else "AI wins!")
            printWinner = True

    pygame.display.update()


pygame.quit()
quit()
