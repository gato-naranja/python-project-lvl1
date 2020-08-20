import prompt


def welcome_user():
    # Get an user name and promt user.:
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def show_mess_when_incorrect_answer(user, answer, result):
    # Output message when answer is incorrect
    print(
            '\'{0}\' is wrong answer ;(. Correct answer was \'{1}\''
            .format(answer, result)
            )
    print('Let\'s try again, {0}!'.format(user))


def brain_game(game):
    # The body of all brain games
    print('Welcome to the Brain Games!')
    attempts_user = 3
    print()
    user_name = welcome_user()
    print()
    print(game.GAME_RULE)
    while attempts_user:
        essence_question, right_answer = game.calculation_values_game()
        print('Question: {0}'.format(essence_question))
        user_answer = prompt.string('Your answer: ')
        if user_answer == right_answer:
            print('Correct!')
            attempts_user -= 1
        else:
            show_mess_when_incorrect_answer(
                    user_name,
                    user_answer,
                    right_answer
                    )
            break
    if not attempts_user:
        print('Congratulations, {0}!'.format(user_name))
