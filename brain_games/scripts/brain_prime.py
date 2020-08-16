# Main program for game of prime number.


from brain_games.set_games import brain_game
from brain_games.games.game_prime import is_number_prime


def main():
    brain_game(is_number_prime)


if __name__ == '__main__':
    main()
