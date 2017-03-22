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
        EvolvedHMM5, EvolvedLookerUp2_2_2, EvolvedFSM16, EvolvedANN5,
        PSOGambler2_2_2, FoolMeOnce, DoubleCrosser, Gradual
    ]),
]

players = [s() for s in axl.strategies] + parameterized_players
players.sort(key=lambda p:p.__repr__())
