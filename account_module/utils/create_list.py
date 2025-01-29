def group_list(custom_list, size=4):
    list_group = []
    for item in range(0, len(custom_list), size):
        list_group.append(custom_list[item:item+size])
    return list_group
