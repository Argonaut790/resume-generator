class Component:
    def __init__(self, title:str, duration:list, description:list=None, subTitle:str=None):
        self._title = title
        self._duration = duration
        self._subTitle = subTitle
        self._description = description
    
    @property
    def title(self) -> str:
        return self._title
    
    @property
    def duration(self) -> str:
        return self._duration
    
    @property
    def subTitle(self) -> str:
        return self._subTitle

    @property
    def description(self) -> list:
        return self._description
    
    @title.setter
    def title(self, title:str) -> None:
        self._title = title

    @duration.setter
    def duration(self, duration:str) -> None:
        self._duration = duration

    @subTitle.setter
    def subTitle(self, subTitle:str) -> None:
        self._subTitle = subTitle

    @description.setter
    def description(self, description:list) -> None:
        self._description = description