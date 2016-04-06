import axelrod as axl
import random


turns = 200
repetitions = 100
noise = 0.05
processes = 0
seed = 1
filename = "data/strategies_noisy_interactions.csv"

if __name__ == '__main__':
    players = [s() for s in axl.ordinary_strategies]
    tournament = axl.Tournament(players, turns=turns, repetitions=repetitions, noise=noise, processes=processes)

    random.seed(seed)  # Setting a seed
    tournament.play(filename)
