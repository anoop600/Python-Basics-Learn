def binary_search(items, left, right, key):
    #Base Case
    if right < left:
        #Item not found
        return -1
    
    mid = (left + right) // 2

    #print("MID = {}".format(mid))

    if items[mid] == key:
        return mid

    elif key < items[mid]:
        print("Checking item in the left")
        return binary_search(items, left, mid-1, key)
    elif key > items[mid]:
        print("Checking item in the right")
        return binary_search(items, mid+1, right, key)


i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20]

print(binary_search(i, 0, len(i)-1, 200))
