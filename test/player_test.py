from app.player import Player
import unittest
from unittest import TestCase


class TestPlayer(unittest.TestCase):
    def test_uid_returns_uid(self):
        player = Player(1, "Luke")
        print(player.uid)
        self.assertEqual(player.uid, 1)

    def test_name_returns_name(self):
        self.assertEqual(Player(1, "Luke").name, "Luke")

    def test_score_returns_score(self):
        player = Player(1, "Luke", 10)
        print(player.score)
        self.assertEqual(player.score, 10)

    # def test_repr(self):
    #     player = Player("1", "Luke", "10")
