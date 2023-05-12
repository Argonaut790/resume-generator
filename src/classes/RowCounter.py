class RowCounter:
    def __init__(self, education_row_counter, education_row_number_view, sideproject_row_counter, sideproject_row_number_view, experience_row_counter, experience_row_number_view, skills_row_counter, skills_row_number_view):
        self._education_row_counter = education_row_counter
        self._education_row_number_view = education_row_number_view
        self._sideproject_row_counter = sideproject_row_counter
        self._sideproject_row_number_view = sideproject_row_number_view
        self._experience_row_counter = experience_row_counter
        self._experience_row_number_view = experience_row_number_view
        self._skills_row_counter = skills_row_counter
        self._skills_row_number_view = skills_row_number_view

    @property
    def education_row_counter(self):
        return self._education_row_counter
    
    @education_row_counter.setter
    def education_row_counter(self, value):
        self._education_row_counter = value

    @property
    def education_row_number_view(self):
        return self._education_row_number_view
    
    @education_row_number_view.setter
    def education_row_number_view(self, value):
        self._education_row_number_view = value

    @property
    def sideproject_row_counter(self):
        return self._sideproject_row_counter
    
    @sideproject_row_counter.setter
    def sideproject_row_counter(self, value):
        self._sideproject_row_counter = value

    @property
    def sideproject_row_number_view(self):
        return self._sideproject_row_number_view
    
    @sideproject_row_number_view.setter
    def sideproject_row_number_view(self, value):
        self._sideproject_row_number_view = value

    @property
    def experience_row_counter(self):
        return self._experience_row_counter
    
    @experience_row_counter.setter
    def experience_row_counter(self, value):
        self._experience_row_counter = value

    @property
    def experience_row_number_view(self):
        return self._experience_row_number_view
    
    @experience_row_number_view.setter
    def experience_row_number_view(self, value):    
        self._experience_row_number_view = value

    @property
    def skills_row_counter(self):
        return self._skills_row_counter
    
    @skills_row_counter.setter
    def skills_row_counter(self, value):
        self._skills_row_counter = value

    @property
    def skills_row_number_view(self):
        return self._skills_row_number_view
    
    @skills_row_number_view.setter
    def skills_row_number_view(self, value):
        self._skills_row_number_view = value
