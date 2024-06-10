import random
from ball import Ball

MATCH_DURATION = 10  # time in seconds
BASE_SPEED = 4  # speed of a player with 1 speed point
SPEED_INCREMENT = 0.228  # each speed point increases speed by 0.228m/s, up to a maximum of 20

class Match:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.time = 0
        self.score = {team1.name: 0, team2.name: 0}
        self.ball = Ball(50, 35)
        self.events = []
        self.ball_positions = []

    def start_match(self):
        self.ball_positions.append(self.ball.position)  # add starting ball position

        self.time = 0
        self.events.append(f"START BALL POSITION: {self.ball.position}")
        starting_team = random.choice([self.team1, self.team2])

        self.ball.player_in_possession = random.choice(starting_team.players)
        self.events.append(f"{self.ball.player_in_possession.team} starts in possession")
        self.ball.player_in_possession.has_ball = True  # player in possession of the ball now has the ball
        self.simulate_match()

    def restart_match(self, team_that_just_scored):
        self.ball.player_in_possession.has_ball = False
        self.ball.player_in_possession = None
        self.ball_positions.append((50, 35))  # add ball restart position
        self.ball.update_position(50, 35)

        if team_that_just_scored == self.team1.name:
            starting_team = self.team1
        else:
            starting_team = self.team2

        self.ball.player_in_possession = random.choice(starting_team.players)
        self.ball.player_in_possession.has_ball = True  # player in possession of the ball now has the ball

    def simulate_match(self):
        while self.time < MATCH_DURATION:
            self.simulate_second()
            self.time += 1

        return self.score, self.events, self.ball_positions

    def simulate_second(self):
        if self.ball.player_in_possession:  # if there is a player in possession of the ball
            action = self.ball.player_in_possession.perform_action()
            self.resolve_action(action)
            self.check_for_score()
        else:  # if no player in possession then give the ball to a random player since it's a turnover
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

    def handle_pass(self):
        current_player = self.ball.player_in_possession
        team = self.team1 if current_player in self.team1.players else self.team2
        pass_success_chance = current_player.passing / 20  # will return a value between 0 and 1

        if random.random() < pass_success_chance:  # if pass is successful
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

        chance_of_being_tackled = 0.5  # 50% chance of a tackle event happening
        run_duration = random.randint(1, 10)  # random duration of run between 1 and 10 seconds

        if random.random() > chance_of_being_tackled:
            self.events.append(f"{current_player.name} is running with the ball")
            new_x = self.ball.position[0] + run_distance_per_second * run_duration
            new_y = self.ball.position[1] + run_distance_per_second * run_duration
            self.ball.update_position(new_x, new_y)
            self.ball_positions.append((new_x, new_y))
        else:
            self.events.append(f"{current_player.name} has been tackled. Turnover!")
            self.turnover_possession()


    def check_for_score(self):
        if self.ball.position[0] <= 0 or self.ball.position[0] >= 100:  # check if ball crosses goal line
            scoring_team = self.team1 if self.ball.player_in_possession in self.team1.players else self.team2
            self.score[scoring_team.name] += 5
            self.events.append(f"TRY by {scoring_team.name}!")
            self.restart_match(scoring_team.name)

    def turnover_possession(self):
        self.ball.player_in_possession.has_ball = False
        self.ball.player_in_possession = None
        self.ball_positions.append(self.ball.position)  # add turnover position
        self.ball.player_in_possession = random.choice(self.team1.players + self.team2.players)
        self.ball.player_in_possession.has_ball = True
