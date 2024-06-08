import random
import ball
import pitch

MATCH_DURATION = 10 #time in seconds
BASE_SPEED = 4 #speed of a player with 1 speed point
SPEED_INCREMENT = 0.228 #each speed point increases speed by 0.228m/s, up to a maximum of 20

class Match:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.time = 0
        self.score = {team1.name: 0, team2.name: 0}
        self.ball = ball.Ball(50, 35)
        self.events = []
        self.ball_positions = []
    

    def start_match(self):
        self.ball_positions.append(self.ball.position)

        self.time = 0
        self.events.append(f"START BALL POSITION: {self.ball.position}")
        starting_team = random.choice([self.team1, self.team2])

        self.ball.player_in_possession = random.choice(starting_team.players)
        self.events.append(f"{self.ball.player_in_possession.team} starts in possession")
        self.ball.player_in_possession.has_ball = True #player in possession of the ball now has the ball
        self.simulate_match()


    def restart_match(self, team_that_just_scored):
        self.ball.player_in_possession.has_ball = False
        self.ball.player_in_possession = None
        self.ball_positions.append((50, 35))
        self.ball.update_position(50, 35)
        
        if (team_that_just_scored == self.team1.name):
            starting_team = self.team1
        else:
            starting_team = self.team2

        self.ball.player_in_possession = random.choice(starting_team.players)
        self.ball.player_in_possession.has_ball = True #player in possession of the ball now has the ball
        
    
    def simulate_match(self):
            while self.time < MATCH_DURATION:
                self.simulate_second()
                self.time += 1
            
            return self.score, self.events, self.ball_positions
    

    def simulate_second(self):
        if self.ball.player_in_possession: #if there is a player in possession of the ball
            action = self.ball.player_in_possession.perform_action()
            self.resolve_action(action)
        else: #if no player in possession then give the ball to a random player since it's a turnover
            self.ball.player_in_possession = random.choice(self.team1.players + self.team2.players)
            self.ball.player_in_possession.has_ball = True
            self.events.append(f"Ball has been turned over to {self.ball.player_in_possession.name}")
            action = self.ball.player_in_possession.perform_action()
            self.resolve_action(action)


    def resolve_action(self, action):
        if action == "pass":
            self.handle_pass()
        elif action == "run":
            self.handle_run()
            self.check_ball_position()


    def handle_pass(self):
        current_player = self.ball.player_in_possession
        team = self.team1 if current_player in self.team1.players else self.team2
        other_team = self.team2 if team == self.team1 else self.team1
        pass_success_chance = current_player.passing / 20
        if random.random() < pass_success_chance:
            self.events.append(f"{current_player.name} has successfully passed the ball")
            players_except_current = [player for player in team.players if player != current_player]
            self.ball.player_in_possession = random.choice(players_except_current)
            self.ball.player_in_possession.has_ball = True
        else:
            self.events.append(f"{current_player.name} has failed to pass the ball. Turnover!")
            self.turnover_possession()


    def handle_run(self):
        current_player = self.ball.player_in_possession
        run_distance_per_second = BASE_SPEED + (current_player.speed - 1) * SPEED_INCREMENT

        chance_of_being_tackled = 0.5
        run_duration = random.randint(1, 10)

        for i in range(run_duration):
            if random.random() < chance_of_being_tackled:
                if current_player.team == self.team1:
                    tackler = random.choice(self.team2.players)
                elif current_player.team == self.team2:
                    tackler = random.choice(self.team1.players)
                
                tackle_success_chance = tackler.tackling / 20
                if random.random() < tackle_success_chance:
                    self.events.append(f"{tackler.name} has successfully tackled {current_player.name}")
                    distance_ball_moved = run_distance_per_second * i
                    self.calculate_ball_position(self.ball.player_in_possession.team, distance_ball_moved)
                    self.events.append(f"{current_player.name} has run {distance_ball_moved}m")
                    self.time += i
                    self.turnover_possession()
                    return
                else:
                    self.events.append(f"{current_player.name} has evaded the tackle by {tackler.name}")
            
        if current_player.team == self.team1:
            self.calculate_ball_position(self.team1, run_distance_per_second * run_duration)
        else:
            self.calculate_ball_position(self.team2, run_distance_per_second * run_duration)
        self.events.append(f"{current_player.name} has run {run_distance_per_second * run_duration }m")
        self.time += run_duration

    def handle_tackle(self):
        pass


    def check_ball_position(self):
        self.events.append(f"Ball position: {self.ball.position}")
        if self.ball.position[0] >= 100:
            self.score[self.team1.name] += 5
            self.events.append(f"{self.team1.name} has scored a try!")
            self.restart_match(self.team1.name)
        elif self.ball.position[0] <= 0:
            self.score[self.team2.name] += 5
            self.events.append(f"{self.team2.name} has scored a try!")
            self.restart_match(self.team2.name)
        else:
            return
    
    
    def turnover_possession(self):
        team_in_possession = self.get_team_in_possession()
        if team_in_possession == self.team1:
            self.ball.player_in_possession = random.choice(self.team2.players)
            self.events.append(f"Turnover! {self.team2.name} now has possession")
        else:
            self.ball.player_in_possession = random.choice(self.team1.players)
            self.events.append(f"Turnover! {self.team1.name} now has possession")


    def get_team_in_possession(self):
        if self.ball.player_in_possession:
            return self.ball.player_in_possession.team
        else:
            return None
        

    def calculate_ball_position(self, team, distance_ball_moved):
        if team == self.team1:
            self.ball.update_position(self.ball.position[0] + distance_ball_moved, self.ball.position[1])
            self.ball_positions.append(self.ball.position)
        elif team == self.team2:
            self.ball.update_position(self.ball.position[0] - distance_ball_moved, self.ball.position[1])
            self.ball_positions.append(self.ball.position)

        
        
