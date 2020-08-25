import pygame, sys, turtle
from player import Player

pygame.init()

FPS = 30
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480
RESOLUTION = (SCREEN_WIDTH, SCREEN_HEIGHT)

clock = pygame.time.Clock()

screen = pygame.display.set_mode(RESOLUTION)

pygame.display.set_caption('Pong!')

running = True

ball = pygame.Rect((SCREEN_WIDTH - 10) / 2, (SCREEN_HEIGHT - 10) / 2, 20, 20)
player_1 = pygame.Rect(15, (SCREEN_HEIGHT - 50) / 2, 20, 100)
player_2 = pygame.Rect(SCREEN_WIDTH - 35, (SCREEN_HEIGHT - 50) / 2, 20, 100)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_ESCAPE]:
        running = False
        pygame.quit()
        sys.exit(0)

    screen.fill((0, 0, 0))
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    pygame.draw.rect(screen, (255, 255, 255), player_1)
    pygame.draw.rect(screen, (255, 255, 255), player_2)

    pygame.display.flip()
    clock.tick(FPS)