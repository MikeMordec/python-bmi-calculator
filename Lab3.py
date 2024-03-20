'''
Created on Apr 12, 2022

@author: michaelmordec
'''

def main():
    weight=float(input("Enter your weight: "))
    height=float(input("Enter your height: "))
    bmi = weight * 703/pow(height,2)              
    print("BMI:", bmi)
    
    if(bmi<18.5):
        print("Underweight")
    elif(bmi>=18.5 and bmi<25):
        print("Optimal")
    else:
        print("Overweight")
main()