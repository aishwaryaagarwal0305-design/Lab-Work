str = input("Enter a string: ")

count = 0
n = len(str)

for i in range(n // 2):
    if str[i] != str[n - 1 - i]:
        count = count + 1

print("Changes needed:", count)