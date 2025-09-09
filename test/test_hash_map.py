from player_hash_map import PlayerHashMap
from player_list import PlayerList

import unittest
from unittest import TestCase


class TestPlayerHashMap(unittest.TestCase):
    def setUp(self):
        ...

    def test_set_item(self):
        test_hash_map = PlayerHashMap()
        test_hash_map.__setitem__("1", "Luke")
        test_hash_map.__setitem__("2", "Bob")
        test_hash_map.__setitem__("3", "Carly")
        test_hash_map.__setitem__("4", "Denny")
        test_hash_map.__setitem__("5", "Emily")
        test_hash_map.__setitem__("6", "Fred")
        test_hash_map.__setitem__("7", "Gus")
        test_hash_map.__setitem__("8", "Helga")
        test_hash_map.__setitem__("9", "Ingrid")
        test_hash_map.__setitem__("10", "Josh")
        print(test_hash_map)
