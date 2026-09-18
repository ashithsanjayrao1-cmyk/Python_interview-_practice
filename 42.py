str = 'test'

unique = []

for char in str:
    if str.count(char) == 1 and char not in unique:
        unique.append(char)

print(unique)