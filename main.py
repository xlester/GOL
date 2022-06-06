# import matplotlib.pyplot as plt
import pygame
import numpy as np
import time
pygame.init()

BLACK = 0, 0, 0
WHITE = 255, 255, 255
GRAY = 128, 128, 128
TIME = 0.01

size = width, height = 1000, 1000
nx_cells = 100
ny_cells = 100

dimCW = (width-1)  / nx_cells
dimCH = (height-1) / ny_cells

screen = pygame.display.set_mode(size)
screen.fill(BLACK)

game_board = np.zeros((nx_cells, ny_cells))
game_board[20, 20] = 1
game_board[20, 21] = 1
game_board[20, 22] = 1
game_board[20, 23] = 1
game_board[19, 23] = 1
game_board[18, 23] = 1
game_board[17, 22] = 1


pause = False

while True:
    new_game_board = np.copy(game_board)
    screen.fill(BLACK)
    time.sleep(TIME)

    # Registro de eventos del teclado y el raton
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.KEYDOWN:
            pause = not pause
        mouse_click = pygame.mouse.get_pressed()
        if sum(mouse_click) > 0:
            posY, posX = pygame.mouse.get_pos()
            cellX, cellY = int(np.floor(posX/dimCW)), int(np.floor(posY/dimCH))
            new_game_board[cellY, cellX] = not mouse_click[2]

    for row in range(ny_cells):
        for col in range(nx_cells):
            if not pause:
                neighbors = game_board[(row - 1) % ny_cells, (col - 1) % nx_cells] + \
                            game_board[(row) % ny_cells    , (col - 1) % nx_cells] + \
                            game_board[(row + 1) % ny_cells, (col - 1) % nx_cells] + \
                            game_board[(row - 1) % ny_cells, (col) % nx_cells] + \
                            game_board[(row + 1) % ny_cells, (col) % nx_cells] + \
                            game_board[(row - 1) % ny_cells, (col + 1) % nx_cells] + \
                            game_board[(row) % ny_cells    , (col + 1) % nx_cells] + \
                            game_board[(row + 1) % ny_cells, (col + 1) % nx_cells]

                # Implementando las reglas de la vida
                if game_board[row, col] == 0 and neighbors == 3:
                    new_game_board[row, col] = 1
                elif game_board[row, col] == 1 and (neighbors < 2 or neighbors > 3):
                    new_game_board[row, col] = 0

            rect = pygame.rect.Rect((row * dimCW, col * dimCH, dimCW, dimCH))

            if game_board[row, col] == 1:
                pygame.draw.rect(screen, color=WHITE, rect=rect, width=0)
            else:
                pygame.draw.rect(screen, color=GRAY, rect=rect, width=1)

    game_board = np.copy(new_game_board)
    pygame.display.flip()

