class Ball:
    def __init__(self, x, y):
        self.position = [x, y]
        self.player_in_possession = None

    def update_position(self, x, y):
        self.position = [x, y]