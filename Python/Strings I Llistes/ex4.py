word = input("Enter a word: ")
vowels = "aeiou"
count = 0

for char in word:
    if char in vowels:
        count += 1

print(count)