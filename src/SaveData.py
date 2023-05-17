# rest key index in dictionary
def ResetKey(content:dict, InputNumber:int) -> dict:
    
    count = 0
    for key, value in content.items():
        if len(key) == 2:
            count += 1
    print(f"count = {count}, InputNumber = {InputNumber}")
    # Check if the content is in correct format
    # Input Number - 1 since the description list's key length is not 2  
    if not count % (InputNumber-1):
        # Since the for loop is dynamically changing, hence we need another dict to store the reseted key index
        reseted_key_index_dict = {}
        previous_key_index = 0
        current_key_index = 0
        index = 0
        for key, value in content.items():
            current_key_index = key[1]
            if not current_key_index == previous_key_index:
                index += 1 
            if len(key) == 2:
                reseted_key_index_dict[key[0], index] = value
            elif len(key) == 3:
                reseted_key_index_dict[key[0], index, key[2]] = value
            previous_key_index = current_key_index
        # Reassign to the original dict
        print("RESETTED KEY")
        print(reseted_key_index_dict)
        return reseted_key_index_dict
    else:
        print("Error: Content data is not in correct format")
    
    return {}

def SaveData() -> None:
    pass