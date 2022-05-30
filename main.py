# import matplotlib.pyplot as plt
import pygame
import numpy as np
import time
pygame.init()

BLACK = 0, 0, 0
WHITE = 255, 255, 255
GRAY = 128, 128, 128
TIME = 0.1

size = width, height = 600, 600
nx_cells = 60
ny_cells = 60

dimCW = (width-1)  / nx_cells
dimCH = (height-1) / ny_cells

screen = pygame.display.set_mode(size)
screen.fill(BLACK)

game_state = np.zeros((nx_cells, ny_cells))

# Automata palo
game_state[10, 20] = 1
game_state[11, 20] = 1
game_state[12, 20] = 1
# Automata nave
game_state[21, 21] = 1
game_state[22, 22] = 1
game_state[22, 23] = 1
game_state[21, 23] = 1
game_state[20, 23] = 1

while 1:
    # Registro de eventos del teclado y el raton
    ev = pygame.event.get()

    for row in range(ny_cells):
        for col in range(nx_cells):
            rect = pygame.rect.Rect((row * dimCW, col * dimCH, dimCW, dimCH))
            # pygame.draw.rect(screen, color=(255, 255, 255), rect=rect, width=1)

            if game_state[row, col] == 0:
                pygame.draw.rect(screen, color=GRAY, rect=rect, width=1)
            else:
                pygame.draw.rect(screen, color=WHITE, rect=rect, width=0)

    pygame.display.flip()

