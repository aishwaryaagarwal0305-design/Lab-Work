sent = input("Enter a sentence: ")

words = sent.split()

for word in words:
    print(len(word), end=" ")