class ListCounter:
    def __init__(self, row_counter, list_counter) -> None:
        self._row_counter = row_counter
        self._list_counter = list_counter

    @property
    def row_counter(self):
        return self._row_counter
    
    @row_counter.setter
    def row_counter(self, value):
        self._row_counter = value

    @property
    def list_counter(self):
        return self._list_counter
    
    @list_counter.setter
    def list_counter(self, value):
        self._list_counter = value