# Main program for game of number even.


from brain_games.set_games import brain_game
from brain_games.games.game_even import ask_even_number


def main():
    brain_game(ask_even_number)


if __name__ == '__main__':
    main()
