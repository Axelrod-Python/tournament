import axelrod as axl
import random

turns = 200
repetitions = 100
processes = 0
seed = 1
filename = "data/strategies_std_interactions.csv"

if __name__ == "__main__":

    players = [s() for s in axl.ordinary_strategies]
    tournament = axl.Tournament(players, turns=turns, repetitions=repetitions)

    random.seed(seed)  # Setting a seed
    tournament.play(filename=filename, processes=processes)
