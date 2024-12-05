word = input("Enter a word: ")
mid = len(word) // 2
palindrome = False
if word[:mid] == word[-1:-mid-1:-1]:
    palindrome = True
print(palindrome)
