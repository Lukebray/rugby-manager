import random

class Player:
    def __init__(self, name, speed, passing, tackling):
        self.name = name
        self.speed = speed
        self.passing = passing
        self.tackling = tackling
        self.team = None
        self.has_ball = False
        
    def __str__(self):
        return f"{self.name} ({self.speed} speed, {self.passing} passing, {self.tackling} tackling)"
        
    def perform_action(self):
        actions = ["pass", "run"]
        return random.choice(actions) #for now just return a random action
    

    def get_team(self):
        return self.team


