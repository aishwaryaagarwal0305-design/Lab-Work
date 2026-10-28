s = input("Enter a string: ")

max_count = 1
c = 1
max_char = s[0]

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        c = c + 1
    else:
        c = 1

    if c > max_count:
        max_count = c
        max_char = s[i]

print(max_char, max_count)