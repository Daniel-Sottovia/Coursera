"""
Pygame
"""

import sys, pygame

pygame.init()

size = widht, height = 800, 600
speed = [3, 5]
black = 0, 50, 20

screen = pygame.display.set_mode(size) # Cria a tela

ball = pygame.image.load('intro_ball.gif')
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Configura o botão para fechar a aba
            sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > widht: # Muda a velocidade horizontal
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height: # Muda a velocidade vertical
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()