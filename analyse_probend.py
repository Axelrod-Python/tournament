import axelrod as axl
from run_probend import prob_end, filename

def label(prefix, results):
    return "{} - prob_end: {}, repetitions: {}, strategies: {}. ".format(prefix,
                prob_end, results.nrepetitions, results.nplayers)

if __name__ == '__main__':
    results = axl.ResultSetFromFile(filename)

    plot = axl.Plot(results)

    f = plot.boxplot(title=label("Payoff", results))
    f.savefig("assets/strategies_prob_end_boxplot.svg")
