"""Strategies to be included in the tournament"""
import axelrod as axl

# Include a list of parametrized strategies
parameterized_players = [
	axl.Random(0.1),
        axl.Random(0.3),
        axl.Random(0.7),
        axl.Random(0.9),
        axl.GTFT(0.1),
        axl.GTFT(0.3),
        axl.GTFT(0.7),
        axl.GTFT(0.9),
        axl.MetaWinner(team=[
        axl.EvolvedHMM5, axl.EvolvedLookerUp2_2_2, axl.EvolvedFSM16,
        axl.EvolvedANN5, axl.PSOGambler2_2_2, axl.FoolMeOnce,
        axl.DoubleCrosser, axl.Gradual
    ]),
]

players = [s() for s in axl.strategies] + parameterized_players
players.sort(key=lambda p:p.__repr__())
