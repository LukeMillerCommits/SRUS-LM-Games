class Player:
    def __init__(self, uid, name):
        self._uid = uid
        self._name = name

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

    def __str__(self) -> str:
        return str(self.name)

    def __hash__(self):
        return self.hash
