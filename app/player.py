import random


class Player:
    def __init__(self, uid, name, score=0):
        self._uid = uid
        self._name = name
        self._score = score
        if score < 0:
            raise ValueError("Score cannot be negative")

    @classmethod
    def quick_sort_by_score(cls, player_list):
        if len(player_list) <= 1:
            return player_list

        # Complexity-inefficient solution

        # list_sorted = True
        # for i in range(len(player_list)-1):
        #     if player_list[i] < player_list[i+1]:
        #         list_sorted = False
        #         break
        # if list_sorted:
        #     print("already sorted")
        #     return player_list
        # returns list or list fragment if already sorted.

        # much more efficient, pivot could be set to player_list[random_index]
        random_index = random.randint(0, len(player_list)-1)

        pivot = player_list[random_index]
        left = []
        right = []

        for player in player_list[:random_index]:
            if player > pivot:
                left.append(player)
            else:
                right.append(player)

        for player in player_list[random_index+1:]:
            if player > pivot:
                left.append(player)
            else:
                right.append(player)

        return (cls.quick_sort_by_score(left)
                + [pivot]
                + cls.quick_sort_by_score(right))

    @classmethod
    def hash(cls, key):
        hash_value = hash(key)
        return hash_value

    @property
    def uid(self) -> str:
        return self._uid

    @uid.setter
    def uid(self, uid):
        _uid = uid

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name):
        _name = name

    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, score):
        _score = score

    def __str__(self) -> str:
        return str(self.name)

    def __hash__(self):
        return self.hash

    def __gt__(self, other):
        return self.score > other.score

    def __eq__(self, other):
        return self.score == other.score
