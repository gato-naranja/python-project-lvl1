# Main program for game of number even.


from brain_games.cli import welcome_user
from brain_games.number_even import game_even


def main():
    # Make a user intreface.
    print('Welcome to the Brain Games!')
    name = welcome_user()
    game_even(name)


if __name__ == '__main__':
    main()
