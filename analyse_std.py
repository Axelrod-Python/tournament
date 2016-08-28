from numpy import median
import axelrod as axl
from run_std import turns, filename
from collections import namedtuple
import csv

def label(prefix, results):
    return "{} - turns: {}, repetitions: {}, strategies: {}. ".format(prefix,
                turns, results.nrepetitions, results.nplayers)

def summary_data(results, filepath=None):
    """
    Obtain summary of performance of each strategy:
    ordered by rank, including median normalised score and cooperation rating.

    Parameters
    ----------

        results : axelrod.results
        filepath : a filepath to which to write the data

    Output
    ------

        A list of the form:

        [[player name, median score, cooperation_rating],...]

        If `filepath` is passed then a summary data file with the following headers will be written:

        "Rank", "Name", "Median-score-per-turn", "Cooperation-rating"
    """

    median_scores = map(median, results.normalised_scores)
    player = namedtuple("Player", ["Rank", "Name", "Median_score", "Cooperation_rating"])

    summary_data = [perf for perf in zip(results.players, median_scores, results.cooperating_rating)]
    summary_data = [player(rank, *summary_data[i]) for rank, i in enumerate(results.ranking)]

    if filepath is not None:
        with open(filepath, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(player._fields)
            for player in summary_data:
                writer.writerow(player)

    return summary_data

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

    summary_data(results, "assets/std_ordinary_ranks.csv")
