# Main program for game of greatest common divisor.


from brain_games.set_games import brain_game
from brain_games.games.game_gcd import calculate_gcd


def main():
    brain_game(calculate_gcd)


if __name__ == '__main__':
    main()
