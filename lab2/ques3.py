h=float(input("Enter Height"))
w=float(input("Enter Weight"))
BMI=(w/h**2)
if BMI<=18.5:
    print("Underweight")
elif BMI>18 and BMI<=25:
    print("Normal Weight")
elif BMI>25 and BMI<=30:
    print("Slightly Overweight")
elif BMI>30 and BMI<=35:
    print("Obese")
else:
    print("Clinically Obese")

