def is_prime(nums):
    if nums <= 1:
        return False

    for i in range(2,nums):
        if nums % i == 0:
            return False

    return True



print(is_prime(1))