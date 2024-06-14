class Ball:
    def __init__(self, x, y):
        self.position = [x, y]
        self.player_in_possession = None

    def update_position(self, x, y):
        self.position = [x, y]

    def turnover_possession(self, player_in_possession):
        self.remove_possession()
        self.assign_possession(player_in_possession)

    def remove_possession(self):
        self.player_in_possession = None

    def assign_possession(self, player):
        self.player_in_possession = player
        player.has_ball = True
        