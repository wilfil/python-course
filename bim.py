#!/usr/bin/env python3.9

# BMI = (weight in kg / height in meters squared)
# Imperial version: BMI BMI *703

def gather_info():
    height = float(input("What's your height? (inches or meters) "))
    weight = float(input("What's your weight? (pounds or kilograms) "))
    system = input("Are you measurements in metric or imperial units? ").lower().strip()
    return (height, weight, system)

def calculate_bmi(weight, height, system='metric'):
    ## doc stream below
    """
    Return the Body Mass Index (BMI) for the given weight, height, and measurement system.
    """
    if system == 'metric':
        BMI = (weight / (height**2))
    else:
        BMI = 703 * (weight / (height**2))
    return BMI

while True:
    height, weight, system = gather_info()
    if system.startswith('i'):
        BMI = calculate_bmi(weight, height, system)
        print("\n"); 
        print(f"Your BMI is {BMI}")
        print("\n");
        break
    elif system.startswith('m'):
        BMI = calculate_bmi(weight, height)
        print(f"Your BMI is {BMI}")
        break
    else:
        print("Error: Unknown measurement system. Please choose between [I]mperial or [M]etric.")


