# rest key index in dictionary
def ResetKey(content:dict, InputNumber:int) -> dict:

    if not len(content) % InputNumber:
        i = 0
        count = 0
        # Since the for loop is dynamic changing, hence we need another dict to store the reseted key index
        reseted_key_index_dict = {}
        for key, value in content.items():
            if count == InputNumber:
                i += 1
                count = 0
            if key[1] != i:
                new_key = list(key)
                new_key[1] = i
                reseted_key_index_dict[tuple(new_key)] = value
            else:
                reseted_key_index_dict[key] = value
            count += 1
        # Reassign to the original dict
        return reseted_key_index_dict
    else:
        print("Error: Content data is not in correct format")
    
    return {}

def SaveData() -> None:
    pass