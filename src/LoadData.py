KEY = "Formal Resume Generator 2023\n"

def LoadData(document, data_path:str) -> None:
    try:
        f = open(data_path, "r")
    except:
        print(f"Error: Unable to open file in {data_path}")
        return
    lines = f.readlines()
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

    # Turn Dictionary String to Dictionary -> data
    res = eval(lines[2].replace("'", "\""))
    print("res = ", res)
    f.close()

    # Update data
    for key, value in res.items():
        document[key].update(value)