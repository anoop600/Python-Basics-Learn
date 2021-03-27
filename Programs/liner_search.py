def linear_search(item_list, key):
    for index in range(len(item_list)):
        if item_list[index] == key:
            #Return index if the search key is present
            return index
    #Worst Case, Key not found
    return -1


num_list = [-2, 6,2,9,100,75,-10]

print(linear_search(num_list, -10))