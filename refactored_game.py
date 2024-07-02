import random

OPTIONS = {
  'STONE': 'piedra',
  'PAPER': 'papel',
  'SCISSOR': 'tijera',
}

RESULTS = {
  'TIE': 'empate',
  'USER': 'usuario',
  'MACHINE': 'maquina',
}

MAX_ROUNDS = 3

def verify_winner(user_option, machine_option):
    if user_option == machine_option:
      return RESULTS['TIE']

    if (user_option == OPTIONS['STONE'] and machine_option == OPTIONS['PAPER']) or \
      (user_option == OPTIONS['PAPER'] and machine_option == OPTIONS['SCISSOR']) or \
      (user_option == OPTIONS['SCISSOR'] and machine_option == OPTIONS['STONE']):
      return RESULTS['MACHINE']

    return RESULTS['USER']

def print_results(winner, user_option, computer_option):
    print('----------------')
    if winner == RESULTS['TIE']:
        print('EMPATE!!')
    elif winner == RESULTS['MACHINE']:
        print('Gano la maquina, :(')
    else:
        print('Ganaste papu, :)')
    print('----------------')
    print('User option =>', user_option)
    print('Computer option =>', computer_option)

def main():
  GAME_OPTIONS = list(OPTIONS.values())
  computer_wins = 0
  user_wins = 0
  round_number = 1
    
  while round_number <= MAX_ROUNDS:
    print('\n', '*' * 10, f'ROUND {round_number}', '*' * 10)

    stone, paper, scissor = GAME_OPTIONS
    user_option = input(f'{stone}, {paper} o {scissor} => ').lower()

    if not user_option in GAME_OPTIONS:
      print('esa opcion no es valida')
      continue

    computer_option = random.choice(GAME_OPTIONS)
    winner = verify_winner(user_option, computer_option)

    print_results(winner, user_option, computer_option)

    if winner == RESULTS['MACHINE']:
      computer_wins += 1
    elif winner == RESULTS['USER']:
      user_wins += 1
    
    round_number += 1

  print('\n----------------')
  if user_wins > computer_wins:
    print('GANASTE EL JUEGO owo')
  elif computer_wins > user_wins:
    print('PERDISTE EL JUEGO unu')
  else:
    print('NADIE GANÓ')        

if __name__ == "__main__":
  main()

'''
  - Creamos funciones para separar el condigo
  - Creamos constantes para evitar los magic values
  - Creamos una funcion principal para ejecutar el game
'''
