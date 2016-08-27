import axelrod as axl
from analyse_std import write_ranks
from run_noisy import turns, noise, filename

def label(prefix, results):
    return "{} - turns: {}, repetitions: {}, noise: {}, strategies: {}. ".format(prefix,
                turns, results.nrepetitions, noise, results.nplayers)

if __name__ == '__main__':
    results = axl.ResultSetFromFile(filename)

    plot = axl.Plot(results)

    f = plot.boxplot(title=label("Payoff", results))
    f.savefig("assets/ordinary_strategies_boxplot_noise_5.svg")

    f = plot.payoff(title=label("Payoff", results))
    f.savefig("assets/ordinary_strategies_payoff_noise_5.svg")

    f = plot.winplot(title=label("Wins", results))
    f.savefig("assets/ordinary_strategies_winplot_noise_5.svg")

    f = plot.sdvplot(title=label("Payoff differences", results))
    f.savefig("assets/ordinary_strategies_sdvplot_noise_5.svg")

    f = plot.pdplot(title=label("Payoff differences", results))
    f.savefig("assets/ordinary_strategies_pdplot_noise_5.svg")

    eco = axl.Ecosystem(results)
    eco.reproduce(1000)
    f = plot.stackplot(eco, title=label("Eco", results))
    f.savefig("assets/ordinary_strategies_reproduce_noise_5.svg")

    write_ranks(results, "assets/noisy_ordinary_ranks.csv")
