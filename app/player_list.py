from player_node import PlayerNode


class PlayerList:
    def __init__(self, _root: PlayerNode | None = None):
        self.root = None

    def is_empty(self):
        if self.root is None:
            return True
        else: return False

    def insert_node(self, player_node):
        if self.is_empty():
            self.root = player_node
            self.root.next_node = self.root
        else:
            self.root.next_node = player_node
            player_node.prev_node = self.root
            self.root = player_node
            self.root.next_node = self.root
