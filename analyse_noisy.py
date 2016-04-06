import axelrod as axl
from run_noisy import turns, noise, filename

def label(prefix, results):
    return "{} - turns: {}, repetitions: {}, noise: {}, strategies: {}. ".format(prefix,
                turns, results.nrepetitions, noise, results.nplayers)

if __name__ == '__main__':
    results = axl.ResultSetFromFile(filename)

    plot = axl.Plot(results)

    f = plot.boxplot(title=label("Payoff", results))
    f.savefig("assets/strategies_boxplot_noise_5.svg")
