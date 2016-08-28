"""
A script with utility functions to get the tournament results
"""
from numpy import median
import axelrod as axl
from run_std import turns, filename
from collections import namedtuple
import csv
import tqdm

def label(prefix, results):
    """
    A label used for the various plots
    """
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
    player = namedtuple("Player", ["Rank", "Name",
                                   "Median_score", "Cooperation_rating"])

    summary_data = [perf for perf in zip(results.players,
                                         median_scores,
                                         results.cooperating_rating)]
    summary_data = [player(rank, *summary_data[i]) for
                    rank, i in enumerate(results.ranking)]

    if filepath is not None:
        with open(filepath, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(player._fields)
            for player in tqdm.tqdm(summary_data, desc="Writing summary data"):
                writer.writerow(player)

    return summary_data

def obtain_assets(results, strategies_name, tournament_type,
                  assets_dir="./assets/", lengthplot=False):
    """
    From the results of a tournament: obtain the various plots and the summary
    data set

    Parameters
    ----------

        results: axelrod.resultset instance
        strategies_name: string, eg: "ordinary_strategies"
        tournament_type: string, eg: "std"

        assets_dir: string [default: "./assets/"]
        lengthplot: boolean [default: False], whether or not to plot the length
        of the matches (only needed for the probabilistic ending matches)
    """

    total = 6 + int(lengthplot)

    pbar = tqdm.tqdm(total=total, desc="Obtaining plots")

    file_path_root = "{}/{}_{}".format(assets_dir, strategies_name,
                                       tournament_type)
    plot = axl.Plot(results)

    f = plot.boxplot(title=label("Payoff", results))
    f.savefig("{}_boxplot.svg".format(file_path_root))
    pbar.update()

    f = plot.payoff(title=label("Payoff", results))
    f.savefig("{}_payoff.svg".format(file_path_root))
    pbar.update()

    f = plot.winplot(title=label("Wins", results))
    f.savefig("{}_winplot.svg".format(file_path_root))
    pbar.update()

    f = plot.sdvplot(title=label("Payoff differences", results))
    f.savefig("{}_sdvplot.svg".format(file_path_root))
    pbar.update()

    f = plot.pdplot(title=label("Payoff differences", results))
    f.savefig("{}_pdplot.svg".format(file_path_root))
    pbar.update()

    eco = axl.Ecosystem(results)
    eco.reproduce(1000)
    f = plot.stackplot(eco, title=label("Eco", results))
    f.savefig("{}_reproduce.svg".format(file_path_root))
    pbar.update()

    if lengthplot is True:
        f = plot.lengthplot(title=label("Length of matches", results))
        f.savefig("{}_lengthplot.svg".format(file_path_root))
        pbar.update()

    summary_data(results, "{}_ranks.csv".format(file_path_root))
