import PySimpleGUI as sg
import src.gui_metadata as data

def duration(type:str, row_counter) -> list:
    return [[sg.Text('Start Date', size=(data.STARTWIDTH,1)),
             sg.Text('Month', size=(data.MONTHWIDTH,1)),
               sg.DD(data.MONTHS, size=(data.DDWIDTH,1), default_value=data.MONTHS[0], key=(f"{type}_START_MON", row_counter), enable_events=True),
                 sg.Text('Year', size=(data.YEARWIDTH,1)),
                   sg.InputText(key=(f"{type}_START_YEAR", row_counter), size=(data.YEARINPUTWIDTH,1), enable_events=True),
            sg.Text('End Date', size=(data.ENDWIDTH,1)),
             sg.Text('Month', size=(data.MONTHWIDTH,1)),
               sg.DD(data.MONTHS, size=(data.DDWIDTH,1), default_value=data.MONTHS[0], key=(f"{type}_END_MON", row_counter), enable_events=True),
                 sg.Text('Year', size=(data.YEARWIDTH,1)),
                   sg.InputText(key=(f"{type}_END_YEAR", row_counter), size=(data.YEARINPUTWIDTH,1), enable_events=True)],
            # Preview of start and end date
            [sg.Text("", size=(data.STARTWIDTH)),
             sg.Text('START', size=(data.MONTHWIDTH + data.DDWIDTH + 2,1)),
             sg.InputText(key=(f"{type}_START", row_counter), size=(data.YEARWIDTH + data.YEARINPUTWIDTH + 3,1), default_text="Jan 2023", use_readonly_for_disable=True, disabled=True, disabled_readonly_background_color=sg.theme_background_color(), disabled_readonly_text_color=sg.theme_text_color()),
             sg.Text('END', size=(data.ENDWIDTH,1)),
             sg.InputText(key=(f"{type}_END", row_counter), size=(data.YEARWIDTH + data.YEARINPUTWIDTH + 3,1), default_text="Jan 2023", use_readonly_for_disable=True, disabled=True, disabled_readonly_background_color=sg.theme_background_color(), disabled_readonly_text_color=sg.theme_text_color()),
             sg.Button("Present", size=(data.YEARWIDTH + data.YEARINPUTWIDTH + 1,1), key=(f"{type}_PRESENT", row_counter), enable_events=True, tooltip="Till Present"),]]

def create_list(type:str, row_counter, list_counter):
    list = [sg.pin(
        sg.Column(
                [[ sg.Text(f"List", font='Arial 11 bold', size=(data.FIRSTTEXTWIDTH,1)),
                 sg.InputText(key=(f"{type}_LIST", row_counter, list_counter), size=(data.DESCRIPTIONWIDTH,1)), 
                 sg.Button('Remove', size=(data.DESCRIPTIONREMOVEBUTTONWIDTH,1), enable_events=True, key=(f"{type}_LIST_REMOVE", row_counter, list_counter), tooltip="Remove Description", pad=(1,0))]],
                key=(f"-{type}_LIST-", row_counter, list_counter),
                pad=(0,8)
        ))]
    return list

def description_layout(type:str, row_counter) -> list:
    return [[sg.Text('Description', size=(data.FIRSTTEXTWIDTH,1))],
             [sg.Column([create_list(type, row_counter, 0)],
                        key=(f"-{type}_LIST_PANEL-", row_counter,),
                        pad=(0,0))],
            [sg.Button('Add List', size=(data.ADDBUTTONWIDTH,1), enable_events=True, key=(f"{type}_LIST_ADD", row_counter), tooltip="Add Description")]]

# add button which can expand another objective input field
def create_education(row_counter, row_number_view) -> list:
    row = [sg.pin(
        sg.Column([[sg.Text(f"#{row_number_view}", font='Arial 11 bold'), sg.Button('Remove', size=(data.REMOVEBUTTONWIDTH,data.BUTTONHEIGHT), enable_events=True, key=("-EDUCATION_ROW_REMOVE-", row_counter), tooltip="Delete Education Field")],
                [sg.Text('School Name', size=(data.FIRSTTEXTWIDTH,1)), sg.InputText(key=("EDUCATION_NAME", row_counter), size=(data.INPUTWIDTH,1)), sg.Text('Degree', size=(data.SECONDTEXTWIDTH,1)), sg.InputText(key=("EDUCATION_DEGREE", row_counter), size=(data.INPUTWIDTH,1))],
                [sg.Column(duration("EDUCATION", row_counter), pad=(0,0))],
                [sg.Column(description_layout("EDUCATION", row_counter), pad=(0,0))]],
                key=("-EDUCATION_ROW-", row_counter),
                pad=(0,8)
        ))]
    return row

def create_sideproject(row_counter, row_number_view) -> list:
    row = [sg.pin(
        sg.Column([[sg.Text(f"# {row_number_view}", font='Arial 11 bold'), sg.Button('Remove', size=(data.REMOVEBUTTONWIDTH,data.BUTTONHEIGHT), enable_events=True, key=("-PJ_ROW_REMOVE-", row_counter), tooltip="Delete Side Project Field")],
             [sg.Text('Title', size=(data.FIRSTTEXTWIDTH,1)), sg.InputText(key=("PJ_NAME", row_counter), size=(data.FULLWIDTH+2,1))],
            [sg.Column(duration("PJ", row_counter), pad=(0,0))],
            [sg.Column(description_layout("PJ", row_counter), pad=(0,0))]],
            key=("-PJ_ROW-", row_counter),
            pad=(0,8)
        ))]
    return row

def create_experience(row_counter, row_number_view) -> list:
    row = [sg.pin(
        sg.Column([[sg.Text(f"# {row_number_view}", font='Arial 11 bold'), sg.Button('Remove', size=(data.REMOVEBUTTONWIDTH,data.BUTTONHEIGHT), enable_events=True, key=("-EXP_ROW_REMOVE-", row_counter), tooltip="Delete Experience Field")],
                [sg.Text('Title', size=(data.FIRSTTEXTWIDTH,1)), sg.InputText(key=("EXP_NAME", row_counter), size=(data.INPUTWIDTH,1)), sg.Text('Subtitle', size=(data.SECONDTEXTWIDTH,1)), sg.InputText(key=("EXP_SUBTITLE", row_counter), size=(data.INPUTWIDTH,1))],
                [sg.Column(duration("EXP", row_counter), pad=(0,0))],
                [sg.Column(description_layout("EXP", row_counter), pad=(0,0))]],
                key=("-EXP_ROW-", row_counter),
                pad=(0,8)
            ))]
    return row

def create_skills(row_counter, row_number_view) -> list:
    row = [sg.pin(
        sg.Column([[sg.Text(f"# {row_number_view}", font='Arial 11 bold'), sg.Button('Remove', size=(data.REMOVEBUTTONWIDTH,data.BUTTONHEIGHT), enable_events=True, key=("-SKILLS_ROW_REMOVE-", row_counter), tooltip="Delete Skills Field")],
                [sg.Text('Category', size=(data.FIRSTTEXTWIDTH,1)), sg.InputText(key=("SKILL_CATEGORY", row_counter), size=(data.INPUTWIDTH,1))],
                [sg.Text('List', size=(data.FIRSTTEXTWIDTH,1)), sg.InputText(key=("SKILL_LIST", row_counter), size=(data.FULLWIDTH+2,1))]],
                key=("-SKILLS_ROW-", row_counter),
                pad=(0,8)
            ))]
    return row