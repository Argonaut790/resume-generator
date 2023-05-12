from src.expend_layout import *
KEY = "Formal Resume Generator 2023\n"

def LoadData(window, row_counter, data_path:str) -> None:
    try:
        f = open(data_path, "r")
    except:
        print(f"Error: Unable to open file in {data_path}")
        return
    lines = f.readlines()
    f.close()
    print("lines = ", lines[1])
    if lines[0] == KEY:
        print("Key is correct")
    else:
        print("Key is incorrect")
        f.close()
        return
    # Get the count of rows
    count = lines[1].split(",")
    education_count = int(count[0])
    side_projects_count = int(count[1])
    experience_count = int(count[2])
    skills_count = int(count[3])
    
    # Extend the layout
    for i in range(1, education_count):
        window.extend_layout(window["-EDUCATION_ROW_PANEL-"], [create_education(i, i+1)])
    for i in range(1, side_projects_count):
        window.extend_layout(window["-SIDEPROJECT_ROW_PANEL-"], [create_sideproject(i, i+1)])
    for i in range(1, experience_count):
        window.extend_layout(window["-EXPERIENCE_ROW_PANEL-"], [create_experience(i, i+1)])
    for i in range(1, skills_count):
        window.extend_layout(window["-SKILLS_ROW_PANEL-"], [create_skills(i, i+1)])

    # Update row counter
    row_counter.education_row_counter = education_count
    row_counter.education_row_number_view = education_count + 1
    row_counter.sideproject_row_counter = side_projects_count
    row_counter.sideproject_row_number_view = side_projects_count + 1
    row_counter.experience_row_counter = experience_count
    row_counter.experience_row_number_view = experience_count + 1
    row_counter.skills_row_counter = skills_count
    row_counter.skills_row_number_view = skills_count + 1

    # refresh the window
    window.refresh()
    window["-EDUCATION_ROW_PANEL-"].contents_changed()
    window["-SIDEPROJECT_ROW_PANEL-"].contents_changed()
    window["-EXPERIENCE_ROW_PANEL-"].contents_changed()
    window["-SKILLS_ROW_PANEL-"].contents_changed()

    # Turn Dictionary String to Dictionary -> data
    heading_content = eval(lines[2].replace("'", "\"").strip())
    objective_content = eval(lines[3].replace("'", "\"").strip())
    education_content = eval(lines[4].replace("'", "\"").strip())
    sideproject_content = eval(lines[5].replace("'", "\"").strip())
    experience_content = eval(lines[6].replace("'", "\"").strip())
    skills_content = eval(lines[7].replace("'", "\"").strip())

    # print data
    print("heading_content = ", heading_content)
    print("objective_content = ", objective_content)
    print("education_content = ", education_content)
    print("sideproject_content = ", sideproject_content)
    print("experience_content = ", experience_content)
    print("skills_content = ", skills_content)

    # Update data
    for key, value in heading_content.items():
        window[key].update(value)
    for key, value in objective_content.items():
        window[key].update(value)
    for key, value in education_content.items():
        window[key].update(value)
    for key, value in sideproject_content.items():
        window[key].update(value)
    for key, value in experience_content.items():
        window[key].update(value)
    for key, value in skills_content.items():
        window[key].update(value)

    