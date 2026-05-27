Weight=float(input("Enter your weight in kg"))
Height=float(input("Enter your height in m"))
BMI=Weight/ (Height/100)**2
print ("Your BMI is",BMI)
if BMI<=18.5:
    print ("You are underweight")
elif BMI>18.5 and BMI<=24.9:    
    print ("You are normal weight")
elif BMI>24.9 and BMI<=34.9:
    print ("You are overweight")  
else:  
    print ("You are extremely overweight")        