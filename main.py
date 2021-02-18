from tictactoe import TicTacToe, Settings

print('Do you play: \n1: solo \n2: with a friend?')
num_of_players = int(input())
size = int(input('Choose size of the board NxN: '))
settings = Settings(number_of_players=num_of_players, size=size)
game = TicTacToe(settings)
game.how_to_play()
game.print_board()
winner = None
while winner == None and len(game.free_fields) != 0:
    game.whose_turn = 'X' if game.whose_turn == 'O' else 'O'
    auto = True if game.players == 1 and game.whose_turn == 'O' else False
    game.make_move(game.whose_turn, auto=auto)
    game.print_board()
    if len(game.free_fields) < 5:
        winner = game.check_winner()

if winner:
    print(f"Player {winner} wins!")
else:
    print("It's a tie.")
