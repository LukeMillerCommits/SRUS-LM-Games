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
        pivot = player_list[0]
        left = []
        right = []
        for player in player_list[1:]:
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

    def __repr__(self):
        return ("Player(name='" + self.name +
                "', uid='" + self.uid +
                "', score= '" + str(self.score) + "')")
