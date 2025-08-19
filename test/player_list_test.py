from app.player_list import PlayerList
from player import Player
import unittest
from unittest import TestCase


class TestPlayerList(unittest.TestCase):
    def setUp(self):
        players = PlayerList()
        players.insert_node(Player("1", "Luke"))

    def test_empty_list_is_empty(self):
        empty_list = PlayerList()
        self.assertIs(empty_list.is_empty(), True)

    def test_full_list_is_not_empty(self):
        players = PlayerList()
        players.insert_node(Player("1", "Luke"))
        self.assertIs(players.is_empty(), False)

    def test_insert_node_into_empty_list(self):
        players = PlayerList()
        players.insert_node(Player("1", "Luke"))
        self.assertEqual(players.pop_from_head(), "Luke")