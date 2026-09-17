def anagram(a,b):
    if len(a) != len(b):
        return False

    return sorted(a) == sorted(b)

print(anagram("listen","silent"))
print(anagram("hello","world"))