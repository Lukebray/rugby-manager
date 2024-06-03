class Player:
    def __init__(self, name, attack, defence):
        self.name = name
        self.attack = attack
        self.defence = defence
    
    def __str__(self):
        return f"{self.name} ({self.attach}, {self.defence})"


