def find_missing(arr,nums):

    expected_sum = nums * (nums + 1) // 2

    actual_sum = sum(arr)
    return expected_sum - actual_sum

print(find_missing([1,2,4,5],6))