import PySimpleGUI as sg
import pathlib
import webbrowser

from src.create_object import *

# Reference:
# 1. Scroll Bar Update
# https://stackoverflow.com/questions/65811804/how-to-automatically-update-the-pysimplegui-column-scroll-bar
# 2. Dynamic Column
# https://github.com/amithr/PySimpleGUI-Dynamically-Add-Elements/blob/main/main.py


# Window size
WINDOWSWIDTH = 1400
WINDOWSHEIGHT = 870
# Column size
FIXEDCOLUMNWIDTH = 673
FIXEDCOLUMNHEIGHT = 120
COLUMNWIDTH = 650
COLUMNHEIGHT = 160
# Content size
FIRSTTEXTWIDTH = 10
SECONDTEXTWIDTH = 6
INPUTWIDTH = 25
FULLWIDTH = INPUTWIDTH * 2 + SECONDTEXTWIDTH + 2
# Button size
ADDBUTTONWIDTH = 6
REMOVEBUTTONWIDTH = 8
BUTTONHEIGHT = 1
# Version
VERSION = "1.0"

education_row_counter = 0
education_row_number_view = 1
sideproject_row_counter = 0
sideproject_row_number_view = 1
experience_row_counter = 0
experience_row_number_view = 1
skills_row_counter = 0
skills_row_number_view = 1

# add button which can expand another objective input field
def create_education(row_counter, row_number_view) -> list:
    row = [sg.pin(
        sg.Column([[sg.Text(f"#{row_number_view}", font='Arial 11 bold'), sg.Button('Remove', size=(REMOVEBUTTONWIDTH,BUTTONHEIGHT), enable_events=True, key=("-EDUCATION_ROW_REMOVE-", row_counter), tooltip="Delete Last Education Field")],
                [sg.Text('School Name', size=(FIRSTTEXTWIDTH,1)), sg.InputText(key="EDUCATION_NAME", size=(INPUTWIDTH,1)), sg.Text('Degree', size=(SECONDTEXTWIDTH,1)), sg.InputText(key="EDUCATION_DEGREE", size=(INPUTWIDTH,1))],
                [sg.Text('Duration', size=(FIRSTTEXTWIDTH,1)), sg.InputText(key="EDUCATION_DURATION", size=(INPUTWIDTH,1))],
                [sg.Text('Description', size=(FIRSTTEXTWIDTH,1)), sg.Multiline(key="EDUCATION_LIST", size=(FULLWIDTH,3))]],
                key=("-EDUCATION_ROW-", education_row_counter)
        ))]
    return row

def create_sideproject(row_counter, row_number_view) -> list:
    row = [sg.pin(
        sg.Column([[sg.Text(f"# {row_number_view}", font='Arial 11 bold'), sg.Button('Remove', size=(REMOVEBUTTONWIDTH,BUTTONHEIGHT), enable_events=True, key=("-SIDEPROJECT_ROW_REMOVE-", row_counter), tooltip="Delete Last Side Project Field")],
             [sg.Text('Name', size=(FIRSTTEXTWIDTH,1)), sg.InputText(key="PJ_NAME", size=(INPUTWIDTH,1)), sg.Text('Duration', size=(SECONDTEXTWIDTH,1)), sg.InputText(key="PJ_DURATION", size=(INPUTWIDTH,1))],
             [sg.Text('Description', size=(FIRSTTEXTWIDTH,1)), sg.Multiline(key="PJ_LIST", size=(FULLWIDTH,3))]],
             key=("-SIDEPROJECT_ROW-", sideproject_row_counter)
        ))]
    return row

def create_experience(row_counter, row_number_view) -> list:
    row = [sg.pin(
        sg.Column([[sg.Text(f"# {row_number_view}", font='Arial 11 bold'), sg.Button('Remove', size=(REMOVEBUTTONWIDTH,BUTTONHEIGHT), enable_events=True, key=("-EXPERIENCE_ROW_REMOVE-", row_counter), tooltip="Delete Last Experience Field")],
                [sg.Text('Name', size=(8,1)), sg.InputText(key="EXP_NAME", size=(25,1)), sg.Text('Duration', size=(8,1)), sg.InputText(key="EXP_DURATION", size=(25,1))],
                [sg.Text('Subtitle', size=(8,1)), sg.InputText(key="EXP_SUBTITLE", size=(25,1))],
                [sg.Text('Description', size=(8,1)), sg.Multiline(key="EXP_LIST", size=(60,3))]],
                key=("-EXPERIENCE_ROW-", experience_row_counter)
            ))]
    return row

def create_skills(row_counter, row_number_view) -> list:
    row = [sg.pin(
        sg.Column([[sg.Text(f"# {row_number_view}", font='Arial 11 bold'), sg.Button('Remove', size=(REMOVEBUTTONWIDTH,BUTTONHEIGHT), enable_events=True, key=("-SKILLS_ROW_REMOVE-", row_counter), tooltip="Delete Last Skills Field")],
                [sg.Text('Category', size=(8,1)), sg.InputText(key="SKILL_CATEGORY", size=(25,1))],
                [sg.Text('List', size=(8,1)), sg.Multiline(key="SKILL_LIST", size=(60,3))]],
                key=("-SKILLS_ROW-", skills_row_counter)
            ))]
    return row


def gui() -> dict:
    # Add a touch of color
    sg.theme('DarkAmber')   
    font = ("Arial", 11)
    
    menu_layout = [['File', ['Open', 'Save', 'Exit', 'Properties']],
                ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
                ['Help', 'About...'], ]

    instruction_layout = [ [sg.Text('Instruction', font='Arial 14 bold')],
                            [sg.Text("This is a Formal Resume Generator, for more infomation, please refer to"),
                             sg.Text("resume-generator", tooltip="https://github.com/Argonaut790/resume-generator.git", enable_events=True, key="URL https://github.com/Argonaut790/resume-generator.git", text_color="skyblue")],
                            [sg.Text("**Disclaimer** All The Information Won't Be Stored", text_color="red", font = ("Arial", 9))] ]

    intro_layout = [[sg.Column([[sg.Image(str(pathlib.Path().resolve()) + "\\assets\icon.png")]], size=(110,110)), sg.Column(instruction_layout)]]

    browse_old_data_layout = [[sg.Text('Browse Old Data', font='Arial 14 bold')],
                            [sg.Text("Please select the old data file", size=(21,1)), sg.InputText(key="OLDDATA", size=(50,1), use_readonly_for_disable=True, disabled=True, background_color=sg.theme_background_color(), text_color="black"), sg.FileBrowse(key="BROWSE", size=(8,1)),
                            sg.Button('Load', size=(8,1))]]
    
    heading_layout = [  [sg.Text('Heading', font='Arial 14 bold')],
                [sg.Text('Name', size=(8,1)), sg.InputText(key="NAME", size=(25,1), ), sg.Text('Nickname', size=(8,1)), sg.InputText(key="NICKNAME", size=(25,1))],
                [sg.Text('Telephone', size=(8,1)), sg.InputText(key="TELEPHONE", size=(25,1)), sg.Text('Email', size=(8,1)), sg.InputText(key="EMAIL", size=(25,1))],
                [sg.Text('Github Link', size=(8,1)), sg.InputText(key="GITHUBLINK", size=(25,1)), sg.Text('Web Link', size=(8,1)), sg.InputText(key="WEBLINK", size=(25,1))],
                 ]
                      
    objective_layout = [[sg.Text('Objective', font='Arial 14 bold')],
                [sg.Text('Objective', size=(8,1)), sg.Multiline(key="OBJECTIVE", size=(60,3))] ]

    education_layout = [[sg.Text('Education', font='Arial 14 bold')],
                        [sg.Column([create_education(0, 1)], key="-EDUCATION_ROW_PANEL-", scrollable=True,  vertical_scroll_only=True, size=(COLUMNWIDTH, COLUMNHEIGHT))],
                        [sg.Button('Add', size=(ADDBUTTONWIDTH,BUTTONHEIGHT), enable_events=True, key="-EDUCATION_ROW_ADD-", tooltip="Add Another Education Field")]]

    sideproject_layout = [[sg.Text('Side Project', font='Arial 14 bold')],
                [sg.Column([create_sideproject(0, 1)], key="-SIDEPROJECT_ROW_PANEL-", scrollable=True,  vertical_scroll_only=True, size=(COLUMNWIDTH, COLUMNHEIGHT))],
                [sg.Button('Add', size=(ADDBUTTONWIDTH,BUTTONHEIGHT), enable_events=True, key="-SIDEPROJECT_ROW_ADD-", tooltip="Add Another Side Project Field")]]
    
    experience_layout = [[sg.Text('Experience', font='Arial 14 bold')],
                [sg.Column([create_experience(0, 1)], key="-EXPERIENCE_ROW_PANEL-", scrollable=True,  vertical_scroll_only=True, size=(COLUMNWIDTH, COLUMNHEIGHT))],
                [sg.Button('Add', size=(ADDBUTTONWIDTH,BUTTONHEIGHT), enable_events=True, key="-EXPERIENCE_ROW_ADD-", tooltip="Add Another Experience Field")]]

    skills_layout = [[sg.Text('Skills', font='Arial 14 bold')],
                [sg.Column([create_skills(0, 1)], key="-SKILLS_ROW_PANEL-", scrollable=True,  vertical_scroll_only=True, size=(COLUMNWIDTH, COLUMNHEIGHT))],
                [sg.Button('Add', size=(ADDBUTTONWIDTH,BUTTONHEIGHT), enable_events=True, key="-SKILLS_ROW_ADD-", tooltip="Add Another Skills Field")]]

    copyright_layout = [[sg.Text("Copyright 2023, Formal Resume Generator, Tse Hui Tung", text_color="gray", font=("mono", 8)),]]

    # All the stuff inside your window.
    layout = [ [sg.Menu(menu_layout, background_color='white', tearoff=False, text_color='black', key="-MENU-") ],
                intro_layout,
                browse_old_data_layout,
                [sg.Column(heading_layout, size=(FIXEDCOLUMNWIDTH, FIXEDCOLUMNHEIGHT)),
                sg.Column(objective_layout, size=(FIXEDCOLUMNWIDTH, FIXEDCOLUMNHEIGHT))],
                [sg.Column(education_layout),
                sg.Column(sideproject_layout)],
                [sg.Column(experience_layout),
                sg.Column(skills_layout)],
              [sg.Button('Generate', size=(8,1)), sg.Button('Cancel')],
              copyright_layout]

    # Create the Window
    window = sg.Window(f'Formal Resume Generator v{VERSION}', layout, size=(WINDOWSWIDTH, WINDOWSHEIGHT), font=font, icon=str(pathlib.Path().resolve()) + "\\assets\icon.ico", margins=(10,10))

    # Initiate global variables
    global education_row_counter
    global education_row_number_view
    global sideproject_row_counter
    global sideproject_row_number_view
    global experience_row_counter
    global experience_row_number_view
    global skills_row_counter
    global skills_row_number_view

    # Object list
    heading_content = []
    objective_content = []
    education_content = []
    sideproject_content = []
    experience_content = []
    skills_content = []

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            return
        if event[0].startswith("URL "):
            url = event.split(" ")[1]
            webbrowser.open(url)
        if event == "OLD_DATA":
            OLD_DATA = values["OLD_DATA"]
            print(OLD_DATA)
        
        if event == "-EDUCATION_ROW_ADD-":
            education_row_counter += 1
            education_row_number_view += 1
            window.extend_layout(window["-EDUCATION_ROW_PANEL-"], [create_education(education_row_counter, education_row_number_view)])
            # Update Scrollbar
            window.refresh()
            window["-EDUCATION_ROW_PANEL-"].contents_changed()
        elif event[0] == "-EDUCATION_ROW_REMOVE-":
            window[("-EDUCATION_ROW-", event[1])].update(visible=False)
            window.refresh()
            window["-EDUCATION_ROW_PANEL-"].contents_changed()
            education_row_number_view -= 1
        if event == "-SIDEPROJECT_ROW_ADD-":
            sideproject_row_counter += 1
            sideproject_row_number_view += 1
            window.extend_layout(window["-SIDEPROJECT_ROW_PANEL-"], [create_sideproject(sideproject_row_counter, sideproject_row_number_view)])
            # Update Scrollbar
            window.refresh()
            window["-SIDEPROJECT_ROW_PANEL-"].contents_changed()
        elif event[0] == "-SIDEPROJECT_ROW_REMOVE-":
            window[("-SIDEPROJECT_ROW-", event[1])].update(visible=False)
            window.refresh()
            window["-SIDEPROJECT_ROW_PANEL-"].contents_changed()
            sideproject_row_number_view -= 1
        if event == "-EXPERIENCE_ROW_ADD-":
            experience_row_counter += 1
            experience_row_number_view += 1
            window.extend_layout(window["-EXPERIENCE_ROW_PANEL-"], [create_experience(experience_row_counter, experience_row_number_view)])
            # Update Scrollbar
            window.refresh()
            window["-EXPERIENCE_ROW_PANEL-"].contents_changed()
        elif event[0] == "-EXPERIENCE_ROW_REMOVE-":
            window[("-EXPERIENCE_ROW-", event[1])].update(visible=False)
            window.refresh()
            window["-EXPERIENCE_ROW_PANEL-"].contents_changed()
            experience_row_number_view -= 1
        if event == "-SKILLS_ROW_ADD-":
            skills_row_counter += 1
            skills_row_number_view += 1
            window.extend_layout(window["-SKILLS_ROW_PANEL-"], [create_skills(skills_row_counter, skills_row_number_view)])
            # Update Scrollbar
            window.refresh()
            window["-SKILLS_ROW_PANEL-"].contents_changed()
        elif event[0] == "-SKILLS_ROW_REMOVE-":
            window[("-SKILLS_ROW-", event[1])].update(visible=False)
            window.refresh()
            window["-SKILLS_ROW_PANEL-"].contents_changed()
            skills_row_number_view -= 1

        if event == 'Generate':
            # TODO: Check if the file is opening or not first, if opening then error to close it first
            print(values)
            for key, value in values.items():
                if key == "NAME":
                    heading_content.append(value)
                elif key == "NICKNAME":
                    heading_content.append(value)
                elif key == "TELEPHONE":
                    heading_content.append(value)
                elif key == "EMAIL":
                    heading_content.append(value)
                elif key == "GITHUBLINK":
                    heading_content.append(value)
                elif key == "WEBLINK":
                    heading_content.append(value)
                elif key == "OBJECTIVE":
                    objective_content.append(value)
                elif key.startswith("EDUCATION"):
                    education_content.append(value)
                elif key.startswith("PJ"):
                    sideproject_content.append(value)
                elif key.startswith("EXP"):
                    experience_content.append(value)
                elif key.startswith("SKILL"):
                    skills_content.append(value)
            break
    #save resume data'
    f = open("resume.txt", "w")
    f.write("Formal Resume Generator 2023")
    f.write(str(values))
    f.close()

    window.close()
    return create_heading_object(heading_content), create_objective_object(objective_content), create_education_object(education_content), create_side_projects_object(sideproject_content), create_experience_object(experience_content), create_skill_object(skills_content)

if __name__ == "__main__":
    gui()
