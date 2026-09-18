def find_max_min(arr):
    highest = arr[0]
    lowest = arr[0]


    for num in arr:
        if num > highest:
            highest = num

        elif num < lowest:
            lowest = num

    return highest,lowest

print(find_max_min([5,2,9,1,7,0]))