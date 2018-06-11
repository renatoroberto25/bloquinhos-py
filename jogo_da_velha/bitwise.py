'''Bitwise TicTacToe game'''
X_CHAR, O_CHAR, E_CHAR = 'xo '
A1, A2, A3, B1, B2, B3, C1, C2, C3 = (1 << n for n in range(0, 9))


def char_taken(x_game, o_game, cell):
    '''Returns the char representing the player who has taken a square'''
    return x_game & cell and X_CHAR or o_game & cell and O_CHAR or E_CHAR


def str_game(x_game, o_game):
    '''Prints two magic numbers as a TicTacToe game'''
    cells = (A1, B1, C1, A2, B2, C2, A3, B3, C3)
    char_rows = [char_taken(x_game, o_game, cell) for cell in cells]

    head = '     A   B   C'
    sep = '     - + - + -'
    line1 = ' 1   {} | {} | {}'.format(*char_rows[0:3])
    line2 = ' 2   {} | {} | {}'.format(*char_rows[3:6])
    line3 = ' 3   {} | {} | {}'.format(*char_rows[6:9])

    return '\n'.join([head, line1, sep, line2, sep, line3])


def square_str(cell_id):
    '''Converts a string to match one of the cell IDs'''
    col, row = cell_id
    offset_x = int(row) - 1
    offset_y = {'a': 0, 'b': 1, 'c': 2}[col] * 3
    return 1 << (offset_y + offset_x)


def is_won(game):
    '''Test if a game matches any win condition'''
    taken = lambda condition: all(game & cell for cell in condition)
    win_conditions = (
        (A1, A2, A3), (B1, B2, B3), (C1, C2, C3),
        (A1, B1, C1), (A2, B2, C2), (A3, B3, C3),
        (A1, B2, C3), (C1, B2, A3)
    )
    return any(map(taken, win_conditions))


def run(x_game, o_game, turn=X_CHAR):
    '''Main game loop'''
    print(str_game(x_game, o_game))
    prompt = '{}>> '.format(turn)
    play = square_str(input(prompt).lower())

    if play & (x_game | o_game):
        return run(x_game, o_game, turn)

    next_x_game = x_game | play if turn == X_CHAR else x_game
    next_o_game = o_game | play if turn == O_CHAR else o_game

    if any(map(is_won, (next_x_game, next_o_game))):
        return {'winner': turn}
    return run(next_x_game, next_o_game, X_CHAR if turn == O_CHAR else O_CHAR)


def main():
    '''Runs the main game loop and prints the winner afterwards'''
    print('Tic Tac Toe!')
    print(run(0, 0)['winner'], 'won!')
    if input('New game? ') in 'yY':
        main()


if __name__ == '__main__':
    main()
