def ex10(sentence):
    words = sentence.split()
    largest = max(words, key=len)
    print(largest, len(largest))


ex10(input())