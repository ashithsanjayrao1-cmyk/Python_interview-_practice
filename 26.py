text = "hello"

nums = [1,2,3]

print(text[::-1])

print(nums[::-1])

nums.reverse()
print(nums)


word = "racecar"

if word == word[::-1]:
    print("It is a palindrome!!")


num = 12345

reversed_num = int(str(num)[::-1])
print(reversed_num)

logs = ["error_1", "error_2", "error_3", "error_4", "error_5"]

recent_logs = logs[-3:]
print(recent_logs)

every_other = logs[::2]
print(every_other)