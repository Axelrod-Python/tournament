import axelrod as axl
import os
import utils

turns = 20
repetitions = 10

processes = 0
seed = 1
filename = "data/strategies_std_interactions.csv"

def main():
    # Deleting the file if it exists
    try:
        os.remove(filename)
    except OSError:
        pass

    axl.seed(seed)  # Setting a seed

    players = [s() for s in axl.ordinary_strategies]
    tournament = axl.Tournament(players, turns=turns, repetitions=repetitions)

    results = tournament.play(filename=filename, processes=processes)
    utils.obtain_assets(results, "strategies", "std")
    results.write_summary('assets/std_summary.csv')

if __name__ == "__main__":
    main()
