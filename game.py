import pygame, sys, turtle
from player import Player
from ball import Ball

pygame.init()

FPS = 30
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480
RESOLUTION = (SCREEN_WIDTH, SCREEN_HEIGHT)

clock = pygame.time.Clock()

screen = pygame.display.set_mode(RESOLUTION)

pygame.display.set_caption('Pong!')

running = True

ball = Ball((SCREEN_WIDTH - Ball.size) // 2, (SCREEN_HEIGHT - Ball.size) // 2, RESOLUTION)
player_1 = Player(2 * Player.size_x, (SCREEN_HEIGHT - Player.size_y) // 2, RESOLUTION)
player_2 = Player(SCREEN_WIDTH - Player.size_x * 3 , (SCREEN_HEIGHT - Player.size_y) // 2, RESOLUTION)

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

    if pressed[pygame.K_UP]:
        player_2.move_up()
    if pressed[pygame.K_DOWN]:
        player_2.move_down()

    if pressed[pygame.K_w]:
        player_1.move_up()
    if pressed[pygame.K_s]:
        player_1.move_down()

    screen.fill((0, 0, 0))
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    pygame.draw.rect(screen, (255, 255, 255), player_1)
    pygame.draw.rect(screen, (255, 255, 255), player_2)
    ball.move()
    ball.check_position()
    ball.check_collision(player_1, player_2)

    pygame.display.flip()
    clock.tick(FPS)