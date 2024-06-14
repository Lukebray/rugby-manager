import random
from ball import Ball

MATCH_DURATION = 30  # time in seconds
BASE_SPEED = 4  # speed of a player with 1 speed point
SPEED_INCREMENT = 0.228  # each speed point increases speed by 0.228m/s, up to a maximum of 20

class Match:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.team_in_possession = random.choice([team1, team2])
        self.time = 0
        self.score = {team1.name: 0, team2.name: 0}
        self.ball = Ball(50, 35)
        self.events = []
        self.ball_positions = []


    def start_match(self):
        self.restart_match(self.team_in_possession)
        self.simulate_match()


    def restart_match(self, team_to_get_possession):
        self.ball.remove_possession()
        self.ball_positions.append((50, 35))  # add ball restart position
        self.team_in_possession = team_to_get_possession
        self.events.append(f"{team_to_get_possession} starts in possession")
        self.ball.assign_possession(random.choice(team_to_get_possession.players))


    def simulate_match(self):
        while self.time < MATCH_DURATION:
            self.simulate_second()
            self.time += 1

        return self.score, self.events, self.ball_positions


    def simulate_second(self):
        if self.ball.player_in_possession:  # if there is a player in possession of the ball
            action = self.ball.player_in_possession.perform_action()
            self.resolve_action(action) #get the outcome of the action
            self.check_for_score()
        else:  # if no player in possession then give the ball to a random player since it's a turnover
            self.ball.player_in_possession = random.choice(self.team1.players + self.team2.players)
            self.ball.player_in_possession.has_ball = True
            self.events.append(f"Ball has been turned over to {self.ball.player_in_possession.name}")
            action = self.ball.player_in_possession.perform_action()
            self.resolve_action(action)

    def resolve_action(self, action):
        if action == "run":
            self.handle_run()


    def handle_run(self):
        current_player = self.ball.player_in_possession
        run_distance_per_second = BASE_SPEED + (current_player.speed - 1) * SPEED_INCREMENT
        run_duration = random.randint(1, 5)  # random duration of run between 1 and 4 seconds

        for i in range(run_duration):
            if self.team_in_possession == self.team1:
                tackling_player = random.choice(self.team2.players)
            else:
                tackling_player = random.choice(self.team1.players)

            distance_run_so_far = run_distance_per_second * i
            is_tackle_made = self.handle_tackle(tackling_player, current_player, distance_run_so_far)
            
            if is_tackle_made:
                self.events.append(f"{current_player.name} ran {distance_run_so_far}m")
                self.events.append(f"{tackling_player.name} made a tackle on {current_player.name}")
                if self.team_in_possession == self.team1:
                    self.ball.update_position(self.ball.position[0] - distance_run_so_far, self.ball.position[1])
                    self.check_for_score()
                else:
                    self.ball.update_position(self.ball.position[0] + distance_run_so_far, self.ball.position[1])
                
                self.ball_positions.append(self.ball.position)
                self.check_for_score()
                self.turnover_possession()
                break
            else:
                self.events.append(f"{current_player.name} ran {distance_run_so_far}m")
                if self.team_in_possession == self.team1:
                    self.ball.update_position(self.ball.position[0] + distance_run_so_far, self.ball.position[1])
                else:
                    self.ball.update_position(self.ball.position[0] - distance_run_so_far, self.ball.position[1])

                self.ball_positions.append(self.ball.position)
                self.check_for_score()


    def handle_tackle(self, tackling_player, current_player, distance_run_so_far):
        tackling_chance = tackling_player.tackling / 20
        if random.random() < tackling_chance:
            return True # tackle successful
        else:
            return False # tackle unsuccessful


    def check_for_score(self):
        if self.ball.position[0] <= 0:
            scoring_team = self.team2
            self.score[scoring_team.name] += 5
            self.events.append(f"TRY by {scoring_team.name}!")
            self.restart_match(scoring_team)
        elif self.ball.position[0] >= 100:
            scoring_team = self.team1
            self.score[scoring_team.name] += 5
            self.events.append(f"TRY by {scoring_team.name}!")
            self.restart_match(scoring_team)


    def turnover_possession(self):
        self.team_in_possession = self.team1 if self.team_in_possession == self.team2 else self.team2
        player_in_possession = random.choice(self.team_in_possession.players)
        self.ball.turnover_possession(player_in_possession)
