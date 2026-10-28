s = input("Enter a string: ")

result = ""

for a in range(len(s)):
    if a % 2 == 0:
        result = result + s[i].upper()
    else:
        result = result + s[i].lower()

print(result)