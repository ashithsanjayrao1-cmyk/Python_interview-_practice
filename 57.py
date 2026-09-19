def sum_of_digits(n):
    total = 0

    while n > 0:
        last_digit = n % 10
        total += last_digit
        n = n // 10

    return total

print(sum_of_digits(145))
