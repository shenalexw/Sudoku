import pygame
pygame.init()

win = pygame.display.set_mode((1000, 800))

pygame.display.set_caption("Sudoku Simulator")

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()
