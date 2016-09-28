"""
Tests for the utils.py file
"""
import axelrod as axl
import unittest
import utils
import tempfile
import csv

class TestUtils(unittest.TestCase):
    """
    Simple tests for the utils
    """

    axl.seed(0)
    players = [s() for s in axl.demo_strategies]
    tournament = axl.Tournament(players)
    results = tournament.play()

    def test_label(self):
        label = utils.label("Test", self.results)
        expected_label = "{} - turns: {}, repetitions: {}, strategies: {}.  ".format("Test",
                    self.tournament.turns, self.tournament.repetitions,
                    len(self.tournament.players))

    def test_obtain_assets(self):
        """Just test that this runs without crashing"""
        self.assertEqual(utils.obtain_assets(self.results, assets_dir="/tmp"), None)
