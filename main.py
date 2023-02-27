#!/usr/bin/env python3

import pygame

pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH = 800
HEIGHT = 600

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

font = pygame.font.SysFont('Calibri', 150)

current_key = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            current_key = pygame.key.name(event.key)

    screen.fill(WHITE)

    if current_key:
        # True for antialiasing for more realism
        text = font.render(current_key, True, BLACK)
        rect = text.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(text, rect)

    # Update the screen
    pygame.display.flip()

    pygame.time.wait(50)


pygame.quit()
