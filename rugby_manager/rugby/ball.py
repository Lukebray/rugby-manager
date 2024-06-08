class Ball:
    def __init__ (self, x, y):
        self.player_in_possession = None #player in possession of the ball
        self.position = (x, y) 

    def update_position(self, x, y):
        self.position = (x, y)