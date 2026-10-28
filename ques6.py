n = int(input("Enter how many terms: "))

a, b = 1, 1   
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b