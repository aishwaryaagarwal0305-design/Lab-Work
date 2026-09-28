pounds=float(input("enter number of pounds of apples:"))
cash=float(input("Enter amount of cash gain"))
total=pounds*0.25
change=cash-total
print("change=",change)
if cash<total:
    print("You own",total-cash)

