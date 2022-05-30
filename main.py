import pygame

pygame.init()
BLACK = 0, 0, 0
WHITE = 255, 255, 255

size = width, height = 600, 600
nx_cells = 100
ny_cells = 100
dimCW = width/nx_cells
dimCH = height/ny_cells

screen = pygame.display.set_mode(size)
screen.fill(BLACK)


while True:
    for row in range(ny_cells):
        for col in range(nx_cells):
            rect = pygame.rect.Rect(row*dimCW, col*dimCH, dimCW, dimCH)
            pygame.draw.rect(screen, color=WHITE, rect=rect, width=1)

    pygame.display.flip()
