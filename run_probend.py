import axelrod as axl

prob_end = .1
repetitions = 100
processes = 0
filename = "std_interactions.csv"

players = [s() for s in axl.ordinary_strategies]
tournament = axl.ProbEndTournament(players, prob_end=prob_end, repetitions=repetitions, processes=processes)
tournament.play(filename)
