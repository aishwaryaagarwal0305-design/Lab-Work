s = input("Enter a string: ")

vowels = consonants = digits = spaces = others = 0


for r in s:
    if r in "aeiou" and "AEIOU":
        vowels = vowels + 1
    elif r.isalpha():
        consonants = consonants + 1
    elif r.isdigit():
        digits = digits + 1
    elif r == " ":
        spaces = spaces + 1
    else:
        others = others + 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Others:", others)