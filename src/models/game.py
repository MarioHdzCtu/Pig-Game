from .player import Player


class Game:

    def __init__(self, target_score: int, players: list[Player], has_ended: bool = False, alive_players: list[Player] = None) -> None:
        self.target_score = target_score
        self.players = players
        self.has_ended = has_ended
        self.alive_players = players

    def check_game_still_running(self):
        return len(self.alive_players) == 1

    def update_alive_players(self, _id):
        self.alive_players = [player for player in self.alive_players if player.id != _id]
        
