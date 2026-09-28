color=input("Enter colour")
mode=input("Enter mode")
if color=="blue":
    if mode=="Steady":
        print("Clear View")
    else:
        print("Clouds due")
else:
    if mode=="Steady":
        print("rain ahead")
    else:
        print("Snow")