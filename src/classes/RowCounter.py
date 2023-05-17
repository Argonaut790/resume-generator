from src.classes.ListCounter import ListCounter

class RowCounter:
    def __init__(self, field_type:str, row_counter:int, row_number_view:int): 
        self._field_type = field_type
        self._row_counter = row_counter
        self._row_number_view = row_number_view
        self._description_dict = {0: ListCounter(0, 0)}

    @property
    def field_type(self):
        return self._field_type
    
    @field_type.setter
    def field_type(self, value):
        self._field_type = value
    
    @property
    def row_counter(self):
        return self._row_counter
    
    @row_counter.setter
    def row_counter(self, value):
        self._row_counter = value
    
    @property
    def row_number_view(self):
        return self._row_number_view
    
    @row_number_view.setter
    def row_number_view(self, value):
        self._row_number_view = value

    @property
    def description_dict(self):
        return self._description_dict
    
    @description_dict.setter
    def description_dict(self, value):
        self._description_dict = value

    def DictAppend(self, key, value):
        self._description_dict[key] = value