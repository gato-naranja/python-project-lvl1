# Main program for game of progression.


from brain_games.set_games import brain_game
from brain_games.games.game_progression import ask_progression_task


def main():
    brain_game(ask_progression_task)


if __name__ == '__main__':
    main()
