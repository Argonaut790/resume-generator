# Create data Object
from src.classes.Heading import Heading
from src.classes.Objective import Objective
from src.classes.Content import Component
from src.classes.Skill import Skill
from src.gui_metadata import *

# from classes.Heading import Heading
# from classes.Objective import Objective
# from classes.Content import Component
# from classes.Skill import Skill


def create_heading_object(li:list) -> Component:
    if len(li) != HEADINGSFIELD:
        raise ValueError(f"Heading list must have {HEADINGSFIELD} elements")
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
    if len(li) != OBJECTIVEFIELD:
        raise ValueError(f"Objective list must have {OBJECTIVEFIELD} element")
    if not li[0]:
        objective = "[Your Objective]"
    else:
        objective = li[0]
    return Objective(objective)

def create_education_object(li:list) -> list:
    if len(li) % EDUCATIONFIELD:
        raise ValueError(f"Education list must have {EDUCATIONFIELD} elements")
    education_list = []
    for i in range(0, len(li), EDUCATIONFIELD):
        if not li[i]:
            education_name = "[Your Education]"
        else:
            education_name = li[i]
        if not li[i+1]:
            education_subTitle = "[Your Degree]"
        else:
            education_subTitle = li[i+1]
        if not li[i+2]:
            education_start_month = "[Start Month]"
        else:
            education_start_month = li[i+2]
        if not li[i+3]:
            education_start_year = "[Start Year]"
        else:
            education_start_year = li[i+3]
        education_start = f"{education_start_month} {education_start_year}"
        if not li[i+4]:
            education_end_month = "[End Month]"
        else:
            education_end_month = li[i+4]
        if not li[i+5]:
            education_end_year = "[End Year]"
        else:
            education_end_year = li[i+5]
        education_end = f"{education_end_month} {education_end_year}"
        if not li[i+6]:
            education_description = ["[Description]"]
        else:
            education_description = li[i+6]
        education_list.append(Component(education_name, education_start, education_end, education_description, education_subTitle))
    return education_list

def create_side_projects_object(li:list) -> list:
    if len(li) % SIDEPROJECTFIELD:
        raise ValueError(f"Side Projects list must have {SIDEPROJECTFIELD} elements")
    side_projects_list = []
    for i in range(0, len(li), SIDEPROJECTFIELD):
        if not li[i]:
            side_projects_name = "[Your Projects]"
        else:
            side_projects_name = li[0]
        if not li[i+1]:
            side_projects_start_month = "[Start Month]"
        else:
            side_projects_start_month = li[i+1]
        if not li[i+2]:
            side_projects_start_year = "[Start Year]"
        else:
            side_projects_start_year = li[i+2]
        side_projects_start = f"{side_projects_start_month} {side_projects_start_year}"
        if not li[i+3]:
            side_projects_end_month = "[End Month]"
        else:
            side_projects_end_month = li[i+3]
        if not li[i+4]:
            side_projects_end_year = "[End Year]"
        else:
            side_projects_end_year = li[i+4]
        side_projects_end = f"{side_projects_end_month} {side_projects_end_year}"
        if not li[i+5]:
            side_projects_description = ["[Description]"]
        else:
            side_projects_description = li[5]
        side_projects_list.append(Component(side_projects_name, side_projects_start, side_projects_end, side_projects_description))
    return side_projects_list

def create_experience_object(li:list) -> list:
    if len(li) % EXPERIENCEFIELD:
        raise ValueError(f"Experience list must have {EXPERIENCEFIELD} elements")
    experience_list = []
    for i in range(0, len(li), EXPERIENCEFIELD):
        if not li[i]:
            experience_name = "[Your Experience]"
        else:
            experience_name = li[i]
        if not li[i+1]:
            experience_subTitle = "[Your Position]"
        else:
            experience_subTitle = li[i+1]
        if not li[i+2]:
            experience_start_month = "[Start Month]"
        else:
            experience_start_month = li[i+2]
        if not li[i+3]:
            experience_start_year = "[Start Year]"
        else:
            experience_start_year = li[i+3]
        experience_start = f"{experience_start_month} {experience_start_year}"
        if not li[i+4]:
            experience_end_month = "[End Month]"
        else:
            experience_end_month = li[i+4]
        if not li[i+5]:
            experience_end_year = "[End Year]"
        else:
            experience_end_year = li[i+5]
        experience_end = f"{experience_end_month} {experience_end_year}"
        if not li[i+4]:
            experience_description = ["[Description]"]
        else:
            experience_description = li[i+4]
        experience_list.append(Component(experience_name, experience_start, experience_end, experience_description, experience_subTitle))
    return experience_list

def create_skill_object(li:list) -> list:
    if len(li) % SKILLSFIELD:
        raise ValueError(f"Skill list must have {SKILLSFIELD} elements")
    skill_list = []
    for i in range(0, len(li), SKILLSFIELD):
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