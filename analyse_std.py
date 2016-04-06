import axelrod as axl
from run_std import turns  # Grab the turns and noise used to create data

def label(prefix, results):
    return "{} - turns: {}, repetitions: {}, strategies: {}. ".format(prefix,
                turns, results.nrepetitions, results.nplayers)

filename = "data/std_interactions.csv"

if __name__ == '__main__':
    results = axl.ResultSetFromFile(filename)

    plot = axl.Plot(results)

    f = plot.boxplot(title=label("Payoff", results))
    f.savefig("assets/strategies_boxplot.svg")
