import axelrod as axl
import random
import os

prob_end = .1
repetitions = 100
processes = 0
seed = 1
filename = "data/strategies_probend_interactions.csv"

if __name__ == "__main__":
    # Deleting the file if it exists
    try:
        os.remove(filename)
    except OSError:
        pass

    random.seed(seed)  # Setting a seed

    players = [s() for s in axl.ordinary_strategies]
    tournament = axl.ProbEndTournament(players, prob_end=prob_end, repetitions=repetitions)

    tournament.play(filename=filename, processes=processes)
