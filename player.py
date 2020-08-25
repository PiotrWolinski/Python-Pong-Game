from pygame import Rect

class Player(Rect):
    size_x = 10
    size_y = 120
    speed = 6

    def __init__(self, position_x, position_y, screen_resolution):
        self.position_x = position_x
        self.position_y = position_y
        self.screen_resolution = screen_resolution
        super(Player, self).__init__(self.position_x, self.position_y, self.size_x, self.size_y)
    
    def move_up(self):
        if self.top > 0:
            self.y -= 6 

    def move_down(self):
        if self.bottom < self.screen_resolution[1]:
            self.y += 6