class RemovedContent:
    def __init__(self, row_counter=None) -> None:
        self._row_counter = row_counter
        self._removed_row = False
        self._removed_list = []

    @property
    def row_counter(self):
        return self._row_counter
    
    @row_counter.setter
    def row_counter(self, value):
        self._row_counter = value

    @property
    def removed_row(self):
        return self._removed_row
    
    @removed_row.setter
    def removed_row(self, value):
        self._removed_row = value

    @property
    def removed_list(self):
        return self._removed_list
    
    @removed_list.setter
    def removed_list(self, value):
        self._removed_list = value

    def ListAppend(self, value):
        self._removed_list.append(value)

    def Print(self):
        print(f"ROW COUNTER: {self._row_counter}")
        print(f"removed row: {self._removed_row}")
        print(f"removed list: {self.removed_list}")