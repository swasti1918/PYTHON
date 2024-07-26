marks1= int(input("Enter marks 1"))
marks2= int(input("Enter marks 2"))
marks3 = int(input("Enter marks 3"))

#  Check for total  percentage  
total_percentage = (marks1 + marks2 + marks3)/300

if(total_percentage>=40 and marks1>33,marks2>33,marks3>33):
    print("You are passed :", total_percentage)
    
else:
    print("you failed, try it next year:", total_percentage)