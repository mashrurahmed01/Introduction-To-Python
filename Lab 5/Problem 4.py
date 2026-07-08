def linear_search(lst, target):
    for index in range(len(lst)):
        if lst[index] == target:
            return index
    return -1

search_list = [15, 25, 35, 45, 55]
print(linear_search(search_list, 35))