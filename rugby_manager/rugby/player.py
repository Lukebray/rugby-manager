class Player:
    def __init__(self, name, speed, strength, stamina, tackling, passing):
        self.name = name
        self.speed = speed
        self.strength = strength
        self.stamina = stamina
        self.tackling = tackling
        self.passing = passing
    
    def __str__(self):
        return f"{self.name} ({self.speed}, {self.strength}, {self.stamina}, {self.tackling}, {self.passing})"


