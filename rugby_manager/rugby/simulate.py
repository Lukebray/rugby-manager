import player
import team
import match
import pitch

team1 = team.Team("Team 1", [])
team2 = team.Team("Team 2", [])

player1 = player.Player("T1-P1", 10, 10, 10)
player2 = player.Player("T1-P2", 10, 10, 10)
player3 = player.Player("T2-P1", 10, 10, 10)
player4 = player.Player("T2-P2", 10, 10, 10)

team1.add_player(player1)
team1.add_player(player2)
team2.add_player(player3)
team2.add_player(player4)

match1 = match.Match(team1, team2)
match1.start_match()

print(f"Final score: {match1.score}")
for event in match1.events:
    print(event)
print(f"Final score: {match1.score}")

pitch1 = pitch.Pitch(length=100, width=70)
pitch1.animate(match1)
print(f"Ball positions: {match1.ball_positions}")
