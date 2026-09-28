sec=int(input("Enter number in sec"))
if sec>1 or sec<86400:
    hour=sec//3600
    min1=sec%3600
    min2=min1//60
    s=sec%60
    print(hour,":",min2,":",s)