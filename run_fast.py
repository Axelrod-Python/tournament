#!/usr/bin/env python
import axelrod as axl
from pathlib import Path

def fast_tournament(turns=200, repetitions=40, processes=0):
    # Choose the fast standard strategies
    players = [s() for s in axl.all_strategies if
               axl.obey_axelrod(s())
               and not s().classifier['long_run_time']]

    # Play the tournament
    tournament = axl.Tournament(
        players=players,
        turns=turns,
        repetitions=repetitions
    )
    results = tournament.play(processes=processes)

    # Make sure the output directory exists
    path = Path("fast")
    path.mkdir(exist_ok=True)

    # Create and save the standard plot set
    plot = axl.Plot(results)
    plot.save_all_plots(prefix=str(path)+'/')

if __name__ == "__main__":
    fast_tournament(processes=4)