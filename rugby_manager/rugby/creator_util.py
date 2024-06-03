import player
import team
import match

team1 = team.Team("Team 1", [])
team2 = team.Team("Team 2", [])

player1 = player.Player("Player 1", 10, 10)
player2 = player.Player("Player 2", 5, 5)

team1.add_player(player1)
team2.add_player(player2)


match1 = match.Match(team1, team2)
score1, score2, events = match1.simulate_match()

print(f"Final Score: {team1.name} {score1} - {team2.name} {score2}")
# for event in events:
#     print(event)