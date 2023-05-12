import PySimpleGUI as sg
import pathlib
import webbrowser
import os

from src.create_object import *
from src.expend_layout import *
from src.LoadData import LoadData
from src.classes.RowCounter import RowCounter

# from create_object import *
# from LoadData import LoadData

# Window size
WINDOWSWIDTH = 1400
WINDOWSHEIGHT = 870
# Column size
FIXEDCOLUMNWIDTH = 673
FIXEDCOLUMNHEIGHT = 120
COLUMNWIDTH = 650
COLUMNHEIGHT = 160
# Button size
ADDBUTTONWIDTH = 6
BUTTONHEIGHT = 1
# Version
VERSION = "1.0"

KEYS_TO_CLEAR = ["NAME", "NICKNAME", "TELEPHONE", "EMAIL", "GITHUBLINK", "WEBLINK", "OBJECTIVE", "EDUCATION_NAME", "EDUCATION_DEGREE", "EDUCATION_DURATION", "EDUCATION_LIST", "PJ_NAME", "PJ_DURATION", "PJ_LIST", "EXP_NAME", "EXP_DURATION", "EXP_SUBTITLE", "EXP_LIST", "SKILL_CATEGORY", "SKILL_LIST"]

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
                            [sg.Text("Please select the old data file", size=(21,1)), sg.InputText(key="OLD_DATA_PATH", size=(50,1), use_readonly_for_disable=True, disabled=True, background_color=sg.theme_background_color(), text_color="black"), sg.FileBrowse(key="BROWSE_DATA", size=(8,1)),
                            sg.Button('Load', size=(8,1), key="LOAD_DATA", tooltip="Load Old Data")]]
    
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
              [sg.Button('Generate', size=(8,1)), sg.Button('Cancel'), sg.Button("Clean", key="CLEAN"), sg.Button("Delete Data", key="DELETE_DATA" , tooltip="Delete All Input Data"), sg.Text("", key="RESPONSE")],
              copyright_layout]

    # Create the Window
    window = sg.Window(f'Formal Resume Generator v{VERSION}', layout, size=(WINDOWSWIDTH, WINDOWSHEIGHT), font=font, icon=str(pathlib.Path().resolve()) + "\\assets\icon.ico", margins=(10,10))

    # Create Row Counter Object
    row_counter = RowCounter(0,1,0,1,0,1,0,1)

    # Object list
    heading_content = {}
    objective_content = {}
    education_content = {}
    sideproject_content = {}
    experience_content = {}
    skills_content = {}

    # Remove row list
    removed_education_row = []
    removed_sideproject_row = []
    removed_experience_row = []
    removed_skills_row = []

    # Get env data
    if os.path.exists("env data.txt"):
        f = open("env data.txt", "r")
        last_modified_filename = f.readline()
        f.close()
    else:
        last_modified_filename = ""

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            return
        if not isinstance(event, tuple):
            if event.startswith("URL "):
                print(event)
                url = event.split(" ")[1]
                webbrowser.open(url)
        if event == "OLD_DATA_PATH":
            OLD_DATA = values["OLD_DATA_PATH"]
            print(OLD_DATA)
        if event == "LOAD_DATA":
            LoadData(window, row_counter, values["OLD_DATA_PATH"])
        if event == "CLEAN":
            # TODO: reset to 1 row in each of them, also key are now tuple

            for key in KEYS_TO_CLEAR:
                window[key]('')
            for i in range(1, row_counter.education_row_counter+1):
                window[("-EDUCATION_ROW-", i)].update(visible=False)
                print(f"{window[('-EDUCATION_ROW-', i)].visible}")
            for i in range(1, row_counter.sideproject_row_counter+1):
                window[("-SIDEPROJECT_ROW-", i)].update(visible=False)
            for i in range(1, row_counter.experience_row_counter+1):
                window[("-EXPERIENCE_ROW-", i)].update(visible=False)
            for i in range(1, row_counter.skills_row_counter+1):
                window[("-SKILLS_ROW-", i)].update(visible=False)
            # Update Scrollbar
            window.refresh()
            window["-EDUCATION_ROW_PANEL-"].contents_changed()
            window["-SIDEPROJECT_ROW_PANEL-"].contents_changed()
            window["-EXPERIENCE_ROW_PANEL-"].contents_changed()
            window["-SKILLS_ROW_PANEL-"].contents_changed()
        if event == "DELETE_DATA":
            if os.path.exists(last_modified_filename + ".txt"):
                os.remove(last_modified_filename + ".txt")
                print(f"{last_modified_filename}.txt Data deleted")
            if os.path.exists(last_modified_filename + ".docx"):
                os.remove(last_modified_filename + ".docx")
                print(f"{last_modified_filename}.docx Data deleted")
            window["RESPONSE"].update("Data deleted")
        # Add and Remove Row
        if event == "-EDUCATION_ROW_ADD-":
            row_counter.education_row_counter += 1
            row_counter.education_row_number_view += 1
            window.extend_layout(window["-EDUCATION_ROW_PANEL-"], [create_education(row_counter.education_row_counter, row_counter.education_row_number_view)])
            # Update Scrollbar
            window.refresh()
            window["-EDUCATION_ROW_PANEL-"].contents_changed()
        elif event[0] == "-EDUCATION_ROW_REMOVE-":
            window[("-EDUCATION_ROW-", event[1])].update(visible=False)
            window.refresh()
            window["-EDUCATION_ROW_PANEL-"].contents_changed()
            removed_education_row.append(event[1])
            row_counter.education_row_number_view -= 1
        if event == "-SIDEPROJECT_ROW_ADD-":
            row_counter.sideproject_row_counter += 1
            row_counter.sideproject_row_number_view += 1
            window.extend_layout(window["-SIDEPROJECT_ROW_PANEL-"], [create_sideproject(row_counter.sideproject_row_counter, row_counter.sideproject_row_number_view)])
            # Update Scrollbar
            window.refresh()
            window["-SIDEPROJECT_ROW_PANEL-"].contents_changed()
        elif event[0] == "-SIDEPROJECT_ROW_REMOVE-":
            window[("-SIDEPROJECT_ROW-", event[1])].update(visible=False)
            window.refresh()
            window["-SIDEPROJECT_ROW_PANEL-"].contents_changed()
            removed_sideproject_row.append(event[1])
            row_counter.sideproject_row_number_view -= 1
        if event == "-EXPERIENCE_ROW_ADD-":
            row_counter.experience_row_counter += 1
            row_counter.experience_row_number_view += 1
            window.extend_layout(window["-EXPERIENCE_ROW_PANEL-"], [create_experience(row_counter.experience_row_counter, row_counter.experience_row_number_view)])
            # Update Scrollbar
            window.refresh()
            window["-EXPERIENCE_ROW_PANEL-"].contents_changed()
        elif event[0] == "-EXPERIENCE_ROW_REMOVE-":
            window[("-EXPERIENCE_ROW-", event[1])].update(visible=False)
            window.refresh()
            window["-EXPERIENCE_ROW_PANEL-"].contents_changed()
            removed_experience_row.append(event[1])
            row_counter.experience_row_number_view -= 1
        if event == "-SKILLS_ROW_ADD-":
            row_counter.skills_row_counter += 1
            row_counter.skills_row_number_view += 1
            window.extend_layout(window["-SKILLS_ROW_PANEL-"], [create_skills(row_counter.skills_row_counter, row_counter.skills_row_number_view)])
            # Update Scrollbar
            window.refresh()
            window["-SKILLS_ROW_PANEL-"].contents_changed()
        elif event[0] == "-SKILLS_ROW_REMOVE-":
            window[("-SKILLS_ROW-", event[1])].update(visible=False)
            window.refresh()
            window["-SKILLS_ROW_PANEL-"].contents_changed()
            removed_skills_row.append(event[1])
            # remove_keys = [('SKILL_LIST', event[1]), ('SKILL_CATEGORY', event[1])]
            # for key in remove_keys:
            #     values.pop(key, None)
            row_counter.skills_row_number_view -= 1
        # Generate
        heading = ["NAME", "NICKNAME", "TELEPHONE", "EMAIL", "GITHUBLINK", "WEBLINK"]
        if event == 'Generate':
            # TODO: Check if the file is opening or not first, if opening then error to close it first
            print(values)
            for key, value in values.items():
                if key in heading:
                    heading_content[key] = value
                if key == "OBJECTIVE":
                    objective_content[key] = value
                if isinstance(key, tuple):
                    if key[0].startswith("EDUCATION"):
                        education_content[key] = value
                    elif key[0].startswith("PJ"):
                        sideproject_content[key] = value
                    elif key[0].startswith("EXP"):
                        experience_content[key] = value
                    elif key[0].startswith("SKILL"):
                        skills_content[key] = value
            break

    for row in removed_education_row:
        education_content.pop(("EDUCATION_NAME", row), None)
        education_content.pop(("EDUCATION_DEGREE", row), None)
        education_content.pop(("EDUCATION_DURATION", row), None)
        education_content.pop(("EDUCATION_LIST", row), None)
    for row in removed_sideproject_row:
        sideproject_content.pop(("PJ_NAME", row), None)
        sideproject_content.pop(("PJ_DURATION", row), None)
        sideproject_content.pop(("PJ_LIST", row), None)
    for row in removed_experience_row:
        experience_content.pop(("EXP_NAME", row), None)
        experience_content.pop(("EXP_DURATION", row), None)
        experience_content.pop(("EXP_SUBTITLE", row), None)
        experience_content.pop(("EXP_LIST", row), None)
    for row in removed_skills_row:
        skills_content.pop(("SKILL_CATEGORY", row), None)
        skills_content.pop(("SKILL_LIST", row), None)

    massaged_heading_content = []
    massaged_objective_content = []
    massaged_education_content = []
    massaged_sideproject_content = []
    massaged_experience_content = []
    massaged_skills_content = []
    massaged_values = {}

    for key, value in heading_content.items():
        massaged_heading_content.append(value)
        massaged_values[key] = value
    for key, value in objective_content.items():
        massaged_objective_content.append(value)
        massaged_values[key] = value
    for key, value in education_content.items():
        massaged_education_content.append(value)
        massaged_values[key] = value
    for key, value in sideproject_content.items():
        massaged_sideproject_content.append(value)
        massaged_values[key] = value
    for key, value in experience_content.items():
        massaged_experience_content.append(value)
        massaged_values[key] = value
    for key, value in skills_content.items():
        massaged_skills_content.append(value)
        massaged_values[key] = value

    print("Massaged Values")
    print(massaged_values)

    #save resume data'
    file_name = values["NAME"] + "_resume"
    f = open(file_name + ".txt", "w")
    f.write("Formal Resume Generator 2023\n")
    f.write(f"{row_counter.education_row_number_view}, {row_counter.sideproject_row_number_view}, {row_counter.experience_row_number_view}, {row_counter.skills_row_number_view}\n")
    f.write(str(heading_content) + "\n")
    f.write(str(objective_content) + "\n")
    f.write(str(education_content) + "\n")
    f.write(str(sideproject_content) + "\n")
    f.write(str(experience_content) + "\n")
    f.write(str(skills_content) + "\n")
    f.close()

    #save last modified meta data, use to delete old data
    f = open("env data.txt", "w")
    f.write(file_name)
    f.close()

    window.close()
    return create_heading_object(massaged_heading_content), create_objective_object(massaged_objective_content), create_education_object(massaged_education_content), create_side_projects_object(massaged_sideproject_content), create_experience_object(massaged_experience_content), create_skill_object(massaged_skills_content)

if __name__ == "__main__":
    gui()
