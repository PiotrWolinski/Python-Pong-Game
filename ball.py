from pygame import Rect
import random

class Ball(Rect):
    size = 20

    def __init__(self, position_x, position_y, screen_resolution):
        self.position_x = position_x
        self.position_y = position_y
        self.screen_resolution = screen_resolution
        self.speed_x = 10
        self.speed_y = 10
        self.random_speed()
        super(Ball, self).__init__(self.position_x, self.position_y, self.size, self.size)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        
    def check_position(self, score):
        if self.bottom >= self.screen_resolution[1] or self.top <= 0:
            self.speed_y *= -1
        if self.left <= 0 or self.right >= self.screen_resolution[0]:
            if self.left <= 0:
                score[1] += 1
            else:
                score[0] += 1
            self.restart()

    def check_collision(self, player_1, player_2):
        if self.colliderect(player_1) or self.colliderect(player_2):
            self.speed_x *= -1

    def random_speed(self):
        self.speed_x = random.choice((1, -1)) * self.speed_x
        self.speed_y = random.choice((1, -1)) * self.speed_y
     
    def restart(self):
        self.x = self.screen_resolution[0] // 2
        self.y = self.screen_resolution[1] // 2

        self.random_speed()
        