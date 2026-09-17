def remove_duplicates(nums):
    if not nums:
        return 0

    unique_index  = 0

    for i in range(1,len(nums)):

        if nums[i] != nums[unique_index]:
            unique_index += 1

            nums[unique_index] = nums[i]

    return unique_index + 1

my_array = [1,2,3,3,3,4,5,9,8,9]

print(remove_duplicates(my_array))