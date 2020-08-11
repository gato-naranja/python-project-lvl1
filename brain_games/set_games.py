import prompt
from brain_games.cli import welcome_user
from brain_games.cli import print_rules
from brain_games.cli import show_mess_when_incorrect_answer
from brain_games.games.game_even import ask_even_number
from brain_games.games.game_gcd import calculate_gcd
from brain_games.games.game_calc import generate_calculator
from brain_games.games.game_progression import ask_progression_task
from brain_games.games.game_prime import is_number_prime


def brain_game(game):
    # In the argument 'game' should be one of following values:
    #   even - for game of number even;
    #   gcd - for game of greatest common divisor;
    #   calc - for game of calculator;
    #   progression - for game of progression;
    #   prime for game of prime number.
    print_rules(game)
    print()
    user_name = welcome_user()
    print()
    attempts_user = 3
    while attempts_user:
        if game == 'even':
            calculation_result = ask_even_number()
            user_answer = prompt.string('Your answer: ')
        elif game == 'gcd':
            calculation_result = calculate_gcd()
            user_answer = prompt.integer('Your answer: ')
        elif game == 'calc':
            calculation_result = generate_calculator()
            user_answer = prompt.integer('Your answer: ')
        elif game == 'progression':
            calculation_result = ask_progression_task()
            user_answer = prompt.integer('Your answer: ')
        elif game == 'prime':
            calculation_result = is_number_prime()
            user_answer = prompt.string('Your answer: ')
        else:
            return print('Sorry, {0}!'.format(user_name))
        if user_answer == calculation_result:
            print('Correct!')
            attempts_user -= 1
        else:
            show_mess_when_incorrect_answer(
                    user_name, user_answer, calculation_result
                    )
            break
    if not attempts_user:
        print('Congratulations, {0}!'.format(user_name))
