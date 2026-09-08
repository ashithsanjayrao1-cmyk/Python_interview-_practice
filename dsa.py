# text = input("Enter the string:")

# vowels = "aeiouAEIOU"
# v_count = 0
# c_count = 0

# for char in text:
#     if char.isalpha():
#         if char in vowels:
#             v_count += 1
#         else:
#             c_count += 1

# print("vowels",v_count)
# print("Consonants",c_count)


# text = input("Enter a string: ")
# reversed_text = text[:: -1]
# if text == reversed_text:
#     print("The entered string is palindrome")

# else:
#     print("It is not a palindrome")


# arr = list(map(int,input("Enter  numbers separated by space: ").split()))

# unique_arr = list(set(arr))

# unique_arr.sort()

# if len(unique_arr) < 2:
#     print("No  second larget exist")
# else:
#     print("Second Largest:",unique_arr[-2])

n = int(input("Enter N: "))

arr = list(map(int,input("Enter the array elements; ").split()))

expected_sum = (n*(n+1))//2

actua_sum = sum(arr)

missing_number = expected_sum - actua_sum
print("Missing Number:", missing_number)