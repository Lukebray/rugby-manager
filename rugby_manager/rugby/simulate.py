import player
import team
import match

team1 = team.Team("Team 1", [])
team2 = team.Team("Team 2", [])

player1 = player.Player("T1-P1", 1, 1)
player2 = player.Player("T1-P2", 1, 1)
player3 = player.Player("T2-P1", 20, 20)
player4 = player.Player("T2-P2", 20, 20)

team1.add_player(player1)
team1.add_player(player2)
team2.add_player(player3)
team2.add_player(player4)

match1 = match.Match(team1, team2)
match1.start_match()

print(f"Final score: {match1.score}")
# for event in match1.events:
#     print(event)
