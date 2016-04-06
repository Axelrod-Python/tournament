import axelrod as axl

turns = 200
repetitions = 100
processes = 0
filename = "std_interactions.csv"

players = [s() for s in axl.ordinary_strategies]
tournament = axl.Tournament(players, turns=turns, repetitions=repetitions, processes=processes)
tournament.play(filename)
