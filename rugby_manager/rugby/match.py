import random

class Match:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.time = 0
        self.events = []
    
    def simulate_minute(self):
        team_in_posession = self.team1 if random.random() < 0.5 else self.team2
        team_in_defence = self.team2 if team_in_posession == self.team1 else self.team1

        attack_strength = team_in_posession.get_attack_strength()
        defence_strength = team_in_defence.get_defence_strength()

        if random.random() < attack_strength / (attack_strength + defence_strength):
            self.events.append(f"{self.time}: {team_in_posession.name} scored!")
            team_in_posession.score += 1
        else:
            self.events.append(f"{self.time}: {team_in_defence.name} defended!")
    
    def simulate_match(self):
        for minute in range(80):
            self.simulate_minute()
        return self.team1.score, self.team2.score, self.events
        
