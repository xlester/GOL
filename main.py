# import matplotlib.pyplot as plt
import pygame
import numpy as np
import time
pygame.init()

BLACK = 0, 0, 0
WHITE = 255, 255, 255
TIME = 0.1

size = width, height = 800, 800
nx_cells = 80
ny_cells = 80

dimCW = (width-1)  / nx_cells
dimCH = (height-1) / ny_cells

screen = pygame.display.set_mode(size)
screen.fill(BLACK)


while 1:
    # Registro de eventos del teclado y el raton
    ev = pygame.event.get()

    for row in range(ny_cells):
        for col in range(nx_cells):
            rect = pygame.rect.Rect((row * dimCW, col * dimCH, dimCW, dimCH))
            pygame.draw.rect(screen, color=(255, 255, 255), rect=rect, width=1)

    pygame.display.flip()

