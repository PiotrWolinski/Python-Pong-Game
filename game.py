import pygame, sys

pygame.init()

FPS = 30

RESOLUTION = (720, 480)

clock = pygame.time.Clock()

screen = pygame.display.set_mode(RESOLUTION)

pygame.display.set_caption('Pong!')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit(0)

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_ESCAPE]:
        running = False
        sys.exit(0)