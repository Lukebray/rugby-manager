class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.score = 0

    def __str__(self):
        return f"{self.name} ({len(self.players)} players)"
    
    def add_player(self, player):
        self.players.append(player)
        player.team = self

    def remove_player(self, player):
        self.players.remove(player)
        player.team = None
    
    def get_score(self):
        return self.score