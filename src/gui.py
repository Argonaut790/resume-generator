import PySimpleGUI as sg
import pathlib
import webbrowser
import os

from src.create_object import *
from src.expend_layout import *
from src.gui_metadata import *
from src.ResetKey import ResetKey
from src.LoadData import LoadData
from src.classes.RowCounter import RowCounter
from src.classes.ListCounter import ListCounter
from src.classes.RemovedContent import RemovedContent

def move_center(window):
    screen_width, screen_height = window.get_screen_dimensions()
    win_width, win_height = window.size
    x, y = (screen_width - win_width)//2, (screen_height - win_height)//2
    window.move(x, y)

def gui(console_message) -> dict:
    # Add a touch of color
    sg.theme(data.THEME)   
    font = ("Arial", 11)
    
    menu_layout = [['File', ['Open', 'Save', 'Exit', 'Properties']],
                ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
                ['Help', 'About...'], ]

    instruction_layout = [ [sg.Text('Instruction', font='Arial 14 bold')],
                            [sg.Text("This is a Formal Resume Generator, for more infomation, please refer to"),
                             sg.Text("resume-generator", tooltip="https://github.com/Argonaut790/resume-generator.git", enable_events=True, key="URL https://github.com/Argonaut790/resume-generator.git", text_color="skyblue")],
                            [sg.Text("**Disclaimer** All The Information Won't Be Stored", text_color="red", font = ("Arial", 9))] ]

    intro_layout = [[sg.Column([[sg.Image(str(pathlib.Path().resolve()) + "\\assets\icon.png")]], size=(107,107)),
                      sg.Column(instruction_layout)]]

    browse_old_data_layout = [[sg.Text('Browse Old Data', font='Arial 14 bold')],
                            [sg.Text("Please select the old data file", size=(21,1)), sg.InputText(key="OLD_DATA_PATH", size=(50,1), use_readonly_for_disable=True, disabled=True, disabled_readonly_background_color=sg.theme_background_color(), disabled_readonly_text_color=sg.theme_text_color()), sg.FileBrowse(key="BROWSE_DATA", size=(8,1)),
                            sg.Button('Load', size=(8,1), key="LOAD_DATA", tooltip="Load Old Data")]]
    
    heading_layout = [  [sg.Text('Heading', font='Arial 14 bold')],
                [sg.Text('Name', size=(8,1)), sg.InputText(key="NAME", size=(25,1), ), sg.Text('Nickname', size=(8,1)), sg.InputText(key="NICKNAME", size=(25,1))],
                [sg.Text('Telephone', size=(8,1)), sg.InputText(key="TELEPHONE", size=(25,1)), sg.Text('Email', size=(8,1)), sg.InputText(key="EMAIL", size=(25,1))],
                [sg.Text('Github Link', size=(8,1)), sg.InputText(key="GITHUBLINK", size=(25,1)), sg.Text('Web Link', size=(8,1)), sg.InputText(key="WEBLINK", size=(25,1))],
                 ]
                      
    objective_layout = [[sg.Text('Objective', font='Arial 14 bold')],
                [sg.Text('Objective', size=(data.FIRSTTEXTWIDTH,1)), sg.Multiline(key="OBJECTIVE", size=(data.FULLWIDTH,5))] ]

    education_layout = [[sg.Text('Education', font='Arial 14 bold')],
                        [sg.Column([create_education(0, 1)], key="-EDUCATION_ROW_PANEL-", scrollable=True,  vertical_scroll_only=True, size=(COLUMNWIDTH, COLUMNHEIGHT))],
                        [sg.Button('Add', size=(ADDBUTTONWIDTH,BUTTONHEIGHT), enable_events=True, key="-EDUCATION_ROW_ADD-", tooltip="Add Another Education Field")]]

    sideproject_layout = [[sg.Text('Side Project', font='Arial 14 bold')],
                [sg.Column([create_sideproject(0, 1)], key="-PJ_ROW_PANEL-", scrollable=True,  vertical_scroll_only=True, size=(COLUMNWIDTH, COLUMNHEIGHT))],
                [sg.Button('Add', size=(ADDBUTTONWIDTH,BUTTONHEIGHT), enable_events=True, key="-PJ_ROW_ADD-", tooltip="Add Another Side Project Field")]]
    
    experience_layout = [[sg.Text('Experience', font='Arial 14 bold')],
                [sg.Column([create_experience(0, 1)], key="-EXP_ROW_PANEL-", scrollable=True,  vertical_scroll_only=True, size=(COLUMNWIDTH, COLUMNHEIGHT))],
                [sg.Button('Add', size=(ADDBUTTONWIDTH,BUTTONHEIGHT), enable_events=True, key="-EXPE_ROW_ADD-", tooltip="Add Another Experience Field")]]

    skills_layout = [[sg.Text('Skills', font='Arial 14 bold')],
                [sg.Column([create_skills(0, 1)], key="-SKILLS_ROW_PANEL-", scrollable=True,  vertical_scroll_only=True, size=(COLUMNWIDTH, COLUMNHEIGHT))],
                [sg.Button('Add', size=(ADDBUTTONWIDTH,BUTTONHEIGHT), enable_events=True, key="-SKILLS_ROW_ADD-", tooltip="Add Another Skills Field")]]

    copyright_layout = [[sg.Text("Copyright 2023, Formal Resume Generator, Tse Hui Tung", text_color="gray", font=("mono", 8)),]]

    # All the stuff inside your window.
    layout = [ 
                # [sg.Menu(menu_layout, background_color='white', tearoff=False, text_color='black', key="-MENU-") ],
                [sg.Column(intro_layout)],
                [sg.Column(browse_old_data_layout)],
                [sg.Column(heading_layout, size=(FIXEDCOLUMNWIDTH, FIXEDCOLUMNHEIGHT)),
                sg.Column(objective_layout, size=(FIXEDCOLUMNWIDTH, FIXEDCOLUMNHEIGHT))],
                [sg.Column(education_layout),
                sg.Column(sideproject_layout)],
                [sg.Column(experience_layout),
                sg.Column(skills_layout)],
              [sg.Button('Generate', size=(8,1)), 
               sg.Button('Cancel'), sg.Button("Clean", key="CLEAN"), 
               sg.Button("Delete Data", key="DELETE_DATA" , tooltip="Delete All Input Data"), 
               sg.Text("", key="RESPONSE")],
              [sg.Column(copyright_layout)]]

    layout = [[sg.Column(layout, size=(WINDOWSWIDTH, WINDOWSHEIGHT), scrollable=True, pad=(0,0))]]
    # Create the Window
    window = sg.Window(f'Formal Resume Generator v{VERSION}', layout, size=(WINDOWSWIDTH, WINDOWSHEIGHT), font=font, icon=str(pathlib.Path().resolve()) + "\\assets\icon.ico", margins=(10,10), resizable=True, finalize=True)
    move_center(window)
    
    # Get env data
    if os.path.exists("env_data.txt"):
        f = open("env_data.txt", "r")
        last_modified_filename = f.readline()
        f.close()
    else:
        last_modified_filename = ""
    print(f"last modified filename = {last_modified_filename}")

    # Create Row Counter Object
    education_row_counter = RowCounter("EDUCATION", 0, 1)
    sideproject_row_counter = RowCounter("PJ", 0, 1)
    experience_row_counter = RowCounter("EXP", 0, 1)
    skills_row_counter = RowCounter("SKILL", 0, 1)

    # Updata console message
    if console_message:
        print(f"current working directory: {os.getcwd()}")
        LoadData(window, education_row_counter, sideproject_row_counter, experience_row_counter, skills_row_counter, os.getcwd() + "\\" + last_modified_filename + ".txt")
        window["RESPONSE"].update(console_message)

    # Object list
    heading_content = {}
    objective_content = {}
    education_content = {}
    sideproject_content = {}
    experience_content = {}
    skills_content = {}

    # Remove row list
    removed_education_row = RemovedContent()
    removed_sideproject_row = RemovedContent()
    removed_experience_row = RemovedContent()
    removed_skills_row = RemovedContent()

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        
        # Close the window
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            return
        
        # URL event
        if not isinstance(event, tuple):
            if event.startswith("URL "):
                url = event.split(" ")[1]
                webbrowser.open(url)

        # Load Data
        if event == "LOAD_DATA":
            LoadData(window, education_row_counter, 
                     sideproject_row_counter, experience_row_counter, 
                     skills_row_counter, 
                     values["OLD_DATA_PATH"])
            print("COUNTER")
            print(f"Counter : {education_row_counter.row_counter}, # : {education_row_counter.row_number_view}")
        
        # Preview Date
        if isinstance(event, tuple):
            if event[0].endswith("MON"):
                preview_value = window.Element((event[0].replace("_MON", ""), event[1])).Get()
                if len(preview_value.split(" ")) == 1 and preview_value.isnumeric():
                    year = preview_value.split(" ")[0]
                    window.Element((event[0].replace("_MON", ""), event[1])).Update(values[event] + " " + year)
                elif len(preview_value.split(" ")) == 2:
                    year = preview_value.split(" ")[1]
                    window.Element((event[0].replace("_MON", ""), event[1])).Update(values[event] + " " + year)
                else:
                    window.Element((event[0].replace("_MON", ""), event[1])).Update(values[event])
            elif event[0].endswith("YEAR"):
                preview_value = window.Element((event[0].replace("_YEAR", ""), event[1])).Get()
                value = window.Element(event).Get()
                if len(value) > 4 or not value.isnumeric():
                    window.Element(event).Update(value[:-1])
                elif len(preview_value.split(" ")) == 1 and preview_value.isalpha() and not preview_value == "Present":
                    month = preview_value.split(" ")[0]
                    window.Element((event[0].replace("_YEAR", ""), event[1])).Update(month + " " + value)
                elif len(preview_value.split(" ")) == 2:
                    month = preview_value.split(" ")[0]
                    window.Element((event[0].replace("_YEAR", ""), event[1])).Update(month + " " + value)
                # Year input validation, only allow 4 digits and numeric
                else:
                    window.Element((event[0].replace("_YEAR", ""), event[1])).Update(value)
            elif event[0].endswith("PRESENT"):
                window.Element((event[0].replace("_PRESENT", "_END"), event[1])).Update("Present")
                
        
        # Clear all input
        if event == "CLEAN":
            # TODO: reset to 1 row in each of them, also key are now tuple
            print("CLEAN")
            print(education_row_counter.row_counter)
            print(sideproject_row_counter.row_counter)
            for key in KEYS_TO_CLEAR:
                window[key]('')
            for i in range(1, education_row_counter.row_counter + 1):
                window[("-EDUCATION_ROW-", i)].update(visible=False)
            for i in range(1, sideproject_row_counter.row_counter + 1):
                window[("-PJ_ROW-", i)].update(visible=False)
            for i in range(1, experience_row_counter.row_counter + 1):
                window[("-EXP_ROW-", i)].update(visible=False)
            for i in range(1, skills_row_counter.row_counter + 1):
                window[("-SKILLS_ROW-", i)].update(visible=False)

            education_row_counter.row_number_view = 1
            sideproject_row_counter.row_number_view = 1
            experience_row_counter.row_number_view = 1
            skills_row_counter.row_number_view = 1

            # Update Scrollbar
            window.refresh()
            window["-EDUCATION_ROW_PANEL-"].contents_changed()
            window["-PJ_ROW_PANEL-"].contents_changed()
            window["-EXP_ROW_PANEL-"].contents_changed()
            window["-SKILLS_ROW_PANEL-"].contents_changed()

        # Delete Data
        if event == "DELETE_DATA":
            try:
                if os.path.exists(last_modified_filename + ".txt"):
                    os.remove(last_modified_filename + ".txt")
                    print(f"{last_modified_filename}.txt Data deleted")
                if os.path.exists(last_modified_filename + ".docx"):
                    os.remove(last_modified_filename + ".docx")
                    print(f"{last_modified_filename}.docx Data deleted")
                window["RESPONSE"].update("Data deleted")
            except:
                window["RESPONSE"].update("Error: Data not deleted, close the file before delete")
        
        # Add and Remove Row Field
        def RowAdd(field_type:str, row_counter_object:RowCounter, create, removed_content_object:RemovedContent):
            if event == f"-{field_type}_ROW_ADD-":
                row_counter_object.row_counter += 1
                row_counter_object.row_number_view += 1
                row_counter_object.DictAppend(row_counter_object.row_counter, ListCounter(row_counter_object.row_counter, 0))
                window.extend_layout(window[f"-{field_type}_ROW_PANEL-"], [create(row_counter_object.row_counter, row_counter_object.row_number_view)])
                # Update Scrollbar
                window.refresh()
                window[f"-{field_type}_ROW_PANEL-"].contents_changed()
            elif event[0] == f"-{field_type}_ROW_REMOVE-":
                window[(f"-{field_type}_ROW-", event[1])].update(visible=False)
                window.refresh()
                window[f"-{field_type}_ROW_PANEL-"].contents_changed()
                temp_removed_content_object = RemovedContent(event[1])
                temp_removed_content_object.removed_row = True
                removed_content_object.ListAppend(temp_removed_content_object)
                row_counter_object.row_number_view -= 1

        RowAdd("EDUCATION", education_row_counter,
               create_education,
               removed_education_row)
        RowAdd("PJ", sideproject_row_counter,
               create_sideproject,
               removed_sideproject_row)
        RowAdd("EXP", experience_row_counter,
               create_experience,
               removed_experience_row)
        RowAdd("SKILLS", skills_row_counter,
               create_skills,
               removed_skills_row)
        
        # Add Description List
        if isinstance(event, tuple):
            if event[0].endswith("LIST_ADD"):
                type = event[0].replace("_LIST_ADD", "")
                row_counter = event[1]

                def ListAdd(field_type:str, row_counter, row_counter_object:RowCounter):
                    list_counter_object = row_counter_object.description_dict[row_counter]
                    list_counter_object.list_counter += 1
                    window.extend_layout(window[(f"-{field_type}_LIST_PANEL-", row_counter)], [create_list(field_type, row_counter, list_counter_object.list_counter)])
                    # Update Scrollbar
                    window.refresh()
                    window[f"-{field_type}_ROW_PANEL-"].contents_changed()
                    
                # Get List Counter
                match type:
                    case "EDUCATION":
                        ListAdd("EDUCATION", row_counter, education_row_counter)
                    case "PJ":
                        ListAdd("PJ", row_counter, sideproject_row_counter)
                    case "EXP":
                        ListAdd("EXP", row_counter, experience_row_counter)
            elif event[0].endswith("LIST_REMOVE"):
                type = event[0].replace("_LIST_REMOVE", "")

                def ListRemove(field_type:str, row_counter, list_counter, removed_content_object:RemovedContent):
                    window[(f"-{field_type}_LIST-", row_counter, list_counter)].update(visible=False)
                    window.refresh()
                    window[f"-{field_type}_ROW_PANEL-"].contents_changed()
                    # Find if there exist corresponding removed row object
                    if removed_content_object.removed_list:
                        for removed_row in removed_content_object.removed_list:
                            if removed_row.row_counter == row_counter:
                                # Add the removed list counter to corresponding removed row object
                                removed_row.ListAppend(list_counter)
                            else:
                                # Removed Row Object Doesn't Exist -> Creat One
                                temp_removed_content_object = RemovedContent(row_counter)
                                temp_removed_content_object.ListAppend(list_counter)
                                removed_content_object.ListAppend(temp_removed_content_object)
                    else:
                        # Removed List Is Empty
                        temp_removed_content_object = RemovedContent(row_counter)
                        temp_removed_content_object.ListAppend(list_counter)
                        removed_content_object.ListAppend(temp_removed_content_object)
                    # removed_list.append(event[1])
                match type:
                    case "EDUCATION":
                        ListRemove(type, event[1], event[2], removed_education_row)
                    case "PJ":
                        ListRemove(type, event[1], event[2], removed_sideproject_row)
                    case "EXP":
                        ListRemove(type, event[1], event[2], removed_experience_row)

        # Generate
        if event == 'Generate':
            # User Input Validation
            print(f"{values}")
            
            # Remove Old Data to prevent a huge amount of txt and docx files
            txt_file_name = last_modified_filename + ".txt"
            if last_modified_filename == "_resume":
                docx_file_name = "[Your Name]_resume.docx"
            else:
                docx_file_name = last_modified_filename + "docx"

            print(f"txt_file_name = {txt_file_name}")
            print(f"docx_file_name = {docx_file_name}")

            try:
                if os.path.exists(txt_file_name):
                    os.remove(txt_file_name)
                    print(f"{txt_file_name} Data deleted")
                if os.path.exists(docx_file_name ):
                    os.remove(docx_file_name)
                    print(f"{docx_file_name} Data deleted")
                window["RESPONSE"].update("Data deleted")
            except:
                pass
            
            # Values Seperation
            for key, value in values.items():
                heading = ["NAME", "NICKNAME", "TELEPHONE", "EMAIL", "GITHUBLINK", "WEBLINK"]
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

    # Remove Content
    def PopContent(removed_content_object: RemovedContent, content):
        content_copy = content.copy()
        # Get The Panel Removed List
        for row_object in removed_content_object.removed_list:
            # Removed Row is True -> remove whole row
            if row_object.removed_row:
                row = row_object.row_counter
                for key, value in content.items():
                    if key[1] == row:
                        res = content_copy.pop(key,f"KEY[1] {key} NOT FOUND")
            else:
                # Removed Row is False -> check if there exist any list to remove
                for list in row_object.removed_list:
                    for key, value in content.items():
                        if len(key) == 3:
                            if key[2] == list:
                                res = content_copy.pop(key,f"KEY[2] {key} NOT FOUND")
        return content_copy
    
    # def PrintRemovedContent(removed_content:RemovedContent):
    #     print("RESULT OF REMOVED CONTENT")
    #     row_result = "["
    #     print("LIST TO BE REMOVED")
    #     for removed_row in removed_content.removed_list:
    #         row_result += " " + str(removed_row.row_counter) + ","
    #         print(f"ROW {removed_row.row_counter} " + str(removed_row.removed_list))
    #     row_result += "]"
    #     print("ROW TO BE REMOVED")
    #     print(row_result)

    # PrintRemovedContent(removed_education_row)

    # Remove the removed content in the dictionary
    education_content = PopContent(removed_education_row, education_content).copy()
    sideproject_content = PopContent(removed_sideproject_row, sideproject_content).copy()
    experience_content = PopContent(removed_experience_row, experience_content).copy()
    skills_content = PopContent(removed_skills_row, skills_content).copy()

    # Reset the key to start from 1
    reseted_education_content = ResetKey(education_content, EDUCATIONFIELD)
    reseted_sideproject_content = ResetKey(sideproject_content, SIDEPROJECTFIELD)
    reseted_experience_content = ResetKey(experience_content, EXPERIENCEFIELD)
    reseted_skills_content = ResetKey(skills_content, SKILLSFIELD)

    # Get the reseted ket index content
    education_content =  reseted_education_content[0].copy()
    sideproject_content = reseted_sideproject_content[0].copy()
    experience_content = reseted_experience_content[0].copy()
    skills_content = reseted_skills_content[0].copy()

    # Get the count number of each field
    education_content_counter = reseted_education_content[1]
    sideproject_content_counter = reseted_sideproject_content[1]
    experience_content_counter = reseted_experience_content[1]

    # Get the Description List Count
    education_list_counter = reseted_education_content[2]
    sideproject_list_counter = reseted_sideproject_content[2]
    experience_list_counter = reseted_experience_content[2]

    # print("CHECKING AFTER RESET KEY")
    # print(heading_content)
    # print(objective_content)
    # print(education_content)
    # print(sideproject_content)
    # print(experience_content)
    # print(skills_content)

    # Only Retrieve the values, not include the key
    def RetrieveValue(content:dict):
        massaged_content = []
        for key, value in content.items():
            massaged_content.append(value)
        return massaged_content
    
    massaged_heading_content = RetrieveValue(heading_content)
    massaged_objective_content = RetrieveValue(objective_content)
    massaged_skills_content = RetrieveValue(skills_content)

    #save resume data
    try:
        file_name = values["NAME"] + "_resume"
        f = open(file_name + ".txt", "w")
        f.write("Formal Resume Generator 2023\n")
        f.write(f"{education_row_counter.row_number_view}, {sideproject_row_counter.row_number_view}, {experience_row_counter.row_number_view}, {skills_row_counter.row_number_view}\n")
        f.write(f"{education_list_counter}\n")
        f.write(f"{sideproject_list_counter}\n")
        f.write(f"{experience_list_counter}\n")
        f.write(str(heading_content) + "\n")
        f.write(str(objective_content) + "\n")
        f.write(str(education_content) + "\n")
        f.write(str(sideproject_content) + "\n")
        f.write(str(experience_content) + "\n")
        f.write(str(skills_content) + "\n")
        f.close()
    except:
        print("Error: Can't Save the data file, please close it and try again.")

    #save last modified meta data, use to delete old data
    f = open("env_data.txt", "w")
    f.write(file_name)
    f.close()

    window.close()
    return [create_heading_object(massaged_heading_content), 
            create_objective_object(massaged_objective_content), 
            create_object(education_content, education_content_counter), 
            create_object(sideproject_content, sideproject_content_counter), 
            create_object(experience_content, experience_content_counter), 
            create_skill_object(massaged_skills_content)]

if __name__ == "__main__":
    gui()
