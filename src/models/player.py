import random
from .TurnResult import TurnResult

class Player:

    def __init__(self, name: str, id: int, score: int = 0, lost: bool = False) -> None:
        self.name = name
        self.id = id
        self.score = score
        self.lost = lost

    def update_score(self, value: int):
        self.score += value
        print(f'Player {self.name} got a {value}. Your new score is {self.score}')

    def remove_player(self):
        print('You got a 1. You have lost.')
        self.lost = True

    def roll(self) -> int:
        value = random.choice(range(1, 7))
        if value != 1:
            print(f'Player {self.name} got a {value}')
        self.score += value
        return value
 
