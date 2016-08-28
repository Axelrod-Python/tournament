from run_probend import prob_end, filename
from analyse_std import summary_data
import axelrod as axl

def label(prefix, results):
    return "{} - prob_end: {}, repetitions: {}, strategies: {}. ".format(prefix,
                prob_end, results.nrepetitions, results.nplayers)


if __name__ == '__main__':
    results = axl.ResultSetFromFile(filename)

    plot = axl.Plot(results)

    f = plot.boxplot(title=label("Payoff", results))
    f.savefig("assets/ordinary_strategies_prob_end_boxplot.svg")

    f = plot.payoff(title=label("Payoff", results))
    f.savefig("assets/ordinary_strategies_prob_end_payoff.svg")

    f = plot.winplot(title=label("Wins", results))
    f.savefig("assets/ordinary_strategies_prob_end_winplot.svg")

    f = plot.sdvplot(title=label("Payoff differences", results))
    f.savefig("assets/ordinary_strategies_prob_end_sdvplot.svg")

    f = plot.pdplot(title=label("Payoff differences", results))
    f.savefig("assets/ordinary_strategies_prob_end_pdplot.svg")

    eco = axl.Ecosystem(results)
    eco.reproduce(1000)
    f = plot.stackplot(eco, title=label("Eco", results))
    f.savefig("assets/ordinary_strategies_prob_end_reproduce.svg")

    summary_data(results, "assets/prob_end_ordinary_ranks.csv")
