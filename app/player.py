class Player:
    def __init__(self, uid, name):
        self._uid = uid
        self._name = name

    def uid(self):
        return self._uid

    def name(self):
        return self._name

    def __str__(self):
        return str(self)
