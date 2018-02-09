"""
A script with utility functions to get the tournament results
"""
from collections import namedtuple
from numpy import median
from run_std import turns, filename
import axelrod as axl
import csv
import tqdm

def label(prefix, results):
    """
    A label used for the various plots
    """
    return "{} - turns: {}, repetitions: {}, strategies: {}. ".format(prefix,
                turns, results.repetitions, results.num_players)

def obtain_assets(results, strategies_name="strategies",
                  tournament_type="std",
                  assets_dir="./assets", lengthplot=False):
    """
    From the results of a tournament: obtain the various plots and the summary
    data set

    Parameters
    ----------

        results: axelrod.resultset instance
        strategies_name: string, eg: "ordinary_strategies"
        tournament_type: string, eg: "std"

        assets_dir: string [default: "./assets"]
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
