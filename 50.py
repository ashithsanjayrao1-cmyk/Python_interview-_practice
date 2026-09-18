def count_frequence(word):
    counts = {}

    for letter in word:
        if letter in counts:
            counts[letter] += 1

        else:
            counts[letter] = 1

    return counts

print(count_frequence("apaple"))