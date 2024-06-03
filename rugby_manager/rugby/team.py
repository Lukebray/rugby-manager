class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def __str__(self):
        return f"{self.name} ({len(self.players)} players)"