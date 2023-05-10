import PySimpleGUI as sg
import src.data
import pathlib
import webbrowser

WINDOWSHEIGHT = 800
WINDOWSWIDTH = 1200
VERSION = "1.0"

# add button which can expand another objective input field
def add_objective() -> None:
    pass

def gui() -> dict:
    print(f"path = {pathlib.Path().resolve()}" + "\src\icon.png")
    # Add a touch of color
    sg.theme('DarkAmber')   
    font = ("Arial", 11)
    
    menu_layout = [['File', ['Open', 'Save', 'Exit', 'Properties']],
                ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
                ['Help', 'About...'], ]

    instruction_layout = [[sg.Text('Instruction', font='Arial 14 bold')],
                            [sg.Text("This is a Formal Resume Generator, for more infomation, please refer to"),
                             sg.Text("resume-generator", tooltip="https://github.com/Argonaut790/resume-generator.git", enable_events=True, key="URL https://github.com/Argonaut790/resume-generator.git", text_color="skyblue")],
                            [sg.Text("**Disclaimer** All The Information Won't Be Stored", text_color="red", font = ("Arial", 9))] ]

    browse_old_data_layout = [[sg.Text('Browse Old Data', font='Arial 14 bold')],
                            [sg.Text("Please select the old data file", size=(40,1)), sg.InputText(key="OLD_DATA", size=(50,1)), sg.FileBrowse(),
                            sg.Button('Load', size=(8,1))]]
    
    heading_layout = [  [sg.Text('Heading', font='Arial 14 bold')],
                [sg.Text('Name', size=(8,1)), sg.InputText(key="NAME", size=(25,1), ), sg.Text('Nickname', size=(8,1)), sg.InputText(key="NICKNAME", size=(25,1))],
                [sg.Text('Telephone', size=(8,1)), sg.InputText(key="TELEPHONE", size=(25,1)), sg.Text('Email', size=(8,1)), sg.InputText(key="EMAIL", size=(25,1))],
                [sg.Text('Github Link', size=(8,1)), sg.InputText(key="GITHUBLINK", size=(25,1)), sg.Text('Web Link', size=(8,1)), sg.InputText(key="WEBLINK", size=(25,1))],
                 ]
                      
    objective_layout = [[sg.Text('Objective', font='Arial 14 bold')],
                [sg.Text('Objective', size=(8,1)), sg.Multiline(key="OBJECTIVE", size=(60,3))] ]

    education_layout = [[sg.Text('Education', font='Arial 14 bold')],
                [sg.Text('School Name', size=(8,1)), sg.InputText(key="EDUCATION_NAME", size=(25,1)), sg.Text('Degree', size=(8,1)), sg.InputText(key="EDUCATION_DEGREE", size=(25,1))],
                [sg.Text('Duration', size=(8,1)), sg.InputText(key="EDUCATION_DURATION", size=(25,1))],
                [sg.Text('Description', size=(8,1)), sg.Multiline(key="EDUCATION_LIST", size=(60,3))],
                [sg.Button('Add', size=(8,1))]]

    sideproject_layout = [[sg.Text('Side Project', font='Arial 14 bold')],
                [sg.Text('Name', size=(8,1)), sg.InputText(key="PJ01_NAME", size=(25,1)), sg.Text('Duration', size=(8,1)), sg.InputText(key="PJ01_DURATION", size=(25,1))],
                [sg.Text('Description', size=(8,1)), sg.Multiline(key="PJ01_LIST", size=(60,3))],
                [sg.Button('Add', size=(8,1))]]
    
    experience_layout = [[sg.Text('Experience', font='Arial 14 bold')],
                [sg.Text('Name', size=(8,1)), sg.InputText(key="EXP_NAME", size=(25,1)), sg.Text('Duration', size=(8,1)), sg.InputText(key="EXP01_DURATION", size=(25,1))],
                [sg.Text('Description', size=(8,1)), sg.Multiline(key="EXP01_LIST", size=(60,3))],
                [sg.Text('Subtitle', size=(8,1)), sg.InputText(key="EXP01_SUBTITLE", size=(25,1))],
                [sg.Button('Add', size=(8,1))]]

    skills_layout = [[sg.Text('Skills', font='Arial 14 bold')],
                [sg.Text('Category', size=(8,1)), sg.InputText(key="SKILL01_CATEGORY", size=(25,1))],
                [sg.Text('List', size=(8,1)), sg.Multiline(key="SKILL01_LIST", size=(60,3))],
                [sg.Button('Add', size=(8,1))]]

    # All the stuff inside your window.
    layout = [ [sg.Menu(menu_layout, background_color='white', tearoff=False, text_color='black') ],
                instruction_layout,
                browse_old_data_layout,
                [sg.Column(heading_layout),
                sg.Column(objective_layout)],
                [sg.Column(education_layout),
                sg.Column(sideproject_layout)],
                [sg.Column(experience_layout),
                sg.Column(skills_layout)],
              [sg.Button('Generate', size=(8,1)), sg.Button('Cancel')]]

    # Create the Window
    window = sg.Window(f'Formal Resume Generator v{VERSION}', layout, size=(WINDOWSWIDTH, WINDOWSHEIGHT), font=font, icon=str(pathlib.Path().resolve()) + "\src\icon.ico", margins=(5,5))

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        elif event.startswith("URL "):
            url = event.split(" ")[1]
            webbrowser.open(url)
        elif event == "OLD_DATA":
            OLD_DATA = values["OLD_DATA"]
            print(OLD_DATA)
        elif event == 'Generate':
            break

    window.close()
    return values

# if __name__ == "__main__":
#     gui()