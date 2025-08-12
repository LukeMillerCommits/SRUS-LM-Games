from player import Player


class PlayerNode:
    def __init__(self,
                 player=Player,
                 next_node=None,
                 prev_node=None):
        self._player = player
        self._next_node = next_node
        self._prev_node = prev_node

    def player(self):
        return self._player

    def next_node(self):
        return self._next_node

    def prev_node(self):
        return self._prev_node

    def key(self):
        return self.player().uid

    def __str__(self):
        return str(self)
