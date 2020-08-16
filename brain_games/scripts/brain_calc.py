# Main program for game of calculator.


from brain_games.set_games import brain_game
from brain_games.games.game_calc import generate_calculator


def main():
    brain_game(generate_calculator)


if __name__ == '__main__':
    main()
