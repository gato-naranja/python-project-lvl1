import prompt


NUMBER_OF_ROUNDS = 3


def execute_game(game):
    # The body of all brain games
    print('Welcome to the Brain Games!')
    attempts_user_counter = NUMBER_OF_ROUNDS
    print()
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print()
    print(game.GAME_RULE)
    while attempts_user_counter:
        essence_question, right_answer = game.generate_question_and_answer()
        print(f'Question: {essence_question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == right_answer:
            print('Correct!')
            attempts_user_counter -= 1
        else:
            print(
                f'\'{user_answer}\' is wrong answer ;(.'
                f' Correct answer was \'{right_answer}\''
            )
            print(f'Let\'s try again, {user_name}!')
            break
    else:
        print(f'Congratulations, {user_name}!')
