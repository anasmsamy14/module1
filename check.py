data = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

print(data)

word = input("Enter word: ")

print(data.get(word, 0))