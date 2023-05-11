class Skill:
    def __init__(self, category, list):
        self._category = category
        self._list = list

    @property
    def category(self) -> str:
        return self._category

    @property
    def list(self) -> list:
        return self._list

    @category.setter
    def category(self, category:str) -> None:
        self._category = category

    @list.setter
    def list(self, list:list) -> None:
        self._list = list