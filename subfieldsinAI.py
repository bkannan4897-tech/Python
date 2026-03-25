class subfieldsinAI:
        def subfields():
            subfields=[
                "Machine Learning",
                "Neural Networks",
                "Vision",
                "Robotics",
                "Speech Processing",
                "Natural Language Processing"
            ]
            print("Sub-fields in AI are:")
            for subfield in subfields:
                 print(subfield)

        def OddEven():
            num=int(input("Enter the Number: "))
            if((num%2)==1):
                print("is Odd Number")
                message="Odd Number"
            else:
                print(num,"is Even Number")
                message="Even Number"
            
                          
        def Eligible():
            Age=int(input("Enter the Age:"))
            
            if(Age<21):
                print("Your Gender:Male")
                print("Your Age:20")
                print("NOT ELIGIBLE")
                message="NOT ELIGIBLE"
            
            elif(Age>18):
                print("Your Gender:Female")
                print("Your Age:18")
                print("ELIGIBLE")
                message="ELIGIBLE"
        
            else:
                print("Not Matured")
                message ="NOT MATURED"
            
              


class FindPercent:
        def percentage():
            subject1 = 98
            subject2 = 87
            subject3 = 95
            subject4 = 95
            subject5 = 93
            
            total = subject1 + subject2 + subject3 + subject4 + subject5
            percentage = (total / 500) * 100
            
            print(f"Subject1= {subject1}")
            print(f"Subject2= {subject2}")
            print(f"Subject3= {subject3}")
            print(f"Subject4= {subject4}")
            print(f"Subject5= {subject5}")
            print(f"Total :  {total}")
            print(f"Percentage :  {percentage}")
    

                                                                                                                                                                                               
class Triangle:
        def Triangle():
            Height=int(input("Height:"))
            Breadth=int(input("Breadth:"))
            print("Area formula: (Height*Breadth)/2")
            area=(Height*Breadth)/2
            print("Area of triangle: ", area)
    
            Height1=int(input("Height1:"))
            Height2=int(input("Height2:"))
            Breadth2=int(input("Breadth:"))
            print("Perimeter formula: Height1+Height2+Breadth")
            Perimeter=Height1+Height2+Breadth2
            print("Perimeter of Triangle: ", Perimeter)
            
            
         
                          
                
                            