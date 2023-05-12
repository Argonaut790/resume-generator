import PySimpleGUI as sg

# Content size
FIRSTTEXTWIDTH = 10
SECONDTEXTWIDTH = 6
INPUTWIDTH = 25
FULLWIDTH = INPUTWIDTH * 2 + SECONDTEXTWIDTH + 2

# Button size
REMOVEBUTTONWIDTH = 8
BUTTONHEIGHT = 1

# add button which can expand another objective input field
def create_education(row_counter, row_number_view) -> list:
    row = [sg.pin(
        sg.Column([[sg.Text(f"#{row_number_view}, counter {row_counter}", font='Arial 11 bold'), sg.Button('Remove', size=(REMOVEBUTTONWIDTH,BUTTONHEIGHT), enable_events=True, key=("-EDUCATION_ROW_REMOVE-", row_counter), tooltip="Delete Last Education Field")],
                [sg.Text('School Name', size=(FIRSTTEXTWIDTH,1)), sg.InputText(key=("EDUCATION_NAME", row_counter), size=(INPUTWIDTH,1)), sg.Text('Degree', size=(SECONDTEXTWIDTH,1)), sg.InputText(key=("EDUCATION_DEGREE", row_counter), size=(INPUTWIDTH,1))],
                [sg.Text('Duration', size=(FIRSTTEXTWIDTH,1)), sg.InputText(key=("EDUCATION_DURATION", row_counter), size=(INPUTWIDTH,1))],
                [sg.Text('Description', size=(FIRSTTEXTWIDTH,1)), sg.Multiline(key=("EDUCATION_LIST", row_counter), size=(FULLWIDTH,3))]],
                key=("-EDUCATION_ROW-", row_counter)
        ))]
    return row

def create_sideproject(row_counter, row_number_view) -> list:
    row = [sg.pin(
        sg.Column([[sg.Text(f"# {row_number_view}", font='Arial 11 bold'), sg.Button('Remove', size=(REMOVEBUTTONWIDTH,BUTTONHEIGHT), enable_events=True, key=("-SIDEPROJECT_ROW_REMOVE-", row_counter), tooltip="Delete Last Side Project Field")],
             [sg.Text('Name', size=(FIRSTTEXTWIDTH,1)), sg.InputText(key=("PJ_NAME", row_counter), size=(INPUTWIDTH,1)), sg.Text('Duration', size=(SECONDTEXTWIDTH,1)), sg.InputText(key=("PJ_DURATION", row_counter), size=(INPUTWIDTH,1))],
             [sg.Text('Description', size=(FIRSTTEXTWIDTH,1)), sg.Multiline(key=("PJ_LIST", row_counter), size=(FULLWIDTH,3))]],
             key=("-SIDEPROJECT_ROW-", row_counter)
        ))]
    return row

def create_experience(row_counter, row_number_view) -> list:
    row = [sg.pin(
        sg.Column([[sg.Text(f"# {row_number_view}", font='Arial 11 bold'), sg.Button('Remove', size=(REMOVEBUTTONWIDTH,BUTTONHEIGHT), enable_events=True, key=("-EXPERIENCE_ROW_REMOVE-", row_counter), tooltip="Delete Last Experience Field")],
                [sg.Text('Name', size=(8,1)), sg.InputText(key=("EXP_NAME", row_counter), size=(25,1)), sg.Text('Duration', size=(8,1)), sg.InputText(key=("EXP_DURATION", row_counter), size=(25,1))],
                [sg.Text('Subtitle', size=(8,1)), sg.InputText(key=("EXP_SUBTITLE", row_counter), size=(25,1))],
                [sg.Text('Description', size=(8,1)), sg.Multiline(key=("EXP_LIST", row_counter), size=(60,3))]],
                key=("-EXPERIENCE_ROW-", row_counter)
            ))]
    return row

def create_skills(row_counter, row_number_view) -> list:
    row = [sg.pin(
        sg.Column([[sg.Text(f"# {row_number_view}", font='Arial 11 bold'), sg.Button('Remove', size=(REMOVEBUTTONWIDTH,BUTTONHEIGHT), enable_events=True, key=("-SKILLS_ROW_REMOVE-", row_counter), tooltip="Delete Last Skills Field")],
                [sg.Text('Category', size=(8,1)), sg.InputText(key=("SKILL_CATEGORY", row_counter), size=(25,1))],
                [sg.Text('List', size=(8,1)), sg.Multiline(key=("SKILL_LIST", row_counter), size=(60,3))]],
                key=("-SKILLS_ROW-", row_counter)
            ))]
    return row