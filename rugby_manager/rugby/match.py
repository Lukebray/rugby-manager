import random
import ball

MATCH_DURATION = 120

class Match:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.time = 0
        self.score = {team1.name: 0, team2.name: 0}
        self.ball = ball.Ball()
        self.events = []
    

    def start_match(self):
        self.time = 0
        self.events.append(f"START BALL POSITION: {self.ball.position}")
        starting_team = random.choice([self.team1, self.team2])
        self.ball.possession = random.choice(starting_team.players)
        self.ball.possession.has_ball = True #player in possession of the ball now has the ball
        self.simulate_match()


    def restart_match(self, team_that_just_scored):
        self.ball.possession.has_ball = False
        self.ball.possession = None
        self.ball.position = 50
        
        if (team_that_just_scored == self.team1.name):
            starting_team = self.team1
        else:
            starting_team = self.team2

        self.ball.possession = random.choice(starting_team.players)
        self.ball.possession.has_ball = True #player in possession of the ball now has the ball
        

    def simulate_second(self):
        if self.ball.possession: #if there is a player in possession of the ball
            action = self.ball.possession.perform_action()
            self.resolve_action(action)
        else: 
            self.ball.possession = random.choice(self.team1.players + self.team2.players)
            self.ball.possession.has_ball = True
            self.events.append(f"Ball has been turned over to {self.ball.possession.name}")
            action = self.ball.possession.perform_action()
            self.resolve_action(action)


    def resolve_action(self, action):
        if action == "pass":
            self.handle_pass()
        # elif action == "tackle":
        #     self.handle_tackle()
        # elif action == "kick":
        #     self.handle_kick()
        elif action == "run":
            self.handle_run()
            self.check_ball_position()


    def handle_pass(self):
        current_player = self.ball.possession
        team = self.team1 if current_player in self.team1.players else self.team2
        other_team = self.team2 if team == self.team1 else self.team1
        pass_success_chance = current_player.passing / 20
        if random.random() < pass_success_chance:
            self.events.append(f"{current_player.name} has successfully passed the ball")
            players_except_current = [player for player in team.players if player != current_player]
            self.ball.possession = random.choice(players_except_current)
            self.ball.possession.has_ball = True
        else:
            self.events.append(f"{current_player.name} has failed to pass the ball. Turnover!")
            self.ball.possession = random.choice(other_team.players)
            self.ball.possession.has_ball = True


    def handle_run(self):
        current_player = self.ball.possession
        base_speed = 4 #slowest player goes at 4m/s
        speed_increment = 0.228 #each speed point increases speed by 0.228m/s, up to a maximum of 20
        run_distance_per_second = base_speed + (current_player.speed - 1) * speed_increment

        run_duration = random.randint(1, 5)
        if current_player.team == self.team1:
            self.ball.position += run_distance_per_second * run_duration
        else:
            self.ball.position -= run_distance_per_second * run_duration
        self.events.append(f"{current_player.name} has run {run_distance_per_second * run_duration }m")
        self.time += run_duration


    def check_ball_position(self):
        self.events.append(f"Ball position: {self.ball.position}")
        if self.ball.position >= 100:
            self.score[self.team1.name] += 5
            self.events.append(f"{self.team1.name} has scored a try!")
            #handle_conversion()
            self.restart_match(self.team1.name)
        elif self.ball.position <= 0:
            self.score[self.team2.name] += 5
            self.events.append(f"{self.team2.name} has scored a try!")
            #handle_conversion()
            self.restart_match(self.team2.name)
        else:
            return
    

    def simulate_match(self):
        while self.time < MATCH_DURATION:
            self.simulate_second()
            self.time += 1

        return self.score, self.events
        
        
