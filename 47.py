def factoiral(nums):
    total = 1
    for i in range(1,nums+1):
        total = total * i

    return total

print(factoiral(1))