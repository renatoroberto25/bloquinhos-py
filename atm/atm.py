'''Script simples simulando funcionalidade de caixa eletrônico'''
from math import floor


def count_money(amt, banknotes):
  '''
  Função que conta as notas.
  Essa função não deve manusear exceções nem cuidar de
  entrada/saída. Para isso, usaremos outra função.
  '''
  remaining_amt = amt
  count = {}
  
  for note in sorted(banknotes, reverse=True):
    note_amt = floor(remaining_amt / note)
    count[note] = note_amt
    remaining_amt -= note * note_amt
  
  if remaining_amt:
    count['remainder'] = remaining_amt
  
  return count
  

def ask(banknotes):
  '''
  Função que faz a pergunta por linha de comando.
  Já que é essa função que cuida de entrada/saída, é ela que
  deve ser responsável pelo manuseio de exceções.
  '''
  notes_str = ', '.join(map(lambda i: 'R$ ' + str(i),
                            sorted(banknotes, reverse=True))
                            )
  
  print('Notas disponíveis:', notes_str)
  while True:
    try:
      amt = int(input('Qual valor você deseja retirar?'))
      money = count_money(amt, banknotes)
    except ValueError:
      print('Insira apenas números!')
    
    print('Retirando R$ ' + str(amt))
    break
  
  return money


def normalize_strlen(string, length):
  '''
  Helper que adiciona enchimento a strings mais curtas
  feita para tabular as linhas da saída
  '''
  
  if len(string) < length:
    return (' ' * (length - len(string))) + string
  
  return string
  

def main():
  retrieval = ask([100, 50, 20, 10, 5, 2])
  template = 'R$ {0}: {1} nota{2}'
  print('\n'.join([template.format(normalize_strlen(str(i), 3),
                                   str(retrieval[i]),
                                   's' if retrieval[i] > 1 else '')
                   for i in retrieval if retrieval[i] > 0]))


main()
