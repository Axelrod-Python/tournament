import axelrod as axl
from run_std import turns, filename

def label(prefix, results):
    return "{} - turns: {}, repetitions: {}, strategies: {}. ".format(prefix,
                turns, results.nrepetitions, results.nplayers)

if __name__ == '__main__':
    results = axl.ResultSetFromFile(filename)

    plot = axl.Plot(results)

    f = plot.boxplot(title=label("Payoff", results))
    f.savefig("assets/ordinary_strategies_boxplot.svg")

    f = plot.payoff(title=label("Payoff", results))
    f.savefig("assets/ordinary_strategies_payoff.svg")

    f = plot.winplot(title=label("Wins", results))
    f.savefig("assets/ordinary_strategies_winplot.svg")

    f = plot.sdvplot(title=label("Payoff differences", results))
    f.savefig("assets/ordinary_strategies_sdvplot.svg")

    f = plot.pdplot(title=label("Payoff differences", results))
    f.savefig("assets/ordinary_strategies_pdplot.svg")

    eco = axl.Ecosystem(results)
    eco.reproduce(1000)
    f = plot.stackplot(eco, title=label("Eco", results))
    f.savefig("assets/ordinary_strategies_reproduce.svg")
