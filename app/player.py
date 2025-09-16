class Player:
    def __init__(self, uid, name, score=0):
        self._uid = uid
        self._name = name
        self._score = score
        if score < 0:
            raise ValueError("Score cannot be negative")

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

    # def __repr__(self):
    #     return ("Player(name='" + self.name +
    #             "', uid='" + self.uid +
    #             "', score= '" + str(self.score) + "')")
