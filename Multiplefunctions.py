class Multiplefunctions():
    def oddEven():
        num=int(input("Enter the Number:"))
        if((num%2)==1):
            print("Odd Number")
            message="Odd Number"
        else:
            print("Even Number")
            message="Even Number"
        return message    
        
    
    def BMI():
        BMI=float(input("Enter the BMI Index:"))
        if (BMI<18.5):
            print("Underweighted")
            message="underweighted"
        elif (BMI<24.9):
            print("Normal")
            message="Normal"
        elif(BMI<29.9):
            print("Overweight")
            message="Overweight"
        else:
            print("Very Overweighted")
            message="Very Overweighted"
        return message
        