from app.player_list import PlayerList
import unittest
from unittest import TestCase


class TestPlayerList(unittest.TestCase):
    def test_insert_node_when_empty(self):
        players = PlayerList()
        players.insert_node("")