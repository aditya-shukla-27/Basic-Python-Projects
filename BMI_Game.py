Weight = float(input("Please enter your weight in Kg \n"))
Height = float(input("Please enter your height in Cm \n"))
Height = Height/100
BMI = Weight/(Height**2)
print(f'So here is your BMI value {BMI}. Based on that ')
if BMI > 0:
    if BMI < 16:
        print("You are severely underweight")
    elif BMI < 18.5:
        print("You are underweight")
    elif BMI <=25:
        print("You are healthy")
    elif BMI <= 30:
        print("You are overweight")
    else:
        print("You are severely overweight")

else:
    print("Enter valid details")