from src.models import Player, Game

num_players = int(input('How many players will play?: '))
target_score = int(input('What is the target winning score?: '))
players: list[Player] = []

for i in range(1, num_players+1):
    name = input(f'Enter the name for player {i}: ')
    players.append(Player(name=name, id=i))

game = Game(target_score=target_score, players=players)

while not game.has_ended:

    for player in game.alive_players:
        choice = input(f'Do you want to roll player {player.name}?: (Y/n): ')
        if choice in 'Yy':
            res: int = player.roll()

            if res == 1:
                player.remove_player()
                game.update_alive_players(_id=player.id)

            if player.score == game.target_score:
                print(f'Player {player.name} won!')
                quit()

            if player.score > game.target_score:
                print(f'Player {player.name} exceeded the game score and lost. Sorry :(')
                game.update_alive_players(_id=player.id)

        if game.check_game_still_running():
            winner: Player = game.alive_players[0]
            print(f'Player {winner.name} has won!')
            quit()
