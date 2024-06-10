import player
import team
import match
import pitch


# Create teams
team1 = team.Team("Team 1", [])
team2 = team.Team("Team 2", [])

# Create players and add to teams
player1 = player.Player("T1-P1", 20, 20, 20)
player2 = player.Player("T1-P2", 10, 10, 10)
player3 = player.Player("T2-P1", 10, 10, 10)
player4 = player.Player("T2-P2", 1, 1, 1)

team1.add_player(player1)
team1.add_player(player2)
team2.add_player(player3)
team2.add_player(player4)

# Start the match
match1 = match.Match(team1, team2)
match1.start_match()

# Print match information for debugging
for event in match1.events:
    print(event)
print(f"Final score: {match1.score}")

# Create a Pitch object
pitch1 = pitch.Pitch(length=100, width=70, ball_positions=match1.ball_positions)
pitch1.animate_ball(match1.ball)


