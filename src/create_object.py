# Create data Object
from src.classes.Heading import Heading
from src.classes.Objective import Objective
from src.classes.Component import Component
from src.classes.Skill import Skill
from src.gui_metadata import *

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

def create_object(content: dict, content_counter: int) -> list:
    content_list = []
    for i in range(content_counter):
        component_object= Component("", "", "")
        description_list = []
        for key, value in content.items():
            if key[1] == i:
                if len(key) == 2:
                    if key[0].endswith("NAME"):
                        if not value:
                            component_object.title = "[Title]"
                        else:
                            component_object.title = value
                    elif key[0].endswith("START"):
                        if not value:
                            component_object.start = "[Start Month] [Start Year]"
                        else:
                            component_object.start = value
                    elif key[0].endswith("END"):
                        if not value:
                            component_object.end = "[End Month] [End Year]"
                        else:
                            component_object.end = value
                    elif key[0].endswith("DEGREE") or key[0].endswith("SUBTITLE"):
                        if not value:
                            component_object.subTitle = "[Subtitle]"
                        else:
                            component_object.subTitle = value
                elif len(key) == 3:
                    if key[0].endswith("LIST"):
                        if not value:
                            description_list.append("[Description]")
                        else:
                            description_list.append(value)
                else:
                    raise ValueError(f"Something wrong with the content key: {key}")
        component_object.description = description_list
        content_list.append(component_object)
    return content_list

def create_skill_object(li:list) -> list:
    if len(li) % (SKILLSFIELD-1):
        raise ValueError(f"Skill list must have {SKILLSFIELD} elements")
    skill_list = []
    for i in range(0, len(li), SKILLSFIELD-1):
        if not li[i]:
            skill_category = "[Skill Category]"
        else:
            skill_category = li[i]
        if not li[i+1]:
            skill_content = "[Skill 1], [Skill 2]"
        else:
            skill_content = li[i+1]
        skill_list.append(Skill(skill_category, skill_content))
    return skill_list