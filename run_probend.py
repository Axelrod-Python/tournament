import axelrod as axl
import random

prob_end = .1
repetitions = 100
processes = 0
seed = 1
filename = "std_interactions.csv"

players = [s() for s in axl.ordinary_strategies]
tournament = axl.ProbEndTournament(players, prob_end=prob_end, repetitions=repetitions, processes=processes)

random.seed(seed)  # Setting a seed
tournament.play(filename)
