from app.player_list import PlayerList
from player_node import PlayerNode
from player import Player

import unittest
from unittest import TestCase


class TestPlayerList(unittest.TestCase):
    def setUp(self):
        players = PlayerList()
        players.insert_node_at_head(PlayerNode(Player("1", "Luke")))

    def test_empty_list_is_empty(self):
        empty_list = PlayerList()
        self.assertIs(empty_list.is_empty(), True)

    def test_full_list_is_not_empty(self):
        players = PlayerList()
        players.insert_node_at_head(PlayerNode(Player("1", "Luke")))
        self.assertIs(players.is_empty(), False)

    def test_insert_node_at_head_into_empty_list(self):
        players = PlayerList()
        players.insert_node_at_head(PlayerNode(Player("1", "Luke")))
        self.assertEqual(players.pop_from_head(), "Luke")

    def test_insert_node_at_head_into_full_list(self):
        players = PlayerList()
        players.insert_node_at_head(PlayerNode(Player("1", "Luke")))
        players.insert_node_at_head(PlayerNode(Player("2", "Jake")))
        self.assertEqual(players.pop_from_head(), "Jake")

    def test_pop_from_head(self):
        players = PlayerList()
        players.insert_node_at_head(PlayerNode(Player("1", "Luke")))
        players.insert_node_at_head(PlayerNode(Player("2", "Jake")))
        players.pop_from_head()
        self.assertEqual(players.pop_from_head(), "Luke")

    def test_insert_node_at_tail(self):
        players = PlayerList()
        players.insert_node_at_tail(PlayerNode(Player("1", "Luke")))
        players.insert_node_at_tail(PlayerNode(Player("2", "Jake")))
        self.assertEqual(players.pop_from_head(), "Luke")
        players.insert_node_at_head(PlayerNode(Player("1", "Luke")))
        self.assertEqual(players.pop_from_tail(), "Jake")
