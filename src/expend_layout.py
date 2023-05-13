import PySimpleGUI as sg
import src.gui_metadata as data
def duration(type:str, row_counter) -> list:
    return [sg.Text('Start Date', size=(data.STARTWIDTH,1)),
             sg.Text('Month', size=(data.MONTHWIDTH,1)),
               sg.DD(data.MONTHS, size=(data.DDWIDTH,1), default_value=data.MONTHS[0], key=(f"{type}_START_MON", row_counter)),
                 sg.Text('Year', size=(data.YEARWIDTH,1)),
                   sg.InputText(key=(f"{type}_START_YEAR", row_counter), size=(data.YEARINPUTWIDTH,1), enable_events=True),
            sg.Text('End Date', size=(data.ENDWIDTH,1)),
             sg.Text('Month', size=(data.MONTHWIDTH,1)),
               sg.DD(data.MONTHS, size=(data.DDWIDTH,1), default_value=data.MONTHS[0], key=(f"{type}_END_MON", row_counter)),
                 sg.Text('Year', size=(data.YEARWIDTH,1)),
                   sg.InputText(key=(f"{type}_END_YEAR", row_counter), size=(data.YEARINPUTWIDTH,1), enable_events=True)]

def description(type:str, row_counter) -> list:
    return [sg.Text('Description', size=(data.FIRSTTEXTWIDTH,1)),
             sg.Multiline(key=(f"{type}_LIST", row_counter), size=(data.FULLWIDTH,3))]

# add button which can expand another objective input field
def create_education(row_counter, row_number_view) -> list:
    row = [sg.pin(
        sg.Column([[sg.Text(f"#{row_number_view}, counter {row_counter}", font='Arial 11 bold'), sg.Button('Remove', size=(data.REMOVEBUTTONWIDTH,data.BUTTONHEIGHT), enable_events=True, key=("-EDUCATION_ROW_REMOVE-", row_counter), tooltip="Delete Education Field")],
                [sg.Text('School Name', size=(data.FIRSTTEXTWIDTH,1)), sg.InputText(key=("EDUCATION_NAME", row_counter), size=(data.INPUTWIDTH,1)), sg.Text('Degree', size=(data.SECONDTEXTWIDTH,1)), sg.InputText(key=("EDUCATION_DEGREE", row_counter), size=(data.INPUTWIDTH,1))],
                duration("EDUCATION", row_counter),
                description("EDUCATION", row_counter)],
                key=("-EDUCATION_ROW-", row_counter)
        ))]
    return row

def create_sideproject(row_counter, row_number_view) -> list:
    row = [sg.pin(
        sg.Column([[sg.Text(f"# {row_number_view}", font='Arial 11 bold'), sg.Button('Remove', size=(data.REMOVEBUTTONWIDTH,data.BUTTONHEIGHT), enable_events=True, key=("-SIDEPROJECT_ROW_REMOVE-", row_counter), tooltip="Delete Side Project Field")],
             [sg.Text('Title', size=(data.FIRSTTEXTWIDTH,1)), sg.InputText(key=("PJ_NAME", row_counter), size=(data.FULLWIDTH+2,1))],
             duration("PJ", row_counter),
            description("PJ", row_counter)],
             key=("-SIDEPROJECT_ROW-", row_counter)
        ))]
    return row

def create_experience(row_counter, row_number_view) -> list:
    row = [sg.pin(
        sg.Column([[sg.Text(f"# {row_number_view}", font='Arial 11 bold'), sg.Button('Remove', size=(data.REMOVEBUTTONWIDTH,data.BUTTONHEIGHT), enable_events=True, key=("-EXPERIENCE_ROW_REMOVE-", row_counter), tooltip="Delete Experience Field")],
                [sg.Text('Name', size=(data.FIRSTTEXTWIDTH,1)), sg.InputText(key=("EXP_NAME", row_counter), size=(data.INPUTWIDTH,1)), sg.Text('Subtitle', size=(data.SECONDTEXTWIDTH,1)), sg.InputText(key=("EXP_SUBTITLE", row_counter), size=(data.INPUTWIDTH,1))],
                duration("EXP", row_counter),
                description("EXP", row_counter)],
                key=("-EXPERIENCE_ROW-", row_counter)
            ))]
    return row

def create_skills(row_counter, row_number_view) -> list:
    row = [sg.pin(
        sg.Column([[sg.Text(f"# {row_number_view}", font='Arial 11 bold'), sg.Button('Remove', size=(data.REMOVEBUTTONWIDTH,data.BUTTONHEIGHT), enable_events=True, key=("-SKILLS_ROW_REMOVE-", row_counter), tooltip="Delete Skills Field")],
                [sg.Text('Category', size=(data.FIRSTTEXTWIDTH,1)), sg.InputText(key=("SKILL_CATEGORY", row_counter), size=(data.INPUTWIDTH,1))],
                [sg.Text('List', size=(data.FIRSTTEXTWIDTH,1)), sg.InputText(key=("SKILL_LIST", row_counter), size=(data.FULLWIDTH+2,1))]],
                key=("-SKILLS_ROW-", row_counter)
            ))]
    return row