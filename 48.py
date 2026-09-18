def fibonnaci(nums):
    a = 0 
    b = 1

    for i in range(nums):
        print(a)
        temp = a+b
        a = b
        b = temp

print(fibonnaci(4))