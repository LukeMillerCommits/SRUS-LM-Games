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
        print(len(self.hashmap), "!")

    def get_index(self, key: str | Player) -> int:
        if isinstance(key, Player):
            return hash(key) % len(self)  # TODO: implement __hash__ in player
        else:
            return Player.hash(key) % len(self)  # TODO implement a hash class method in Player

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
            else:
                current_node = current_node.prev_node

        # if player_list.head is not None:
        #     for players in player_list:
        #         if players.uid == key:
        #             player_present = True

        if player_present:
            current_node.player.name = name
        else:
            player_list.insert_node_at_head(PlayerNode(Player(uid=key, name=name)))

    def __len__(self):
        return 10       # FIX!!!

    def __delitem__(self, key):
        # self.SIZE -= 1
        pass
