from player_node import PlayerNode


class PlayerList:
    def __init__(self,
                 _head: PlayerNode | None = None,
                 _tail: PlayerNode | None = None):
        self.head = _head
        self.tail = _tail

    def is_empty(self):
        return self.head is None

    def insert_node_at_head(self, new_node):
        if self.is_empty():
            # every node has four connections,
            # .next, .prev, .next.prev, .prev.next

            # Connections 1 - new_node.next is None by default
            # Connection 2 - new_node.prev is None by default
            # Connection 3 and 4:
            self.head = new_node
            self.tail = new_node

        else:
            # head node moves when inserting from head, tail does not.
            old_head_node = self.head
            # Connection 1 - new_node.next is None by default
            old_head_node.next_node = new_node
            new_node.prev_node = old_head_node
            self.head = new_node

    def insert_node_at_tail(self, new_node):
        if self.is_empty():
            self.head = new_node
            self.tail = new_node

        else:
            # the opposite of insert node at head
            old_tail_node = self.tail
            old_tail_node.prev_node = new_node
            new_node.next_node = old_tail_node
            self.tail = new_node

    def pop_from_head(self):
        if self.head is not None:
            pop_name = self.head.player.name
            self.head = self.head.prev_node
            return pop_name
