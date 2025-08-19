class Player:
    def __init__(self, uid, name):
        self._uid = uid
        self._name = name

    @property
    def uid(self) -> str:
        return self._uid

    @property
    def name(self) -> str:
        return self._name

    def __str__(self) -> str:
        return str(self.name)
