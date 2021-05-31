import random
import pygame
import sys

WIDTH = 360
HEIGHT = 480
FPS = 60
BLACK = (0,0,0)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("My 1st game")

clock = pygame.time.Clock()

run = True

while run:
    #задержка на частоту кадров
    clock.tick(FPS)
    # 1 - обработка ввода (клавиши клавиатуры, мышь)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    # 2 - изменяем игровые объекты
    # 3 - отрисовка
    screen.fill(BLACK)
    pygame.display.flip()

pygame.quit()
sys.exit()
