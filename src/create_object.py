# Create data Object
from src.classes.Heading import Heading
from src.classes.Objective import Objective
from src.classes.Content import Component
from src.classes.Skill import Skill

# from classes.Heading import Heading
# from classes.Objective import Objective
# from classes.Content import Component
# from classes.Skill import Skill


def create_heading_object(li:list) -> Component:
    if len(li) != 6:
        raise ValueError("Heading list must have 6 elements")
    if not li[0]:
        name = "[Your Name]"
    else:
        name = li[0]
    if not li[1]:
        nickname = "[Your Nickname]"
    else:
        nickname = li[1]
    if not li[2]:
        telephone = "[Your Telephone]"
    else:
        telephone = li[2]
    if not li[3]:
        email = "[Your Email]"
    else:
        email = li[3]
    if not li[4]:
        github = "[Your Github]"
    else:
        github = li[4]
    if not li[5]:
        website = "[Your Website]"
    else:
        website = li[5]
    return Heading(name, nickname, email, telephone, github, website)

def create_objective_object(li:list) -> Component:
    if len(li) != 1:
        raise ValueError("Objective list must have 1 element")
    if not li[0]:
        objective = "[Your Objective]"
    else:
        objective = li[0]
    return Objective(objective)

def create_education_object(li:list) -> list:
    if len(li)%4:
        raise ValueError("Education list must have 4 elements")
    education_list = []
    for i in range(0, len(li), 4):
        if not li[i]:
            education_name = "[Your Education]"
        else:
            education_name = li[i]
        if not li[i+1]:
            education_subTitle = "[Your Degree]"
        else:
            education_subTitle = li[i+1]
        if not li[i+2]:
            education_duration = ["[Start Date]", "[End Date]"]
        else:
            education_duration = li[i+2]
        if not li[i+3]:
            education_description = ["[Description]"]
        else:
            education_description = li[i+3]
        education_list.append(Component(education_name, education_duration, education_description, education_subTitle))
    return education_list

def create_side_projects_object(li:list) -> list:
    if len(li)%3:
        raise ValueError("Side Projects list must have 3 elements")
    side_projects_list = []
    for i in range(0, len(li), 3):
        if not li[i]:
            side_projects_name = "[Your Projects]"
        else:
            side_projects_name = li[0]
        if not li[i+1]:
            side_projects_duration = ["[Start Date]", "[End Date]"]
        else:
            side_projects_duration = li[1]
        if not li[i+2]:
            side_projects_description = ["[Description]"]
        else:
            side_projects_description = li[2]
        side_projects_list.append(Component(side_projects_name, side_projects_duration, side_projects_description))
    return side_projects_list

def create_experience_object(li:list) -> list:
    if len(li)%4:
        raise ValueError("Experience list must have 4 elements")
    experience_list = []
    for i in range(0, len(li), 4):
        if not li[i]:
            experience_name = "[Your Experience]"
        else:
            experience_name = li[i]
        if not li[i+1]:
            experience_subTitle = "[Your Position]"
        else:
            experience_subTitle = li[i+1]
        if not li[i+2]:
            experience_duration = ["[Start Date]", "[End Date]"]
        else:
            experience_duration = li[i+2]
        if not li[i+3]:
            experience_description = ["[Description]"]
        else:
            experience_description = li[i+3]
        experience_list.append(Component(experience_name, experience_duration, experience_description, experience_subTitle))
    return experience_list

def create_skill_object(li:list) -> list:
    if len(li)%2:
        raise ValueError("Skill list must have 2 elements")
    print(f"list = {li}")
    skill_list = []
    for i in range(0, len(li), 2):
        if not li[i]:
            skill_category = "[Your Skills]"
        else:
            skill_category = li[i]
        if not li[i+1]:
            skill_content = "[Skill 1], [Skill 2]"
        else:
            skill_content = li[i+1]
        skill_list.append(Skill(skill_category, skill_content))
    return skill_list