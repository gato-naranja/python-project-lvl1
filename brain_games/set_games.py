import prompt
from brain_games.cli import welcome_user
from brain_games.cli import show_mess_when_incorrect_answer


def brain_game(game):
    # The body of all brain games
    print('Welcome to the Brain Games!')
    attempts_user = 3
    print()
    user_name = welcome_user()
    print()
    calculation_result = game(attempts_user)
    print(calculation_result[0])
    while attempts_user:
        print('Question: {0}'.format(calculation_result[attempts_user][0]))
        user_answer = prompt.string('Your answer: ')
        if user_answer == calculation_result[attempts_user][1]:
            print('Correct!')
            attempts_user -= 1
        else:
            show_mess_when_incorrect_answer(
                    user_name,
                    user_answer,
                    calculation_result[attempts_user][1]
                    )
            break
    if not attempts_user:
        print('Congratulations, {0}!'.format(user_name))
