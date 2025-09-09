from __future__ import annotations

from player import Player


class PlayerNode:
    def __init__(self,
                 player: Player):
        assert isinstance(player, Player), f"Should pass players not {player} of {type(player)}"
        self._player = player
        self._next_node = None
        self._prev_node = None
        # next node moves towards the head
        # prev node moves towards the tail

    def __str__(self):
        return f"Player: {self.key}, {self.player}"

    @property
    def player(self) -> Player:
        return self._player

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, next_node=None):
        self._next_node = next_node

    @property
    def prev_node(self):
        return self._prev_node

    @prev_node.setter
    def prev_node(self, prev_node=None):
        self._prev_node = prev_node

    @property
    def key(self):
        return self.player.uid


