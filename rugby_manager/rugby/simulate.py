import player
import team
import match


# Create teams
team1 = team.Team("Team 1", [])
team2 = team.Team("Team 2", [])

# Create players and add to teams
player1 = player.Player("T1-P1", 10, 10, 10)
player2 = player.Player("T1-P2", 10, 10, 10)
player3 = player.Player("T2-P1", 10, 10, 10)
player4 = player.Player("T2-P2", 10, 10, 10)

team1.add_player(player1)
team1.add_player(player2)
team2.add_player(player3)
team2.add_player(player4)

# Start the match
match1 = match.Match(team1, team2)
match1.start_match()

# Print match information for debugging
print(f"Final score: {match1.score}")
for event in match1.events:
    print(event)

