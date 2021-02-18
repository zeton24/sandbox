import numpy as np
from pydantic import BaseModel, ValidationError, validator


class Settings(BaseModel):
    number_of_players : int
    size : int


class TicTacToe():
    def __init__(self, settings):
        self.players = settings.number_of_players
        self.size = settings.size
        self.how_many_to_win = 3
        self.board = self.create_board(settings.size)
        self.whose_turn = np.random.choice(['X','O'])
        self.free_fields = list(range(settings.size**2))
        self.moves =  {'X': set(), 'O': set()}


    def how_to_play(self):
        print('How to play: choose a number of field where you want to put a mark.\n' \
             'Fields are numerate from left to right and top-bottom starting with 1.\n')
        print("Let's begin!")

    def create_board(self,size):
        board = np.chararray(shape=(size,size), unicode=True)
        return board

    def make_move(self, player, auto=False) -> None:
        if auto:
            field_number = np.random.choice(self.free_fields)
        else:
            field_number = int(input(f'{player} player moves: ')) - 1

        if field_number not in self.free_fields:
                print("You can't make this move.")
                self.make_move(player)
        else:
            x, y = np.divmod(field_number, self.size)
            self.board[x,y] = player
            self.free_fields.remove(field_number)
            self.moves[self.whose_turn].add(field_number)

    def check_winner(self) -> str:
        for i,field in enumerate(self.moves[self.whose_turn]):
            row_win = set([field + x for x in range(self.how_many_to_win)])
            column_win = set([field + self.size*x for x in range(self.how_many_to_win)])
            diagonal_win = set([field + self.size*x for x in range(self.how_many_to_win)])
            if (row_win & self.moves[self.whose_turn] ==  row_win) \
                or (column_win & self.moves[self.whose_turn] ==  column_win) \
                or (diagonal_win & self.moves[self.whose_turn] ==  diagonal_win):
                return self.whose_turn


    def print_board(self) -> None:
        print()
        for row in self.board[:-1, :]:
            print('  |  '.join(row))
            print('_' *int(np.ceil(4*self.size)))
        print('  |  '.join(self.board[-1,:]))
