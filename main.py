class Note:
    __id = []

    def __new__(cls):
        cls.__id.append(get_new_id())
        if len(cls.__id) >= 2 and cls.__id[-2] >= cls.__id[-1]:
            cls.__id[-1] = cls.__id[-2] + 1
        return super().__new__(cls)

    def __init__(self):
        self.id = self.get_id()
        self.date = None

    @classmethod
    def get_id(cls):
        return cls.__id[-1]

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, d):
        self._data = d

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, t):
        self._title = t

