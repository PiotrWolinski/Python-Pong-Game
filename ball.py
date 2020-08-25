from pygame import Rect

class Ball(Rect):
    size = 20

    def __init__(self, position_x, position_y, screen_resolution):
        self.position_x = position_x
        self.position_y = position_y
        self.screen_resolution = screen_resolution
        self.speed_x = 10
        self.speed_y = 10
        super(Ball, self).__init__(self.position_x, self.position_y, self.size, self.size)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        
    def check_position(self):
        if self.bottom >= self.screen_resolution[1] or self.top <= 0:
            self.speed_y *= -1
        if self.left <= 0 or self.right >= self.screen_resolution[0]:
            self.speed_x *= -1

    def check_collision(self, player_1, player_2):
        if self.colliderect(player_1) or self.colliderect(player_2):
            self.speed_x *= -1
     