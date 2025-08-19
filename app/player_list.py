from player_node import PlayerNode


class PlayerList:
    def __init__(self, _root: PlayerNode | None = None):
        self.root = None

    def is_empty(self):
        return self.root is None

    def insert_node(self, new_node):
        if self.is_empty():
            # every node has four connections,
            # .next, .prev, .next.prev, .prev.next

            # Connections 1 - new_node.next is None by default
            # Connection 2 - new_node.prev is None by default
            # Connection 3
            self.root = new_node

            # Connection 4
            # self.root_tail = new_node

        else:
            old_head_node = self.root

            # Connection 1 - new_node.next is None by default
            # Connection 3
            old_head_node.next_node = new_node
            # Connection 2
            new_node.prev_node = old_head_node
            # Connection 4
            self.root = new_node

    def pop_from_head(self):
        if self.root is not None:
            pop_name = self.root.name
            # self.root = self.root.next_node
            return pop_name
