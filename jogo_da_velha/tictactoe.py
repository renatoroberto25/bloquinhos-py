# Versão mais organizada do jogo da velha CLI, com a mesma funcionalidade.

class TicTacToe:
    """Main TicTacToe data and operations"""

    def __init__(self, player1='X', player2='O', empty_cell=' '):
        self._player1, self._player2 = player1, player2
        self.empty = empty_cell
        self._round = 0
        self._winner = None

        self._turn = self._player1
        self._running = False

        self._reset_field()

    @property
    def running(self):
        return self._running

    @property
    def turn(self):
        return self._turn

    @property
    def field(self):
        return self._field

    @property
    def winner(self):
        return self._winner

    @property
    def round(self):
        return self._round

    def _reset_field(self):
        assert self._running == False, "The game is not running!"

        self._field = [
            [self.empty, self.empty, self.empty],
            [self.empty, self.empty, self.empty],
            [self.empty, self.empty, self.empty],
        ]

    def _next_turn(self):
        assert self._running == True, "The game is not running!"

        self._round += 1

        if self._turn == self._player1:
            self._turn = self._player2
        else:
            self._turn = self._player1


    def _set_cell(self, row, col, player):
        assert self._field[row][col] == self.empty, "This cell has already been filled!"

        self._field[row][col] = player

    def _check_gameover(self):
        assert self._running == True, "The game is not running!"

        if self._field[1][1] != self.empty:
            diagonal_1_win = self._field[0][0] == self._field[1][1] == self._field[2][2]
            diagonal_2_win = self._field[0][2] == self._field[1][1] == self._field[2][0]

            if diagonal_1_win or diagonal_2_win:
                self._winner = self._field[1][1]
                self._running = False

                return self

        for row in self._field:
            if row[0] != self.empty and row[0] == row[1] == row[2]:
                self._winner = row[0]
                self._running = False

                return self

        for i in range(0, 3):
            if self._field[0][i] != self.empty and self._field[0][i] == self._field[1][i] == self._field[2][i]:
                self._winner = self._field[0][i]
                self._running = False

                return self

        if self._round == 8:
            self._running = False

        return self

    def start_game(self):
        assert self._running == False, "Can't start a game while one is running!"

        self._running = True

        return self

    def play(self, cell):
        col = 0 if cell[0].upper() == "A" else 1 if cell[0].upper() == "B" else 2 if cell[0].upper() == "C" else 4
        row = int(cell[1]) - 1

        self._set_cell(row, col, self._turn)
        self._check_gameover()

        if self._running:
            self._next_turn()

        return self


class GabesT3:
    """TicTacToe CLI front end"""

    def __init__(self, game):
        self._game = game

    def write_game(self):
        g = self._game.field

        print(f'''
                  A   B   C
                1 {g[0][0]} | {g[0][1]} | {g[0][2]}
                  - + - + -
                2 {g[1][0]} | {g[1][1]} | {g[1][2]}
                  - + - + -
                3 {g[2][0]} | {g[2][1]} | {g[2][2]}
                ''')

        return self

    def start(self):
        input("Pressione enter para iniciar...")

        self._game.start_game()

        while self._game.running:

            self.write_game()

            print(f"{self._game.turn}, é a sua vez!")

            try:
                self._game.play(input("Insira uma letra e um número (ex.: A2): "))
            except IndexError:
                print("Não dá pra jogar aí!")
                continue

        self.write_game()

        if self._game.winner:
            print(f'\n{self._game.winner} venceu em {self._game.round} jogadas!')
        else:
            print(f'\nDeu empate! :(')


if __name__ == '__main__':
    game = GabesT3(TicTacToe()).start()
