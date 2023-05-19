from src.expend_layout import *

KEY = "Formal Resume Generator 2023\n"

def LoadData(window, education_row_counter, sideproject_row_counter, experience_row_counter, skills_row_counter, data_path:str) -> None:
    # Open the file
    try:
        f = open(data_path, "r")
    except:
        print(f"Error: Unable to open file in {data_path}")
        return
    lines = f.readlines()
    f.close()
    
    # Check if the key is correct
    if lines[0] == KEY:
        print("Key is correct")
    else:
        print("Key is incorrect")
        f.close()
        return
    
    # Get the count of rows
    count = lines[1].split(",")
    education_count = int(count[0]) - 1
    side_projects_count = int(count[1]) - 1
    experience_count = int(count[2]) - 1
    skills_count = int(count[3]) - 1

    # Get the count of list description
    education_list_count = lines[2].strip('][\n').split(', ')
    side_projects_list_count = lines[3].strip('][\n').split(', ')
    experience_list_count = lines[4].strip('][\n').split(', ')
    
    # Extend the row and list layout
    # Since the following expend layout is not going to affect row 0, 
    # hence in order to expand the list in row 0, we need another way to expand it
    for i in range(1, education_count + 1):
        window.extend_layout(window["-EDUCATION_ROW_PANEL-"], [create_education(i, i+1)])
        for index, list_count in enumerate(education_list_count):
            if index == i:
                for j in range(1, int(list_count)):
                    window.extend_layout(window[(f"-EDUCATION_LIST_PANEL-", index)], [create_list("EDUCATION", i, j)])
    for i in range(1, side_projects_count + 1):
        window.extend_layout(window["-PJ_ROW_PANEL-"], [create_sideproject(i, i+1)])
        for index, list_count in enumerate(side_projects_list_count):
            if index == i:
                for j in range(1, int(list_count)):
                    window.extend_layout(window[(f"-PJ_LIST_PANEL-", index)], [create_list("PJ", i, j)])
    for i in range(1, experience_count + 1):
        window.extend_layout(window["-EXP_ROW_PANEL-"], [create_experience(i, i+1)])
        for index, list_count in enumerate(experience_list_count):
            if index == i:
                for j in range(1, int(list_count)):
                    window.extend_layout(window[(f"-EXP_LIST_PANEL-", index)], [create_list("EXP", i, j)])
    for i in range(1, skills_count + 1):
        window.extend_layout(window["-SKILLS_ROW_PANEL-"], [create_skills(i, i+1)])

    # Expending the list description in row 0
    for j in range(1, int(education_list_count[0])):
        window.extend_layout(window[("-EDUCATION_LIST_PANEL-", 0)], [create_list("EDUCATION", 0, j)])
    for j in range(1, int(side_projects_list_count[0])):
        window.extend_layout(window[("-PJ_LIST_PANEL-", 0)], [create_list("PJ", 0, j)])
    for j in range(1, int(experience_list_count[0])):
        window.extend_layout(window[("-EXP_LIST_PANEL-", 0)], [create_list("EXP", 0, j)])

    # Update row counter
    education_row_counter.row_counter = education_count
    education_row_counter.row_number_view = education_count + 1
    sideproject_row_counter.row_counter = side_projects_count
    sideproject_row_counter.row_number_view = side_projects_count + 1
    experience_row_counter.row_counter = experience_count
    experience_row_counter.row_number_view = experience_count + 1
    skills_row_counter.row_counter = skills_count
    skills_row_counter.row_number_view = skills_count + 1

    # refresh the window
    window.refresh()
    window["-EDUCATION_ROW_PANEL-"].contents_changed()
    window["-PJ_ROW_PANEL-"].contents_changed()
    window["-EXP_ROW_PANEL-"].contents_changed()
    window["-SKILLS_ROW_PANEL-"].contents_changed()

    # Turn Dictionary String to Dictionary -> data
    heading_content = eval(lines[5].replace("'", "\"").strip())
    objective_content = eval(lines[6].replace("'", "\"").strip())
    education_content = eval(lines[7].replace("'", "\"").strip())
    sideproject_content = eval(lines[8].replace("'", "\"").strip())
    experience_content = eval(lines[9].replace("'", "\"").strip())
    skills_content = eval(lines[10].replace("'", "\"").strip())

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

    