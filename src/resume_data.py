class reseume_data:
    def __init__(self):
        self._name = "Your Name"
        self._nickname = "Your Nickname"
        self._email = "Your Email"
        self._phone = "Your Phone Number"
        self._github = "Your Github Link"
        self._website = "Your Website Link"
        self._objective = "Your Objective"
        self._education = "Your Education"
        self._experience = "Your Experience"
        self._skills = "Your Skills"
        self._projects = "Your Projects"

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def email(self) -> str:
        return self._email

    @property
    def phone(self) -> str:
        return self._phone
    
    @property
    def objective(self) -> str:
        return self._objective
    
    @property
    def education(self) -> str:
        return self._education
    
    @property
    def experience(self) -> str:
        return self._experience
    
    @property
    def skills(self) -> str:
        return self._skills
    
    @property
    def projects(self) -> str:
        return self._projects
    
    @name.setter
    def name(self, name:str) -> None:
        self._name = name

    @email.setter
    def email(self, email:str) -> None:
        self._email = email
    
    @phone.setter
    def phone(self, phone:str) -> None:
        self._phone = phone

    @objective.setter
    def objective(self, objective:str) -> None:
        self._objective = objective

    @education.setter
    def education(self, education:str) -> None:
        self._education = education
    
    @experience.setter
    def experience(self, experience:str) -> None:
        self._experience = experience

    @skills.setter
    def skills(self, skills:str) -> None:
        self._skills = skills

    @projects.setter
    def projects(self, projects:str) -> None:
        self._projects = projects

    