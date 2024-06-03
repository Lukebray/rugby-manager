class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.score = 0

    def __str__(self):
        return f"{self.name} ({len(self.players)} players)"
    
    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)
    
    def get_attack_strength(self):
        return sum(player.attack for player in self.players)
    
    def get_defence_strength(self):
        return sum(player.defence for player in self.players)
    
    def get_scroe(self):
        return self.score