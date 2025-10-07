from player import Player
from player_list import PlayerList
from player_node import PlayerNode


class PlayerHashMap:
    def __init__(self,
                 _player_list: PlayerList | None = None,
                 _hashmap: [PlayerList()] = None):
        if _hashmap is None:
            _hashmap = []
            for i in range(10):
                _hashmap.append(PlayerList())

        self.player_list = _player_list
        self.hashmap = _hashmap
        self.size = 0
        print(len(self.hashmap), "!")

    def get_index(self, key: str | Player) -> int:
        if isinstance(key, Player):
            return hash(key) % max(len(self), 1)  # TODO: implement __hash__ in player
        else:
            return Player.hash(key) % max(len(self), 1)  # TODO implement a hash class method in Player

    def __getitem__(self, key: str):
        # get correct player_list
        player_index = self.get_index(key)
        player_list = self.hashmap[player_index]
        # get correct player
        for players in player_list:
            if players.uid == key:
                return players

    def __setitem__(self, key: str, name: str) -> None:
        """ Get the correct player list,
        check if the player is in the list,
        is yes, update the players name,
        if no, create the player and add it to the list"""

        player_index = self.get_index(key)
        print(player_index)

        player_list = self.hashmap[player_index]

        player_present = False
        current_node = player_list.head
        while current_node is not None:
            if current_node.player.uid == key:
                player_present = True
                current_node.player.name = name
                break
            else:
                current_node = current_node.prev_node

        if not player_present:
            player_list.insert_node_at_head(PlayerNode(Player(uid=key, name=name)))
            self.size += 1

    def __len__(self):
        return self.size

    def __delitem__(self, key):
        player_index = self.get_index(key)
        player_list = self.hashmap[player_index]
        player_list.pop_by_key(key)
        self.size -= 1
        pass
