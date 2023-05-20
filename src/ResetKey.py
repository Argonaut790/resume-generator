# rest key index in dictionary
def ResetKey(content:dict, InputNumber:int) -> dict:
    # Sort the content dict by key index [1]
    content = dict(sorted(content.items(), key=lambda key: key[0][1]))
    count = 0
    for key, value in content.items():
        if len(key) == 2:
            count += 1
    # Check if the content is in correct format
    # Input Number - 1 since the description list's key length is not 2  
    if not count % (InputNumber-1):
        # Since the for loop is dynamically changing, hence we need another dict to store the reseted key index
        reseted_key_index_dict = {}
        previous_key_index = 0
        current_key_index = 0
        index = 0
        list_index = 0
        list_count_list = []
        count = 0
        for key, value in content.items():
            count += 1
            current_key_index = key[1]
            if not current_key_index == previous_key_index:
                # Since Current is already the next key
                index += 1 
                list_count_list.append(list_index)
                list_index = 0
            elif count == len(content):
                # append the list index of the last key, this key is not the next key, hence need add one for list_index
                list_count_list.append(list_index + 1)
            if len(key) == 2:
                reseted_key_index_dict[key[0], index] = value
            elif len(key) == 3:
                reseted_key_index_dict[key[0], index, list_index] = value
                list_index += 1
            previous_key_index = current_key_index
        # Reassign to the original dict
        maximum_count = count // (InputNumber-1)
        return reseted_key_index_dict, maximum_count, list_count_list
    else:
        print("Error: Content data is not in correct format")
    
    return {}