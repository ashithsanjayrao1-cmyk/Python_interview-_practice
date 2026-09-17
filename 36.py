def find_missing_number(nums):
    n = len(nums)

    exp_sum = n*(n+1) //2

    actual_sum = sum(nums)

    return exp_sum - actual_sum

print(find_missing_number([3,0,1]))