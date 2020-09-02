import prompt


def brain_game(game):
    # The body of all brain games
    print('Welcome to the Brain Games!')
    attempts_user_counter = 3
    print()
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user_name))
    print()
    print(game.GAME_RULE)
    while attempts_user_counter:
        essence_question, right_answer = game.generate_question_and_answer()
        print('Question: {0}'.format(essence_question))
        user_answer = prompt.string('Your answer: ')
        if user_answer == right_answer:
            print('Correct!')
            attempts_user_counter -= 1
        else:
            print(
                '\'{0}\' is wrong answer ;(. Correct answer was \'{1}\''
                .format(user_answer, right_answer)
            )
            print('Let\'s try again, {0}!'.format(user_name))
            break
    else:
        print('Congratulations, {0}!'.format(user_name))
