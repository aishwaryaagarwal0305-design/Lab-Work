c=int(input("costs of a company"))
r=int(input("revenue of a company"))
if c==r:
    print("Break Even")
else:
    if c>r:
        print("loss")
    else:
        print("Profit")
        