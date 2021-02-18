import numpy as np
from pydantic import BaseModel, ValidationError, validator


class Settings(BaseModel):
    number_of_players : int
    size : int


class TicTacToe():
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        self.whose_turn = np.random.choice(['X','O']) 
        self.free_fields = list(range(9))
        self.winning_sets = [{0,1,2},{3,4,5},{6,7,8},
                            {0,3,6},{1,4,7},{2,5,8},
                            {0,4,8},{6,4,2}]
    def __init__(self, settings):
        self.players = settings.number_of_players
        self.moves =  {'X': set(), 'O': set()}


    def how_to_play(self):
        print('How to play: choose a number of field where you want to put a mark.\n')
        print(" 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9\n")
        print("Let's begin!")
    

    def make_move(self, player, auto=False) -> None:
        if auto:
            field_number = np.random.choice(self.free_fields)
        else:
            field_number = input(f'{player} player moves: ')
            field_number = int(field_number) - 1

        if field_number not in self.free_fields:
            print("You can't make this move.")
            self.make_move(player)
        else:
            x, y = np.divmod(field_number, 3)
            self.board[x][y] = player
            self.free_fields.remove(field_number)
            self.moves[self.whose_turn].add(field_number)


    def check_winner(self) -> str:
        result = None
        for l in self.winning_sets:
            if l.issubset(self.moves[self.whose_turn]):
                result = self.whose_turn
                break
        return result


    def print_board(self) -> None:
        rows = []
        for x in self.board:
            rows.append(f"\n {x[0]} | {x[1]} | {x[2]}\n")
        print(('-' *11).join(rows))