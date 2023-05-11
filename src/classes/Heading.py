class Heading:
    def __init__(self, name:str, nickname:str, email:str, phone:str, github:str, website:str):
        self._name = name
        self._nickname = nickname
        self._email = email
        self._phone = phone
        self._github = github
        self._website = website

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def nickname(self) -> str:
        return self._nickname

    @property
    def email(self) -> str:
        return self._email

    @property
    def phone(self) -> str:
        return self._phone
    
    @property
    def github(self) -> str:
        return self._github
    
    @property
    def website(self) -> str:
        return self._website
    
    @name.setter
    def name(self, name:str) -> None:
        self._name = name

    @nickname.setter
    def nickname(self, nickname:str) -> None:
        self._nickname = nickname
    
    @email.setter
    def email(self, email:str) -> None:
        self._email = email
    
    @phone.setter
    def phone(self, phone:str) -> None:
        self._phone = phone

    @github.setter
    def github(self, github:str) -> None:
        self._github = github

    @website.setter
    def website(self, website:str) -> None:
        self._website = website
    

    