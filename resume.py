from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

from src.Content import Component
from src.Skill import Skill
from src.Style import *
import src.data as data
from src.gui import gui

def Heading(document) -> None:
    #First Line
    name = document.add_paragraph(data.NAME + ", " + data.NICKNAME)
    name_format = name.paragraph_format
    name_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    name_format.space_before = 0
    name_format.space_after = Cm(0.2)
    name_format.line_spacing = 1
    name.runs[0].bold = True
    name.runs[0].font.size = Pt(26)
    
    #Second Line
    secondLine = document.add_paragraph("Telephone: ")
    secondLine.add_run(data.TELEPHONE)
    secondLine.add_run(" Email: ")
    secondLine.add_run(data.EMAIL)
    HeadingStyle(secondLine)

    #Third Line
    thirdLine = document.add_paragraph("Github: ")
    thirdLine.add_run(data.GITHUBLINK)
    thirdLine.add_run(" Website: ")
    thirdLine.add_run(data.WEBLINK)
    HeadingStyle(thirdLine)

def Objective(document) -> None:
    heading = document.add_paragraph("OBJECTIVE")
    objective = document.add_paragraph(data.OBJECTIVE + "\n")
    objective_format = objective.paragraph_format
    objective_format.space_before = 0
    objective_format.space_after = 0
    objective_format.line_spacing = data.CONTENTLINESPACE
    objective.runs[0].bold = False
    objective.runs[0].font.size = Pt(11)
    SubHeadingStyle(heading)

def Education(document) -> None:
    # Create object list
    education_content = []
    education_content.append(Component(data.EDUCATION_NAME, data.EDUCATION_DURATION, data.EDUCATION_LIST, data.EDUCATION_DEGREE))
    # Subheading
    heading = document.add_paragraph("EDUCATION")
    SubHeadingStyle(heading)
    # Add Content
    for component in education_content:
        education = document.add_paragraph(component.title)
        table = document.add_table(rows=1, cols=2)
        heading_cells = table.rows[0].cells
        heading_cells[0].text = component.subTitle
        heading_cells[1].text = component.duration[0] + " - " + component.duration[1]
        TableStyle(table)

        ContentDescriptionStyle(document, component.description)

    ContentHeadingStyle(education)

def SideProjects(document) -> None:
    # Create object list
    sideProjects_content = []
    sideProjects_content.append(Component(data.PJ01_NAME, data.PJ01_DURATION, data.PJ01_LIST))
    sideProjects_content.append(Component(data.PJ02_NAME, data.PJ02_DURATION, data.PJ02_LIST))
    # Subheading
    sideProjects = document.add_paragraph("SIDE PROJECT")
    SubHeadingStyle(sideProjects)
    # Add Content
    for component in sideProjects_content:
        if component.subTitle != None:
            sideProject = document.add_paragraph(component.title)
            table = document.add_table(rows=1, cols=2)
            heading_cells = table.rows[0].cells
            heading_cells[0].text = component.subTitle
            heading_cells[1].text = component.duration[0] + " - " + component.duration[1]
            ContentHeadingStyle(sideProject)
        else:
            table = document.add_table(rows=1, cols=2)
            heading_cells = table.rows[0].cells
            heading_cells[0].text = component.title
            heading_cells[1].text = component.duration[0] + " - " + component.duration[1]
            ContentHeadingStyle(heading_cells[0].paragraphs[0])
        TableStyle(table)
        ContentDescriptionStyle(document, component.description)

def Experience(document) -> None:
    # Create object list
    experience_content = []
    experience_content.append(Component(data.EXP01_NAME, data.EXP01_DURATION, data.EXP01_LIST, data.EXP01_SUBTITLE))
    experience_content.append(Component(data.EXP02_NAME, data.EXP02_DURATION, data.EXP02_LIST, data.EXP02_SUBTITLE))
    
    # Subheading
    experience = document.add_paragraph("EXPERIENCE")
    SubHeadingStyle(experience)

    # Add Content
    for component in experience_content:
        experience = document.add_paragraph(component.title)
        table = document.add_table(rows=1, cols=2)
        heading_cells = table.rows[0].cells
        heading_cells[0].text = component.subTitle
        heading_cells[1].text = component.duration[0] + " - " + component.duration[1]
        TableStyle(table)
        ContentHeadingStyle(experience)
        ContentDescriptionStyle(document, component.description)
        

def Skills(document) -> None:
    # Create object list
    skills_content = []
    skills_content.append(Skill(data.SKILL01_CATEGORY, data.SKLL01_LIST))
    skills_content.append(Skill(data.SKILL02_CATEGORY, data.SKILL02_LIST))

    # Subheading
    skills = document.add_paragraph("SKILLS")
    SubHeadingStyle(skills)

    # Add Content
    table = document.add_table(rows=0, cols=2)
    for skill in skills_content:
        table.add_row()
        heading_cells = table.rows[-1].cells
        heading_cells[0].text = skill.category
        heading_cells[1].text = ", ".join(skill.list)
        SkillHeadingStyle(heading_cells[0].paragraphs[0])

    SkillStyle(table)

def main() -> None:
    # Call gui
    user_data = gui()
    print(user_data)

    # Create Document
    document = Document()
    style = document.styles["Normal"]
    style.paragraph_format.space_before = Cm(0.2)
    style.paragraph_format.space_after = 0
    style.paragraph_format.line_spacing = 1.5
    font = style.font
    font.name = "Times New Roman"
    font.size = Pt(11)
    font.bold = False
    
    # font.color.rgb = RGBColor(255,0,0)

    sections = document.sections
    for section in sections:
        section.top_margin = Cm(1)
        section.bottom_margin = Cm(1)
        section.left_margin = Cm(1)
        section.right_margin = Cm(1)

    Heading(document)
    Objective(document)
    Education(document)
    SideProjects(document)
    Experience(document)
    Skills(document)

    # Meta Data
    document.core_properties.author = data.NAME
    document.core_properties.title = data.NAME + " Resume"
    document.core_properties.subject = "Resume"
    document.core_properties.keywords = "Resume, CV, " + data.NAME
    document.core_properties.category = "Resume"
    document.core_properties.language = "en-US"
    
    # Save File
    try:
        document.save(data.NAME + "_resume.docx")
        print("File saved successfully")
    except:
        print("Error: Unable to save file")


if __name__ == "__main__":
    __author__ = "TSE Hui Tung"
    __copyright__ = "Copyright 2023, Formal Resume Generator"
    __license__ = "MIT"
    __version__ = "1.0.0"
    __maintainer__ = "TSE Hui Tung"
    __email__ = "tung23966373@gmail.com"
    __status__ = "Production"
    main()