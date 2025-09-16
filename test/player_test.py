from app.player import Player
import random
import unittest
from unittest import TestCase


class TestPlayer(unittest.TestCase):
    def test_uid_returns_uid(self):
        player = Player("1", "Luke")
        # print(player.uid)
        self.assertEqual(player.uid, "1")

    def test_name_returns_name(self):
        self.assertEqual(Player("1", "Luke").name, "Luke")

    def test_score_returns_score(self):
        player = Player("1", "Luke", 10)
        # print(player.score)
        self.assertEqual(player.score, 10)

    def test_sort_players(self):
        players = [Player('1', "Alice", score=10),
                   Player('2', "Bob", score=5),
                   Player('3', "Charlie", score=15)]
        # note: ensure initialization code is valid for **your** implementation.
        # For example, is your parameter called uid? is the first parameter name?

        # do **not** change the following code:
        sorted_players = sorted(players)

        # players must be sorted by score as shown here:
        manually_sorted_players = [Player('2', "Bob", score=5),
                                   Player('1', "Alice", score=10),
                                   Player('3', "Charlie", score=15)]

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_players_can_be_compared_by_score(self):
        alice = Player("1", "Alice", 10)
        bob = Player("2", "Bob", 5)

        self.assertGreater(alice, bob)

    def test_quick_sort_by_score(self):
        players = [Player('1', "Alice", score=10),
                   Player('2', "Bob", score=5),
                   Player('3', "Charlie", score=15)]

        sorted_players = Player.quick_sort_by_score(players)

        manually_sorted_players = [Player('3', "Charlie", score=15),
                                   Player('1', "Alice", score=10),
                                   Player('2', "Bob", score=5)]

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_quick_sort_at_scale(self):
        players = [Player(f"{i:03}", f"{i}", score=random.randint(0, 1000))
                   for i in range(1000)]

        sorted_players = Player.quick_sort_by_score(players)

        self.assertListEqual(sorted_players, sorted(players, reverse=True))

    def test_quick_sort_already_sorted(self):
        players = [Player(f"{i:03}", f"{i}", score=random.randint(0, 1000))
                   for i in range(1000)]

        pre_sorted_players = sorted(players, reverse=True)

        # pre_sorted_players[0], pre_sorted_players[1] = pre_sorted_players[1], pre_sorted_players[0]

        print(pre_sorted_players[0].score, pre_sorted_players[1].score)
        sorted_players = Player.quick_sort_by_score(pre_sorted_players)

        self.assertListEqual(sorted_players, pre_sorted_players)
