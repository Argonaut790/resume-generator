class Component:
    def __init__(self, title:str, start:str, end:str, description:list=None, subTitle:str=None):
        self._title = title
        self._start = start
        self._end = end
        self._subTitle = subTitle
        self._description = description
    
    @property
    def title(self) -> str:
        return self._title
    
    @property
    def start(self) -> str:
        return self._start
    
    @property
    def end(self) -> str:
        return self._end

    @property
    def subTitle(self) -> str:
        return self._subTitle

    @property
    def description(self) -> list:
        return self._description
    
    @title.setter
    def title(self, title:str) -> None:
        self._title = title

    @start.setter
    def start(self, start:str) -> None:
        self._start = start

    @end.setter
    def end(self, end:str) -> None:
        self._end = end

    @subTitle.setter
    def subTitle(self, subTitle:str) -> None:
        self._subTitle = subTitle

    @description.setter
    def description(self, description:list) -> None:
        self._description = description