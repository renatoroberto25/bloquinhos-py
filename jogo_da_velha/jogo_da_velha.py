e = lambda s: s == ' '

write_game = lambda g: f'''
  A   B   C
1 {g[0][0]} | {g[0][1]} | {g[0][2]}
  - + - + -
2 {g[1][0]} | {g[1][1]} | {g[1][2]}
  - + - + -
3 {g[2][0]} | {g[2][1]} | {g[2][2]}
'''

def play(letter, row, col, game):
  game2 = list(game)
  if not e(game2[row][col]):
    return False

  game2[row][col] = letter
  return game2

def check_gameover(game):
  d1win = not e(game[0][0]) and game[0][0] == game[1][1] == game[2][2] and game[0][0] or False
  d2win = not e(game[0][2]) and game[0][2] == game[1][1] == game[2][0] and game[0][2] or False
  dwin = d1win or d2win
  
  fh = lambda r: not e(game[r][0]) and game[r][0] == game[r][1] == game[r][2] and game[r][0] or False
  hwin = fh(0) or fh(1) or fh(2)
  
  fv = lambda c: not e(game[0][c]) and game[0][c] == game[1][c] == game[2][c] and game[0][c] or False
  vwin = fv(0) or fv(1) or fv(2)
  
  return dwin or hwin or vwin

letter_to_number = lambda l: 0 if l.upper() == "A" else l.upper() == "B" and 1 or l.upper() == "C" and 2 or 4

def main():
  input("Pressione enter para começar...")
  g = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
  turn = 'X'
  gameover = False
  
  while not gameover:
    print(write_game(g))
    print(f'{turn}, é sua vez!')
    cell = input("Insira uma letra e um número (ex. A2) ")
    try:
      g2 = play(turn, int(cell[1]) - 1, letter_to_number(cell[0]), g)
      if not g2:
        print("Essa casa já foi preenchida!")
        continue
      g = g2
    except IndexError:
      print("Insira uma letra de A a C e um número de 1 a 3!")
      continue
    gameover = check_gameover(g)
    turn = 'O' if turn == 'X' else 'X'
  
  print(write_game(g))
  print(f'{gameover} venceu!')
  
if __name__ == "__main__":
  main()
