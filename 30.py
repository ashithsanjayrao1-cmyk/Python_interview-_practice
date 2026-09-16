nums = [1, 2, 3, 4, 5, 6,8]
even_squares = []

for x in nums:
    if x % 2 == 0:
        even_squares.append(x ** 2)
        #print(x)
        print(even_squares)


even_squares = [x**2 for x in nums if x % 2 == 0]

print(even_squares)