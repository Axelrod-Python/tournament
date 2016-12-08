import axelrod as axl
import os
import utils

from players import players

turns = 200
repetitions = 100
noise = 0.05
processes = 0
seed = 1
filename = "data/strategies_noisy_interactions.csv"

def main(players=players):
    # Deleting the file if it exists
    try:
        os.remove(filename)
    except OSError:
        pass

    axl.seed(seed)  # Setting a seed

    tournament = axl.Tournament(players, turns=turns, repetitions=repetitions,
                                noise=noise)

    results = tournament.play(filename=filename, processes=processes)
    utils.obtain_assets(results, "strategies", "noisy")
    results.write_summary('assets/noisy_summary.csv')

if __name__ == '__main__':
    main()
