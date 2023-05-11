class Objective:
    def __init__(self, objective) -> None:
        self._objective = objective

    @property
    def objective(self) -> str:
        return self._objective
    
    @objective.setter
    def objective(self, objective:str) -> None:
        self._objective = objective
    